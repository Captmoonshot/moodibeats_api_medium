from django.db import models

# Create your models here.
class NewVideo(models.Model):
	MOOD_CHOICES = (
	('HAPPY', 'Happy'),
	('IN-LOVE', 'In-Love'),
	('SAD', 'Sad'),
	('CONFIDENT-SASSY', 'Confident-sassy'),
	('CHILL', 'Chill'),
	('ANGRY', 'Angry'),
	)
	video_title 			= models.TextField(db_index=True, null=True, blank=True)
	video_id 				= models.CharField(max_length=11, null=False, blank=True, primary_key=True)
	moods 					= models.CharField(choices=MOOD_CHOICES, max_length=20,  default='HAPPY')
	labeled					= models.NullBooleanField()

	def __str__(self):
		return self.video_title