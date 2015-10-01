if __name__ == '__main__':
    la = [1, 2, 3, 4, 5]
    lb = [6, 7, 8, 9, 10]

    lc = ["abc", 5, 5.9, "zzz"]  # List can have multiple types

    # Printing whole list
    print(la)

    # Printing one element
    print(la[0])

    # Iterating over a list
    for i in la:
        print(i)

    # Not very nice
    for i in range(len(lc)):
        print(i, lc[i])

    # Much better
    for it, elem in enumerate(lc):
        print(it, elem)

    # Adding a single element
    la.append(11)
    print(la)
    print(len(la))

    # Contatenating two lists together
    la.extend(lb)
    print(la)

    # Adding one list as an element of another list
    la.append(lb)
    print(la)

    # Check if element is in the list
    print("zzz" in lc)

    unsorted = [2, 5, 1, 6, 9, 8, 10, 88, 11]
    # Sort list
    print(sorted(unsorted))
