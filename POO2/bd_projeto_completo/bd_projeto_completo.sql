gitCREATE DATABASE projetoPOO;

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

CREATE TABLE Venda(
	idVenda int NOT NULL auto_increment,
    dataVenda date not null,
    valorVenda float not null,
    idCliente int not null,
    primary key (idVenda)
);

create table ItemVenda(
	idItemVenda int not null auto_increment,
    idVenda int not null,
    idProduto int not null,
    qtdProduto int not null,
    vlrUnitario float not null,
    
    primary key (idItemVenda),
    foreign key (idVenda) references Venda(idVenda),
    foreign key (idProduto) references Produto(idProduto)
);

SELECT * FROM cliente;