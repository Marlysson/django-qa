from django.db import models
from django.conf import settings
import mistune

from .mixins import MixinCriacaoEAlteracao

class Perfil(models.Model):

	usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
	data_nascimento = models.DateField(blank=False,null=False)
	biografia = models.TextField(blank=True)
	avatar = models.ImageField(upload_to="fotos",blank=True,null=True)
	pontos = models.IntegerField(default=0,blank=True,null=True)
	website = models.URLField(blank=True,null=True)

	def __str__(self):
		return self.usuario.username

class Pergunta(MixinCriacaoEAlteracao):

	titulo = models.CharField(max_length=100,blank=False)
	conteudo = models.TextField(blank=False)
	criada_por = models.ForeignKey(Perfil,related_name="minhas_perguntas",on_delete=models.CASCADE)
	up_votes = models.IntegerField(default=0)
	down_votes = models.IntegerField(default=0)
	tags = models.ManyToManyField('Tag')

	@property
	def all_tags(self):
		return [tag for tag in self.tags.all()]

	@property
	def votos(self):
		return self.up_votes - self.down_votes

	@property
	def has_util(self):
		resposta_util = self.respostas.filter(mais_util=True)

		if resposta_util.count() > 0:
			return True
		return False
	
	@property
	def parsed(self):
            return mistune.markdown(self.conteudo)

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
	def is_util(self):
		return self.mais_util
		
	@property
	def votos(self):
		return self.up_votes - self.down_votes

	def __str__(self):
		return "{}".format(self.conteudo)

class Comentario(MixinCriacaoEAlteracao):

	conteudo = models.CharField(max_length=200)
	criado_por = models.ForeignKey(Perfil)
	pergunta = models.ForeignKey(Pergunta,related_name="comentarios",on_delete=models.CASCADE)

	def __str__(self):
		return self.conteudo

class Tag(models.Model):

	nome = models.CharField(max_length=20)

	@property
	def slugfy(self):
		return self.nome.lower().replace(" ","-")

	def __str__(self):
		return self.nome
