from ninja import Field, Schema

class SiteSchema(Schema):
    id: int
    hostname: str
    port: int
    site_name: str
    root_page_id: int
    is_default_site: bool

class SiteInputSchema(Schema):
    hostname: str
    port: int = ...
    site_name: str = ...
    root_page: int = Field(alias="root_page_id")  # noqa: PYI015
    is_default_site: bool = ...
