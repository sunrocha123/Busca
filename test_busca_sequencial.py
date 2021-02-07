import busca_sequencial
import pytest

class Test:

    @pytest.mark.parametrize("lista, elemento, resposta_esperada", [
        ([1,'a',78,-9,'bala'],'ovo', False),
        ([1,3,4,5,6,7,'ovo'],4, 2),
        (['Judson','Antonio','Fabio','Pedro'],'judson', False),
        (['99',100,102,'000'],'000', 3)
    ])
    def test(self, lista, elemento, resposta_esperada):
        assert busca_sequencial.busca(lista, elemento) == resposta_esperada