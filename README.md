What is it? 
-----------

A simple django app that makes using an WYSIWYG editor (CLEditor) extremely easy.
Optionally includes a mixin that activates file upload handling.

![Screenshot](https://github.com/yuchant/django-cleditor/raw/master/cleditor.png)



Installation instructions
-------------------------

Add ``cleditor`` to your ``INSTALLED_APPS`` and run the ``collectstatic`` management command to get the static files.




Usage instructions
------------------

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


Upload handler
--------------

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




Credits
-------
* Chris Landowski - cleditor jquery plugin creator
http://premiumsoftware.net/cleditor/

* Dmitry Dedukhim - original cleditor image upload plugin
https://github.com/dmitry-dedukhin/cleditor-extimage-plugin
