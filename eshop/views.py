import itertools

from django.shortcuts import render, redirect

from eshop_products.models import Product
from eshop_settings.models import SiteSetting
from eshop_slider.models import Slider


# header code behind
def header(request, *args, **kwargs):
    context = {

    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, "shared/Footer.html", context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    most_visited_count = Product.objects.order_by('-visit_count').all()[:8]
    latest_add = Product.objects.order_by('-id').all()[:8]
    context = {
        "data": "new data",
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visited_count),
        'latest': my_grouper(4, latest_add)
    }
    return render(request, "home_page.html", context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, "about_page.html", context)
