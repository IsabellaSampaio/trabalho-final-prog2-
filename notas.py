#Trabalho final de Programação II
#Aluna: Isabella Sampaio
#Matrícula: 20211BSI0208  
#--------------//--------------

import os 
import pickle

#Função para limpar a tela 
def limpaTela():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")

#--------------//--------------

#Função que salvará as informações no arquivo binário
def salvarInfos(a,n):
	with open ("entrada.bin","wb+") as f:
		pickle.dump(a,f)
		pickle.dump(n,f)

#--------------//--------------

#Função 1 de ordenação: Função responsável por indicar as funções partição e quick sort quais os criterios de ordenação. 
def anterior(x,y, alunos):

	#Definindo variáveis locais

	x1,x2,x3,x4,x5,x6 = x
	y1,y2,y3,y4,y5,y6 = y

	somax = x2 + x3 + x4 + x5
	somay = y2 + y3 + y4 + y5

	#Primeiro critério: Soma total de pontos
	if somax > somay: return True
	if somax < somay : return False

	#Segundo critério: Nota 2 
	if x3 > y3: return True
	if x3 < y3: return False 

	#Terceiro critério: Tempo de execução  
	if x6 < y6: return True
	if x6 > y6:return False

	#Colaca os alunos em ordem alfabética
	if alunos[x1] < alunos[y1]: return True
	return False

#--------------//--------------

#Função 2 de ordenação: Função responsável por ordenar i e j (menores e maiores) de acordo com a função anterior      
def particao(l,inf,sup, alunos):
	pivot = l[inf]
	i = inf+1
	j = sup

	#Andando com i e com j de acordo com o pivot e sua posição 
	while i <= j:
		while i <= j and anterior(l[i], pivot, alunos):
			i+=1
		while j >= i and not anterior(l[j], pivot, alunos):
			j -= 1
		if i < j: l[i], l[j] = l[j], l[i]
	
	#Troca de posição final, para colocar o pivot no lugar certo  		
	l[inf],l[j] = l[j],l[inf]
	return j 

#--------------//--------------

#Função 3 de ordenação: Função responsável por de fato ordenar de acordo com as outras duas   
def quickSort(l,inf,sup, alunos):
	if inf < sup:
		pos = particao(l,inf,sup, alunos)
		quickSort(l,inf,pos-1, alunos)
		quickSort(l,pos+1,sup, alunos)

#--------------//--------------

#Função para inserir alunos
def addAluno(alunos):
	matricula = int(input("INSIRA A MATRÍCULA DO ALUNO: "))
	nome = input("INSIRA O NOME DO ALUNO: ")

	if matricula in alunos:
		print("MATRÍCULA JÁ EXISTE NO SISTEMA.") 
	else:
		alunos[matricula] = nome
	
		print("ALUNO ADICIONADO","\n")

#--------------//--------------

#Função para inserir as notas
def addNotas(notas):
	l = []
	matricula = int(input("INSIRA O NUMERO DA MATRÍCULA: "))
	nota1 = int(input("INSIRA A NOTA 1: "))
	nota2 = int(input("INSIRA A NOTA 2: "))
	nota3 = int(input("INSIRA A NOTA 3: "))
	nota4 = int(input("INSIRA A NOTA 4: "))
	tempExec = int(input("INSIRA O TEMPO DE EXECUÇÃO: "))

	i = 1
	
	notas.append((matricula,nota1,nota2,nota3,nota4,tempExec))
	limpaTela()	
	print(notas)
	print("NOTAS ADICIONADAS","\n")

#--------------//--------------

#Função que chama o quickSort e faz o acréscimo de +2 pontos  
def soma(l,alunos):

	#definindo variavis locais
	n = []
	n2 = []
	i = 0
	sup = (len(l)-1)
	inf = (len(l)-1-sup)
	
	#Chamando a ordenação uma unica vez e logo depois fazendo o acrescimo dos +2 pontos 
	quickSort(l,inf,sup,alunos)
	for i in range (len(l)):

		total = sum(list(l[i][1:5])) 
		n.append(total)
		n2.append(l[i][:1])
		pos = [i[0] for i in n2]

		if n[i] and i <=4:
			print(alunos[pos[i]],"", n[i]+2)
		elif (n[i] == n[4]) and (l[i][2] == l[i-1][2]) and (l[i][5] == l[i-1][5]):
			print(alunos[pos[i]],"", n[i]+2)
		else:
			print(alunos[pos[i]],"", n[i])

	#nota: n e n2 são apenas listas auxiliares 

#--------------//--------------

#Função principal 
def main():

	opcaoUsuario = str
	alunos = {}
	notas = []	
	
	
	menu = '''\nOLÁ, VOCÊ ENTROU NO SISTEMA.\n
DIGITE 1 PARA VISUALIZAR AS NOTAS.
->: '''
	
	#Lendo o que tem dentro do arquivo  
	if os.path.isfile("entrada.bin"):
		with open("entrada.bin","rb") as f:
			alunos = pickle.load(f)
			notas = pickle.load(f)
	
	opcaoUsuario = input(menu)
	limpaTela()

	if opcaoUsuario == "1": 
		print("AS NOTAS SÃO:","\n")
		soma(notas,alunos)

	else:
		print("OPÇÃO INVALIDA. TENTE NOVAMENTE.") 
		opcaoUsuario = input(menu)		

	#while opcaoUsuario != "3":
		#if opcaoUsuario == "1":
			#addAluno(alunos)
		#elif opcaoUsuario == "2":
			#addNotas(notas)
		#menu='''DESEJA ADICIONAR MAIS NOTAS E/OU ALUNOS? 
#DIGITE 1 PARA ADICIONAR + ALUNOS, 2 PARA ADICIONAR + NOTAS OU 3 CASO QUEIRA SAIR
#: '''	
		#opcaoUsuario= input(menu)
	#limpaTela()

	#Salvando no arquivo e printando a lista ordenada de alunos e seus correspondentes pontos   	
	salvarInfos(alunos,notas)
		


#Fim da função principal e do programa
if __name__=='__main__':
    main()