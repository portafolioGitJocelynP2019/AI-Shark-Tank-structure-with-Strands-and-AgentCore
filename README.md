
# 🦈 AI Shark Tank: Multi-Agent System on AWS
Bienvenido a la demo interactiva. Este proyecto usa **Strands Agents** y **Amazon Bedrock AgentCore** Community Day Argentina.

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
<img width="1984" height="2152" alt="Gemini_Generated_Image_k8qqwgk8qqwgk8qq" src="https://github.com/user-attachments/assets/a259f66a-1cd9-483a-bdde-409738f0b4b8" />

---

## 📂 Estructura del Proyecto

```text
ai-shark-tank/
├── src/
│   └── lambda_function.py       # Lógica Multi-Agente (Strands SDK + boto3)
├── infrastructure/
│   └── infrastructure.yaml      # Plantilla AWS CloudFormation (IaC)
├── requirements.txt             # Dependencias (strands-agents, boto3)
└── README.md                    # Documentación del proyecto
---
# 🦈 AI Shark Tank - Multi-Agent System (AWS)

## Requisitos
- Python 3.10+
- AWS CLI configurado
- Acceso a Amazon Bedrock y AgentCore

## ¿Cómo desplegar con AI (Cursor/Claude)?
Dado que eres desarrollador/arquitecto, puedes pedirle a tu IDE (Cursor) o a Claude lo siguiente:

> "Actúa como experto en AWS CDK. Conviérteme el código de `agents.py` en un despliegue de AWS usando **AgentCore Runtime**. Necesito una tabla DynamoDB llamada 'SharkTankEvaluations' y los roles de IAM necesarios."

## Despliegue con AgentCore CLI
Si usas la CLI nativa de AgentCore:
```bash
# 1. Inicializa el proyecto
agentcore create --name shark-tank --no-agent

# 2. Despliega la infraestructura base
agentcore deploy

# 3. Empaqueta y sube tu código Strands al Runtime
# (AgentCore Runtime hospeda y escala el agente)
```

## Integración con QuickSight Q
1. Ve a la consola de **AWS QuickSight**.
2. Conecta QuickSight a **Athena** (vía S3) o directamente a tu exportación de DynamoDB.
3. Activa **QuickSight Q** (Preguntas en lenguaje natural).
4. Escribe en el buscador del Dashboard: *"Mostrar startups rechazadas por bajo puntaje técnico pero alto puntaje de negocio"*.
---
## 🚀 Guía de Configuración y Ejecución Local

### Prerrequisitos
* Python 3.10 o superior instalado.
* Credenciales de AWS configuradas localmente (`aws configure`).
* Acceso habilitado a los modelos de Anthropic Claude en **Amazon Bedrock** (Región `us-east-1` o `us-west-2`).

* 🚀 Guía de Despliegue Express
Sigue estos pasos para desplegar esta arquitectura en tu propia cuenta de AWS en menos de 10 minutos.

Requisitos Previos
Una cuenta de AWS.

Acceso habilitado a los modelos Claude 3.5 Sonnet y Claude 3 Haiku en Amazon Bedrock (Región us-east-1 o us-west-2).

Python 3.10+ instalado localmente.

Paso 1: Empaquetar el Código Fuente
Abre tu terminal, navega a la carpeta src/ e instala las dependencias directamente en la carpeta para crear el paquete de despliegue de Lambda:

Bash
cd src
pip install strands-agents boto3 -t .
zip -r deploy.zip .
(Conserva este archivo deploy.zip, lo necesitarás en el Paso 3).

Paso 2: Desplegar la Infraestructura (CloudFormation)
Inicia sesión en la consola de AWS y ve a CloudFormation.

Haz clic en Create stack (With new resources).

Sube el archivo infrastructure/infrastructure.yaml de este repositorio.

Nombra la pila AI-SharkTank-Stack y acepta los permisos de IAM en el último paso.

Espera a que el estado sea CREATE_COMPLETE. Ve a la pestaña Outputs y copia la URL de tu ApiGatewayUrl.

Paso 3: Subir la Lógica Multi-Agente
Ve al servicio AWS Lambda y busca la función creada (ej. SharkTankOrchestrator).

⚠️ Un detalle técnico importantísimo para AWS Lambda
Para que este .zip funcione a la perfección en la consola de AWS sin arrojar errores de "módulo no encontrado" (ModuleNotFoundError), recuerda que AWS Lambda necesita que las librerías físicas estén dentro del .zip.

Si descargas este archivo y lo subes directo a AWS, te dirá que no encuentra strands-agents. Para solucionarlo en tu computadora antes de subirlo:

Descomprime el deploy.zip que acabas de descargar en una carpeta vacía.

Abre la terminal en esa carpeta y ejecuta el comando de instalación para que descargue las dependencias ahí mismo:

Bash
pip install strands-agents boto3 -t .
Vuelve a comprimir todos los archivos de esa carpeta (el código y las carpetas nuevas que se crearon) en un nuevo .zip.

¡Ese es el .zip definitivo que subes a la consola de AWS!
### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/ai-shark-tank.git](https://github.com/TU_USUARIO/ai-shark-tank.git)
cd ai-shark-tank
