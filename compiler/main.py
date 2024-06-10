# main.py

import sys
from solveExpresions import solve_expression  # Supongamos que este archivo contiene la lógica para resolver expresiones

def main():
    try:
        with open('entrada.txt', 'r') as file:
            code = file.read()
        result = solve_expression(code)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
