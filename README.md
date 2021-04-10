# Github Commit Boost
A git autocommit script that can boost up your contributions

## Requirements:
- Linux
- Python3
- SSH keys for pushing without prompting the username and password
> https://gist.github.com/xirixiz/b6b0c6f4917ce17a90e00f9b60566278

## How it works:

The script will simply create a .txt file and append random numbers to it, a git commit and push will occur each time

## Istructions:

1. Clone this repo
```
git clone https://github.com/fiordiconio/githubCommitBoost
```

2. Copy commitGenerator.py inside the repository you want commit for

3. Modifiy constant value inside of commitGenerator.py
```
NUM_OF_COMMITS = # whatever number of commits you want
```

4. Run the script
```
python3 main.py
```

5. Enjoy

## NOTE

* This has been done just for educational purpose, lots of commits does not necessary make you a good programmer

* I am not using it, all of my commits are legit

* Do not abuse this

* Keep in mind that the file .txt that gets modified each time will grow up in size, clear it after some time to avoid filling up Github servers

