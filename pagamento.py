# 1. Painel de Controle do Diretor (Feature Flags)
flag_cupom_desconto = True # Ativado: Vamos testar o cupom hoje!
flag_pagamento_pix = False # Desativado: O sistema de PIX ainda está com erros.

# 2. Criando a tela de pagamento do site
def renderizar_tela():
 print("--- TELA DE PAGAMENTO (Compra-Tudo.com) ---")
 valor_compra = 150.00
 print("Valor do produto: R$", valor_compra)
 # Verificando se o campo do cupom deve aparecer (Lógica do Cupom)
 if flag_cupom_desconto == True:
  print("[ NOVO CAMPO ]: Digite seu Cupom de Desconto aqui!")
 # Verificando qual método de pagamento exibir (Lógica do Pagamento)
 if flag_pagamento_pix == True:
  print("[ BOTÃO ]: Pagar com PIX ")
 else:
  print("[ BOTÃO ]: Pagar com Cartão de Crédito ")

# 3. Executando o sistema
renderizar_tela()

