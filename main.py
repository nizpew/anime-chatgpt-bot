from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/api', methods=['GET'])
def api():
    query = request.args.get('query', '')

    ##prompt = f"I will give you a prompt. reponse in less than 50 words, Roleplay as an anime shoujo (anime genre, search its meaning) character. search their quotes if needed. now here is the prompt - {query}"
    ##prompt = f"I will give you a prompt. reponse in less than 50 words, and act like medical, health chatbot. search about how to cure my issue. now here is the prompt - {query}"



    #scrapping between ""
    command = f'~/anime-chatgpt-bot/filteressay.sh "{query}"'







    try:
        output = subprocess.check_output(command, shell=True, text=True)
        result = {'query': query, 'output': output.strip()}
        return jsonify(result)
    except subprocess.CalledProcessError as e:
        error_message = f"Error running command 'tgpt': {e}"
        return jsonify({'error': error_message})

if __name__=="__main__":
	app.run(debug=True)
