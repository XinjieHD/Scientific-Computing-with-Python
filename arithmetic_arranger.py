def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    index = 0  

    for problem in problems:
        parts = problem.split()
        left_operand = parts[0]
        operator = parts[1]
        right_operand = parts[2]


      
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (left_operand.isdigit() and right_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

       
        width = max(len(left_operand), len(right_operand)) + 2
        first_line += left_operand.rjust(width)
        second_line += operator + right_operand.rjust(width - 1)
        dashes += "-" * width

        if show_answers:
            result = str(eval(problem))  # Calculate the result
            answers += result.rjust(width)

      
        if index < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            if show_answers:
                answers += "    "

        index += 1  


    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    if show_answers:
        arranged_problems += "\n" + answers

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
