
from . import f_test2
from . import bool_math
# import f_test2
# import bool_math
def sign_harf(son):
    sing = [
        'A','B','C','D','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','Y','Z','X','W'
    ]
    sings = []
    for i in range(son):
        sings.append(sing[i])
    return sings

def onlik_to_biner(number, s=''):
    # s = ''
    qoldiq = str(number%2)
    qoldiq += s
    s = qoldiq
    # print('s =', s)
    if (number//2 == 0):
        return s
    return onlik_to_biner(number//2, s)

def only_one_item(string, item):
    if string not in item:
        item.append(string)
    return item
def gray_code(ozgaruvchi):
    k_map=[]
    for i in range(2**ozgaruvchi):
        k = i^i>>1
        # print(k)
        bin = onlik_to_biner(k)
        bin = 10**ozgaruvchi+int(bin)
        bin = str(bin)[1:]
        k_map.append(str(bin))
    return k_map
# print(gray_code(2))
def main(ozgaruvchi):
    row_item = []
    column_item=[]
    row=0
    column=0
    if ozgaruvchi%2==1: 
        row = ozgaruvchi//2+1
        column = ozgaruvchi-row
    else:
        row = ozgaruvchi//2
        column = ozgaruvchi-row
    row_item=gray_code(row)
    column_item = gray_code(column) 
    return row_item, column_item


def find_item(item, item_list):
    row_i = 0
    for i, row in enumerate(item_list):
        if item in row:
            index = row.index(item)
            row_i=i
    return row_i, index

def one_index(items):
    i=0
    group = []
    for row in items:
        if type(row)!=int:
            for item in row:
                if item == 1:
                    group.append(i)
                i+=1
        else:
            if row == 1:
                group.append(i)
            i+=1
    return group

# a = [0,0,1,1]
# print(one_index(a))

def f_oddit_func(a, son):
    f_oddiy = []
    for i in range(2**(a//2+a%2)):
        row = []
        for j in range(2**(a-a//2-a%2)):
            bin = onlik_to_biner(son)
            bin = str(10**a+int(bin))
            bin = bin[1:]
            row.append(bin)
            son+=1
        f_oddiy.append(row)
    return f_oddiy

print('f_oddit_func(3,0)=', f_oddit_func(3,0))

def k_map_func(a):
    rows, columns= main(a)
    k_map = []
    f_main = []
    for row in (rows):
        f_main_row = []
        k_map_row=[]
        for column in columns:
            f_main_row.append('')
            k_map_row.append(row+column)
        f_main.append(f_main_row)
        k_map.append(k_map_row)
    return f_main, k_map


def bin_func(a, k_map):
    bin = []
    for i in range(2**(a//2+a%2)):
        row = []
        for j in range(2**(a-a//2-a%2)):
            # bin = onlik_to_biner(son)
            # bin = str(10**a+int(bin))
            bin.append(k_map[i][j])
            # bin = k_map[i][j]
    return bin

def web_f_qiymat(a, f_amount, f_combi):
    f_main, k_map = k_map_func(a)
    son =0 
    f_oddiy = f_oddit_func(a,son)
    row = []

    for i in range(len(f_combi)):
        row_i, index = find_item(f_combi[i][2:], f_oddiy)
        f_main[row_i][index] = f_amount[i]
    
    changer_1_list = gray_code(a//2+a%2)
    changer_2_list = gray_code(a - (a//2 + a%2))

    return f_main, changer_1_list, changer_2_list


def web_f_qiymatlar(a):
    f_oddiy = f_oddit_func(a, 0)
    f_qiymat = []
    son = 0
    for row in f_oddiy:
        for index in row:
            f_qiymat.append(index)
    return f_qiymat

# web_f_qiymat(3)


def birinchi_check(changer):
    # k_map = []
    a = changer
    f_main, k_map = k_map_func(changer)
    
    # print(k_map)
    # print(f_main)
    f_item = []
    son = 0
    
    # print('f_oddit =', f_oddiy)
    # son = 0
    f_oddiy = f_oddit_func(a, son)
    # for i in range(2**(a//2+a%2)):
    row = []
    #     for j in range(2**(a-a//2-a%2)):
    #         # bin = onlik_to_biner(son)
    #         # bin = str(10**a+int(bin))
    bin = bin_func(a, k_map)
    print('bin =', bin)
    print('f_oddiy =', f_oddiy)
    print('f_main =', f_main)
    # bin = k_map[i][j]
    for i in range(len(bin)):
        bin_s = bin[i]
        # bin_s = str(10**a+int(bin_s))
        # bin_s = bin_s[1:]
        # print(bin_s)
        row_i, index = find_item(bin_s, f_oddiy)
        print(row_i, index)
        f = int(input(f'F({bin_s}) = '))
        f_main[row_i][index] = f
        # row.append(f)
        # # son+=1
        # f_item.append(row)
    # print(f_item)
    print('f_main', f_main)
    return f_main
from sympy import symbols
from sympy.logic.boolalg import SOPform, POSform


# def karno_jadval()

def web_karno_karto(changer, f_main):
    group = one_index(f_main)
    # A = symbols('A B')
    # print(group)
    mdnf = SOPform(sign_harf(changer), group)
    mdnf = bool_math.mdnsh_to_simple(mdnf)
    mknf = POSform(sign_harf(changer), group)

    mknf = bool_math.mdnsh_to_simple(mknf)
    return mdnf, mknf


def karno_karta(check, changer):
    if check == 1:
        f_main = birinchi_check(changer)
    elif check == 2:
        f_main, words = f_test2.main(changer)
        changer = words
    group = one_index(f_main)
    # A = symbols('A B')
    # print(group)
    mdnf = SOPform(sign_harf(changer), group)
    mknf = POSform(sign_harf(changer), group)
    mdnf = bool_math.mdnsh_to_simple(mdnf)
    mknf = bool_math.mknfh_to_simple(mknf)
    return mdnf, mknf