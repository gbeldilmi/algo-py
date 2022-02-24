import list as L


def eval_postfix(expr):
    stack = None
    for op in expr.split():
        if op in ["+", "-", "*", "/", "^", "%"]:
            # Eval
            assert L.length(stack) >= 2
            a = L.head(L.tail(stack))
            b = L.head(stack)
            r = 0
            if op == "+":
                r = a + b
            elif op == "-":
                r = a - b
            elif op == "*":
                r = a * b
            elif op == "/":
                r = a / b
            elif op == "%":
                r = a % b
            else:
                r = a**b
            stack = L.build(r, L.tail(L.tail(stack)))
        else:
            # Push to the stack
            num = float(op)
            stack = L.build(num, stack)
            pass
    assert L.tail(stack) == None
    return L.head(stack)


if __name__ == "__main__":
    e1 = "2 7 ^ 28 - 5 / 3 -"  # 17
    e2 = "8 3 % 7 +"  # 9
    print(eval_postfix(e1))
    print(eval_postfix(e2))
