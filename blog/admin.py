from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)	#관리자 페이지에서 직접만든 Post 모델을 보려면 추가해야함.