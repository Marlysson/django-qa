from django.db import models
from django.conf import settings

from .mixins import MixinCriacaoEAlteracao

class Perfil(models.Model):

	usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
	data_nascimento = models.DateField(blank=False,null=False)
	biografia = models.TextField(blank=True)
	avatar = models.ImageField(upload_to="fotos",blank=True,null=True)
	pontos = models.IntegerField(default=0,blank=True,null=True)
	website = models.URLField(blank=True,null=True)

	def __str__(self):
		return self.username

class Pergunta(MixinCriacaoEAlteracao):

	titulo = models.CharField(max_length=100,blank=False)
	conteudo = models.TextField(blank=False)
	criada_por = models.ForeignKey(Perfil,related_name="minhas_perguntas",on_delete=models.CASCADE)
	up_votes = models.IntegerField(default=0)
	down_votes = models.IntegerField(default=0)
	tags = models.ManyToManyField('Tag')

	@property
	def votos(self):
		return abs(self.up_votes - self.down_votes)

	def up_vote(self):
		self.up_votes += 1
		self.save()

	def down_vote(self):
		self.down_vote += 1
		self.save()

	def __str__(self):
		return "{} , {}".format(self.titulo,self.tags)

class Resposta(MixinCriacaoEAlteracao):

	conteudo = models.TextField(blank=False)
	criada_por = models.ForeignKey(Perfil,related_name="minhas_respostas",on_delete=models.CASCADE)
	up_votes = models.IntegerField(default=0)
	down_votes = models.IntegerField(default=0)
	mais_util = models.BooleanField(default=False)
	pergunta = models.ForeignKey(Pergunta,related_name="respostas",on_delete=models.CASCADE)

	@property
	def votos(self):
		return abs(self.up_votes - self.down_votes)

	def __str__(self):
		return "{}".format(self.conteudo)

class Comentario(MixinCriacaoEAlteracao):

	conteudo = models.CharField(max_length=200)
	criado_por = models.ForeignKey(Perfil)
	pergunta = models.ForeignKey(Pergunta,related_name="comentarios",on_delete=models.CASCADE)

class Tag(models.Model):

	nome = models.CharField(max_length=20)

	def __repr__(self):
		return self.nome
