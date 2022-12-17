from sqlalchemy import Table
from sqlalchemy.orm import registry

from crenata.abc.domain import AbstractDomain


class OverridableRegistry(registry):
    def override(self, domain: type[AbstractDomain], table: Table):
        self.map_declaratively(domain.__base__)
        self.map_imperatively(domain, table)


mapper_registry = OverridableRegistry()
