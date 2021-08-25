from produto.models import produto
from django.shortcuts import render, redirect
from django.http import HttpResponse
from produto.forms import produtoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def home(request):
    data = {}
    filter = request.GET.get('filter')
    filterAlf = request.GET.get('filterAlf')
    buscar_data = request.GET.get("buscar_data")
    search = request.GET.get('search')
    
    if search:
        data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
        data['re'] = produto.objects.all().order_by('-editado_em')[:5]        
        data['filter'] = produto.objects.filter(nome__icontains=search)
        paginator = Paginator(data['filter'], 10)
        page = request.GET.get('page')
        data['filter'] = paginator.get_page(page)

    elif filter:
        data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
        data['re'] = produto.objects.all().order_by('-editado_em')[:5]
        data['filter'] = produto.objects.filter(tipo__icontains=filter)
        paginator = Paginator(data['filter'], 10)
        page = request.GET.get('page')
        data['filter'] = paginator.get_page(page)
    elif filterAlf:

        if filterAlf == 'crescente':
            data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
            data['re'] = produto.objects.all().order_by('-editado_em')[:5]
            data["filter"] = produto.objects.all().order_by('nome', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        elif filterAlf == 'recentes':
            data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
            data['re'] = produto.objects.all().order_by('-editado_em')[:5]
            data["filter"] = produto.objects.all().order_by('-data', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        elif filterAlf == 'antigos':
            data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
            data['re'] = produto.objects.all().order_by('-editado_em')[:5]
            data["filter"] = produto.objects.all().order_by('data', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

        else:
            data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
            data['re'] = produto.objects.all().order_by('-editado_em')[:5]     
            data["filter"] = produto.objects.all().order_by('-nome', '-criado_em')
            paginator = Paginator(data['filter'], 10)
            page = request.GET.get('page')
            data['filter'] = paginator.get_page(page)

    elif buscar_data:
        data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
        data['re'] = produto.objects.all().order_by('-editado_em')[:5]        
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


@login_required()
def form(request):
    data = {}
    data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
    data['re'] = produto.objects.all().order_by('-editado_em')[:5]     
    data['form'] = produtoForm()
    return render(request, 'produtos/form.html', data)


@login_required()
def create(request):
    form = produtoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")


@login_required()
def edit(request, pk):
    data = {}
    data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
    data['re'] = produto.objects.all().order_by('-editado_em')[:5]     
    data['db'] = produto.objects.get(pk=pk)
    data['form'] = produtoForm(instance=data['db'])
    return render(request, 'produtos/form.html', data)


@login_required()
def update(request, pk):
    data = {}
    data['db'] = produto.objects.get(pk=pk)
    form = produtoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home') 


@login_required()
def delete(request, pk):
    db = produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')


@login_required()
def view(request, pk):
    data = {}
    data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
    data['re'] = produto.objects.all().order_by('-editado_em')[:5]     
    data['db'] = produto.objects.get(pk=pk)
    return render(request, 'produtos/view.html', data)


@login_required()
def table(request):
    data = {}
    data['rc'] = produto.objects.all().order_by('-criado_em')[:5]
    data['re'] = produto.objects.all().order_by('-editado_em')[:5]    
    data['db'] = produto.objects.all()
    paginator = Paginator(data['db'], 20)
    page = request.GET.get('page')
    data['db'] = paginator.get_page(page)    
    return render(request, 'produtos/table.html', data)
   