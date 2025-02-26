#  AnimeChatBot: Engage with Your Favorite Anime Characters
Description
AnimeChatBot is an interactive application that allows users to engage with their favorite anime characters through prompts. By utilizing a command-line tool, this chatbot generates responses that roleplay as various anime characters, providing a fun and immersive experience. Users can input their queries, and the bot will respond with character-appropriate replies, making it a delightful tool for anime fans.


## Screenshots
![image](https://github.com/user-attachments/assets/c1947898-0ed8-4a9d-b5b0-66ec86412691)

Screenshots can be added here to showcase the application interface and functionality.




##  Features
Interactive Roleplaying
Character Roleplay: Generate responses as if they were coming from an anime shoujo character based on user prompts.
Dynamic Queries: Input any query to receive a tailored response that reflects the character's personality.
Command-Line Integration
Shell Command Execution: Utilize shell commands to process queries and fetch responses efficiently.
Error Handling: Robust error handling ensures that users receive informative messages in case of issues.

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
    see the windwos branch of the repo
    
For Linux
    ## Clone the repository and install the required dependencies
    git clone https://github.com/nizpew/anime-chatgpt-bot.git
    cd anime-chatgpt-bot
    python3 -m venv venv ; source venv/bin/activate ; pip install flask
    python main.py
    
## External Dependencies
[tgpt](https://github.com/aandrew-me/tgpt)


## Run the application
python3 main.py
Run the Application
bash

## Start the Flask application
python main.py
