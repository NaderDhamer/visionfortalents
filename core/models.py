from django.db import models
from django.urls import reverse


class WorkPackage(models.Model):
    number = models.PositiveIntegerField(unique=True, help_text="1–7")
    slug = models.SlugField(unique=True, help_text="Used in the URL, e.g. 'wp3-training'")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='work_packages/')
    coordinator = models.CharField(max_length=200, help_text="e.g. 'Institut Pasteur de Tunis'")

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"WP{self.number}: {self.title}"

    def get_absolute_url(self):
        return reverse('core:work_package_detail', kwargs={'slug': self.slug})


class SABMember(models.Model):
    name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='sab_members/', blank=True, null=True)
    bio = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class ConsortiumPartner(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='consortium_logos/', blank=True, null=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class TrainingProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='training/', blank=True, null=True)
    application_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} — {self.name}"        