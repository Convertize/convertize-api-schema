# coding: utf-8

import coreapi
from apidocs import modules

freight_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do frete"),
    modules.new_propertie(name="zipcode", type="integer", nullable=False, description=u"Código postal"),
    modules.new_propertie(name="amount", type="float", nullable=False, description=u"Quantidade de itens no carrinho"),
    modules.new_propertie(name="items", type="array", nullable=False, description=u"Itens"),
    modules.new_propertie(name="weight", type="float", nullable=False, description=u"Peso"),
    modules.new_propertie(name="ean_13", type="integer", nullable=False, description=u"Código de barras"),
    modules.new_propertie(name="height", type="float", nullable=False, description=u"Altura"),
    modules.new_propertie(name="width", type="float",nullable=False, description=u"Largura"),
    modules.new_propertie(name="reference_code", type="integer", nullable=False, description=u"Código de referência SKU"),
    modules.new_propertie(name="depth", type="float", nullable=False, description=u"Profundidade"),
    modules.new_propertie(name="quantity", type="integer", nullable=False, description=u"Quantidade")
])

freights_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "title"]),
        modules.new_propertie(name="properties", enum=freight_componente)
    )))
)))


freight_schema = modules.new_propertie(
    name="schema", type="object", properties=freight_componente, required=["id", "title"])

export = {
    "Fretes": modules.ConvertizeLink(
        tags=["Fretes"],
        url='/{environment}/api/v2/calculate/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de fretes',
        summary='',
        operationId='Lista de Fretes',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        freights_schema[0]: freights_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/calculate/?page=2",
                            "previous": None,
                            "results": [
                                {
                                    "services": [{
                                        "price": 0,
                                        "original_price": 0,
                                        "delivery_time": 2,
                                        "original_delivery_time": 2,
                                        "label": "Clique e Retire - Grátis - Até 2h",
                                        "service": "CLICK_RETIRE",
                                        "pickup_store": True,
                                        "pickups": [
                                            74,
                                            75,
                                            77,
                                            79,
                                            82
                                        ],
                                        "scheduled_deliveries_times": None
                                    },
                                        {
                                        "price": 0.0,
                                        "original_price": 0.0,
                                        "delivery_time": 2,
                                        "original_delivery_time": 2,
                                        "label": "Clique e Retire - Grátis - Até 2h",
                                        "service": "CLICK_RETIRE",
                                        "pickups": [
                                            2,
                                            3,
                                            4
                                        ],
                                        "scheduled_deliveries_times":None
                                    }
                                    ]
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
    "Frete": modules.ConvertizeLink(
        tags=["Fretes"],
        url='/{environment}/api/v2/calculate/{freight_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='freight_id', required=True, location='path',
                          description=u"ID do frete", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna frete por `ID`',
        summary='',
        operationId='Detalhes do frete',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        freight_schema[0]: freight_schema[1],
                        "results": [
                            {
                                "services": [{
                                    "price": 5.90,
                                    "delivery_time": 4,
                                    "original_delivery_time": 4,
                                    "label": "Motoboy - Grátis - Até 1 dia útil",
                                    "service": "MOTOBOY",
                                    "pickups": [
                                        31
                                    ],
                                    "scheduled_deliveries_times": None,
                                },
                                    {
                                    "price": 0.0,
                                    "original_price": 0.0,
                                    "delivery_time": 2,
                                    "original_delivery_time": 2,
                                    "label": "Clique e Retire - Grátis - Até 2h",
                                    "service": "CLICK_RETIRE",
                                    "pickups": [
                                        2,
                                        3,
                                        4
                                    ],
                                    "scheduled_deliveries_times":None
                                }
                                ]
                            }
                        ]
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
    "FreightCreate": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/calculate/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar frete',
        summary='',
        operationId='Criar frete',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    freight_schema[0]: freight_schema[1],
                    "example": {
                        "zipcode": "14015130",
                        "amount": "190.00000",
                        "items": [{
                            "weight": "",
                            "ean_13": "0123456789012",
                            "height": "100.000",
                            "width": "0.349",
                            "depth": "0.410",
                            "reference_code": None,
                            "id": 2,
                            "quantity": 1
                        },
                            {
                            "weight": "6.350",
                            "ean_13": "978020137962",
                            "height": "71.000",
                            "width": "0.500",
                            "depth": "0.250",
                            "reference_code": "123",
                            "id": 1,
                            "quantity": 1

                        }
                        ]
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
                        freight_schema[0]: freight_schema[1],
                        "example": {
                            "results": [
                                {
                                    "services": [{
                                        "price": 0,
                                        "original_price": 0,
                                        "delivery_time": 2,
                                        "original_delivery_time": 2,
                                        "label": "Clique e Retire - Grátis - Até 2h",
                                        "service": "CLICK_RETIRE",
                                        "pickup_store": True,
                                        "pickups": [
                                            74,
                                            75,
                                            77,
                                            79,
                                            82
                                        ],
                                        "scheduled_deliveries_times": None,
                                    },
                                        {
                                        "price": 0.0,
                                        "original_price": 0.0,
                                        "delivery_time": 2,
                                        "original_delivery_time": 2,
                                        "label": "Clique e Retire - Grátis - Até 2h",
                                        "service": "CLICK_RETIRE",
                                        "pickups": [
                                            2,
                                            3,
                                            4
                                        ],
                                        "scheduled_deliveries_times":None
                                    }
                                    ]
                                }
                            ]
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
    "FreightDelete": modules.ConvertizeLink(
        tags=["Fretes"],
        url='/{environment}/api/v2/calculate/{freight_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='categorie_id', required=True, location='path',
                          description=u"ID da categoria", schema={"type": "integer"}),
        ],
        description='Deletar Frete',
        summary='',
        operationId='Deletar Frete',
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
