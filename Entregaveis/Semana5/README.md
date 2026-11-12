# Sistema de Análise de Dados

Projeto simples em Python que lê um arquivo CSV, valida os dados com regex e gera um relatório.

## Como executar

```bash
python script_principal.py
```

O arquivo `dados.csv` deve estar na mesma pasta.

## Validações

- E-mail no formato `nome@dominio.com`
- CPF no formato `000.000.000-00`
- Telefone no formato `(99) 99999-9999`
- Data no formato `dd/mm/aaaa`

## Exceções

- `FileNotFoundError`: arquivo não encontrado
- `ValueError`: valor inválido
- `KeyError`: coluna ausente no CSV
- `FormatoInvalidoError`: dado com formato inválido

## Exemplo de saída

```text
===== RELATÓRIO =====
Email: joao@email.com
CPF: 123.456.789-00
Telefone: (98) 91234-5678
Data: 10/05/2024
Status: Válido
----------------------
Total de registros: 5
Registros válidos: 2
Registros inválidos: 3
```
