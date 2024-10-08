from django.db import models

# Create your models here.

JOP_TYPE=(
    ('full time','full time'),
    ('part time','part time'),
)

def upload_image (instance,name):
    image_name,extension = name.split(".")
    return f'jobs/{instance.id}.{extension}'


class job (models.Model):
    title = models.CharField( max_length=100)
    job_tybe = models.CharField( max_length=50,choices= JOP_TYPE)
    description = models.TextField(max_length=500)
    experience = models.IntegerField(default=1)
    published_at=models.DateField( auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    category = models.ForeignKey("category", on_delete=models.CASCADE,default=2)
    job_image = models.ImageField( upload_to= upload_image, height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.title
    

class category (models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name
    
