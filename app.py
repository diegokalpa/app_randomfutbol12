from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')  # se crea inicialmente esta linea para conectar con inde.html
def home():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])  #Se agrega esto para traer por POST datos de algo de html, es una entrada
def procesar():
    lista1 = request.form.get("lista") #trae la lista desde el formulario web desde index.html
    lista1 = lista1.splitlines()            #se divide el string anterior por lineas ya que es un string
    lista2 = random.shuffle(lista1)    #se hace aleatoria la lista
    print("la lista final es: ", lista1, "El tipo es:    ", type(lista1))
    # Verificar paridad para comprobar que la lista ingresada es par si no muestra error
    listapar = len(lista1)
    if listapar % 2 != 0:
        print("es par:",listapar)
        return render_template('index.html', listapar=listapar)
    else:
        equipoblanco = lista1[0:len(lista1) // 2]   #se seleciiona el primer equipo desde la posicion 0 hasta la posicion de la mitad del tamaño de la lista
        equipooscuro = lista1[len(lista1) // 2:len(lista1)]
        print(equipoblanco, equipooscuro)
        return render_template('index.html', lista1=lista1, equipoblanco=equipoblanco, equipooscuro=equipooscuro)


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
    