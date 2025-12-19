'''
Funcão principal que irá realizar a chamada dos arquivos .py

Caso de Uso - Automatizando a captura dos dados dos CNPJs de empresas através do site da receita

https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/Cnpjreva_Comprovante.asp.

'''

# Função comprimentar que recebe o argumento msg
def comprimentar(msg):
    print(msg)


# Sempre que for rodar um arquivo no python esse é o padrão de chamada
# por exemplo: Aqui estamos dentro do arquivo main.py, então logo:
# chamamos if="se" depois __name__ aqui automaticamente você está verificando se é o arquivo main.py
# E depois usamos == pois é assim no python para comparar duas variaveis, argumentos, parametros se são iguais.
# e por fim usamos '__main__': que é uma função, se você clicar com botão direito segurando o ctrl em cima 
# vai abrir algo parecido com "def __getattr__(name: str): ...  # incomplete module", que recebe o atributo
# e sabe exatamente qual arquivo chamar no modo debug.
# e dentro temos a variavels msg="Hello World", = é para atribuir a string "Hello World" à variável msg
# depois chamamos a função que queremos que é comprimentar e dentro dos parenteses passamos a variavel 
# msg dentro de parenteses.

if __name__ == '__main__':
    msg="Hello World"
    comprimentar(msg)


