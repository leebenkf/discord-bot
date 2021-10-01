import discord
from discord.ext import commands

app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name, 'has connected to Discord!')
    await app.change_presence(status=discord.Status.online, activity=None)
    print("ready")

@app.event
async def on_member_join(message):
    await member.send("이서버에 오신걸 환영합니다 규칙 숙지해주시고 서버 멤버와 친해지길 바래요!")



@app.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!'or f'{ctx.author.mention}님!저는 오휳봇이에요!')

@app.command(aliases=['gugudan'])
async def 구구단(ctx):
    await ctx.send('아러알ㅇㄹㄹ')

@app.command(aliases=['와'])
async def 샌즈(ctx):
    await ctx.send('샌즈!')
    

@app.command(aliases=['아시는'])
async def 샌즈2(ctx):
    await ctx.send('구나!')

@app.command(aliases=['도움말'])
async def 기능(ctx):
    await ctx.send('개발중')





  
app.run('ODkyMzMxMjExNzU2ODA2MTQ0.YVLWMw.5okhiS09ZNJMG8Bh_-oLQq0C9Ak')
