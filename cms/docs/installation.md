Installation
============

copy the cms and mptt folder into your project or pythonpath

Apps
----

add the following to your INSTALLED_APPS in your settings.py:

	INSTALLED_APPS = (
 		...
    	'cms',
    	'cms.plugins.text',
    	'cms.plugins.picture',
    	'mptt',
    	...
    
Django-cms 2.0 is compatible with django-reversion for versioning all the page content and its plugins.

Middleware
----------

add the following middlewares:

	MIDDLEWARE_CLASSES = (
    	...
    	'cms.middleware.CurrentSiteMiddleware',
    	'cms.middleware.CurrentPageMiddleware',
    	'cms.middleware.MultilingualURLMiddleware',
    	...
    	)
    
If your site is not multilingual you can leave out the MutilingualURLMiddleware

Context Processors
------------------
add the following context processors if not already present:

	TEMPLATE_CONTEXT_PROCESSORS = (
    	...
    	"django.core.context_processors.request",
    	"cms.context_processors.media",
    	...
    	)

Templates
---------

Add some template names you use and that have some placeholder templatetags present to your settings.py

	CMS_TEMPLATES = (
    	('base.html', gettext('default')),
    	('2col.html', gettext('2 Column')),
    	('3col.html', gettext('3 Column')),
    	('extra.html', gettext('Some extra wired template')),
	)

For some template examples see the templates used in the example project

a quick example:

	{% load cms_tags %}

	<div id="menu">{% show_menu 0 100 100 100 %}</div> 
	<div id="breadcrumb">{% show_breadcrumb %}</div>
	<div id="languagechooser">{% language_chooser %}</div>
	<div id="content">{% placeholder "content" %}</div>
	<div id="left_column">{% placeholder "left_column" %}</div>
    
i18n
----

If your site is multilingual be sure to have the LANGUAGES present in your settings:

	LANGUAGES = (
    	('fr', gettext('French')),
    	('de', gettext('German')),
    	('en', gettext('English')),
	)

Other settings
--------------

For a list of all settings that can be overwritten in your settings.py have a look at cms/settings.py

More information is available in the docs folder: cms/docs/
or have a look at the example project


