from django.shortcuts import render, redirect
from .models import ArtigoBlog, Reserva, Destaque

def home(request):
    destaques = Destaque.objects.all()
    return render(request, 'index.html', {'destaques': destaques})

def blog(request):
    artigos = ArtigoBlog.objects.all()[:4]
    return render(request, 'blog/blog.html', {'artigos': artigos})

def artigo(request, id):
    artigo = ArtigoBlog.objects.get(id=id)
    return render(request, 'blog/artigo.html', {'artigo': artigo})

def sobre(request):
    return render(request, 'sobre.html')

def criar_reserva(request):
    if request.method == 'POST':
        numero = request.POST.get('numero_pessoas')

        if numero == '5+':
            numero = 5
        else:
            numero = int(numero)

        Reserva.objects.create(
            nome=request.POST.get('nome'),
            data=request.POST.get('data'),
            hora=request.POST.get('hora'),
            numero_pessoas=numero
        )
    return redirect('home')