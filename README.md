# HammarSKOS
A SKOS API and web application providing access to controlled vocabularies such as thesauri that can be expressed in SKOS.

This application contains a REST API for working with vocabularies and Linked Data. The API is written with and largely auto-documented via Python's FastAPI library.

It also contains a modern components-based frontend leveraging Vue 3 and NuxtJS.

The API is designed to leverage a SPARQL endpoint, usually located on the same host or accessible within the same network, to translate output to JSON-LD, etc., and is largely based on the API provided by Skosmos. So that means you need a SPARQL endpoint running somewhere the app can access.