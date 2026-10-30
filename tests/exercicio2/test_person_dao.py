"""Suíte de testes TDD para o Exercício 2: Validação de Cadastro (PersonDAO)."""

import pytest

from exercicio2.person import Email, Person, PersonDAO


def test_pessoa_totalmente_valida() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Maria Silva",
        age=30,
        emails=[Email(id=1, name="maria@empresa.com")],
    )
    assert dao.isValidToInclude(person) == []


def test_nome_com_apenas_uma_parte_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Maria",
        age=25,
        emails=[Email(id=1, name="maria@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "nome" in errors[0].lower()


def test_nome_vazio_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="   ",
        age=25,
        emails=[Email(id=1, name="maria@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "nome" in errors[0].lower()


def test_nome_contendo_numeros_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Maria Silva123",
        age=25,
        emails=[Email(id=1, name="maria@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "nome" in errors[0].lower()


def test_nome_contendo_simbolos_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Maria @Silva",
        age=25,
        emails=[Email(id=1, name="maria@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "nome" in errors[0].lower()


def test_idade_valor_limite_zero_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Joao Souza",
        age=0,
        emails=[Email(id=1, name="joao@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "idade" in errors[0].lower()


def test_idade_valor_limite_um_valido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Joao Souza",
        age=1,
        emails=[Email(id=1, name="joao@empresa.com")],
    )
    assert dao.isValidToInclude(person) == []


def test_idade_valor_limite_duzentos_valido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Joao Souza",
        age=200,
        emails=[Email(id=1, name="joao@empresa.com")],
    )
    assert dao.isValidToInclude(person) == []


def test_idade_valor_limite_duzentos_e_um_invalido() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Joao Souza",
        age=201,
        emails=[Email(id=1, name="joao@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "idade" in errors[0].lower()


def test_idade_negativa_invalida() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Joao Souza",
        age=-5,
        emails=[Email(id=1, name="joao@empresa.com")],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "idade" in errors[0].lower()


def test_pessoa_sem_email_lista_vazia() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Carlos Pereira",
        age=40,
        emails=[],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "email" in errors[0].lower()


def test_pessoa_sem_email_lista_nula() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Carlos Pereira",
        age=40,
        emails=None,  # type: ignore[arg-type]
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "email" in errors[0].lower()


@pytest.mark.parametrize(
    "invalid_email",
    [
        "usuarioempresa.com",  # sem @
        "usuario@empresacom",  # sem .
        "@empresa.com",  # parte antes do @ vazia
        "usuario@.com",  # parte entre @ e . vazia
        "usuario@empresa.",  # parte após o . vazia
        "",  # string vazia
    ],
)
def test_formatos_de_email_invalidos(invalid_email: str) -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Ana Costa",
        age=28,
        emails=[Email(id=1, name=invalid_email)],
    )
    errors = dao.isValidToInclude(person)
    assert len(errors) == 1
    assert "email" in errors[0].lower()


def test_save_pessoa_valida() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Fernanda Lima",
        age=35,
        emails=[Email(id=1, name="fernanda@dominio.org")],
    )
    dao.save(person)
    assert person in dao._storage


def test_save_pessoa_invalida_lanca_excecao() -> None:
    dao = PersonDAO()
    person = Person(
        id=1,
        name="Fernanda",
        age=300,
        emails=[],
    )
    with pytest.raises(ValueError, match="nome"):
        dao.save(person)

