from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16pxsans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;

            }
        </style>
     
    </head>
    <body>
      <!-- create your form here -->
      <form method = "POST">
        <label for "rotate_number">Rotate by:</label>
        <input id = "rotate_number" type = "text" name = "rot" value ="0"/>
        <textarea name = "text"></textarea>
        <input type ="submit" value = "Submit Query"/>
      </form>
    </body>
  
  
  
  
</html>"""
@app.route("/")
def index():
    return form

app.run()