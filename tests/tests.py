from __future__ import unicode_literals

from django.test import TestCase
from django.test.utils import override_settings

from international.models import Country
from international.forms import *

class CountryTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(code='AR', continent='SA')

    def test_can_get_country(self):
        c = self.country
        self.assertEquals(c.code, 'AR')
        self.assertEquals(c.continent, 'SA')
        self.assertEquals(c.get_code_display(), 'Argentina')
        self.assertEquals(c.get_continent_display(), 'South America')

    def tearDown(self):
        Country.objects.all().delete()

# We need a whole bunch of overrides to make sure all settings are at defaults
@override_settings(
    COUTNRY_FORM_LABEL='currency',
    COUNTRY_FORM_INCLUDE_EMPTY=False,
    COUNTRY_FORM_EMPTY_VALUE='',
    COUNTRY_FORM_EMPTY_LABEL='All countries',
    COUNTRY_FORM_INITIAL_VALUE='',
    COUNTRY_FORM_USE_STATIC=False,
)
class CountryFormTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(code='AR', continent='SA')

    def tearDown(self):
        Country.objects.all().delete()

    def test_default_form(self):
        # We do the import here so that settings are properly evaluated
        form = CountryForm()
        self.assertIn(('AR', 'Argentina'), form.fields['country'].choices)
        self.assertNotIn(('US', 'United States'),
                         form.fields['country'].choices)

    @override_settings(COUNTRY_FORM_USE_STATIC=True)
    def test_form_with_static(self):
        form = CountryForm()
        self.assertIn(('AR', 'Argentina'), form.fields['country'].choices)
        self.assertIn(('US', 'United States'),
                      form.fields['country'].choices)

    @override_settings(COUNTRY_FORM_LABEL='location')
    def test_form_label(self):
        form = CountryForm()
        self.assertEquals(form.fields['country'].label, 'location')

    @override_settings(COUNTRY_FORM_INCLUDE_EMPTY=True)
    def test_has_empty_item(self):
        form = CountryForm()
        self.assertIn(('', 'All countries'), form.fields['country'].choices)

    @override_settings(COUNTRY_FORM_INCLUDE_EMPTY=True,
                       COUNTRY_FORM_EMPTY_VALUE='*',
                       COUNTRY_FORM_EMPTY_LABEL='Any country')
    def test_empty_label(self):
        form = CountryForm()
        self.assertIn(('*', 'Any country'), form.fields['country'].choices)


    @override_settings(COUNTRY_FORM_INITIAL_VALUE='AR',
                       COUNTRY_FORM_ALLOW_EMPTY=True,
                       COUNTRY_FORM_EMPTY_VALUE='*')
    def test_initial_value(self):
        form = CountryForm()
        self.assertEquals(form.fields['country'].initial, 'AR')

        form = CountryForm(initial={'country': '*'})
        self.assertEquals(form.fields['country'].initial, '*')

# We need a whole bunch of overrides to make sure all settings are at defaults
@override_settings(
    CURRENCY_FORM_LABEL='currency',
    CURRENCY_FORM_INCLUDE_EMPTY=False,
    CURRENCY_FORM_EMPTY_VALUE='',
    CURRENCY_FORM_EMPTY_LABEL='All currencies',
    CURRENCY_FORM_INITIAL_VALUE=None,
)
class CurrencyFormTestCase(TestCase):
    def test_default_form(self):
        form = CurrencyForm()
        self.assertEquals(form.fields['currency'].choices[0][0], 'USD')

    @override_settings(CURRENCY_FORM_LABEL='transaction in')
    def test_label(self):
        form = CurrencyForm()
        self.assertEquals(form.fields['currency'].label, 'transaction in')

    @override_settings(CURRENCY_FORM_INCLUDE_EMPTY=True,
                       CURRENCY_FORM_EMPTY_VALUE='*',
                       CURRENCY_FORM_EMPTY_LABEL='Any currency')
    def test_empty(self):
        form = CurrencyForm()
        self.assertIn(('*', 'Any currency'), form.fields['currency'].choices)

    @override_settings(CURRENCY_FORM_INITIAL_VALUE='JPY')
    def test_default_value(self):
        form = CurrencyForm()
        self.assertEquals(form.fields['currency'].initial, 'JPY')
        form = CurrencyForm(initial={'currency': 'GBP'})
        self.assertEquals(form.fields['currency'].initial, 'GBP')
