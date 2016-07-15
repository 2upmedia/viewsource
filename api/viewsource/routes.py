from flask import request, g, redirect, request, json, jsonify, Response
from viewsource import app
# import pydevd
from urllib.error import URLError
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from hashlib import md5
from .helpers import beautify, file_extension, decorate_response


@app.route('/sources', methods=['GET'])
def get_source():
    try:
        url = request.args.get('url')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103 Safari/537.36'
        }
        response = urlopen(Request(url, headers=headers, method='GET'))

        charset = response.info().get_charset()
        decoded_source = response.read().decode(charset) if charset else response.read().decode('latin1')
        extension = file_extension(urlparse(url).path)

        try:
            content_type = response.headers['Content-Type'] or 'text/html' if not extension else None
            decoded_source = beautify(decoded_source, content_type, extension)
        except SyntaxError:
            pass

        response = jsonify({'data': {'id': md5(url.encode('utf-8')).hexdigest(), 'type': 'sources',
                                     'attributes': {'source_code': decoded_source}}})
        """:type: Response"""

        decorate_response(response)

        return response
    except (URLError, ValueError) as e:
        fully_qualified_tmpl = 'Please enter a fully qualified URL: {0}'
        please_check_tmpl = 'Please check URL: {0}'
        error = fully_qualified_tmpl.format(url) if isinstance(e, ValueError) else please_check_tmpl.format(url)

        response = jsonify(
            {'errors': [{'status': 400, 'title': 'URL Error', 'detail': error}]})

        decorate_response(response)

        return response, 400
