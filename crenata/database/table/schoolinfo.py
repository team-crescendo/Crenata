from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Table

from crenata.database.registry import mapper_registry

schoolinfo_table = Table(
    "school_info",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id", BigInteger, ForeignKey("user.id", ondelete="CASCADE"), unique=True
    ),
    Column("school_name", String),
    Column("grade", Integer),
    Column("room", Integer),
    Column("ATPT_OFCDC_SC_CODE", String),
    Column("SD_SCHUL_CODE", String),
)
