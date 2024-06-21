from django.contrib import admin
from .models import Post

#isso vai fazer que os post fiquem acessíveis na área admistrativa
admin.site.register(Post)



