def exception_handeling(num1, operator, num2):
    # check if num is only digits
    try:
        int(num1) and int(num2)
    except:
        return 'Error: Numbers must only contain digits.'
    # check for length
    try:
        if len(num1) > 4 or len(num2) > 4:
            raise BaseException
    except:
        return 'Error: Numbers cannot be more than four digits.'
    # check the operator
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ''

# max(argv) = 5 else Error: Too many problems.
# missing +/- Error : Operator must be '+' or '-'.
# only digits else Error: Numbers must only contain digits.
# max len(num) = 4 else Error: Numbers cannot be more than four digits.

def arithmetic_arranger(problems, display=False):
    # variables
    spaceBetween = '    '
    first = True
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    # check the input
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return 'Error: Too many problems.'

    for problem in problems:
        temp = problem.split()
        #store single values to check in exception_handeling
        num1 = temp[0]
        num2 = temp[2]
        operator = temp[1]
        error = exception_handeling(num1, operator, num2)

        # if error.empty() =O True -> input valid
        if error != '':
            return error

        # get the max length for output
        length = max(len(num1), len(num2))

        # first operation sperate because of space inbetween
        if first == True:
            line1 += num1.rjust(length + 2)
            line2 += operator + ' ' + num2.rjust(length)
            line3 += '-' * (length + 2)
            if display == True:
                if operator == '+':
                    line4 += str(int(num1) + int(num2)).rjust(length + 2)
                else:
                    line4 += str(int(num1) - int(num2)).rjust(length + 2)
            first = False

        # the following operations
        else:
            line1 += num1.rjust(length + 6)
            line2 += operator.rjust(5) + ' ' + num2.rjust(length)
            line3 += spaceBetween + '-' * (length + 2)
            if display == True:
                if operator == '+':
                    line4 += spaceBetween + str(int(num1) + int(num2)).rjust(length + 2)
                else:
                    line4 += spaceBetween + str(int(num1) - int(num2)).rjust(length + 2)

    #to display
    if display == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
