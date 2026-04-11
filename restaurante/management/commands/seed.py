from django.core.management.base import BaseCommand
from restaurante.models import ArtigoBlog, Destaque, Reserva
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Popula o banco com dados iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write('Limpando dados antigos...')
        ArtigoBlog.objects.all().delete()
        Destaque.objects.all().delete()
        Reserva.objects.all().delete()

        self.stdout.write('Criando destaques...')
        Destaque.objects.create(
            titulo="Chef's capacitados",
            descricao="Nossa equipe de chef's especializados criam pratos únicos com técnicas refinadas.",
            ordem=1
        )
        Destaque.objects.create(
            titulo="Vantagens do local",
            descricao="Bem localizado e altamente confortável, aconchegante para você e sua família.",
            ordem=2
        )
        Destaque.objects.create(
            titulo="Premiações",
            descricao="Reconhecido por diversas revistas gastronômicas e críticos renomados.",
            ordem=3
        )
        Destaque.objects.create(
            titulo="Horários",
            descricao="Aberto todos os dias com horários estendidos. De 13h às 22h.",
            ordem=4
        )

        self.stdout.write('Criando artigos do blog...')
        ArtigoBlog.objects.create(
            titulo="Os segredos da massa italiana",
            trecho="Descubra os segredos por trás da massa perfeita e as técnicas dos grandes chefs.",
            primeiro_paragrafo="A culinária italiana é conhecida mundialmente por sua simplicidade e sabor marcante. A massa é um dos seus maiores símbolos, feita tradicionalmente com poucos ingredientes.",
            segundo_paragrafo="O segredo está na qualidade dos ingredientes e no tempo de preparo. Cada região da Itália tem sua própria receita tradicional passada de geração em geração.",
            citacao1="A simplicidade é a sofisticação máxima na culinária italiana.",
            autor="Lucas Fernandes",
            data_publicacao=datetime.date(2026, 3, 10)
        )
        ArtigoBlog.objects.create(
            titulo="A Importância dos Ingredientes Naturais",
            trecho="Como os ingredientes naturais transformam um prato comum em uma experiência gastronômica.",
            primeiro_paragrafo="Ingredientes frescos e naturais fazem toda a diferença no resultado final de um prato. A escolha certa começa na feira e no mercado.",
            segundo_paragrafo="Chefs renomados ao redor do mundo defendem o uso de produtos locais e sazonais para garantir sabor e qualidade.",
            citacao1="Cozinhar bem começa com escolher bem.",
            autor="Beatriz Nunes",
            data_publicacao=datetime.date(2026, 3, 8)
        )
        ArtigoBlog.objects.create(
            titulo="Sobremesas: A arte do sabor",
            trecho="As sobremesas são a parte mais criativa da gastronomia. Conheça as técnicas dos grandes pâtissiers.",
            primeiro_paragrafo="A confeitaria é considerada a parte mais técnica e artística da gastronomia. Cada detalhe importa, do ponto do caramelo à temperatura do chocolate.",
            segundo_paragrafo="As sobremesas francesas influenciaram o mundo inteiro, mas cada cultura adaptou as técnicas ao seu próprio paladar.",
            citacao1="Uma boa sobremesa é a memória mais doce de uma refeição.",
            autor="Camila Duarte",
            data_publicacao=datetime.date(2026, 3, 1)
        )
        ArtigoBlog.objects.create(
            titulo="O Segredo: Vinhos e Pratos",
            trecho="A harmonização de vinhos e pratos é uma arte que eleva qualquer refeição a outro nível.",
            primeiro_paragrafo="Harmonizar vinho com comida é uma das habilidades mais valorizadas na gastronomia. A combinação certa pode transformar uma refeição simples em algo memorável.",
            segundo_paragrafo="Vinhos tintos encorpados combinam com carnes vermelhas, enquanto brancos frescos acompanham peixes e frutos do mar.",
            citacao1="O vinho certo transforma uma refeição em uma experiência.",
            autor="Ricardo Almeida",
            data_publicacao=datetime.date(2026, 3, 5)
        )

        self.stdout.write('Criando reservas de exemplo...')
        Reserva.objects.create(
            nome="Maria Silva",
            data=datetime.date(2026, 4, 15),
            hora=datetime.time(19, 0),
            numero_pessoas=2
        )
        Reserva.objects.create(
            nome="João Santos",
            data=datetime.date(2026, 4, 16),
            hora=datetime.time(20, 30),
            numero_pessoas=4
        )

        self.stdout.write(self.style.SUCCESS('Seed concluída com sucesso!'))