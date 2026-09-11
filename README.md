# 🦈 AI Shark Tank - Multi-Agent System (AWS)

Bienvenido a la demo interactiva. Este proyecto usa **Strands Agents** y **Amazon Bedrock AgentCore**.

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
