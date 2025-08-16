# defines a function to calculate the area of a rectangle

def area(length, width):
    return length * width

def main():
    # calculates the areas
    house = area(172, 230)
    fence = area(520, 872)
    
    # add total area
    total = house + fence

    # `str` converts total to string and `chr` used to add superscript '2' to m
    print("Total Area: " + str(total) + "m" + chr(178))


main()
