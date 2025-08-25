from os import getenv

from dotenv import load_dotenv


load_dotenv(override=True)

POSTGRES_URI: str = (
    'postgresql+psycopg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'.format(
        PG_USER=getenv('PG_USER'),
        PG_PASSWORD=getenv('PG_PASSWORD'),
        PG_HOST=getenv('PG_HOST'),
        PG_NAME=getenv('PG_NAME'),
        PG_PORT=getenv('PG_PORT')
    )
)
