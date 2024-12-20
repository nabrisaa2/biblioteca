from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from datetime import date

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="CPF",
        validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF inválido. Formato: 000.000.000-00")]
    )
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(
        max_length=15,
        verbose_name="Telefone",
        validators=[RegexValidator(regex=r'^\(\d{2}\) \d{4,5}-\d{4}$', message="Telefone inválido. Formato: (XX) XXXXX-XXXX")]
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Livro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="ISBN",
        validators=[RegexValidator(regex=r'^\d{13}$', message="ISBN inválido. Deve conter 13 dígitos.")]
    )
    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    num_copias = models.IntegerField(
        verbose_name="Número de cópias",
        validators=[MinValueValidator(0, message="O número de cópias não pode ser negativo.")]
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    data_emprestimo = models.DateField(verbose_name="Data do empréstimo")
    data_devolucao = models.DateField(verbose_name="Data da devolução")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente', verbose_name="Status")

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.data_devolucao <= self.data_emprestimo:
            raise ValidationError("A data de devolução deve ser posterior à data de empréstimo.")

    def __str__(self):
        return f"{self.usuario.nome} - {self.livro.titulo}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
