import discord
from discord.ext import commands
from discord import Client
import pprint
import random

bot = commands.Bot(command_prefix = '!')

#Token: https://discordapp.com/developers/applications/SuaAplicacao/bots
token = 'Insira token obtida acima aqui'

procurando = False
qtRuim = 0
limiar = 200

@bot.event
async def on_ready():
    print('WhiteCat entrou no jogo. Escondam suas waifus...')

@bot.event
async def on_message(message):
    global procurando
    #Customize os canais dos servidores em que você quer monitorar mensagens
    channels = ['liga-das-waifu','geral']
    comandosDisable = ['$mmk','$mmr','$im','$imar','$top','$tu','$mu','$mm','$k']

    if str(message.channel) in channels:
        if (message.content.find('!alust') != -1):
            responstaAlust = ['Deus','#1 BR','Paulo Roberto','Meu pai','Vai te banir','Mercenário','Solteiro','Fica programando esse bot ao invés de streamar']
            print('alust')
            await message.channel.send(f"{random.choice(responstaAlust)}")

    if str(message.channel) in channels:
        if (message.content.find('!yuzao') != -1):
            responstaYuzao = ['/r/osureport | Yuuzinho (Cheating). \nhttps://www.reddit.com/r/osureport/comments/ae1li3/osustd_yuuzinho_cheating/','727pp','chupa4567']
            print('yuzao')
            await message.channel.send(f"{random.choice(responstaYuzao)}")

    if str(message.channel) in channels:
        if (message.content.find('!cat') != -1):
            print('gato')
            await message.channel.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    if str(message.channel) in channels:
        if (message.content.find('!whitecat') != -1):
            procurando = True
            await message.channel.send("WhiteCat entrou no jogo. Escondam suas waifus...")

    if str(message.channel) in channels:
        if (message.content.find('$w') != -1):
            if (message.content.find('$wish') != -1 or message.content.find('$wl') != -1):
                procurando = False
            else:
                procurando = True

    if str(message.channel) in channels:
        if (message.content.find('!wcsleep') != -1):
            procurando = False
            await message.channel.send("WhiteCat vai descansar. Até mais...")

    if str(message.channel) in channels:
        for comando in comandosDisable:
            if (message.content.find(comando) != -1):
                procurando = False

    if (procurando):
        if str(message.channel) in channels:
            #print(f'{message.author} escreveu: {message.content} | ID: {message.author.id} | Canal: {message.channel}, {message.channel.id}')
            await start(message)
            

async def start(message):
    global procurando,limiar,qtRuim
    #Verifica se é mudamaid
    if str(message.author.id == "539387420953542675"):
        for embed in message.embeds:
            content = embed.description
            try:
                kakera = extractKakera(content)
                #print('Meow')
                if (kakera>limiar):
                    print(message.content)
                    print(f'Kakera: {kakera}')
                    #Se quiser que o bot adicione reações, descomente a linha abaixo, só aceita emotes unicode.
                    #await message.add_reaction('👍')
                    if (qtRuim > 40):
                        await message.channel.send(f"Finalmente um roll decente")
                    if (kakera > 700):
                        await message.channel.send(f"Carai, {kakera} kakera!")
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

#Token: https://discordapp.com/developers/applications/626067378400133141/bots
bot.run(token)
