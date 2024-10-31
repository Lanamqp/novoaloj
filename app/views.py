from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.views import View
from .models import Cidade, Curso, Turma, Alojamento, Quarto, Pessoa, Feedback

# View para a página inicial
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse("Formulário enviado com sucesso!")

# View para exibir a página de login
class CadastroView(View):
    template_name = 'cadastro.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect('index')  # Redireciona para a página inicial ou outra página após cadastro
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redireciona para a página inicial ou outra página após login
        return render(request, self.template_name, {'form': form})
# View para exibir a lista de Pessoas
class PessoaView(View):
    template_name = 'pessoa.html'

    def get(self, request):
        pessoas = Pessoa.objects.all()  
        return render(request, self.template_name, {'pessoas': pessoas})
    
    def post(self, request):
        pass

# View para exibir a lista de Cidades
class CidadeView(View):
    template_name = 'cidade.html'

    def get(self, request):
        cidades = Cidade.objects.all()  
        return render(request, self.template_name, {'cidades': cidades})
    
    def post(self, request):
        pass

# View para exibir a lista de Cursos
class CursoView(View):
    template_name = 'curso.html'

    def get(self, request):
        cursos = Curso.objects.all()  
        return render(request, self.template_name, {'cursos': cursos})
    
    def post(self, request):
        pass

# View para exibir a lista de Turmas
class TurmaView(View):
    template_name = 'turmas.html'

    def get(self, request):
        turmas = Turma.objects.all() 
        return render(request, self.template_name, {'turmas': turmas})
    
    def post(self, request):
        pass

# View para exibir a lista de Alojamentos
class AlojamentoView(View):
    template_name = 'alojamentos.html'

    def get(self, request):
        alojamentos = Alojamento.objects.all()  
        return render(request, self.template_name, {'alojamentos': alojamentos})
    
    def post(self, request):
        pass

# View para exibir a lista de Quartos
class QuartoView(View):
    template_name = 'quarto.html'

    def get(self, request):
        quartos = Quarto.objects.all()  
        return render(request, self.template_name, {'quartos': quartos})
    
    def post(self, request):
        pass



class FeedbackView(View):
    def post(self, request):
        data = json.loads(request.body)
        nome = data.get('nome')
        email = data.get('email')
        mensagem = data.get('mensagem')

        # Salva o feedback no banco de dados
        feedback = Feedback.objects.create(nome=nome, email=email, mensagem=mensagem)
        feedback.save()

        return JsonResponse({'status': 'success', 'message': 'Feedback enviado com sucesso!'})


