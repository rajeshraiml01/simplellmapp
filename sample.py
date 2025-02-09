from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    print("This is a sample script")
    print("Current working directory: ", os.getcwd())
    print("List of files in the current directory: ", os.listdir())
    print(os.getenv('OPENAI_API_KEY'))