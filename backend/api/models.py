from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CSVHistory(models.Model):
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary_data = models.JSONField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Keep only last 5 records
        objects = CSVHistory.objects.all().order_by('-uploaded_at')
        if objects.count() > 5:
            # Delete everyone after 5th
            ids_to_keep = objects[:5].values_list('id', flat=True)
            CSVHistory.objects.exclude(id__in=ids_to_keep).delete()

    def __str__(self):
        return self.file_name
