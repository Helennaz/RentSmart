# RentSmart — Sistema de Orçamento de Locação

## Sobre o projeto

O RentSmart é um programa desenvolvido em Python para ajudar a calcular o orçamento de aluguel de imóveis da R.M Imóveis. Ele calcula o aluguel mensal, os adicionais, possíveis descontos e a taxa contratual, além de gerar um arquivo CSV com a projeção dos pagamentos durante 12 meses.

## Funcionalidades

- Escolha entre apartamento, casa e estúdio.
- Cálculo de adicionais por quantidade de quartos.
- Cálculo de garagem para apartamentos e casas.
- Cálculo do pacote de estacionamento e vagas extras para estúdios.
- Desconto de 5% para apartamentos quando o cliente informa que não possui crianças.
- Parcelamento da taxa contratual de R$ 2.000,00 em até 5 vezes.
- Validação das entradas do usuário.
- Geração do arquivo `rentsmart_projecao.csv` com a projeção de 12 meses.

## Requisitos

- Python 3 instalado no computador.
- Não é necessário instalar bibliotecas externas: o programa usa módulos que já vêm com o Python.

## Como executar

1. Baixe ou clone este repositório.
2. Abra a pasta do projeto no VS Code.
3. Abra o terminal do VS Code.
4. Execute o comando:

   ```bash
   python rentsmart.py
   ```

5. Responda às perguntas exibidas no terminal.
6. Ao final, o programa criará o arquivo `rentsmart_projecao.csv` na pasta em que foi executado.

Se o comando `python` não funcionar no Windows, tente:

```bash
py rentsmart.py
```

## Arquivos do projeto

- `rentsmart.py`: código-fonte do programa.
- `README.md`: explicação do projeto e instruções de execução.
- `rentsmart_projecao.csv`: arquivo gerado automaticamente após executar o programa.

## Regras de negócio implementadas

- Apartamento de 1 quarto: aluguel-base de R$ 700,00.
- Apartamento de 2 quartos: adicional de R$ 200,00.
- Casa de 1 quarto: aluguel-base de R$ 900,00.
- Casa de 2 quartos: adicional de R$ 250,00.
- Garagem para apartamento ou casa: adicional de R$ 300,00 por mês.
- Estúdio: aluguel-base de R$ 1.200,00.
- Estacionamento do estúdio: pacote inicial de 2 vagas por R$ 250,00 e R$ 60,00 por vaga adicional.
- Apartamento sem crianças: desconto de 5% sobre o aluguel após os adicionais.
- Taxa contratual: R$ 2.000,00, parcelada em até 5 vezes.

## Observação

O CSV mostra o aluguel mensal e a parcela da taxa contratual nos meses em que ela é paga. A taxa contratual é apresentada separadamente do aluguel.

## Autor

Mayra Helena Santos Varela.
