from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


        
class Company(models.Model):
	name = models.CharField(max_length=200, db_index=True, verbose_name="Наименование организации")
	inn = models.CharField(max_length=200, db_index=True, verbose_name = "ИНН-КПП")
	created = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")
	updated = models.DateTimeField(auto_now=True, verbose_name = "Дата изменения")
	class Meta:
		verbose_name = 'Организацию'
		verbose_name_plural = 'Организация'
	def __str__(self):
		return self.name	

class Price(models.Model):
	name = models.CharField(max_length=200, db_index=True, verbose_name="Услуга")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена услуги")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	description = models.TextField(blank=True, verbose_name="Описание")
	
	class Meta:
		verbose_name = 'Услугу'
		verbose_name_plural = 'Прайс'
	def __str__(self):
		return self.name
	
class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	
	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
        
class Type(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	
	class Meta:
		verbose_name = 'Тип услуги'
		verbose_name_plural = 'Тип услуги'
	def __str__(self):
		return self.name
        
class Kkt(models.Model):
	name = models.CharField(max_length=20, db_index=True)
	our = models.BooleanField(verbose_name="Наша ККТ")
	def __str__(self):
		return self.name
        
        
class Job(models.Model):
	CLOSE = "CL"
	OPEN = "OP"
	NEW = "NW"
	ERROR = "ER"
	APPOINTED = "AD"
	STATUS_CHOICES = (
	(CLOSE,'Закрыт'),
	(OPEN,'Открыт'),
	(NEW,'Новый'),
	(ERROR,'Отказ'),
	(APPOINTED,'Назначен'),
	)
	name_company = models.ForeignKey(Company,related_name='name_company', on_delete=models.PROTECT,verbose_name='Организация',default=None, blank=True, null=True)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES,default=NEW,verbose_name='Статус')
	responsible = models.ForeignKey(User,related_name='user', on_delete=models.PROTECT,verbose_name='Ответственный',default=None, blank=True, null=True)
	#inn = models.CharField(max_length=20, db_index=True,verbose_name='ИНН')
	incident = models.IntegerField(default=0)
	bill = models.CharField(max_length=20, db_index=True)
	created = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
	updated = models.DateTimeField(auto_now=True,verbose_name='Дата изменение')
	price = models.ManyToManyField(Price,)
	slug = models.SlugField(max_length=200, db_index=True,default=None, blank=True, null=True)
	available = models.BooleanField(default=True, verbose_name="Доступен")
	description = models.TextField(max_length=2000, db_index=True,verbose_name='Комментарий')
	created_user = models.ForeignKey('auth.User',on_delete=models.PROTECT,verbose_name='Создал')
	docfile = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	typez = models.ForeignKey(Type, on_delete=models.PROTECT)
	close_date = models.DateField(default=None, blank=True, null=True)
	kkt = models.ForeignKey(Kkt, on_delete=models.PROTECT)
	class Meta:
		verbose_name = 'Работу'
		verbose_name_plural = 'Работы'
		
	def get_absolute_url(self):
		return reverse('api.job:my_job_id', args=[self.id])
		
		

	

class Description(models.Model):
	user_name = models.ForeignKey(User,related_name='user_comment', on_delete=models.PROTECT)
	comment = models.TextField(blank=True)
	data_comment = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
	comment_job = models.ForeignKey(Job,related_name='comment_job',on_delete=models.PROTECT)
