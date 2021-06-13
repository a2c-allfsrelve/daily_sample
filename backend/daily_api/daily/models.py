from django.db import models
from markdownx.models import MarkdownxField

class Daily(models.Model):
    date = models.DateField()
    univ = MarkdownxField()
    study = MarkdownxField()
    other = MarkdownxField()
    first_meet = MarkdownxField()
    wanna_do = MarkdownxField()
    summary = MarkdownxField()
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT) #一日の評価は外部キーに
    isOpen = models.BooleanField(default=True) #公開・非公開

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str

class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation