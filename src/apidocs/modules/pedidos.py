# coding: utf-8
import coreapi
from apidocs import modules

order_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do pedido"),
    modules.new_propertie(name="referece_code", type="string", nullable=False, description=u"Código de referência no marketplace"),
    modules.new_propertie(name="erp_code", type="string", description=u"Código de referência ou código da grade no ERP"),
    modules.new_propertie(name="customer", type="integer", format="int4", description=u"ID do cliente"),
    modules.new_propertie(name="billing_detail_name", type="string", nullable=False, description=u"Nome do cliente"),
    modules.new_propertie(name="billing_detail_document", type="string", nullable=False, description=u"Documento do cliente"),
    modules.new_propertie(name="billing_detail_address", type="string",nullable=False, description=u"Endereço"),
    modules.new_propertie(name="billing_detail_number",type="string",nullable=False, description=u"Número"),
    modules.new_propertie(name="billing_detail_complement", type="string",nullable=False, description=u"Complemento"),
    modules.new_propertie(name="billing_detail_neighborhood", type="string",nullable=False, description=u"Bairro"),
    modules.new_propertie(name="billing_detail_city",type="string",nullable=False, description=u"Cidade"),
    modules.new_propertie(name="billing_detail_state",type="string",nullable=False, description=u"Estado"),
    modules.new_propertie(name="billing_detail_postcode",type="string",nullable=False, description=u"CEP"),
    modules.new_propertie(name="billing_detail_phone", type="string", nullable=False, description=u"Telefone"),
    modules.new_propertie(name="billing_detail_email",type="string",nullable=False, description=u"E-mail do cliente"),
    modules.new_propertie(name="shipping_detail_name",type="string",nullable=False, description=u"Nome do cliente"),
    modules.new_propertie(name="shipping_detail_document", type="string", nullable=False, description=u"Documento do cliente"),
    modules.new_propertie(name="shipping_detail_address", type="string", nullable=False, description=u"Endereço"),
    modules.new_propertie(name="shipping_detail_number", type="string", nullable=False, description=u"Número"),
    modules.new_propertie(name="shipping_detail_complement", type="string", nullable=False, description=u"Complemento"),
    modules.new_propertie(name="shipping_detail_neighborhood", type="string", nullable=False, description=u"Bairro"),
    modules.new_propertie(name="shipping_detail_city", type="string", nullable=False, description=u"Cidade"),
    modules.new_propertie(name="shipping_detail_state", type="string", nullable=False, description=u"Estado"),
    modules.new_propertie(name="shipping_detail_postcode",type="string", nullable=False, description=u"CEP"),
    modules.new_propertie(name="shipping_detail_phone", type="string", nullable=False, description=u"Telefone"),
    modules.new_propertie(name="shipping_detail_email", type="string", nullable=False, description=u"E-mail do cliente"),
    modules.new_propertie(name="shipping_total",type="float", nullable=False, description=u"Custo do envio"),
    modules.new_propertie(name="shipping_discount", type="float", nullable=False, description=u"Desconto no envio"),
    modules.new_propertie(name="shipping_delivery_date", type="datetime.date", nullable=False, description=u"Data de entrega"),
    modules.new_propertie(name="shipping_type", type="string", nullable=False, description=u"Tipo de entrega"),
    modules.new_propertie(name="shipping_delivery_date", type="datetime.date", nullable=False, description=u"Data de entrega"),
    modules.new_propertie(name="pickup_store", type="integer",format="int4", nullable=False, description=u"ID da loja para retirada"),
    modules.new_propertie(name="item_total", type="float", nullable=False, description=u"Total do pedido em itens"),
    modules.new_propertie(name="discount_total",type="float", nullable=False, description=u"Total de desconto"),
    modules.new_propertie(name="total", type="float", nullable=False, descriptio=u"Total do pedido"),
    modules.new_propertie(name="payment_method", type="string", nullable=False, description=u"Forma de pagamento"),
    modules.new_propertie(name="institution", type="string", nullable=False, description=u"Instituição Financeira"),
    modules.new_propertie(name="installments", type="integer", format="int4", description=u"Parcelas"),
    modules.new_propertie(name="captured", type="boolean", description="Informa se o pedido esta capturado"),
    modules.new_propertie(name="status", type="string", nullable=False, description=u"Status do pedido"),
    modules.new_propertie(name="channel", type="integer", format="int4", nullable=False, description=u"Código do canal de compra"),
    modules.new_propertie(name="observation", type="string", description=u"Texto de observação"),
    modules.new_propertie(name="transaction_id", type="string", description=u"Código da transação"),
    modules.new_propertie(name="pan", type="string", description=u"PAN da transação"),
    modules.new_propertie(name="nsu", type="string", description=u"NSU da transação"),
    modules.new_propertie(name="card_mask", type="string", description=u"Cartão mascarado"),
    modules.new_propertie(name="ip_addrress", type="string", description=u"IP da transação"),
    modules.new_propertie(name="weddinglist", type="integer", format="int4", description=u"ID da lista de presente"),
    modules.new_propertie(name="seller", type="integer", format="int4", description=u"ID do vendedor"),
    modules.new_propertie(name="items", type="list", nullable=False, description=u"Lista de items do pedido"),
    modules.new_propertie(name="items.order", type="integer",format="int4", nullable=False, description=u"ID do pedido"),
    modules.new_propertie(name="items.sku", type="integer", format="int4", nullable=False, description=u"ID do item"),
    modules.new_propertie(name="items.description", type="string",nullable=False, description=u"ID do item"),
    modules.new_propertie(name="items.quantity", type="integer", format="int4", nullable=False, description=u"Quantidade do item"),
    modules.new_propertie(name="items.unit_price", type="float", nullable=False, description=u"Preço unitário"),
    modules.new_propertie(name="items.total_price", type="float", nullable=False, description=u"Preço total"),
    modules.new_propertie(name="items.discount", type="float", nullable=False, description=u"Desconto no item"),
    modules.new_propertie(name="items.is_gift", type="boolean", nullable=False, description=u"Informa se o item é presente"),
    modules.new_propertie(name="trackers", type="list", description="Lista de códigos de rastreio"),
    modules.new_propertie(name="trackers.id", type="integer", format="int4", nullable=False, description=u"ID do código de rastreio"),
    modules.new_propertie(name="trackers.order", type="integer", format="int4", nullable=False, descrtipion=u"ID do pedido"),
    modules.new_propertie(name="trackers.code", type="string", nullable=False, description=u"Código do Rastreio"),
    modules.new_propertie(name="trackers.status", type="string",nullable=False, description=u"Status do pedido"),
    modules.new_propertie(name="invoices", type="list", description=u"Lista de notas fiscais"),
    modules.new_propertie(name="trackers.id", type="integer", format="int4", nullable=False, description=u"ID da nota fiscal"),
    modules.new_propertie(name="trackers.order", type="integer", format="int4",nullable=False, description=u"ID do pedido"),
    modules.new_propertie(name="trackers.key", type="string", description=u"Código da Nota Fiscal"),
    modules.new_propertie(name="trackers.date_issue", type="datetime.datetime", nullable=False, description=u"Data de emissão (yyyy-mm-ddTHH:ii:ss)"),
    modules.new_propertie(name="trackers.series", type="string", nullable=False, description=u"Serie da Nota Fiscal"),
    modules.new_propertie(name="trackers.total", type="float", nullable=False, description=u"Total da Nota Fiscal")               
])


orders_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "customer"]),
            modules.new_propertie(name="properties", enum=order_componente)
        )))
    )))


order_schema = modules.new_propertie(name="schema", type="object", properties=order_componente)


export = {
    "Pedidos": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/customers/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"ID do pedido", schema={"type": "integer"}),            
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Código de referência no marketplace", schema={"type": "string"}),
            coreapi.Field(name="erp_code", required=False, location='query', description=u"Código de referência no ERP", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Pedidos',
        summary='',
        operationId='Lista de Categorias',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    orders_schema[0]: orders_schema[1],
                    "example": {
                      "count": 114,
                      "next": "https://api.convertize.com.br/{environment}/api/1.0/orders/?page=2",
                      "previous": None,
                      "results": [
                        {
                      "id": 172,
                      "reference_code": None,
                      "erp_code": None,
                      "customer": 1,
                      "billing_detail_name": "TESTE NOME",
                      "billing_detail_document": "12312312312",
                      "billing_detail_address": "R BERNARDINO DE CAMPOS",
                      "billing_detail_number": "1001",
                      "billing_detail_complement": "SALA 1001",
                      "billing_detail_neighborhood": "CENTRO",
                      "billing_detail_city": "RIBEIRÃO PRETO",
                      "billing_detail_state": "SP",
                      "billing_detail_postcode": "14015130",
                      "billing_detail_phone": "(16) 30757676",
                      "billing_detail_email": "dev@convertize.com.br",
                      "shipping_detail_name": "TESTE NOME",
                      "shipping_detail_document": "12312312312",
                      "shipping_detail_address": "R BERNARDINO DE CAMPOS",
                      "shipping_detail_number": "1001",
                      "shipping_detail_complement": "SALA 1001",
                      "shipping_detail_neighborhood": "CENTRO",
                      "shipping_detail_city": "RIBEIRÃO PRETO",
                      "shipping_detail_state": "SP",
                      "shipping_detail_postcode": "14015130",
                      "shipping_detail_phone": "(16) 30757676",
                      "shipping_detail_email": "dev@convertize.com.br",
                      "shipping_total": "13.50",
                      "shipping_discount": "0.00",
                      "shipping_delivery_date": "2016-08-05",
                      "item_total": "260.00",
                      "discount_total": "0.00",
                      "total": "273.50",
                      "payment_method": "Boleto",
                      "institution": "Bancodobrasil",
                      "installments": 1,
                      "captured": False,
                      "status": "PEN",
                      "channel": 0,
                      "observation": None,
                      "transaction_id": None,
                      "pan": None,
                      "nsu": None,
                      "card_mask": None,
                      "ip_addrress": "127.0.0.1",
                      "weddinglist": None,
                      "seller": None,
                      "add_date": "2016-07-26T17:06:11.408989",
                      "update_date": "2016-07-26T17:06:20.554219",
                      "items": [
                          {
                            "order": 172,
                            "sku": 1694,
                            "description": "COMBO TESTE",
                            "quantity": 4,
                            "unit_price": "20.00",
                            "total_price": "80.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
                        },
                        {
                            "order": 172,
                            "sku": 1693,
                            "description": "COMBO TESTE",
                            "quantity": 4,
                            "unit_price": "45.00",
                            "total_price": "180.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
                        }
                    ]
                         },
                     {
                      "id": 171,
                      "reference_code": None,
                      "erp_code": None,
                      "customer": 1,
                      "billing_detail_name": "TESTE NOME",
                      "billing_detail_document": "12312312312",
                      "billing_detail_address": "R BERNARDINO DE CAMPOS",
                      "billing_detail_number": "1001",
                      "billing_detail_complement": "SALA 1001",
                      "billing_detail_neighborhood": "CENTRO",
                      "billing_detail_city": "RIBEIRÃO PRETO",
                      "billing_detail_state": "SP",
                      "billing_detail_postcode": "14015130",
                      "billing_detail_phone": "(16) 30757676",
                      "billing_detail_email": "dev@convertize.com.br",
                      "shipping_detail_name": "TESTE NOME",
                      "shipping_detail_document": "12312312312",
                      "shipping_detail_address": "R BERNARDINO DE CAMPOS",
                      "shipping_detail_number": "1001",
                      "shipping_detail_complement": "SALA 1001",
                      "shipping_detail_neighborhood": "CENTRO",
                      "shipping_detail_city": "RIBEIRÃO PRETO",
                      "shipping_detail_state": "SP",
                      "shipping_detail_postcode": "14015130",
                      "shipping_detail_phone": "(16) 30757676",
                      "shipping_detail_email": "dev@convertize.com.br",
                      "shipping_total": "13.50",
                      "shipping_discount": "0.00",
                      "shipping_delivery_date": "2016-08-05",
                      "item_total": "195.00",
                      "discount_total": "0.00",
                      "total": "208.50",
                      "payment_method": "Boleto",
                      "institution": "Bancodobrasil",
                      "installments": 1,
                      "captured": False,
                      "status": "PEN",
                      "channel": 0,
                      "observation": None,
                      "transaction_id": None,
                      "pan": None,
                      "nsu": None,
                      "card_mask": None,
                      "ip_addrress": "127.0.0.1",
                      "weddinglist": None,
                      "seller": None,
                      "add_date": "2016-07-26T16:55:25.319729",
                      "update_date": "2016-07-26T16:55:49.012298",
                      "items": [
                        {
                            "order": 171,
                            "sku": 1694,
                            "description": "COMBO TESTE",
                            "quantity": 3,
                            "unit_price": "20.00",
                            "total_price": "60.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
                        },
                        {
                            "order": 171,
                            "sku": 1693,
                            "description": "COMBO TESTE",
                            "quantity": 3,
                            "unit_price": "45.00",
                            "total_price": "135.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
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
    "Pedido": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='order_id', required=False, location='query', description=u"ID do pedido", schema={"type": "integer"}),            
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Código de referência no marketplace", schema={"type": "string"}),
            coreapi.Field(name="erp_code", required=False, location='query', description=u"Código de referência no ERP", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
           
        ],
        description='Retorna um pedido por `ID`',
        summary='',
        operationId='Detalhes de um pedido',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    order_schema[0]: order_schema[1],
                    "example": {
                       "id": 172,
                       "reference_code": None,
                       "erp_code": None,
                       "customer": 1,
                       "billing_detail_name": "TESTE NOME",
                       "billing_detail_document": "12312312312",
                       "billing_detail_address": "R BERNARDINO DE CAMPOS",
                       "billing_detail_number": "1001",
                       "billing_detail_complement": "SALA 1001",
                       "billing_detail_neighborhood": "CENTRO",
                       "billing_detail_city": "RIBEIRÃO PRETO",
                       "billing_detail_state": "SP",
                       "billing_detail_postcode": "14015130",
                       "billing_detail_phone": "(16) 30757676",
                       "billing_detail_email": "dev@convertize.com.br",
                       "shipping_detail_name": "TESTE NOME",
                       "shipping_detail_document": "12312312312",
                       "shipping_detail_address": "R BERNARDINO DE CAMPOS",
                       "shipping_detail_number": "1001",
                       "shipping_detail_complement": "SALA 1001",
                       "shipping_detail_neighborhood": "CENTRO",
                       "shipping_detail_city": "RIBEIRÃO PRETO",
                       "shipping_detail_state": "SP",
                       "shipping_detail_postcode": "14015130",
                       "shipping_detail_phone": "(16) 30757676",
                       "shipping_detail_email": "dev@convertize.com.br",
                       "shipping_total": "13.50",
                       "shipping_discount": "0.00",
                       "shipping_delivery_date": "2016-08-05",
                       "item_total": "260.00",
                       "discount_total": "0.00",
                       "total": "273.50",
                       "payment_method": "Boleto",
                       "institution": "Bancodobrasil",
                       "installments": 1,
                       "captured": False,
                       "status": "PEN",
                       "channel": 0,
                       "observation": None,
                       "transaction_id": None,
                       "pan": None,
                       "nsu": None,
                       "card_mask": None,
                       "ip_addrress": "127.0.0.1",
                       "weddinglist": None,
                       "seller": None,
                       "add_date": "2016-07-26T17:06:11.408989",
                       "update_date": "2016-07-26T17:06:20.554219",
                           "items": [
                        {
                            "order": 172,
                            "sku": 1694,
                            "description": "COMBO TESTE",
                            "quantity": 4,
                            "unit_price": "20.00",
                            "total_price": "80.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
                        },
                        {
                            "order": 172,
                            "sku": 1693,
                            "description": "COMBO TESTE",
                            "quantity": 4,
                            "unit_price": "45.00",
                            "total_price": "180.00",
                            "discount": "0.00",
                            "delivery_time": None,
                            "shipping_type": None,
                            "is_gift": False
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
    "StatusUpdate": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/status/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='order_id', required=True, location='path', description=u"ID do pedido", schema={"type": "integer"}),
        ],
        description='Alterar um Status',
        summary='',
        operationId='Alterar um Status',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "customer"],
                    order_schema[0]: order_schema[1],
                    "example": {
                       "status": "PEN"                        
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
                    "required": ["id", "customer"],
                    order_schema[0]: order_schema[1],
                    "example": {
                        "status": "PEN"
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
    "CodigoRastreio": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/trackers/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='order_id', required=True, location='path', description=u"ID do pedido", schema={"type": "integer"}),
        ],
        description='Adicionar um código de rastreio',
        summary='',
        operationId='Adicionar um código de rastreio',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "customer"],
                    order_schema[0]: order_schema[1],
                    "example": {
                       "code": "SW902295112BR",
                       "status": "ETP"                        
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
                    "required": ["id", "customer"],
                    order_schema[0]: order_schema[1],
                    "example": {
                        "id": 84,
                        "order": 172,
                        "code": "SW902295112BR",
                        "status": "ETP",
                        "add_date": "2016-10-11T16:10:38.626884",
                        "update_date": "2016-10-11T16:10:38.626930"
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
    "PedidoDelete": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/trackers/{tracker_id}',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='tracker_id', required=True, location='path', description=u"ID relativo ao código de rastreio", schema={"type": "integer"}),
        ],
        description='Deletar um código de rastreio',
        summary='',
        operationId='Deletar um código de Rastreio',
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
    ),
    "NotaFiscal": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/invoices/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='order_id', required=True, location='path', description=u"ID do pedido", schema={"type": "integer"}),
        ],
        description='Adicionar uma nota fiscal',
        summary='',
        operationId='Adicionar uma nota fiscal',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "order"],
                    order_schema[0]: order_schema[1],
                    "example": {
                       "order": 172,
                       "key": "12312312313212",
                       "series": "123",
                       "reference_code": "01",
                       "date_issue": "1989-10-01T10:59:59",
                       "total": "150.50"                        
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
                    "required": ["id", "customer"],
                    order_schema[0]: order_schema[1],
                    "example": {
                        "id": 9,
                        "order": 172,
                        "reference_code": "01",
                        "key": "12312312313212",
                        "series": "123",
                        "date_issue": "1989-10-01T10:59:59",
                        "total": "150.50",
                        "add_date": "2016-10-11T16:35:44.614333",
                        "update_date": "2016-10-11T16:35:44.614360"
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
    "NotaFiscalDelete": modules.ConvertizeLink(
        tags=["Pedidos"],
        url='/{environment}/api/v2/orders/{order_id}/trackers/{invoice_id}',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='invoice_id', required=True, location='path', description=u"ID relativo a nota fiscal", schema={"type": "integer"}),
        ],
        description='Deletar uma nota fiscal',
        summary='',
        operationId='Deletar uma nota fiscal',
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
    ),   
    
}

