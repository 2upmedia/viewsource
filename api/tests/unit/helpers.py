import unittest
from unittest_data_provider import data_provider
from viewsource.helpers import parse_content_type, file_extension, beautify


class ParseContentTypeTest(unittest.TestCase):
    content_types = lambda: (
        ('application/javascript; charset=UTF-8', 'application/javascript'),
        ('application/javascript', 'application/javascript'),
        (None, None)
    )

    @data_provider(content_types)
    def test_returns_correct_content_type(self, content_type, expected):
        self.assertEqual(expected, parse_content_type(content_type))


class FileExtensionTest(unittest.TestCase):
    extensions = lambda: (
        ('/test/this/file.js', 'js'),
        ('/js/wp-embed.min.js?ver=4.5.3', 'js'),
        ('/test/this/file', None),
        ('', None),
    )

    @data_provider(extensions)
    def test_returns_correct_extension(self, content_type, expected):
        self.assertEqual(expected, file_extension(content_type))


class BeautifyTest(unittest.TestCase):
    extensions = lambda: (
        ('''
<html>
  <head>
  </head>
  <body>
  </body>
</html>
'''[1:], '<html><head></head></html>', 'text/html'),
        ('''
html {
  font-family         : sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%
}
body {
  margin              : 0
}
'''[1:-1],'html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}', 'text/css', 'css'),
        ('''
(function(window) {
  window.alert("hello");
  console.log("hello");
})(window);
'''[1:-1], '(function(window){window.alert("hello");console.log("hello");})(window)', 'application/javascript',  'js'),
        ('''
{
  "data": [
    1,
    2,
    3
  ],
  "message": "hello"
}
'''[1:-1], '{"data": [1,2,3], "message": "hello"}', 'application/json',  'json'),
    )

    @data_provider(extensions)
    def test_returns_correct_extension(self, expected, raw, content_type, extension=None):
        self.assertEqual(expected, beautify(raw, content_type, extension))