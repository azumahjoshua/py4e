def arithmetic_arranger(problems, answer=""):
    # check  the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operator = []

    # split the problem
    for problem in problems:
        piece = problem.split()
        # print("Piece: ",piece)
        first_operand.append(piece[0])
        second_operand.append(piece[2])
        operator.append(piece[1])
        # print(first_operand)
        # print(second_operand)
        # print(operator)

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

#  check if first operand is a digit
    for operand in first_operand:
        if not operand.isdigit():
            return "Error: Numbers must only contain digits."
        # print(operand)

# check if second operand is  a digit
    for operand in second_operand:
        if not operand.isdigit():
            return "Error: Numbers must only contain digits."

    for operand in first_operand:
        if len(operand) > 4:
            # print(len(operand))
            return "Error: Numbers cannot be more than four digits."
        # print(len(operand))

    for operand in second_operand:
        if len(operand) > 4:
            # print(len(operand))
            return "Error: Numbers cannot be more than four digits."

    firstrow = []
    secondrow = []
    thirdrow = []
    fourthrow = []

    # first row
    for operand in range(len(first_operand)):
        if len(first_operand[operand]) > len(second_operand[operand]):
            firstrow.append(" "*2 + first_operand[operand])
        else:
            firstrow.append(
                " "*(len(second_operand[operand]) - len(first_operand[operand])+2) + first_operand[operand])

    # second row
    for operand in range(len(second_operand)):
        if len(second_operand[operand]) > len(first_operand[operand]):
            secondrow.append(operator[operand]+" "+second_operand[operand])
        else:
            secondrow.append(operator[operand]+" "*(len(first_operand[operand]) -
                             len(second_operand[operand]) + 1) + second_operand[operand])

    # third row
    for item in range(len(first_operand)):
        thirdrow.append(
            "_"*(max(len(first_operand[item]), len(second_operand[item])) + 2))

# fourth row answer
    if answer:
        for item in range(len(first_operand)):
            if operator[item] == "+":
                result = str(
                    int(first_operand[item]) + int(second_operand[item]))
            else:
                result = str(
                    int(first_operand[item]) - int(second_operand[item]))
            # print("-----"+result+"------")
            if len(result) > max(len(first_operand[item]), len(second_operand[item])):
                fourthrow.append(" "+result)
            else:
                fourthrow.append(
                    " "*(max(len(first_operand[item]), len(second_operand[item])) - len(result) + 2) + result)
        arranged_problems = "    ".join(firstrow) + "\n" + "    ".join(
            secondrow) + "\n" + "    ".join(thirdrow) + "\n" + "    ".join(fourthrow)
    else:
        arranged_problems = "    ".join(
            firstrow) + "\n" + "    ".join(secondrow) + "\n" + "    ".join(thirdrow)
    # print(firstrow)
    # print(secondrow)
    # print(thirdrow)
#   print(fourthrow)

    return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801',
      '45 + 43', '123 + 49', '988 + 40'], True))
