# 🌱 Sistema Especialista GROW — Inteligência Artificial Simbólica

Software de Inteligência Artificial Simbólica modelado sob o paradigma de Sistemas Baseados em Regras (Rule-Based Systems). Atua como o cérebro eletrônico automatizado e determinístico de estufas de cultivo indoor (grow rooms) de alta precisão agronômica.

## 🚀 Funcionalidades
- **Motor de Inferência Autônomo**: Capta a base de fatos (temperatura, umidade) e avalia rigidamente contra uma Base de Conhecimento, evitando os erros probabilísticos de redes neurais tradicionais.
- **Controle de Atuadores Climáticos**: Lógica de disparo programada para Exaustores, Umidificadores, Luzes de espectro e Bombas de Irrigação baseados nos limiares críticos.
- **Tolerância a Falhas de Energia**: Diferente de simples arquivos TXT, o sistema utiliza o motor transacional ACID do banco SQLite para garantir que os dados históricos não sejam corrompidos em quedas bruscas de luz.
- **Consultas Analíticas**: Ferramentas embutidas para análise de dados retroativos via SQL.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **SQLite3** (Driver de banco de dados relacional nativo, embarcado no código)
- **Lógica Simbólica (If-Then Rule Engine)** (Base de conhecimento hard-coded)

## ⚙️ Como Executar
1. O banco `grow.db` é criado automaticamente no diretório caso seja a primeira vez.
2. Inicie a simulação interativa via console executando:
   ```bash
   python main.py
   ```
3. Insira as variáveis ambientais (simulando sensores físicos) quando o terminal pedir (ex: Temperatura 30, Umidade 35).
4. O motor de inferência fará o cálculo e decidirá quais equipamentos ligar/desligar no instante.
5. Para consultar os logs e o histórico de decisões salvas em banco de forma persistente, rode:
   ```bash
   python ver_dados.py
   ```

## 📸 Demonstração
*(Espaço reservado para visualização das tabelas de decisão lógicas do sistema)*
