from os.path import join
from django.conf import settings
from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from cms.settings import CMS_MEDIA_URL
from cms.plugins.text import settings
from django.utils.translation.trans_real import get_language


class WYMEditor(Textarea):
    class Media:
        js = [join(CMS_MEDIA_URL, path) for path in (
            #'javascript/jquery.js',
            'wymeditor/jquery.wymeditor.js',
            'wymeditor/plugins/resizable/jquery.wymeditor.resizable.js',
        )]

    def __init__(self, attrs=None):
        
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render_textarea(self, name, value, attrs=None):
        return super(WYMEditor, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language()
        context = {
            'name': name,
            'language': language,
            'CMS_MEDIA_URL': CMS_MEDIA_URL,
            'WYM_TOOLS': mark_safe(settings.WYM_TOOLS),
            'WYM_CONTAINERS': mark_safe(settings.WYM_CONTAINERS),
            'WYM_CLASSES': mark_safe(settings.WYM_CLASSES),
            'WYM_STYLES': mark_safe(settings.WYM_STYLES),
        }
        return mark_safe(render_to_string(
            'text/widgets/wymeditor.html', context))

    def render(self, name, value, attrs=None):
        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)
