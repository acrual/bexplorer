from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Adolfo"
    letras = list(nombre)
    puppies = ['manuo', 'pepeito', 'que pasa']
    return render_template('basic.html', mivariable = nombre, milista = puppies)


if __name__ == '__main__':
    app.run(debug=True)
