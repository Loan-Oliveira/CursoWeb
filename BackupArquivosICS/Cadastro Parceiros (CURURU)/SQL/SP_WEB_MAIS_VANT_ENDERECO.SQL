USE [ics]
GO

/****** Object:  StoredProcedure [dbo].[SP_WEB_MAIS_VANT_ENDERECO]    Script Date: 27/03/2024 11:14:37 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SP_WEB_MAIS_VANT_ENDERECO]
   @NR_ID_PARC INT = 0,
   @NR_ID_ENDERECO INT = 0,
	@LOGRADOURO VARCHAR(150)  = NULL,
	@NUMERO VARCHAR(50) = NULL,
	@COMPLEMENTO VARCHAR(100) = NULL,
	@BAIRRO VARCHAR(150) = NULL,
	@CEP VARCHAR(50) = NULL,
	@DDD CHAR(2) = 0,
	@FONE CHAR(10) = NULL,
	@DDD_CELULAR CHAR(2) = 0,
	@CELULAR CHAR(10) = NULL,
	@SITE VARCHAR(150) = NULL,
   @TP_OP INT = 0
AS BEGIN
	
	/**** BUSCA ****/
	IF @TP_OP = 0
	BEGIN
		IF (SELECT T837_NR_ID FROM T837_MAIS_VANT_PARC WHERE T837_NR_ID = @NR_ID_PARC) IS NULL
		BEGIN
			SELECT 1 AS 'CODERRO', 'PARCEIRO N�O ENCONTRADO' AS 'MSGERRO'
			RETURN	
		END ELSE
		BEGIN
			SELECT
			T838_NR_ID_ENDERECO,
			T838_CA_LOGRADOURO,
			T838_CA_NUMERO,
			T838_CA_COMPLEMENTO,
			T838_CA_BAIRRO,
			T838_CA_CEP,
			T838_CA_DDD,
			T838_CA_FONE,
			T838_CA_DDD_CELULAR,
			T838_CA_CELULAR,
			T838_CA_SITE
			FROM T838_ENDERECO_PARCEIRO 
			WHERE T837_NR_ID = @NR_ID_PARC
			ORDER BY T838_NR_ID_ENDERECO
		END
	END

	/**** INCLUS�O ****/
	IF @TP_OP = 1
	BEGIN
		IF @NR_ID_PARC = NULL
		OR @LOGRADOURO = NULL
		OR @NUMERO = NULL
		OR @BAIRRO = NULL
		OR @CEP = NULL
		OR @DDD = NULL
		OR @FONE = NULL
		BEGIN
			SELECT 2 AS 'CODERRO', 'CAMPOS OBRIGAT�RIOS N�O PREENCHIDOS' AS 'MSGERRO'
			RETURN
		END
		ELSE IF (SELECT T837_NR_ID FROM T837_MAIS_VANT_PARC WHERE T837_NR_ID = @NR_ID_PARC) IS NULL
		BEGIN
			SELECT 1 AS 'CODERRO', 'PARCEIRO N�O ENCONTRADO' AS 'MSGERRO'
			RETURN
		END ELSE
		BEGIN
			INSERT INTO T838_ENDERECO_PARCEIRO
           (T837_NR_ID,
			T838_CA_LOGRADOURO,
			T838_CA_NUMERO,
			T838_CA_COMPLEMENTO,
			T838_CA_BAIRRO,
			T838_CA_CEP,
			T838_CA_DDD,
			T838_CA_FONE,
			T838_CA_DDD_CELULAR,
			T838_CA_CELULAR,
			T838_CA_SITE)
     VALUES
           (@NR_ID_PARC,
			@LOGRADOURO,
			@NUMERO,
			@COMPLEMENTO,
			@BAIRRO,
			@CEP,
			@DDD,
			@FONE,
			@DDD_CELULAR,
			@CELULAR,
			@SITE)
		END
	END

	/**** EXCLUS�O ****/
	IF @TP_OP = 2
	BEGIN
		IF (SELECT T838_NR_ID_ENDERECO FROM T838_ENDERECO_PARCEIRO WHERE T838_NR_ID_ENDERECO = @NR_ID_ENDERECO) IS NULL
		BEGIN
			SELECT 3 AS 'CODERRO', 'ENDERE�O DE PARCEIRO N�O ENCONTRADO' AS 'MSGERRO'
			RETURN
		END
		ELSE
		BEGIN
			DELETE FROM T838_ENDERECO_PARCEIRO WHERE T838_NR_ID_ENDERECO = @NR_ID_ENDERECO
		END
	END

END



GO


