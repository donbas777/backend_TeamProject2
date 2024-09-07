from django.contrib import admin

from .models import (
    Embroidery,
    Book,
    EmbroideryImage,
    BookImage,
)

admin.site.register(Embroidery)
admin.site.register(Book)
admin.site.register(EmbroideryImage)
admin.site.register(BookImage)
