from django.contrib import admin
from .models import Post

admin.site.register(Post)

python manage.py createsuperuser

Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.
# Register your models here.
