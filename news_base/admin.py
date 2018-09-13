from django.contrib import admin
from . models import News, Events, Imformation, About, Cooperation,Services



# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body', 'date')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'create_time')

class ImformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'sub', 'create_time')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'img')

class  CooperationAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'img', 'creat')




admin.site.register(Events, EventsAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(Imformation, ImformationAdmin)

admin.site.register(About, AboutAdmin)

admin.site.register(Cooperation, CooperationAdmin)

admin.site.register(Services, ServicesAdmin)
