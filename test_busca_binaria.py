import pytest
import busca_binaria

lista = [10,20,30,40,50]

@pytest.mark.parametrize("lista, valor, resposta_esperada",[
    (a,10,0),
    (a,20,1),
    (a,30,2),
    (a,40,3),
    (a,50,4),
    (a,60,False),
    (a,25, False),
    (a,-20,False)
])
def testa_busca_binaria(lista, valor, resposta_esperada):
    assert busca_binaria.busca_binaria(lista, valor) == resposta_esperada