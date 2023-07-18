from django.db import models

class tvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 5 characters"
        if len(postData['description']) < 4:
            errors["description"] = "show description should be at least 10 characters"
        return errors


   

class tv(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=255)
    description =models.TextField()
    releace_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = tvManager()
    
    
