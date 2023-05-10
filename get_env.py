import dotenv
import os

def print_env(body):
    try:
        dotenv.load_dotenv()
        dict = {}
        for field in body:
            dict[field] = os.getenv(field)
        return dict
    except Exception as e:
        print(f"Houve um erro inesperado: {e}")

if __name__ == "__main__":
    body = ["api_key"]
    print(print_env(body))

