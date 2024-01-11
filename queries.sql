-- Criar a tabela Jogadores
CREATE TABLE IF NOT EXISTS Jogadores (
    ID INTEGER PRIMARY KEY UNIQUE,
    Nome TEXT,
    Nacionalidade TEXT,
    Idade INTEGER,
    Posicao TEXT,
    ClubeAtual TEXT
);

-- Inserir jogadores
INSERT OR IGNORE INTO Jogadores (Nome, Nacionalidade, Idade, Posicao, ClubeAtual)
VALUES 
    -- Los Pollos Hermanos
    ('Walter White', 'Estados Unidos', 52, 'Guarda-Redes', 'Los Pollos Hermanos'),
    ('Jesse Pinkman', 'Estados Unidos', 35, 'Defesa Central', 'Los Pollos Hermanos'),
    ('Skyler White', 'Estados Unidos', 48, 'Lateral Esquerdo', 'Los Pollos Hermanos'),
    ('Hank Schrader', 'Estados Unidos', 47, 'Lateral Direito', 'Los Pollos Hermanos'),
    ('Mike Ehrmantraut', 'Alemanha', 57, 'Médio Centro', 'Los Pollos Hermanos'),
    ('Saul Goodman', 'Estados Unidos', 48, 'Médio Ofensivo', 'Los Pollos Hermanos'),
    ('Gus Fring', 'Chile', 54, 'Extremo Direito', 'Los Pollos Hermanos'),
    ('Todd Alquist', 'Estados Unidos', 28, 'Ponta de Lança', 'Los Pollos Hermanos'),
    ('Lydia Rodarte-Quayle', 'Estados Unidos', 39, 'Extremo Esquerdo', 'Los Pollos Hermanos'),
    ('Steven Gomez', 'Estados Unidos', 41, 'Defesa Central', 'Los Pollos Hermanos'),
    ('Badger Mayhew', 'Estados Unidos', 35, 'Médio Ofensivo', 'Los Pollos Hermanos'),
    ('Skinny Pete', 'Estados Unidos', 37, 'Extremo Direito', 'Los Pollos Hermanos'),
    ('Gretchen Schwartz', 'Estados Unidos', 52, 'Médio Centro', 'Los Pollos Hermanos'),
    ('Elliot Schwartz', 'Estados Unidos', 53, 'Médio Defensivo', 'Los Pollos Hermanos'),
    ('Tuco Salamanca', 'México', 35, 'Ponta de Lança', 'Los Pollos Hermanos'),
    ('Hector Salamanca', 'México', 76, 'Defesa Central', 'Los Pollos Hermanos'),
    ('Gale Boetticher', 'Estados Unidos', 40, 'Médio Ofensivo', 'Los Pollos Hermanos'),
    ('Huell Babineaux', 'Estados Unidos', 42, 'Médio Defensivo', 'Los Pollos Hermanos'),
    ('Lawson', 'Estados Unidos', 45, 'Lateral Esquerdo', 'Los Pollos Hermanos'),

    -- Benfica
    ('Anatoliy Trubin', 'Ucrânia', 22, 'Guarda-Redes', 'Benfica'),
    ('Samuel Soares', 'Portugal', 21, 'Guarda-Redes', 'Benfica'),
    ('Leo Kokubo', 'Japão', 22, 'Guarda-Redes', 'Benfica'),
    ('António Silva', 'Portugal', 20, 'Defesa Central', 'Benfica'),
    ('Morato', 'Brasil', 22, 'Defesa Central', 'Benfica'),
    ('Tomás Araújo', 'Portugal', 21, 'Defesa Central', 'Benfica'),
    ('Nicolás Otamendi', 'Argentina', 35, 'Defesa Central', 'Benfica'),
    ('David Jurásek', 'República Checa', 23, 'Lateral Esquerdo', 'Benfica'),
    ('Juan Bernat', 'Espanha', 30, 'Lateral Esquerdo', 'Benfica'),
    ('Alexander Bah', 'Dinamarca', 26, 'Lateral Direito', 'Benfica'),
    ('João Neves', 'Portugal', 19, 'Médio Defensivo', 'Benfica'),
    ('Florentino', 'Portugal', 24, 'Médio Defensivo', 'Benfica'),
    ('Orkun Kökçü', 'Turquia', 23, 'Médio Centro', 'Benfica'),
    ('Gonçalo Guedes', 'Portugal', 27, 'Extremo Esquerdo', 'Benfica'),
    ('David Neres', 'Brasil', 26, 'Extremo Direito', 'Benfica'),
    ('Ángel Di María', 'Argentina', 35, 'Extremo Direito', 'Benfica'),
    ('Tiago Gouveia', 'Portugal', 22, 'Extremo Direito', 'Benfica'),
    ('Rafa', 'Portugal', 30, 'Segundo Avançado', 'Benfica'),
    ('Marcos Leonardo', 'Brasil', 20, 'Ponta de Lança', 'Benfica'),
    ('Arthur Cabral', 'Brasil', 25, 'Ponta de Lança', 'Benfica'),
    ('Petar Musa', 'Croácia', 25, 'Ponta de Lança', 'Benfica'),
    ('Casper Tengstedt', 'Dinamarca', 23, 'Ponta de Lança', 'Benfica'),

    -- Sporting
    ('Franco Israel', 'Uruguai', 23, 'Guarda-Redes', 'Sporting'),
    ('Diego Callai', 'Brasil', 19, 'Guarda-Redes', 'Sporting'),
    ('Antonio Adán', 'Espanha', 36, 'Guarda-Redes', 'Sporting'),
    ('Gonçalo Inácio', 'Portugal', 22, 'Defesa Central', 'Sporting'),
    ('Ousmane Diomande', 'Costa do Marfim', 20, 'Defesa Central', 'Sporting'),
    ('Jerry St. Juste', 'Holanda', 27, 'Defesa Central', 'Sporting'),
    ('Sebastián Coates', 'Uruguai', 33, 'Defesa Central', 'Sporting'),
    ('Eduardo Quaresma', 'Portugal', 21, 'Defesa Central', 'Sporting'),
    ('João Muniz', 'Portugal', 18, 'Defesa Central', 'Sporting'),
    ('Rafael', 'Brasil', 20, 'Defesa Central', 'Sporting'),
    ('Nuno Santos', 'Portugal', 28, 'Lateral Esquerdo', 'Sporting'),
    ('Matheus Reis', 'Brasil', 28, 'Lateral Esquerdo', 'Sporting'),
    ('Iván Fresneda', 'Espanha', 19, 'Lateral Direito', 'Sporting'),
    ('Ricardo Esgaio', 'Portugal', 30, 'Lateral Direito', 'Sporting'),
    ('Morten Hjulmand', 'Dinamarca', 24, 'Médio Defensivo', 'Sporting'),
    ('Dário Essugo', 'Portugal', 18, 'Médio Defensivo', 'Sporting'),
    ('Hidemasa Morita', 'Japão', 28, 'Médio Centro', 'Sporting'),
    ('Daniel Bragança', 'Portugal', 24, 'Médio Centro', 'Sporting'),
    ('Trincão', 'Portugal', 24, 'Extremo Esquerdo', 'Sporting'),
    ('Pedro Gonçalves', 'Portugal', 25, 'Extremo Direito', 'Sporting'),
    ('Marcus Edwards', 'Inglaterra', 25, 'Extremo Direito', 'Sporting'),
    ('Geny Catamo', 'Moçambique', 22, 'Extremo Direito', 'Sporting'),
    ('Rafael Camacho', 'Portugal', 23, 'Extremo Direito', 'Sporting'),
    ('Viktor Gyökeres', 'Suécia', 25, 'Ponta de Lança', 'Sporting'),
    ('Paulinho', 'Portugal', 31, 'Ponta de Lança', 'Sporting'),
    ('Rodrigo Ribeiro', 'Portugal', 18, 'Ponta de Lança', 'Sporting'),

    -- Porto
    ('Diogo Costa', 'Portugal', 24, 'Guarda-Redes', 'Porto'),
    ('Cláudio Ramos', 'Portugal', 32, 'Guarda-Redes', 'Porto'),
    ('Samuel Portugal', 'Brasil', 29, 'Guarda-Redes', 'Porto'),
    ('David Carmo', 'Portugal', 24, 'Defesa Central', 'Porto'),
    ('Fábio Cardoso', 'Portugal', 29, 'Defesa Central', 'Porto'),
    ('Zé Pedro', 'Portugal', 26, 'Defesa Central', 'Porto'),
    ('Pepe', 'Portugal', 40, 'Defesa Central', 'Porto'),
    ('Iván Marcano', 'Espanha', 36, 'Defesa Central', 'Porto'),
    ('Wendell', 'Brasil', 30, 'Lateral Esquerdo', 'Porto'),
    ('Zaidu', 'Nigéria', 26, 'Lateral Esquerdo', 'Porto'),
    ('João Mário', 'Portugal', 24, 'Lateral Direito', 'Porto'),
    ('Jorge Sánchez', 'México', 26, 'Lateral Direito', 'Porto'),
    ('Alan Varela', 'Argentina', 22, 'Médio Defensivo', 'Porto'),
    ('Marko Grujić', 'Sérvia', 27, 'Médio Defensivo', 'Porto'),
    ('Stephen Eustaquio', 'Canadá', 27, 'Médio Centro', 'Porto'),
    ('Nico González', 'Espanha', 22, 'Médio Centro', 'Porto'),
    ('Romário Baró', 'Portugal', 23, 'Médio Centro', 'Porto'),
    ('Iván Jaime', 'Espanha', 23, 'Médio Ofensivo', 'Porto'),
    ('André Franco', 'Portugal', 25, 'Médio Ofensivo', 'Porto'),
    ('Pepê', 'Brasil', 26, 'Extremo Esquerdo', 'Porto'),
    ('Galeno', 'Brasil', 26, 'Extremo Esquerdo', 'Porto'),
    ('Francisco Conceição', 'Portugal', 21, 'Extremo Direito', 'Porto'),
    ('Gonçalo Borges', 'Portugal', 22, 'Extremo Direito', 'Porto'),
    ('Evanilson', 'Brasil', 24, 'Ponta de Lança', 'Porto'),
    ('Mehdi Taremi', 'Irão', 31, 'Ponta de Lança', 'Porto'),
    ('Toni Martínez', 'Espanha', 26, 'Ponta de Lança', 'Porto'),
    ('Danny Namaso', 'Inglaterra', 23, 'Ponta de Lança', 'Porto');
