from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/external', methods=['GET'])
def get_data_from_external_api():
    api_key = 'your_api_key'
    url = 'https://external-api.com/data'
    
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
