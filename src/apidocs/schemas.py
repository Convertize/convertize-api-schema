# -*- coding: utf-8 -*-
import os
import pkgutil
import coreapi

from utils import import_string

content = {}

for loader, module_name, is_pkg in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), "modules")]):
    if not is_pkg:
        export = import_string("apidocs.modules.{}.export".format(module_name))
        content.update(export)

class ConvertizeDocument(coreapi.Document):
    def __init__(self, url=None, title=None, description=None, media_type=None, content=None, version=None, termsOfService=None, license=None, contact=None, servers=None, tags=None):
        super(ConvertizeDocument, self).__init__(
            url=url,
            title=title,
            description=description,
            media_type=media_type,
            content=content,
        )

        self._version = version
        self._termsOfService = termsOfService
        self._license = license
        self._contact = contact
        self._servers = servers
        self._tags = tags

    @property
    def version(self):
        return self._version

    @property
    def termsOfService(self):
        return self._termsOfService

    @property
    def license(self):
        return self._license

    @property
    def contact(self):
        return self._contact

    @property
    def servers(self):
        return self._servers

    @property
    def tags(self):
        return self._tags


schema = ConvertizeDocument(
    title='API Reference',
    content=content,
    version="v2",
    description="Convertize Privated API",
    termsOfService="https://compliance.convertize.com.br/",
    license={
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    },
    contact={
      "email": "dev@convertize.com.br"
    },
    servers=[{
        "url": "https://api.convertize.com.br"
    }],
    tags=[{
      "name": "Customers",
      "description": "Endpoints for customers",
      "externalDocs": {
        "description": "Found an error? Let us know.",
        "url": "https://github.com/convertize/convertize-api-docs/issues/new/?title=API%20Documentation%20Error:%20/api/customers/&template=api_error_template.md"
      }
    },
    {
      "name": "Integration",
      "x-sidebar-name": "Integration API",
      "description": "Endpoints for the integration api",
      "externalDocs": {
        "description": "Found an error? Let us know.",
        "url": "https://github.com/convertize/convertize-api-docs/issues/new/?title=API%20Documentation%20Error:%20/api/integration-platform/&template=api_error_template.md"
      }
    }]
)