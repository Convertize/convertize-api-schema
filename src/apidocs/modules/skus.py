import coreapi
from apidocs import modules

sku_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do SKU"),
    modules.new_propertie(name="product", type="integer", format="int4", description=u"ID do produto"),
    modules.new_propertie(name="title", type="string", description=u"Título do SKU"),
    modules.new_propertie(name="ean_13", type="integer", description=u"EAN13 ou Código de barras"),
    modules.new_propertie(name="referece_code", type="string", description=u"Código de referência ou código da grade no ERP"),
    modules.new_propertie(name="weight",type="string", description=u"Peso"),
    modules.new_propertie(name="height", type="float",description=u"Altura"),
    modules.new_propertie(name="width", type="float", description=u"Largura"),
    modules.new_propertie(name="depth",type="float", description=u"Profundidade"),
    modules.new_propertie(name="cost_price", type="float", description=u"Preço de Custo"),
    modules.new_propertie(name="unit_price", type="float", description=u"Preço de Venda"),
    modules.new_propertie(name="sale_price", type="float", description=u"Preço de Venda Promocional"),
    modules.new_propertie(name="stock", type="integer", format="int4", description=u"Estoque"),
    modules.new_propertie(name="reserves_stock", type="integer", format="int4", description=u"Estoque Reserva"),
    modules.new_propertie(name="minimum_stock", type="integer", format="int4", description=u"Estoque Mínimo"),
    modules.new_propertie(name="max_buy", type="integer", format="int4", description=u"Quantidade máxima de compra"),
    modules.new_propertie(name="available", type="boolean", description=u"Indica se o SKU esta disponivel para venda `default = true`"),
    modules.new_propertie(name="default", type="boolean", description=u"Indica se o SKU é o principal `default = false`"),
    modules.new_propertie(name="image", type="integer", description=u"ID da Imagem"),
    modules.new_propertie(name="options", type="array", format="int4", description="ID`s dos valores das opções do SKU"),
    modules.new_propertie(name="availability", type="integer", format="int4", description="Disponibilidade do SKU ou Tempo de manuseio do produto"),
    modules.new_propertie(name="sell_out_of_stock", type="boolean", description=u"Vender SKU sem estoque default = False")
])


skus_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=sku_componente)
        )))
    )))


sku_schema = modules.new_propertie(name="schema", type="object", properties=sku_componente, required=["id", "title"])



export = {
    "Skus": modules.ConvertizeLink(
        tags=["Skus"],
        url='/{environment}/api/v2/skus/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='referece_code', required=False, location='query', description=u"Código de referência ou código da grade no ERP"),
            coreapi.Field(name='ean_13', required=False, location='query', description=u"Filtro pelo EAN13 ou Código de barras"),            
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Sku`s',
        summary='',
        operationId='Lista de Sku`s',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                       skus_schema[0]: skus_schema[1],
                        "example": {
                            "count": 1,
                            "next": None,
                            "previous": None,
                            "results": [
                              {
                                "id": 1699,
                                "title": None,
                                "ean_13": None,
                                "reference_code": None,
                                "weight": "0.000",
                                "height": None,
                                "width": None,
                                "depth": None,
                                "cost_price": None,
                                "unit_price": None,
                                "sale_price": None,
                                "stock": 0,
                                "reserves_stock": 0,
                                "minimum_stock": 0,
                                "max_buy": None,
                                "available": True,
                                "default": False,
                                "add_date": "2016-10-08T12:52:37.028820",
                                "change_date": "2016-10-08T12:52:37.028856",
                                "options": [
                                    21,
                                    17
                                ],
                                "availability": None,
                                "sell_out_of_stock": False,
                                "product": 1664,
                                "image": None                                
                              },
                            {
                                "id": 1700,
                                "title": None,
                                "ean_13": None,
                                "reference_code": None,
                                "weight": "0.000",
                                "height": None,
                                "width": None,
                                "depth": None,
                                "cost_price": None,
                                "unit_price": None,
                                "sale_price": None,
                                "stock": 0,
                                "reserves_stock": 0,
                                "minimum_stock": 0,
                                "max_buy": None,
                                "available": True,
                                "default": False,
                                "add_date": "2016-10-08T12:52:37.286080",
                                "change_date": "2016-10-08T12:52:37.286104",
                                "options": [
                                    21,
                                    19
                                ],
                                "availability": None,
                                "sell_out_of_stock": False,
                                "product": 1664,
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
    "Sku": modules.ConvertizeLink(
        tags=["Skus"],
        url='/{environment}/api/v2/skus/{sku_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='referece_code', required=False, location='query', description=u"Código de referência ou código da grade no ERP"),
            coreapi.Field(name='ean_13', required=False, location='query', description=u"Filtro pelo EAN13 ou Código de barras"),            
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma SKU por `ID`',
        summary='',
        operationId='Detalhes de uma SKU',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    sku_schema[0]: sku_schema[1],
                    "example": {
                      "id": 1699,
                      "title": None,
                      "ean_13": None,
                      "reference_code": None,
                      "weight": "0.000",
                      "height": None,
                      "width": None,
                      "depth": None,
                      "cost_price": None,
                      "unit_price": None,
                      "sale_price": None,
                      "reserves_stock": 0,
                      "minimum_stock": 0,
                      "max_buy": None,
                      "available": True,
                      "default": False,
                      "add_date": "2016-10-08T12:52:37.028820",
                      "change_date": "2016-10-08T12:52:37.028856",
                      "options": [
                           21,
                           17
                    ],
                      "availability": None,
                      "sell_out_of_stock": None,
                      "product": 1664,
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
    "SkuCreate": modules.ConvertizeLink(
        tags=["Skus"],
        url='/{environment}/api/v2/skus/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar um Sku',
        summary='',
        operationId='Criar um Sku',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    sku_schema[0]: sku_schema[1],
                    "example": {
                        "id": 1699,
                        "weight": "0.000",
                        "stock": 0,
                        "reserves_stock": 0,
                        "minimum_stock": 0,
                        "available": True,
                        "default": False,
                        "options": [
                            21,
                            17
                        ],
                        "sell_out_of_stock": False,
                        "product": 1664
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
                    sku_schema[0]: sku_schema[1],
                    "example": {
                      "id": 1699,
                      "title": None,
                      "ean_13": None,
                      "reference_code": None,
                      "weight": "0.000",
                      "height": None,
                      "width": None,
                      "depth": None,
                      "cost_price": None,
                      "unit_price": None,
                      "sale_price": None,
                     "stock": 0,
                     "reserves_stock": 0,
                     "minimum_stock": 0,
                     "max_buy": None,
                     "available": True,
                     "default": False,
                     "add_date": "2016-10-08T12:52:37.028820",
                     "change_date": "2016-10-08T12:52:37.028856",
                     "options": [
                        21,
                        17
                    ],
                     "availability": None,
                     "sell_out_of_stock": False,
                     "product": 1664,
                     "image": None
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
    "SkuUpdate": modules.ConvertizeLink(
        tags=["Skus"],
        url='/{environment}/api/v2/skus/{sku_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='sku_id', required=True, location='path', description=u"ID do Produto", schema={"type": "integer"}),
        ],
        description='Alterar um Sku',
        summary='',
        operationId='Alterar um Sku',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    sku_schema[0]: sku_schema[1],
                    "example": {
                        "id": 1699,
                        "weight": "0.000",
                        "stock": 0,
                        "reserves_stock": 0,
                        "minimum_stock": 0,
                        "available": True,
                        "default": False,
                        "options": [
                            21,
                            17
                        ],
                        "sell_out_of_stock": False,
                        "product": 1664
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
                    sku_schema[0]: sku_schema[1],
                    "example": {
                      "id": 1699,
                      "title": None,
                      "ean_13": None,
                      "reference_code": None,
                      "weight": "0.000",
                      "height": None,
                      "width": None,
                      "depth": None,
                      "cost_price": None,
                      "unit_price": None,
                      "sale_price": None,
                      "stock": 0,
                      "reserves_stock": 0,
                      "minimum_stock": 0,
                      "max_buy": None,
                      "available": True,
                      "default": False,
                      "add_date": "2016-10-08T12:52:37.028820",
                      "change_date": "2016-10-08T12:52:37.028856",
                      "options": [
                         21,
                         17
                    ],
                      "availability": None,
                      "sell_out_of_stock": False,
                      "product": 1664,
                      "image": None
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
    "SkuDelete": modules.ConvertizeLink(
        tags=["Skus"],
        url='/{environment}/api/v2/skus/{sku_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='sku_id', required=True, location='path', description=u"ID do Produto", schema={"type": "integer"}),
        ],
        description='Deletar um Sku',
        summary='',
        operationId='Deletar um Sku',
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