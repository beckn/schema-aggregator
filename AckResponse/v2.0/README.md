# AckResponse — v2.0

Schema definition for AckResponse in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/AckResponse/attributes.yaml](https://schema.nfh.global/AckResponse/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/AckResponse/v2.0/attributes.yaml](https://schema.nfh.global/AckResponse/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/AckResponse/attributes.jsonschema.yaml](https://schema.nfh.global/AckResponse/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/AckResponse/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/AckResponse/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/AckResponse/context.jsonld](https://schema.nfh.global/AckResponse/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/AckResponse/v2.0/context.jsonld](https://schema.nfh.global/AckResponse/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/AckResponse/vocab.jsonld](https://schema.nfh.global/AckResponse/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/AckResponse/v2.0/vocab.jsonld](https://schema.nfh.global/AckResponse/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `transaction_id` | yes | string | - |
| `timestamp` | yes | string | - |
| `ack_status` | yes | string | - |
| `error` | no | $ref: https://schema.nfh.global/Error/v2.0/attributes.yaml#/components/schemas/Error | - |
