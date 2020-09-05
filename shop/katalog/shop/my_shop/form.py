from django.forms import forms, CharField, BooleanField, EmailField, Textarea, TextInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = CharField(required=False)
    shipping_address2 = CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = CharField(required=False)

    billing_address = CharField(required=False)
    billing_address2 = CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))


class CouponForm(forms.Form):
    code = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = CharField()
    message = CharField(widget=Textarea(attrs={
        'rows': 4
    }))
    email = EmailField()


class PaymentForm(forms.Form):
    stripeToken = CharField(required=False)
    save = BooleanField(required=False)
    use_default = BooleanField(required=False)