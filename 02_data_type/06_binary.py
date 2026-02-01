class DataTypesDemo:
    @staticmethod
    def bytes_example(name, age, city):
        # bytes → immutable
        data = f"{name},{age},{city}"
        result = bytes(data, encoding="utf-8")
        return result

    @staticmethod
    def bytearray_example(name, age, city):
        # bytearray → mutable
        data = f"{name},{age},{city}"
        result = bytearray(data, encoding="utf-8")

        # modify data (change 's' → 'S')
        result[0] = ord('S')
        return result

    @staticmethod
    def memoryview_example(name, age, city):
        # memoryview → view of bytes without copying
        data = f"{name},{age},{city}"
        byte_data = bytes(data, encoding="utf-8")
        view = memoryview(byte_data)
        return view


# ---- Usage ----
name = "sunil"
age = 56
city = "hyderabad"

print("Bytes:", DataTypesDemo.bytes_example(name, age, city))
print("Bytearray:", DataTypesDemo.bytearray_example(name, age, city))
print("Memoryview:", DataTypesDemo.memoryview_example(name, age, city))
