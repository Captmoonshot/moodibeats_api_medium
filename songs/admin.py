from django.contrib import admin

from .models import NewVideo, NewVideoDescription

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

class NewVideoDescriptionModelAdmin(admin.ModelAdmin):
	class Meta:
		model = NewVideoDescription
	list_display = [
		'video_id',
		'video_title',
		'predicted_moods',
	]
	search_fields = [
		'video_id',
		'video_title',
		'predicted_moods',
	]
	list_editable = ['predicted_moods']

admin.site.register(NewVideoDescription, NewVideoDescriptionModelAdmin)









