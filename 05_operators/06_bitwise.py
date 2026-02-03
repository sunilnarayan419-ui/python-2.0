# Bitwise operators

class BitwiseOperators:
    """This class demonstrates bitwise operators with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        a = int(num_1)
        b = int(num_2)

        results = {
            "AND (&)": f"{a} & {b} → {a & b}",
            "OR (|)": f"{a} | {b} → {a | b}",
            "XOR (^)": f"{a} ^ {b} → {a ^ b}",
            "NOT (~a)": f"~{a} → {~a}",
            "Left Shift (a << 1)": f"{a} << 1 → {a << 1}",
            "Right Shift (a >> 1)": f"{a} >> 1 → {a >> 1}",
        }
        return results


while True:
    try:
        num_1 = int(input("Enter first integer : "))
        num_2 = int(input("Enter second integer : "))

        result = BitwiseOperators.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break

    except ValueError:
        print("Enter integer values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
