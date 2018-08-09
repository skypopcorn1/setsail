from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import (UserAdminChangeForm, UserAdminCreationForm)
from .models import (User, Profile, YachtClub, Yacht, Role)
from race.models import (Division, Race, RaceCourse, Season)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin', 'timestamp',)
    list_filter = ('admin','user_role')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Roles', {'fields': ('user_role',)}),
        ('Permissions', {'fields': ('admin','staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','user_role',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class ProfileModelAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"user",
		"mobile",
		]

	list_display_links = [
		"id",
		]


	search_fields = [ "mobile" ]

	class Meta:
		model = Profile

class YachtClubModelAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"name",
		"created_at",
		"updated_at"
		]

	list_display_links = [
		"id",
		"name",
		"created_at",
		"updated_at",
		]

	list_filter = [
		"created_at",
		"updated_at",
		]

	search_fields = [ "name" ]

	class Meta:
		model = YachtClub

class YachtModelAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"name",
        "manufacturer",
        "model",
		"created_at",
		"updated_at"
		]

	list_display_links = [
		"id",
		"name",
		"created_at",
		"updated_at",
		]

	list_filter = [
		"created_at",
		"updated_at",
		]

	search_fields = [ "name", "model", "manufacturer" ]

	class Meta:
		model = Yacht

class RaceModelAdmin(admin.ModelAdmin):
	list_display = [
        "race_course",
		"race_start",
        "race_finish",
		"created_at",
		]

	list_display_links = [
		"race_course",
		"created_at",
		]

	search_fields = [ "race_date", ]

	class Meta:
		model = Race

class SeasonModelAdmin(admin.ModelAdmin):
	list_display = [
        "name",
		"season_start",
        "season_finish",
		"created_at",
		]

	list_display_links = [
		"name",
		"created_at",
		]

	search_fields = [ "name", ]

	class Meta:
		model = Season

class DivisionModelAdmin(admin.ModelAdmin):
	list_display = [
        "name",
		"created_at",
		]

	list_display_links = [
		"name",
		"created_at",
		]

	search_fields = [ "name", ]

	class Meta:
		model = Division

admin.site.register(Division, DivisionModelAdmin)
admin.site.register(Role)
admin.site.register(Race, RaceModelAdmin)
admin.site.register(RaceCourse)
admin.site.register(Season, SeasonModelAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(YachtClub, YachtClubModelAdmin)
admin.site.register(Yacht, YachtModelAdmin)
