"""Country and currency forms

Settings
========

There are a few settings you can use to configure the behavior of the forms.
Note that these settings are for the form mixins, and not the form classes. So
forms that contain both country and currency form mixins will be affected by
both sets of

COUNTRY_FORM_LABEL
------------------

Label for the 'country' field. Defaults to 'country'.

COUNTRY_FORM_INCLUDE_EMPTY
--------------------------

This settings controls whether country form will include empty value when
instantiated. You can also use the ``COUNTRY_FORM_EMPTY_VALUE`` to control the
value of the item that will be treted as empty (no country). Default is
``False``.

COUNTRY_FORM_EMPTY_VALUE
------------------------

This setting controls the value that is assigned to empty value (no country) if
``COUNTRY_FORM_INCLUDE_EMPTY`` is set to ``True``.

COUNTRY_FORM_EMPTY_LABEL
------------------------

Customizes the label for the empty value (no country). Default is 'All
countries'.

COUNTRY_FORM_USE_STATIC
-----------------------

Use hard-coded values instead of reading the database.

CURRENCY_FORM_LABEL
-------------------

Label for the 'currency' field. Defaults to 'currency'.

CURRENCY_FORM_INCLUDE_EMPTY
---------------------------

Same as ``COUNTRY_FORM_INCLUDE_EMPTY`` but for currency form.

CURRENCY_FORM_EMPTY_VALUE
-------------------------

Same as ``COUNTRY_FORM_EMPTY_VALUE`` but for currency form.

CURRENCY_FORM_EMPTY_LABEL
-------------------------

Same as ``COUNTRY_FORM_EMPTY_LABEL`` but for currency form. Defaults to 'All
currencies'.

"""

from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _

from models import currencies, countries, Country


class CountryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)

        choices = []

        # Use static data or not
        if settings.COUNTRY_FORM_USE_STATIC:
            choices = list(countries)
        else:
            # Create choices for country field
            for country in Country.objects.all():
                choices.append((country.code, country.get_code_display()))

        # Include empty or not
        if settings.COUNTRY_FORM_INCLUDE_EMPTY:
            choices.insert(0, (settings.COUNTRY_FORM_EMPTY_VALUE,
                               settings.COUNTRY_FORM_EMPTY_LABEL))

        # Assign values
        self.fields['country'].choices = choices
        self.fields['country'].label = settings.COUNTRY_FORM_LABEL
        self.fields['country'].initial = kwargs.get('initial', {}).get(
            'country', settings.COUNTRY_FORM_INITIAL_VALUE)

    country = forms.ChoiceField(required=False,
                                choices=())


class CurrencyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)

        choices = list(currencies)

        if settings.CURRENCY_FORM_INCLUDE_EMPTY:
            choices.insert(0, (settings.CURRENCY_FORM_EMPTY_VALUE,
                               settings.CURRENCY_FORM_EMPTY_LABEL))

        self.fields['currency'].label = settings.CURRENCY_FORM_LABEL
        self.fields['currency'].choices = choices
        self.fields['currency'].initial = kwargs.get(
            'initial', {}
        ).get('currency', settings.CURRENCY_FORM_INITIAL_VALUE)

    currency = forms.ChoiceField(required=False,
                                 choices=())


class CountryCurrencyForm(CountryForm, CurrencyForm, forms.Form):
    pass
