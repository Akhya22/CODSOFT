
print("=====SIMPLE CALCULATOR=====")


print("Arithmetic Operators -")
print("Addition (+)")
print("Subtraction (-) ")
print("Multiplication (*)")
print("Division (/)")

print()

m=float(input("Enter a: "))
n=float(input("Enter b: "))

print()


print("Select operators: +  -  *  / ")
operator = input("Enter operator: ")

def calculations(a,b):

    match operator:
        case "+":
            print(f"Result: {a} + {b} = {a + b}")

        case "-":
            print(f"Result: {a} - {b} = {a - b}")

        case "*":
            print(f"Result: {a} * {b} = {a * b}")

        case "/":
            if b==0:
                print("Error! Cannot divide by zero.")
            else:
                print(f"Result: {a} / {b} = {a / b}")

        case _:
            print()
            print("Invalid operator! Please select valid operators.")


calculations(m,n)
print()

print("-------END-------")


