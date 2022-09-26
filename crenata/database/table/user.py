from sqlalchemy import BigInteger, Column, String, Table

from crenata.database.registry import mapper_registry

user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", BigInteger, primary_key=True),
    Column("school_name", String),
    Column("ATPT_OFCDC_SC_CODE", String),
    Column("SD_SCHUL_CODE", String),
)
