from django.contrib import admin
from .models import *

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass

@admin.register(Pergunta)
class Pergunta(admin.ModelAdmin):
	list_display = ['titulo','get_tags']

	def get_tags(self,obj):
		return obj.all_tags

@admin.register(Resposta)
class Resposta(admin.ModelAdmin):
	pass

@admin.register(Comentario)
class Comentario(admin.ModelAdmin):
	pass