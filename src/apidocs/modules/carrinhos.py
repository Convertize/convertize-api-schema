# coding: utf-8
import coreapi
from apidocs import modules

cart_componente = dict([
    modules.new_propertie(name="id", type="integer", format="int64", nullable=False, description=u"ID do carrinho"),
    modules.new_propertie(name="status", type="string", nullable=False, description=u"Status do carrinho"),
    modules.new_propertie(name="customer", type="object",  nullable=False, description=u"Informações do cliente."),
    modules.new_propertie(name="utm_partner", type="string",description=u"Inserir UTM partner"),
    modules.new_propertie(name="utm_medium", type="string",  description=u"Inserir UTM medium"),
    modules.new_propertie(name="utm_source", type="string", description=u"Inserir UTM source"),
    modules.new_propertie(name="utm_campaign", type="string",description=u"Inserir UTM campaign"),
    modules.new_propertie(name="token_remake", type="string", description=u"Token gerado para refazer carrinho."),
    modules.new_propertie(name="payment_method", type="string", description=u"Forma de Pagamento"),
    modules.new_propertie(name="payment_discount",type="float", description=u"Desconto"),
    modules.new_propertie(name="payment_interest", type="float", description=u"Juros de pagamento"),
    modules.new_propertie(name="installment",type="integer", description=u"Parcelas"),
    modules.new_propertie(name="items", type="list", description=u"Lista de items do carrinho"),
    modules.new_propertie(name="order", type="integer",description=u"Número do pedido"),
    modules.new_propertie(name="seller", type="object",description=u"Vendedor.")
])


carts_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True,
                          description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True,
                          description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False,
                          description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "status"]),
        modules.new_propertie(name="properties", enum=cart_componente)
    )))
)))


cart_schema = modules.new_propertie(
    name="schema", type="object", properties=cart_componente, required=["id", "status"])


export = {
    "Carrinhos": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v1/carts/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query',
                          description=u"Filtro pelo ID do carrinho", schema={"type": "string"}),
            coreapi.Field(name='status', required=False, location='query',
                          description=u"Filtro pelo status do carrinho", schema={"type": "string"}),
            coreapi.Field(name='order', required=False, location='query',
                          description=u"Filtro pelo número do pedido", schema={"type": "integer"}),
            coreapi.Field(name='seller', required=False, location='query',
                          description=u"Filtro pelo vendedor", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Carrinhos',
        summary='',
        operationId='Lista de Carrinhos',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        carts_schema[0]: carts_schema[1],
                        "example": {
                            "count": 312,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/1.0/carts/?page=2",
                            "previous": None,
                            "results": [
                                {
                                    "id": 1496,
                                    "add_date": "2021-10-20T16:14:29.634520",
                                    "last_updated": "2021-10-20T18:00:16.555955",
                                    "status": "declined",
                                    "customer": {
                                        "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                                        "id": 71,
                                        "reference_code": None,
                                        "email": "felipe.banqueri@convertize.com.br",
                                        "document": "43381727893",
                                        "corporate_document": None,
                                        "name": "Felipe Banqueri",
                                        "corporate_name": None,
                                        "inscricao_estadual_isento": False,
                                        "inscricao_estadual": None,
                                        "fancy_name": None,
                                        "birthdate": None,
                                        "gender": None,
                                        "blocked": False,
                                        "newsletter": 0,
                                        "gdpr_agreement": False,
                                        "receiver": "Felipe Banqueri",
                                        "zipcode": "14060360",
                                        "address": "R DAVID SALOMÃO",
                                        "number": "943",
                                        "neighborhood": "JD JANDAIA",
                                        "complement": None,
                                        "city": "RIBEIRÃO PRETO",
                                        "state": "SP",
                                        "phone1": "16991985427",
                                        "phone2": None,
                                        "reference": None,
                                        "city_id": "9560",
                                        "code_ibge": "3543402",
                                        "add_date": "2021-05-24T08:07:37.693385",
                                        "change_date": "2021-08-30T10:51:38.461233",
                                        "limit_credit": None,
                                        "balance_of_credit": None,
                                        "group": None
                                    },
                                    "utm_partner": None,
                                    "utm_medium": None,
                                    "utm_source": None,
                                    "utm_campaign": None,
                                    "token_remake": "603AF534F764486AAC188996DAA7B63D",
                                    "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                                    "payment_method": "CartaoDeCredito",
                                    "payment_discount": "0.00",
                                    "payment_interest": "0.00",
                                    "installment": 1,
                                    "items": [
                                        {
                                            "id": 583,
                                            "cart": 1496,
                                            "description": "Pantufa Big Iron",
                                            "sku": {
                                                "id": 63,
                                                "product": 45,
                                                "title": None,
                                                "ean_13": None,
                                                "reference_code": None,
                                                "weight": "0.000",
                                                "height": None,
                                                "width": None,
                                                "depth": None,
                                                "cost_price": None,
                                                "unit_price": "99.00000",
                                                "sale_price": None,
                                                "min_seller_sale_price": None,
                                                "loyalty_price": None,
                                                "percentage_discount_price": None,
                                                "stock": 9,
                                                "multiple_stock": 1,
                                                "reserves_stock": 2,
                                                "minimum_stock": 0,
                                                "max_buy": None,
                                                "available": True,
                                                "default": True,
                                                "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                                "add_date": "2021-05-04T11:03:28.210257",
                                                "change_date": "2021-10-20T16:14:14.988085",
                                                "options": None,
                                                "availability": None,
                                                "sell_out_of_stock": False
                                            },
                                            "quantity": 1,
                                            "original_price": "99.00000",
                                            "unit_price": "99.00000",
                                            "total_price": "99.00000",
                                            "manual_price": None,
                                            "discount": "0.00000",
                                            "unit_discount": "0.00000",
                                            "url": "/pantufa-big-iron/p",
                                            "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                            "parent": None,
                                            "required": False,
                                            "is_gift": False,
                                            "is_bundle": False,
                                            "extra_data": None
                                        }
                                    ],
                                    "order": None,
                                    "seller": None
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
    "Carrinho": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v1/carts/{cart_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='cart_id', required=True, location='path',
                          description=u"ID do carrinho", schema={"type": "integer"}),
            coreapi.Field(name='status', required=False, location='query',
                          description=u"Filtro pelo status do carrinho", schema={"type": "string"}),
            coreapi.Field(name='order', required=False, location='query',
                          description=u"Filtro pelo número do pedido", schema={"type": "integer"}),
            coreapi.Field(name='seller', required=False, location='query',
                          description=u"Filtro pelo vendedor", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna um Carrinho por `ID`',
        summary='',
        operationId='Detalhes de um Carrinho',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        cart_schema[0]: cart_schema[1],
                        "example": {
                            "id": 1496,
                            "add_date": "2021-10-20T16:14:29.634520",
                            "last_updated": "2021-10-20T18:00:16.555955",
                            "status": "declined",
                            "customer": {
                                "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                                "id": 71,
                                "reference_code": None,
                                "email": "felipe.banqueri@convertize.com.br",
                                "document": "43381727893",
                                "corporate_document": None,
                                "name": "Felipe Banqueri",
                                "corporate_name": None,
                                "inscricao_estadual_isento": False,
                                "inscricao_estadual": None,
                                "fancy_name": None,
                                "birthdate": None,
                                "gender": None,
                                "blocked": False,
                                "newsletter": 0,
                                "gdpr_agreement": False,
                                "receiver": "Felipe Banqueri",
                                "zipcode": "14060360",
                                "address": "R DAVID SALOMÃO",
                                "number": "943",
                                "neighborhood": "JD JANDAIA",
                                "complement": None,
                                "city": "RIBEIRÃO PRETO",
                                "state": "SP",
                                "phone1": "16991985427",
                                "phone2": None,
                                "reference": None,
                                "city_id": "9560",
                                "code_ibge": "3543402",
                                "add_date": "2021-05-24T08:07:37.693385",
                                "change_date": "2021-08-30T10:51:38.461233",
                                "limit_credit": None,
                                "balance_of_credit": None,
                                "group": None
                            },
                            "utm_partner": None,
                            "utm_medium": None,
                            "utm_source": None,
                            "utm_campaign": None,
                            "token_remake": "603AF534F764486AAC188996DAA7B63D",
                            "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                            "payment_method": "CartaoDeCredito",
                            "payment_discount": "0.00",
                            "payment_interest": "0.00",
                            "installment": 1,
                            "items": [
                                    {
                                        "id": 583,
                                        "cart": 1496,
                                        "description": "Pantufa Big Iron",
                                        "sku": {
                                            "id": 63,
                                            "product": 45,
                                            "title": None,
                                            "ean_13": None,
                                            "reference_code": None,
                                            "weight": "0.000",
                                            "height": None,
                                            "width": None,
                                            "depth": None,
                                            "cost_price": None,
                                            "unit_price": "99.00000",
                                            "sale_price": None,
                                            "min_seller_sale_price": None,
                                            "loyalty_price": None,
                                            "percentage_discount_price": None,
                                            "stock": 9,
                                            "multiple_stock": 1,
                                            "reserves_stock": 2,
                                            "minimum_stock": 0,
                                            "max_buy": None,
                                            "available": True,
                                            "default": True,
                                            "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                            "add_date": "2021-05-04T11:03:28.210257",
                                            "change_date": "2021-10-20T16:14:14.988085",
                                            "options": None,
                                            "availability": None,
                                            "sell_out_of_stock": False
                                        },
                                        "quantity": 1,
                                        "original_price": "99.00000",
                                        "unit_price": "99.00000",
                                        "total_price": "99.00000",
                                        "manual_price": None,
                                        "discount": "0.00000",
                                        "unit_discount": "0.00000",
                                        "url": "/pantufa-big-iron/p",
                                        "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                        "parent": None,
                                        "required": False,
                                        "is_gift": False,
                                        "is_bundle": False,
                                        "extra_data": None
                                    }
                            ],
                            "order": None,
                            "seller": None
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
    "Carrinho": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v1/carts/{cart_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='cart_id', required=True, location='path',
                          description=u"ID do carrinho", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna um Carrinho por `ID`',
        summary='',
        operationId='Detalhes de um Carrinho',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        cart_schema[0]: cart_schema[1],
                        "example": {
                            "id": 1496,
                            "add_date": "2021-10-20T16:14:29.634520",
                            "last_updated": "2021-10-20T18:00:16.555955",
                            "status": "declined",
                            "customer": {
                                "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                                "id": 71,
                                "reference_code": None,
                                "email": "felipe.banqueri@convertize.com.br",
                                "document": "43381727893",
                                "corporate_document": None,
                                "name": "Felipe Banqueri",
                                "corporate_name": None,
                                "inscricao_estadual_isento": False,
                                "inscricao_estadual": None,
                                "fancy_name": None,
                                "birthdate": None,
                                "gender": None,
                                "blocked": False,
                                "newsletter": 0,
                                "gdpr_agreement": False,
                                "receiver": "Felipe Banqueri",
                                "zipcode": "14060360",
                                "address": "R DAVID SALOMÃO",
                                "number": "943",
                                "neighborhood": "JD JANDAIA",
                                "complement": None,
                                "city": "RIBEIRÃO PRETO",
                                "state": "SP",
                                "phone1": "16991985427",
                                "phone2": None,
                                "reference": None,
                                "city_id": "9560",
                                "code_ibge": "3543402",
                                "add_date": "2021-05-24T08:07:37.693385",
                                "change_date": "2021-08-30T10:51:38.461233",
                                "limit_credit": None,
                                "balance_of_credit": None,
                                "group": None
                            },
                            "utm_partner": None,
                            "utm_medium": None,
                            "utm_source": None,
                            "utm_campaign": None,
                            "token_remake": "603AF534F764486AAC188996DAA7B63D",
                            "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                            "payment_method": "CartaoDeCredito",
                            "payment_discount": "0.00",
                            "payment_interest": "0.00",
                            "installment": 1,
                            "items": [
                                    {
                                        "id": 583,
                                        "cart": 1496,
                                        "description": "Pantufa Big Iron",
                                        "sku": {
                                            "id": 63,
                                            "product": 45,
                                            "title": None,
                                            "ean_13": None,
                                            "reference_code": None,
                                            "weight": "0.000",
                                            "height": None,
                                            "width": None,
                                            "depth": None,
                                            "cost_price": None,
                                            "unit_price": "99.00000",
                                            "sale_price": None,
                                            "min_seller_sale_price": None,
                                            "loyalty_price": None,
                                            "percentage_discount_price": None,
                                            "stock": 9,
                                            "multiple_stock": 1,
                                            "reserves_stock": 2,
                                            "minimum_stock": 0,
                                            "max_buy": None,
                                            "available": True,
                                            "default": True,
                                            "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                            "add_date": "2021-05-04T11:03:28.210257",
                                            "change_date": "2021-10-20T16:14:14.988085",
                                            "options": None,
                                            "availability": None,
                                            "sell_out_of_stock": False
                                        },
                                        "quantity": 1,
                                        "original_price": "99.00000",
                                        "unit_price": "99.00000",
                                        "total_price": "99.00000",
                                        "manual_price": None,
                                        "discount": "0.00000",
                                        "unit_discount": "0.00000",
                                        "url": "/pantufa-big-iron/p",
                                        "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                        "parent": None,
                                        "required": False,
                                        "is_gift": False,
                                        "is_bundle": False,
                                        "extra_data": None
                                    }
                            ],
                            "order": None,
                            "seller": None
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
    "CarrinhosDeclined": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v1/carts/?status=declined',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='status', required=False, location='query',
                          description=u"Status do carrinho", schema={"type": "string"}),

        ],
        description='Retorna uma lista de Carrinhos com status `declined`',
        summary='',
        operationId='Lista de carrinhos com status `declined`',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        carts_schema[0]: carts_schema[1],
                        "example": {
                            "count": 160,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/carts/?page=2&status=declined",
                            "previous": None,
                            "results": [
                                {
                                    "id": 1496,
                                    "add_date": "2021-10-20T16:14:29.634520",
                                    "last_updated": "2021-10-20T18:00:16.555955",
                                    "status": "declined",
                                    "customer": {
                                        "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                                        "id": 71,
                                        "reference_code": None,
                                        "email": "felipe.banqueri@convertize.com.br",
                                        "document": "43381727893",
                                        "corporate_document": None,
                                        "name": "Felipe Banqueri",
                                        "corporate_name": None,
                                        "inscricao_estadual_isento": False,
                                        "inscricao_estadual": None,
                                        "fancy_name": None,
                                        "birthdate": None,
                                        "gender": None,
                                        "blocked": False,
                                        "newsletter": 0,
                                        "gdpr_agreement": False,
                                        "receiver": "Felipe Banqueri",
                                        "zipcode": "14060360",
                                        "address": "R DAVID SALOMÃO",
                                        "number": "943",
                                        "neighborhood": "JD JANDAIA",
                                        "complement": None,
                                        "city": "RIBEIRÃO PRETO",
                                        "state": "SP",
                                        "phone1": "16991985427",
                                        "phone2": None,
                                        "reference": None,
                                        "city_id": "9560",
                                        "code_ibge": "3543402",
                                        "add_date": "2021-05-24T08:07:37.693385",
                                        "change_date": "2021-08-30T10:51:38.461233",
                                        "limit_credit": None,
                                        "balance_of_credit": None,
                                        "group": None
                                    },
                                    "utm_partner": None,
                                    "utm_medium": None,
                                    "utm_source": None,
                                    "utm_campaign": None,
                                    "token_remake": "603AF534F764486AAC188996DAA7B63D",
                                    "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                                    "payment_method": "CartaoDeCredito",
                                    "payment_discount": "0.00",
                                    "payment_interest": "0.00",
                                    "installment": 1,
                                    "items": [
                                        {
                                            "id": 583,
                                            "cart": 1496,
                                            "description": "Pantufa Big Iron",
                                            "sku": {
                                                "id": 63,
                                                "product": 45,
                                                "title": None,
                                                "ean_13": None,
                                                "reference_code": None,
                                                "weight": "0.000",
                                                "height": None,
                                                "width": None,
                                                "depth": None,
                                                "cost_price": None,
                                                "unit_price": "99.00000",
                                                "sale_price": None,
                                                "min_seller_sale_price": None,
                                                "loyalty_price": None,
                                                "percentage_discount_price": None,
                                                "stock": 9,
                                                "multiple_stock": 1,
                                                "reserves_stock": 2,
                                                "minimum_stock": 0,
                                                "max_buy": None,
                                                "available": True,
                                                "default": True,
                                                "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                                "add_date": "2021-05-04T11:03:28.210257",
                                                "change_date": "2021-10-20T16:14:14.988085",
                                                "options": None,
                                                "availability": None,
                                                "sell_out_of_stock": False
                                            },
                                            "quantity": 1,
                                            "original_price": "99.00000",
                                            "unit_price": "99.00000",
                                            "total_price": "99.00000",
                                            "manual_price": None,
                                            "discount": "0.00000",
                                            "unit_discount": "0.00000",
                                            "url": "/pantufa-big-iron/p",
                                            "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                            "parent": None,
                                            "required": False,
                                            "is_gift": False,
                                            "is_bundle": False,
                                            "extra_data": None
                                        }
                                    ],
                                    "order": None,
                                    "seller": None
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
    "CarrinhoUpdate": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v2/carts/{cart_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='cart_id', required=True, location='path',
                          description=u"ID do Carrinho", schema={"type": "integer"}),
        ],
        description='Alterar Carrinho',
        summary='',
        operationId='Alterar um Carrinho',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "status"],
                    cart_schema[0]: cart_schema[1],
                    "example": {
                        "image": "logo.png",
                        "last_updated": "2021-10-20T18:00:16.555955",
                        "status": "declined",
                        "customer": {
                            "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                            "id": 71,
                            "reference_code": None,
                            "email": "felipe.banqueri@convertize.com.br",
                            "document": "43381727893",
                            "corporate_document": None,
                            "name": "Felipe Banqueri",
                            "corporate_name": None,
                            "inscricao_estadual_isento": False,
                            "inscricao_estadual": None,
                            "fancy_name": None,
                            "birthdate": None,
                            "gender": None,
                            "blocked": False,
                            "newsletter": 0,
                            "gdpr_agreement": False,
                            "receiver": "Felipe Banqueri",
                            "zipcode": "14060360",
                            "address": "R DAVID SALOMÃO",
                            "number": "943",
                            "neighborhood": "JD JANDAIA",
                            "complement": None,
                            "city": "RIBEIRÃO PRETO",
                            "state": "SP",
                            "phone1": "16991985427",
                            "phone2": None,
                            "reference": None,
                            "city_id": "9560",
                            "code_ibge": "3543402",
                            "add_date": "2021-05-24T08:07:37.693385",
                            "change_date": "2021-08-30T10:51:38.461233",
                            "limit_credit": None,
                            "balance_of_credit": None,
                            "group": None},
                        "utm_partner": None,
                        "utm_medium": None,
                        "utm_source": None,
                        "utm_campaign": None,
                        "token_remake": "603AF534F764486AAC188996DAA7B63D",
                        "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                        "payment_method": "CartaoDeCredito",
                        "payment_discount": "0.00",
                        "payment_interest": "0.00",
                        "installment": 1,
                        "items": [
                            {
                                "id": 583,
                                "cart": 1496,
                                "description": "Pantufa Big Iron",
                                "sku": {
                                    "id": 63,
                                    "product": 45,
                                    "title": None,
                                    "ean_13": None,
                                    "reference_code": None,
                                    "weight": "0.000",
                                    "height": None,
                                    "width": None,
                                    "depth": None,
                                    "cost_price": None,
                                    "unit_price": "99.00000",
                                    "sale_price": None,
                                    "min_seller_sale_price": None,
                                    "loyalty_price": None,
                                    "percentage_discount_price": None,
                                    "stock": 9,
                                    "multiple_stock": 1,
                                    "reserves_stock": 2,
                                    "minimum_stock": 0,
                                    "max_buy": None,
                                    "available": True,
                                    "default": True,
                                    "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                    "options": None,
                                    "availability": None,
                                    "sell_out_of_stock": False},
                                "quantity": 1,
                                "original_price": "99.00000",
                                "unit_price": "99.00000",
                                "total_price": "99.00000",
                                "manual_price": None,
                                "discount": "0.00000",
                                "unit_discount": "0.00000",
                                "url": "/pantufa-big-iron/p",
                                "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                "parent": None,
                                "required": False,
                                "is_gift": False,
                                "is_bundle": False,
                                "extra_data": None
                            }

                        ],
                        "order": None,
                        "seller": None
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
                        cart_schema[0]: cart_schema[1],
                        "example": {
                            "id": 1496,
                            "add_date": "2021-10-20T16:14:29.634520",
                            "last_updated": "2021-10-20T18:00:16.555955",
                            "status": "declined",
                            "customer": {
                                "uuid": "1417698f-e14f-4546-a9ff-388442cd94f5",
                                "id": 71,
                                "reference_code": None,
                                "email": "felipe.banqueri@convertize.com.br",
                                "document": "43381727893",
                                "corporate_document": None,
                                "name": "Felipe Banqueri",
                                "corporate_name": None,
                                "inscricao_estadual_isento": False,
                                "inscricao_estadual": None,
                                "fancy_name": None,
                                "birthdate": None,
                                "gender": None,
                                "blocked": False,
                                "newsletter": 0,
                                "gdpr_agreement": False,
                                "receiver": "Felipe Banqueri",
                                "zipcode": "14060360",
                                "address": "R DAVID SALOMÃO",
                                "number": "943",
                                "neighborhood": "JD JANDAIA",
                                "complement": None,
                                "city": "RIBEIRÃO PRETO",
                                "state": "SP",
                                "phone1": "16991985427",
                                "phone2": None,
                                "reference": None,
                                "city_id": "9560",
                                "code_ibge": "3543402",
                                "add_date": "2021-05-24T08:07:37.693385",
                                "change_date": "2021-08-30T10:51:38.461233",
                                "limit_credit": None,
                                "balance_of_credit": None,
                                "group": None
                            },
                            "utm_partner": None,
                            "utm_medium": None,
                            "utm_source": None,
                            "utm_campaign": None,
                            "token_remake": "603AF534F764486AAC188996DAA7B63D",
                            "uuid": "7c94b1aa-3f3b-4269-b37c-8bcc0e76660b",
                            "payment_method": "CartaoDeCredito",
                            "payment_discount": "0.00",
                            "payment_interest": "0.00",
                            "installment": 1,
                            "items": [
                                    {
                                        "id": 583,
                                        "cart": 1496,
                                        "description": "Pantufa Big Iron",
                                        "sku": {
                                            "id": 63,
                                            "product": 45,
                                            "title": None,
                                            "ean_13": None,
                                            "reference_code": None,
                                            "weight": "0.000",
                                            "height": None,
                                            "width": None,
                                            "depth": None,
                                            "cost_price": None,
                                            "unit_price": "99.00000",
                                            "sale_price": None,
                                            "min_seller_sale_price": None,
                                            "loyalty_price": None,
                                            "percentage_discount_price": None,
                                            "stock": 9,
                                            "multiple_stock": 1,
                                            "reserves_stock": 2,
                                            "minimum_stock": 0,
                                            "max_buy": None,
                                            "available": True,
                                            "default": True,
                                            "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                            "add_date": "2021-05-04T11:03:28.210257",
                                            "change_date": "2021-10-20T16:14:14.988085",
                                            "options": None,
                                            "availability": None,
                                            "sell_out_of_stock": False
                                        },
                                        "quantity": 1,
                                        "original_price": "99.00000",
                                        "unit_price": "99.00000",
                                        "total_price": "99.00000",
                                        "manual_price": None,
                                        "discount": "0.00000",
                                        "unit_discount": "0.00000",
                                        "url": "/pantufa-big-iron/p",
                                        "image": "shop/products/images/45/small/pantufa-big-iron_100.webp",
                                        "parent": None,
                                        "required": False,
                                        "is_gift": False,
                                        "is_bundle": False,
                                        "extra_data": None
                                    }
                            ],
                            "order": None,
                            "seller": None
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
    "CarrinhoDelete": modules.ConvertizeLink(
        tags=["Carrinhos"],
        url='/{environment}/api/v2/carts/{cart_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='cart_id', required=True, location='path',
                          description=u"ID do carrinho", schema={"type": "integer"}),
        ],
        description='Deletar um Carrinho',
        summary='',
        operationId='Deletar um Carrinho',
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
