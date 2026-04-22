from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

groq_client = Groq(api_key=groq_api_key)





def classify_with_llm(log_message):

    prompt=f'''Classify the following log message into one of the following categories name: 
        (1) Workflow Error , (2) Deprecation Warning,
        If you cant figure out the category, return "Unclassified".
        Ony return the category, no other text or explanation.
        Log message: {log_message}'''

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(classify_with_llm('Workflow failed at step 23:hello'))