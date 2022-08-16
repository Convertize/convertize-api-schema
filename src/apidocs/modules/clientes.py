# coding: utf-8
import coreapi
from apidocs import modules

customer_componente = dict([
    modules.new_propertie(name="id", type="integer", nullable=False, format="int64", description=u"ID do Cliente"),
    modules.new_propertie(name="email", type="string", nullable=False, description=u"E-mail do Cliente"),
    modules.new_propertie(name="reference_code", type="string", nullable=True, description=u"E-mail do Cliente"),
    modules.new_propertie(name="name", type="string", nullable=True, description=u"Nome do Cliente"),
    modules.new_propertie(name="corporate_name", type="string", nullable=True, description=u"Razão Social"),
    modules.new_propertie(name="document", type="string", nullable=True, description=u"CPF/CNPJ"),
    modules.new_propertie(name="corporate_document", type="string", nullable=True, description=u""),
    modules.new_propertie(name="inscricao_estadual_isento", type="boolean", nullable=True, description=u"Inscrição Estadual Isento"),
    modules.new_propertie(name="inscricao_estadual", type="string", nullable=True, description=u"Inscrição Estadual"),
    modules.new_propertie(name="fancy_name", type="string", nullable=True, description=u"Nome Fantasia"),
    modules.new_propertie(name="birthdate", type="string", nullable=True, description=u"Data de Nascimento"),
    modules.new_propertie(name="gender", type="string", nullable=True, description=u"Gênero"),
    modules.new_propertie(name="blocked", type="boolean", description=u"Indica se esta bloqueado `default = false`"),
    modules.new_propertie(name="newsletter", type="integer", format="int4", description=u"Indica se o cliente quer receber `newsletter (1 = SIM, 2 = NÃO, 0 = NÃO)`"),
    modules.new_propertie(name='gdpr_agreement', type="string",description=u"Acordo GDPR"),
    modules.new_propertie(name='receiver', type="string", nullable=False,description=u"Destinatário"),
    modules.new_propertie(name="zipcode", type="string", description=u"CEP"),
    modules.new_propertie(name="address", type="string", description=u"Endereço"),
    modules.new_propertie(name="number", type="integer", description=u"Número"),
    modules.new_propertie(name="neighborhood", type="string", description=u"Bairro"),
    modules.new_propertie(name="complement", type="string", description=u"Complemento"),
    modules.new_propertie(name="city", type="string", description=u"Cidade"),
    modules.new_propertie(name="state", type="string", description=u"Estado"),
    modules.new_propertie(name="phone1", type="string", description=u"Telefone residencial"),
    modules.new_propertie(name="phone2", type="string", description=u"Telefone celular"),
    modules.new_propertie(name="reference", type="string", description=u"Ponto de Referencia"),
    modules.new_propertie(name="city_id", type="integer", description=u"ID da cidade"),
    modules.new_propertie(name="code_ibge", type="string", description=u"Código do IBGE da cidade"),
    modules.new_propertie(name="add_date", type="string", description=u"Data de criação"),
    modules.new_propertie(name="change_date", type="string", description=u"Data de alteração"),
    modules.new_propertie(name="limit_credit", type="float", description=u"Limite de Crédito"),
    modules.new_propertie(name="balance_of_credit", type="float", description=u"Saldo de Crédito"),
    modules.new_propertie(name='group', type="integer",description=u"Grupo"),
])

customers_schema = modules.new_propertie(name="schema", type="object", properties=dict((
        modules.new_propertie(name="next", type="string", nullable=True, description=u"URL com os proximos registro, quando `null`, chegou na ultima pagina."),
        modules.new_propertie(name="previous", type="string", nullable=True, description=u"URL com os registro anteriores, quando `null`, chegou na primeira pagina."),
        modules.new_propertie(name="count", type="integer", nullable=False, description=u"Quantidade total de paginas"),
        modules.new_propertie(name="results", type="array", items=dict((
            modules.new_propertie(name="required", enum=["id", "email"]),
            modules.new_propertie(name="properties", enum=customer_componente)
        )))
    )))

customer_schema = modules.new_propertie(name="schema", type="object", properties=customer_componente)

export = {
    "Clientes": modules.ConvertizeLink(
        tags=["Clientes"],
        url='/{environment}/api/v2/customers/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='id', required=False, location='query', description=u"Filtro por id do cliente", schema={"type": "string"}),
            coreapi.Field(name='group', required=False, location='query', description=u"Filtro por grupo", schema={"type": "string"}),
            coreapi.Field(name='blocked', required=False, location='query', description=u"Filtro por conta bloqueada", schema={"type": "boolean"}),
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Filtro pelo Código de referência no ERP", schema={"type": "string"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma lista de clientes',
        summary='',
        operationId='Lista de Categorias',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    customers_schema[0]: customers_schema[1],
                    "example": {
                      "count": 40607,
                      "next": "https://api.convertize.com.br/{environment}/api/1.0/customers/?page=2",
                      "previous": None,
                      "results": [
                        {
                            "id": 138468,
                            "reference_code": None,
                            "email": "contato@convertize.com.br",
                            "document":None,
                            "corporate_document":None,
                            "name": "Convertize E-Commerce",
                            "corporate_name":None,
                            "inscricao_estadual_isento":False,
                            "inscricao_estadual":None,
                            "fancy_name":None,
                            "birthdate":None,
                            "gender":None,
                            "blocked": False,
                            "newsletter": 1,
                            "gdpr_agreement":True,
                            "receiver":"Convertize E-Commerce",
                            "zipcode": None,
                            "address": None,
                            "number": None,
                            "neighborhood": None,
                            "complement": None,
                            "city": None,
                            "state": None,
                            "phone1": None,
                            "phone2": None,
                            "reference": None,
                            "city_id": None,
                            "code_ibge": None,
                            "add_date": "2017-08-18T14:04:04.826000",
                            "change_date": "2017-08-18T14:04:04.826020",
                            "limit_credit": None,
                            "balance_of_credit": None,
                            "group":None
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
    "Customer": modules.ConvertizeLink(
        tags=["Clientes"],
        url='/{environment}/api/v2/customers/{customer_id}/',
        action='get',
        fields=[
            coreapi.Field(name='environment', required=True, location='path', description=u"Ambinete do cliente", schema={"type": "string"}),
            coreapi.Field(name='customer_id', required=True, location='path', description=u"ID do cliente", schema={"type": "integer"}),
            coreapi.Field(name='reference_code', required=False, location='query', description=u"Filtro pelo Código de referência no ERP", schema={"type": "string"}),
            coreapi.Field(name='newsletter', required=False, location='query', description=u"Filtro pelo campo newsletter", schema={"type": "integer"}),
            coreapi.Field(name='add_date__lte', required=False, location='query', description=u"Filtro por data de criação menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='add_date__gte', required=False, location='query', description=u"Filtro por data de criação maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__lte', required=False, location='query', description=u"Filtro por data de alteração menor ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
            coreapi.Field(name='change_date__gte', required=False, location='query', description=u"Filtro por data de alteração maior ou igual. formato: `YYYY-mm-DDT:H:M:S`", schema={"type": "integer"}),
        ],
        description='Retorna uma um cliente por `ID`',
        summary='',
        operationId='Detalhes de uma categorias',
        template={
            "200": {
            "description": "Success",
            "content": {
                "application/json": {
                    customer_schema[0]: customer_schema[1],
                    "example": {
                        "id": 138468,
                        "reference_code": None,
                        "email": "contato@convertize.com.br",
                        "document":None,
                        "corporate_document":None,
                        "name": "Convertize E-Commerce",
                        "corporate_name":None,
                        "inscricao_estadual_isento":False,
                        "inscricao_estadual":None,
                        "fancy_name":None,
                        "birthdate":None,
                        "gender":None,
                        "blocked": False,
                        "newsletter": 1,
                        "gdpr_agreement":True,
                        "receiver":"Convertize E-Commerce",
                        "zipcode": None,
                        "address": None,
                        "number": None,
                        "neighborhood": None,
                        "complement": None,
                        "city": None,
                        "state": None,
                        "phone1": None,
                        "phone2": None,
                        "reference": None,
                        "city_id": None,
                        "code_ibge": None,
                        "add_date": "2017-08-18T14:04:04.826000",
                        "change_date": "2017-08-18T14:04:04.826020",
                        "limit_credit": None,
                        "balance_of_credit": None,
                        "group":None
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
    )
}
