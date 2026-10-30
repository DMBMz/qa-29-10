"""Módulo de entidades e validação de cadastro de pessoas (Exercício 2)."""

from dataclasses import dataclass, field
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@.\s]+\.[^@.\s]+$")


@dataclass
class Email:
    """Representa um endereço de e-mail associado a uma pessoa."""

    id: int
    name: str


@dataclass
class Person:
    """Representa uma pessoa no cadastro."""

    id: int
    name: str
    age: int
    emails: list[Email] = field(default_factory=list)


class PersonDAO:
    """Data Access Object responsável pela validação e persistência de objetos Person."""

    def __init__(self) -> None:
        self._storage: list[Person] = []

    def save(self, p: Person) -> None:
        """Persiste um objeto Person caso seja válido; caso contrário, lança ValueError."""
        errors = self.isValidToInclude(p)
        if errors:
            raise ValueError("; ".join(errors))
        self._storage.append(p)

    def isValidToInclude(self, p: Person) -> list[str]:
        """Valida se um objeto Person atende a todas as regras de inclusão.

        Regras:
            1. O nome deve ser composto por ao menos 2 partes e cada parte deve conter apenas letras.
            2. A idade deve estar no intervalo fechado [1, 200].
            3. O objeto Person deve possuir pelo menos um objeto Email associado.
            4. O atributo name de cada Email deve seguir o formato '_____@____._____'.

        Args:
            p: Objeto Person a ser validado.

        Returns:
            Lista de mensagens de erro encontradas (vazia se válido).
        """
        errors: list[str] = []

        parts = p.name.strip().split() if p.name else []
        if len(parts) < 2 or not all(part.isalpha() for part in parts):
            errors.append(
                "O nome deve ser composto por ao menos 2 partes e conter apenas letras."
            )

        if p.age < 1 or p.age > 200:
            errors.append("A idade deve estar no intervalo [1, 200].")

        if not p.emails:
            errors.append("O objeto Person deve possuir pelo menos um Email associado.")
        else:
            for email in p.emails:
                if not email.name or not EMAIL_REGEX.match(email.name):
                    errors.append(
                        f"O email '{email.name}' é inválido. Formato esperado: _____@____._____"
                    )

        return errors

