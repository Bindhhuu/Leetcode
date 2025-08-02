stack = []
        result = 0
        num = 0
        sign = 1  # 1 means +, -1 means -

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # handle multi-digit numbers

            elif char in ['+', '-']:
                result += sign * num  # finalize the previous number
                num = 0
                sign = 1 if char == '+' else -1

            elif char == '(':
                # Push the result and sign into stack to start a new context
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif char == ')':
                result += sign * num  # finalize inner expression
                num = 0
                result *= stack.pop()  # apply the sign before '('
                result += stack.pop()  # add the result before '('

        result += sign * num  # add any remaining number
        return result
