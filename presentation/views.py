from django.shortcuts import render
from django.forms import forms

def index(request):
    return render(
        request, "presentation/index.html", {}
    )
def unit0(request):
    return render( 
        request, "presentation/unit0.html"
    )
def overview(request):
    return render( 
        request, "presentation/overview.html"
    )
def search(request):
    return render(
        request, "presentation/search/searchIndex.html"
    )

def advanced(request):
    return render(
        request, "presentation/search/advanced.html"
    )

def image(request):
    return render(
        request, "presentation/search/image.html"
    )

def unit1(request):
    return render(
        request, "presentation/unit1.html"
    )
def unit1more(request):
    return render(
        request, "presentation/unit1more.html"
    )
def unit2(request):
    return render(
        request, "presentation/unit2.html"
    )
def ebay(request):
    return render(
        request, "presentation/ebay.html"
    )
def thanks(request):
    return render(
        request, "presentation/thanks.html"
    )