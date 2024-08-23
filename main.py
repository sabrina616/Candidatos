def candidato1():
    print ('nome: João')
    print('vice: Maria')
    print('partido: PG')
    print('cargos: Deputado Federal, Governador(a)')
def candidato2():
    print('nome: Kuan')
    print('vice: José')
    print('partido: PP')
    print('cargos: Deputado Estadual, Deputado Federal')
def candidato3():
    print('nome: Renan')
    print('vice: Jair')
    print('partido: PT')
    print('cargos: Prefeito(a), Presidente')
def candidato4():
    print('nome: Liz')
    print('vice: Laura')
    print('partido: LL')
    print('cargos: Governador(a), Presidente')
def candidato5():
    print('nome: Loro')
    print('vice: Lucas')
    print('partido: JBL')
    print('cargos: Governador(a), Deputado Estadual')
def candidato6():
    print('nome: Paulo')
    print('vice: Antônio')
    print('partido: CC')
    print('cargos: Presidente, Prefeito')
def candidato7():
    print('nome: Salomão')
    print('vice: Filomena')
    print('partido: JP')
    print('cargos: Presidente, Prefeito(a)')
def candidato8():
    print('nome: Luís')
    print('vice: Maria Antonieta')
    print('partido: MF')
    print('cargos: Presidente, Prefeito')
switch = {
    1:candidato1,
    2:candidato2,
    3:candidato3,
    4:candidato4,
    5:candidato5,
    6:candidato6,
    7:candidato7,
    8:candidato8
  }
entrada=int(input('Digite o número do candidato: '))
switch.get(entrada, candidato4) ()


    