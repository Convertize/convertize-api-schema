import coreapi
import json
from collections import namedtuple

class ConvertizeLink(coreapi.Link):
    def __init__(self, url=None, action=None, encoding=None, transform=None, title=None, description=None, fields=None, template=None, tags=None, requestBody=None, operationId=None):
        super(ConvertizeLink, self).__init__(
            url=url,
            action=action,
            encoding=encoding,
            transform=transform,
            title=title,
            description=description,
            fields=fields
        )

        self._template = template
        self._tags = tags
        self._requestBody = requestBody
        self._operationId = operationId

    @property
    def requestBody(self):
        return self._requestBody

    @property
    def operationId(self):
        return self._operationId

class ConvertizeField(coreapi.Field):
    pass

def new_propertie(name, **kwargs):
    if "enum" in kwargs:
        kwargs = kwargs["enum"]

    # print(name)
    # print(kwargs)

    return (name, kwargs)

