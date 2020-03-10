from django.db import models


class Issue(models.Model):
    """ISSUE"""
    name = models.CharField('name', max_length=255)
    issueKey = models.CharField('issueKey', max_length=255, blank=True)
    summary = models.CharField('summary', max_length=255, blank=True)
    elapsedTime = models.CharField('elapsedTime', max_length=255, blank=True)
    modificationTimeStamp = models.DateTimeField('modificationTimeStamp')

    def __str__(self):
        return self.name
