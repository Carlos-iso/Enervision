---
⚡ EnerVision

Sistema Inteligente de Monitoramento e Otimização Energética

EnerVision é um sistema em Python que simula e monitora o consumo energético de uma residência em tempo real, utilizando sensores virtuais por cômodo e uma IA adaptativa baseada em estatística para detectar anomalias, prever picos de demanda e otimizar o consumo de energia.

O projeto foi desenvolvido para rodar em ambientes leves como Termux, sem dependências pesadas como scikit-learn, mantendo foco em eficiência, clareza e portabilidade.
---

🎯 Objetivos do Projeto

Monitorar o consumo energético em tempo real

Simular sensores energéticos por cômodo da casa

Detectar anomalias de consumo

Prever picos de demanda

Aplicar otimizações automáticas

Manter histórico de consumo por cômodo

Promover uso eficiente e sustentável da energia

---

🧠 Inteligência Artificial (IA)

A IA do EnerVision é estatística e adaptativa, utilizando:

Média móvel

Desvio padrão

Z-Score para detecção de anomalias

Análise de tendência para previsão de consumo

Regras inteligentes para otimização preventiva

➡️ Não utiliza bibliotecas externas de machine learning, garantindo compatibilidade total com Termux e ambientes restritos.

---

🏠 Sensores Virtuais

Cada cômodo da casa funciona como um sensor energético

O consumo:

Possui inércia

Oscila de forma realista

Nunca sofre variações bruscas irreais

Cada sensor respeita uma potência máxima configurável

Histórico individual é mantido para cada cômodo

---

🗂️ Estrutura do Projeto

```
enervision/
│
├── src/
│ ├── main.py # Loop principal do sistema
│ ├── sensores.py # Sensores por cômodo e simulação de consumo
│ ├── relatorios.py # Interface de exibição no terminal
│ └── ia/
│ └── enervision_ai.py # IA adaptativa do sistema
```

---

⚙️ Funcionamento Geral

1. Os cômodos são cadastrados com sua potência máxima

2. A cada ciclo:

O consumo de cada cômodo é atualizado

O consumo total da casa é calculado

A IA analisa o histórico

3. A IA:

Prevê o próximo consumo

Detecta anomalias

Decide se deve otimizar

4. O sistema exibe:

Consumo atual

Consumo otimizado

Alertas inteligentes

Histórico por cômodo

---

📊 Informações Exibidas

Consumo total da residência

Consumo otimizado pela IA

Previsão da próxima leitura

Alertas de pico de demanda

Alertas de anomalia

Histórico recente por cômodo

Consumo atual de cada cômodo

---

🖥️ Execução do Projeto

Requisitos

Python 3.10+

Nenhuma dependência externa

Executar

python main.py

Compatível com:

Linux

Windows

macOS

Termux (Android)

---

🌱 Sustentabilidade e Impacto

O EnerVision demonstra como tecnologias simples e acessíveis podem:

Reduzir desperdícios energéticos

Antecipar falhas

Melhorar eficiência energética

Apoiar decisões sustentáveis

Servir como base para sistemas reais de smart grid e smart homes

---

🚀 Possíveis Evoluções

Interface gráfica (GUI ou Web)

Persistência de dados em banco

Integração com sensores reais (IoT)

Machine Learning avançado (ambientes compatíveis)

Controle automático de dispositivos

Dashboards em tempo real

---

👨‍💻 Autor

Projeto desenvolvido para fins educacionais, técnicos e de portfólio, com foco em engenharia de software, eficiência energética e inteligência artificial aplicada.

---

```

```
