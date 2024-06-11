from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    numero = random.randint(1, 10)
    if numero > 0:
    return "El número es positivo":
    elif numero == 0:
    return "El número es cero"
    else:
    return 'Hello World!2'
    
if __name__ == '__main__':
    app.run()
