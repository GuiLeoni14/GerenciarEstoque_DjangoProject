from produto.models import produto
from django.shortcuts import render, redirect
from django.http import HttpResponse
from produto.forms import produtoForm
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    data = {}
    filter = request.GET.get('filter')
    filterAlf = request.GET.get('filterAlf')
    buscar_data = request.GET.get("buscar_data")
    search = request.GET.get('search')
    
    if search:
        data['filter'] = produto.objects.filter(nome__icontains=search)
        paginator = Paginator(data['filter'], 10)
        page = request.GET.get('page')
        data['filter'] = paginator.get_page(page)

    elif filter:
        data['filter'] = produto.objects.filter(tipo__icontains=filter)
        paginator = Paginator(data['filter'], 10)
        page = request.GET.get('page')
        data['filter'] = paginator.get_page(page)
    elif filterAlf:

        if filterAlf == 'crescente':
            data["filter"] = produto.objects.all().order_by('nome', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        elif filterAlf == 'recentes':
            data["filter"] = produto.objects.all().order_by('-data', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        elif filterAlf == 'antigos':
            data["filter"] = produto.objects.all().order_by('data', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        else:
            data["filter"] = produto.objects.all().order_by('-nome', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

    elif buscar_data:
        data["filter"] = produto.objects.filter(data__icontains=buscar_data)
        paginator = Paginator(data['filter'], 10)
        page = request.GET.get('page')
        data['filter'] = paginator.get_page(page)

    else:
        data['db'] = produto.objects.all().order_by('-criado_em')
        data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
        data['re'] = produto.objects.all().order_by('-editado_em')[:5]
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

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
   