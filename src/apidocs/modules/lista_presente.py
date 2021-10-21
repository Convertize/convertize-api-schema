# coding: utf-8
import coreapi
from apidocs import modules

gift_list_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID da lista"),
    modules.new_propertie(name="reference_code",type="string",description=u"Código de referência"),
    modules.new_propertie(name="url",type="string", description=u"URL da Lista de Presente (On-Line) gerado automaticamente"),
    modules.new_propertie(name="type_list", type="integer", format="Int4", description=u"ID do Tipo da Lista"),
    modules.new_propertie(name="customer", type="integer", format="int4", description=u"ID do Cliente"),
    modules.new_propertie(name="date", type="datetime.date", description=u"Data do Evento"),
    modules.new_propertie(name="state", type="string", description=u"Estado do Evento"),
    modules.new_propertie(name="guests", type="string", description=u"Número de Convidados"),
    modules.new_propertie(name="message", type="string", description=u"Mensagem para os convidados que acessarem a sua lista"),
    modules.new_propertie(name="collection", type="integer", format="int4", description=u"ID da coleção, usado para lista pronta"),
    modules.new_propertie(name="notification", type="boolean", description=u"Deseja receber informações sobre minha lista por e-mail"),
    modules.new_propertie(name="publish", type="boolean", description=u"Deixar minha lista disponível no site"),
    modules.new_propertie(name="status", type="string", nullable=False, description=u"Status da lista (A = Ativa, F = Finalizada, I = Inativa, E = Excluída), default = A"),
    modules.new_propertie(name="ceremony_zipcode", type="string", description=u"CEP do Local da Cerimônia"),
    modules.new_propertie(name="ceremony_address", type="string", description=u"Endereço do Local da Cerimônia"),
    modules.new_propertie(name="ceremony_number", type="string", description=u"Número do local da Cerimônia"),
    modules.new_propertie(name="ceremony_neighborhood", type="string", description=u"Bairro do Local da Cerimônia"),
    modules.new_propertie(name="ceremony_complement", type="string", description=u"Complemento do Local da Cerimônia"),
    modules.new_propertie(name="ceremony_city", type="string", description=u"Cidade do Local da Cerimônia"),
    modules.new_propertie(name="ceremony_state", type="string", description=u"Estado do Local da Cerimônia"),
    modules.new_propertie(name="reception_zipcode", type="string", description=u"CEP do Local da Festa"),
    modules.new_propertie(name="reception_address", type="string", description=u"Endereço do Local da Festa"),
    modules.new_propertie(name="reception_number", type="string", description=u"Número do Local da Festa"),
    modules.new_propertie(name="reception_neighborhood", type="string", description=u"Bairro do Local da Festa"),
    modules.new_propertie(name="reception_complement", type="string", description=u"Complemento do Local da Festa"),
    modules.new_propertie(name="reception_city", type="string", description=u"Cidade do Local da Festa"),
    modules.new_propertie(name="reception_state", type="string", description=u"Estado do Local da Festa"),
    modules.new_propertie(name="name", type="string", description=u"Nome do dono da Lista"),
    modules.new_propertie(name="email", type="string", description=u"E-mail do dono da Lista"),
    modules.new_propertie(name="mother_name", type="string", description=u"Nome da mãe do dono da Lista"),
    modules.new_propertie(name="father_name", type="string", description=u"Nome do pai do dono da Lista"),
    modules.new_propertie(name="partner_name", type="string", description=u"Nome do parceiro da Lista"),
    modules.new_propertie(name="partner_email", type="string", description=u"E-mail do parceiro da Lista"),
    modules.new_propertie(name="partner_mother_name", type="string", description=u"Nome da mãe do parceiro da Lista"),
    modules.new_propertie(name="partner_father_name", type="string", description=u"Nome do pai do parceiro da Lista"),
    modules.new_propertie(name="shipping_zipcode", type="string", description=u"CEP de Entrega"),
    modules.new_propertie(name="shipping_address", type="string", description=u"Endereço de Entrega"),
    modules.new_propertie(name="shipping_number", type="string", description=u"Número de Entrega"),
    modules.new_propertie(name="shipping_neighborhood", type="string", description=u"Bairro de Entrega"),
    modules.new_propertie(name="shipping_complement", type="string", description=u"Complemento de Entrega"),
    modules.new_propertie(name="shipping_city", type="string", description=u"Cidade de Entrega"),
    modules.new_propertie(name="shipping_state", type="string", description=u"Estado de Entrega"),
    modules.new_propertie(name="shipping_date", type="datetime.date", description=u"Data de entrega"),
    modules.new_propertie(name="shipping_description", type="string", description=u"Observação da entrega"),
    modules.new_propertie(name="add_date", type="datetime.date", description=u"Data de criação"),
    modules.new_propertie(name="change_date", type="datetime.date", description=u"Data de alteração"),
    modules.new_propertie(name="user", type="integer", format="int4",  description=u"ID do usuario, quando criado pela administração"),
    modules.new_propertie(name="giftcard", type="integer", format="int4",  description=u"Dados do GiftCard, quando o pedido é entregue por vale. Gerado automaticamente"),
    ])



gift_lists_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "referece_code"]),
            modules.new_propertie(name="properties", enum=gift_list_componente)
        )))
    )))



gift_list_schema = modules.new_propertie(name="schema", type="object", properties=gift_list_componente, required=["id", "referece_code"])



export = {
    "ListasPresente": modules.ConvertizeLink(
        tags=["Presentes"],
        url='/{environment}/api/v2/giftlists/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"ID da Lista", schema={"type":"integer"}),
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Código de referência", schema={"type":"string"}),
            coreapi.Field(name='type_list', required=False, location='query', description=u"Tipo de lista"),           
            
        ],
        description='Retorna uma lista de presentes',
        summary='',
        operationId='Lista de Presentes',
        template={
            "200": {
                "description": "Success",
                "content": {
                    "application/json": {
                        gift_lists_schema[0]: gift_lists_schema[1],
                        "example": {
                             "count": 188,
                             "next": "https://api.convertize.com.br/{ENVIRONMENT}/api/v2/giftlists/?page=2",
                             "previous": None,
                             "results": [
                                {
                                    "id": 24,
                                    "reference_code": "",
                                    "url": "/lista/presente/isabella-magalhaes-e-murillo-augusto-moreira-bonamini/24/",
                                    "type_list": 4,
                                    "customer": 72,
                                    "date": "2018-12-29",
                                    "state": None,
                                    "city": None,
                                    "guests": None,
                                    "message": None,
                                    "collection": None,
                                    "notification": True,
                                    "publish": True,
                                    "status": "A",
                                    "ceremony_zipcode": "",
                                    "ceremony_address": "",
                                    "ceremony_number": "",
                                    "ceremony_neighborhood": "",
                                    "ceremony_complement": "",
                                    "ceremony_city": "",
                                    "ceremony_state": None,
                                    "reception_zipcode": "",
                                    "reception_address": "",
                                    "reception_number": "",
                                    "reception_neighborhood": "",
                                    "reception_complement": "",
                                    "reception_city": "",
                                    "reception_state": None,
                                    "name": "Isabella Magalhães",
                                    "email": "isahiroshima1999@gmail.com",
                                    "mother_name": "Andreia Magalhães",
                                    "father_name": "Sidney Cortiglio",
                                    "partner_name": "Murillo Augusto Moreira Bonamini",
                                    "partner_email": "",
                                    "partner_mother_name": "Andrea Bonamini",
                                    "partner_father_name": "Gilberto Bonamini",
                                    "shipping_zipcode": "37580-000",
                                    "shipping_address": "Rua Bahia",
                                    "shipping_number": "261",
                                    "shipping_neighborhood": "Magioli",
                                    "shipping_complement": "Loja",
                                    "shipping_city": "MONTE SIÃO",
                                    "shipping_state": "MG",
                                    "shipping_date": None,
                                    "shipping_description": None,
                                    "add_date": "2018-07-02T17:05:26.448387",
                                    "change_date": "2018-07-02T17:21:02.975380",
                                    "user": None,
                                    "giftcard": None,
                                    "gift_items": []
                                },
                                {
                                    "id": 23,
                                    "reference_code": "",
                                    "url": "/lista/presente/leonardo-moreira-e-jessica-lopes-de-lima/23/",
                                    "type_list": 1,
                                    "customer": 69,
                                    "date": "2018-07-25",
                                    "state": None,
                                    "city": None,
                                    "guests": None,
                                    "message": "",
                                    "collection": None,
                                    "notification": True,
                                    "publish": True,
                                    "status": "E",
                                    "ceremony_zipcode": "",
                                    "ceremony_address": "",
                                    "ceremony_number": "",
                                    "ceremony_neighborhood": "",
                                    "ceremony_complement": "",
                                    "ceremony_city": "",
                                    "ceremony_state": None,
                                    "reception_zipcode": "",
                                    "reception_address": "",
                                    "reception_number": "",
                                    "reception_neighborhood": "",
                                    "reception_complement": "",
                                    "reception_city": "",
                                    "reception_state": None,
                                    "name": "Leonardo Moreira",
                                    "email": "leomoreiraa.94@gmail.com",
                                    "mother_name": "Benedita Ap. Pinto",
                                    "father_name": "Leonel Moreira",
                                    "partner_name": "Jéssica Lopes de Lima",
                                    "partner_email": "jessicahlima431@gmail.com",
                                    "partner_mother_name": "Tatiane Marques Lopes",
                                    "partner_father_name": "José Edilson de Lima",
                                    "shipping_zipcode": "18460-000",
                                    "shipping_address": "Rua Lauro Novaes Ribas",
                                    "shipping_number": "23",
                                    "shipping_neighborhood": "Tonico Adolfo",
                                    "shipping_complement": "Casa",
                                    "shipping_city": "ITARARÉ",
                                    "shipping_state": "SP",
                                    "shipping_date": None,
                                    "shipping_description": "",
                                    "add_date": "2018-06-22T03:46:40.451939",
                                    "change_date": "2018-06-25T13:12:38.486048",
                                    "user": None,
                                    "giftcard": None,
                                    "gift_items": []
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
    "ListaPresente": modules.ConvertizeLink(
        tags=["Presentes"],
        url='/{environment}/api/v2/giftlists/{list_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='list_id', required=False, location='query', description=u"ID da Lista", schema={"type":"integer"}),
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Código de referência", schema={"type":"string"}),
            coreapi.Field(name='type_list', required=False, location='query', description=u"Tipo de lista"),
                    ],
        description='Retorna uma lista por `ID`',
        summary='',
        operationId='Detalhes de uma Lista',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    gift_list_schema[0]: gift_list_schema[1],
                    "example": {
                        "id": 24,
                        "reference_code": "",
                        "url": "/lista/presente/isabella-magalhaes-e-murillo-augusto-moreira-bonamini/24/",
                        "type_list": 4,
                        "customer": 72,
                        "date": "2018-12-29",
                        "state": None,
                        "city": None,
                        "guests": None,
                        "message": None,
                        "collection": None,
                        "notification": True,
                        "publish": True,
                        "status": "A",
                        "ceremony_zipcode": "",
                        "ceremony_address": "",
                        "ceremony_number": "",
                        "ceremony_neighborhood": "",
                        "ceremony_complement": "",
                        "ceremony_city": "",
                        "ceremony_state": None,
                        "reception_zipcode": "",
                        "reception_address": "",
                        "reception_number": "",
                        "reception_neighborhood": "",
                        "reception_complement": "",
                        "reception_city": "",
                        "reception_state": None,
                        "name": "Isabella Magalhães",
                        "email": "isahiroshima1999@gmail.com",
                        "mother_name": "Andreia Magalhães",
                        "father_name": "Sidney Cortiglio",
                        "partner_name": "Murillo Augusto Moreira Bonamini",
                        "partner_email": "",
                        "partner_mother_name": "Andrea Bonamini",
                        "partner_father_name": "Gilberto Bonamini",
                        "shipping_zipcode": "37580-000",
                        "shipping_address": "Rua Bahia",
                        "shipping_number": "261",
                        "shipping_neighborhood": "Magioli",
                        "shipping_complement": "Loja",
                        "shipping_city": "MONTE SIÃO",
                        "shipping_state": "MG",
                        "shipping_date": None,
                        "shipping_description": None,
                        "add_date": "2018-07-02T17:05:26.448387",
                        "change_date": "2018-07-02T17:21:02.975380",
                        "user": None,
                        "giftcard": None,
                        "gift_items": []
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
    "ListaPresenteCreate": modules.ConvertizeLink(
        tags=["Presentes"],
        url='/{environment}/api/v2/giftlists/',
        action='post',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
        ],
        description='Criar uma Lista de Presentes',
        summary='',
        operationId='Criar uma Lista de Presentes',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "referece_code"],
                    gift_list_schema[0]: gift_list_schema[1],
                    "example": {
                        "reference_code": "",
                        "type_list": 4,
                        "customer": 72,
                        "date": "2018-12-29",
                        "state": None,
                        "city": None,
                        "guests": None,
                        "message": None,
                        "collection": None,
                        "notification": True,
                        "publish": True,
                        "status": "A",
                        "ceremony_zipcode": "",
                        "ceremony_address": "",
                        "ceremony_number": "",
                        "ceremony_neighborhood": "",
                        "ceremony_complement": "",
                        "ceremony_city": "",
                        "ceremony_state": None,
                        "reception_zipcode": "",
                        "reception_address": "",
                        "reception_number": "",
                        "reception_neighborhood": "",
                        "reception_complement": "",
                        "reception_city": "",
                        "reception_state": None,
                        "name": "Isabella Magalhães",
                        "email": "isahiroshima1999@gmail.com",
                        "mother_name": "Andreia Magalhães",
                        "father_name": "Sidney Cortiglio",
                        "partner_name": "Murillo Augusto Moreira Bonamini",
                        "partner_email": "",
                        "partner_mother_name": "Andrea Bonamini",
                        "partner_father_name": "Gilberto Bonamini",
                        "shipping_zipcode": "37580-000",
                        "shipping_address": "Rua Bahia",
                        "shipping_number": "261",
                        "shipping_neighborhood": "Magioli",
                        "shipping_complement": "Loja",
                        "shipping_city": "MONTE SIÃO",
                        "shipping_state": "MG",
                        "shipping_date": None,
                        "shipping_description": None,
                        "user": None
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
                    gift_list_schema[0]: gift_list_schema[1],
                    "example": {
                        "id": 24,
                        "reference_code": "",
                        "url": "/lista/presente/isabella-magalhaes-e-murillo-augusto-moreira-bonamini/24/",
                        "type_list": 4,
                        "customer": 72,
                        "date": "2018-12-29",
                        "state": None,
                        "city": None,
                        "guests": None,
                        "message": None,
                        "collection": None,
                        "notification": True,
                        "publish": True,
                        "status": "A",
                        "ceremony_zipcode": "",
                        "ceremony_address": "",
                        "ceremony_number": "",
                        "ceremony_neighborhood": "",
                        "ceremony_complement": "",
                        "ceremony_city": "",
                        "ceremony_state": None,
                        "reception_zipcode": "",
                        "reception_address": "",
                        "reception_number": "",
                        "reception_neighborhood": "",
                        "reception_complement": "",
                        "reception_city": "",
                        "reception_state": None,
                        "name": "Isabella Magalhães",
                        "email": "isahiroshima1999@gmail.com",
                        "mother_name": "Andreia Magalhães",
                        "father_name": "Sidney Cortiglio",
                        "partner_name": "Murillo Augusto Moreira Bonamini",
                        "partner_email": "",
                        "partner_mother_name": "Andrea Bonamini",
                        "partner_father_name": "Gilberto Bonamini",
                        "shipping_zipcode": "37580-000",
                        "shipping_address": "Rua Bahia",
                        "shipping_number": "261",
                        "shipping_neighborhood": "Magioli",
                        "shipping_complement": "Loja",
                        "shipping_city": "MONTE SIÃO",
                        "shipping_state": "MG",
                        "shipping_date": None,
                        "shipping_description": None,
                        "add_date": "2018-07-02T17:05:26.448387",
                        "change_date": "2018-07-02T17:21:02.975380",
                        "user": None,
                        "giftcard": None,
                        "gift_items": []
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
    "ListaPresenteUpdate": modules.ConvertizeLink(
        tags=["Presentes"],
        url='/{environment}/api/v2/giftlists/{categorie_id}/',
        action='put',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='list_id', required=True, location='path', description=u"ID da categoria", schema={"type": "integer"}),
        ],
        description='Alterar uma Categoria',
        summary='',
        operationId='Alterar uma Categoria',
        requestBody={
            "content": {
                "application/json": {
                    "required": ["id", "referece_code"],
                    gift_list_schema[0]: gift_list_schema[1],
                    "example": {
                        "reference_code": "1234",
                        "type_list": 4,
                        "customer": 72,
                        "date": "2018-12-29",
                        "state": None,
                        "city": None,
                        "guests": None,
                        "message": None,
                        "collection": None,
                        "notification": True,
                        "publish": True,
                        "status": "A",
                        "ceremony_zipcode": "",
                        "ceremony_address": "",
                        "ceremony_number": "",
                        "ceremony_neighborhood": "",
                        "ceremony_complement": "",
                        "ceremony_city": "",
                        "ceremony_state": None,
                        "reception_zipcode": "",
                        "reception_address": "",
                        "reception_number": "",
                        "reception_neighborhood": "",
                        "reception_complement": "",
                        "reception_city": "",
                        "reception_state": None,
                        "name": "Isabella Magalhães",
                        "email": "isahiroshima1999@gmail.com",
                        "mother_name": "Andreia Magalhães",
                        "father_name": "Sidney Cortiglio",
                        "partner_name": "Murillo Augusto Moreira Bonamini",
                        "partner_email": "",
                        "partner_mother_name": "Andrea Bonamini",
                        "partner_father_name": "Gilberto Bonamini",
                        "shipping_zipcode": "37580-000",
                        "shipping_address": "Rua Bahia",
                        "shipping_number": "261",
                        "shipping_neighborhood": "Magioli",
                        "shipping_complement": "Loja",
                        "shipping_city": "MONTE SIÃO",
                        "shipping_state": "MG",
                        "shipping_date": None,
                        "shipping_description": None,
                        "user": None
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
                    "required": ["id", "referece_code"],
                    gift_list_schema[0]: gift_list_schema[1],
                    "example": {
                        "id": 24,
                        "reference_code": "1234",
                        "url": "/lista/presente/isabella-magalhaes-e-murillo-augusto-moreira-bonamini/24/",
                        "type_list": 4,
                        "customer": 72,
                        "date": "2018-12-29",
                        "state": None,
                        "city": None,
                        "guests": None,
                        "message": None,
                        "collection": None,
                        "notification": True,
                        "publish": True,
                        "status": "A",
                        "ceremony_zipcode": "",
                        "ceremony_address": "",
                        "ceremony_number": "",
                        "ceremony_neighborhood": "",
                        "ceremony_complement": "",
                        "ceremony_city": "",
                        "ceremony_state": None,
                        "reception_zipcode": "",
                        "reception_address": "",
                        "reception_number": "",
                        "reception_neighborhood": "",
                        "reception_complement": "",
                        "reception_city": "",
                        "reception_state": None,
                        "name": "Isabella Magalhães",
                        "email": "isahiroshima1999@gmail.com",
                        "mother_name": "Andreia Magalhães",
                        "father_name": "Sidney Cortiglio",
                        "partner_name": "Murillo Augusto Moreira Bonamini",
                        "partner_email": "",
                        "partner_mother_name": "Andrea Bonamini",
                        "partner_father_name": "Gilberto Bonamini",
                        "shipping_zipcode": "37580-000",
                        "shipping_address": "Rua Bahia",
                        "shipping_number": "261",
                        "shipping_neighborhood": "Magioli",
                        "shipping_complement": "Loja",
                        "shipping_city": "MONTE SIÃO",
                        "shipping_state": "MG",
                        "shipping_date": None,
                        "shipping_description": None,
                        "add_date": "2018-07-02T17:05:26.448387",
                        "change_date": "2018-07-02T17:21:02.975380",
                        "user": None,
                        "giftcard": None,
                        "gift_items": []
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
    "ListaPresenteDelete": modules.ConvertizeLink(
        tags=["Presentes"],
        url='/{environment}/api/v2/giftlists/{list_id}/',
        action='delete',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambiente do cliente", schema={"type": "string"}),
            coreapi.Field(name='list_id', required=True, location='path', description=u"ID da lista", schema={"type": "integer"}),
        ],
        description='Deletar uma Lista de Presentes',
        summary='',
        operationId='Deletar uma Lista de Presentes',
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


