CREATE TABLE dim_pokemon(
  id_pokemon SERIAL PRIMARY KEY,
  nome_pokemon varchar(100) NOT NULL,
  altura decimal(10,2),
  peso decimal(10,2),
  url_imagem varchar(255)
);

CREATE TABLE dim_tipo(
  id_tipo SERIAL PRIMARY KEY,
  nome_tipo varchar(100) UNIQUE NOT NULL
);

CREATE TABLE dim_habilidade(
  id_habilidade SERIAL PRIMARY KEY,
  nome_habilidade varchar(100) UNIQUE NOT NULL
);

CREATE TABLE bridge_pokemon_tipo(
  id_pokemon INTEGER NOT NULL,
  id_tipo INTEGER NOT NULL,
  PRIMARY KEY (id_pokemon, id_tipo),
  CONSTRAINT bridge_poke_pokemon FOREIGN KEY (id_pokemon) REFERENCES dim_pokemon(id_pokemon) ON DELETE CASCADE,
  CONSTRAINT bridge_tipo FOREIGN KEY (id_tipo) REFERENCES dim_tipo(id_tipo)

);

CREATE INDEX idx_pokemon_tipo ON bridge_pokemon_tipo(id_pokemon);
CREATE INDEX idx_tipo ON bridge_pokemon_tipo(id_tipo);

CREATE TABLE bridge_pokemon_habilidade(
  id_pokemon INTEGER NOT NULL,
  id_habilidade INTEGER NOT NULL,
  PRIMARY KEY (id_pokemon, id_habilidade),
  CONSTRAINT bridge_hab_pokemon FOREIGN KEY (id_pokemon) REFERENCES dim_pokemon(id_pokemon) ON DELETE CASCADE,
  CONSTRAINT bridge_hab_habilidade FOREIGN KEY (id_habilidade) REFERENCES dim_habilidade(id_habilidade)
);

CREATE INDEX idx_pokemon_habilidade ON bridge_pokemon_habilidade(id_pokemon);
CREATE INDEX idx_habilidade ON bridge_pokemon_habilidade(id_habilidade);

CREATE TABLE fato_pokemon_stats(
  id_fato SERIAL PRIMARY KEY,
  id_pokemon INTEGER NOT NULL,
  hp INTEGER NOT NULL,
  attack INTEGER NOT NULL,
  defense INTEGER NOT NULL,
  special_attack INTEGER NOT NULL,
  special_defense INTEGER NOT NULL,
  speed INTEGER NOT NULL,
  CONSTRAINT fk_fato_pokemon_stats FOREIGN KEY (id_pokemon) REFERENCES dim_pokemon(id_pokemon) ON DELETE CASCADE
);

CREATE INDEX idx_fato_pokemon ON fato_pokemon_stats(id_pokemon);