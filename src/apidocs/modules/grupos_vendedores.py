# coding: utf-8
import coreapi
from apidocs import modules

sellers_group_componente = dict([
    modules.new_propertie(name="id", type="integer", format="int64", nullable=False, description=u"ID do grupo"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título do grupo")    
])


sellers_groups_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=sellers_group_componente)
        )))
    )))


sellers_group_schema = modules.new_propertie(name="schema", type="object", properties=sellers_group_componente, required=["id", "title"])


export = {
    "GruposVendedores": modules.ConvertizeLink(
        tags=["Grupos"],
        url='/{environment}/api/v2/telesales/groups',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),            
        ],
        description='Retorna uma lista de grupos de vendedores',
        summary='',
        operationId='Lista de Grupos de Vendedores',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        sellers_groups_schema[0]: sellers_groups_schema[1],
                        "example": {
                            "count": 3,
                            "next": None,
                            "previous": None,
                            "results": [                             
                                      {
                                    "id": 2,
                                    "title": "Prata"
                                      },
                                    {
                                    "id": 1,
                                    "title": "Bronze"
                                    },
                                    {
                                    "id": 3,
                                    "title": "Ouro"
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
    "GrupoVendedores": modules.ConvertizeLink(
        tags=["Grupos"],
        url='/{environment}/api/v2/telesales/sellers/?group={group_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='group_id', required=True, location='path', description=u"ID do grupo", schema={"type": "integer"}),
                    ],
        description='Retorna grupo por `ID`',
        summary='',
        operationId='Detalhes de um grupo',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    sellers_group_schema[0]: sellers_group_schema[1],
                    "example": {
                        "id": 2,
                        "title": "Prata"
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
    "GrupoVendedoresCreate": modules.ConvertizeLink(
        tags=["Categorias"],
        url='/{environment}/api/v2/telesales/groups/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar um Grupo de Vendedores',
        summary='',
        operationId='Criar um Grupo de Vendores',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    sellers_group_schema[0]: sellers_group_schema[1],
                    "example": {
                        "title": "Ouro"                        
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
                    sellers_group_schema[0]: sellers_group_schema[1],
                    "example": {
                        "id":3,
                        "title": "Ouro"                        
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
    "GrupoVendedoresUpdate": modules.ConvertizeLink(
        tags=["Grupos"],
        url='/{environment}/api/v2/telesales/groups/{group_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='group_id', required=True, location='path', description=u"ID do grupo", schema={"type": "integer"}),
        ],
        description='Alterar um Grupo de Vendedores',
        summary='',
        operationId='Alterar um Grupo de Vendedores',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    sellers_group_schema[0]: sellers_group_schema[1],
                    "example": {                        
                        "title": "Ouro"
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
                    sellers_group_schema[0]: sellers_group_schema[1],
                    "example": {
                        "id": 74,
                        "title": "Ouro"                        
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
    "GrupoVendedoresDelete": modules.ConvertizeLink(
        tags=["Grupos"],
        url='/{environment}/api/v2/telesales/groups/{group_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='group_id', required=True, location='path', description=u"ID do grupo de vendedores", schema={"type": "integer"}),
        ],
        description='Deletar um Grupo de Vendedores',
        summary='',
        operationId='Deletar um Grupo de Vendedores',
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

