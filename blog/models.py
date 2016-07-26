#이 곳은 모델을 정의하는 코드입니다. 참고로 모델은 객체입니다.

from django.db import models
from django.utils import timezone

#class는 객체를 정의한다는 것을 의미합니다. 클래스의 첫 글자는 대문자입니다.
#Post는 모델의 이름입니다.
#models.Model은 Post가 django의 model임을 의미합니다. 이로써 장고는 Post가 db에 저장될 것을 알게됩니다.
class Post(models.Model):
	author = models.ForeignKey('auth.User')		#Foreignkey는 다른 모델에 대한 링크를 의미합니다.
	title = models.CharField(max_length=200)	#CharField는 글자 수 제한이 있을 때 사용합니다.
	text = models.TextField()	#TextField는 글자 수 없는 긴 텍스트를 사용할 때 사용합니다.
	created_date = models.DateTimeField(blank=True, null=True)	#날짜와 시간

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title