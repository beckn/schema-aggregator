# SelectAction — v2.0

Beckn /beckn/select message payload. Sent by a BAP to a BPP to select
items and offers from a catalog, initiating the negotiation cycle.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/SelectAction/attributes.yaml](https://schema.nfh.global/SelectAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/SelectAction/v2.0/attributes.yaml](https://schema.nfh.global/SelectAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/SelectAction/attributes.jsonschema.yaml](https://schema.nfh.global/SelectAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/SelectAction/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/SelectAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/SelectAction/context.jsonld](https://schema.nfh.global/SelectAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/SelectAction/v2.0/context.jsonld](https://schema.nfh.global/SelectAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/SelectAction/vocab.jsonld](https://schema.nfh.global/SelectAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/SelectAction/v2.0/vocab.jsonld](https://schema.nfh.global/SelectAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.nfh.global/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
