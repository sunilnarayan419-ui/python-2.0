# Assignment operators

class AssignmentOperators:
    """This class demonstrates assignment operators with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        results = {}

        a = num_1
        a += num_2
        results["Addition Assignment (+=)"] = f"a += b → {a}"

        a = num_1
        a -= num_2
        results["Subtraction Assignment (-=)"] = f"a -= b → {a}"

        a = num_1
        a *= num_2
        results["Multiplication Assignment (*=)"] = f"a *= b → {a}"

        a = num_1
        a /= num_2
        results["Division Assignment (/=)"] = f"a /= b → {a}"

        a = num_1
        a %= num_2
        results["Modulus Assignment (%=)"] = f"a %= b → {a}"

        a = num_1
        a **= num_2
        results["Exponent Assignment (**=)"] = f"a **= b → {a}"

        a = num_1
        a //= num_2
        results["Floor Division Assignment (//=)"] = f"a //= b → {a}"

        return results


while True:
    try:
        num_1 = float(input("Enter first number : "))
        num_2 = float(input("Enter second number : "))

        result = AssignmentOperators.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break

    except ValueError:
        print("Enter numeric values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
