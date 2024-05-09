"""
URL configuration for money_man project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import path


def my_view(request: HttpRequest):
    return HttpResponse("hello <b>world!</b>")


def birthday_view(request: HttpRequest, name: str, age: int):
    return HttpResponse(f"{name} is {age} years old.")


def hello_view(request: HttpRequest, name: str):
    return HttpResponse(f"hello {name}!")


def color_view(request: HttpRequest, name: str):
    return HttpResponse(f'<body bgcolor="{name}">{name}</body>')


def repeat_view(request: HttpRequest, name: str, times: int):
    return HttpResponse(f"hello {name * times}!")


def numbers_view(request: HttpRequest):
    return JsonResponse({"nums": [1, 2, 3]})


urlpatterns = [
    path("", my_view),
    path("color/<name>/", color_view),
    path("birthday/<name>/<int:age>/", birthday_view),
    path("birthday/<int:age>/<name>/", birthday_view),
    path("old/<name>/", birthday_view, kwargs={"age": 88}),
    path("young/<name>/", birthday_view, kwargs={"age": 18}),
    path("nums/", numbers_view),
    path("hello/<name>/", hello_view),
    path("repeat/<name>/<int:times>/", repeat_view),
    path("admin/", admin.site.urls),
]
