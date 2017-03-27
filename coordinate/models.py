from django.db import models

# Create your models here.
class Coordinate(models.Model):
	point_x = models.IntegerField()
	point_y = models.IntegerField()

	def __str__(self):
		return "%s, %s" %(self.point_x, self.point_y)
