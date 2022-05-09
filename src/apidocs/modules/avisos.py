# coding: utf-8

import coreapi 
from apidocs import modules

notice_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da categoria"),
    modules.new_propertie(name="name", type="string", nullable=False, description=u"Nome"),
    modules.new_propertie(name="email", type="string", nullable=False, description=u"Email"),
    modules.new_propertie(name="sent", type="boolean", nullable=False, description=u"Indica se o aviso foi enviado`default = true`"),
    modules.new_propertie(name="SKU", type="integer", nullable=False, description=u"Código SKU"),
])

notices_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=notice_componente)
        )))
    )))

notice_schema = modules.new_propertie(name="schema", type="object", properties=notice_componente, required=["id", "title"])

export = {
    "Notices": modules.ConvertizeLink(
        tags=["Avisos"],
        url='/{environment}/api/v2/letmeknow/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de avisos',
        summary='',
        operationId='Lista de avisos',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        notices_schema[0]: notices_schema[1],
                        "example": {
                            "count": 4,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "id": 4,
                                    "name": "wilker",
                                    "email": "wilker_ferreira@yahoo.com.br",
                                    "sent": True,
                                    "add_date": "2021-08-05T11:54:52.572183",
                                    "change_date": "2021-08-06T07:00:05.055349",
                                    "sku": 65
                                },
                                {
                                    "id": 3,
                                    "name": "wilker ferreira",
                                    "email": "wilker.ferreira@convertize.com.br",
                                    "sent": True,
                                    "add_date": "2021-08-05T11:54:44.838884",
                                    "change_date": "2021-08-06T07:00:05.078632",
                                    "sku": 65
                                },
                                {
                                    "id": 2,
                                    "name": "Wilker - Teste",
                                    "email": "wilker.ferreira@convertize.com.br",
                                    "sent": True,
                                    "add_date": "2021-08-05T11:36:41.705218",
                                    "change_date": "2021-08-30T10:27:42.785228",
                                    "sku": 77
                                },
                                {
                                    "id": 1,
                                    "name": "Felipe Teste",
                                    "email": "felipe.banqueri@convertize.com.br",
                                    "sent": True,
                                    "add_date": "2021-08-05T11:35:54.560656",
                                    "change_date": "2021-08-30T10:27:42.799118",
                                    "sku": 77
                                }
                            ]
                        }
                    },
                }
            },
            "401": {
                "description": "Permission Denied"
            },
            "403": {
                "description": "Forbidden"
            },
            "404": {
                "description": "Not Found"
            }
        }
    ),
    "Notice": modules.ConvertizeLink(
        tags=["Avisos"],
        url='/{environment}/api/v2/letmeknow/{notice_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='aviso_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma uma categoria por `ID`',
        summary='',
        operationId='Detalhes de uma Categoria',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    notice_schema[0]: notice_schema[1],
                    "example": {
                        "id": 2,
                        "name": "Wilker - Teste",
                        "email": "wilker.ferreira@convertize.com.br",
                        "sent": True,
                        "add_date": "2021-08-05T11:36:41.705218",
                        "change_date": "2021-08-30T10:27:42.785228",
                        "sku": 77
                    }
                },
            }
          },
          "401": {
            "description": "Permission Denied"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found"
          }
        }
    ),
    "NoticeCreate": modules.ConvertizeLink(
        tags=["Avisos"],
        url='/{environment}/api/v2/letmeknow/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar um Aviso',
        summary='',
        operationId='Criar um Aviso',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    notice_schema[0]: notice_schema[1],
                    "example": {
                        "name": "wilker",
                        "email": "wilker_ferreira@yahoo.com.br",
                        "sent": True,
                        "sku": 65
                    }
                }
            },
            "required": True
        },
        template={
            "201": {
            "description": "Created",
            "content": {
                "application/json": {
                    notice_schema[0]: notice_schema[1],
                    "example": {
                        "name": "wilker",
                        "email": "wilker_ferreira@yahoo.com.br",
                        "sent": True,
                        "add_date": "2021-08-05T11:54:52.572183",
                        "change_date": "2021-08-06T07:00:05.055349",
                        "sku": 65
                    }
                },
            }
          },
          "400": {
            "description": "Bad input"
          },
          "401": {
            "description": "Permission Denied"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found"
          }
        }
    ),
    "NoticeUpdate": modules.ConvertizeLink(
        tags=["Avisos"],
        url='/{environment}/api/v2/letmeknow/{notice_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='notice_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
        ],
        description='Alterar um Aviso',
        summary='',
        operationId='Alterar um Aviso',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    notice_schema[0]: notice_schema[1],
                    "example": {
                        "name": "wilker",
                        "email": "wilker_ferreira@yahoo.com.br",
                        "sent": True,
                        "sku": 65
                    }
                }
            },
            "required": True
        },
        template={
            "200": {
            "description": "Created",
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    notice_schema[0]: notice_schema[1],
                    "example": {
                        "name": "wilker",
                        "email": "wilker_ferreira@yahoo.com.br",
                        "sent": True,
                        "add_date": "2021-08-05T11:54:52.572183",
                        "change_date": "2021-08-06T07:00:05.055349",
                        "sku": 65
                    }
                },
            }
          },
          "400": {
            "description": "Bad input"
          },
          "401": {
            "description": "Permission Denied"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found"
          }
        }
    ),
    "NoticeDelete": modules.ConvertizeLink(
        tags=["Avisos"],
        url='/{environment}/api/v2/letmeknow/{notice_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='aviso_id', required=True, location='path', description=u"ID do aviso", schema={"type": "integer"}),
        ],
        description='Deletar um aviso',
        summary='',
        operationId='Deletar um aviso',
        template={
            "204": {
                "description": "Success",
            },
            "401": {
                "description": "Permission Denied"
            },
            "403": {
                "description": "Forbidden"
            },
            "404": {
                "description": "Not Found"
            }
        }
    )
}
