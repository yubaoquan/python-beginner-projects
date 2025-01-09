from dotenv import load_dotenv
import os

load_dotenv()


def showProperty(key):
    value = os.getenv(key)
    print(f'{key} is {value} ({len(value)})')


for key in ['name', 'age', 'gender']:
    showProperty(key)
