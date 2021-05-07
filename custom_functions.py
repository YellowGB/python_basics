def helloWorld():
    print("Hello World")

def addNumbers(num1,num2):
    sum = num1 + num2
    return sum

def substractNumbers(num1,num2):
    sub = num1 - num2
    return sub

def squareNum(num1):
    mul = num1 * num1
    print(mul)

# Ce qui suit ne s'exécutera que si le "programme"
# est lancé directement depuis ce fichier
# et pas s'il est appelé dans un import
# depuis un autre fichier (exemple dans exercices_algo.py)
if __name__ == "__main__":
    # Call the function helloWorld
    helloWorld()

    # Add numbers
    addNumbers(2,3)
    addNumbers(4,5)

    # Square number
    squareNum(12)