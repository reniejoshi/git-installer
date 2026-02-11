import os
import requests
import time
from tqdm import tqdm

os.system("echo Hello, world!")

def practiceMain():
    response = requests.get("https://dummyjson.com/quotes")
    data = response.json()
    quote = data["quotes"][0]
    print('\"' + quote["quote"] + '\"')
    print(quote["author"])

    for i in tqdm(range(10000)):
        time.sleep(0.0001)

def main():
    account_name = os.getlogin()
    download_location = f"C:\\Users\\{account_name}\\Downloads"

    response = requests.get('https://github.com/git-for-windows/git/releases/download/v2.53.0.windows.1/Git-2.53.0-64-bit.exe')
    filepath = f'{download_location}\\git.exe'
    print(filepath)

    chunk_size = 1024
    with open(filepath, "wb") as file:
        for data in response.iter_content(chunk_size):
            file.write(data)

main()