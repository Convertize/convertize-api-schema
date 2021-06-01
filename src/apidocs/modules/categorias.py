# coding: utf-8
import coreapi
from apidocs import modules


categorie_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da categoria"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título"),
    modules.new_propertie(name="slug", type="string", nullable=False, description=u"Slug `(url)`, caso vazio o sistema gera automaticamente"),
    modules.new_propertie(name="active", type="boolean", nullable=False, description=u"Indica se esta ativo `default = true`"),
    modules.new_propertie(name="parent", type="integer", nullable=False, description=u"ID da categoria pai"),
    modules.new_propertie(name="meta_title", type="string", nullable=False, description=u"Titulo da categoria para SEO"),
    modules.new_propertie(name="meta_description", type="string", nullable=False, description=u"Descrição da categoria para SEO"),
    modules.new_propertie(name="meta_keywords", type="string", nullable=False, description=u"Keywords da categoria para SEO separadas por `“,”`"),
    modules.new_propertie(name="inherit_template", type="boolean", nullable=False, description=u"Herdar template do pai"),
    modules.new_propertie(name="global_code", type="boolean", nullable=False, description=u"Código da categoria Global `(Google)`")
])

categories_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=categorie_componente)
        )))
    )))

categorie_schema = modules.new_propertie(name="schema", type="object", properties=categorie_componente, required=["id", "title"])



export = {
    "Categorias": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/categories/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de categorias',
        summary='',
        operationId='Lista de Categorias',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        categories_schema[0]: categories_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/categories/?page=2",
                            "previous": None,
                            "results": [
                                {
                                    "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/categories/4/",
                                    "id": 4,
                                    "parent": None,
                                    "_order": 2,
                                    "title": "Borracharia",
                                    "slug": "borracharia",
                                    "active": True,
                                    "add_date": "2014-07-24T09:39:34.660080",
                                    "change_date": "2016-10-06T13:13:00.845996",
                                    "meta_title": "Borracharia - Materiais para Borracharia",
                                    "meta_description": "Grande variedade em ferramentas para Borracharia. Compre agora suas ferramentas para Borracharia, aproveite as melhores marcas e modelos que temos para oferecer. Acesse!",
                                    "meta_keywords": "borracharia",
                                    "inherit_template": False,
                                    "global_code": None,
                                    "lft": 1,
                                    "rght": 36,
                                    "tree_id": 2,
                                    "level": 0
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
    "Categorie": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/categories/{categorie_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='categorie_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma uma categoria por `ID`',
        summary='',
        operationId='Detalhes de uma Categoria',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    categorie_schema[0]: categorie_schema[1],
                    "example": {
                        "id": 4,
                        "parent": None,
                        "_order": 2,
                        "title": "Borracharia",
                        "slug": "borracharia",
                        "active": True,
                        "add_date": "2014-07-24T09:39:34.660080",
                        "change_date": "2016-10-06T13:13:00.845996",
                        "meta_title": "Borracharia - Materiais para Borracharia",
                        "meta_description": "Grande variedade em ferramentas para Borracharia. Compre agora suas ferramentas para Borracharia, aproveite as melhores marcas e modelos que temos para oferecer. Acesse!",
                        "meta_keywords": "borracharia",
                        "inherit_template": False,
                        "global_code": None,
                        "lft": 1,
                        "rght": 36,
                        "tree_id": 2,
                        "level": 0
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
    "CategorieCreate": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/categories/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Categoria',
        summary='',
        operationId='Criar uma Categoria',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    categorie_schema[0]: categorie_schema[1],
                    "example": {
                        "title": "TITULO",
                        "active": True,
                        "meta_title": "TITULO SEO",
                        "meta_description": "DESCRICAO SEO",
                        "meta_keywords": "KEYWORDS SEO",
                        "inherit_template": False
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
                    categorie_schema[0]: categorie_schema[1],
                    "example": {
                        "title": "TITULO",
                        "active": True,
                        "meta_title": "TITULO SEO",
                        "meta_description": "DESCRICAO SEO",
                        "meta_keywords": "KEYWORDS SEO",
                        "inherit_template": False
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
    "CategorieUpdate": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/categories/{categorie_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='categorie_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
        ],
        description='Alterar uma Categoria',
        summary='',
        operationId='Alterar uma Categoria',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    categorie_schema[0]: categorie_schema[1],
                    "example": {
                        "title": "TITULO",
                        "slug": "teste",
                        "active": True,
                        "meta_title": "TITULO SEO",
                        "meta_description": "DESCRICAO SEO",
                        "meta_keywords": "KEYWORDS SEO",
                        "inherit_template": False
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
                    categorie_schema[0]: categorie_schema[1],
                    "example": {
                        "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/categories/74/",
                        "id": 74,
                        "parent": 4,
                        "_order": 65,
                        "title": "TITULO",
                        "slug": "teste",
                        "active": True,
                        "add_date": "2014-09-11T14:19:23.997496",
                        "change_date": "2014-12-26T16:38:32.426313",
                        "meta_title": "TITULO SEO",
                        "meta_description": "DESCRICAO SEO",
                        "meta_keywords": "KEYWORDS SEO",
                        "inherit_template": False,
                        "global_code": None,
                        "lft": 2,
                        "rght": 3,
                        "tree_id": 2,
                        "level": 1
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
    "CategorieDelete": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/categories/{categorie_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='categorie_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
        ],
        description='Deletar uma Categoria',
        summary='',
        operationId='Deletar uma Categoria',
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
