from processor_regex import classify_with_regex




if __name__ == "__main__":
    logs=['User User685 logged out...','File uploaded successfully by user sadd','Account with ID chakka created by manga']
    for log in logs:
        print(f"Log: {log}")
        print(f"Classified as: {classify_with_regex(log)}")
        print("-"*50)