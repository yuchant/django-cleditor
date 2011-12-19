What is it? 
-----------

A simple app that makes using an WYSIWYG editor (CLEditor) extremely easy.
https://github.com/cleditor/cleditor

CLEditor is MIT licensed. 


Installation instructions
-------------------------

Add ``cleditor`` to your ``INSTALLED_APPS`` and run the ``collectstatic`` management command to get the static files.




Usage instructions
------------------

This package supplies a ``CLEditorWidget`` form widget in ``cleditor.widgets`` that you can use anywhere the django forms framework expects a widget.

To replace all textfields in a ``ModelAdmin`` with ``CLEditors`` simply paste two lines:

    
    from django.db import models
    from cleditor.widgets import CLEditorWidget

    class MyModelAdmin(admin.ModelAdmin):
        formfield_overrides = { models.TextField: {'widget': CLEditorWidget()}}

You're done!

If you need finer control over which textfields get overriden, look into ``ModelAdmin.formfield_for_dbfield``