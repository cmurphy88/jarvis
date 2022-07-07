from __future__ import with_statement

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

from api import config as config_env
from api.db import Base
from api.users.models import User
from api.home.models import Home
from api.room.models import Room
from api.routine.models import Routine
from api.camera.models import Camera
from api.media.models import Media
from api.trv.models import Trv
from api.media_room.models import MediaRoom
from api.trv_room.models import TrvRoom
from api.light_room.models import LightRoom
from api.light.models import Light
from api.media_routine_setting.models import MediaRoutineSetting
from api.trv_routine_setting.models import TrvRoutineSetting
from api.light_routine_setting.models import LightRoutineSetting

target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    db_user = config_env.DATABASE_USERNAME
    db_password = config_env.DATABASE_PASSWORD
    db_host = config_env.DATABASE_HOST
    db_name = config_env.DATABASE_NAME
    return f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()