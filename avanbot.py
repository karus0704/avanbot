import discord
import datetime
from captcha.image import ImageCaptcha
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("'아반 도움말' 명령어 입력")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("아반 프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 별명", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 도움말"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="< 아반 도움말 >\n\n개인정보", value="`아반 이메일`, `아반 만든이`, `아반 누구야`, `아반 서버주소`", inline=False)
        embed.add_field(name="재미", value="`아반 안녕`, `아반 바보`, `아반 잘생겼다`, `아반 천재다`, `아반 잘가`, `아반 못생겼다`, `아반 ㅉㅉ`, `아반 한심하다`", inline=False)
        embed.add_field(name="미니게임", value="`아반 캡챠`", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 이메일"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="< 아반 이메일 >\n\n만든이 이메일", value="Gmail : karusgame074@gmail.com\nNaver : karusgame074@naver.com", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 만든이"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="< 아반 제작자 >\n\n제작자 이름", value="`@에이큐#9034`", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 서버주소"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="< 아반 서버 주소 >\n\n서버 주소", value="아직 미완성 (완성 될 시 배포)", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 누구야"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="< 아반 누구야 >\n\n아반의 뜻", value="아무 뜻 없음", inline=False)
        embed.add_field(name="아반의 생일", value="이천십구년 십월 팔일이다", inline=False)
        embed.add_field(name="아반의 성별", value="남자도 아니고 여자도 아니다 그저 로봇이다", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 안녕"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="안녕하살법", value="반가워🖐", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 바보"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="바보라니", value="무지개 반사🌈", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 잘생겼다"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="잘생겼다고?", value="그건 어디서나 많이 들어😎", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 천재다"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="천재라고?", value="나는 말이야, 한살때부터 컴퓨터를 만졌어💻", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 잘가"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="안녕하살법 받아치기", value="잘가🖐", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 못생겼다"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="못생겼다고?", value="무지개 반사🌈", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 한심하다"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="한심하다고?", value="무지개 반사🌈", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 ㅉㅉ"):
        embed = discord.Embed(color=0xFF4C4C)
        embed.add_field(name="ㅉㅉ?", value="짱이라고? 알겠엉💖", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("아반 캡챠"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("시간이 지났다.. 아직 내 제자가 되려면 멀었군..")
            return

        if msg.content ==  a:
            await message.channel.send("척척박사 아반이 인정할 실력이군..")
        else:
            await message.channel.send("풉ㅋ 틀렸다고 전해라~")


client.run("NjMxMDEyMTQyNTE0MDQ0OTI5.XZwp6A.kTzhnykMekZ00temqAaME-oMTyA")