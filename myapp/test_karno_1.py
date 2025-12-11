from . import main_karno

def main():

    print("1. F qiymatlarni qo'lda kiritish.\n2.Misol orqali kiritish.3.Chiqish")
    check = int(input('Tanlang_: '))
    if check==1:
        print("Nechta o'garuvchili bo'lsin.(Son)")
        son = int(input('Qiymat_: '))
        a = main_karno.karno_karta(check, son)
        print(a)
    elif check == 2:
        # print("Nechta o'garuvchili bo'lsin.(Son)")
        # son = int(input('Qiymat_: '))
        print("Misol yozing.(AB' yoki A*B yokida A+B'A')")
        misol_text = str(input('Misol_: '))
        a = main_karno.karno_karta(check, misol_text)
        print(a)
    else:
        return
    return main()
main()

