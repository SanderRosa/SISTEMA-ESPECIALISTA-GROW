class SistemaEspecialistaGrow:
    def __init__(self, temperatura, umidade, umidade_solo, hora, estado):
        self.temperatura = temperatura
        self.umidade = umidade
        self.umidade_solo = umidade_solo
        self.hora = hora
        self.estado = estado
        self.acoes = []

    def ligar(self, equipamento):
        if not self.estado[equipamento]:
            self.estado[equipamento] = True
            self.acoes.append(f"Ligar {equipamento}")
        else:
            self.acoes.append(f"Manter {equipamento} ligado")

    def desligar(self, equipamento):
        if self.estado[equipamento]:
            self.estado[equipamento] = False
            self.acoes.append(f"Desligar {equipamento}")
        else:
            self.acoes.append(f"{equipamento} já desligado")