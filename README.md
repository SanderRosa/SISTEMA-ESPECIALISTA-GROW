# 🌱 Sistema Especialista GROW — Inteligência Artificial Simbólica para Cultivo Indoor

> Sistema especialista baseado em regras lógicas para automação e controle climático e hidropônico de cultivos indoor (grow rooms), desenvolvido em Python com persistência transacional em banco de dados SQLite.

---

## 📋 Visão Geral e Contexto de Engenharia

O **GROW** é um software de **Inteligência Artificial Simbólica** modelado sob o paradigma de **Sistemas Baseados em Regras (Rule-Based Systems)**. O sistema atua como o cérebro eletrônico de uma estufa automatizada de cultivo indoor de alta precisão.

Ao ler dados ambientais fornecidos por sensores analógicos de temperatura, umidade do ar, umidade do solo e tempo cronológico, o sistema processa um motor de inferência que avalia regras de tomadas de decisão estruturadas para coordenar múltiplos atuadores elétricos (luzes, bombas de água, exaustores e umidificadores).

---

## 🧠 Arquitetura de Inteligência Artificial Simbólica

Diferente de modelos de aprendizado de máquina (Machine Learning) probabilísticos modernos, a Inteligência Artificial Simbólica é determinística e baseia-se na manipulação explícita de símbolos e regras formais. O projeto é estruturado de forma desacoplada dividindo-se em:

1. **Base de Fatos (Fact Base):** Mapeada em `sistema.py`, representa o estado físico atual capturado pelos sensores (leituras de temperatura, umidade, etc.).
2. **Base de Conhecimento (Knowledge Base):** Mapeada em `regras.py`, armazena as regras lógicas condicionais estruturadas (SE-ENTÃO / IF-THEN) que definem os limites ideais de cultivo validados por especialistas agronômicos.
3. **Motor de Inferência (Inference Engine):** O núcleo lógico que avalia o estado atual da Base de Fatos contra as restrições da Base de Conhecimento, inferindo e disparando as ações de controle sequenciais corretas sem redundâncias ou estados concorrentes.

---

## 💾 Persistência de Alta Confiabilidade: Por que SQLite?

Para registrar e monitorar o histórico de variações ambientais da estufa, o projeto rejeita o uso de arquivos de texto comuns (`.txt` ou `.csv`). Em vez disso, implementa persistência via **SQLite3**, um motor de banco de dados relacional leve embutido diretamente no arquivo local (`grow.db`).

### Justificativas Técnicas do SQLite frente a Arquivos Planos (TXT/CSV):
* **Garantias ACID (Atomicidade, Consistência, Isolamento e Durabilidade):** Em sistemas de controle contínuo, uma queda de energia repentina durante uma operação de gravação em arquivo de texto corromperia todo o arquivo. O SQLite utiliza logs de transação que garantem a atomicidade (ou a escrita ocorre por completo ou nada é alterado), protegendo a integridade dos dados históricos.
* **Consultas Relacionais Estruturadas (SQL):** Permite realizar buscas complexas e agregadas no histórico temporal (ex: calcular médias de temperatura da última semana, máximas e mínimas, horas de iluminação ativa) com extrema facilidade de código e velocidade de execução.
* **Prevenção de Conflitos de Acesso:** O SQLite gerencia de forma segura as leituras e escritas concorrentes por travas de transação internas, impedindo colisões de dados.

---

## ⚙️ Lógica de Controle (Base de Regras)

O motor de inferência aplica a seguinte matriz lógica de regras:

| Sensor | Condição | Ação nos Atuadores |
|---|---|---|
| Temperatura do Ar | `> 28°C` | Ligar **Exaustor** (Resfriamento) |
| Temperatura do Ar | `< 22°C` | Desligar **Exaustor** |
| Umidade do Ar | `< 40%` | Ligar **Umidificador** |
| Umidade do Ar | `> 65%` | Desligar **Umidificador** |
| Sensor de Luminosidade / Hora | `6h às 18h` (Fotoperíodo) | Ligar **Luz de Cultivo** |
| Sensor de Luminosidade / Hora | Fora do intervalo | Desligar **Luz de Cultivo** |
| Umidade do Solo | `< 30%` (Solo Seco) | Ligar **Bomba de Irrigação** |
| Umidade do Solo | `> 60%` | Desligar **Bomba de Irrigação** |

---

## 🏗️ Estrutura do Projeto

```
SISTEMA ESPECIALISTA GROW/
├── main.py          # Ponto de entrada: loop de console para leitura de inputs
├── sistema.py       # Definição da classe SistemaEspecialistaGrow (Base de Fatos e Atuadores)
├── regras.py        # Base de Conhecimento: regras lógicas condicionais SE-ENTÃO
├── banco.py         # Camada de Persistência: conexões e transações SQL no SQLite
├── ver_dados.py     # Script utilitário para consulta SQL de histórico persistido
├── teste.py         # Script de testes unitários da lógica de regras e banco
├── interface.py     # Protótipo de interface visual de monitoramento
└── grow.db          # Arquivo do banco de dados relacional SQLite
```

---

## 🚀 Como Executar

### 1. Iniciar o sistema
```bash
python main.py
```

### 2. Informar as leituras no terminal
```text
Temperatura: 30
Umidade do ar: 35
Umidade do solo: 25
Hora: 10
```

### 3. Verificar o histórico gravado
```bash
python ver_dados.py
```
