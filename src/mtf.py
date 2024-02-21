# Move-To-Front algorithm
# https://en.wikipedia.org/wiki/Move-to-front_transform

def code(s):
    abc = [chr(i) for i in range(256)]
    result = []
    for c in s:
        i = abc.index(c)
        result.append(i)
        del abc[i]
        abc.insert(0, c)
    return result

def decode(s):
    abc = [chr(i) for i in range(256)]
    result = ""
    for i in s:
        c = abc[i]
        result += str(c)
        del abc[i]
        abc.insert(0, c)
    return result

if __name__ == '__main__':
    s = 'bananaaa ist ein text'
    l = code(s)
    print(l)
    print(decode(l))
