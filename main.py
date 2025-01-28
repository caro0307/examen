from faulthandler import cancel_dump_traceback_later

from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    #result = "hola, retorno un resultado"
    #print('asdfasdfadsf')
    return render_template('home.html')


@app.route('/calculo')
def calculo():
    return render_template('calculoCompra.html')


@app.route('/calcularcompra', methods=['GET', 'POST'])
def contadorNombres():
    if request.method == 'POST':
        nombre =  str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidad = float(request.form['cantidad'])
        saldoTotal = cantidad * 9000.0
        valor1 = 0
        valor2 = 0
        valor3 = 0

        if 18 <= edad <= 30:
            valor1 = saldoTotal * 15
            valor2 = round(valor1 / 100)
            valor3 = saldoTotal - valor2
            return render_template('calculoCompra.html', nombre=nombre, valor2=valor2, saldoTotal=saldoTotal, valor3=valor3)

        if edad > 30:
            valor1 = saldoTotal * 25
            valor2 = round(valor1 / 100)
            valor3 = saldoTotal - valor2
            return render_template('calculoCompra.html', nombre=nombre, valor2=valor2, saldoTotal=saldoTotal, valor3=valor3)

        return render_template('calculoCompra.html', nombre=nombre, valor2=valor2, saldoTotal=saldoTotal, valor3=valor3)
    return render_template('calculoCompra.html')




@app.route('/iniciosesion')
def inicioSesion():
    return render_template('inicioSesion.html')

@app.route('/validarinicio', methods=['GET', 'POST'])
def validarInicio():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        passw = str(request.form['pass'])

        if nombre == 'juan' and passw == 'admin':
            resultado = 'Bienvenido administrador juan'
            return render_template('inicioSesion.html', resultado=resultado)

        if nombre == 'pepe' and passw == 'user':
            resultado = 'Bienvenido usuario pepe'
            return render_template('inicioSesion.html', resultado=resultado)
    resultado = 'Usuario o contraseña incorrectos'
    return render_template('inicioSesion.html', resultado=resultado)

app.run(debug=True)


