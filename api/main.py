import os, json
from functools import lru_cache
from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends
from api.config import Settings

@lru_cache
def get_settings():
    return Settings()

app = FastAPI(
    title=get_settings().app_title,
    description=get_settings().description
)

def load_vocabulary(vocabulary):
    vocabularies = get_settings().vocabularies
    found_vocabularies = list(filter(lambda v: v == vocabulary, vocabularies))
    if len(found_vocabularies) > 0:
        return found_vocabularies[0]
    else:
        raise HTTPException(status_code=404, detail=f'The requested vocabulary, {vocabulary}, was not found.')

@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.get("/vocabularies")
async def get_vocabularies(settings: Annotated[Settings, Depends(get_settings)]):
    vocabularies = settings.vocabularies
    return_vocabularies = []
    for v in vocabularies:
        try:
            print(f'Loading {v}.json')
            f = open(f'vocabularies/{v}.json')
            found_v = json.load(f)
            found_v["local_path"] = f'{settings.app_base_url }/{v}'
            return_vocabularies.append(found_v)
            f.close()
        except:
            raise
    return return_vocabularies

@app.get("/search")
def get_search():
    return {}

@app.get("/label")
def get_label():
    return {}

@app.get("/data")
def get_data():
    return {}

@app.get("/types")
def get_types():
    # Types/classes in all vocabularies?
    return []

@app.get("/{vocabulary}")
def get_vocabulary(vocabulary, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/{id}")
def get_concept(vocabulary, id):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/types")
def get_vocabulary_types(vocabulary, lang: str = "en"):
    # types/classes in this vocabulary
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/topConcepts")
def get_top_concepts(vocabulary, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/data")
def get_vocabulary_data(vocabulary, lang: str = "en", uri: str | None = None):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/search")
def search_vocabulary(vocabulary, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/lookup")
def get_concept_by_label(vocabulary, label: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/vocabularyStatistics")
def get_vocabulary_statistics(vocabulary, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/labelStatistics")
def get_label_statistics(vocabulary, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/index")
def get_vocabulary_alpha_index(vocabulary, lang: str = "en"):
    # For alphabetizing concepts...
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/index/{letter}")
def get_vocabulary_alpha_index_by_letter(vocabulary, letter, lang: str = "en"):
    # Should make sure this works with Arabic, Russian, and Chinese
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/label")
def get_concept_label(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/broader")
def get_broader(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/broaderTransitive")
def get_broader_transitive(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/narrower")
def get_narrower(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/narrowerTransitive")
def get_narrower_transitive(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/related")
def get_related(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/children")
def get_children(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/groups")
def get_groups(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/new")
def get_new(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/modified")
def get_modified(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/groupMembers")
def get_group_members(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/hierarchy")
def get_hierarchy(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}

@app.get("/{vocabulary}/mappings")
def get_mappings(vocabulary, uri: str, lang: str = "en"):
    this_v = load_vocabulary(vocabulary)
    return {}
