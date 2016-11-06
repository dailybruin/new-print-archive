from haystack import indexes
from .models import ArchivePage

class ArchivePageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='text')
    date = indexes.DateField(model_attr='publication_date')
    page = indexes.IntegerField(model_attr='page')

    def get_model(self):
        return ArchivePage
