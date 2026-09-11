from strands import Agent, Tool
from strands.llms import AmazonBedrock

# 1. Definimos los motores de IA optimizados por caso de uso
llm_orquestador = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0")
llm_tecnico = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0") # O Llama 3.1 70B
llm_rapido = AmazonBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0")

# 2. Asignamos los modelos a los agentes
tech_agent = Agent(
    name="Arquitecto_Cloud",
    role="Analizas la viabilidad técnica...",
    llm=llm_tecnico # Modelo de alto razonamiento
)

business_agent = Agent(
    name="Inversor_Tiburon",
    role="Analizas el modelo de negocio...",
    llm=llm_rapido # Modelo rápido y eficiente en costos
)

orchestrator_agent = Agent(
    name="Mr_Wonderful_AI",
    role="Líder del panel. Decide e invoca herramientas.",
    llm=llm_orquestador, # Modelo experto en Tool Calling
    tools=[tool_quicksight],
    sub_agents=[tech_agent, business_agent]
)