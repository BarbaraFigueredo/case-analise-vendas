-- Criando a tabela de Vendas para teste
CREATE TABLE vendas (
    id_pedido INT,
    produto VARCHAR(50),
    categoria VARCHAR(50),
    qtd INT,
    preco_unitario DECIMAL(10, 2)
);

-- Inserindo os dados fictícios
INSERT INTO vendas VALUES
(101, 'Notebook', 'Eletrônicos', 1, 3500.00),
(102, 'Mouse', 'Periféricos', 5, 50.00),
(103, 'Teclado', 'Periféricos', 2, 100.00),
(104, 'Notebook', 'Eletrônicos', 1, 3500.00),
(105, 'Monitor', 'Eletrônicos', 2, 800.00),
(106, 'Mouse', 'Periféricos', -1, 50.00); -- Devolução