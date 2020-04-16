from google.cloud import bigquery
from google.oauth2 import service_account


def match_existing_schema_and_append_description(table: bigquery.table.TableReference,
                                                 schema_description: dict) -> list:
    """
    기존 Table에 있는 스키마 정보를 읽은 후, 적용할 schema_description를 추가한 BigQuery SchemaField 생성

    :param table: BigQuery Table Reference Object
    :param schema_description: 업데이트할 스키마의 Description
    :return: description을 포함한 bigquery SchemaField
    """
    table_schema = table.schema
    assert len(table_schema) == len(schema_description)
    new_schema_field_list = []

    for existing_schema in table_schema:
        for description_dict in schema_description:
            if existing_schema.name == description_dict['name']:
                schema_field = bigquery.SchemaField(name=existing_schema.name,
                                                    field_type=existing_schema.field_type,
                                                    mode=existing_schema.mode,
                                                    description=description_dict['description'])
                new_schema_field_list.append(schema_field)
    return new_schema_field_list


def update_schema_description(table_fullname: str, schema_description: dict) -> None:
    """
    정의한 schema description을 BigQuery Table에 적용

    :param table_fullname: BigQuery Table Fullname.
    :param schema_description: 업데이트할 스키마의 Description
    :return: None
    """
    credentials = service_account.Credentials.from_service_account_file('****.json')
    client = bigquery.Client(project='', credentials=credentials)
    table_ref = bigquery.table.TableReference.from_string(table_fullname)
    table = client.get_table(table_ref)

    new_schema = match_existing_schema_and_append_description(table, schema_description)

    table.schema = new_schema
    table = client.update_table(table, ['schema'])
