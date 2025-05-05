from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro

# Inline para o modelo Livro, permitindo a edição de livros diretamente no formulário do Autor
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  # Número de livros adicionais para adicionar no admin (você pode ajustar esse valor)

# Admin do modelo Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos que serão exibidos na listagem
    search_fields = ('nome',)  # Campos que serão pesquisados no admin
    # Remover a linha abaixo se você não quer livros no formulário de Autor
    inlines = [LivroInline]  # Adiciona a tabela de livros no admin de autores (se desejado)

# Admin do modelo Livro
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'preco', 'data_pub', 'status')  # Campos exibidos no admin
    search_fields = ('nome', 'autor__nome')  # Pesquisa no nome do livro e no nome do autor
    list_filter = ('autor', 'editora', 'genero')  # Filtros para facilitar a busca por autor, editora e gênero

# Registrando os modelos no admin
admin.site.register(Cidade)
admin.site.register(Autor, AutorAdmin)  # Registra o Autor com a customização de AutorAdmin
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
admin.site.register(Livro, LivroAdmin)  # Registra o Livro com a customização de LivroAdmin
