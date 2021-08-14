from produto.models import produto
from django.shortcuts import render, redirect
from django.http import HttpResponse
from produto.forms import produtoForm

# Create your views here.


def home(request):
    data = {}
    data['db'] = produto.objects.all()
    return render(request, 'produtos/index.html', data)


def form(request):
    data = {}
    data['form'] = produtoForm()
    return render(request, 'produtos/form.html', data)

def create(request):
    form = produtoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")


def edit(request, pk):
    data = {}
    data['db'] = produto.objects.get(pk=pk)
    data['form'] = produtoForm(instance=data['db'])
    return render(request, 'produtos/form.html', data)

def update(request, pk):
    data = {}
    data['db'] = produto.objects.get(pk=pk)
    form = produtoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home') 


def delete(request, pk):
    db = produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = produto.objects.get(pk=pk)
    return render(request, 'produtos/view.html', data)


def table(request):
    data = {}
    data['db'] = produto.objects.all()
    return render(request, 'produtos/table.html', data)