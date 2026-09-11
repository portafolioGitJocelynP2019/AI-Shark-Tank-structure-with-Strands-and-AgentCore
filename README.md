# 🦈 AI Shark Tank: Multi-Agent System on AWS

[![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20AgentCore%20%7C%20DynamoDB-orange?logo=amazon-aws)](https://aws.amazon.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org)
[![Strands](https://img.shields.io/badge/Framework-Strands%20Agents-green)](https://github.com)

Un sistema multi-agente autónomo diseñado para evaluar, debatir y calificar ideas de startups en tiempo real, conectando la lógica de agentes conversacionales con analítica avanzada en **Amazon QuickSight Q**. 

Este proyecto fue creado para demostrar cómo llevar aplicaciones de Inteligencia Artificial Generativa de una simple prueba de concepto (PoC) a un entorno de producción *serverless* y escalable en AWS.

---

## 🏗️ Arquitectura de la Solución

La arquitectura separa el motor lógico de los agentes, la infraestructura de ejecución segura y la capa de analítica ejecutiva:

* **Cerebro y Razonamiento:** Modelos fundacionales alojados en **Amazon Bedrock** (Claude 3.5 Sonnet para razonamiento profundo y Claude 3 Haiku para tareas rápidas).
* **Orquestación:** SDK **Strands** operando bajo un patrón multi-agente (Swarm / Jerárquico) ejecutado sobre **Bedrock AgentCore Runtime**.
* **Persistencia:** Tabla de **Amazon DynamoDB** para almacenar los puntajes y veredictos en tiempo real mediante herramientas personalizadas con `boto3`.
* **Visualización y BI:** **Amazon QuickSight y QuickSight Q**, permitiendo realizar consultas en lenguaje natural sobre las decisiones del panel de IA.

---

## 📂 Estructura del Proyecto

* `src/`: Contiene el código fuente de los agentes, la lógica de orquestación y las herramientas de integración.
* `infrastructure/`: Plantillas de infraestructura como código (Terraform) para aprovisionar los recursos en AWS.
* `analytics/`: Esquemas de datos y configuraciones para conectar la persistencia con QuickSight.

---

## 🚀 Guía de Configuración y Ejecución Local

### Prerrequisitos
* Python 3.10 o superior instalado.
* Credenciales de AWS configuradas localmente (`aws configure`).
* Acceso habilitado a los modelos de Anthropic Claude en **Amazon Bedrock** (Región `us-east-1` o `us-west-2`).

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/ai-shark-tank.git](https://github.com/TU_USUARIO/ai-shark-tank.git)
cd ai-shark-tank
# AI-Shark-Tank-structure-with-Strands-and-AgentCore Estructura
ai-shark-tank/
├── .gitignore
├── README.md
├── requirements.txt
├── architecture.png
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agents.py
├── infrastructure/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
└── analytics/
    └── quicksight_dataset.json

   # Arquitectura
    <img width="1984" height="2152" alt="Gemini_Generated_Image_k8qqwgk8qqwgk8qq" src="https://github.com/user-attachments/assets/d5665373-eecb-4f3a-9c4b-9a7e408caf8d" />

