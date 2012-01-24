import os

from django import http
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import patterns
from django.core.files.storage import default_storage


class CLEditorUploadAdmin(admin.ModelAdmin):
	upload_to = 'cleditoruploads/'

	"""
	CLEditor Upload Admin
	---------------------
	"""
	def get_urls(self):
		urls = super(CLEditorUploadAdmin, self).get_urls()
		my_urls = patterns('',
			(r'upload-image/$', self.admin_site.admin_view(self.upload_handler)),
		)
		return my_urls + urls

	def upload_handler(self, request):
		"""
		Handle widget uploader
		"""
		return cleditor_upload_handler(request, upload_to=self.upload_to)


def cleditor_upload_handler(request, upload_to='cleditoruploads/'):
	if not request.POST:
		raise http.Http404

	f = request.FILES['imageName']
	result = default_storage.save(os.path.join(upload_to, f.name), f)
	return http.HttpResponse('<div id="image">{static_url}{path}</div>'.format(static_url=settings.STATIC_URL, path=result))

