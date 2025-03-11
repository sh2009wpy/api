from flask import Flask, request, jsonify

app = Flask(__name__)

# 存储字符串的列表
strings = []

@app.route('/add', methods=['POST'])
def add_string():
    # 获取请求中的 JSON 数据
    data = request.get_json()
    if not data or 'string' not in data:
        return jsonify({'error': 'Missing string parameter'}), 400
    
    string = data['string']
    strings.append(string)
    return jsonify({'message': f'String "{string}" added successfully', 'count': len(strings)}), 201

@app.route('/strings', methods=['GET'])
def get_strings():
    return jsonify({'strings': strings, 'count': len(strings)}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
