from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta():
        db_table = 'category'
    category_title = models.CharField(verbose_name='', max_length=50)

class Head(models.Model):
    class Meta():
        db_table = 'head'
    head_title = models.CharField(verbose_name='', max_length=50)
    head_category = models.ForeignKey(Category)

class BodyText(models.Model):
    class Meta():
        db_table = 'body'
    body_text = models.TextField()
    body_text_head = models.ForeignKey(Head)