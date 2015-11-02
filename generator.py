def grep(pattern):
    print("Looking for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

if __name__ == "__main__":
    g = grep("test")
    next(g)

    g.send("What is the new version of python?")
    g.send("I am testing this now")
