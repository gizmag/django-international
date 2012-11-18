====================
django-international
====================

django-international is a combination of data, models, and forms, for handling
country- and currency-related information in your Django_ project. The data
used in this app comes from Wikipedia_ and XE.com_, and will be updated from
time to time when sources become updated.

international.models.countries_raw
==================================

This is a tuple of tuples in the following format:

    countries_raw = (
        (CO, CC, CNT, NUM, FN),
        ...
    )

*CO* is the two-letter continent code. *CC* is the country code as per ISO
3166-1 standard. *CNT* is the 3-letter code as per ISO 3166-1 standard. *NUM*
is the three-digit code as per ISO-3166-1 standard. *FN* is the full name of
the country as a translatable string (wrapped in 
``django.util.translation.ugettext``).

This tuple is processed at runtime to derive the choices-compatible tuple.

Please note that some country names were modified and that the choices tuple
will omit anything that appears in brackets compared to the original list on
Wikipedia_.

international.models.countries
==============================

This is a tuple of tuples compatible with ``choices`` argument passed to
Django's model/form fields. The values are 2-letter country codes, and display
values are full country names without the parts that appear in brackets.

This tuple is also used as choices argument in the country form if
``use_static`` argument is passed to the constructor, or
``COUNTRY_FORM_USE_STATIC`` configuration setting is set to ``True``.

international.models.currencies
===============================

This is atuple of tuples compatible with ``choices`` argument passed to
Django's model/form fields. The values are ISO 4217 3-letter currency codes,
and display values are the same codes with full currency names. For example:

    ('USD', 'USD - United States Dollar')

This tuple is used as ``choices`` argument for the ``ChoicesField`` in the
currency form.

international.models.Country
============================

The ``models`` module contains a ``Country`` model. It is a full model (not
abstract) and it is meant to be linked to from your other modules via foreign
keys.

Country.code
------------

This field contains 2-letter ISO code for your country as per ISO 3166-1 alpha
2 standard. The field is constrained by choices which allows a full set of
countries found on Wikipedia_. There is currently no way of restricting the
choices with configuration settings.

The full names of countries are translatable strings, and can be displayed by
using the standard Django API for display names:

    >>> c = Country(code='AR', continent='SA')
    >>> c.get_code_display()
    u'Argentina'

Country.continent
-----------------

This field contains two-letter codes for continents as per Wikipedia_. These
are restricted to:

 + *AF*  --  Africa
 + *AS*  --  Asia
 + *EU*  --  Europe
 + *NA*  --  North America
 + *SA*  --  South America
 + *OC*  --  Oceania
 + *AN*  --  Antarctica

The full names are translatable, and can be obtained using Django's standard
display name API:

    >>> c = Country(code='AR', continent='SA')
    >>> c.get_continent_display()
    u'South America'

international.forms.CountryForm(*arg, use_static=False, include_empty=False, empty_value='', empty_label='All countries', **kwarg)
==================================================================================================================================

This is a simple form with a single ``ChoiceField`` field called ``country``.
It is marked as optional, has a translatable label that reads 'country', and
has empty string as initial value.

Some aspects of this form can be controlled using configuration settings or
constructor arguments. Any arguments that a standard Django form accepts are
also acceptable (e.g., ``initial`` or ``data``). Note that constructor
arguments always take precedence over settings.

Following sections describe available configuration settings and matching
constructor arguments.

COUNTRY_FORM_USE_STATIC or use_static
-------------------------------------

These options control whether to use the ``countries`` tuple or use existing
countries from the ``Country`` model as choices for the field. If the model
objects are used, they are read from the database each time the form is
initialized. There is currently no caching involved.

COUNTRY_FORM_INCLUDE_EMPTY or include_empty
-------------------------------------------

Whether to include an 'empty' item in the choices. This can be treated as a
``None`` value in the views, depending on your needs. If set to ``True``, a
single two-tuple will be prepended to the choices tuple that uses empty value
specified by ``COUNTRY_FORM_EMPTY_VALUE`` setting or the ``empty_value`` 
constructor argument, and label matching the ``COUNTRY_FORM_EMPTY_LABEL`` 
setting or ``empty_label`` constructor argument.

COUNTRY_FORM_EMPTY_VALUE or empty_value
---------------------------------------

The value to use as empty. Defaults to empty string.

COUNTRY_FORM_EMPTY_LABEL or empty_label
---------------------------------------

Value to use as display value for the empty item. Default to a translatable
string 'All countries'.

international.forms.CurrencyForm(*arg, include_empty=False, empty_value='', empty_label='All currencies', **kwarg)
==================================================================================================================

Simple form with a simple ``ChoiceField`` field called ``currency``. It uses
the ``currencies`` tuple as choices argument.

This form has similar configuration parameters as the ``CountryForm`` form.

CURRENCY_FORM_INCLUDE_EMPTY or include_empty
--------------------------------------------

Whether to include an empty item in the choices. The value and label of the
empty item are controlled via the ``CURRENCY_FORM_EMPTY_VALUE`` and
``CURRENCY_FORM_EMPTY_LABEL`` settings, or the ``empty_value`` and
``empty_label`` constructor arguments.

CURRENCY_FORM_EMPTY_VALUE or empty_value
----------------------------------------

Controls the empty item's value. Defaults to ''.

CURRENCY_FORM_EMPTY_LABEL or empty_label
----------------------------------------

Controls the label used for the empty item. Defaults to a translatable string
'All currencies'.

international.forms.CountryCurrencyForm(*args, **kwargs)
========================================================

This is an experimental feature that combines both the ``CountryForm`` and
``CurrencyForm`` into a single form. This form is governed by both sets of
settings and constructor arguments that apply to either of the simple forms.

This feature hsan't been tested thoroughly (especially the constructor
arguments), but it is known to work as expected with configuration settings.

Fixtures
========

The ``international/fixtures/`` directory contains a set of fixtures that can
be loaded using the ``loaddata`` management command. The fixtures are generated
based on ``countries_raw`` tuple, and contains the data for the ``Country``
model. It is intentionally not the initial data fixture, since the purpose of
the ``Country`` model is to create an editable list of countries, and not have
them hard-coded. Initial data fixture would overwrite the data each time 
``syncdb`` command is used, so it would effectively invalidate the very purpose
of the model.

Reporting bugs
==============

Bugs can be reported to Bitbucket_.

.. _Django: http://www.djangoproject.com/
.. _Wikipedia: http://en.wikipedia.org/wiki/List_of_countries_by_continent_%28data_file%29
.. _XE.com: http://www.xe.com/iso4217.php
.. _Bitbucket: https://bitbucket.org/monwara/django-international/issues
