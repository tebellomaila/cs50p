def main():
    expr = input("Expression: ").strip()

    x, y, z = expr.split()

    x = float(x)
    z = float(z)

    ans = calculate(x, y, z)

    print(ans)

def calculate(x, y, z):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return "undefined" if z == 0 else x / z
        case "%":
            return x % z
        case "^":
            return x ** z
        case _:
            return "INVALID OPERATOR"

if __name__ == "__main__":
    main()
