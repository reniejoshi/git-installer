import os
import time
from tqdm import tqdm

os.system("echo Hello, world!")

def main():
    for i in tqdm(range(10000)):
        time.sleep(0.0001)

main()