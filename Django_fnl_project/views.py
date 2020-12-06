from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def practice(request):
    return render(request, 'the_practice.html')


def cleansing(request):
    return render(request, 'nrg_cleansing.html')


def massage(request):
    return render(request, 'nrg-massage.html')
