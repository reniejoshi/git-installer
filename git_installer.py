import os
import requests
import time
from tqdm import tqdm

os.system("echo Hello, world!")

def main():
    response = requests.get("https://dummyjson.com/quotes")
    data = response.json()
    quote = data["quotes"][0]
    print('\"' + quote["quote"] + '\"')
    print(quote["author"])

    for i in tqdm(range(10000)):
        time.sleep(0.0001)

main()