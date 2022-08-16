# coding: utf-8
import coreapi
from apidocs import modules

seller_componente = dict([
    modules.new_propertie(name="id", type="integer",format="int64", nullable=False, description=u"ID do vendedor"),
    modules.new_propertie(name="name", type="string", nullable=False, description=u"Nome completo"),
    modules.new_propertie(name="email", type="string", nullable=False, description=u"E-mail do vendedor"),
    modules.new_propertie(name="group",type="array",description=u"Grupo de vendedores"),
    modules.new_propertie(name="blocked", type="boolean", description=u"Indica se está bloqueado `default = false`"),
    modules.new_propertie(name="reference_code",type="string", description=u"Código de referência"),
    modules.new_propertie(name="supervisor", type="string", description=u"Nome do supervisor"),
    modules.new_propertie(name="add_manual_value", type="boolean", description=u"Indica se pode adicionar valor manual `default = false`"),
    modules.new_propertie(name="receive_mail", type="boolean", description=u"Indica se receberá emails `default = false`"),
    modules.new_propertie(name="view_only_own_budget", type="boolean", description=u"Indica se irá visualizar somente o próprio orçamento `default = true`"),
    modules.new_propertie(name="image", type="string", description=u"URL da imagem"),
    modules.new_propertie(name="store", type="boolean", description=u"Indica se tem uma loja `default = false`"),
    modules.new_propertie(name="url", type="string", description=u"URL da loja do vendedor."),
    modules.new_propertie(name="description", type="string", description=u"Descrição da loja do vendedor."),
    modules.new_propertie(name="phone", type="string", description=u"Telefone"),
    modules.new_propertie(name="sales", type="integer",format="int4", description=u"Indica o número de vendas"),
    modules.new_propertie(name="physical_store", type="object", description=u"Local de retirada."),
    modules.new_propertie(name="seller_type", type="string", description=u"Tipo de vendedor."),
    modules.new_propertie(name="store_identification", type="", description=u"Identificação da loja."),
    modules.new_propertie(name="logo_url", type="string", description=u"URL do logo."),
    modules.new_propertie(name='return_policy', type='string', description=u"Política de Troca e Devolução"),
    modules.new_propertie(name='delivery_policy', type='string', description=u"Política de entrega"),
    modules.new_propertie(name='security_privacy_policy', type='string', description=u"Política de Segurança e Privacidade"),
    modules.new_propertie(name='use_giftcard', type='boolean', description=u"Indica se pode usar GiftCard como forma de pagamento `default = false` "),
    modules.new_propertie(name='product_commission', type='float', description=u"Comissão em Produtos"),
    modules.new_propertie(name='freight_commission', type='float', description=u"Comissão em Frete"),
    modules.new_propertie(name='fulfillment_endpoint', type='string', description=u"URL do endpoint de Fullfillment"),
    modules.new_propertie(name='catalog_endpoint', type='string', description=u"URL do endpoint de Catalogo"),
    modules.new_propertie(name='merchant_name', type='string', description=u"Merchant name"),
    modules.new_propertie(name='is_full_store', type='boolean', description=u""),
    modules.new_propertie(name='trust_policy', type='string', description=u"Política de confiança"),
    modules.new_propertie(name="extra_data", type="object", description=u"Informações adicionais."),
    modules.new_propertie(name='document', type='string', description=u"CPF/CNPJ"),     
        
])


sellers_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "name"]),
            modules.new_propertie(name="properties", enum=seller_componente)
        )))
    )))



seller_schema = modules.new_propertie(name="schema", type="object", properties=seller_componente, required=["id", "name"])


export = {
    "Vendedores": modules.ConvertizeLink(
        tags=["Vendedores"],
        url='/{environment}/api/v2/telesales/sellers',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro por id do vendedor", schema={"type": "string"}),
            coreapi.Field(name='blocked', required=False, location='query', description=u"Filtro por vendedor bloqueado", schema={"type": "boolean"}),
            coreapi.Field(name='store', required=False, location='query', description=u"Filtro por vendedor que tenha loja", schema={"type": "boolean"}),
            coreapi.Field(name='group', required=False, location='query', description=u"Filtro por grupo", schema={"type": "integer"}),
            coreapi.Field(name='supervisor', required=False, location='query', description=u"Filtro por supervisor", schema={"type":"string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de vendedores',
        summary='',
        operationId='Lista de Vendedores',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    sellers_schema[0]: sellers_schema[1],
                    "example": {
                      "count": 6,
                      "next": None,
                      "previous": None,
                      "results": [
                        {
                            "id": 8,
                            "name": "Isabela Sanchez",
                            "email": "isabela.sanchez@convertize.com.br",
                            "group": None,
                            "blocked": False,
                            "reference_code": None,
                            "supervisor": None,
                            "add_manual_value": False,
                            "receive_mail": False,
                            "view_only_own_budget": True,
                            "image": None,
                            "store": False,
                            "url": None,
                            "description": "",
                            "phone": "",
                            "sales": 0,
                            "physical_store": None,
                            "seller_Type": "store",
                            "store_identification": None,
                            "logo_url": None,
                            "return_policy": None,
                            "delivery_policy": None,
                            "secutity_privacy_policy": None,
                            "use_giftcard": False,
                            "product_commission": "0.00",
                            "freight_commission": "0.00",
                            "fulfillment_endpoint": None,
                            "catalog_endpoint": None,
                            "merchant_name": None,
                            "is_full_store": False,
                            "trust_policy": "default",
                            "add_date": "2021-07-21T16:12:41.466987",
                            "change_date": "2021-07-21T16:12:41.467003",
                            "extra_data": None,
                            "document":None
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
    "Vendedor": modules.ConvertizeLink(
        tags=["Vendedores"],
        url='/{environment}/api/v2/telesales/sellers/{seller_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='seller_id', required=True, location='path', description=u"ID do vendedor", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna um vendedor por `ID`',
        summary='',
        operationId='Detalhes de um vendedor',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    seller_schema[0]: seller_schema[1],
                    "example": {
                        "id": 8,
                        "name": "Isabela Sanchez",
                        "email": "isabela.sanchez@convertize.com.br",
                        "group": None,
                        "blocked": False,
                        "reference_code": None,
                        "supervisor": None,
                        "add_manual_value": False,
                        "receive_mail": False,
                        "view_only_own_budget": True,
                        "image": None,
                        "store": False,
                        "url": None,
                        "description": "",
                        "phone": "",
                        "sales": 0,
                        "physical_store": None,
                        "seller_Type": "store",
                        "store_identification": None,
                        "logo_url": None,
                        "return_policy": None,
                        "delivery_policy": None,
                        "secutity_privacy_policy": None,
                        "use_giftcard": False,
                        "product_commission": "0.00",
                        "freight_commission": "0.00",
                        "fulfillment_endpoint": None,
                        "catalog_endpoint": None,
                        "merchant_name": None,
                        "is_full_store": False,
                        "trust_policy": "default",
                        "add_date": "2021-07-21T16:12:41.466987",
                        "change_date": "2021-07-21T16:12:41.467003",
                        "extra_data": None,
                        "document":None
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
    "VendedorCreate": modules.ConvertizeLink(
        tags=["Vendedores"],
        url='/{environment}/api/v2/telesales/sellers',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),            
        ],
        description='Adicionar um Vendedor',
        summary='',
        operationId='Adicionar um Vendedor',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "name"],
                    seller_schema[0]: seller_schema[1],
                    "example": {
                        "name": "Isabela Sanchez",
                        "email": "isabela.sanchez@convertize.com.br",                        
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
                    seller_schema[0]: seller_schema[1],
                    "example": {
                        "id": 8,
                        "name": "Isabela Sanchez",
                        "email": "isabela.sanchez@convertize.com.br",
                        "group": None,
                        "blocked": False,
                        "reference_code": None,
                        "supervisor": None,
                        "add_manual_value": False,
                        "receive_mail": False,
                        "view_only_own_budget": True,
                        "image": None,
                        "store": False,
                        "url": None,
                        "description": "",
                        "phone": "",
                        "sales": 0,
                        "physical_store": None,
                        "seller_Type": "store",
                        "store_identification": None,
                        "logo_url": None,
                        "return_policy": None,
                        "delivery_policy": None,
                        "secutity_privacy_policy": None,
                        "use_giftcard": False,
                        "product_commission": "0.00",
                        "freight_commission": "0.00",
                        "fulfillment_endpoint": None,
                        "catalog_endpoint": None,
                        "merchant_name": None,
                        "is_full_store": False,
                        "trust_policy": "default",
                        "add_date": "2021-07-21T16:12:41.466987",
                        "change_date": "2021-07-21T16:12:41.467003",
                        "extra_data": None,
                        "document":None
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
    "VendedorUpdate": modules.ConvertizeLink(
        tags=["Vendedores"],
        url='/{environment}/api/v2/telesales/sellers/{seller_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='seller_id', required=True, location='path', description=u"ID da do vendedor", schema={"type": "integer"}),
        ],
        description='Alterar um Vendedor',
        summary='',
        operationId='Alterar um Vendedor',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "name"],
                    seller_schema[0]: seller_schema[1],
                    "example": {
                        "name": "Isabela Sanchez",
                        "email": "isabela.sanchez@convertize.com.br",
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
                    "required": ["id", "name"],
                    seller_schema[0]: sellers_schema[1],
                    "example": {
                        "id": 8,
                        "name": "Isabela Sanchez",
                        "email": "isabela.sanchez@convertize.com.br",
                        "group": None,
                        "blocked": False,
                        "reference_code": None,
                        "supervisor": None,
                        "add_manual_value": False,
                        "receive_mail": False,
                        "view_only_own_budget": True,
                        "image": None,
                        "store": False,
                        "url": None,
                        "description": "",
                        "phone": "",
                        "sales": 0,
                        "physical_store": None,
                        "seller_Type": "store",
                        "store_identification": None,
                        "logo_url": None,
                        "return_policy": None,
                        "delivery_policy": None,
                        "secutity_privacy_policy": None,
                        "use_giftcard": False,
                        "product_commission": "0.00",
                        "freight_commission": "0.00",
                        "fulfillment_endpoint": None,
                        "catalog_endpoint": None,
                        "merchant_name": None,
                        "is_full_store": False,
                        "trust_policy": "default",
                        "add_date": "2021-07-21T16:12:41.466987",
                        "change_date": "2021-07-21T16:12:41.467003",
                        "extra_data": None,
                        "document":None
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
    "VendedorDelete": modules.ConvertizeLink(
        tags=["Vendedores"],
        url='/{environment}/api/v2/telesales/sellers/{seller_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='seller_id', required=True, location='path', description=u"ID do vendedor", schema={"type": "integer"}),
        ],
        description='Deletar um Vendedor',
        summary='',
        operationId='Deletar um Vendedor',
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