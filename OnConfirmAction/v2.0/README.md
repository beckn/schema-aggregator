# OnConfirmAction — v2.0

Beckn /beckn/on_confirm message payload. Sent by a BPP to a BAP in
response to a /beckn/confirm call, returning the confirmed contract
with status set to CONFIRMED.
(Context wrapper stripped; only the message-content portion is inlined.)

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/OnConfirmAction/attributes.yaml](https://schema.nfh.global/OnConfirmAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/OnConfirmAction/v2.0/attributes.yaml](https://schema.nfh.global/OnConfirmAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/OnConfirmAction/attributes.jsonschema.yaml](https://schema.nfh.global/OnConfirmAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/OnConfirmAction/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/OnConfirmAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/OnConfirmAction/context.jsonld](https://schema.nfh.global/OnConfirmAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/OnConfirmAction/v2.0/context.jsonld](https://schema.nfh.global/OnConfirmAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/OnConfirmAction/vocab.jsonld](https://schema.nfh.global/OnConfirmAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/OnConfirmAction/v2.0/vocab.jsonld](https://schema.nfh.global/OnConfirmAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `contract` | yes | $ref: https://schema.nfh.global/Contract/v2.0/attributes.yaml#/components/schemas/Contract | - |
