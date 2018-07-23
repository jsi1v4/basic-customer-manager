CREATE TABLE tb_customer_account (
    id_customer INT NOT NULL AUTO_INCREMENT,
    cpf_cnpj VARCHAR(14) NOT NULL,
    nm_customer VARCHAR(30) NOT NULL,
    is_active BOOLEAN NOT NULL,
    vl_total FLOAT NOT NULL,
    PRIMARY KEY (id_customer)
    );