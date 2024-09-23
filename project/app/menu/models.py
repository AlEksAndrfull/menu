from django.db import models
from django.urls import reverse


class MenuItem(models.Model):

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=150, default='main_menu')


    def get_absolute_url(self):
        return reverse(self.url)
    


    def __str__(self) -> str:
        return self.title
    