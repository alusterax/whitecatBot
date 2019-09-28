import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord import Client
import pprint
import random

bot = commands.Bot(command_prefix = '!',case_insensitive=True)

#Token: https://discordapp.com/developers/applications/SuaAplicacao/bots
token = 'Insira token obtida acima aqui'

procurando = False
qtRuim = 1
limiar = 200

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Anime Ban 3mod'))
    print('WhiteCat entrou no jogo. Escondam suas waifus...')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, CommandNotFound):
        return await ctx.send(f'Comando não existe! Digite !comandos ou !commands para ver a lista de comandos')
    raise error

@bot.event
async def on_message(message):
    global procurando
    channels = ['liga-das-waifu','geral','mudamaidadm']
    comandosDisable = ['$mmk','$mmr','$im','$imar','$top','$tu','$mu','$mm','$k','$wl','$wish','$wr']
    comandosEnable = ['$w','$wg','$h','$hg','$wa','$ha','$mg','$m','$mb','$wb']

    if str(message.channel) in channels:
        if str(message.author.id != "539387420953542675"):
            if (str(message.content).strip() in comandosEnable):
                procurando = True
            if (str(message.content).strip() in comandosDisable):
                procurando = False

    if (procurando):
        if str(message.channel) in channels:
            #print(f'{message.author} escreveu: {message.content} | ID: {message.author.id} | Canal: {message.channel}, {message.channel.id}')
            await start(message)
    await bot.process_commands(message)

#Pessoais
@bot.command(aliases=['yuuzinho','chupa4567'])
async def yuzao(ctx):
    respostaYuzao = ['/r/osureport | Yuuzinho (Cheating). \nhttps://www.reddit.com/r/osureport/comments/ae1li3/osustd_yuuzinho_cheating/'
                        ,'727pp','chupa4567','Man if u think this guy is legit u stupid as fuck']
    await ctx.send(f"{random.choice(respostaYuzao)}")

@bot.command(aliases=['mouseeasy','pr7'])
async def alust(ctx):
    respostaAlust = ['Deus','#1 BR','Paulo Roberto','Meu pai','Vai te banir','Mercenário','Solteiro','Fica programando esse bot ao invés de streamar']
    await ctx.send(f"{random.choice(respostaAlust)}")

@bot.command(aliases=['gato'])
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
#------------------------------------------------------------------------------
#Utilidade
@bot.command(aliases=['comandos'])
async def commands(ctx):
    await ctx.send(f"DM enviada!")

    helpembed = discord.Embed(title = 'Comandos WhiteCat BOT',color=discord.Color.purple())
    #helpembed.set_author(name="Comandos:")
    helpembed.add_field(name="!comandos (!commands)", value="Desativa o tracking do bot",inline=False)
    helpembed.add_field(name="!mousepoints (!points, !mousepontos)", value="Diz a quantidade de mousepoints acumulados na stream",inline=False)
    helpembed.add_field(name="!rolls", value="Diz a quantidade de rolls ruins seguidos no #liga-das-waifu",inline=False)
    helpembed.add_field(name="!cat (!gato)", value='Envia um gif de gato aleatório',inline=False)
    helpembed.add_field(name="!barata", value="Envia a lendária gif das baratas",inline=False)
    helpembed.add_field(name="!alust, !yuzao, !animeban", value="Zoeira",inline=False)
    helpembed.add_field(name="!whitecat", value="Ativa o tracking do bot",inline=False)
    helpembed.add_field(name="!wcsleep", value="Desativa o tracking do bot",inline=False)
    helpembed.set_footer(text = 'Qualquer problema com o bot, mande uma mensagem pro alust, ele que roda essa bagaça.')
    helpembed.set_image(url="https://media.discordapp.net/attachments/539730926800994314/623568231625392128/image0.gif")

    await ctx.author.send(embed=helpembed)

@bot.command()
async def rolls(ctx):
    await ctx.send(f"{qtRuim} rolls ruins seguidos")

@bot.command(aliases=['mousepontos','points'])
async def mousepoints(ctx):
    #Pega ID do discord da pessoa que escreveu a mensagem, cruza na database de mousepoints e printa aqui ('👍')
    await ctx.send(f"em desenvolvimento...")

@bot.command()
async def whitecat(ctx):
    procurando = True
    await ctx.send("WhiteCat entrou no jogo. Escondam suas waifus...")

@bot.command()
async def wcsleep(ctx):
    procurando = False
    await ctx.send("WhiteCat vai descansar. Até mais...")
#------------------------------------------------------------------------------
#Zoeira
@bot.command()
async def barata(ctx):
    await ctx.send("https://media.discordapp.net/attachments/539730926800994314/623568231625392128/image0.gif")

@bot.command()
async def animeban(ctx):
    respostaAnimeban = ['https://www.twitch.tv/mouseeasy/clip/SavoryNastyTeaTF2John?filter=clips&range=all&sort=time','um dia...','671pp','04/03/2018']
    await ctx.send(f"{random.choice(respostaAnimeban)}")

#------------------------------------------------------------------------------
#Funções
async def start(message):
    global procurando,limiar,qtRuim
    if str(message.author.id == "539387420953542675"):
        for embed in message.embeds:
            name = embed.author.name
            content = embed.description
            try:
                kakera = extractKakera(content)
                #print('Meow')
                if (kakera>limiar):
                    print(f"{name} | Kakera: {kakera}")
                    #await message.add_reaction('👍')
                    if (qtRuim > 40):
                        await message.channel.send(f"Finalmente um roll decente")
                    if (kakera > 700):
                        await message.channel.send(f"Carai, {name}, {kakera} kakera!")
                    else:
                        await message.channel.send(f"Meow. {kakera} kakera!")
                    qtRuim = 0
                    procurando = False
                else:
                    print(f'Meow {qtRuim} rolls ruins')
                    qtRuim+=1
                    if notificaRuim(qtRuim):
                        await message.channel.send(f"Já foram {qtRuim} rolls ruins seguidos, porra meow!")
            except Exception as e:
                print("erro! ", str(e))

def extractKakera(mensagem):
    letraAnterior = ''
    idxInicio = 0
    idxFinal = 0

    for idx,letra in enumerate(mensagem):
        if (letra == '*' and letraAnterior == '*'):
            idxInicio = idx;
            break
        else:
            letraAnterior = letra

    for idx,letra in enumerate(mensagem):
        if (letra == '*' and letraAnterior == '*' and idx>idxInicio):
            idxFinal = idx;
            break
        else:
            letraAnterior = letra
    kakeraQtd = mensagem[idxInicio+1:idxFinal-1]
    return int(kakeraQtd)

def notificaRuim(qtRuim):
    if (qtRuim%40 == 0):
        return True
    else:
        return False

#Token: https://discordapp.com/developers/applications/SuaAplicacao/bots
bot.run(token)
