# Rating — v2.0

Schema definition for Rating in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/Rating/attributes.yaml](https://schema.nfh.global/Rating/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/Rating/v2.0/attributes.yaml](https://schema.nfh.global/Rating/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/Rating/attributes.jsonschema.yaml](https://schema.nfh.global/Rating/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/Rating/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/Rating/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/Rating/context.jsonld](https://schema.nfh.global/Rating/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/Rating/v2.0/context.jsonld](https://schema.nfh.global/Rating/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/Rating/vocab.jsonld](https://schema.nfh.global/Rating/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/Rating/v2.0/vocab.jsonld](https://schema.nfh.global/Rating/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@type` | yes | string | Type of the rating |
| `beckn:ratingValue` | no | number | Rating value (0-5) |
| `beckn:ratingCount` | no | integer | Number of ratings |
