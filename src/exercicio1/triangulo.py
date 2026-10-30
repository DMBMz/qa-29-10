"""Módulo de classificação de triângulos (Exercício 1)."""


def classificar_triangulo(a: int, b: int, c: int) -> str:
    """Classifica um triângulo a partir das medidas inteiras de seus três lados.

    Regras de validade:
        - Todos os lados devem ser estritamente maiores que zero.
        - A soma de quaisquer dois lados deve ser estritamente maior que o terceiro lado.

    Args:
        a: Medida do primeiro lado.
        b: Medida do segundo lado.
        c: Medida do terceiro lado.

    Returns:
        "Equilatero", "Isosceles", "Escaleno" ou "Invalido".
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalido"

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalido"

    if a == b == c:
        return "Equilatero"

    if a == b or a == c or b == c:
        return "Isosceles"

    return "Escaleno"


class Triangulo:
    """Representa um triângulo com três lados inteiros."""

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def classificar(self) -> str:
        """Retorna a classificação do triângulo."""
        return classificar_triangulo(self.a, self.b, self.c)

