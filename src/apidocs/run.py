# -*- coding: utf-8 -*-
import click
import json
import coreapi

from coreapi_swagger_openapi.codecs import OpenAPICodec, DocumentToSwaggerConverter
from coreapi.compat import force_bytes

from apidocs.schemas import schema


@click.group()
def generate():
    "Convertize API Docs."


@generate.command()
@click.pass_context
def start(ctx):
    codec = OpenAPICodec()

    click.echo(json.dumps(json.loads(codec.dump(schema)), indent=4, sort_keys=True))
