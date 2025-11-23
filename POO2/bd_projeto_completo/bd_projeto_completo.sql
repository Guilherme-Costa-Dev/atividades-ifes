CREATE DATABASE projetoPOO;

USE projetoPOO;

CREATE TABLE Produto(
	idProduto INT NOT NULL auto_increment,
    codProduto INT NOT NULL,
    nomeProduto VARCHAR(30) NOT NULL,
    qtdProduto INT NOT NULL,
    valorProduto FLOAT NOT NULL,
    PRIMARY KEY (idProduto)
);

CREATE TABLE Cliente(
	idCliente INT NOT NULL AUTO_INCREMENT,
    CPF VARCHAR(14) NOT NULL,
    nomeCliente VARCHAR(30) NOT NULL,
    emailCliente VARCHAR(50) NOT NULL,
    PRIMARY KEY (idCliente)
);

SELECT * FROM cliente;