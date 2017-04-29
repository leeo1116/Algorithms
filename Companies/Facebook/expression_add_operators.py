def add_operator(num_str, target):
    expressions = []
    add_operator_helper(num_str, 0, target, "", expressions, 0, 0)
    return expressions


def add_operator_helper(num_str, start, target, expression, expressions, evaluation, evaluation_tmp):
    if start == len(num_str):  # A complete traversal
        if evaluation == target:
            expressions.append(expression)
            return
    for i in range(start, len(num_str)):
        if num_str[start] == '0' and i > start:
            break
        num = num_str[start:i + 1]
        expression_tmp = expression  # protect expression
        if start == 0:  # The first operand has no operator to its left
            add_operator_helper(num_str, i + 1, target, expression + num, expressions,
                                evaluation + int(num), int(num))
            expression = expression_tmp  # restore expression
        else:
            # try adding
            add_operator_helper(num_str, i + 1, target, expression + '+' + num, expressions,
                                evaluation + int(num), int(num))
            expression = expression_tmp  # restore expression
            # try subtracting
            add_operator_helper(num_str, i + 1, target, expression + '-' + num, expressions,
                                evaluation - int(num), -int(num))
            expression = expression_tmp  # restore expression
            # try multiplying
            add_operator_helper(num_str, i + 1, target, expression + '*' + num, expressions,
                                evaluation - evaluation_tmp + evaluation_tmp * int(num), evaluation_tmp * int(num))


print(add_operator("123", 6))
