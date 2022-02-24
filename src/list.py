def head(list):
    assert list != None
    (head, tail) = list
    return head


def tail(list):
    assert list != None
    (head, tail) = list
    return tail


def build(head, tail):
    return (head, tail)


def itoj(i, j, step=1):
    if i == j:
        return build(i, None)
    if i > j:
        return build(i, itoj(i - step, j, step))
    return build(i, itoj(i + step, j, step))


def length(list):
    if list == None:
        return 0
    return 1 + length(tail(list))


def map(function, list):
    if list == None:
        return None
    return build(function(head(list)), map(function, tail(list)))


def sum(list):
    if list == None:
        return 0
    return head(list) + sum(tail(list))


if __name__ == "__main__":
    list = itoj(-2, 9)
    print(list)
    print(length(list))
    print(map((lambda x: x * 10), list))
    print(sum(list))
