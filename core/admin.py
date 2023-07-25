from django.contrib import admin
from .models import Profile,Post,likepost,Followers_count
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(likepost)
admin.site.register(Followers_count)

