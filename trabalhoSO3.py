'''
Trabalho 3: Alocação de Arquivos
Alunos: Davi Wesley e Tayar Santiago

OBS:
não se fez uso de matrizes porque no python não existe, ao invés foram
usadas estruturas de dados mais modernas como dicionarios, listas e listas de listas.
como executar?
'python3 nome.py'

como depurar o código(modo avançado)
'python3 -i nome.py'
'''

def espacosVazios(disco,tam):
    """
    :param disco: Disco a ser lido(lista de lista)
    :param tam: quantidade de espaços em um único bloco
    :return: retorna uma lista com o número dos indexes vazios
    """
    # essa linha usa muitas funçoes avançadas do python
    # ver List Comprehensions 
    # ver função enumarate
    return [i for i, e in enumerate(disco) if e == [i*0 for i in range(tam)]]


def splitWords(word, tam):
    """
    :param word: string para ser lida(uma frase ou palavra)
    :param tam: tamanho da fatia
    :return: retorna uma lista com as palavras fatiadas
    """
    start = 0
    end = tam
    cont = round(len(word)/tam)
    cont += 1 #correçao de um bug aqui pra aumentar mais um espaço
    x = []
    for i in range(0, cont):
        x.append(word[start:end])
        start = end
        end += tam

    return x


def gravar_arquivo(conteudo, nome, disco, tabelaFAT, tabDiretorio, tamBlocos):
    """
    :param conteudo: uma variavel do tipo string
    :param nome: nome do arquivo a ser lido
    :param disco: disco onde se encontra o arquivo
    :tabelaFAT: tabela FAT onde se encontra os indexes
    :tabDiretorio: tabela onde se encontra o nome e o bloco do arquivo
    :tamBlocos: tamanho dos blocos
    :return: imprime na tela as informações encontradas do arquivo
    """
    vazios = espacosVazios(disco,tamBlocos)
    palavras = splitWords(conteudo, 5)
    tabDiretorio[nome] = vazios[0]
    
    for i in range(0, len(palavras)):
        disco[vazios[i]] = palavras[i]
        if (len(palavras)-1) != i:
            tabelaFAT[vazios[i]] = vazios[i+1]
        else:
            tabelaFAT[vazios[i]] = -1

            
def atualizar_arquivo(conteudo, nome, disco, tabelaFAT, tabDiretorio, tamBlocos):
    """
    :param conteudo: uma variavel do tipo string
    :param nome: nome do arquivo a ser lido
    :param disco: disco onde se encontra o arquivo
    :tabelaFAT: tabela FAT onde se encontra os indexes
    :tabDiretorio: tabela onde se encontra o nome e o bloco do arquivo
    :tamBlocos: tamanho dos blocos
    :return: Atualizar o conteudo de um arquio já existente
    """
    vazios = espacosVazios(disco,tamBlocos)
    palavras = splitWords(conteudo, 5)
    lastIndex = getIndexes(nome, tabelaFAT, tabDiretorio)# último index
    lastIndex = lastIndex[-1]
    tabelaFAT[lastIndex] = vazios[0]
    
    for i in range(0, len(palavras)):
        disco[vazios[i]] = palavras[i]
        if (len(palavras)-1) != i:
            tabelaFAT[vazios[i]] = vazios[i+1]
        else:
            tabelaFAT[vazios[i]] = -1

def apagar_arquivo(nome, disco, tabelaFAT, tabDiretorio, tamBlocos):
    """
    :param nome: nome do aquivo
    :param tabelaFAT: tabela FAT onde se encontra o aquivo
    :param tabDiretorio: tabela de diretorios onde encontra o nome e o bloco do arquivo
    :tamBlocos: tamanho dos blocos
    :return: apaga todas as referencias do arquivo(disco,tabela FAT e tabela de diretórios)
    """
    indexes = getIndexes(nome, tabelaFAT, tabDiretorio)
    del tabDiretorio[nome]
    
    for i in range(len(indexes)):
        disco[indexes[i]] = [i*0 for i in range(tamBlocos)]
        tabelaFAT[indexes[i]] = 0
        
        
def getIndexes(nome, tabelaFAT, tabDiretorio):
    """
    :param nome: nome do aquivo
    :param tabelaFAT: tabela FAT onde se encontra o aquivo
    :param tabDiretorio: tabela de diretorios onde encontra o nome e o bloco do arquivo
    """
    bloco = tabDiretorio[nome]
    nextbloco = 0
    arquivo = [bloco]
    while bloco != -1:
        if tabelaFAT[bloco] == -1:
            break
        arquivo.append(tabelaFAT[bloco])
        bloco = tabelaFAT[bloco]

    return arquivo


def criar_tabelaFAT(tamanho):
    """
    :param tamanho: quantidade indexes na tabela
    :return: retorna uma lista preenchidas com 0's
    """
    # essa linha usa muitas funçoes avançadas do python
    # ver List Comprehensions 
    return [i*0 for i in range(tamanho)]


def ler_arquivo(nome, disco, tabela_fat, tabela_diretorio):
    """
    :param nome: Nome do arquivo a ser lido
    :param disco: Qual disco será lido
    :param tabela_fat: tabela FAT para a leitura dos blocos
    :param tabela_diretorio: um dicionario com o nome do arquivo e bloco inicial
    :return: imprime na tela o conteúdo do arquivo
    """
    bloco = tabela_diretorio[nome]
    nextbloco = 0
    arquivo = [bloco]
    while bloco != -1:
        if tabela_fat[bloco] == -1:
            break
        arquivo.append(tabela_fat[bloco])
        bloco = tabela_fat[bloco]

    for i in arquivo:
        print(disco[i])


def criar_disco(n, m):
    """
    :param n: Quantidade de blocos
    :param m: Tamanho dos blocos
    :return: retorna uma lista de uma lista(matriz de duas dimensões)
    """
    a = [[0] * m for i in range(n)]
    return a

#testes
#tabdir = {} # cria uma tabela de diretórios vazia
#disco = criar_disco(10,5)#cria um disco com 10 blocos de tamanho 5
#tabFAT = criar_tabelaFAT(10)# cria uma tabela
#gravar_arquivo("DAVIdCAKEd","teste", disco, tabFAT, tabdir, 5)
#ler_arquivo("teste", disco, tabFAT, tabdir)

TAM_BLOCOS = int(input("Digite a quantidade de blocos"))
TAM_DISCO = int(input("Digite o tamanho do Disco"))
disco = criar_disco(TAM_DISCO,TAM_BLOCOS)
tabelaFAT = criar_tabelaFAT(TAM_DISCO)
tabDiretorio = {}# tabela de diretórios(estrutura de dados usada: dicionario)

opcao = 0
while opcao != 6:
  print('''	[1] Criar aquivo
        [2] Apagar aquivo
        [3] Ler aquivo
        [4] Gravar aquivo
        [5] Inserir conteúdo no final do aquivo
        [6] Sair
        ''')
  opcao = int(input("Qual é sua opção?"))
  if opcao == 1:
    #essa opão eh ignorada ja que as variaveis em python são dinamicas
    pass
  elif opcao == 2:
    nome = str(input("Digite o nome do arquivo"))
    apagar_arquivo(nome, disco, tabelaFAT, tabDiretorio, TAM_BLOCOS)
  elif opcao == 3:
    nome = str(input("Digite o nome do arquivo"))
    ler_arquivo(nome, disco, tabelaFAT, tabDiretorio)
  elif opcao == 4:
    nome = str(input("Digite o nome do arquivo"))
    conteudo = str(input("Digite o conteudo do arquivo"))
    gravar_arquivo(conteudo, nome, disco, tabelaFAT, tabDiretorio, TAM_BLOCOS)
  elif opcao == 5:
    nome = str(input("Digite o nome do arquivo"))
    conteudo = str(input("Digite o conteudo do arquivo"))
    atualizar_arquivo(conteudo, nome, disco, tabelaFAT, tabDiretorio, TAM_BLOCOS)
  elif opcao == 6:
      pass
  else:
      print("Opção inválida. Tente novamente")
  print("==" * 10)
print("Terminou :)")
