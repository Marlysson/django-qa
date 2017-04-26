from django.shortcuts import render
from .models import Pergunta , Tag

def listagem(request):

	perguntas = Pergunta.objects.all()
	tags = Tag.objects.all()

	dados = {"perguntas":perguntas,"tags":tags}

	return render(request,'listagem.html',dados)