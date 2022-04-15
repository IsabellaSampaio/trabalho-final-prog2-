#Trabalho final de Programação II
#Aluna: Isabella Sampaio
#--------------//--------------

import os 
import pickle

def limpaTela():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")



def salvarInfos(a,n):
	with open ("entrada.bin","wb+") as f:
		pickle.dump(a,f)
		pickle.dump(n,f)




def anterior(x,y, alunos):


	x1,x2,x3,x4,x5,x6 = x
	y1,y2,y3,y4,y5,y6 = y

	somax = x2 + x3 + x4 + x5
	somay = y2 + y3 + y4 + y5

	
	if somax > somay: return True
	if somax < somay : return False

	 
	if x3 > y3: return True
	if x3 < y3: return False 

	
	if x6 < y6: return True
	if x6 > y6:return False

	
	if alunos[x1] < alunos[y1]: return True
	return False
  
def particao(l,inf,sup, alunos):
	pivot = l[inf]
	i = inf+1
	j = sup

	 
	while i <= j:
		while i <= j and anterior(l[i], pivot, alunos):
			i+=1
		while j >= i and not anterior(l[j], pivot, alunos):
			j -= 1
		if i < j: l[i], l[j] = l[j], l[i]
	
	 		
	l[inf],l[j] = l[j],l[inf]
	return j 


def quickSort(l,inf,sup, alunos):
	if inf < sup:
		pos = particao(l,inf,sup, alunos)
		quickSort(l,inf,pos-1, alunos)
		quickSort(l,pos+1,sup, alunos)



def addAluno(alunos):
	matricula = int(input("INSIRA A MATRÍCULA DO ALUNO: "))
	nome = input("INSIRA O NOME DO ALUNO: ")

	if matricula in alunos:
		print("MATRÍCULA JÁ EXISTE NO SISTEMA.") 
	else:
		alunos[matricula] = nome
	
		print("ALUNO ADICIONADO","\n")



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


  
def soma(l,alunos):

	
	n = []
	n2 = []
	i = 0
	sup = (len(l)-1)
	inf = (len(l)-1-sup)
	
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


def main():

	opcaoUsuario = str
	alunos = {}
	notas = []	
	
	
	menu = '''\nOLÁ, VOCÊ ENTROU NO SISTEMA.\n
DIGITE 1 PARA VISUALIZAR AS NOTAS.
->: '''
	
	
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

	
	salvarInfos(alunos,notas)
		


if __name__=='__main__':
    main()
