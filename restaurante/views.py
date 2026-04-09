from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Funcionario
from .models import Reserva
from .models import ArtigoBlog

def home(request): #Redirecionamento para página inicial
    return render(request, "index.html")

def blog(request):#Redirecionamento para o blog
    return render(request, "blog.html")

def artigo(request): #Redirecionando para o artigo dentro do blog
    return render(request, "artigo.html")

def sobre(request):
    return render(request, "sobre.html")

def criar_reserva(request):
    if request.method == "POST":
        numero = request.POST.get('numero_pessoas')

        if numero == "5+":
            numero = 5 
        else:
            numero = int(numero)

        Reserva.objects.create(
            nome=request.POST.get('nome'),
            data=request.POST.get('data'),
            hora=request.POST.get('hora'),
            numero_pessoas=numero
        )
    return redirect(request.META.get('HTTP_REFERER', '/'))

def login_funcionario(request): #aqui é a lógica de login
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)

            except  User.DoesNotExist:
                user = None

            if user:
                user = authenticate(request, username=user.username, password=password)

                if user:
                    if not Funcionario.objects.filter(usuario=user).exists():
                        user = None
                    else:
                        login(request, user)
                        return redirect("home")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form}) #Adicionar página de login.html
               
def artigo(request,id):
    artigo = ArtigoBlog.objects.get(id=id)
    return render(request, "artigo.html", {"artigo": artigo})

def blog(request):
    artigos = ArtigoBlog.objects.all()[:4]
    return render(request, "blog.html", {"artigos": artigos})

# Create your views here.
