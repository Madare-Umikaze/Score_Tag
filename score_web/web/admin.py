from django.contrib import admin
from .models import Score,Memo,Media,Genre

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
class MemoAdmin(admin.ModelAdmin):
    list_display = ('document', 'posteddate')
    
class MediaAdmin(admin.ModelAdmin):
    list_display = ('uploaddate', 'comment', 'mediatype')


    

admin.site.register(Score, ScoreAdmin)
admin.site.register(Memo, MemoAdmin)
admin.site.register(Media, MediaAdmin)