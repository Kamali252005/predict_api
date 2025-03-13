from flask import Flask, request, jsonify

app = Flask(_name_)  # Corrected Flask instance

@app.route('/predict', methods=['GET'])
def predict():
    name = request.args.get('name')

    if not name:  # Correct condition
        return jsonify({'error': 'No name provided'}), 400
    
    return jsonify({'status': 'success', 'name': name})  # Correct response

if _name_ == '_main_':
    app.run(debug=True)  # Runs Flask server

