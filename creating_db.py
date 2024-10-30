from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

username = "despesas_pessoais_db_user"
password = "J7CaAZQ0uv8qGMfya1K5oBvvjF78ZzUp"
host = "dpg-csfp8v2j1k6c73b1uek0-a.oregon-postgres.render.com"
port = "5432"
database = "despesas_pessoais_db"

connection_string = "postgresql://{}:{}@{}/{}".format(username, password, host, database)

engine = create_engine(connection_string)

session_make = sessionmaker(bind=engine)

Base = declarative_base()

session = session_make()

session.execute(text("DROP TABLE IF EXISTS forma_pagamento CASCADE"))
session.execute(text("DROP TABLE IF EXISTS categoria_despesa CASCADE"))
session.execute(text("DROP TABLE IF EXISTS categoria_receita CASCADE"))
session.execute(text("DROP TABLE IF EXISTS despesa CASCADE"))
session.execute(text("DROP TABLE IF EXISTS receita CASCADE"))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS forma_pagamento (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS categoria_despesa (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS categoria_receita (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS despesa (
        id SERIAL PRIMARY KEY,
        categoria VARCHAR(100) NOT NULL REFERENCES categoria_receita(name),
        name VARCHAR(100) NOT NULL,
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        forma_pagamento_id INTEGER NOT NULL REFERENCES forma_pagamento(id),
        valor FLOAT NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE receita (
        id SERIAL PRIMARY KEY,
        categoria VARCHAR(100) NOT NULL REFERENCES categoria_receita(name),
        name VARCHAR(100) NOT NULL,
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        forma_pagamento_id INTEGER NOT NULL REFERENCES forma_pagamento(id),
        valor FLOAT NOT NULL
    );
'''))

session.commit()

session.close()