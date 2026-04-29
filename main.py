from sistema import SistemaEspecialistaGrow
from regras import aplicar_regras
from banco import criar_banco, salvar_leitura

criar_banco()

temp = float(input("Temperatura: "))
umid = float(input("Umidade do ar: "))
solo = float(input("Umidade do solo: "))
hora = int(input("Hora: "))

estado = {
    "exaustor": False,
    "umidificador": False,
    "luz": False,
    "bomba_irrigacao": False
}

sistema = SistemaEspecialistaGrow(temp, umid, solo, hora, estado)

aplicar_regras(sistema)

print("\nAÇÕES:")
for acao in sistema.acoes:
    print("-", acao)

salvar_leitura(temp, umid, solo, hora, sistema.acoes)