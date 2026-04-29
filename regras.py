def aplicar_regras(sistema):

    # TEMPERATURA
    if sistema.temperatura > 28:
        sistema.ligar("exaustor")
    elif sistema.temperatura < 22:
        sistema.desligar("exaustor")

    # UMIDADE DO AR
    if sistema.umidade < 40:
        sistema.ligar("umidificador")
    elif sistema.umidade > 65:
        sistema.desligar("umidificador")

    # ILUMINAÇÃO
    if 6 <= sistema.hora < 18:
        sistema.ligar("luz")
    else:
        sistema.desligar("luz")

    # 🌱 UMIDADE DO SOLO (NOVO)
    if sistema.umidade_solo < 30:
        sistema.ligar("bomba_irrigacao")
    elif sistema.umidade_solo > 60:
        sistema.desligar("bomba_irrigacao")