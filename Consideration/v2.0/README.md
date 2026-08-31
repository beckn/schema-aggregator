# Consideration — v2.0

Generalized representation of value exchanged under a Contract.

Consideration is domain-neutral and may represent:
- Monetary value
- Credits / tokens
- Asset transfer
- Service exchange
- Compliance artifact

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/Consideration/attributes.yaml](https://schema.nfh.global/Consideration/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/Consideration/v2.0/attributes.yaml](https://schema.nfh.global/Consideration/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/Consideration/attributes.jsonschema.yaml](https://schema.nfh.global/Consideration/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/Consideration/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/Consideration/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/Consideration/context.jsonld](https://schema.nfh.global/Consideration/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/Consideration/v2.0/context.jsonld](https://schema.nfh.global/Consideration/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/Consideration/vocab.jsonld](https://schema.nfh.global/Consideration/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/Consideration/v2.0/vocab.jsonld](https://schema.nfh.global/Consideration/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Identifier of this consideration |
| `status` | yes | $ref: https://schema.nfh.global/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | The status of this consideration |
| `considerationAttributes` | no | $ref: https://schema.nfh.global/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Domain-specific attributes of this consideration. For monetary considerations, use the PriceSpecification schema to capture total value with breakup. For other consideration types, use a generic Attributes bag. |
