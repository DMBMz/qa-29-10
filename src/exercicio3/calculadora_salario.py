"""Módulo de cálculo de salário líquido de funcionários (Exercício 3)."""

from dataclasses import dataclass
from enum import Enum


class Cargo(Enum):
    """Cargos disponíveis para um funcionário."""

    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


@dataclass
class Funcionario:
    """Representa um funcionário com salário base e cargo."""

    nome: str
    email: str
    salario_base: float
    cargo: Cargo


class CalculadoraSalario:
    """Calculadora de salário líquido de acordo com o cargo e faixa salarial."""

    REGRAS_DESCONTO: dict[Cargo, tuple[float, float, float]] = {
        Cargo.DESENVOLVEDOR: (3000.00, 0.20, 0.10),
        Cargo.DBA: (2000.00, 0.25, 0.15),
        Cargo.TESTADOR: (2000.00, 0.25, 0.15),
        Cargo.GERENTE: (5000.00, 0.30, 0.20),
    }

    def calcular_salario_liquido(self, funcionario: Funcionario) -> float:
        """Calcula o salário líquido aplicando a alíquota de desconto correspondente ao cargo.

        Args:
            funcionario: Instância de Funcionario contendo cargo e salário base.

        Returns:
            Valor do salário líquido calculado.
        """
        limite, desconto_maior_igual, desconto_menor = self.REGRAS_DESCONTO[
            funcionario.cargo
        ]
        if funcionario.salario_base >= limite:
            aliquota = desconto_maior_igual
        else:
            aliquota = desconto_menor
        return round(funcionario.salario_base * (1.0 - aliquota), 2)
