from typing import Optional, Tuple
from jinja2.exceptions import TemplateNotFound

def reset_template_info_cache() -> None: ...
def find_template(template_name: str) -> Optional[str]: ...
def template_type(template_path: str) -> str: ...

def template_info(template_name: str) -> Tuple[str, str]: ...
