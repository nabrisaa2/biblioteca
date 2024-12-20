from django.contrib import admin
from .models import Usuario, Livro, Emprestimo  # Importe seus modelos

# Registre os modelos para que eles apareçam no admin
admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Emprestimo)
