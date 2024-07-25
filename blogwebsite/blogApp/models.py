from django.db import models

# Create your models here.

class BlogDetail(models.Model):
  blog_id = models.AutoField(primary_key=True)
  blog_title = models.CharField(max_length=50)
  blog_desc = models.CharField(max_length=250)
  blog_date=models.DateField()
  class Meta:
      db_table = "BlogTable"

class Blogreviews(models.Model):
   blog_id = models.AutoField(primary_key=True)
   blog_review_title = models.CharField(max_length=50)
   blog_review_desc = models.CharField(max_length=250)
   blog_review_date=models.DateField()
   class Meta:
      db_table = "BlogReviewTable"