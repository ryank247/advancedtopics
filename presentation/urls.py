from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("unit0", views.unit0, name="unit0"),
    path("unit1", views.unit1, name="unit1"),
    path("unit1more", views.unit1more, name="unit1more"),
    path("unit2", views.unit2, name="unit2"),
    path("overview", views.overview, name="overview"),
    path("ebay", views.ebay, name="ebay"),
    path("thanks", views.thanks, name="thanks"),
    path("search",views.search,name="search"),
    path("image",views.image,name="image"),
    path("advanced",views.advanced,name="advanced"),
]