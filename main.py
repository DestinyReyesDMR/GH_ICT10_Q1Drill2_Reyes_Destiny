from pyscript import document

def get_inputs():
    val1 = document.querySelector("#num1").value
    val2 = document.querySelector("#num2").value
    if not val1 or not val2:
        return None, None
    return float(val1), float(val2)

def set_output(text):
    out_el = document.querySelector("#output")
    if out_el:
        out_el.innerHTML = text

# Addition: Adds two numbers
def add_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    set_output(f"The sum of {n1} and {n2} is {n1 + n2}")

# Subtraction: Subtracts second number from first
def subtract_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    set_output(f"The difference of {n1} and {n2} is {n1 - n2}")

# Multiplication: Multiplies two numbers
def multiply_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    set_output(f"The product of {n1} and {n2} is {n1 * n2}")

# Division: Divides first number by second
def divide_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    res = n1 / n2 if n2 != 0 else "Cannot divide by zero"
    set_output(f"The quotient of {n1} and {n2} is {res}")

# Floor Division: Divides and rounds down to whole number
def floor_divide_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    res = n1 // n2 if n2 != 0 else "Undefined"
    set_output(f"The floor division of {n1} and {n2} is {res}")

# Modulus: Calculates remainder after division
def modulus_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    res = n1 % n2 if n2 != 0 else "Undefined"
    set_output(f"The modulus of {n1} and {n2} is {res}")

# Exponent: Raises first number to the power of second
def power_numbers(event=None):
    n1, n2 = get_inputs()
    if n1 is None: return
    set_output(f"The exponent of {n1} raised to {n2} is {n1 ** n2}")