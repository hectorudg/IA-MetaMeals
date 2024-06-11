from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    numero = random.randint(1, 10)
    if numero > 0:
        m =  "El número es positivo"
    if numero == 1:
        m = "El número es cero"
    if numero == 2:
        m = 'Hello World!2'
    return m
    
if __name__ == '__main__':
    app.run()
