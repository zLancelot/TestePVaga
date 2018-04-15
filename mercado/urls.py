from django.conf.urls import url
from mercado.views import home, vendas, salvar_venda, clientes_compras

urlpatterns = [
    url(r'^$', home),
    url(r'^vendas_mes/$', vendas),
    url(r'^clientes_compras/', clientes_compras),
    url(r'^vender/$', salvar_venda)
];