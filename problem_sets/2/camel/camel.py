def camel_to_snake(s):
    snake = []

    for c in s:
        if c.isupper():
            if c != s[0]:
                snake.append("_")

                snake.append(c.lower())
        else:
            snake.append(c)

    for c in snake:
        print(c, end="")


def main():
    camel_str = input("camelCase: ").strip()
    camel_to_snake(camel_str)
    


if __name__ == "__main__":
    main()
