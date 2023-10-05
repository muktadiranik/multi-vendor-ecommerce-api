from django.db import models
from django_quill.fields import QuillField
from apps.utilities.validators import validate_site_icon_size
from django.core.validators import FileExtensionValidator


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = QuillField(blank=True, null=True)
    image = models.ImageField(upload_to='about_us_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'About Us'


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Privacy Policies'


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Terms And Conditions'


class ReportType(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Report Types'


class Report(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Reports'

class HomePage(models.Model):
    site_logo = models.ImageField(upload_to='images/site/logo/', verbose_name='Site Logo', null=True)
    site_video = models.FileField(upload_to='videos/site/', verbose_name='Site Video',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv'])], null=True)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.site_logo)

    class Meta:
        verbose_name_plural = 'Home Page contents'


class GoVeloWork(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=255, null=True)
    icon = models.ImageField(upload_to='images/goveloworks/',
                             validators=[validate_site_icon_size], null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Go Velo Works'
