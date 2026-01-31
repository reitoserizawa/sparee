from app.models import BaseModel
from app import create_app
import os
import sys
import logging
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from geoalchemy2 import alembic_helpers

# -------------------------------------------------
# Fix PYTHONPATH so `import app` works
# -------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# -------------------------------------------------
# Create Flask app + context
# -------------------------------------------------

flask_app = create_app()
app_ctx = flask_app.app_context()

# -------------------------------------------------
# Alembic config
# -------------------------------------------------
config = context.config

if config.config_file_name:
    fileConfig(config.config_file_name)

logger = logging.getLogger("alembic.env")

target_metadata = BaseModel.metadata

# -------------------------------------------------
# Sync DB URL (Alembic MUST be sync)
# -------------------------------------------------


def process_revision_directives(context, revision, directives):
    if getattr(config.cmd_opts, "autogenerate", False):
        script = directives[0]
        if script.upgrade_ops.is_empty():
            directives[:] = []
            logger.info("No schema changes detected.")


def get_sync_url():
    url = flask_app.config["SQLALCHEMY_DATABASE_URI"]
    return url.replace(
        "postgresql+asyncpg://",
        "postgresql+psycopg2://",
    )


config.set_main_option("sqlalchemy.url", get_sync_url())

# -------------------------------------------------
# Offline migrations
# -------------------------------------------------

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


def run_migrations_offline():
    context.configure(
        url=get_sync_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

# -------------------------------------------------
# Online migrations
# -------------------------------------------------


def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": get_sync_url()},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            render_item=alembic_helpers.render_item,
            process_revision_directives=process_revision_directives,
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
