from django.contrib import admin

from core.models import Category, Person, Film, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class FilmAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Film, FilmAdmin)
