from flask import Flask, jsonify
from faker import Faker
import random

fake = Faker()

# Generar 500 registros ficticios
data = []
for _ in range(500):
    record = {
        'name': fake.name(),
        'address': fake.address(),
        'phone_number': fake.phone_number(),
        'email': fake.email(),
        'age': random.randint(18, 65),
    }
    data.append(record)

# Puedes imprimir los registros generados para verificarlos
for record in data:
    print(record)

app = Flask(__name__) 


@app.route('/fake-data', methods=['GET'])
def api():
    return jsonify(messaje=data)

app.run(debug=True)
