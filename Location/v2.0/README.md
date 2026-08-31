# Location — v2.0

A place represented by GeoJSON geometry and optional address.
Source: main/schema/core/v2/attributes.yaml#Location

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/Location/attributes.yaml](https://schema.nfh.global/Location/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/Location/v2.0/attributes.yaml](https://schema.nfh.global/Location/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/Location/attributes.jsonschema.yaml](https://schema.nfh.global/Location/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/Location/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/Location/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/Location/context.jsonld](https://schema.nfh.global/Location/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/Location/v2.0/context.jsonld](https://schema.nfh.global/Location/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/Location/vocab.jsonld](https://schema.nfh.global/Location/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/Location/v2.0/vocab.jsonld](https://schema.nfh.global/Location/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `geo` | yes | $ref: https://schema.nfh.global/GeoJSONGeometry/v2.0/attributes.yaml#/components/schemas/GeoJSONGeometry | - |
| `address` | no | $ref: https://schema.nfh.global/Address/v2.0/attributes.yaml#/components/schemas/Address | - |
