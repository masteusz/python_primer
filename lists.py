if __name__ == '__main__':
    la = [1, 2, 3, 4, 5]
    lb = [6, 7, 8, 9, 10]

    print(la)

    print(la[0])

    for i in la:
        print(i)

    # Not very nice
    for i in range(len(la)):
        print(i, la[i])

    # Much better
    for it, elem in enumerate(la):
        print(it, elem)

    la.append(11)
    print(la)

    print(len(la))
