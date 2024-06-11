from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    numero = random.randint(1, 10)
    if numero == 1:
        m =  "{
                  "nombre": "Quinoa con Verduras Asadas",
                  "ingredientes": [
                    "1 taza de quinoa",
                    "2 tazas de agua",
                    "1 pimiento rojo",
                    "1 pimiento amarillo",
                    "1 calabacín",
                    "1 berenjena",
                    "2 cucharadas de aceite de oliva",
                    "1 diente de ajo",
                    "1 cucharadita de comino",
                    "1 cucharadita de pimentón dulce",
                    "Sal al gusto",
                    "Pimienta al gusto"
                  ],
                  "preparacion": [
                    "1. Enjuaga la quinoa bajo agua fría hasta que el agua salga clara.",
                    "2. En una cacerola, lleva las 2 tazas de agua a ebullición. Agrega la quinoa, reduce el fuego y cocina a fuego lento durante 15-20 minutos, o hasta que la quinoa haya absorbido toda el agua. Retira del fuego y deja reposar tapado por 5 minutos.",
                    "3. Precalienta el horno a 200°C (400°F).",
                    "4. Lava y corta los pimientos, el calabacín y la berenjena en trozos medianos.",
                    "5. Coloca las verduras en una bandeja para hornear. Añade el aceite de oliva, el ajo picado, el comino, el pimentón dulce, la sal y la pimienta. Mezcla bien para que las verduras queden bien cubiertas con los condimentos.",
                    "6. Asa las verduras en el horno durante 20-25 minutos, o hasta que estén tiernas y ligeramente doradas.",
                    "7. Mezcla la quinoa cocida con las verduras asadas y sirve caliente."
                  ],
                  "informacion_nutricional": {
                    "porciones": 4,
                    "calorias_por_porcion": 250,
                    "grasas_totales": "9g",
                    "grasas_saturadas": "1g",
                    "colesterol": "0mg",
                    "sodio": "150mg",
                    "carbohidratos_totales": "35g",
                    "fibra_dietetica": "7g",
                    "azucares": "5g",
                    "proteinas": "7g",
                    "vitamina_A": "30% VD",
                    "vitamina_C": "100% VD",
                    "calcio": "6% VD",
                    "hierro": "15% VD"
                  }
                }"
    if numero == 2:
        m = "El número es cero"
    if numero == 3:
        m = 'Hello World!2'
    if numero == 4:
        m = 'Hello World!2'
    if numero == 5:
        m = 'Hello World!2'
    if numero == 6:
        m = 'Hello World!2'
    if numero == 7:
        m = 'Hello World!2'
    if numero == 8:
        m = 'Hello World!2'
    if numero == 9:
        m = 'Hello World!2'
    if numero == 10:
        m = 'Hello World!2'
    return m
    
if __name__ == '__main__':
    app.run()
