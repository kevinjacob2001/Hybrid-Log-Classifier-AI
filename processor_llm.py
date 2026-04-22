from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

groq_client = Groq(api_key=groq_api_key)

def classify_with_llm(log_message):
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": log_message}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(classify_with_llm('Hello bro, chill yaa'))