from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Register your models here.

class SofaAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style = "color:red; font-size:14px">Загружайте изображения с минимальным разрешением {}X{}</span style>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Мб!')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image

class SofaAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SofaAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sofa'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PufAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style = "color:red; font-size:14px">Загружайте изображения с минимальным разрешением {}X{}</span style>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Мб!')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image

class PufAdmin(admin.ModelAdmin):

    form = PufAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='puf'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class BedAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style = "color:red; font-size:14px">Загружайте изображения с минимальным разрешением {}X{}</span style>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Мб!')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image

class BedAdmin(admin.ModelAdmin):

    form = BedAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bed'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ChairAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style = "color:red; font-size:14px">Загружайте изображения с минимальным разрешением {}X{}</span style>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Мб!')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image

class ChairAdmin(admin.ModelAdmin):

    form = ChairAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='chair'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Sofa, SofaAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Puf, PufAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
