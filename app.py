from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    lista1 = request.form.get("lista")
    lista1 = lista1.split()
    lista2 = random.shuffle(lista1)
    print("la lista final es: ", lista1, "El tipo es:    ", type(lista1))
    # Verificar paridad
    listapar = len(lista1)
    if listapar % 2 != 0:
        print("es par:",listapar)
        return render_template('index.html', listapar=listapar)
    else:
        equipoblanco = lista1[0:len(lista1) // 2]
        equipooscuro = lista1[len(lista1) // 2:len(lista1)]
        print(equipoblanco, equipooscuro)
        return render_template('index.html', lista1=lista1, equipoblanco=equipoblanco, equipooscuro=equipooscuro)


if __name__ == '__main__':
    app.run(port = 5000, debug=True)