"""Suíte de testes TDD para o Exercício 1: Classificação de Triângulos."""

from exercicio1.triangulo import Triangulo, classificar_triangulo


# CT01: Triângulo escaleno válido
def test_ct01_triangulo_escaleno_valido() -> None:
    triangulo = Triangulo(3, 4, 5)
    assert triangulo.classificar() == "Escaleno"
    assert classificar_triangulo(3, 4, 5) == "Escaleno"


# CT02: Triângulo isósceles válido
def test_ct02_triangulo_isosceles_valido() -> None:
    assert classificar_triangulo(6, 6, 4) == "Isosceles"


# CT03: Triângulo equilátero válido
def test_ct03_triangulo_equilatero_valido() -> None:
    assert classificar_triangulo(5, 5, 5) == "Equilatero"


# CT04: Pelo menos 3 CTs para isósceles válido contendo a permutação dos mesmos valores
def test_ct04a_triangulo_isosceles_permutacao_1() -> None:
    assert classificar_triangulo(5, 5, 3) == "Isosceles"


def test_ct04b_triangulo_isosceles_permutacao_2() -> None:
    assert classificar_triangulo(5, 3, 5) == "Isosceles"


def test_ct04c_triangulo_isosceles_permutacao_3() -> None:
    assert classificar_triangulo(3, 5, 5) == "Isosceles"


# CT05: Um valor zero
def test_ct05_um_valor_zero() -> None:
    assert classificar_triangulo(0, 4, 5) == "Invalido"
    assert classificar_triangulo(4, 0, 5) == "Invalido"
    assert classificar_triangulo(4, 5, 0) == "Invalido"


# CT06: Um valor negativo
def test_ct06_um_valor_negativo() -> None:
    assert classificar_triangulo(-2, 4, 5) == "Invalido"
    assert classificar_triangulo(4, -2, 5) == "Invalido"
    assert classificar_triangulo(4, 5, -2) == "Invalido"


# CT07 e CT08: A soma de 2 lados é igual ao terceiro lado (1 CT para cada permutação)
def test_ct07a_soma_dois_lados_igual_terceiro_permutacao_1() -> None:
    assert classificar_triangulo(2, 3, 5) == "Invalido"


def test_ct07b_soma_dois_lados_igual_terceiro_permutacao_2() -> None:
    assert classificar_triangulo(2, 5, 3) == "Invalido"


def test_ct08_soma_dois_lados_igual_terceiro_permutacao_3() -> None:
    assert classificar_triangulo(5, 2, 3) == "Invalido"


# CT09 e CT10: A soma de 2 lados é menor que o terceiro lado (1 CT para cada permutação)
def test_ct09a_soma_dois_lados_menor_terceiro_permutacao_1() -> None:
    assert classificar_triangulo(2, 3, 6) == "Invalido"


def test_ct09b_soma_dois_lados_menor_terceiro_permutacao_2() -> None:
    assert classificar_triangulo(2, 6, 3) == "Invalido"


def test_ct10_soma_dois_lados_menor_terceiro_permutacao_3() -> None:
    assert classificar_triangulo(6, 2, 3) == "Invalido"


# CT11: Os três valores iguais a zero
def test_ct11_tres_valores_iguais_a_zero() -> None:
    assert classificar_triangulo(0, 0, 0) == "Invalido"

