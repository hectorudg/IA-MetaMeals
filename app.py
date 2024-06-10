from flask import Flask

app = Flask(__name__)

@app.route('/')
def case_example():
    switch = {
        1: "HelloW",
        2: "bye"
    }
    return switch.get(1, default_case)
    
if __name__ == '__main__':
    app.run()
