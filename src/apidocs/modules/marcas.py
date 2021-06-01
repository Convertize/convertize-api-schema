# coding: utf-8
import coreapi
from apidocs import modules


brand_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da Marca"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título"),
    modules.new_propertie(name="slug", type="string", nullable=False, description=u"Slug `(url)`, caso vazio o sistema gera automaticamente"),
    modules.new_propertie(name="active", type="boolean", nullable=False, description=u"Indica se esta ativo `default = true`"),
    modules.new_propertie(name="description", type="string", nullable=False, description=u"Descrição da mrca para SEO"),
    modules.new_propertie(name="keywords", type="string", nullable=False, description=u"Keywords da marca para SEO separadas por `“,”`"),
    modules.new_propertie(name="image", type="string", nullable=False, description=u"URL da imagem"),
])

brands_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=brand_componente)
        )))
    )))

brand_schema = modules.new_propertie(name="schema", type="object", properties=brand_componente, required=["id", "title"])



export = {
    "Marcas": modules.ConvertizeLink(
        tags=["Marcas"],
        url='/{environment}/api/v2/brands/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID da marca", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Marcas',
        summary='',
        operationId='Lista de Marcas',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        brands_schema[0]: brands_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/brands/?page=2",
                            "previous": None,
                            "results": [
                              {
                                "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/brands/735/",
                                "id": 735,
                                "title": "ACR",
                                "slug": "acr",
                                "active": True,
                                "description": "",
                                "keywords": "",
                                "add_date": "2014-08-01T16:27:17.913597",
                                "change_date": "2014-08-01T16:27:17.913621",
                                "image": None
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
    "Marca": modules.ConvertizeLink(
        tags=["Marcas"],
        url='/{environment}/api/v2/brands/{brand_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='brand_id', required=True, location='path', description=u"ID da Marca", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma uma Marca por `ID`',
        summary='',
        operationId='Detalhes de uma Marcas',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    brand_schema[0]: brand_schema[1],
                    "example": {
                      "id": 735,
                      "title": "ACR",
                      "slug": "acr",
                      "active": True,
                      "description": "",
                      "keywords": "",
                      "add_date": "2014-08-01T16:27:17.913597",
                      "change_date": "2014-08-01T16:27:17.913621",
                      "image": None
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
    "MarcaCreate": modules.ConvertizeLink(
        tags=["Marcas"],
        url='/{environment}/api/v2/brands/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Marca\n\nAo contrário de outras solicitações de API, os arquivos devem ser carregados usando o tipo de conteúdo (content-type): multipart/form-data',
        summary='',
        operationId='Criar uma Marca',
        requestBody={
            "content": {
                "multipart/form-data": {
                    "required": ["id", "title"],
                    brand_schema[0]: brand_schema[1],
                    "example": {
                      "image": "logo.png",
                      "title": "TESTE",
                      "slug": "teste",
                      "active": True,
                      "description": None,
                      "keywords": None
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
                    brand_schema[0]: brand_schema[1],
                    "example": {
                      "id": 790,
                      "title": "TESTE",
                      "slug": "teste",
                      "active": True,
                      "description": None,
                      "keywords": None,
                      "add_date": "2016-10-07T19:06:06.076498",
                      "change_date": "2016-10-07T19:06:06.076534",
                      "image": "https://api.convertize.com.br/{ENVIRONMENT}/products/brands/2016/logo.png"
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
    "MarcaUpdate": modules.ConvertizeLink(
        tags=["Marcas"],
        url='/{environment}/api/v2/brands/{brand_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='brand_id', required=True, location='path', description=u"ID da Marca", schema={"type": "integer"}),
        ],
        description='Alterar uma Marca\n\nAo contrário de outras solicitações de API, os arquivos devem ser carregados usando o tipo de conteúdo (content-type): multipart/form-data',
        summary='',
        operationId='Alterar uma Marca',
        requestBody={
            "content": {
                "multipart/form-data": {
                    "required": ["id", "title"],
                    brand_schema[0]: brand_schema[1],
                    "example": {
                      "image": "logo.png",
                      "title": "TESTE",
                      "slug": "teste",
                      "active": True,
                      "description": None,
                      "keywords": None
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
                    brand_schema[0]: brand_schema[1],
                    "example": {
                      "id": 790,
                      "title": "TESTE",
                      "slug": "teste",
                      "active": True,
                      "description": None,
                      "keywords": None,
                      "add_date": "2016-10-07T19:06:06.076498",
                      "change_date": "2016-10-07T19:06:06.076534",
                      "image": "https://api.convertize.com.br/{ENVIRONMENT}/products/brands/2016/logo.png"
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
    "MarcaDelete": modules.ConvertizeLink(
        tags=["Marcas"],
        url='/{environment}/api/v2/brands/{brand_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='brand_id', required=True, location='path', description=u"ID da Marca", schema={"type": "integer"}),
        ],
        description='Deletar uma Marca',
        summary='',
        operationId='Deletar uma Marca',
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
