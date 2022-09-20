class Pagamento:

    def juros(self, valor, juros):
        return valor * (juros/100)
    
    def desconto(self, preco, desconto):
        return preco - desconto
    
    def parcela(self, preco, parcelas):
        return preco / parcelas