from django.db import models
from django.utils.encoding import python_2_unicode_compatible
                                                        # Models classes are mapped to database tables, instances to rows
                                                        # Fields are mapped to columns
@python_2_unicode_compatible
class List(models.Model):                               # models.Models lets us save the data from the class to the Database
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List: {}".format(self.name)

@python_2_unicode_compatible
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)          # blank = True means its optional
    list = models.ForeignKey(List, related_name="cards")        # Providing a foreignkey to relate it to the List Class
    story_points = models.IntegerField(null=True, blank = True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Card: {}".format(self.title)

# After every change you need to makemigrations to the source folder to update the database according to the changes
