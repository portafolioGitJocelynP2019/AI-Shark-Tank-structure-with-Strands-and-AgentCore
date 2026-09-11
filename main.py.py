import os
from strands import Agent
from strands.llms import AmazonBedrock

# Le decimos al código qué región usar (cambia a us-west-2 si habilitaste los modelos ahí)
os.environ["AWS_DEFAULT_REGION"] = "us-east-1" 

print("Conectando con Claude en Amazon Bedrock...")

# 1. Inicializamos a Claude 3.5 Sonnet
llm = AmazonBedrock(model_id="anthropic.claude-3-5-sonnet-20241022-v2:0")

# 2. Creamos al Agente Técnico
arquitecto = Agent(
    name="Arquitecto_Cloud",
    role="Eres un Arquitecto de Soluciones muy estricto y sarcástico.",
    instructions="Evalúa la tecnología de la idea. Sé crítico. No des más de 3 oraciones.",
    llm=llm
)

# 3. Creamos al Agente de Negocios
inversor = Agent(
    name="Inversor_Tiburon",
    role="Eres un inversor agresivo enfocado solo en el dinero y el mercado.",
    instructions="Evalúa si la idea hará dinero. Sé directo. No des más de 3 oraciones.",
    llm=llm
)

# 4. Creamos al Jefe (Orquestador)
orquestador = Agent(
    name="Mr_AI",
    role="Líder del panel. Tomas la decisión final de invertir o rechazar.",
    instructions="""
    Pide la opinión del Arquitecto_Cloud y luego la del Inversor_Tiburon. 
    Basado en sus respuestas, da un veredicto final.
    """,
    llm=llm,
    sub_agents=[arquitecto, inversor] # ¡Aquí los unimos en un enjambre!
)

# 5. ¡A probar la idea loca!
pitch = "Una app móvil en Excel que usa Bluetooth para traducir los ladridos de perro a lenguaje humano."

print(f"\n💡 Analizando Pitch: '{pitch}'\n")
print("El enjambre está debatiendo (esto puede tomar unos 10-15 segundos)...\n")

# Ejecutamos el agente principal
resultado = orquestador.run(f"Evalúa este pitch de startup: {pitch}")

print("--------------------------------------------------")
print("VEREDICTO FINAL:")
print("--------------------------------------------------")
print(resultado)