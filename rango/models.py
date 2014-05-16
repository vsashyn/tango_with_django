from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
#unique attribute. If set to True, only one instance of a particular value in that field may exist throughout the entire database model.
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	class Meta:
		ordering = ["name"]
		verbose_name_plural = "Categories"
	
	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
#CharField, a field for storing character data (e.g. strings). Specify max_length to provide a maximum number of characters the field can store.
	title = models.CharField(max_length=128)
#URLField, much like a CharField, but designed for storing resource URLs. You may also specify a max_length parameter
	url = models.URLField()
#IntegerField, which stores integers.
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __unicode__(self):
		return self.user.username
