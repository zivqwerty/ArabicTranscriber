from math import *

operations = ("+", "-", "*", "/", "^", "v", "!")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "^":
        return num1 ** num2
    elif operation == "v":
        return num2 ** (1 / num1)
    elif operation == "!":
        return factorial(num1)


class Calculation:

    def interpret(self):

        if not is_number(self.code):

            if ")" in self.code:
                rev = reversed(self.code)
                bracket_count = 0
                closing_bracket_index = self.code.rindex(")")
                opening_bracket_index = None
                index_counter = len(self.code)

                for c in rev:
                    if c == ")":
                        bracket_count += 1
                    elif c == "(":
                        bracket_count -= 1
                        if bracket_count == 0:
                            opening_bracket_index = index_counter
                            break

                    index_counter -= 1

                inside_brackets = self.code[opening_bracket_index+1:closing_bracket_index]
                if closing_bracket_index < len(self.code)-1:
                    self.code = self.code[0:opening_bracket_index] + str(Calculation(inside_brackets).get_value()) + self.code[closing_bracket_index+1:]
                else:
                    self.code = self.code[0:opening_bracket_index] + str(Calculation(inside_brackets).get_value())

            if "+" in self.code or "-" in self.code:
                if "+" not in self.code:
                    operation_index = self.code.rindex("-")
                elif "-" not in self.code:
                    operation_index = self.code.rindex("+")
                else:
                    operation_index = max(self.code.rindex("+"), self.code.rindex("-"))

            elif "*" in self.code or "/" in self.code:
                if "*" not in self.code:
                    operation_index = self.code.rindex("/")
                elif "/" not in self.code:
                    operation_index = self.code.rindex("*")
                else:
                    operation_index = max(self.code.rindex("*"), self.code.rindex("/"))

            elif "^" in self.code or "v" in self.code:
                if "^" not in self.code:
                    operation_index = self.code.rindex("v")
                elif "v" not in self.code:
                    operation_index = self.code.rindex("^")
                else:
                    operation_index = max(self.code.rindex("^"), self.code.rindex("v"))

            self.left = Calculation(self.code[0:operation_index])
            self.right = Calculation(self.code[operation_index + 1:])
            self.operation = self.code[operation_index]

    def __init__(self, code):
        self.code = str(code)
        self.operation = ""
        self.left = None
        self.right = None

        self.interpret()

    def get_value(self):
        if self.code == "":
            return None
        elif is_number(self.code):
            return float(self.code)
        else:
            return calculate(self.left.get_value(), self.operation, self.right.get_value())


calculation = Calculation(input("Enter calculation: "))
print(calculation.get_value())
