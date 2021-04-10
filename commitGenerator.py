# Change NUM_OF_COMMITS to whatever number of commits you want !

#!/usr/bin/env python3 

import random
import os
import threading

NUM_OF_COMMITS = 100

def commitCreation():

    file = open("randomIsBetter.txt", "a")

    file.write(str(random.randint(1, 100000)) + '\n')

    os.system("git add *")

    os.system(f'git commit -m "{num}"')

    os.system("git push origin main")
    file.close()

def main():

    threads = []

    for i in range(NUM_OF_COMMITS):
        x = threading.Thread(target=commitCreation)
        x.daemon = True
        threads.append(x)

    for i in range(NUM_OF_COMMITS):
        threads[i].start()
        threads[i].join()
    
if __name__ == "__main__":
    main()
