from django.contrib import admin

from .models import NewVideo

class NewVideoAdmin(admin.ModelAdmin):
	list_display = [
		'video_id',
		'video_title',
		'moods',
		'labeled',
	]
	search_fields = [
		'video_id',
		'video_title',
		'moods',
	]
	list_editable = [
		'moods',
		'labeled',
	]

admin.site.register(NewVideo, NewVideoAdmin)






