# -*- coding: utf-8 -*-

__revision__ = '$Id$'


from django.core.files.uploadhandler import FileUploadHandler


class LoggingUploadHandler(FileUploadHandler):

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.uploaded = 0
        self._log_percentage()
        return None

    def receive_data_chunk(self, raw_data, start):
        self.uploaded = self.uploaded + self.chunk_size
        self._log_percentage()
        return raw_data

    def file_complete(self, file_size):
        self._log_percentage()
        return None

    def _log_percentage(self):
        print 'uploaded %d bytes' % self.uploaded