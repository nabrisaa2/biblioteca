from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # Importe as views corretas

app_name = 'app'

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Login e Logout
    path('login/', LoginView.as_view(), name='login'),  # Usando LoginView do Django
    path('logout/', LogoutView.as_view(), name='logout'),  # Usando LogoutView do Django

    # Gerenciar Usuários
    path('usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),

    # Gerenciar Livros
    path('livros/', views.gerenciar_livros, name='gerenciar_livros'),
    path('livros/editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('livros/excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),

    # Registrar Empréstimos
    path('emprestimos/', views.registrar_emprestimos, name='registrar_emprestimos'),
    path('emprestimos/concluir/<int:emprestimo_id>/', views.concluir_emprestimo, name='concluir_emprestimo'),
]
