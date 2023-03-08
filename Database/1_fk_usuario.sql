ALTER TABLE usuario
	ADD CONSTRAINT FK_usuario_tipousuario
    FOREIGN KEY (tipousuario_id) REFERENCES tipousuario (id);