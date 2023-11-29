class ExampleClass:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def add(self):
        sum_result = self.val1 + self.val2
        print("Sum is:", sum_result)


def another_function():
    print("This function does nothing useful")


example = ExampleClass(5, 10)
example.add()

for i in range(0, 10):
    print(i)


def unused_function():
    pass


example_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


def yet_another_function():
    if True:
        print("This block has consistent indentation")


def function_with_too_many_arguments(a, b, c, d, e, f, g, h, i, j, k):
    pass


if __name__ == "__main__":
    another_function()
    unused_function()
    yet_another_function()
    function_with_too_many_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)