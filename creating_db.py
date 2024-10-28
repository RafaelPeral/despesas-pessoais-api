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

session.execute(text("DROP TABLE IF EXISTS formas_pagamento CASCADE"))
session.execute(text("DROP TABLE IF EXISTS categorias_despesas CASCADE"))
session.execute(text("DROP TABLE IF EXISTS categorias_receitas CASCADE"))
session.execute(text("DROP TABLE IF EXISTS despesas CASCADE"))
session.execute(text("DROP TABLE IF EXISTS receitas CASCADE"))


session.execute(text('''
    CREATE TABLE IF NOT EXISTS formas_pagamento (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS categorias_despesas (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS categorias_receitas (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) UNIQUE NOT NULL
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS despesas (
        id SERIAL PRIMARY KEY,
        categoria VARCHAR(100) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        forma_pagamento VARCHAR(100) NOT NULL,
        valor FLOAT NOT NULL,
        FOREIGN KEY (forma_pagamento) REFERENCES formas_pagamento (nome),
        FOREIGN KEY (categoria) REFERENCES categorias_despesas (nome)
    )
'''))

session.execute(text('''
    CREATE TABLE IF NOT EXISTS receitas (
        id SERIAL PRIMARY KEY,
        categoria VARCHAR(100) NOT NULL,
        nome VARCHAR(100) NOT NULL,
        data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        forma_pagamento VARCHAR(100) NOT NULL,
        valor FLOAT NOT NULL,
        FOREIGN KEY (forma_pagamento) REFERENCES formas_pagamento (nome),
        FOREIGN KEY (categoria) REFERENCES categorias_receitas (nome)
    )
'''))

session.commit()

session.close()