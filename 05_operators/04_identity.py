# Identity operators

class IdentityOperators:
    """This class demonstrates identity operators with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        a = num_1
        b = num_2
        c = a   

        results = {
            "a is b": f"{a} is {b} → {a is b}",
            "a is not b": f"{a} is not {b} → {a is not b}",
            "a is c": f"{a} is c → {a is c}",
            "a == b": f"{a} == {b} → {a == b} (value comparison)",
        }
        return results


while True:
    try:
        num_1 = float(input("Enter first number : "))
        num_2 = float(input("Enter second number : "))

        result = IdentityOperators.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break

    except ValueError:
        print("Enter numeric values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
