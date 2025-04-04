from django.db import models



class News(models.Model):
    name = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=290)
    text2 = models.TextField('Статья')
    date = models.DateTimeField("Дата публикации")
    photo = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
