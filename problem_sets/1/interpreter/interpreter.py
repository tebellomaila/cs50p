def main():
    expr = input("Expression: ").strip()

    x, operator, y = expr.split()

    x = float(x)
    y = float(y)

    ans = calculate(x, operator, y)

    print(ans)

def calculate(x, operator, y):
    match operator:
        case "+":
            return x + y
        case "-":   
            return x - y
        case "*":
            return x * y
        case "/":
            return "undefined" if z == 0 else x / y
        case "%":
            return x % y
        case "^":
            return x ** y
        case _:
            return "INVALID OPERATOR"

if __name__ == "__main__":
    main()
