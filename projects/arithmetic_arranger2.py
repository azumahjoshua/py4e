def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first_operand.append(pieces[0])
        operator.append(pieces[1])
        second_operand.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    firstrow = []
    secondrow = []
    thirdrow = []
    fourthrow = []

    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            firstrow.append(" "*2 + first_operand[i])
        else:
            firstrow.append(
                " "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            secondrow.append(operator[i] + " " + second_operand[i])
        else:
            secondrow.append(
                operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

    for i in range(len(first_operand)):
        thirdrow.append(
            "-"*(max(len(first_operand[i]), len(second_operand[i])) + 2))

    if answer:
        for i in range(len(first_operand)):
            if operator[i] == "+":
                ans = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                ans = str(int(first_operand[i]) - int(second_operand[i]))

            if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
                fourthrow.append(" " + ans)
            else:
                fourthrow.append(
                    " "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(firstrow) + "\n" + "    ".join(
            secondrow) + "\n" + "    ".join(thirdrow) + "\n" + "    ".join(fourthrow)
    else:
        arranged_problems = "    ".join(
            firstrow) + "\n" + "    ".join(secondrow) + "\n" + "    ".join(thirdrow)
    return arranged_problems


# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
