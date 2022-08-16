# coding: utf-8
import coreapi
from apidocs import modules

price_componente = dict([
    modules.new_propertie(name="id", type="integer", format="int4", nullable=False, description=u"ID do preço"),
    modules.new_propertie(name="table", type="integer", format="int4", nullable=False, description=u"ID da tabela"),
    modules.new_propertie(name="sku", type="integer", format="int4", nullable=False, description=u"ID do SKU"),
    modules.new_propertie(name="value_type", type="string",nullable=False, description=u"Tipo do valor (percent, nominal)"),
    modules.new_propertie(name="field_discount", type="string", nullable=False, description=u"Campo usado para calculo do desconto (cost_price, unit_price, sale_price)"),
    modules.new_propertie(name="value", type="float", description=u"Valor do desconto"),
])


prices_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "table"]),
            modules.new_propertie(name="properties", enum=price_componente)
        )))
    )))


price_schema = modules.new_propertie(name="schema", type="object", properties=price_componente, required=["id", "table"])


export = {
    "Prices": modules.ConvertizeLink(
        tags=["Precos"],
        url='/{environment}/api/v2/pricing/prices/skus',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=True, location='path', description=u"Filtro pelo ID do preço", schema={"type": "integer"}),
            coreapi.Field(name='table', required=True, location='path', description=u"Filtro pelo ID da tabela", schema={"type": "integer"}),
            coreapi.Field(name='sku', required=True, location='path', description=u"Filtro pelo ID do SKU", schema={"type": "integer"}),            
            coreapi.Field(name='sku__in', required=True, location='path', description=u"Filtro pela lista de ID do SKU separados por `,`", schema={"type": "integer"}) 
            ],
        description='Retorna uma lista de preços',
        summary='',
        operationId='Lista de Preços',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        prices_schema[0]: prices_schema[1],
                        "example": {
                            "count": 62,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                   "id": 64,
                                    "table": 1,
                                    "sku": 1696,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 63,
                                    "table": 1,
                                    "sku": 1695,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
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
    "Price": modules.ConvertizeLink(
        tags=["Precos"],
        url='/{environment}/api/v2/pricing/prices/skus/{price_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='price_id', required=True, location='path', description=u"ID relativo ao preço", schema={"type": "integer"}),
            coreapi.Field(name='table', required=True, location='path', description=u"Filtro pelo ID da tabela", schema={"type": "integer"}),
            coreapi.Field(name='sku', required=True, location='path', description=u"Filtro pelo ID do SKU", schema={"type": "integer"}),
            coreapi.Field(name='sku__in', required=True, location='path', description=u"Filtro pela lista de ID do SKU separados por `,`", schema={"type": "integer"})           
             ],
        description='Retorna um preço por `ID`',
        summary='',
        operationId='Detalhes do preço',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    price_schema[0]: price_schema[1],
                    "example": {
                        "id": 64,
                        "table": 1,
                        "sku": 1696,
                        "value_type": "percent",
                        "field_discount": "unit_price",
                        "value": "0.00000"
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
    "PriceCreate": modules.ConvertizeLink(
        tags=["Precos"],
        url='/{environment}/api/v2/pricing/prices/skus/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar Preço',
        summary='',
        operationId='Criar Preço',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "table"],
                    price_schema[0]: price_schema[1],
                    "example": {
                        "table": 1,
                        "sku": 1696,
                        "value_type": "percent",
                        "field_discount": "unit_price",
                        "value": "0.00000"
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
                    price_schema[0]: price_schema[1],
                    "example": {
                        "id": 64,
                        "table": 1,
                        "sku": 1696,
                        "value_type": "percent",
                        "field_discount": "unit_price",
                        "value": "0.00000"
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
    "PriceUpdate": modules.ConvertizeLink(
        tags=["Precos"],
        url='/{environment}/api/v2/pricing/prices/skus/{price_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='price_id', required=True, location='path', description=u"ID do preço", schema={"type": "integer"}),
        ],
        description='Alterar um Preço',
        summary='',
        operationId='Alterar um Preço',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "table"],
                    price_schema[0]: price_schema[1],
                    "example": {
                        "table": 1,
                        "sku": 1696,
                        "value_type": "percent",
                        "field_discount": "unit_price",
                        "value": "0.00000"
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
                    "required": ["id", "table"],
                    price_schema[0]: price_schema[1],
                    "example": {
                        "id": 64,
                        "table": 1,
                        "sku": 1696,
                        "value_type": "percent",
                        "field_discount": "unit_price",
                        "value": "0.00000"
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
    "PriceDelete": modules.ConvertizeLink(
        tags=["Precos"],
        url='/{environment}/api/v2/pricing/prices/skus/{price_id}',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='price_id', required=True, location='path', description=u"ID relativo ao preço", schema={"type": "integer"}),
        ],
        description='Deletar um Preço',
        summary='',
        operationId='Deletar um Preço',
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