'''
Construa uma função de ordenacao que ordene os alunos por nota. Se houver empate em nota, o nome
deverá definir a ordem

>>> alunos = [('Renzo', 0), ('Luciano', 10), ('Renzo Santos', 10), ('Renzo Nuccitelli', 10)]
>>> import operator
>>> ordernar_por_nota_e_nome = operator.itemgetter(1,0)
>>> alunos.sort(key=ordernar_por_nota_e_nome)
>>> print(alunos)
[('Renzo', 0), ('Luciano', 10), ('Renzo Nuccitelli', 10), ('Renzo Santos', 10)]
>>> print(list(map(ordernar_por_nota_e_nome, alunos)))
>>> [(0, 'Renzo'), (10, 'Luciano'), (10, 'Renzo Nuccitelli'), (10, 'Renzo Santos')]

'''


