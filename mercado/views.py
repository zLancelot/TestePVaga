from django.shortcuts import render, redirect
from mercado.models import Vendedor, Venda, Cliente, Produto
from mercado.forms import VendaForm
import json
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'mercado/index.html')



def vendas(request):
    vendas = Venda.objects.all()

    ## Pega data do sistema
    now = datetime.now()

    meses = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho",
             8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

    dic_vendas = {}
    for venda in vendas:
        ## Compara o mês atual com o da informação que está no banco
        if int(venda.data_venda.strftime("%d/%m/%y")[3:5]) == now.month:
            try:
                dic_vendas[str(venda.id_vendedor.nome)] +=1
            except:
                dic_vendas[str(venda.id_vendedor.nome)] = 1

    ## Data dos dados: [str(vendas[0].data_venda)]



    context = {
        'nomes' : json.dumps(list(dic_vendas.keys())),
        'qtd_vendas': json.dumps(list(dic_vendas.values())),
        'mes': meses[now.month],
    }


    return render(request, 'mercado/vendas_mes.html', context)


def salvar_venda(request):
    clientes = Cliente.objects.order_by('nome')
    produtos = Produto.objects.order_by('descricao')
    vendedores = Vendedor.objects.order_by('nome')


    if request.method == 'POST':
        form = VendaForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.data_venda = datetime.now()

            for cliente in clientes:
                if cliente.id == request.POST.get("id_client"):
                    post.id_cliente = cliente

            for vendedor in vendedores:
                if vendedor.id == request.POST.get("id_vendedor"):
                    post.id_vendedor = vendedor

            for produto in produtos:
                if produto.id == request.POST.get("id_produto"):
                    post.id_produto == produto

            post.save()
            return redirect(vendas)

    context = {
        'vendedores': vendedores,
        'produtos': produtos,
        'clientes': clientes
    }

    return render(request, 'mercado/vender.html', context)

def clientes_compras(request):
    vendas = Venda.objects.all()
    produtos = Produto.objects.all()

    produto_comprado = ""

    if request.method == "POST":
        id_produto = request.POST.get("id_produto")

        for produto in produtos:
            if produto.id == int(id_produto):
                produto_comprado = produto.descricao

    else:
        id_produto = 0

    dic_compras = {}
    nao_tem_items = True

    for venda in vendas:
        if venda.id_produto.id == int(id_produto):
            try:
                dic_compras[str(venda.id_cliente.nome)] +=1
            except:
                dic_compras[str(venda.id_cliente.nome)] = 1
            nao_tem_items = False

    context = {
        'nomes' : json.dumps(list(dic_compras.keys())),
        'qtd_compras': json.dumps(list(dic_compras.values())),
        'produtos': produtos,
        'nao_tem_item': nao_tem_items,
        'produto_comprado': produto_comprado,
    }

    return render(request, 'mercado/clientes_compras.html', context)
