# Logical operators

class LogicalOperators:
    """This class demonstrates logical operators with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        results = {
            "AND (num_1 > 0 and num_2 > 0)":
                f"({num_1} > 0 and {num_2} > 0) → {num_1 > 0 and num_2 > 0}",

            "OR (num_1 > 0 or num_2 > 0)":
                f"({num_1} > 0 or {num_2} > 0) → {num_1 > 0 or num_2 > 0}",

            "NOT (not num_1 > 0)":
                f"(not {num_1} > 0) → {not num_1 > 0}",
        }
        return results


while True:
    try:
        num_1 = float(input("Enter first number : "))
        num_2 = float(input("Enter second number : "))

        result = LogicalOperators.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break

    except ValueError:
        print("Enter numeric values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
