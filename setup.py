import discord
from discord.ext import commands
import os
app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name, 'has connected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")


@app.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!'or f'{ctx.author.mention}님!저는 숟밥봇이에요!')

@app.command(aliases=['gugudan'])
async def 구구단(ctx):
    await ctx.send('아러알ㅇㄹㄹ')

@app.command(aliases=['와'])
async def 샌즈(ctx):
    await ctx.send('샌즈!')
    

@app.command(aliases=['아시는'])
async def 샌즈2(ctx):
    await ctx.send('구나!')



@app.event
async def on_member_join(member):
  fmt = '{1.name} 에 오신걸 환영합니다, {0.mention} 님'
  channel = member.server.get_channel1("channe1_id_here")
  await clinet.send_mssage(channel, fmt.format(member, member. server))

access_token = os.environ["BOT_TOKEN"]
app.run(access_token)


