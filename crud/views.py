from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import emp
from .models import employee

# Create your views here.

# created and showed
def reg(request):
    if request.method == "POST":
        fm = emp(request.POST)
        if fm.is_valid():
            print("post request")
            fm.save()
            fm = emp()
            return HttpResponseRedirect("/")
    else:
        fm = emp()
    std = employee.objects.all()
    return render(request, "crud/crud.html", {"fm": fm, "std": std})


def update(request, id):
    if request.method == "POST":
        pm = employee.objects.get(pk=id)
        fm = emp(request.POST, instance=pm)
        if fm.is_valid():
            fm.save()
    else:
        pm = employee.objects.get(pk=id)
        fm = emp(instance=pm)
    return render(request, "crud/update.html", {"fm": fm})


def deleted(request, id):
    if request.method == "POST":
        di = employee.objects.get(pk=id)
        di.delete()
        return HttpResponseRedirect("/")
