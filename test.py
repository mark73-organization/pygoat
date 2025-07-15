import os
import pickle
import flask

app = flask.Flask(__name__)

# --- Vulnerability 1: Command Injection ---
@app.route('/run')
def run_command():
    cmd = flask.request.args.get('cmd')
    os.system(cmd)  # Dangerous: unsanitized input used directly in shell command
    return f"Executed: {cmd}"

# --- Vulnerability 2: Insecure Deserialization ---
@app.route('/deserialize', methods=['POST'])
def deserialize_data():
    data = flask.request.data
    obj = pickle.loads(data)  # Dangerous: allows remote code execution
    return f"Deserialized: {obj}"

# --- Vulnerability 3: Hardcoded Secret ---
SECRET_KEY = "supersecretkey123"  # Dangerous: hardcoded secret key

if __name__ == '__main__':
    app.run(debug=True)
