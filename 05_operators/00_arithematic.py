# Arithematic operators

class Arithmetics:
    """This class demonstrates arithmetic operations with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        results = {
            "Addition": f"{num_1} + {num_2} = {num_1 + num_2}",
            "Subtraction": f"{num_1} - {num_2} = {num_1 - num_2}",
            "Multiplication": f"{num_1} * {num_2} = {num_1 * num_2}",
            "Division": f"{num_1} / {num_2} = {num_1 / num_2}",
            "Modulus": f"{num_1} % {num_2} = {num_1 % num_2}",
            "Exponential": f"{num_1} ** {num_2} = {num_1 ** num_2}",
            "Floor Division": f"{num_1} // {num_2} = {num_1 // num_2}",
        }
        return results


while True:
    try:
        num_1 = float(input("Enter first number : "))
        num_2 = float(input("Enter second number : "))

        result = Arithmetics.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break   

    except ValueError:
        print("Enter numeric values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
