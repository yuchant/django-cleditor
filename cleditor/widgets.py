from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils import simplejson
from django.middleware.csrf import get_token
from django.core.exceptions import ImproperlyConfigured
from django.forms.util import flatatt



class CLEditorWidget(forms.Textarea):
    """
    Widget providing CLEditor for Rich Text Editing.
    Supports direct image uploads and embed.
    """
    class Media:
        js = [
            'cleditor/jquery-1.7.1.min.js',
            'cleditor/jquery.cookie.js',
            'cleditor/jquery.cleditor.min.js',
        ]
        css = {
            'all': ('cleditor/jquery.cleditor.css',),
        }

    def __init__(self, config_name='default', *args, **kwargs):

        super(CLEditorWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs={}):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        # self.config['filebrowserUploadUrl'] = reverse('ckeditor_upload')
        # self.config['filebrowserBrowseUrl'] = reverse('ckeditor_browse')
        return mark_safe(u'''<textarea{flat_attrs}>{value}</textarea>
        <script type="text/javascript">
            $("#{id}").cleditor();
        </script>'''.format(
            flat_attrs=flatatt(final_attrs),
            value=value,
            id=final_attrs.get('id'),
        ))


class CLEditorUploadWidget(CLEditorWidget):
    class Media:
        js = [
            'cleditor/jquery-1.7.1.min.js',
            'cleditor/jquery.cookie.js',
            'cleditor/jquery.cleditor.min.js',
            'cleditor/jquery.cleditor.extimage.js',
        ]
        css = {
            'all': ('cleditor/jquery.cleditor.css',),
        }

    def __init__(self, config_name='default', upload_url='upload-image/', *args, **kwargs):
        self.upload_url = upload_url
        super(CLEditorUploadWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs={}):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        # self.config['filebrowserUploadUrl'] = reverse('ckeditor_upload')
        # self.config['filebrowserBrowseUrl'] = reverse('ckeditor_browse')
        return mark_safe(u'''<textarea{flat_attrs}>{value}</textarea>
        <script type="text/javascript">
            $.cleditor.buttons.image.uploadUrl = '{upload_url}';
            $("#{id}").cleditor();
        </script>'''.format(
            flat_attrs=flatatt(final_attrs),
            value=value,
            id=final_attrs.get('id'),
            upload_url=self.upload_url,
        ))

