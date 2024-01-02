from django.contrib import admin
from .models import Question

class QuetsionAdmin(admin.ModelAdmin):
  search_fields = ['subject']
  
admin.site.register(Question, QuetsionAdmin)