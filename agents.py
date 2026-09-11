import json
import boto3
from strands import Agent, Tool
from strands.llms import AmazonBedrock

# Inicializamos el modelo (Claude 3.5 Sonnet en Bedrock)
llm = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0")

# --- Herramientas (Tools) ---
def guardar_analisis_quicksight(nombre_startup: str, puntaje_tec: int, puntaje_biz: int, veredicto: str):
    """Guarda los resultados en DynamoDB para que QuickSight Q los consuma."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SharkTankEvaluations')
    table.put_item(
        Item={
            'startup_id': nombre_startup,
            'tech_score': puntaje_tec,
            'business_score': puntaje_biz,
            'decision': veredicto,
            'timestamp': '2026-08-06T12:00:00Z' # En prod usar datetime.now()
        }
    )
    return "Datos guardados exitosamente para QuickSight."

tool_quicksight = Tool.from_function(guardar_analisis_quicksight)

# --- Definición de Agentes (Strands) ---

# Agente 1: El Arquitecto (Técnico)
tech_agent = Agent(
    name="Arquitecto_Cloud",
    role="Analizas la viabilidad técnica, arquitectura y stack de la startup.",
    instructions="Eres un experto en AWS. Critica la arquitectura. ¿Es escalable? ¿Es segura? Devuelve un puntaje del 1 al 10 y un análisis corto.",
    llm=llm
)

# Agente 2: El Inversor (Negocio)
business_agent = Agent(
    name="Inversor_Tiburon",
    role="Analizas el modelo de negocio, TAM (Mercado) y ROI.",
    instructions="Eres un inversor agresivo. ¿Cómo hacen dinero? ¿El mercado es grande? Devuelve un puntaje del 1 al 10 y un análisis corto.",
    llm=llm
)

# Agente 3: El Orquestador
orchestrator_agent = Agent(
    name="Mr_Wonderful_AI",
    role="Líder del panel. Tomas las opiniones de los otros agentes y decides si inviertes.",
    instructions="""
    Coordina con Arquitecto_Cloud e Inversor_Tiburon. 
    1. Pide la evaluación técnica.
    2. Pide la evaluación de negocio.
    3. Toma una decisión final (Inversión o Rechazo).
    4. Usa la herramienta 'guardar_analisis_quicksight' para guardar los datos.
    """,
    llm=llm,
    tools=[tool_quicksight],
    sub_agents=[tech_agent, business_agent] # Patrón Swarm/Jerárquico en Strands
)

# Ejecución de prueba
if __name__ == "__main__":
    pitch = """
    Nuestra startup es un SaaS de IA para veterinarias. Usamos una base de datos local en Excel y 
    cobramos $5 USD al mes. Queremos $1 Millón de dólares por el 5%.
    """
    resultado = orchestrator_agent.run(f"Evalúa este pitch: {pitch}")
    print(resultado)
