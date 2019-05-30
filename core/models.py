
from django.contrib.gis.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
    model that will be inherited by all models to add common fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_createdby',  on_delete=models.CASCADE, null=True, blank=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='%(class)s_modifiedby', on_delete=models.CASCADE,  null=True, blank=True)

    class Meta:
        abstract = True


class Branch(models.Model):

    branch_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sales(models.Model):
    branch = models.ForeignKey('Branch', on_delete = models.CASCADE)
    sales_amount = models.IntegerField()
    year = models.CharField(max_length=4) 

    class Meta:
        unique_together = (('year', 'branch'),)

    def __str__(self):
        return self.branch.name


class Device(BaseModel):
    id = models.CharField(primary_key=True, max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    current_location = models.PointField()


class LocationHistory(BaseModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    coordinates = models.PointField()




