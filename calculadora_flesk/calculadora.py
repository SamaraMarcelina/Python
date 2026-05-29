import math
from flask import render_template, request


def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "bhaskara":

        a = float(request.form["num1"])
        b = float(request.form["b"])
        c = float(request.form["c"])

        delta = b**2 - 4*a*c

        if delta < 0:
            resultado = "Sem raízes reais"
            etapas = f"Δ = {delta}"

        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)

            resultado = f"x1 = {x1}, x2 = {x2}"

            etapas = (
                f"Δ = {b}² - 4·{a}·{c} = {delta}<br>"
                f"x1 = {x1}<br>"
                f"x2 = {x2}"
            )

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "log":

            if num1 <= 0:
                resultado = "Erro"
                etapas = "Logaritmo só existe para números positivos."
            else:
                resultado = math.log(num1, num2)
                etapas = f"log({num1} log {num2}) = {resultado}"
        

        elif operacao == '+':
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"
            else:
                resultado = "Erro: Não é possível divisão por zero"
                etapas = "Operacão inrealizável"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ** {num2} = {resultado}"
        else:
            resultado = "Operação inválida"
            etapas = "A operação selecioaa é inválida"

    return render_template("calculadora.html", etapas=etapas, resultado=resultado)
            
