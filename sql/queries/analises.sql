-- Os 10 pokemons mais fortes
SELECT
    p.nome_pokemon,
    (F.hp + f.attack + f.defense + f.special_attack + f.special_defense + f.speed) as total_stats
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p on f.id_pokemon = p.id_pokemon
ORDER BY total_stats DESC
LIMIT 10;

-- Os 10 Pokemons mais rápidos
SELECT
    p.nome_pokemon,
    f.speed
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
ORDER BY speed DESC
LIMIT 10;

-- Média de ataque por tipo de pokemon
SELECT
    t.nome_tipo,
    AVG(f.attack) as attack_averege
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
INNER JOIN bridge_pokemon_tipo as bt ON p.id_pokemon = bt.id_pokemon
INNER JOIN dim_tipo as t ON bt.id_tipo = t.id_tipo
GROUP BY nome_tipo
ORDER BY attack_averege DESC;

-- Quantidade de pokemons por tipo
SELECT
    t.nome_tipo,
    COUNT(p.id_pokemon) as pokemons_amount
FROM bridge_pokemon_tipo as bt
INNER JOIN dim_tipo as t ON t.id_tipo = bt.id_tipo
INNER JOIN dim_pokemon as p ON bt.id_pokemon = p.id_pokemon
GROUP BY t.nome_tipo
ORDER BY pokemons_amount DESC

-- 10 pokemons com melhor equilibrio
SELECT
    p.nome_pokemon,
    ROUND((f.hp + f.speed + f.attack + f.defense + f.special_attack + f.special_defense) / 6.0, 2) as  media_stats
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
ORDER BY Media_stats DESC
LIMIT 10;

-- 10 pokemons mais defensível
SELECT
    p.nome_pokemon,
    (f.defense + f.special_defense + f.hp) as defense_total
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
ORDER BY defense_total DESC
LIMIT 10;

-- 10 pokemons mais ofensívos
SELECT
    p.nome_pokemon,
    (f.attack + f.special_attack) as ataque_total
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
ORDER BY Ataque_Total DESC
LIMIT 10;

-- Tipos mais fortes
SELECT
    t.nome_tipo,
    AVG(f.hp + f.attack + f.defense + f.special_attack + f.special_defense + f.speed) as media_total
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
INNER JOIN bridge_pokemon_tipo as bt ON p.id_pokemon = bt.id_pokemon
INNER JOIN dim_tipo as t ON bt.id_tipo = t.id_tipo
GROUP BY t.nome_tipo
ORDER BY media_total DESC

-- Tipo mais rápido
SELECT
    t.nome_tipo,
    AVG(f.speed) as Media_Speed
FROM fato_pokemon_stats as f
INNER JOIN dim_pokemon as p ON f.id_pokemon = p.id_pokemon
INNER JOIN bridge_pokemon_tipo as bt ON p.id_pokemon = bt.id_pokemon
INNER JOIN dim_tipo as t ON bt.id_tipo = t.id_tipo
GROUP BY t.nome_tipo
ORDER BY Media_Speed DESC

-- Tipos com mais habilidades únicas
SELECT
    dt.nome_tipo,
    COUNT(DISTINCT(ph.id_habilidade)) as Total_Habilidades
FROM bridge_pokemon_habilidade as ph
INNER JOIN dim_pokemon as p ON ph.id_pokemon = p.id_pokemon
INNER JOIN bridge_pokemon_tipo as pt ON p.id_pokemon = pt.id_pokemon
INNER JOIN dim_tipo as dt ON pt.id_tipo = dt.id_tipo
INNER JOIN dim_habilidade as h ON ph.id_habilidade = h.id_habilidade
GROUP BY dt.nome_tipo
ORDER BY Total_Habilidades DESC


-- Rank geral de score
SELECT
    p.nome_pokemon,
    (
        f.attack * 0.3 +
        f.special_attack * 0.2 +
        f.speed * 0.2 +
        f.hp * 0.1 +
        f.defense * 0.1 +
        f.special_defense * 0.1
    ) AS score
FROM fato_pokemon_stats f
JOIN dim_pokemon p ON p.id_pokemon = f.id_pokemon
ORDER BY score DESC
LIMIT 10;

-- Pokemons com mais Habilidades
SELECT
    p.nome_pokemon,
    COUNT(ph.id_habilidade) as total_habilidades
FROM dim_pokemon p
JOIN bridge_pokemon_habilidade ph ON p.id_pokemon = ph.id_pokemon
GROUP BY p.nome_pokemon
ORDER BY total_habilidades DESC
LIMIT 10;

