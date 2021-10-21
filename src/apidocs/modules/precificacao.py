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
        url='/{environment}/api/v2/categories/',
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
                                },
                                {
                                    "id": 40,
                                    "table": 1,
                                    "sku": 1694,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 61,
                                    "table": 1,
                                    "sku": 1693,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 60,
                                    "table": 1,
                                    "sku": 1692,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 59,
                                    "table": 1,
                                    "sku": 1691,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 58,
                                    "table": 1,
                                    "sku": 1687,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 57,
                                    "table": 1,
                                    "sku": 1686,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 56,
                                    "table": 1,
                                    "sku": 1685,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 55,
                                    "table": 1,
                                    "sku": 1684,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 54,
                                    "table": 1,
                                    "sku": 1683,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 49,
                                    "table": 1,
                                    "sku": 1682,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 48,
                                    "table": 1,
                                    "sku": 1681,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 47,
                                    "table": 1,
                                    "sku": 1680,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 46,
                                    "table": 1,
                                    "sku": 1679,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 51,
                                    "table": 1,
                                    "sku": 1678,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 50,
                                    "table": 1,
                                    "sku": 1677,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 38,
                                    "table": 1,
                                    "sku": 1676,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 37,
                                    "table": 1,
                                    "sku": 1675,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 36,
                                    "table": 1,
                                    "sku": 1674,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 35,
                                    "table": 1,
                                    "sku": 1673,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 34,
                                    "table": 1,
                                    "sku": 1672,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 33,
                                    "table": 1,
                                    "sku": 1671,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 32,
                                    "table": 1,
                                    "sku": 1670,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 31,
                                    "table": 1,
                                    "sku": 1669,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 30,
                                    "table": 1,
                                    "sku": 1668,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 29,
                                    "table": 1,
                                    "sku": 1667,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 21,
                                    "table": 1,
                                    "sku": 1645,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 22,
                                    "table": 1,
                                    "sku": 1644,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 23,
                                    "table": 1,
                                    "sku": 1643,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 27,
                                    "table": 1,
                                    "sku": 1642,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 26,
                                    "table": 1,
                                    "sku": 1641,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 25,
                                    "table": 1,
                                    "sku": 1640,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 24,
                                    "table": 1,
                                    "sku": 1639,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 17,
                                    "table": 1,
                                    "sku": 1377,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 3,
                                    "table": 1,
                                    "sku": 106,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 12,
                                    "table": 1,
                                    "sku": 32,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 11,
                                    "table": 1,
                                    "sku": 31,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 10,
                                    "table": 1,
                                    "sku": 29,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 9,
                                    "table": 1,
                                    "sku": 28,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 8,
                                    "table": 1,
                                    "sku": 27,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 15,
                                    "table": 1,
                                    "sku": 26,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 6,
                                    "table": 1,
                                    "sku": 22,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 4,
                                    "table": 1,
                                    "sku": 21,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 5,
                                    "table": 1,
                                    "sku": 20,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "10.00000"
                                },
                                {
                                    "id": 16,
                                    "table": 1,
                                    "sku": 19,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 18,
                                    "table": 1,
                                    "sku": 18,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 39,
                                    "table": 1,
                                    "sku": 16,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 28,
                                    "table": 1,
                                    "sku": 15,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 14,
                                    "table": 1,
                                    "sku": 14,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 13,
                                    "table": 1,
                                    "sku": 12,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 20,
                                    "table": 1,
                                    "sku": 11,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 45,
                                    "table": 1,
                                    "sku": 10,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 43,
                                    "table": 1,
                                    "sku": 9,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 42,
                                    "table": 1,
                                    "sku": 8,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 41,
                                    "table": 1,
                                    "sku": 7,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 44,
                                    "table": 1,
                                    "sku": 6,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 62,
                                    "table": 1,
                                    "sku": 5,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 53,
                                    "table": 1,
                                    "sku": 4,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 52,
                                    "table": 1,
                                    "sku": 3,
                                    "value_type": "percent",
                                    "field_discount": "unit_price",
                                    "value": "0.00000"
                                },
                                {
                                    "id": 19,
                                    "table": 1,
                                    "sku": 2,
                                    "value_type": "nominal",
                                    "field_discount": "unit_price",
                                    "value": "750.00000"
                                },
                                {
                                    "id": 7,
                                    "table": 1,
                                    "sku": 1,
                                    "value_type": "percent",
                                    "field_discount": "sale_price",
                                    "value": "50.00000"
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