from flask import Flask, render_template_string, request
import re

app = Flask(__name__)

def check_password_policy(password):
    if len(password) >= 16:
        upper = len(re.findall(r'[A-Z]', password))
        lower = len(re.findall(r'[a-z]', password))
        digits = len(re.findall(r'\d', password))
        special = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        if upper >= 4 and lower >= 4 and digits >= 4 and special >= 4:
            return "Password is Too Strong."
    
    if len(password) < 9:
        return "Password must be at least 9 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    return "Password is Strong."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        password = request.form['password']
        result = check_password_policy(password)
    
    return render_template_string('''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Password Validator</title>
    <style>
      body {
        font-family: 'Arial', sans-serif;
        background-image: url('/static/ABC2.jpg'); /* Corrected syntax */
        background-size: cover; /* Ensure the image covers the entire background */
        background-position: center; /* Center the image */
        color: #333;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      .container {
        background-color: #F1E5D1;
        opacity: 89%;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        width: 100%;
      }
      
      h1 {
        color: #E90074;
        opacity: 100%;
        font-weight: 600;
        margin-bottom: 20px;
        text-align: center;
      }
      p {
        font-size: 16px;
        line-height: 1.6;
      }
      ul {
        margin-top: 10px;
        padding-left: 20px;
      }
      ul li {
        margin-bottom: 8px;
        font-size: 14px;
      }
      form {
        margin-top: 20px;
      }
      label {
        display: block;
        font-weight: 600;
        margin-bottom: 5px;
      }
      input[type="password"] {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
        text-align: center;
        font-size: 14px;
      }
      button {
        width: 50%;
        padding: 10px;
        margin-left: 25%;
        background-color: #E90074;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;
        transition: background-color 0.3s ease;
      }
      button:hover {
        background-color: #45a049;
      }
      .result {
        margin-top: 20px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
      }
      .error {
        color: red;
      }
      .success {
        color: green;
      }
      .too-strong {
        color: green;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1><b>Welcome to the Password Validator!</b></h1>
      <p><b>Please enter a password that meets the following requirements:</b></p>
      <p><b>Password policies should be maintained*</b></p>
      <ul>
        <li>At least 9 characters long</li>
        <li>At least one uppercase letter</li>
        <li>At least one lowercase letter</li>
        <li>At least one digit</li>
        <li>At least one special character (!@#$%^&*(),.?":{}|<>)</li>
        <li>For "Too Strong" passwords: At least 16 characters with at least 4 uppercase, 4 lowercase, 4 digits, and 4 special characters</li>
      </ul>
      <form method="post">
        <div>
          <label for="password">Enter your password:</label>
          <input type="password" id="password" name="password" required>
        </div>
        <div>
          <button type="submit">Check It</button>
        </div>
      </form>
      <p class="result {{ 'error' if 'must' in result else 'success' if 'Strong' in result else 'too-strong' }}">{{ result }}</p>
    </div>
  </body>
</html>                               
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
