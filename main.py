from pyscript import display, document

# First example
def julias_answer(e):
    document.getElementById("output").innerHTML = ''

    response = document.getElementById("input1").value.lower()

    if response == 'yes':
        display(f"Kian will be her valentine", target="output")
    elif response == 'no':
        display(f"Kian will be rejected/heart broken", target="output")
    elif response == 'maybe':
        display(f"Don't give up try again!", target="output")
    else:
        display(f"Invalid input", target="output")

# Second example
def students_classification(e):
    document.getElementById("result").innerHTML = ''

    grade = float(document.getElementById("number1").value)

    if grade >= 95:
        display(f"Bergamo 1", target="result")
    elif grade >= 91 and grade < 95:
        display(f"Bergamo 2", target="result")
    elif grade >= 86 and grade <= 90:
        display(f"Bergamo 3", target="result")
    elif grade >= 75 and grade <= 85:
        display(f"Perugia 1", target="result")
    else:
        display(f"Perugia 2", target="result")