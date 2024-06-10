from flask import Flask

app = Flask(__name__)

@app.route('/')
def case_example(value):
    def case_one():
        return "Caso 1: valor es 1"

    def case_two():
        return "Caso 2: valor es 2"

    def default_case():
        return "Caso por defecto: valor no reconocido"

    switch = {
        1: case_one,
        2: case_two
    }

    return switch.get(1, default_case)()
case_example(1)


if __name__ == '__main__':
    app.run()
