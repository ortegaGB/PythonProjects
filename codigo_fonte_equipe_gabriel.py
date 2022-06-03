"""
Este código foi produzido pela Equipe Gabriel, composta pelos acadêmicos Gabriel Ortega e Gabriel Rezende do curso de Ciência da Computação, UFMS.

"""

#As seguintes funções buscam ler o arquivo texto referido juntamente com este código de modo a extrair
#em colunas os valores de x e y, superiores esquerdo e, x e y inferiores direito, respectivamente em cada
#função com um determinado nome de "chamada"
def xsuperior(): # Definindo o comando de chamada
    f=open("areas_estudadas.txt","r") #Abrindo o arquivo e armanzenando o mesmo em uma variável
    lines=f.readlines()               #Este comando cria uma lista com todas as linhas do arquivo
    result=[]                         #Uma lista inicial pra armazenar o resultado de uma coluna
    for x in lines:                   #A variável x está presente na lista definida anteriormente
        result.append(x.split()[0])   #Este comando une os valores de x na primeira coluna, refer-       
                                      #idos como números "0", o comando split lê os espaços como
                                      #divisórias e toma somente os valores da primeira coluna.
    f.close()                         #Fecha o arquivo, pois nossas ações com ele estão encerradas.
    return list(map(int,result))      #O valor a ser retornado ao chamar pela função, nesse caso, 
                                      #uma lista contendo todos os valores de x superior
#A mesma explicação segue para as outras funções, somente as variáveis e valores de retorno sofrem alterações                                  
def ysuperior():
    f=open("areas_estudadas.txt","r")
    lines=f.readlines()
    result=[]
    for x in lines:
        result.append(x.split()[1])
    f.close()
    return list(map(int,result))
def xinferior():
    f=open("areas_estudadas.txt","r")
    lines=f.readlines()
    result=[]
    for x in lines:
        result.append(x.split()[2])
    f.close()
    return list(map(int,result))
def yinferior():
    f=open("areas_estudadas.txt","r")
    lines=f.readlines()
    result=[]
    for x in lines:
        result.append(x.split()[3])
    f.close()
    return list(map(int,result))
#Para tomar o valor final do retângulo mínimo, é preciso tomar a posição X mais próxima da origem(menor)
#bem como o valor de Y mais próximo da posição X, constatado por nós como o maior dos valores de Y superior.
valor_finalXSE,valor_finalYSE = min(xsuperior()),max(ysuperior())
#Assim como o canto superior esquerdo, é preciso tomar pontos seguindo condições específicas, como se trata
#do lado inferior direito, é preciso buscar pelo maior valor de X e o menor Y, como é o extremo direito, o mais
#distante da origem será ele, bem como o mais próximo da origem em Y (menor).
valor_finalXID,valor_finalYID = max(xinferior()),min(yinferior())

#Por último, é informado a posição final do retângulo que tange todas as áreas de preservação
print("(%i,%i) (%i,%i)" %(valor_finalXSE,valor_finalYSE,valor_finalXID,valor_finalYID))