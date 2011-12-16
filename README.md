What is it? 
-----------

A simple app that makes using an WYSIWYG editor (CLEditor) extremely easy.
https://github.com/cleditor/cleditor

CLEditor is MIT licensed. 


Instructions
------------

To replace all textfields in a ``ModelAdmin`` with ``CLEditors`` simply paste two lines:

    
    from django.db import models
    from cleditor.widgets import CLEditorWidget

    class MyModelAdmin(admin.ModelAdmin):
        formfield_overrides = { models.TextField: {'widget': CLEditorWidget()}}

You're done!