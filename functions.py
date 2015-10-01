def hello_world():
    print("Hello World!")


def function_with_arguments(first_arg, second_arg):
    print("This is the first argument:", first_arg)
    print("This is the second argument:", second_arg)


def add_one(number):
    return number + 1


if __name__ == "__main__":
    hello_world()

    function_with_arguments("This is a string", 1.32)

    print(add_one(5))
    print(add_one(1.22))
