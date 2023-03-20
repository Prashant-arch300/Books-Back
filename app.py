#python3 -m venv env
#source env/bin/activate
#pip install Flask
#pip install pandas


from flask import Flask, request, jsonify, abort
import pandas as pd

app = Flask(__name__)

# Read data from CSV file
books_df = pd.read_csv('books.csv')

# Database of user credentials
users = [
    {
        'email': 'test@example.com',
        'password': 'password'
    }
]

# Login API endpoint
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = next((user for user in users if user['email'] == email), None)
    if not user or user['password'] != password:
        abort(401)
    return jsonify({'message': 'Logged in successfully'})

# Books API endpoint
@app.route('/books', methods=['GET'])
def books():
    rows = request.args.get('rows')
    if rows:
        try:
            rows = int(rows)
        except ValueError:
            abort(400)
        data = books_df.head(rows).to_dict('records')
    else:
        data = books_df.to_dict('records')
    return jsonify({'books': data})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
