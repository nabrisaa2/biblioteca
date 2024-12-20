from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Usuario, Livro, Emprestimo
from .forms import UsuarioForm, LivroForm, EmprestimoForm

# Página inicial
def home(request):
    return render(request, 'app/home.html')

# Login de usuário
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial após login
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})

# Logout de usuário
def logout_view(request):
    logout(request)
    return redirect('home')  # Redireciona para a página inicial após logout

# Proteger as páginas de administração para usuários autenticados
@login_required
def gerenciar_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:gerenciar_usuarios')
    else:
        form = UsuarioForm()

    usuarios = Usuario.objects.all()
    context = {'form': form, 'usuarios': usuarios}
    return render(request, 'app/gerenciar_usuarios.html', context)

# Editar usuário
@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app:gerenciar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    
    context = {'form': form, 'usuario': usuario}
    return render(request, 'app/editar_usuario.html', context)

# Excluir usuário
@login_required
def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app:gerenciar_usuarios')
    
    context = {'usuario': usuario}
    return render(request, 'app/excluir_usuario.html', context)

# Gerenciar livros
@login_required
def gerenciar_livros(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:gerenciar_livros')
    else:
        form = LivroForm()

    livros = Livro.objects.all()
    context = {'form': form, 'livros': livros}
    return render(request, 'app/gerenciar_livros.html', context)

# Editar livro
@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('app:gerenciar_livros')
    else:
        form = LivroForm(instance=livro)
    
    context = {'form': form, 'livro': livro}
    return render(request, 'app/editar_livro.html', context)

# Excluir livro
@login_required
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('app:gerenciar_livros')
    
    context = {'livro': livro}
    return render(request, 'app/excluir_livro.html', context)

# Registrar empréstimos
@login_required
def registrar_emprestimos(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:registrar_emprestimos')
    else:
        form = EmprestimoForm()

    emprestimos = Emprestimo.objects.all()
    context = {'form': form, 'emprestimos': emprestimos}
    return render(request, 'app/registrar_emprestimos.html', context)

# Concluir empréstimo
@login_required
def concluir_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if request.method == 'POST':
        emprestimo.status = 'Concluído'
        emprestimo.save()
        return redirect('app:registrar_emprestimos')
    
    context = {'emprestimo': emprestimo}
    return render(request, 'app/concluir_emprestimo.html', context)
