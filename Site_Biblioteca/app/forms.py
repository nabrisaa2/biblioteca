from django import forms
from .models import Usuario, Livro, Emprestimo

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX', 'maxlength': '14'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX', 'maxlength': '15'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Aqui você pode adicionar uma validação para o CPF, se necessário
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        # Aqui você pode adicionar uma validação para o telefone, se necessário
        return telefone

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'categoria', 'num_copias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),
            'num_copias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Cópias'}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_emprestimo', 'data_devolucao']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'livro': forms.Select(attrs={'class': 'form-control'}),
            'data_emprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
