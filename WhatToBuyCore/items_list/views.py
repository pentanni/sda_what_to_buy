from django.shortcuts import render
from django.http import HttpResponse
from.models import ShoppingList


def hello(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request,"shopping_list.html", context={"list" : shopping_lists})


def hello2(request):
    anything = request.GET.get("situation")
    return HttpResponse(f'<h1>Potato Wars are {anything}?</h1>')

