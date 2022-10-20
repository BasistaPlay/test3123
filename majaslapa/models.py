from distutils.command.upload import upload
from email.policy import default
from itertools import product
from tkinter import Image
from unicodedata import category
from django.conf import settings
from django.urls import reverse
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


# from django.contrib.auth.models import User
# User._meta.get_field('email')._unique = True


class Category(MPTTModel):
    name = models.CharField(
    verbose_name = ('Nepieciešams un unikāls'),
    help_text=('Request and unique'),
    max_length = 255,
    unique= True
    )

    slug = models.SlugField(verbose_name=_('Kategorijas drošs URL'), max_length=250, unique = True, )
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name = 'children',verbose_name = ('Līdzīgie produkti'))
    is_active = models.BooleanField(default=True,verbose_name = ('Ir aktīvs'))
    image =models.ImageField(
        verbose_name= 'Attēls priekš kategorijas',
        help_text='Augšupielādējiet produkta attēlu',
        upload_to='images_category/',
        default='images_category/default.png'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = ('Kategorija')
        verbose_name_plural = ('Kategorījas')

    def get_absolute_url(self):
        return reverse("store:category_list", args={self.slug})

    def __str__(self):
        return self.name


class ProductType(models.Model):

    name = models.CharField(verbose_name=('Produkta nosaukums'), help_text='Obligāti', max_length=255, unique=True)
    is_active = models.BooleanField(verbose_name=('Ir aktīvs'), default=True)

    class Meta:
        verbose_name = ('Produkta veids')
        verbose_name_plural = ('Produkta veidi')

    def __str__(self):
        return self.name

class ProductSpecification(models.Model):

    Product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=('Nosaukums'),help_text='Obligāti', max_length=255)

    class Meta:
        verbose_name = ('Produkta specifikācija')
        verbose_name_plural = ('Produkta specifikācijas')

    def __str__(self):
        return self.name


class Product(models.Model):

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT, verbose_name = ('Produkta Veids'))
    category = models.ForeignKey(Category,on_delete=models.RESTRICT, verbose_name = ('Kategorija'))
    title = models.CharField(
        verbose_name = ('Nosaukums'),
        help_text=('nepieciešams'),
        max_length = 255
    )

    desciption = models.TextField(verbose_name='Apraksts', help_text=('nav nepieciešams'), blank=True)
    slug = models.SlugField(max_length=255, verbose_name = ('tīmekļa adreses identifikācija'))
    regular_price = models.DecimalField(
        verbose_name='Parastā cena',
        help_text = ('Maksimums 9999.99'),
        error_messages= {
            'name' : {
                'max_lenght': 'Cenai jābūt no 0 līdz 9999,99!'
            }
        },
        max_digits=6,
        decimal_places=2,
        )

    discount_price = models.DecimalField(
        verbose_name=('Atlaides cena'),
        help_text= ('Maksimalais ir 9999.99'),
        error_messages={
            'name' : {
                'max_lenght': 'Cenai jābūt no 0 līdz 9999,99!'
            }
        },
        max_digits=6,
        decimal_places=2,
    )

    is_active = models.BooleanField(
        verbose_name = 'Produkta redzamība',
        help_text = 'Mainīt produkta redzamību',
        default=True
    )
    created_at = models.DateTimeField(('Izveidots plkst'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(('Atjaunināts plkst'), auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Prece'
        verbose_name_plural = ('Preces')

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=('Vērtība'),
        help_text= ('Produkta specifikācijas vērtība (maksimums 255 vārdi)'),
        max_length=255,
    )

    class Meta:
        verbose_name = 'Produkta specifikacijas vērtība'
        verbose_name_plural = 'Produkta specifikacijas vērtības'

    def __str__(self):
        return self.value

class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name=('Produkta_attēls'))
    image =models.ImageField(
        verbose_name= 'Attēls',
        help_text='Augšupielādējiet produkta attēlu',
        upload_to='images/',
        default='images/default.png'
    )

    alt_text = models.CharField(
        verbose_name=('Alternatīva teksts'),
        help_text='Lūdzu pievienojiet alternatīvu tekstu',
        max_length=255,
        null=True,
        blank=True,
    )

    is_feature = models.BooleanField(default=False,verbose_name = ('Galvenā bilde'))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Produkta attēls'
        verbose_name_plural = 'Produkta attēli'
