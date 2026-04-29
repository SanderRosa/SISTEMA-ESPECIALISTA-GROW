# 🌱 Sistema Especialista GROW

> Sistema especialista baseado em regras para controle automatizado de ambiente de cultivo indoor (grow room), desenvolvido em Python.

---

## 🧠 Sobre o Projeto

O **GROW** é um sistema especialista que simula um controlador inteligente de ambiente para cultivo de plantas. Com base em leituras de sensores ambientais, o sistema aplica uma **base de regras SE-ENTÃO** para determinar quais dispositivos devem ser ligados ou desligados a fim de manter as condições ideais de cultivo.

---

## 🔧 Lógica de Controle (Base de Regras)

| Sensor | Condição | Ação |
|---|---|---|
| Temperatura | `> 28°C` | Liga **Exaustor** |
| Temperatura | `< 22°C` | Desliga **Exaustor** |
| Umidade do Ar | `< 40%` | Liga **Umidificador** |
| Umidade do Ar | `> 65%` | Desliga **Umidificador** |
| Hora do dia | `6h às 18h` | Liga **Luz** |
| Hora do dia | Fora do intervalo | Desliga **Luz** |
| Umidade do Solo | `< 30%` | Liga **Bomba de Irrigação** |
| Umidade do Solo | `> 60%` | Desliga **Bomba de Irrigação** |

---

## 🏗️ Estrutura do Projeto

```
SISTEMA ESPECIALISTA GROW/
├── main.py          # Ponto de entrada: coleta entradas e exibe ações
├── sistema.py       # Classe SistemaEspecialistaGrow (estado e atores)
├── regras.py        # Base de regras SE-ENTÃO
├── banco.py         # Persistência SQLite (criar banco e salvar leituras)
├── ver_dados.py     # Utilitário para visualizar dados históricos
├── teste.py         # Testes do sistema
├── interface.py     # Interface (WIP)
└── grow.db          # Banco de dados SQLite com histórico de leituras
```

---

## 🚀 Como Usar

### 1. Executar o sistema
```bash
python main.py
```

### 2. Informar as leituras dos sensores
```
Temperatura: 30
Umidade do ar: 35
Umidade do solo: 25
Hora: 10
```

### 3. O sistema exibe as ações recomendadas
```
AÇÕES:
- Ligar exaustor
- Ligar umidificador
- Ligar luz
- Ligar bomba_irrigacao
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| `Python 3` | Linguagem principal |
| `SQLite3` | Persistência do histórico de leituras |

---

## 📌 Conceitos Aplicados

- **Sistema Especialista** baseado em regras (Rule-Based Expert System)
- **Separação de responsabilidades**: regras, estado do sistema e persistência em módulos distintos
- **Persistência com SQLite** para histórico de acionamentos
