from pathlib import Path

import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()

OUTPUT_DIR = Path("resources")
OUTPUT_FILE = OUTPUT_DIR / "output.csv"
REQUIRED_COLUMNS = {"source", "log_message"}


@app.post("/classify")
async def classify_logs(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    try:
        dataframe = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Unable to read the uploaded CSV file.")
    finally:
        file.file.close()

    missing_columns = REQUIRED_COLUMNS - set(dataframe.columns)
    if missing_columns:
        raise HTTPException(
            status_code=400,
            detail=f"CSV is missing required columns: {', '.join(sorted(missing_columns))}"
        )

    try:
        records = list(zip(dataframe["source"], dataframe["log_message"]))

        #perform classification
        predicted_labels = classify(records)
        dataframe["target_label"] = predicted_labels

        #save the output to a csv file
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        dataframe.to_csv(OUTPUT_FILE, index=False)

        return FileResponse(
            path=str(OUTPUT_FILE),
            media_type="text/csv",
            filename="classified_logs.csv"
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Classification failed: {str(exc)}"
        )