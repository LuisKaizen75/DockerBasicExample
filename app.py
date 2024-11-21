from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the main page
form_html = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>HBD App</title>
  </head>
  <body>
    <h1>Enter your name</h1>
    <form action="/hbd" method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
"""

# HTML template for the response
response_html = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>HBD App</title>
  </head>
  <body>
    <h1>{{ message }}</h1>
    <a href="/">Go back</a>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/hbd', methods=['GET', 'POST'])
def salute():
    if request.method == 'POST':
        name = request.form.get('name')
    else:
        name = request.args.get('name')
    
    if name:
        message = f"Happy Birthday, {name}!"
    else:
        message = "Happy Birthday, stranger!"
    
    return render_template_string(response_html, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)