# Membership operators

class MembershipOperators:
    """This class demonstrates membership operators with examples."""

    @staticmethod
    def calculate(text, value):
        results = {
            "in (value in text)": f"'{value}' in '{text}' → {value in text}",
            "not in (value not in text)": f"'{value}' not in '{text}' → {value not in text}",
        }
        return results


while True:
    try:
        text = input("Enter a string : ")
        value = input("Enter value to check : ")

        result = MembershipOperators.calculate(text, value)

        for operation, output in result.items():
            print(output)

        break

    except Exception as e:
        print("Something went wrong !!", e)
