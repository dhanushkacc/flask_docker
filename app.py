from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if not operation or not num1 or not num2:
        return '''
       
         the following format to calculate:
        /?operation=<operation>&num1=<number1>&num2=<number2>
        
        Supported operations: add, subtract, multiply, divide
        '''

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Invalid numbers provided"}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)