# LogisticsRating — v2.0

A numeric score given by a user for a logistics service, driver, or carrier.

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/LogisticsRating/attributes.yaml](https://schema.nfh.global/LogisticsRating/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/LogisticsRating/v2.0/attributes.yaml](https://schema.nfh.global/LogisticsRating/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/LogisticsRating/attributes.jsonschema.yaml](https://schema.nfh.global/LogisticsRating/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/LogisticsRating/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/LogisticsRating/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/LogisticsRating/context.jsonld](https://schema.nfh.global/LogisticsRating/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/LogisticsRating/v2.0/context.jsonld](https://schema.nfh.global/LogisticsRating/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/LogisticsRating/vocab.jsonld](https://schema.nfh.global/LogisticsRating/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/LogisticsRating/v2.0/vocab.jsonld](https://schema.nfh.global/LogisticsRating/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | - |
| `value` | yes | number | - |
| `ratingFor` | yes | string | - |
| `ratedBy` | no | string | User ID who gave the rating |
| `shipmentId` | no | string | - |
| `categories` | no | object | Category-wise ratings |
| `timestamp` | no | string | - |
