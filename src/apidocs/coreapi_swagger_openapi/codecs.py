import json

from six.moves.urllib.parse import urlparse

from coreapi.codecs import base
from coreapi.compat import force_bytes


class OpenAPICodec(base.BaseCodec):
    media_type = 'application/json'

    def dump(self, document, **kwargs):
        converter = DocumentToSwaggerConverter(document)
        return force_bytes(json.dumps(converter.convert()))


class DocumentToSwaggerConverter(object):
    def __init__(self, document):
        self.document = document

    def convert(self):
        return self._generate_swagger_object()

    def _generate_swagger_object(self):
        """
        Generates root of the Swagger spec.
        """

        return {
            'openapi': '3.0.1',
            'info': self._get_info_object(),
            'servers': self.document.servers,
            'tags': self.document.tags,
            'paths': self._get_paths_object(),
        }

    def _get_info_object(self):
        return {
            'title': self.document.title,
            'version': self.document.version,
            'termsOfService': self.document.termsOfService,
            'license': self.document.license,
            'contact': self.document.contact,
            'description': self.document.description
        }

    def _get_paths_object(self):
        paths = {}
        for tag, object_ in self.document.links.items():
            if not object_.url in paths:
                paths[object_.url] = {}
            
            operation = self._get_operation(tag, object_)
            paths[object_.url].update({object_.action: operation})

        # print(paths)

        return paths

    @classmethod
    def _get_operation(cls, tag, link):
        _data = {
            'tags': link._tags,
            'description': link.description,
            'operationId': link.operationId,
            'responses': cls._get_responses(link),
            'parameters': cls._get_parameters(link.fields)
        }

        if link.requestBody:
            _data["requestBody"] = link.requestBody

        return _data

    @classmethod
    def _get_parameters(cls, fields):
        """
        Generates Swagger Parameter Item object.
        """
        return [
            {
                'name': field.name,
                'required': field.required,
                'in': cls._convert_location_to_in(field.location),
                'description': field.description,
                'schema': field.schema
            }
            for field in fields
        ]

    @classmethod
    def _convert_location_to_in(cls, location):
        """
        Translates the CoreAPI field `location` into the Swagger `in`.
        The values are all the same with the exception of form -> formData.
        """
        if location == 'form':
            return 'formData'

        return location

    @classmethod
    def _get_responses(cls, link):
        """
        Returns minimally acceptable responses object based
        on action / method type.
        """
        return link._template
