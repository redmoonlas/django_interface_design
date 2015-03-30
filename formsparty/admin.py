from django.contrib import admin

from formsparty.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
