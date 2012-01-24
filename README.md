What is it? 
============

A simple django app that makes using an WYSIWYG editor (CLEditor) extremely easy.
Optionally includes a mixin that activates file upload handling.

![Screenshot](https://github.com/yuchant/django-cleditor/raw/master/cleditor.png)



Installation instructions
=========================

Download and add ``django-cleditor`` to your packages however you wish.

- The easiest method is to use pip: `pip install django-cleditor`
- Add ``cleditor`` to your ``INSTALLED_APPS``
- Run the ``python manage.py collectstatic`` management command to ... collect the static files.
- Use `cleditor.widgets.CLEditorWidget` anywhere a django form widget is expected.
- For admin upload handling subclass `cleditor.admin.CLEditorUploadAdmin` and use `cleditor.widgets.CLEditorUploadWidget` instead.



Usage instructions
==================


Editor only
-----------

This package supplies a ``CLEditorWidget`` form widget in ``cleditor.widgets`` that you can use anywhere the django forms framework expects a widget.

To replace all textfields in a ``ModelAdmin`` with ``CLEditors`` simply paste two lines:
    
```python
from django.db import models
from cleditor.widgets import CLEditorWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': CLEditorWidget()}}
```

_Note: If you need finer control over which textfields get overriden, look into ``ModelAdmin.formfield_for_dbfield``_

You're done!


Easy admin upload handler
-------------------------

To allow users to upload via a the insert image widget, you must use the `CLEditorUploadWidget` widget and you must subclass the included `ModelAdmin` which adds a fully csrf protected upload handler to your admin site.

You can specify a new upload directory by adding an `upload_to` attribute to the `ModelAdmin`

```python
from django.db import models
from cleditor.widgets import CLEditorUploadWidget
from cleditor.admin import CLEditorUploadAdmin

class MyModelAdmin(CLEditorUploadAdmin):
    # upload_to = 'cleditorupload/' # default 
    formfield_overrides = { models.TextField: {'widget': CLEditorUploadWidget()}}
```


Stand alone uploader (non admin)
--------------------------------

To upload images without the admin panel, you'll have to map a URL to the upload handler and pass in your custom handler URL to the widget.


```python
# urls.py

from cleditor.admin import cleditor_upload_handler

urlpatterns = patterns('',
	(r'^my-upload-handler/$', cleditor_upload_handler, {'upload_to': 'my_upload_directory'}),
)
```


```python
# widget instantiation

class MyForm(forms.Form):
    myfield = forms.TextField(widget=CLEditorUploadAdmin(upload_url='path-to-my-upload-handler'))
```


Credits
========
* Chris Landowski - original cleditor image upload plugin
https://github.com/dmitry-dedukhin/cleditor-extimage-plugin

* Dmitry Dedukhim - cleditor jquery plugin creator
http://premiumsoftware.net/cleditor/