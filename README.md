# check_branch_protection
an utility check Github repos branch protection status

## Dependencies
### platform
Python3
### packages
* pyGithub
* click

## Install
```shell script
git clone https://github.com/dawncold/check_branch_protection
cd check_branch_protection
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
```

## Usage
```shell script
Usage: main.py [OPTIONS]

Options:
  --token TEXT        personal access token with repo privilege  [required]
  --repo-prefix TEXT  filter repos prefix  [required]
  --branch TEXT       branch to check  [default: master]
  --setup             setup basic branch protection (disable force push)
  --delete            delete branch protection
  --help              Show this message and exit.
```

## List not protected repos
```shell script
python3 main.py --token TOKEN --repo-prefix PREFIX
```

## Setup basic branch protection
```shell script
python3 main.py --token TOKEN --repo-prefix PREFIX --setup
```

## Delete branch protection
```shell script
python3 main.py --token TOKEN --repo-prefix PREFIX --delete
```