import streamlit
from streamlit import _RerunData, _RerunException
from streamlit.source_util import get_pages

def switch_page(page_name: str): #Fonte da função: https://discuss.streamlit.io/t/navigate-multipage-app-with-buttons-instead-of-sidebar/27986/6

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)
    pages = get_pages("home.py")

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")