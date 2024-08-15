from flask import Flask, render_template, request, redirect
app = Flask(__name__)

adicionar_ = []

@app.route('/')
def index():
    return render_template('index.html', adicionar=adicionar_)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/verificar_adicionar', methods=['GET', 'POST'])
def verificar_adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        ano = request.form['ano']
        genero = request.form['genero']
        elenco = request.form['elenco']
        duracao = request.form['duracao']
        codigo = len(adicionar_)
        adicionar_.append([codigo, nome, ano, genero, elenco, duracao])
        return render_template('index.html', adicionar=adicionar_)
    return redirect('/')

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/verificar_editar/<int:codigo>', methods=['GET', 'POST'])
def verificar_editar(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        ano = request.form['ano']
        genero = request.form['genero']
        elenco = request.form['elenco']
        duracao = request.form['duracao']
        adicionar_.append([codigo, nome, ano, genero, elenco, duracao])
        return render_template('index.html', adicionar=adicionar_)

    else:
        adicionar = adicionar_[codigo]
        return render_template('editar.html', adicionar=adicionar)

@app.route('/apagar/<int:codigo>')
def apagar(codigo):
    del adicionar_[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)