from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Pergunta , Tag , Resposta

def perguntas_recentes(request):

	perguntas = Pergunta.objects.all()
	tags = Tag.objects.all()

	dados = {"perguntas":perguntas,"tags":tags}

	return render(request,'listagem_perguntas.html',dados)

def respostas(request,id_pergunta):

	pergunta = Pergunta.objects.get(pk=id_pergunta)
	respostas = Resposta.objects.filter(pergunta=id_pergunta)
	tags = Tag.objects.all()
	comentarios = pergunta.comentarios.all()

	dados = {"respostas":respostas,
			"pergunta":pergunta,
			"tags":tags,
			"comentarios":comentarios
	}

	return render(request,"listagem_respostas.html",dados)

def excluir_pergunta(request,id_pergunta):

	pergunta = Pergunta.objects.get(pk=id_pergunta)
	pergunta.delete()

	return redirect('index')

def escolher_resposta(request,id_resposta):

	resposta = Resposta.objects.get(pk=id_resposta)
	resposta.mais_util = True
	resposta.save()

	return redirect('index')