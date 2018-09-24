from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Pedro', 'idade': 21},
        {'nome': 'Joaquim', 'idade': 22}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    return {'nome': 'Não encotrado',  'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' +str(result['idade']) + ' anos')
    else:
        return HttpResponse(result['nome'])

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})

