
from django.db import models

class MixinCriacaoEAlteracao(models.Model):

	criado_em = models.DateTimeField(auto_now_add=True)
	modificado_em = models.DateTimeField(auto_now=True)	

	class Meta:
		abstract = True