# coding: utf-8
import coreapi
from apidocs import modules


logistic_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do stock"),
    modules.new_propertie(name="sku", type="integer", nullable=False, format="int4", description=u"ID do SKU"),
    modules.new_propertie(name="quantity", type="integer", nullable=False, format="int4", description=u"Estoque"),
    modules.new_propertie(name="infinity", type="boolean", nullable=False, description=u"Indica se o estoque é infinito `default = false`"),
])


logistics_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=logistic_componente)
        )))
    )))


logistic_schema = modules.new_propertie(name="schema", type="object", properties=logistic_componente, required=["id", "title"])


export = {
    "Estoques": modules.ConvertizeLink(
        tags=["Estoques"],
        url='/{environment}/api/v2/logistics/stocks/skus/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='sku', required=True, location='query', description=u"Filtro pelo ID do SKU", schema={"type": "integer"}),
            coreapi.Field(name='sku__in', required=False, location='query', description=u"Filtro pela lista de ID do SKU separados por `,`", schema={"type": "string"}),
            coreapi.Field(name='quantity__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='quantity__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}), 
        ],
        description='Retorna uma lista de estoques',
        summary='',
        operationId='Lista de Estoques',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        logistics_schema[0]: logistics_schema[1],
                        "example": {
                            "count": 6,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "id": 1,
                                    "stock": 1,
                                    "parent": None,
                                    "sku": 1676,
                                    "quantity": 10,
                                    "slug": "borracharia",                                  
                                },
                                 {
                                    "id": 2,
                                    "stock": 1,
                                    "sku": 1669,
                                    "quantity": 5,
                                    "infinity": False
                                },
                                 {
                                    "id": 3,
                                    "stock": 1,
                                    "sku": 1,
                                    "quantity": 3,
                                    "infinity": False
                                },
                                  {
                                    "id": 4,
                                    "stock": 1,
                                    "sku": 2,
                                    "quantity": 3,
                                    "infinity": False
                                },
                                   {
                                    "id": 6,
                                    "stock": 2,
                                    "sku": 2,
                                    "quantity": 1,
                                    "infinity": False
                                },
                                {
                                    "id": 5,
                                    "stock": 2,
                                    "sku": 1,
                                    "quantity": 1,
                                    "infinity": False
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
    "Estoque": modules.ConvertizeLink(
        tags=["Estoques"],
        url='/{environment}/api/v2/categories/stocks/skus/{sku_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='sku_id', required=True, location='query', description=u"Filtro pelo ID do SKU", schema={"type": "integer"}),
            coreapi.Field(name='sku__in', required=False, location='query', description=u"Filtro pela lista de ID do SKU separados por `,`", schema={"type": "string"}),
            coreapi.Field(name='quantity__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='quantity__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),     
        ],
        description='Retorna um SKU por `ID`',
        summary='',
        operationId='Detalhes de um SKU',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    logistic_schema[0]: logistic_schema[1],
                    "example": {
                        "id": 1,
                        "stock": 1,
                        "sku": 1676,
                        "quantity": 10,
                        "infinity": False
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
    "EstoqueCreate": modules.ConvertizeLink(
        tags=["Estoques"],
        url='/{environment}/api/v2/logistics/stocks/skus/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar Estoque',
        summary='',
        operationId='Criar Estoque',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "sku"],
                    logistic_schema[0]: logistic_schema[1],
                    "example": {
                        "stock": 1,
                        "sku": 1676,
                        "quantity": 10,
                        "infinity": False
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
                    logistic_schema[0]: logistic_schema[1],
                    "example": {
                        "id": 1,
                        "stock": 1,
                        "sku": 1676,
                        "quantity": 10,
                        "infinity": False
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
    "EstoqueUpdate": modules.ConvertizeLink(
        tags=["Estoques"],
        url='/{environment}/api/v2/logistics/stocks/skus/{id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=True, location='path', description=u"ID do estoque", schema={"type": "integer"}),
        ],
        description='Alterar Estoque',
        summary='',
        operationId='Alterar Estoque',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "sku"],
                    logistic_schema[0]: logistic_schema[1],
                    "example": {
                        "stock": 1,
                        "sku": 1676,
                        "quantity": 10,
                        "infinity": False
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
                    "required": ["id", "sku"],
                    logistic_schema[0]: logistic_schema[1],
                    "example": {
                        "id": 1,
                        "stock": 1,
                        "sku": 1676,
                        "quantity": 10,
                        "infinity": False
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
    "EstoqueDelete": modules.ConvertizeLink(
        tags=["Estoques"],
        url='/{environment}/api/v2/logistics/stocks/skus/{stock_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='stock_id', required=True, location='path', description=u"ID do estoque", schema={"type": "integer"}),
        ],
        description='Deletar um Estoque',
        summary='',
        operationId='Deletar um Estoque',
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
