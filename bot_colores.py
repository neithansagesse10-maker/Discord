import os
import discord
from discord.ext import commands

# 1. Configuración de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ==========================================
# 2. SISTEMA DE ROLES POR REACCIONES
# ==========================================
ROLE_MAP = {
    "pink_1": 1559032859128373299, "pink_2": 1559004433063346247, "pink_3": 1559004470019489922, "pink_4": 1559032779172487168, "pink_5": 1559004588835868702,
    "blue_1": 1559004645450449017, "blue_2": 1559004729185406996, "blue_3": 1559032595159720028, "blue_4": 1559032661241106462, "blue_5": 1559004880587329617,
    "purple_1": 1559031796258308217, "purple_2": 1559031867213226044, "purple_3": 1559005075332923472, "purple_4": 1559005129905152000, "purple_5": 1559005190516903998,
    "red_1": 1559005287548190901, "red_2": 1559005328706899978, "red_3": 1559032098285821983, "red_4": 1559032153617076384, "red_5": 1559005444423290970,
    "yellow_1": 1559005500966707240, "yellow_2": 1559005550455291955, "yellow_3": 1559031928324096153, "yellow_4": 1559032001854574592, "yellow_5": 1559005820597968987,
    "orange_1": 1559005906996301985, "orange_2": 1559032315001315420, "orange_3": 1559032258990575688, "orange_4": 1559006162819612712, "orange_5": 1559006217458941963,
    "green_1": 1559006290267742268, "green_2": 1559006362846109847, "green_3": 1559032413802201168, "green_4": 1559032499936563290, "green_5": 1559006498854797402,
    "white": 1559006646661943386, "grey": 1559006743550234725,
}

MENSAJES_ROLES = {}

# ==========================================
# 3. EVENTOS
# ==========================================
@bot.event
async def on_ready():
    print(f'Bot conectado exitosamente como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"¡Sincronizados {len(synced)} comandos Slash correctamente!")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return
    if payload.message_id in MENSAJES_ROLES:
        emoji = str(payload.emoji)
        mapping = MENSAJES_ROLES[payload.message_id]
        if emoji in mapping:
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(mapping[emoji])
            member = payload.member
            if role and member:
                await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id in MENSAJES_ROLES:
        emoji = str(payload.emoji)
        mapping = MENSAJES_ROLES[payload.message_id]
        if emoji in mapping:
            guild = bot.get_guild(payload.guild_id)
            role = guild.get_role(mapping[emoji])
            member = guild.get_member(payload.user_id)
            if role and member:
                await member.remove_roles(role)

# ==========================================
# 4. COMANDOS DE PANELES Y SYNC
# ==========================================
@bot.command(name="sync")
@commands.has_permissions(administrator=True)
async def sync_cmd(ctx):
    try:
        synced = await bot.tree.sync()
        await ctx.send(f"✅ ¡Se han sincronizado {len(synced)} comandos Slash correctamente!")
    except Exception as e:
        await ctx.send(f"❌ Error al sincronizar: {e}")

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_pink(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['pink_1']}>\n2. <@&{ROLE_MAP['pink_2']}>\n3. <@&{ROLE_MAP['pink_3']}>\n4. <@&{ROLE_MAP['pink_4']}>\n5. <@&{ROLE_MAP['pink_5']}>", color=0xE16C82)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['pink_1'], "2️⃣": ROLE_MAP['pink_2'], "3️⃣": ROLE_MAP['pink_3'], "4️⃣": ROLE_MAP['pink_4'], "5️⃣": ROLE_MAP['pink_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_blue(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['blue_1']}>\n2. <@&{ROLE_MAP['blue_2']}>\n3. <@&{ROLE_MAP['blue_3']}>\n4. <@&{ROLE_MAP['blue_4']}>\n5. <@&{ROLE_MAP['blue_5']}>", color=0x54B3DF)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['blue_1'], "2️⃣": ROLE_MAP['blue_2'], "3️⃣": ROLE_MAP['blue_3'], "4️⃣": ROLE_MAP['blue_4'], "5️⃣": ROLE_MAP['blue_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_purple(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['purple_1']}>\n2. <@&{ROLE_MAP['purple_2']}>\n3. <@&{ROLE_MAP['purple_3']}>\n4. <@&{ROLE_MAP['purple_4']}>\n5. <@&{ROLE_MAP['purple_5']}>", color=0x7851C8)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['purple_1'], "2️⃣": ROLE_MAP['purple_2'], "3️⃣": ROLE_MAP['purple_3'], "4️⃣": ROLE_MAP['purple_4'], "5️⃣": ROLE_MAP['purple_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_red(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['red_1']}>\n2. <@&{ROLE_MAP['red_2']}>\n3. <@&{ROLE_MAP['red_3']}>\n4. <@&{ROLE_MAP['red_4']}>\n5. <@&{ROLE_MAP['red_5']}>", color=0xBD1214)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['red_1'], "2️⃣": ROLE_MAP['red_2'], "3️⃣": ROLE_MAP['red_3'], "4️⃣": ROLE_MAP['red_4'], "5️⃣": ROLE_MAP['red_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_yellow(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['yellow_1']}>\n2. <@&{ROLE_MAP['yellow_2']}>\n3. <@&{ROLE_MAP['yellow_3']}>\n4. <@&{ROLE_MAP['yellow_4']}>\n5. <@&{ROLE_MAP['yellow_5']}>", color=0xF0D558)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['yellow_1'], "2️⃣": ROLE_MAP['yellow_2'], "3️⃣": ROLE_MAP['yellow_3'], "4️⃣": ROLE_MAP['yellow_4'], "5️⃣": ROLE_MAP['yellow_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_orange(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['orange_1']}>\n2. <@&{ROLE_MAP['orange_2']}>\n3. <@&{ROLE_MAP['orange_3']}>\n4. <@&{ROLE_MAP['orange_4']}>\n5. <@&{ROLE_MAP['orange_5']}>", color=0xC1451B)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['orange_1'], "2️⃣": ROLE_MAP['orange_2'], "3️⃣": ROLE_MAP['orange_3'], "4️⃣": ROLE_MAP['orange_4'], "5️⃣": ROLE_MAP['orange_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_green(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['green_1']}>\n2. <@&{ROLE_MAP['green_2']}>\n3. <@&{ROLE_MAP['green_3']}>\n4. <@&{ROLE_MAP['green_4']}>\n5. <@&{ROLE_MAP['green_5']}>", color=0x23C377)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['green_1'], "2️⃣": ROLE_MAP['green_2'], "3️⃣": ROLE_MAP['green_3'], "4️⃣": ROLE_MAP['green_4'], "5️⃣": ROLE_MAP['green_5']}

@bot.command()
@commands.has_permissions(administrator=True)
async def panel_neutros(ctx):
    embed = discord.Embed(description=f"1. <@&{ROLE_MAP['white']}>\n2. <@&{ROLE_MAP['grey']}>", color=0xFFFFFF)
    msg = await ctx.send(embed=embed)
    for e in ["1️⃣", "2️⃣"]: await msg.add_reaction(e)
    MENSAJES_ROLES[msg.id] = {"1️⃣": ROLE_MAP['white'], "2️⃣": ROLE_MAP['grey']}

# Ejecutar el bot
if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])