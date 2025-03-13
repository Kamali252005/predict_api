from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
name= request.args.get('name')

if name:
    return jsonify({'error': 'No file uploaded'}), 400

else:
    return jsonify({'status': 'success', 'filename': file.filename})
    if_name_==_main_':
        app.run(debug=True)
