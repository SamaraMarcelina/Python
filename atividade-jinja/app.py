from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    nome = "Samara"
    idade = 17

    usuario = {
        "nome": "Samara",
        "email": "samara@email.com"
    }

    alunos = {
        "Samara": 10,
        "João": 3,
        "Maria": 10,
        "Pedro": 6
    }

    aluno_selecionado = request.args.get("aluno")
    resultado = None

    if aluno_selecionado:
        nota = alunos.get(aluno_selecionado)

        if nota >= 7:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"

    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        usuario=usuario,
        alunos=alunos,
        resultado=resultado,
        aluno_selecionado=aluno_selecionado
    )

if __name__ == "__main__":
    app.run(debug=True)