import csv


class Imovel:
    def __init__(self, tipo, aluguel_base):
        self.tipo = tipo
        self.aluguel_base = aluguel_base
        self.adicional_quartos = 0
        self.adicional_garagem = 0
        self.desconto = 0

    def calcular_aluguel(self):
        valor = self.aluguel_base + self.adicional_quartos + self.adicional_garagem
        valor = valor - self.desconto
        return round(valor, 2)


class Apartamento(Imovel):
    def __init__(self):
        super().__init__("Apartamento", 700.00)


class Casa(Imovel):
    def __init__(self):
        super().__init__("Casa", 900.00)


class Estudio(Imovel):
    def __init__(self):
        super().__init__("Estúdio", 1200.00)


class Orcamento:
    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.taxa_contrato = 2000.00
        self.parcelas_contrato = parcelas_contrato

    def calcular_parcela_contrato(self):
        return round(self.taxa_contrato / self.parcelas_contrato, 2)

    def mostrar_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela_contrato()

        print("\n========== RESUMO DO ORÇAMENTO ==========")
        print("Tipo de imóvel:", self.imovel.tipo)
        print(f"Aluguel-base: R$ {self.imovel.aluguel_base:.2f}")
        print(f"Adicional por quartos: R$ {self.imovel.adicional_quartos:.2f}")
        print(f"Adicional de garagem/estacionamento: R$ {self.imovel.adicional_garagem:.2f}")
        print(f"Desconto: R$ {self.imovel.desconto:.2f}")
        print("-----------------------------------------")
        print(f"Aluguel mensal: R$ {aluguel:.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contrato:.2f}")
        print(f"Parcelamento da taxa: {self.parcelas_contrato} parcela(s) de R$ {parcela:.2f}")
        print("=========================================")

    def gerar_csv(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela_contrato()

        with open("rentsmart_projecao.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([
                "Mês",
                "Aluguel mensal (R$)",
                "Parcela da taxa contratual (R$)",
                "Total previsto no mês (R$)"
            ])

            for mes in range(1, 13):
                if mes <= self.parcelas_contrato:
                    taxa_mes = parcela
                else:
                    taxa_mes = 0.00

                total_mes = round(aluguel + taxa_mes, 2)
                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}".replace(".", ","),
                    f"{taxa_mes:.2f}".replace(".", ","),
                    f"{total_mes:.2f}".replace(".", ",")
                ])

        print("\nArquivo 'rentsmart_projecao.csv' gerado com sucesso.")


def pedir_opcao(pergunta, opcoes):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in opcoes:
            return resposta
        print("Opção inválida. Tente novamente.")


def pedir_inteiro(pergunta, minimo, maximo):
    while True:
        try:
            numero = int(input(pergunta))
            if minimo <= numero <= maximo:
                return numero
            print(f"Valor inválido! Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def executar():
    print("=========================================")
    print("       RENTSMART - ORÇAMENTO DE ALUGUEL")
    print("=========================================")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    escolha = pedir_opcao("Escolha o tipo de imóvel (1, 2 ou 3): ", ["1", "2", "3"])

    if escolha == "1":
        imovel = Apartamento()
        quartos = pedir_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)

        if quartos == 2:
            imovel.adicional_quartos = 200.00

        garagem = pedir_opcao("Deseja uma vaga de garagem por R$ 300,00 ao mês? (s/n): ", ["s", "n"])
        if garagem == "s":
            imovel.adicional_garagem = 300.00

        criancas = pedir_opcao("O cliente possui crianças? (s/n): ", ["s", "n"])
        if criancas == "n":
            valor_antes_desconto = imovel.aluguel_base + imovel.adicional_quartos + imovel.adicional_garagem
            imovel.desconto = round(valor_antes_desconto * 0.05, 2)

    elif escolha == "2":
        imovel = Casa()
        quartos = pedir_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)

        if quartos == 2:
            imovel.adicional_quartos = 250.00

        garagem = pedir_opcao("Deseja uma vaga de garagem por R$ 300,00 ao mês? (s/n): ", ["s", "n"])
        if garagem == "s":
            imovel.adicional_garagem = 300.00

    else:
        imovel = Estudio()
        estacionamento = pedir_opcao(
            "Deseja o pacote inicial de 2 vagas por R$ 250,00 ao mês? (s/n): ",
            ["s", "n"]
        )

        if estacionamento == "s":
            vagas_extras = pedir_inteiro("Quantas vagas adicionais deseja? (0 a 20): ", 0, 20)
            imovel.adicional_garagem = 250.00 + (vagas_extras * 60.00)

    parcelas = pedir_inteiro(
        "Em quantas parcelas deseja pagar a taxa contratual (1 a 5)? ",
        1,
        5
    )

    orcamento = Orcamento(imovel, parcelas)
    orcamento.mostrar_resumo()
    orcamento.gerar_csv()


if __name__ == "__main__":
    executar()
