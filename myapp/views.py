from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import main_karno
# Create your views here.
def index(request):
    return render(request, 'test1.html')

def f_qiymatlar(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(list(request.POST))
        # print(request.POST.get('f_01'))
        f_qiymat_list = list(request.POST)
        f_qiymat_list.remove('csrfmiddlewaretoken')
        changer = len(f_qiymat_list[0][2:])
        # print('changer =', changer)
        f_qiymat_dict = dict(request.POST)
        # print(f_qiymat_dict)
        f_qiymat_dict.pop('csrfmiddlewaretoken')
        # print(f_qiymat_dict)
        
        f_qiymatlari = []
        for item in f_qiymat_list:
            f_qiymatlari.append(int(f_qiymat_dict[item][0]))
        print(f_qiymat_list)
        print(f_qiymatlari)
        f_main, changer_1_qiymat, changer_2_qiymat = main_karno.web_f_qiymat(changer, f_qiymatlari, f_qiymat_list)
        print(f_main)
        print('changer_1_qiymat =', changer_1_qiymat)
        print('changer_2_qiymat =', changer_2_qiymat)
        mdnf, mknf = main_karno.web_karno_karto(changer, f_main)
        # print(mdnf)
        return JsonResponse({
            'mdnf' : mdnf,
            'mknf' : mknf,
            'changer_1_qiymat' : changer_1_qiymat,
            'changer_2_qiymat' : changer_2_qiymat
        })
    return JsonResponse({
        'data':'sa'
    })

def f_qiymat_much(request):
    if request.method == 'POST':
        changer = request.POST.get('changer_son')
        ff_qiymat = main_karno.web_f_qiymatlar(int(changer))
        print('ff_qiymat =', ff_qiymat)
        return JsonResponse({
            'f_qiymat': ff_qiymat
        })
    return JsonResponse({'da':'da'})

def son_input(request):
    if request.method == 'POST':
        f_oddiy = []
        f_oddiy_item = []
        f_qiymat = []
        son_input = request.POST.get('son_input')
        daraja = 0
        binar_str = main_karno.onlik_to_biner(int(son_input))
        while True:
            if 2**daraja >= len(binar_str):
                break
            daraja +=1
        changer = daraja
        f_oddiy_mount = main_karno.f_oddit_func(changer, 0)
        for item in f_oddiy_mount:
            for index in item:
                f_oddiy_item.append(index)
                f_oddiy.append('f_'+index)
        
        if len(binar_str) < 2**changer:
            farq = 2**changer - len(binar_str)
            binar_str = binar_str + '0'*farq
        

        for i in range(len(binar_str)):
            f_qiymat.append(int(binar_str[i]))
        f_main, changer_1_qiymat, changer_2_qiymat = main_karno.web_f_qiymat(changer, f_qiymat, f_oddiy)
        mdnf, mknf = main_karno.web_karno_karto(changer, f_main)
        print(mdnf)
        print(mknf)
        return JsonResponse({
            'mdnf' : mdnf,
            'mknf' : mknf,
            'changer_1_qiymat' : changer_1_qiymat,
            'changer_2_qiymat' : changer_2_qiymat,
            'f_oddiy_mount': f_oddiy_item,
            # 'f_oddiy_mount': f_oddiy_mount,
            'f_qiymat': f_qiymat,
            'menu': '2'
        })
        