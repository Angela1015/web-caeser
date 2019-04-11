from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
from caesar import rotate_string

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16pxsans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;

            }}
        </style>
     
    </head>
    <body>
      <!-- create your form here -->
      <form method = "POST">
        <label for "rotate_number">Rotate by:</label>
        <input id = "rotate_number" type = "text" name = "rot" value ="0"/>
<<<<<<< HEAD
        <textarea name = "text">{0}</textarea>
=======
        <textarea name = "text">{}</textarea>
>>>>>>> f970c36740cef6953e17f55caf1170eaf515a1a2
        <input type ="submit" value = "Submit Query"/>
      </form>
    </body>
  
  
  
  
</html>"""
@app.route("/")
def index():
    return form.format("")
@app.route("/" , methods = ["POST"])
def encrypt():
    text = request.form["text"]
    rot =  int(request.form["rot"])
    for char in text:
        encrypted_text = rotate_string(text,rot)
        
    return form.format(encrypted_text)


app.run()