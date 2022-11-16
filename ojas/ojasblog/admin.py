from django.contrib import admin

# Register your models here.
from .models import Bhagavan,ContactForm
# Register your models here.
@admin.register(Bhagavan)
class OjserModelAdmin(admin.ModelAdmin):
 list_display=('id', 'heading', 'paragram')


@admin.register(ContactForm)

class AboutAdmin(admin.ModelAdmin):

    list_display=('name','age','feedback')