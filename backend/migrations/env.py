from app.db.database import Base
import os
import sys
import logging
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from geoalchemy2 import alembic_helpers

# Add app folder to path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# Import your Base for metadata

target_metadata = Base.metadata

# Alembic config
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

# -------------------
# Database URLs
# -------------------
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set")
SYNC_DATABASE_URL = DATABASE_URL.replace(
    "postgresql+asyncpg://", "postgresql+psycopg2://")

config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

# -------------------
# Include / ignore objects
# -------------------

POSTGIS_TABLE_PREFIXES = (
    "spatial_ref_sys",
    "tiger_",
    "direction_",
    "zip_",
    "county",
    "countysub",
    "state_",
    "state",
    "street_",
    "place_",
    "geom_",
    "tgr_",
    "tabblock",
    "secondary_unit_lookup",
)

GEOCODER_TABLES = {
    "addr",
    "addrfeat",
    "bg",
    "cousub",
    "edges",
    "faces",
    "featnames",
    "layer",
    "place",
    "tract",
    "zcta5",
    "topology",
    "pagc_gaz",
    "pagc_lex",
    "pagc_rules",
    "loader_platform",
    "loader_variables",
    "loader_lookuptables",
    "geocode_settings",
    "geocode_settings_default",
    "secondary_unit_lookup",
}

IGNORED_INDEXES = {
    "secondary_unit_lookup_abbrev_idx",
}


def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table":
        # Ignore PostGIS / TIGER / geocoder tables
        if name.startswith(POSTGIS_TABLE_PREFIXES) or name in GEOCODER_TABLES:
            return False

    elif type_ == "index":
        if name in IGNORED_INDEXES:
            return False

    return True


# -------------------
# Migration functions
# -------------------

def run_migrations_offline():
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        include_object=include_object,
    )
    with context.begin_transaction():
        context.run_migrations()

# -------------------------------------------------
# Online migrations
# -------------------------------------------------


def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": SYNC_DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            render_item=alembic_helpers.render_item,
        )

        with context.begin_transaction():
            context.run_migrations()


# -------------------------------------------------
# Run
# -------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
