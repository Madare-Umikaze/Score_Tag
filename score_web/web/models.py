from django.db import models

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genrename = models.CharField('ジャンル', max_length=100)
    
    def __str__(self):
        return self.genrename
    
    
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('曲名', max_length=100)
    registration_date = models.DateTimeField('登録日', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.TextField('メモ', max_length=1000)
    posteddate = models.DateTimeField('投稿日', auto_now_add=True)
    titles = models.ManyToManyField(Score, verbose_name='メモを追加する曲')
    
    
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    mediatype = models.CharField('種類', max_length=50)
    mediapath = models.CharField('メディアパス', max_length=10000)
    uploaddate = models.DateTimeField('投稿日', auto_now_add=True)
    comment = models.TextField('コメント')
    titles = models.ManyToManyField(Score, verbose_name='メディアを追加する曲')
    
    
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher = models.CharField('出版社', max_length=100)
    titles = models.ManyToManyField(Score)