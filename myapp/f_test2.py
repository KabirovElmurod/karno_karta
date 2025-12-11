from . import bool_math
# import bool_math
word = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
]
sign = [
    '*', "+"
]

def sort_only_word(items):
    max=ord(items[0])
    for i in range(len(items)):
        for j in range(len(items)):
            if(ord(items[i])<ord(items[j])):
                max = items[i]
                items[i] = items[j]
                items[j] = max
    return items

def rostlik_jadval(item, words):
    for i in item:
        print(i, '  ', end='')
    print()
    for i in range(len(item['A'])):
        s= ''
        for j in item:
            # print(j)
            s+= str(item[j][i]) + '   '
        print(s)


def main(misol_text):
    a = bool_math.main(misol_text)
    only_one_word = []

    for i in a:
        if i in word and i not in only_one_word:
            only_one_word.append(i)
    only_one_word = sort_only_word(only_one_word)
    amount = {}
    for i in range(0, len(only_one_word)):
        son=0
        bir=False
        mass = {
            only_one_word[i] : []
        }
        for j in range(0, 2**(len(only_one_word))):
            
            if (len(only_one_word)**2)//(2**(i+1))==son:
                if(not bir):
                    bir=True
                else:
                    bir=False
                son = 0
            if bir:
                mass[only_one_word[i]].append(1)
                son+=1
            else:
                mass[only_one_word[i]].append(0)
                son+=1
        # print('mass=', mass)
        amount[only_one_word[i]] =mass[only_one_word[i]]

    # print('amount =', amount)

    a = list(a)

    for i in range(len(a)):
        if a[i] == '¬':
            a[i] ='(not '
            if(a[i+1]=='('):
                qavs = 0
                for j in range(i, len(a)):
                    if a[j]=='(':
                        qavs+=1
                    if a[j] == ')':
                        qavs-=1
                        if(qavs==0):
                            a[j] = '))'
                            break 

    a = (''.join(a))
    # print('sa', amount)
    misol=a
    natija = {
        'natija' :[]
    }
    for i in range(2**len(only_one_word)):
        a=misol
        for j in range(len(only_one_word)):
            a = a.replace(only_one_word[j], str(amount[only_one_word[j]][i]))
        # print('a =', a)
        a=eval(a)
        if (a>1):
            a=1
            natija['natija'].append(1)
        else:
            natija['natija'].append(a)
            
        # print(a)

    amount['natija']=(natija['natija'])

    rostlik_jadval(amount, only_one_word)
    # print(amount)

    return amount['natija'], len(only_one_word)
