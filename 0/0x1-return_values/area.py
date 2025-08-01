def area(length, width):
    return length * width

if __name__ == "__main__":
    house = area(172, 230)
    fence = area(520, 872)

    total = house + fence

    print("Total Area: " + str(total) + "m" + chr(178))

