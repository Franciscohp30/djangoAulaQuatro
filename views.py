from django.shortcuts import render, redirect
from website.models import Veiculos
from website.form import FormVeiculo


def home(request):
    return render(request, 'website/index.html')


def listaVeiculo(request):
    dados = Veiculos.objects.all()
    return render(request, 'website/listaVeiculo.html' , {'dados': dados})

def cadastraVeiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_listaVeiculo')
    else:
        return render(request,'website/form_veiculo.html', {'form':form , 'acao':'Cadastra' })

def atualizaVeiculo( request, pk):
    veiculo = Veiculos.objects.get(pk=pk)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('url_listaVeiculo')
    else:
        return render(request,'website/form_veiculo.html', {'form':form , 'acao':'Atualiza' })

def deletaVeiculo( request  , pk):
    veiculo = Veiculos.objects.get(pk=pk)
    veiculo.delete()
    return redirect('url_listaVeiculo')
