from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, Table

from crenata.database.registry import mapper_registry

preferences_table = Table(
    "preferences",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "user_id", BigInteger, ForeignKey("user.id", ondelete="CASCADE"), unique=True
    ),
    Column("private", Boolean),
    Column("ephemeral", Boolean),
)
