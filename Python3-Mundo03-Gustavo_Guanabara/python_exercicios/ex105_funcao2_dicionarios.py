# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*numero, situcao=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param numero: uma ou mais notas dos alunos(aceita várias notas).
    :param situação: valor opcional, informa a situação do aluno com base na sua média.
    :return: dicionário com várias informações sobre a situação da turma de alunos.
    """
    # ok = False
    alunos_informacoes = dict()
    alunos_informacoes["total"] = len(numero)
    alunos_informacoes["maior"] = max(numero)
    alunos_informacoes["menor"] = min(numero)
    alunos_informacoes["media"] = sum(numero) / alunos_informacoes["total"]
    if situcao:
        # ok = True
        # if ok:
        if alunos_informacoes["media"] >= 7:
            situcao = "BOA"
        elif alunos_informacoes["media"] >= 5:
            situcao = "RAZOÁVEL"
        else:
            situcao = "RUIM"
        alunos_informacoes["situação"] = situcao
    return alunos_informacoes


r1 = resposta = notas(5.5, 9.5, 10, 6.5, situcao=True)
r2 = resposta = notas(4, 3.5, 7, 6.5, 8, 6.5, situcao=True)
r3 = resposta = notas(5.5, 2.5, 3, 2, 0, 5.5, 6, situcao=True)
r4 = resposta = notas(5.5, 9.5, 10, 6.5, 9, 3.5, 7, 5.5, 8, 6.5)

print(
    f"""
        {r1},
        {r2},
        {r3},
        {r4}
"""
)
# help(notas)
