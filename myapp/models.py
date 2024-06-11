from django.db import models


class Fechas(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
   

    def __str__(self):
        return f'Inicio: {self.fecha_inicio}, Fin: {self.fecha_final}'
#Crear los modelos--------------------------------------------------------

class PublicationStatu(models.Model):
    name =models.CharField(max_length=255)
    description=models.CharField(max_length=255)

class Administrative(models.Model):
    administrativeId=models.PositiveIntegerField()

class User(models.Model):
    name =models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    statu=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    type_user=models.CharField(max_length=10)
    administartive_id=models.PositiveIntegerField()
    editor_id=models.PositiveIntegerField()

class Editor(models.Model):
    suscription_points =models.CharField(max_length=255)

class Presenter(models.Model):
    full_name =models.CharField(max_length=255)
    photo_url =models.URLField(max_length=100)
    sex=models.CharField(max_length=10)

class ElementPresenter(models.Model):
    content =models.CharField(max_length=255)
    expression=models.CharField(max_length=255)

class ElementVideo(models.Model):
    elementvideoId=models.PositiveIntegerField()

class Element(models.Model):
    titulo =models.CharField(max_length=255)
    video_url =models.URLField(max_length=100)
    type_element=models.DateField()
    elementPresnet_id=models.PositiveIntegerField()
    elementVideo_id=models.PositiveIntegerField()

class Project(models.Model):
    name =models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    cover_url =models.URLField(max_length=100)
    video_url =models.URLField(max_length=100)
    statu=models.CharField(max_length=10)
    presenter_id=models.PositiveIntegerField()
    editor_id=models.PositiveIntegerField()
    element_id=models.PositiveIntegerField()

class News(models.Model):
    titulo =models.CharField(max_length=255)
    content=models.CharField(max_length=255)
    publication_date=models.DateField()
    publicationStatu_id=models.PositiveIntegerField()
    administrative_id=models.PositiveIntegerField()
    project_id=models.PositiveIntegerField()

