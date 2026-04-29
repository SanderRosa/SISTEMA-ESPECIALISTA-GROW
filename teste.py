import random
from sistema import SistemaEspecialistaGrow
from regras import aplicar_regras
from banco import criar_banco, salvar_leitura

criar_banco()

estado = {
    "exaustor": False,
    "umidificador": False,
    "luz": False,
    "bomba_irrigacao": False
}

def gerar_dados():
    return (
        round(random.uniform(18, 32), 1),
        round(random.uniform(35, 75), 1),
        round(random.uniform(10, 80), 1)
    )

def monitorar(horas=24):
    hora = 0

    for _ in range(horas):
        temp, umid, solo = gerar_dados()

        sistema = SistemaEspecialistaGrow(temp, umid, solo, hora, estado)
        aplicar_regras(sistema)

        print(f"\nHora {hora}")
        print(f"T={temp} U={umid} Solo={solo}")

        for acao in sistema.acoes:
            print("-", acao)

        print("Estado:", estado)

        salvar_leitura(temp, umid, solo, hora, sistema.acoes)

        hora = (hora + 1) % 24


monitorar(24)