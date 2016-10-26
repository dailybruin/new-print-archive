from django.db import models
from django.contrib.postgres import search

class ArchivePage(models.Model):
    oldmgid = models.TextField()
    id = models.TextField(primary_key=True)
    download_link = models.TextField(blank=True, null=True)
    direct_link = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tsv = search.SearchVectorField(null=True)

    class Meta:
        managed = True
        db_table = 'archive'
