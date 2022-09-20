import pytest
from pagamento import Pagamento

class TestPagamento():
    
    def setup_method(self):
        self.pagamento = Pagamento()

    
    def teardown_class(self):
        print('\n teardown')
        
    @pytest.mark.skip()   
    def test_juros(self):
        assert self.pagamento.juros(10,20) == 2
    
    def test_desconto(self):
        assert self.pagamento.desconto(10,1) == 9, "Esperava 3, mas o resultado foi {}".format(self.calc.subtraction(10,1))

    def test_zero_parcela(self):
        with pytest.raises(ZeroDivisionError):
            self.pagamento.parcela(10,0)