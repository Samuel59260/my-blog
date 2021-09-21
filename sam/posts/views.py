from django.shortcuts import render
# Create your views here.

from django.http import JsonResponse


def my_view(request):
    # View code here...
    print('salut')
    return JsonResponse({'key': 'salope'})

def my_new(resquest):
    print(resquest)
    dico = {'key': 'value'}
    print(dico['key'])
    return JsonResponse(dico)