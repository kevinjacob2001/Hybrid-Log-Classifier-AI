from processor_regex import classify_with_regex


def classify(logs):
    labels=[]
    for source, log_msg in logs:
       label=classify_log(source, log_msg)
       labels.append((source,log_msg,label))
    return labels

def classify_log(log):
    if(source=="LegacyCRM"):
        pass #LLM
    else:
        label= classify_with_regex(log)
        if label is None:
            pass #BERT
        return label


if __name__ == "__main__":
    logs=[("ModernCRM", "User User685 logged out..." ),
    ("AnalyticsEngine", "File uploaded successfully by user sadd"),
    ("ModernHR", "Account with ID chakka created by manga"),
    ("LegacyCRM", "User User685 logged out...")] 

    classified_logs=classify(logs)

    # for log in logs:
    #     class