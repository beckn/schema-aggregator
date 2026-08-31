# TripResult — v2.0

The result of a trip planning request, containing one or more journey options with leg details and timing.

## Files

| File | Purpose |
|---|---|
| [https://schema.nfh.global/TripResult/attributes.yaml](https://schema.nfh.global/TripResult/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.nfh.global/TripResult/v2.0/attributes.yaml](https://schema.nfh.global/TripResult/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.nfh.global/TripResult/attributes.jsonschema.yaml](https://schema.nfh.global/TripResult/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.nfh.global/TripResult/v2.0/attributes.jsonschema.yaml](https://schema.nfh.global/TripResult/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.nfh.global/TripResult/context.jsonld](https://schema.nfh.global/TripResult/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.nfh.global/TripResult/v2.0/context.jsonld](https://schema.nfh.global/TripResult/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.nfh.global/TripResult/vocab.jsonld](https://schema.nfh.global/TripResult/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.nfh.global/TripResult/v2.0/vocab.jsonld](https://schema.nfh.global/TripResult/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `itineraries` | no | $ref: https://schema.nfh.global/Itinerary/v2.0/attributes.yaml#/components/schemas/Itinerary | List of itinerary options in the result |
| `requestRef` | no | $ref: https://schema.nfh.global/TripRequest/v2.0/attributes.yaml#/components/schemas/TripRequest | Reference to the originating trip request |
| `id` | no | string | Unique identifier for the catalog |
| `descriptor` | no | $ref: https://schema.nfh.global/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the catalog |
| `tags` | no | string | Tags associated with the catalog |
