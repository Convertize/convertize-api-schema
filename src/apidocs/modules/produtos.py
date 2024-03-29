#coding: utf-8
import coreapi
from apidocs import modules

product_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False,  format="int64", description=u"ID do produto"),
    modules.new_propertie(name="category", type="string",   description=u"Categoria"),
    modules.new_propertie(name="similar_category", type="array",   format="int4", description=u"ID`s dos produtos similares"),
    modules.new_propertie(name="brand", type="integer",   format="int4", description=u"ID da marca"),
    modules.new_propertie(name="grid", type="integer",  format="int4", description=u"ID da grade"),
    modules.new_propertie(name="suggestions", type="array", format="int4", description=u"ID`s dos produtos como sugestão"),
    modules.new_propertie(name="similars", type="array",   format="int4", description=u"ID`s dos produtos similares"),
    modules.new_propertie(name="accessories", type="array", format="int4", description=u"ID`s dos produtos como acessórios"),
    modules.new_propertie(name="telesales_exclusive", type="boolean", nullable=False, description=u"Indica se o produto é exclusivo de televenda `default = false`"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título do produto para SEO"),
    modules.new_propertie(name="slug", type="string", description="Slug (url), caso vazio o sistema gera automaticamente"),
    modules.new_propertie(name="meta_title", type="string", description="Titulo da categoria para SEO"),
    modules.new_propertie(name="description", type="string",  description="Descrição da categoria para SEO"),
    modules.new_propertie(name="keywords", type="string",  description="Keywords da categoria para SEO separadas por `,`"),
    modules.new_propertie(name="product_type", type='integer', description=u"Tipo do produto"),
    modules.new_propertie(name="name", type="string", description="Nome do produto no ERP"),
    modules.new_propertie(name="upc", type="string", description="Código de código UPC ou SKU"),
    modules.new_propertie(name="fiscal_code", type="string", description="Código classificação fiscal"),
    modules.new_propertie(name="distributor", type="string", description="Fornecedor"),
    modules.new_propertie(name="reference_code", type="string", description="Código de referência ou código da grade no ERP"),
    modules.new_propertie(name="kits", type="array",   format="int4", description=u"Kits"),
    modules.new_propertie(name="available", type="boolean", nullable=False, description="Indica se o produto esta disponivel para venda `default = false`"),
    modules.new_propertie(name="status", type="integer", format="int2", description="Satus do produto (1 = Rascunho, 2 = Publicado) `default = 1`"),
    modules.new_propertie(name="details", type="string", description="Detalhes do produto em HTML"),
])

products_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True,
                          description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True,
                          description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False,
                          description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "title"]),
        modules.new_propertie(name="properties", enum=product_componente)
    )))
)))

product_schema = modules.new_propertie(
    name="schema", type="object", properties=product_componente, required=["id", "title"])

specification_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False,
                          format="int64", description=u"ID do valor da especificação"),
    modules.new_propertie(name="specification", type="integer",
                          nullable=False, description="Código da grade"),
    modules.new_propertie(name="product", type="integer",
                          nullable=False, description="Código do produto"),
    modules.new_propertie(name="value", type="string",
                          nullable=False, description="Valor"),

])

specifications_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True,
                          description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True,
                          description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False,
                          description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "title"]),
        modules.new_propertie(
            name="properties", enum=specification_componente)
    )))
)))

specification_schema = modules.new_propertie(
    name="schema", type="object", properties=product_componente, required=["id", "title"])

image_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False,
                          format="int64", description=u"ID da Imagem"),
    modules.new_propertie(name="position", type="integer",
                          nullable=False, description="Posição"),
    modules.new_propertie(name="product", type="integer",
                          nullable=False, description="ID do Produto"),
    modules.new_propertie(name="title", type="string", description="Título"),
    modules.new_propertie(name="image", type="string",
                          nullable=False, description="URL da Imagem"),
    modules.new_propertie(name="video", type="string", description="Vídeo"),
    modules.new_propertie(name="skus", type="list",
                          description="Lista de SKUs vinculados a imagem"),
])

images_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True,
                          description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True,
                          description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False,
                          description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "title"]),
        modules.new_propertie(name="properties", enum=image_componente)
    )))
)))

image_schema = modules.new_propertie(
    name="schema", type="object", properties=image_componente, required=["id", "title"])

distributor_componente = dict([
    modules.new_propertie(name="id", type="integer",
                          nullable=False, format="int64", description="ID"),
    modules.new_propertie(name="name", type="string",
                          nullable=False, description="Título"),
    modules.new_propertie(name="active", type="boolean",
                          description="Indica se esta ativo `default = true`"),
    modules.new_propertie(name="reference_code", type="string",
                          description="Código de referência ou código da grade no ERP")
])

distributors_schema = modules.new_propertie(name="schema", type="object", properties=dict((
    modules.new_propertie(name="next", type="string", nullable=True,
                          description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
    modules.new_propertie(name="previous", type="string", nullable=True,
                          description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
    modules.new_propertie(name="count", type="integer", nullable=False,
                          description=u"Quantidade total de paginas"),
    modules.new_propertie(name="results", type="array", items=dict((
        modules.new_propertie(name="required", enum=["id", "title"]),
        modules.new_propertie(
            name="properties", enum=distributor_componente)
    )))
)))

distributor_schema = modules.new_propertie(
    name="schema", type="object", properties=distributor_componente, required=["id", "title"])


export = {
    "Produtos": modules.ConvertizeLink(
        tags=["Produtos"],
        url='/{environment}/api/v2/products/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',  description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query',  description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='reference_code', required=False, location='query',   description=u"Código de referência ou código da grade no ERP", schema={"type": "string"}),
            coreapi.Field(name='upc', required=False, location='query',  description=u"Código de código UPC ou SKU"),
            coreapi.Field(name='status', required=False, location='query',  description=u"Filtro por status", schema={"type": "string"}),
            coreapi.Field(name='available', required=False, location='query',   description=u"Filtro por disponibilidade para venda", schema={"type": "boolean"}),
            coreapi.Field(name='telesales_exclusive', required=False, location='query',     description=u"Filtro por exclusivo de televendas", schema={"type": "boolean"}),
            coreapi.Field(name='grid', required=False,   location='query', description=u"Filtro por grade"),
            coreapi.Field(name='brand', required=False, location='query', description=u"Filtro por marca", schema={"type": "string"}),
            coreapi.Field(name='distributor', required=False, location='query',   description=u"Filtro por fornecedor", schema={"type": "string"}),
            coreapi.Field(name='SKU', required=False, location='query',  description=u"Filtro SKU", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',   description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',  description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',    description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',  description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Produtos',
        summary='',
        operationId='Lista de Produtos',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        products_schema[0]: products_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/products/?page=2",
                            "previous": None,
                            "results": [
                                {
                                    "id": 70,
                                    "title": "Kit para Teste",
                                    "slug": "kit-para-teste",
                                    "description": "",
                                    "keywords": "",
                                    "add_date": "2022-04-19T10:51:55.627172",
                                    "change_date": "2022-05-12T09:17:29.386565",
                                    "product_type": 2,
                                    "name": "Kit para Teste",
                                    "upc": "kit2022",
                                    "fiscal_code": "",
                                    "reference_code": None,
                                    "available": True,
                                    "status": 2,
                                    "details": "",
                                    "category": None,
                                    "brand": None,
                                    "distributor": None,
                                    "grid": None,
                                    "similar_category": [],
                                    "suggestions": [],
                                    "similars": [],
                                    "accessories": [],
                                    "kits": [
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 73
                                        },
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 101
                                        },
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 99
                                        }
                                    ],
                                    "telesales_exclusive": False
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
    "Produto": modules.ConvertizeLink(
        tags=["Produtos"],
        url='/{environment}/api/v2/products/{product_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='product_id', required=False, location='query',
                          description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='reference_code', required=False, location='query',
                          description=u"Código de referência ou código da grade no ERP", schema={"type": "string"}),
            coreapi.Field(name='upc', required=False, location='query',
                          description=u"Código de código UPC ou SKU"),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Produto por `ID`',
        summary='',
        operationId='Detalhes de um Produto',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        product_schema[0]: product_schema[1],
                        "example": {
                            "id": 70,
                            "title": "Kit para Teste",
                            "slug": "kit-para-teste",
                                    "description": "",
                                    "keywords": "",
                                    "add_date": "2022-04-19T10:51:55.627172",
                                    "change_date": "2022-05-12T09:17:29.386565",
                                    "product_type": 2,
                                    "name": "Kit para Teste",
                                    "upc": "kit2022",
                                    "fiscal_code": "",
                                    "reference_code": None,
                                    "available": True,
                                    "status": 2,
                                    "details": "",
                                    "category": None,
                                    "brand": None,
                                    "distributor": None,
                                    "grid": None,
                                    "similar_category": [],
                                    "suggestions": [],
                                    "similars": [],
                                    "accessories": [],
                                    "kits": [
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 73
                                        },
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 101
                                        },
                                        {
                                            "quantity": 1,
                                            "unit_price": "0.00",
                                            "sku": 99
                                        }
                                    ],
                            "telesales_exclusive": False
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
    "ProdutoCreate": modules.ConvertizeLink(
        tags=["Produtos"],
        url='/{environment}/api/v2/products/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambente do cliente", schema={"type": "string"}),
        ],
        description='Criar um Produto',
        summary='',
        operationId='Criar um Produto',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    product_schema[0]: product_schema[1],
                    "example": {
                        "title": "Kit para Teste",
                        "slug": "kit-para-teste",
                        "description": "",
                        "keywords": "",
                        "product_type": 2,
                        "name": "Kit para Teste",
                        "upc": "kit2022",
                        "fiscal_code": "",
                        "reference_code": None,
                        "available": True,
                        "status": 2,
                        "details": "",
                        "category": None,
                        "brand": None,
                        "distributor": None,
                        "grid": None,
                        "similar_category": [],
                        "suggestions": [],
                        "similars": [],
                        "accessories": [],
                        "kits": [
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 73
                            },
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 101
                            },
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 99
                            }
                        ],
                        "telesales_exclusive": False
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
                        product_schema[0]: product_schema[1],
                        "example": {
                            "id": 70,
                            "title": "Kit para Teste",
                            "slug": "kit-para-teste",
                            "description": "",
                            "keywords": "",
                            "add_date": "2022-04-19T10:51:55.627172",
                            "change_date": "2022-05-12T09:17:29.386565",
                            "product_type": 2,
                            "name": "Kit para Teste",
                            "upc": "kit2022",
                            "fiscal_code": "",
                            "reference_code": None,
                            "available": True,
                            "status": 2,
                            "details": "",
                            "category": None,
                            "brand": None,
                            "distributor": None,
                            "grid": None,
                            "similar_category": [],
                            "suggestions": [],
                            "similars": [],
                            "accessories": [],
                            "kits": [
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 73
                                },
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 101
                                },
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 99
                                }
                            ],
                            "telesales_exclusive": False
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
    "ProdutoUpdate": modules.ConvertizeLink(
        tags=["Produtos"],
        url='/{environment}/api/v2/products/{product_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='product_id', required=True, location='path',
                          description=u"ID do produto", schema={"type": "integer"}),
        ],
        description='Alterar um Produto',
        summary='',
        operationId='Alterar um Produto',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    product_schema[0]: product_schema[1],
                    "example": {
                        "title": "Kit para Teste",
                        "slug": "kit-para-teste",
                        "description": "",
                        "keywords": "",
                        "product_type": 2,
                        "name": "Kit para Teste",
                        "upc": "kit2022",
                        "fiscal_code": "",
                        "reference_code": None,
                        "available": True,
                        "status": 2,
                        "details": "",
                        "category": None,
                        "brand": None,
                        "distributor": None,
                        "grid": None,
                        "similar_category": [],
                        "suggestions": [],
                        "similars": [],
                        "accessories": [],
                        "kits": [
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 73
                            },
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 101
                            },
                            {
                                "quantity": 1,
                                "unit_price": "0.00",
                                "sku": 99
                            }
                        ],
                        "telesales_exclusive": False
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
                        product_schema[0]: product_schema[1],
                        "example": {
                            "id": 70,
                            "title": "Kit para Teste",
                            "slug": "kit-para-teste",
                            "description": "",
                            "keywords": "",
                            "add_date": "2022-04-19T10:51:55.627172",
                            "change_date": "2022-05-12T09:17:29.386565",
                            "product_type": 2,
                            "name": "Kit para Teste",
                            "upc": "kit2022",
                            "fiscal_code": "",
                            "reference_code": None,
                            "available": True,
                            "status": 2,
                            "details": "",
                            "category": None,
                            "brand": None,
                            "distributor": None,
                            "grid": None,
                            "similar_category": [],
                            "suggestions": [],
                            "similars": [],
                            "accessories": [],
                            "kits": [
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 73
                                },
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 101
                                },
                                {
                                    "quantity": 1,
                                    "unit_price": "0.00",
                                    "sku": 99
                                }
                            ],
                            "telesales_exclusive": False
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
    "ProdutoDelete": modules.ConvertizeLink(
        tags=["Produtos"],
        url='/{environment}/api/v2/grids/{product_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='product_id', required=True, location='path',
                          description=u"ID do produto", schema={"type": "integer"}),
        ],
        description='Deletar um Produto',
        summary='',
        operationId='Deletar um Produto',
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

    #
    # Specifications
    #

    "Especificacoes": modules.ConvertizeLink(
        tags=["Especificacoes"],
        url='/{environment}/api/v2/products/specifications/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query',
                          description=u"Filtro pelo ID do valor da especificação", schema={"type": "string"}),
            coreapi.Field(name='product', required=False, location='query',
                          description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='specification', required=False, location='query',
                          description=u"Filtro pelo ID da especificação"),
            coreapi.Field(name='value', required=False, location='query',
                          description=u"Filtro pelo valor da especificação"),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Especificações',
        summary='',
        operationId='Lista de Especificações',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        specifications_schema[0]: specifications_schema[1],
                        "example": {
                            "count": 1845,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/products/specifications/?page=2",
                            "previous": None,
                            "results": [
                                {
                                    "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/products/specifications/220/",
                                    "id": 220,
                                    "product": 92,
                                    "specification": 2,
                                    "value": "Waves",
                                    "value_as_float": None,
                                    "add_date": "2018-10-27T12:54:12.531948",
                                    "change_date": "2018-10-27T12:54:37.644119"
                                },
                                {
                                    "url": "/api/1.0/products/specifications/250/",
                                    "id": 250,
                                    "product": 446,
                                    "specification": 2,
                                    "value": "Colibri",
                                    "value_as_float": None,
                                    "add_date": "2018-11-02T13:41:10.200595",
                                    "change_date": "2018-11-02T13:42:23.529897"
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
    "Especificacao": modules.ConvertizeLink(
        tags=["Especificacao"],
        url='/{environment}/api/v2/options/{specification_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='specification_id', required=True, location='path',
                          description=u"ID da especificação", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Especificação por `ID`',
        summary='',
        operationId='Detalhes de uma Especificação',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        specification_schema[0]: specification_schema[1],
                        "example": {
                            "id": 250,
                            "product": 446,
                            "specification": 2,
                            "value_as_float": None,
                            "add_date": "2018-11-02T13:41:10.200595",
                            "change_date": "2018-11-02T13:42:23.529897"
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
    "EspecificacaoCreate": modules.ConvertizeLink(
        tags=["Especificacoes"],
        url='/{environment}/api/v2/products/specifications/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Especificação',
        summary='',
        operationId='Criar uma Especificação',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    specification_schema[0]: specification_schema[1],
                    "example": {
                        "product": 446,
                        "specification": 2,
                        "value": "Colibri",
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
                        specification_schema[0]: specification_schema[1],
                        "example": {
                            "id": 250,
                            "product": 446,
                            "specification": 2,
                            "value": "Colibri",
                            "value_as_float": None,
                            "add_date": "2018-11-02T13:41:10.200595",
                            "change_date": "2018-11-02T13:42:23.529897"
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
    "EspecificacaoUpdate": modules.ConvertizeLink(
        tags=["Especificacoes"],
        url='/{environment}/api/v2/options/{specification_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='specification_id', required=True, location='path',
                          description=u"ID da Especificação", schema={"type": "integer"}),
        ],
        description='Alterar uma Especificação',
        summary='',
        operationId='Alterar uma Especificação',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    specification_schema[0]: specification_schema[1],
                    "example": {
                        "product": 446,
                        "specification": 2,
                        "value": "Colibri"
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
                        specification_schema[0]: specification_schema[1],
                        "example": {
                            "id": 250,
                            "product": 446,
                            "specification": 2,
                            "value": "Colibri",
                            "value_as_float": None,
                            "add_date": "2018-11-02T13:41:10.200595",
                            "change_date": "2018-11-02T13:42:23.529897"
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
    "EspecificacaoDelete": modules.ConvertizeLink(
        tags=["Especificacoes"],
        url='/{environment}/api/v2/products/specifications/{specification_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='specification_id', required=True, location='path',
                          description=u"ID da Especificação", schema={"type": "integer"}),
        ],
        description='Deletar uma Especificação',
        summary='',
        operationId='Deletar uma Especificação',
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

    #
    # Imagens
    #

    "Imagens": modules.ConvertizeLink(
        tags=["Imagens"],
        url='/{environment}/api/v2/images/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query',
                          description=u"Filtro pelo ID da Imagem", schema={"type": "string"}),
            coreapi.Field(name='product_id', required=False, location='query',
                          description=u"Filtro pelo ID do produto", schema={"type": "string"}),
            coreapi.Field(name='title__icontains', required=False, location='query',
                          description=u"Filtro pelo Título da foto", schema={"type": "string"}),
            coreapi.Field(name='title__isnull', required=False, location='query',
                          description=u"Filtro pelo Título quando vazio", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Imagens',
        summary='',
        operationId='Lista de Imagens',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        images_schema[0]: images_schema[1],
                        "example": {
                            "count": 18,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "id": 14,
                                    "position": 1,
                                    "title": "",
                                    "image": "https://io.convertiez.com.br/m/apisandbox/shop/products/images/2020562/roupao-microfibra-home-design-p-rosa-antigo-100-poliester-corttex_ff794107-e505-4677-8619-a360c99c1cd4.jpg",                              "color": "",
                                    "video": "",
                                    "add_date": "2019-07-23T13:44:27.935202",
                                    "change_date": "2019-07-23T13:44:27.935266",
                                    "product": 2020562,
                                    "skus": []
                                },
                                {
                                    "id": 646,
                                    "position": 1,
                                    "title": "",
                                    "image": "https://io.convertiez.com.br/m/apisandbox/shop/products/images/2020563/roupao-microfibra-home-design-g-rosa-antigo-100-poliester-corttex_c682cdde-866f-4247-985e-aa817677688a.jpg",
                                    "video": "",
                                    "add_date": "2019-07-23T13:45:56.633235",
                                    "change_date": "2019-07-23T13:45:56.633265",
                                    "product": 2020563,
                                    "skus": []
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
    "Imagem": modules.ConvertizeLink(
        tags=["Imagens"],
        url='/{environment}/api/v2/images/{image_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='image_id', required=True, location='path',
                          description=u"ID da imagem", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Detalhes de uma imagem por `ID`',
        summary='',
        operationId='Detalhes de uma imagem',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        image_schema[0]: image_schema[1],
                        "example": {
                            "id": 646,
                            "position": 1,
                            "title": "",
                            "image": "https://io.convertiez.com.br/m/apisandbox/shop/products/images/2020563/roupao-microfibra-home-design-g-rosa-antigo-100-poliester-corttex_c682cdde-866f-4247-985e-aa817677688a.jpg",
                            "video": "",
                            "add_date": "2019-07-23T13:45:56.633235",
                            "change_date": "2019-07-23T13:45:56.633265",
                            "product": 2020563,
                            "skus": []
                        },
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
    "ImagemCreate": modules.ConvertizeLink(
        tags=["Imagens"],
        url='/{environment}/api/v2/images/download/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Imagem',
        summary='',
        operationId='Criar uma Imagem',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    image_schema[0]: image_schema[1],
                    "example": {
                        "title": None,
                        "image": None,
                        "video": None,
                        "position": 2,
                        "product": 2020562,
                        "skus": []
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
                        image_schema[0]: image_schema[1],
                        "example": {
                            "id": 668,
                            "position": 2,
                            "title": None,
                            "image": None,
                            "video": None,
                            "add_date": "2019-10-04T16:29:22.079009",
                            "change_date": "2019-10-04T16:29:22.079040",
                            "product": 2020562,
                            "skus": []
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
    "ImagemUpdate": modules.ConvertizeLink(
        tags=["Imagens"],
        url='/{environment}/api/v2/images/{image_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='image_id', required=True, location='path',
                          description=u"ID da Imagem", schema={"type": "integer"}),
        ],
        description='Alterar uma Imagem',
        summary='',
        operationId='Alterar uma Imagem',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    image_schema[0]: image_schema[1],
                    "example": {
                        "title": None,
                        "image": None,
                        "video": None,
                        "position": 2,
                        "product": 2020562,
                        "skus": []
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
                        image_schema[0]: image_schema[1],
                        "example": {
                            "id": 668,
                            "position": 2,
                            "title": None,
                            "image": None,
                            "video": None,
                            "add_date": "2019-10-04T16:29:22.079009",
                            "change_date": "2019-10-04T16:34:10.487435",
                            "product": 2020562,
                            "skus": []
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
    "ImagemDelete": modules.ConvertizeLink(
        tags=["Imagens"],
        url='/{environment}/api/v2/images/{image_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='image_id', required=True, location='path',
                          description=u"ID da Imagem", schema={"type": "integer"}),
        ],
        description='Deletar uma Imagem',
        summary='',
        operationId='Deletar uma Imagem',
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
    #
    # Distributors
    #

    "Fornecedores": modules.ConvertizeLink(
        tags=["Fornecedores"],
        url='/{environment}/api/v2/distributors/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query',
                          description=u"ID do distribuidor", schema={"type": "string"}),
            coreapi.Field(name='name__icontains', required=False, location='query',
                          description=u"Nome que contenha", schema={"type": "string"}),
            coreapi.Field(name='active', required=False, location='query',
                          description=u"Ativo (1 = Sim, 0 = Não)"),
            coreapi.Field(name='reference_code', required=False,
                          location='query', description=u"Codigo de referencia"),
            coreapi.Field(name='reference_code__isnull', required=False, location='query',
                          description=u"Somente referencias vazias", schema={"type": "string"}),
        ],
        description='Retorna uma lista de Fornecedores',
        summary='',
        operationId='Lista de Fornecedores',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        distributors_schema[0]: distributors_schema[1],
                        "example": {
                            "count": 1,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "url": "/api/1.0/distributors/2/",
                                    "id": 2,
                                    "name": "Teste",
                                    "active": True,
                                    "min_value": None,
                                    "single_purchase": False,
                                    "add_date": "2019-10-04T17:08:59.085531",
                                    "change_date": "2019-10-04T17:08:59.085576",
                                    "reference_code": None
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
    "Fornecedor": modules.ConvertizeLink(
        tags=["Fornecedores"],
        url='/{environment}/api/v2/distributors/{distributor_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='distributor_id', required=True, location='path',
                          description=u"ID do fornecedor ", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query',
                          description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query',
                          description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query',
                          description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query',
                          description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Fornecedor por `ID`',
        summary='',
        operationId='Detalhes de um Fornecedor',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        specification_schema[0]: specification_schema[1],
                        "example": {
                            "url": "/api/1.0/distributors/2/",
                            "id": 2,
                            "name": "Teste",
                            "active": True,
                            "min_value": None,
                            "single_purchase": False,
                            "add_date": "2019-10-04T17:08:59.085531",
                            "change_date": "2019-10-04T17:08:59.085576",
                            "reference_code": None
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
    "FornecedorCreate": modules.ConvertizeLink(
        tags=["Fornecedores"],
        url='/{environment}/api/v2/distributors/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar um Fornecedor',
        summary='',
        operationId='Criar um Fornecedor',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    distributor_schema[0]: distributor_schema[1],
                    "example": {
                        "name": "Teste",
                        "active": True,
                        "min_value": None,
                        "single_purchase": False,
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
                        distributor_schema[0]: distributor_schema[1],
                        "example": {
                            "url": "/api/1.0/distributors/2/",
                            "id": 2,
                            "name": "Teste",
                            "active": True,
                            "min_value": None,
                            "single_purchase": False,
                            "add_date": "2019-10-04T17:08:59.085531",
                            "change_date": "2019-10-04T17:08:59.085576",
                            "reference_code": None
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
    "FornecedorUpdate": modules.ConvertizeLink(
        tags=["Fornecedores"],
        url='/{environment}/api/v2/distributors/{distributor_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='distributor_id', required=True, location='path',
                          description=u"ID do fornecedor", schema={"type": "integer"}),
        ],
        description='Alterar um Fornecedor',
        summary='',
        operationId='Alterar um Fornecedor',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    specification_schema[0]: specification_schema[1],
                    "example": {
                        "name": "Teste",
                        "active": True,
                        "single_purchase": False
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
                        distributor_schema[0]: distributor_schema[1],
                        "example": {
                            "url": "/api/1.0/distributors/2/",
                            "id": 2,
                            "name": "Teste",
                            "active": True,
                            "min_value": None,
                            "single_purchase": False,
                            "add_date": "2019-10-04T17:08:59.085531",
                            "change_date": "2019-10-04T17:08:59.085576",
                            "reference_code": None
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
    "FornecedorDelete": modules.ConvertizeLink(
        tags=["Fornecedores"],
        url='/{environment}/api/v2/products/distributors/{distributor_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path',
                          description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='distributor_id', required=True, location='path',
                          description=u"ID da Especificação", schema={"type": "integer"}),
        ],
        description='Deletar um Fornecedor',
        summary='',
        operationId='Deletar um Fornecedor',
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
