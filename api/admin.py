from django.contrib import admin
from .models import (YachtClub, Yacht)
# Register your models here.
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

admin.site.register(YachtClub, YachtClubModelAdmin)
admin.site.register(Yacht, YachtModelAdmin)
