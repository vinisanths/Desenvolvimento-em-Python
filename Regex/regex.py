import re
"""
Expressões regulares(Regex) são padrões de texto usados para buscar, validar, extrair e substituir informações

re.match(padrao, texto) -> Verifica se o texto começa com o padrão
re.search(padrao, texto) -> Procura o padrão em qualquer parte
re.findall(padrao, texto) -> Retorna todas as ocorrênçias
re.sub(padrao, novo, texto) -> Substitui ocorrênçias
re.split(padrao, novo) -> Divide o texto pelo padrão
"""
texto = "Meu email é ana@gmail.com e o dele é bruno@gmail.com"
padrao = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(padrao, texto)
print(emails)


#Validar data no formato YYYY-MM-DD
padraoData = r"^\d{4}-\d{2}-\d{2}$"
print(re.match(padraoData, "2026-10-30"))
print(re.match(padraoData, "20/10/2026"))

#Extrair números de um texto
texto = "Comprei 3 livros por 120 reais"
numeros = re.findall(r"\d+", texto)
print(numeros)