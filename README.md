#  RPG Master Branch
Description
AnimeChatBot is an interactive application that allows users to engage with their favorite anime characters through prompts. By utilizing a command-line tool, this chatbot generates responses that roleplay as various anime characters, providing a fun and immersive experience. Users can input their queries, and the bot will respond with character-appropriate replies, making it a delightful tool for anime fans.


## Screenshots
![image](https://github.com/user-attachments/assets/c1947898-0ed8-4a9d-b5b0-66ec86412691)

Screenshots can be added here to showcase the application interface and functionality.




##  Futures perks
image generation with https://github.com/lllyasviel/Fooocus:
'''
   1  git clone https://github.com/lllyasviel/Fooocus.git
    2  cd Fooocus/
    3  python entry_with_update.py --share
    4  pip install -r requirements_versions.txt
    5  python entry_with_update.py --share
    6  pip install packaging
    7  pip install pygit2
    8  python entry_with_update.py --share
    9  pip3 install packaging
   10  python --version
   11  which python  # On Unix-like systems
   12  where python  # On Windows
   13  pip list
   14  savio.nery@AN0100148066254 MINGW64 ~/Fooocus
   15  $ python --version
   16  which python  # On Unix-like systems
   17  where python  # On Windows
   18  Python 3.11.7
   19  /usr/bin/python
   20  C:\Program Files\GNU Octave\Octave-9.2.0\usr\bin\python.exe
   21  C:\Program Files\Python312\python.exe
   22  C:\Users\savio.nery\AppData\Local\Microsoft\WindowsApps\python.exe
   23  savio.nery@AN0100148066254 MINGW64 ~/Fooocus
   24  $ pip list
   25  Package
   26  # For venv
   27  source path_to_venv/bin/activate  # On Unix-like systems
   28  path_to_venv\Scripts\activate  # On Windows
   29  # For conda
   30  conda activate your_env_name
   31  python entry_with_update.py --share
   32  which python
   33  "C:\Program Files\Python312\python.exe" -m pip install packaging
   34  "C:\Program Files\Python312\python.exe" -m pip list
   35  "C:\Program Files\Python312\python.exe" entry_with_update.py --share

'''

## Project Structure

.
├── filteressay.sh         # Shell script for processing queries.
├── healthbotessay.txt     # Sample output or reference for health-related queries.
├── main.py                # Main application file that runs the Flask server.
└── templates              # Directory containing HTML templates.
    └── home.html          # HTML template for the home page of the application.
## How to Use
Start the Application: Run the Flask app to initiate the server.
Input Queries: Access the API endpoint to input your queries and receive responses.
Engage with Characters: Use various prompts to interact with different anime characters.

## Installation
For Windows

#powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install https://raw.githubusercontent.com/aandrew-me/tgpt/main/tgpt.json   
    
    ## Clone the repository and navigate to the project folder
    git clone --branch windows-branch https://github.com/nizpew/anime-chatgpt-bot.git
    cd anime-chatgpt-bot python3 -m venv venv ; source venv/bin/activate ; pip install flask ; python main.py

    For Linux
  
    
    
    ## Clone the repository and install the required dependencies
    git clone https://github.com/nizpew/anime-chatgpt-bot.git
    cd anime-chatgpt-bot
    pip install -r requirements.txt

## External Dependencies
[tgpt](https://github.com/aandrew-me/tgpt)


## Run the application
python3 main.py
Run the Application
bash

## Start the Flask application
python main.py
