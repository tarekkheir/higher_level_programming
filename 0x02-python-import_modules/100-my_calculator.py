#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    n = 0
    n = len(sys.argv)
    if n == 4:
        a = int(sys.argv[1])
        b = sys.argv[2]
        c = int(sys.argv[3])
        print("{} {} {}".format(a, b, c), end=' ')
        if sys.argv[2] == '+':
              print("= {}".format(calculator_1.add(a, c)))
        elif sys.argv[2] == '*':
              print("= {}".format(calculator_1.mul(a, c)))
        elif sys.argv[2] == '-':
              print("= {}".format(calculator_1.sub(a, c)))
        elif sys.argv[2] == '/':
              print("= {}".format(calculator_1.div(a, c)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
