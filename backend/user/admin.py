from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from user.models import UserBio, SocialNetwork


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 1


@admin.register(UserBio)
class UserBioAdmin(admin.ModelAdmin):
    list_display = ("user", "faculty", "course", "rating")
    inlines = [SocialNetworkInline]


class BioInline(admin.StackedInline):
    model = UserBio
    can_delete = False
    verbose_name_plural = "Биография"


# Снимаем регистрацию стандартного UserAdmin
admin.site.unregister(User)

# Регистрируем своего
@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    inlines = [BioInline]