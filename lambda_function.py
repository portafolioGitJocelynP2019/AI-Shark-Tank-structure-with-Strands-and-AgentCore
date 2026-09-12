import json
import boto3
import os
from strands import Agent, Tool
from strands.llms import AmazonBedrock

# 1. Inicializamos los modelos. Sonnet para razonar, Haiku para velocidad.
llm_orquestador = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0")
llm_tecnico = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0")
llm_rapido = AmazonBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0")

# 2. Herramienta para guardar en DynamoDB
def guardar_analisis_quicksight(nombre_startup: str, puntaje_tec: int, puntaje_biz: int, veredicto: str):
    """Guarda los resultados en DynamoDB para que QuickSight Q los consuma."""
    dynamodb = boto3.resource('dynamodb')
    # El nombre de la tabla lo pasaremos como variable de entorno desde CloudFormation
    table_name = os.environ.get('TABLE_NAME', 'SharkTankEvaluations') 
    table = dynamodb.Table(table_name)
    
    table.put_item(
        Item={
            'startup_id': nombre_startup,
            'tech_score': puntaje_tec,
            'business_score': puntaje_biz,
            'decision': veredicto
        }
    )
    return f"Datos guardados exitosamente para QuickSight. Veredicto: {veredicto}"

tool_quicksight = Tool.from_function(guardar_analisis_quicksight)

# 3. Definición de los Agentes
tech_agent = Agent(
    name="Arquitecto_Cloud",
    role="Analizas la viabilidad técnica, arquitectura y stack de la startup.",
    instructions="Eres un experto en AWS. Critica la arquitectura. ¿Es escalable? ¿Es segura? Devuelve un puntaje del 1 al 10 y un análisis corto.",
    llm=llm_tecnico
)

business_agent = Agent(
    name="Inversor_Tiburon",
    role="Analizas el modelo de negocio, TAM (Mercado) y ROI.",
    instructions="Eres un inversor agresivo. ¿Cómo hacen dinero? ¿El mercado es grande? Devuelve un puntaje del 1 al 10 y un análisis corto.",
    llm=llm_rapido
)

orchestrator_agent = Agent(
    name="Mr_Wonderful_AI",
    role="Líder del panel. Tomas las opiniones de los agentes y decides si inviertes.",
    instructions="""
    Coordina con Arquitecto_Cloud e Inversor_Tiburon. 
    1. Pide la evaluación técnica.
    2. Pide la evaluación de negocio.
    3. Toma una decisión final (Inversión o Rechazo).
    4. Usa la herramienta 'guardar_analisis_quicksight' para guardar los datos.
    """,
    llm=llm_orquestador,
    tools=[tool_quicksight],
    sub_agents=[tech_agent, business_agent]
)

# 4. El "Handler" que AWS Lambda ejecuta
def lambda_handler(event, context):
    try:
        # Extraemos el pitch que viene desde el API Gateway
        body = json.loads(event.get('body', '{}'))
        pitch = body.get('pitch', 'SaaS genérico de IA')
        
        print(f"Evaluando pitch: {pitch}")
        
        # Ejecutamos el enjambre
        resultado = orchestrator_agent.run(f"Evalúa este pitch de startup: {pitch}")
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'veredicto': str(resultado)})
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }