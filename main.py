from pyscript import display, document

def students_classification(e):
    document.getElementById("result").innerHTML = ''

    grade = float(document.getElementById("number1").value)

    if grade >= 95 and grade <= 100:
        display(f"Bergamo 1", target="result")
    elif grade >= 91 and grade < 95:
        display(f"Bergamo 2", target="result")
    elif grade >= 86 and grade <= 90:
        display(f"Bergamo 3", target="result")
    elif grade >= 75 and grade <= 85:
        display(f"Perugia 1", target="result")
    elif grade >= 65 and grade <= 74:
        display(f"Perugia 2", target="result")
    else:
        pass
