# coding: utf-8
import coreapi
from apidocs import modules


grid_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da categoria"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título"),
    modules.new_propertie(name="display", type="string", nullable=False, description=u"Forma de display opções", enum=["radio", "select", "custom"]),
    modules.new_propertie(name="active", type="boolean", nullable=False, description=u"Indica se esta ativo `default = true`"),
    modules.new_propertie(name="reference_code", type="string", nullable=True, description=u"Código de referência ou código da grade no ERP"),
])

grids_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=grid_componente)
        )))
    )))

grid_schema = modules.new_propertie(name="schema", type="object", properties=grid_componente, required=["id", "title"])

option_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da opção"),
    modules.new_propertie(name="grid", type="integer", nullable=False, description=u"ID da Grade"),
    modules.new_propertie(name="position", type="integer", nullable=False, description=u"Ordem das opções"),
    modules.new_propertie(name="title", type="string", nullable=False, description=u"Título"),
    modules.new_propertie(name="slug", type="string", nullable=False, description=u"Slug `(url)`, caso vazio o sistema gera automaticamente"),
    modules.new_propertie(name="filterable", type="boolean", nullable=False, description=u"Define se a opção será filtravel `default = true`"),
    modules.new_propertie(name="ungroup", type="boolean", nullable=False, description=u"Define se a opção deverá ser desagrupada `default = true`"),
    modules.new_propertie(name="display", type="string", nullable=False, description=u"Forma de display opções (`checkbox, color, size`)", enum=["checkbox", "color", "size"]),
    modules.new_propertie(name="reference_code", type="string", nullable=True, description=u"Código de referência ou código da grade no ERP"),
])

options_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=option_componente)
        )))
    )))

option_schema = modules.new_propertie(name="schema", type="object", properties=option_componente, required=["id", "title"])

value_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do valor"),
    modules.new_propertie(name="option", type="integer", nullable=False, description=u"ID da Opção"),
    modules.new_propertie(name="position", type="integer", nullable=False, description=u"Ordem do Valor"),
    modules.new_propertie(name="value", type="string", nullable=False, description=u"Valor"),
    modules.new_propertie(name="color", type="string", nullable=False, description=u"#Hexadecimal - (`separar por virgula caso haja mais de uma`)"),
    modules.new_propertie(name="reference_code", type="string", nullable=True, description=u"Código de referência ou código da grade no ERP"),
])

values_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "title"]),
            modules.new_propertie(name="properties", enum=value_componente)
        )))
    )))

value_schema = modules.new_propertie(name="schema", type="object", properties=value_componente, required=["id", "title"])



export = {
    "Grades": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v1/grids/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID da grade", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Grades',
        summary='',
        operationId='Lista de Grades',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        grids_schema[0]: grids_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/grids/?page=2",
                            "previous": None,
                            "results": [
                                {
                                  "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/grids/1/",
                                  "id": 1,
                                  "title": "Esmerilhadeiras",
                                  "display": "radio",
                                  "reference_code": None,
                                  "add_date": "2014-07-24T09:44:23.173981",
                                  "change_date": "2014-07-24T09:53:45.519836"
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
    "Grade": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v1/grids/{grid_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='grid_id', required=True, location='path', description=u"ID da grade", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Grade por `ID`',
        summary='',
        operationId='Detalhes de uma Grade',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    grid_schema[0]: grid_schema[1],
                    "example": {
                        "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/grids/1/",
                        "id": 1,
                        "title": "Esmerilhadeiras",
                        "display": "radio",
                        "reference_code": None,
                        "add_date": "2014-07-24T09:44:23.173981",
                        "change_date": "2014-07-24T09:53:45.519836"
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
    "GradeCreate": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v1/grids/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Grade',
        summary='',
        operationId='Criar uma Grade',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    grid_schema[0]: grid_schema[1],
                    "example": {
                        "title": "Trenas",
                        "active": True,
                        "display": "radio",
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
                    grid_schema[0]: grid_schema[1],
                    "example": {
                      "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/grids/2/",
                      "id": 2,
                      "title": "Trenas",
                      "display": "radio",
                      "reference_code": None,
                      "active": True,
                      "add_date": "2014-07-31T10:14:19.039051",
                      "change_date": "2014-07-31T10:14:41.881381"
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
    "GradeUpdate": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v1/grids/{grid_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='grid_id', required=True, location='path', description=u"ID da grade", schema={"type": "integer"}),
        ],
        description='Alterar uma Grade',
        summary='',
        operationId='Alterar uma Grade',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    grid_schema[0]: grid_schema[1],
                    "example": {
                        "title": "Trenas",
                        "active": True,
                        "display": "radio",
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
                    grid_schema[0]: grid_schema[1],
                    "example": {
                      "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v1/grids/2/",
                      "id": 2,
                      "title": "Trenas",
                      "display": "radio",
                      "reference_code": None,
                      "active": True,
                      "add_date": "2014-07-31T10:14:19.039051",
                      "change_date": "2014-07-31T10:14:41.881381"
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
    "GradeDelete": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v1/grids/{grid_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='grid_id', required=True, location='path', description=u"ID da grade", schema={"type": "integer"}),
        ],
        description='Deletar uma Grade',
        summary='',
        operationId='Deletar uma Grade',
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
    # Options
    #

    "GradesOpcoes": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v2/options/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID da opção", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
        ],
        description='Retorna uma lista de Opções',
        summary='',
        operationId='Lista de Opções',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        options_schema[0]: options_schema[1],
                        "example": {
                            "count": 188,
                            "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/options/?page=2",
                            "previous": None,
                            "results": [
                                {
                                  "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/options/5/",
                                  "id": 5,
                                  "grid": 43,
                                  "position": 0,
                                  "title": "Cor",
                                  "slug": "cor",
                                  "filterable": False,
                                  "ungroup": False,
                                  "display": None,
                                  "reference_code": None,
                                  "add_date": "2015-11-11T18:06:14.024972",
                                  "change_date": "2015-11-11T18:06:14.024989"
                              },
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
    "GradesOpcao": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v2/options/{option_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='option_id', required=True, location='path', description=u"ID da grade", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de Opção por `ID`',
        summary='',
        operationId='Detalhes de uma Opção',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    option_schema[0]: option_schema[1],
                    "example": {
                        "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/options/1/",
                        "id": 1,
                        "title": "Esmerilhadeiras",
                        "display": "radio",
                        "reference_code": None,
                        "add_date": "2014-07-24T09:44:23.173981",
                        "change_date": "2014-07-24T09:53:45.519836"
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
    "GradesOpcaoCreate": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v2/options/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Opção',
        summary='',
        operationId='Criar uma Opção',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    option_schema[0]: option_schema[1],
                    "example": {
                      "title": "Tamanho",
                      "filterable": False,
                      "filterable": False,
                      "ungroup": False,
                      "grid": 5
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
                    option_schema[0]: option_schema[1],
                    "example": {
                      "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/options/2/",
                      "id": 2,
                      "grid": 5,
                      "position": 0,
                      "title": "Tamanho",
                      "slug": "tamanho",
                      "filterable": False,
                      "ungroup": False,
                      "display": None,
                      "reference_code": None,
                      "add_date": "2014-08-18T16:58:42.012403",
                      "change_date": "2014-08-18T17:03:43.902259"
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
    "GradesOpcaoUpdate": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v2/options/{option_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='option_id', required=True, location='path', description=u"ID da Opção", schema={"type": "integer"}),
        ],
        description='Alterar uma Opção',
        summary='',
        operationId='Alterar uma Opção',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "title"],
                    option_schema[0]: option_schema[1],
                    "example": {
                      "title": "Tamanho",
                      "filterable": False,
                      "filterable": False,
                      "ungroup": False,
                      "grid": 5
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
                    option_schema[0]: option_schema[1],
                    "example": {
                      "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/options/2/",
                      "id": 2,
                      "grid": 5,
                      "position": 0,
                      "title": "Tamanho",
                      "slug": "tamanho",
                      "filterable": False,
                      "ungroup": False,
                      "display": None,
                      "reference_code": None,
                      "add_date": "2014-08-18T16:58:42.012403",
                      "change_date": "2014-08-18T17:03:43.902259"
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
    "GradesOpcaoDelete": modules.ConvertizeLink(
        tags=["Grades"],
        url='/{environment}/api/v2/options/{option_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='option_id', required=True, location='path', description=u"ID da Opção", schema={"type": "integer"}),
        ],
        description='Deletar uma Opção',
        summary='',
        operationId='Deletar uma Opção',
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
  # Valores
  #

  "GradesOpcoesValores": modules.ConvertizeLink(
      tags=["Grades"],
      url='/{environment}/api/v2/values/',
      action='get',
      fields=[
          coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
          coreapi.Field(name='id', required=False, location='query', description=u"Filtro pelo ID da opção", schema={"type": "string"}),
          coreapi.Field(name='reference_code', required=False, location='query', description=u"Código de referência ou código da grade no ERP", schema={"type": "string"}),
          coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
          coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
          coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
          coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "string", "format": "date-time"}),
      ],
      description='Retorna uma lista de Valores',
      summary='',
      operationId='Lista de Valores',
      template={
          "200": {
              "description": "Success",
              "content": {
                  "application/json": {
                      values_schema[0]: values_schema[1],
                      "example": {
                          "count": 188,
                          "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/values/?page=2",
                          "previous": None,
                          "results": [
                            {
                              "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/values/14/",
                              "id": 14,
                              "option": 5,
                              "position": 0,
                              "value": "Azul",
                              "color": "",
                              "reference_code": None,
                              "add_date": "2015-11-11T18:06:14.383121",
                              "change_date": "2015-11-11T18:38:46.746944"
                            },
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
  "GradesOpcoesValor": modules.ConvertizeLink(
      tags=["Grades"],
      url='/{environment}/api/v2/values/{option_id}/',
      action='get',
      fields=[
          coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
          coreapi.Field(name='option_id', required=True, location='path', description=u"ID da grade", schema={"type": "integer"}),
          coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
          coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
          coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
          coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
      ],
      description='Detalhes de um Valor por `ID`',
      summary='',
      operationId='Detalhes de um Valor',
      template={
          "200": {
          "description": "Success",
          "content": {
              "application/json": {
                  value_schema[0]: value_schema[1],
                  "example": {
                    "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/values/14/",
                    "id": 14,
                    "option": 5,
                    "position": 0,
                    "value": "Azul",
                    "color": "",
                    "reference_code": None,
                    "add_date": "2015-11-11T18:06:14.383121",
                    "change_date": "2015-11-11T18:38:46.746944"
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
  "GradesOpcoesValorCreate": modules.ConvertizeLink(
      tags=["Grades"],
      url='/{environment}/api/v2/values/',
      action='post',
      fields=[
          coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
      ],
      description='Criar um Valor',
      summary='',
      operationId='Criar um Valor',
      requestBody={
          "content": {
              "application/json": {
                  "required": ["id", "title"],
                  value_schema[0]: value_schema[1],
                  "example": {
                    "value": "Azul",
                    "option": 5
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
                  value_schema[0]: value_schema[1],
                  "example": {
                    "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/values/14/",
                    "id": 14,
                    "option": 5,
                    "position": 0,
                    "value": "Azul",
                    "color": "",
                    "reference_code": None,
                    "add_date": "2015-11-11T18:06:14.383121",
                    "change_date": "2015-11-11T18:38:46.746944"
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
  "GradesOpcoesValorUpdate": modules.ConvertizeLink(
      tags=["Grades"],
      url='/{environment}/api/v2/values/{value_id}/',
      action='put',
      fields=[
          coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
          coreapi.Field(name='value_id', required=True, location='path', description=u"ID do Valor", schema={"type": "integer"}),
      ],
      description='Alterar um Valor',
      summary='',
      operationId='Alterar um Valor',
      requestBody={
          "content": {
              "application/json": {
                  "required": ["id", "title"],
                  value_schema[0]: value_schema[1],
                  "example": {
                    "value": "Azul",
                    "option": 5
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
                  value_schema[0]: value_schema[1],
                  "example": {
                    "url": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/values/14/",
                    "id": 14,
                    "option": 5,
                    "position": 0,
                    "value": "Azul",
                    "color": "",
                    "reference_code": None,
                    "add_date": "2015-11-11T18:06:14.383121",
                    "change_date": "2015-11-11T18:38:46.746944"
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
  "GradesOpcoesValorDelete": modules.ConvertizeLink(
      tags=["Grades"],
      url='/{environment}/api/v2/values/{value_id}/',
      action='delete',
      fields=[
          coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
          coreapi.Field(name='value_id', required=True, location='path', description=u"ID do Valor", schema={"type": "integer"}),
      ],
      description='Deletar um Valor',
      summary='',
      operationId='Deletar um Valor',
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
