from django.db import models


class BenchmarkingEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='benchmarking/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class MediaMention(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200, help_text="e.g. 'La Presse', 'Nature'")
    date = models.DateField()
    external_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='media_mentions/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.source})"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=300, blank=True)
    registration_link = models.URLField(blank=True)
    flyer = models.FileField(upload_to='events/', blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title