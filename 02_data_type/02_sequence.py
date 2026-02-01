# List
def list_examples():
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('date')

    print("fruits:", fruits)
    print("first element:", fruits[0])
    print("slice [1:3]:", fruits[1:3])

    squares = [x * x for x in range(5)]
    print("squares:", squares)


# Tuple
def tuple_examples():
    point = (2, 3)
    single = (5,)   # single-element tuple

    print("point:", point)
    print("single-element tuple:", single)

    x, y = point
    print("unpacked values:", x, y)


# Range
def range_examples():
    r = range(0, 10, 2)

    print("range r as list:", list(r))

    print("iterate range(5):", end=" ")
    for i in range(5):
        print(i, end=" ")
    print()

    print("length of range(100):", len(range(100)))


# Main execution
if __name__ == "__main__":
    print("\n--- List Examples ---")
    list_examples()

    print("\n--- Tuple Examples ---")
    tuple_examples()

    print("\n--- Range Examples ---")
    range_examples()
