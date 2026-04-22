from processor_regex import classify_with_regex
from processor_llm import classify_with_llm
from processor_bert import classify_with_bert

def classify(logs):
    labels=[]
    for source, log_msg in logs:
       label=classify_log(source, log_msg)
       labels.append((source,log_msg,label))
    return labels

def classify_log(source,log):
    if(source == "LegacyCRM"):
        label = classify_with_llm(log)
    else:
        label = classify_with_regex(log)
        if label is None:
            label = classify_with_bert(log)
        return label


if __name__ == "__main__":
    logs=[("ModernCRM", "User User685 logged out..." ),
    ("BillingSystem", "User User12 logged in." ),
    ("AnalyticsEngine", "File uploaded successfully by user sadd"),
    ("ModernHR", "Account with ID chakka created by manga"),
    ("LegacyCRM", "User User685 logged out..."),
    ("LegacyCRM", "Workflow failed at step 23:hello"),
    ("LegacyCRM", "System updated to version 1.0.0")] 

    classified_logs=classify(logs)
    print(classified_logs)

    # for log in logs:
    #     class