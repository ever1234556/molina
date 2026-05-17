def generar_codigo(prompt):
    prompt = prompt.lower()

    if "discord" in prompt:
        return '''
# ============================================
# BOT PROFESIONAL DE DISCORD EN PYTHON
# ============================================

import discord
from discord.ext import commands
import asyncio
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# --------------------------------------------
# EVENTOS
# --------------------------------------------

@bot.event
async def on_ready():
    print("="*50)
    print(f"BOT CONECTADO: {bot.user}")
    print(f"ID: {bot.user.id}")
    print("Estado: ONLINE")
    print("="*50)

@bot.event
async def on_member_join(member):
    canal = member.guild.system_channel
    if canal:
        await canal.send(f"Bienvenido {member.mention}")

# --------------------------------------------
# COMANDOS
# --------------------------------------------

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(bot.latency*1000)}ms")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola {ctx.author.mention}")

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Información del Bot",
        description="Bot avanzado generado por IA",
        color=0x8a2be2,
        timestamp=datetime.datetime.utcnow()
    )

    embed.add_field(
        name="Servidor",
        value=ctx.guild.name
    )

    embed.add_field(
        name="Usuarios",
        value=ctx.guild.member_count
    )

    await ctx.send(embed=embed)

@bot.command()
async def limpiar(ctx, cantidad: int):
    await ctx.channel.purge(limit=cantidad+1)

@bot.command()
async def ayuda(ctx):
    texto = """
!ping
!hola
!info
!limpiar 10
!ayuda
"""
    await ctx.send(texto)

# --------------------------------------------
# INICIAR BOT
# --------------------------------------------

bot.run("TU_TOKEN")
'''

    elif "html" in prompt:
        return '''
<!DOCTYPE html>
<html>
<head>
<title>Página Profesional</title>

<style>
body{
background:linear-gradient(135deg,#0f0f0f,#240046);
color:white;
font-family:Arial;
text-align:center;
padding:100px;
}

h1{
font-size:70px;
animation: glow 2s infinite alternate;
}

@keyframes glow{
from{opacity:.5;}
to{opacity:1;}
}

button{
padding:20px 50px;
border:none;
border-radius:20px;
font-size:25px;
cursor:pointer;
background:purple;
color:white;
}
</style>
</head>

<body>

<h1>Proyecto Avanzado</h1>
<p>Generado por IA profesional</p>

<button onclick="alert('Hola mundo')">
Haz clic
</button>

</body>
</html>
'''

    else:
        return f'''
# ============================================
# PROYECTO GENERADO POR IA
# ============================================

Solicitud:
{prompt}

Explicación:
Este proyecto fue creado automáticamente por la IA.

Características:
- Código limpio
- Estructura profesional
- Fácil de editar
- Escalable
- Buen rendimiento

print("Proyecto generado correctamente")
'''