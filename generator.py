def countdown(cnt=10):
    for i in range(cnt, -1, -1):
        yield i


if __name__ == "__main__":
    for i in countdown(15):
        print(i)
