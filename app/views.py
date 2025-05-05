from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'index.html', {'livros': livros})


class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})


class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})


class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})


class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = Livro.objects.get(id=id)
        livro.delete()
        messages.success(request, 'Livro excluído comsucesso!') # Success message
        return redirect('livros') 
    
class EditarLivroView(View):
    template_name = 'editar_livro.html'

    def get(self, request, id, *args, **kwargs):
        # Recupera o livro ou retorna 404 se não encontrado
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(instance=livro)  # Cria um formulário preenchido com o livro existente
        return render(request, self.template_name, {'livro': livro, 'form': form})

    def post(self, request, id, *args, **kwargs):
        # Recupera o livro ou retorna 404 se não encontrado
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(request.POST, instance=livro)  # Preenche o formulário com os dados enviados pelo POST
        
        if form.is_valid():
            form.save()  # Salva as edições feitas no livro
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect('editar', id=id)  # Redireciona para a página de edição do livro (evita resubmissão do formulário)
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'livro': livro, 'form': form})  # Retorna o formulário com erros para o usuário corrigir
