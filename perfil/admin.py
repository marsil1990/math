from django.contrib import admin


from .models import Project
# Register your models here.
#admin.site.register(Project)
#admin.site.register(Project, ProjectAdmin)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('id', 'title', 'desc', 'created')
    list_editable = ('title', 'desc')
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)
