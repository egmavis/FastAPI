[![Python application test with Github Actions](https://github.com/egmavis/FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/egmavis/FastAPI/actions/workflows/main.yml)

# FastAPI
This is a repo demonstrating continuous delivery of a Fast API on AWS (IDS 706 Project 2).  
  
This project demonstrates how to use introductory-level Fast API functions with an already completed API. I modify it slightly by posting an image on the root page, and utilize string formatting to include a variety of user input.  
  


### Step 1: Create a new Repository and C9 environment
- create a new respository in GitHub
- create a new C9 environment
- open the IDE
- generate new SSH keys
- clone the repository into the environment
- navigate into the repository and create python virtual environment
- create project scaffolding

### Step 2: Find an API
I am using an already completed FastAPI to work off of, which can be found [here](https://github.com/tapaswenipathak/Horoscope-API). It is a horoscope generator that requires a time-frame and zodiac sign as URL inputs.

### Step 3: Write Fast API
See the main.py file.

### Step 4: Write Testing File
See the test_main.py file

#### *configure inbound rules*
- ppen up AWS EC2 
- go to security groups and select your working environment
- edit your inbound rules and select "add rule"
- custom TCP: port range = 8080 and source = 0.0.0.0/0

### Step 5: Deploy Github Actions for Automated Testing
- set up a new workflow yourself
- paste in stored text to populate the main.yml file
- start commit
- fix any errors until build has passed

### Step 6: Connect to AWS App Runner
- create a new service from source code repository
- connect to Github and specify which repoository to link
- select python3 runtime
- build command: "pip install -r requirements.txt"
- start command: "python main.py"
- create service name, then create and deploy

#### *Extra Step 7*
Future changes to integrate:
  - add custom features such as color, font, images
  - integrate into command line tool that can interact with user and prompt user for input

## Sources
- tapaswenipathak/Horoscope-API [link](https://github.com/tapaswenipathak/Horoscope-API)
- How to insert image file in FastAPI [link](https://www.youtube.com/watch?v=vpTAqnAbowo)
- Noah Gift's FastAPI Code [link](https://github.com/noahgift/fastapi-duke/blob/main/main.py)
- Sydney Donati Leach's FastAPI instructions [link](https://github.com/sdonatileach/fastapi/blob/main/README.md)
