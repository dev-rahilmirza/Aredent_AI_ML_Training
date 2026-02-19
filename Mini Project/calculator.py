"""
Advanced Calculator - Supports +, -, *, /, %, mean, median, mode, avg
Modes:
  - Separate Input : Enter numbers one by one
  - Single Line    : Enter expression like  10 + 5  or  3 * 4 / 2 + 1
"""

import statistics
import re


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def smart_display(value):
    """Typecast float to int if it is a whole number, else round to 6 dp."""
    return int(value) if value == int(value) else round(value, 6)


def get_number(prompt):
    """Get a single float number from user with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Invalid input! Please enter a valid number.")


def get_numbers_list():
    """Get a space-separated list of numbers from user."""
    while True:
        raw = input("  Enter numbers separated by spaces: ")
        try:
            numbers = [float(x) for x in raw.strip().split()]
            if len(numbers) < 1:
                print("  ⚠️  Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("  ⚠️  Invalid input! Please enter valid numbers separated by spaces.")


# ─────────────────────────────────────────────
#  MODE A — SEPARATE INPUT (one number at a time)
# ─────────────────────────────────────────────

def separate_basic_operation(op):
    """Perform a single basic operation with step-by-step input."""
    a = get_number("  Enter first number  : ")
    b = get_number("  Enter second number : ")

    a_d = smart_display(a)
    b_d = smart_display(b)

    if op in ('/', '%') and b == 0:
        label = "Division" if op == '/' else "Modulus"
        print(f"\n  ❌  Error: {label} by zero is not allowed!")
        return

    if op == '+':
        result, expr = a + b, f"{a_d} + {b_d}"
    elif op == '-':
        result, expr = a - b, f"{a_d} - {b_d}"
    elif op == '*':
        result, expr = a * b, f"{a_d} × {b_d}"
    elif op == '/':
        result, expr = a / b, f"{a_d} ÷ {b_d}"
    elif op == '%':
        result, expr = a % b, f"{a_d} % {b_d}"

    print(f"\n  ✅  Result: {expr} = {smart_display(result)}")


# ─────────────────────────────────────────────
#  MODE B — SINGLE LINE EXPRESSION EVALUATOR
# ─────────────────────────────────────────────

def tokenize(expr):
    """Tokenize an expression into numbers and operators."""
    token_pattern = re.compile(r'\d+\.?\d*|[+\-*/%]')
    return token_pattern.findall(expr)


def evaluate_expression(expr):
    """
    Evaluate a multi-operator arithmetic expression respecting
    standard operator precedence (* / % before + -).
    Returns (result, steps_list).
    """
    tokens = tokenize(expr)
    if not tokens:
        raise ValueError("Empty expression.")

    # Build value and operator lists
    values, operators = [], []
    expect_number = True
    for tok in tokens:
        if expect_number:
            try:
                values.append(float(tok))
            except ValueError:
                raise ValueError(f"Expected a number, got '{tok}'.")
            expect_number = False
        else:
            if tok not in ('+', '-', '*', '/', '%'):
                raise ValueError(f"Unknown operator: '{tok}'.")
            operators.append(tok)
            expect_number = True

    if expect_number:
        raise ValueError("Expression ends with an operator.")
    if not values:
        raise ValueError("No numbers found.")

    steps = []
    nums = list(values)
    ops  = list(operators)

    # Pass 1: higher-precedence operators  * / %
    i = 0
    while i < len(ops):
        op = ops[i]
        if op in ('*', '/', '%'):
            a, b = nums[i], nums[i + 1]
            if op == '*':
                res, sym = a * b, '×'
            elif op == '/':
                if b == 0: raise ZeroDivisionError("Division by zero.")
                res, sym = a / b, '÷'
            else:
                if b == 0: raise ZeroDivisionError("Modulus by zero.")
                res, sym = a % b, '%'
            steps.append(f"{smart_display(a)} {sym} {smart_display(b)} = {smart_display(res)}")
            nums[i] = res
            nums.pop(i + 1)
            ops.pop(i)
        else:
            i += 1

    # Pass 2: lower-precedence operators  + -
    i = 0
    while i < len(ops):
        a, b, op = nums[i], nums[i + 1], ops[i]
        res = a + b if op == '+' else a - b
        steps.append(f"{smart_display(a)} {op} {smart_display(b)} = {smart_display(res)}")
        nums[i] = res
        nums.pop(i + 1)
        ops.pop(i)

    return nums[0], steps


def single_line_mode():
    """Interactive single-line expression evaluator."""
    print("\n  ─────────────────────────────────────────")
    print("  📝  SINGLE LINE EXPRESSION MODE")
    print("  ─────────────────────────────────────────")
    print("  Supports  : + - * / %")
    print("  Precedence: (* / %) evaluated before (+ -)")
    print("  Examples  :")
    print("    10 + 5")
    print("    100 / 4 + 3 * 2")
    print("    15 % 4 - 1 * 2 + 7")
    print("  Type 'back' to return to the main menu.")
    print("  ─────────────────────────────────────────")

    while True:
        expr = input("\n  Enter expression : ").strip()
        if expr.lower() == 'back':
            break
        if not expr:
            print("  ⚠️  Please enter an expression.")
            continue
        try:
            result, steps = evaluate_expression(expr)
            print(f"\n  Expression : {expr}")
            if len(steps) > 1:
                print("  Steps      :")
                for idx, step in enumerate(steps, 1):
                    print(f"    Step {idx}: {step}")
            print(f"\n  ✅  Final Result = {smart_display(result)}")
        except ZeroDivisionError as e:
            print(f"\n  ❌  Error: {e}")
        except ValueError as e:
            print(f"\n  ⚠️  Invalid expression — {e}")
            print("      Example: 10 + 5 * 3 / 2")


# ─────────────────────────────────────────────
#  STATISTICAL OPERATIONS
# ─────────────────────────────────────────────

def stat_operation(op):
    print(f"\n  --- {op.upper()} ---")
    numbers = get_numbers_list()
    print(f"  Numbers entered : {[smart_display(n) for n in numbers]}")

    if op in ('mean', 'average'):
        result, label = statistics.mean(numbers), "Mean / Average"
    elif op == 'median':
        result, label = statistics.median(numbers), "Median"
    elif op == 'mode':
        try:
            result, label = statistics.mode(numbers), "Mode"
        except statistics.StatisticsError:
            print("\n  ❌  No unique mode found (multiple values appear equally often).")
            modes = statistics.multimode(numbers)
            print(f"  ℹ️   All modes: {[smart_display(m) for m in modes]}")
            return

    print(f"\n  ✅  {label} = {smart_display(result)}")


# ─────────────────────────────────────────────
#  MENU
# ─────────────────────────────────────────────

def display_menu():
    print("\n" + "=" * 52)
    print("            🧮  ADVANCED CALCULATOR")
    print("=" * 52)
    print("  Basic — Separate Input (enter numbers one by one):")
    print("    1. Addition          (+)")
    print("    2. Subtraction       (-)")
    print("    3. Multiplication    (*)")
    print("    4. Division          (/)")
    print("    5. Modulus           (%)")
    print()
    print("  Basic — Single Line (type full expression):")
    print("    6. Expression Evaluator  e.g.  10 + 5 * 3 - 2")
    print()
    print("  Statistical Operations (list of numbers):")
    print("    7. Mean / Average")
    print("    8. Median")
    print("    9. Mode")
    print()
    print("    0. Exit")
    print("=" * 52)


def main():
    print("\n  Welcome to the Advanced Python Calculator!")
    print("  ✦ Separate mode  — enter numbers step by step")
    print("  ✦ Single-line mode — type full expression at once")
    print("  All values are typecasted (int / float) automatically.")

    while True:
        display_menu()
        choice = input("  Enter your choice (0-9): ").strip()

        if choice == '0':
            print("\n  👋  Thank you for using the calculator. Goodbye!\n")
            break
        elif choice == '1':
            print("\n  --- ADDITION  [Separate Input] ---")
            separate_basic_operation('+')
        elif choice == '2':
            print("\n  --- SUBTRACTION  [Separate Input] ---")
            separate_basic_operation('-')
        elif choice == '3':
            print("\n  --- MULTIPLICATION  [Separate Input] ---")
            separate_basic_operation('*')
        elif choice == '4':
            print("\n  --- DIVISION  [Separate Input] ---")
            separate_basic_operation('/')
        elif choice == '5':
            print("\n  --- MODULUS  [Separate Input] ---")
            separate_basic_operation('%')
        elif choice == '6':
            single_line_mode()
            continue        # single_line_mode has its own loop; skip the pause
        elif choice == '7':
            stat_operation('mean')
        elif choice == '8':
            stat_operation('median')
        elif choice == '9':
            stat_operation('mode')
        else:
            print("\n  ⚠️  Invalid choice! Please select between 0 and 9.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
