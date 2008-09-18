# -*- coding: utf-8 -*-

__revision__ = '$Id$'


from django.core.files.uploadhandler import FileUploadHandler


class LoggingUploadHandler(FileUploadHandler):

    def __init__(self, request=None):
        self.file_size = None
        super(LoggingUploadHandler, self).__init__(request)

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        if self.file_size is None and content_length:
            self.file_size = float(content_length)
        return None

    def new_file(self, field_name, file_name, content_type, content_length, charset):
        if self.file_size is None and content_length:
            self.file_size = float(content_length)
        self.uploaded = 0.0
        self._log_percentage()

    def receive_data_chunk(self, raw_data, start):
        self.uploaded = self.uploaded + float(self.chunk_size)
        self._log_percentage()
        return raw_data

    def file_complete(self, file_size):
        self._log_percentage()
        return None

    def _log_percentage(self):
        if self.file_size is None:
            percentage = 'unknown'
        else:
            percents = (self.uploaded / self.file_size) * 100
            percentage = '%.2f' % percents
        print 'uploaded %d bytes (%s %%)' % (self.uploaded, percentage)