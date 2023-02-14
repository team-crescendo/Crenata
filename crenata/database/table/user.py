from sqlalchemy import BigInteger, Column, Table

from crenata.database.registry import mapper_registry

user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", BigInteger, primary_key=True),
)
