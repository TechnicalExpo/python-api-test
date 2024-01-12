from flask import Flask, jsonify
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def autocomplete(query):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    response = requests.get(url)
    suggestions = response. json()[1]
    
    return jsonify(suggestions)

# if __name__ == '__main__':
#     app.run(debug=True)
serve(app, host='0.0.0.0', port=8080)