# Comparison (Relational) operators

class ComparisonOperators:
    """This class demonstrates comparison operators with examples."""

    @staticmethod
    def calculate(num_1, num_2):
        results = {
            "Equal to (==)": f"{num_1} == {num_2} → {num_1 == num_2}",
            "Not equal to (!=)": f"{num_1} != {num_2} → {num_1 != num_2}",
            "Greater than (>)": f"{num_1} > {num_2} → {num_1 > num_2}",
            "Less than (<)": f"{num_1} < {num_2} → {num_1 < num_2}",
            "Greater than or equal to (>=)": f"{num_1} >= {num_2} → {num_1 >= num_2}",
            "Less than or equal to (<=)": f"{num_1} <= {num_2} → {num_1 <= num_2}",
        }
        return results


while True:
    try:
        num_1 = float(input("Enter first number : "))
        num_2 = float(input("Enter second number : "))

        result = ComparisonOperators.calculate(num_1, num_2)

        for operation, value in result.items():
            print(value)

        break

    except ValueError:
        print("Enter numeric values only !!")
    except Exception as e:
        print("Something went wrong !!", e)
