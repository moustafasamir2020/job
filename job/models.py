from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

JOP_TYPE=(
    ('full time','full time'),
    ('part time','part time'),
)

def upload_image (instance,name):
    image_name,extension = name.split(".")
    return f'jobs/{instance.id}.{extension}'


class job (models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    job_tybe = models.CharField( max_length=50,choices= JOP_TYPE)
    description = models.TextField(max_length=500)
    experience = models.IntegerField(default=1)
    published_at=models.DateField( auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    category = models.ForeignKey("category", on_delete=models.CASCADE,default=2)
    image = models.ImageField( upload_to= upload_image, height_field=None, width_field=None, max_length=None)
    slug=models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title) 
        super(job,self).save(*args, **kwargs)
    



    def __str__(self):
        return self.title
    

class category (models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name
    

class apply(models.Model):
    job = models.ForeignKey(job,related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    website = models.URLField( max_length=200)
    cv = models.FileField( upload_to='apply/')
    cover = models.TextField()
    published = models.DateField( auto_now=True)

    def __str__(self):
        return self.name


