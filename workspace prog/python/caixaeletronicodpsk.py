"""
Simulador de Caixa Eletrônico
Autor: Python Senior Dev
Descrição: Programa que calcula a quantidade mínima de cédulas para um saque
"""

from typing import Dict, List, Tuple


class CaixaEletronico:
    """
    Classe que simula o funcionamento de um caixa eletrônico
    """
    
    # Cédulas disponíveis em ordem decrescente
    CEDULAS = [100, 50, 10, 5, 2, 1]
    
    def __init__(self):
        """Inicializa o caixa eletrônico"""
        self.saldo_disponivel = 10000  # Saldo inicial do caixa (exemplo)
        
    def validar_valor(self, valor: int) -> Tuple[bool, str]:
        """
        Valida se o valor do saque é válido
        
        Args:
            valor: Valor a ser sacado
            
        Returns:
            Tuple[bool, str]: (válido, mensagem de erro)
        """
        if valor <= 0:
            return False, "Valor inválido. O saque deve ser um valor positivo."
        
        if valor > self.saldo_disponivel:
            return False, f"Saldo insuficiente no caixa. Disponível: R$ {self.saldo_disponivel:.2f}"
        
        # Verifica se é possível compor o valor com as cédulas disponíveis
        # Como temos cédula de 1 real, qualquer valor positivo é possível
        return True, ""
    
    def calcular_cedulas(self, valor: int) -> Dict[int, int]:
        """
        Calcula a quantidade mínima de cédulas para o valor solicitado
        
        Args:
            valor: Valor a ser sacado
            
        Returns:
            Dict[int, int]: Dicionário com a quantidade de cada cédula
        """
        restante = valor
        cedulas_utilizadas = {}
        
        for cedula in self.CEDULAS:
            if restante >= cedula:
                quantidade = restante // cedula
                cedulas_utilizadas[cedula] = quantidade
                restante -= quantidade * cedula
        
        return cedulas_utilizadas
    
    def exibir_cedulas(self, cedulas: Dict[int, int]) -> None:
        """
        Exibe as cédulas que serão entregues
        
        Args:
            cedulas: Dicionário com a quantidade de cada cédula
        """
        if not cedulas:
            print("Nenhuma cédula será entregue.")
            return
        
        print("\n" + "=" * 50)
        print("CÉDULAS A SEREM ENTREGUES:")
        print("=" * 50)
        
        total_cedulas = 0
        for cedula in self.CEDULAS:
            quantidade = cedulas.get(cedula, 0)
            if quantidade > 0:
                print(f"  R$ {cedula:3d} x {quantidade:2d} = R$ {cedula * quantidade:6.2f}")
                total_cedulas += quantidade
        
        print("=" * 50)
        print(f"Total de cédulas: {total_cedulas}")
        print("=" * 50)
    
    def sacar(self, valor: int) -> bool:
        """
        Realiza o saque do valor solicitado
        
        Args:
            valor: Valor a ser sacado
            
        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário
        """
        # Validação
        valido, mensagem = self.validar_valor(valor)
        if not valido:
            print(f"\n❌ ERRO: {mensagem}")
            return False
        
        # Cálculo das cédulas
        cedulas = self.calcular_cedulas(valor)
        
        # Exibição do resultado
        print(f"\n✅ Saque de R$ {valor:.2f} autorizado!")
        self.exibir_cedulas(cedulas)
        
        # Atualiza o saldo do caixa
        self.saldo_disponivel -= valor
        
        return True
    
    def exibir_menu(self) -> None:
        """Exibe o menu principal do caixa eletrônico"""
        print("\n" + "=" * 50)
        print("         CAIXA ELETRÔNICO")
        print("=" * 50)
        print(f"Saldo disponível no caixa: R$ {self.saldo_disponivel:.2f}")
        print("Cédulas disponíveis: 100, 50, 10, 5, 2, 1")
        print("=" * 50)


def main():
    """
    Função principal do programa
    """
    caixa = CaixaEletronico()
    
    print("\n" + "=" * 60)
    print("BEM-VINDO AO CAIXA ELETRÔNICO")
    print("=" * 60)
    
    while True:
        try:
            # Exibe o menu
            caixa.exibir_menu()
            
            # Solicita o valor do saque
            entrada = input("\nDigite o valor do saque (ou 'sair' para encerrar): R$ ").strip()
            
            # Verifica se o usuário quer sair
            if entrada.lower() in ['sair', 'exit', 'quit', '']:
                print("\n" + "=" * 60)
                print("Obrigado por usar nosso caixa eletrônico!")
                print("=" * 60)
                break
            
            # Converte para inteiro
            valor = int(entrada)
            
            # Realiza o saque
            caixa.sacar(valor)
            
            # Pergunta se deseja continuar
            print("\n" + "-" * 50)
            continuar = input("Deseja realizar outro saque? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("\n" + "=" * 60)
                print("Obrigado por usar nosso caixa eletrônico!")
                print("=" * 60)
                break
                
        except ValueError:
            print("\n❌ ERRO: Valor inválido! Por favor, digite apenas números inteiros.")
        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("Operação cancelada pelo usuário. Até logo!")
            print("=" * 60)
            break
        except Exception as e:
            print(f"\n❌ ERRO inesperado: {e}")
            print("Por favor, tente novamente.")


def versao_simples():
    """
    Versão mais simples e direta do programa (sem orientação a objetos)
    Útil para casos onde se deseja apenas a funcionalidade básica
    """
    cedulas = [100, 50, 10, 5, 2, 1]
    
    print("\n" + "=" * 50)
    print("CAIXA ELETRÔNICO - VERSÃO SIMPLES")
    print("=" * 50)
    
    while True:
        try:
            valor = int(input("\nDigite o valor do saque (número inteiro): R$ "))
            
            if valor <= 0:
                print("❌ Valor inválido! Digite um valor positivo.")
                continue
            
            valor_original = valor
            cedulas_utilizadas = {}
            
            # Calcula as cédulas
            for cedula in cedulas:
                if valor >= cedula:
                    quantidade = valor // cedula
                    cedulas_utilizadas[cedula] = quantidade
                    valor -= quantidade * cedula
            
            # Exibe o resultado
            print(f"\n✅ Saque de R$ {valor_original:.2f} realizado com sucesso!")
            print("-" * 50)
            print("Cédulas entregues:")
            
            total_cedulas = 0
            for cedula in cedulas:
                quantidade = cedulas_utilizadas.get(cedula, 0)
                if quantidade > 0:
                    print(f"  R$ {cedula:3d} x {quantidade:2d} = R$ {cedula * quantidade:6.2f}")
                    total_cedulas += quantidade
            
            print("-" * 50)
            print(f"Total de cédulas: {total_cedulas}")
            print("=" * 50)
            
            # Pergunta se deseja continuar
            continuar = input("\nDeseja realizar outro saque? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("\nObrigado por usar nosso caixa eletrônico!")
                break
                
        except ValueError:
            print("❌ ERRO: Digite apenas números inteiros!")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada. Até logo!")
            break


if __name__ == "__main__":
    # Escolha qual versão executar
    # main()  # Versão completa com orientação a objetos
    versao_simples()  # Versão simples e direta