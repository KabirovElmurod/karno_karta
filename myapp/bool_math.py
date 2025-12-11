def simple_to_math(item):
    sing = [
        'A','B','C','D','E','F','G','J'
    ]
    find = False
    for i in range(len(item)):
        if item[i] == '|':
            item = item[:i] + '+' + item[i+1:]
        if i!=0:
            if item[i] in sing:
                # print(item)
                if item[i-1] == "'":
                    find = True
                    item = item[:i]+'*'+item[i:]
                    return simple_to_math(item)
                elif item[i-1] in sing:
                    find = True
                    item = item[:i] + '*' + item[i:]
                    return simple_to_math(item)
    if find == False:
        return item

def mdnsh_to_simple(a):
    a = str(a)
    for i in range(len(a)):
        if a[i] == '|':
            a = a[:i] + '+' + a[i+1:]
        elif a[i] == '&':
            a = a[:i] + '*' + a[i+1:]
        elif a[i] == '~':
            a=a[:i]+a[i+1]+"'"+a[i+2:]
    return a


def str_to_bool(item):
    find = False
    for i in range(len(item)):
        if item[i] == "'":
            find = True
            item = item[:i-1] + '(not ' + item[i-1] + ')' + item[i+1:]
    if find == True:
        return str_to_bool(item)
    else:
        return item

def main(misol_text):
    a = misol_text
    a = simple_to_math(a)
    return str_to_bool(a)