from html5print import HTMLBeautifier, JSBeautifier, CSSBeautifier
from os import path
from urllib import response
import json
from flask import Response


def file_extension(url):
    if url:
        url_find = url.find('?')
        url = url if url_find == -1 else url[:url_find]
        _, ext = path.splitext(url)
        return ext[1:] if ext else None


def beautify(raw: str, content_type: str, extension: str=None):
    content_type = parse_content_type(content_type)

    try:
        if extension == 'js' or content_type == 'application/javascript':
            return JSBeautifier.beautify(raw)
        if extension == 'json' or content_type == 'application/json':
            try:
                return json.dumps(json.loads(raw), indent=2, sort_keys=True)
            except json.decoder.JSONDecodeError:
                return raw
        if extension == 'css' or content_type == 'text/css':
            return CSSBeautifier.beautify(raw)

        if content_type == 'text/html':
            return HTMLBeautifier.beautify(raw)
    except:
        return raw

    return raw


def parse_content_type(content_type: str):
    return content_type[:content_type.find(';')] if content_type and ';' in content_type else content_type


def decorate_response(response: Response):
    response.headers['Access-Control-Allow-Origin'] = '*'