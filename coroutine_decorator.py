# Based on http://www.dabeaz.com/coroutines/Coroutines.pdf


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def grep(pattern):
    print("Looking for", pattern)
    try:
        while True:
            # What happens here?
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye!")


if __name__ == "__main__":
    g = grep("test")

    g.send("What is the new version of python?")
    g.send("I am testing this now")
