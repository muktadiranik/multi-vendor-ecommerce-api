from django.db import models
from . import choices
from django.contrib.auth import get_user_model

User = get_user_model()




class Language(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Language Name', null=True, blank=True)
    code = models.CharField(max_length=10, unique=True, choices=choices.LANGUAGE_CODES,
                            verbose_name='Language Code', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'


class Currency(models.Model):
    name = models.CharField(max_length=20, unique=True,
                            verbose_name='Currency Name', null=True, blank=True)
    code = models.CharField(max_length=20, unique=True,
                            choices=choices.CURRENCY_CODES, null=True, blank=True)
    symbol = models.CharField(
        max_length=20, choices=choices.CURRENCY_SYMBOLS, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'


class NominationType(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Nomination Type', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nomination Types'


class Nomination(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    nomination_type = models.ForeignKey(NominationType, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    email= models.EmailField(null=True, blank=True)
    rental_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Nominations'


class AddressType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Address Type Name',
                            null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Address Types'


class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Product Type Name', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Types'


class ProductRateType(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Product Rate Type Name', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Rate Types'


class ContactType(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Contact Type Name', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Types'


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    rental_booking = models.CharField(max_length=100, null=True, blank=True, verbose_name='Rental/Booking Number')
    email = models.EmailField(null=True, blank=True)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Contacts'


class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Event Type Name', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Event Types'


class Event(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Events'
