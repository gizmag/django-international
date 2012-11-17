from __future__ import unicode_literals

from django.test import TestCase

from international.models import Country
from international.forms import *

class CountryTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(code='AR', continent='SA')

    def test_can_get_country(self):
        c = self.country
        self.assertEqual(c.code, 'AR')
        self.assertEqual(c.continent, 'SA')
        self.assertEqual(c.get_code_display(), 'Argentina')
        self.assertEqual(c.get_continent_display(), 'South America')

    def tearDown(self):
        Country.objects.all().delete()

class CountryFormTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(code='AR', continent='SA')

    def tearDown(self):
        Country.objects.all().delete()

    def test_default_form(self):
        form = CountryForm()
        self.assertIn(('AR', 'Argentina'), form.fields['country'].choices)
        self.assertNotIn(('US', 'United States'),
                         form.fields['country'].choices)

    def test_form_with_static(self):
        form = CountryForm(use_static=True)
        self.assertIn(('AR', 'Argentina'), form.fields['country'].choices)
        self.assertIn(('US', 'United States'),
                      form.fields['country'].choices)

    def test_has_empty_item(self):
        form = CountryForm(include_empty=True)
        self.assertIn(('', 'All countries'), form.fields['country'].choices)

    def test_empty_label_and_value(self):
        form = CountryForm(include_empty=True, empty_value='*',
                           empty_label='Any country')
        self.assertIn(('*', 'Any country'), form.fields['country'].choices)


class CurrencyFormTestCase(TestCase):
    def test_default_form(self):
        form = CurrencyForm()
        self.assertEqual(form.fields['currency'].choices[0][0], 'USD')

    def test_empty(self):
        form = CurrencyForm(include_empty=True)
        self.assertIn(('', 'All currencies'), form.fields['currency'].choices)

    def test_empty_label(self):
        form = CurrencyForm(include_empty=True, empty_value='*',
                            empty_label='Any currency')
        self.assertIn(('*', 'Any currency'), form.fields['currency'].choices)

