import gradio as gr


def generar(prompt, imagen=None):

    if not prompt:
        return "Escribe un proyecto"

    if "discord" in prompt.lower():
        lenguaje = "python"
        codigo = '''
# archivo: bot.py

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def saludo(ctx):
    await ctx.send(f"Hola {ctx.author.mention}")


bot.run(TOKEN)
'''
    else:
        lenguaje = "html"
        codigo = f'''
<!-- archivo: index.html -->

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{prompt}</title>

<style>
body {{
    background: linear-gradient(135deg,#0f172a,#1e3a8a);
    color:white;
    font-family:Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}}

button {{
    padding:20px 40px;
    border:none;
    border-radius:15px;
    background:#3b82f6;
    color:white;
    font-size:20px;
    cursor:pointer;
    transition:.3s;
}

button:hover {{
    transform:scale(1.1);
    box-shadow:0 0 30px #60a5fa;
}}
</style>

</head>
<body>

<button>Botón Animado</button>

</body>
</html>
'''

    return codigo, lenguaje


with gr.Blocks(
    theme=gr.themes.Soft(),
    title="Mi IA Programadora REAL"
) as demo:

    gr.Markdown("# 🚀 Mi IA Programadora REAL")
    gr.Markdown("### Pide cualquier proyecto")

    prompt = gr.Textbox(
        placeholder="Ej: hazme una página azul con botón animado"
    )

    imagen = gr.Image(type="filepath", label="Sube Imagen")

    salida = gr.Code(
        label="Código generado",
        language="python",
        lines=35
    )

    estado = gr.Textbox(label="Estado")

    boton = gr.Button("⚡ Generar")

    boton.click(
        fn=lambda p, i: (*generar(p, i), "Proyecto generado correctamente"),
        inputs=[prompt, imagen],
        outputs=[salida, salida.language, estado]
    )

demo.launch()