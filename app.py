import gradio as gr
import random

def generar_codigo(prompt):
    prompt = prompt.lower()

    if "discord" in prompt:
        return """
# BOT DE DISCORD EN PYTHON

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola!")

bot.run("TU_TOKEN")
"""

    elif "html" in prompt:
        return """
<!DOCTYPE html>
<html>
<head>
<title>Mi Página</title>
<style>
body{
background:black;
color:lime;
font-family:monospace;
text-align:center;
padding:50px;
}
</style>
</head>
<body>
<h1>Hola Mundo</h1>
</body>
</html>
"""

    else:
        return f"""
# Código generado para:
# {prompt}

print("Proyecto generado correctamente")
"""

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Mi IA Programadora REAL")

    entrada = gr.Textbox(
        label="Pide cualquier proyecto",
        placeholder="Ejemplo: haz un bot de discord"
    )

    salida = gr.Code(
        label="Código generado",
        language="python"
    )

    boton = gr.Button("Generar")

    boton.click(
        fn=generar_codigo,
        inputs=entrada,
        outputs=salida
    )

demo.launch()