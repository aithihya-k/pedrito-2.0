import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="pedrito ", intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')

@bot.command()
async def smack(ctx, member: discord.Member):
  # Replace 'your_image_url_here' with the URL of the image you want to use
  image_url = ('images/wakala.jpg')

  # Send a message with the smack text and image
  await ctx.send(f"*smacks {member.mention}*",
                 file=discord.File(image_url, filename="smack.gif"))


@bot.event
async def on_message(message):
  response = ""
  sad_words = [
    "sad", 
    "depressed", 
    "depression", 
    "anxious", 
    "anxiety", 
    "anxiety inducing", 
    "crisis",
    "panic"
    "panik",
    "panicking",
    "hate myself",
    "fear"
  ]
  
  encouraging_quotes = [
    "don't worry, things will get better :)",
    "you're stronger than you think!",
    "you're braver than you believe, stronger than you seem, and smarter than you think :)",
    "take a deep breath and focus on the positive.",
    "you're not alone, we're here for you!",
    "you're doing great, keep going!",
    "you're like a tornado in a trailer park, keep it up!",
    "when you're lost in the darkness, look for the light.",
    "you're the brightest star in the sky :)",
    "no one is you, and that's your superpower.",
    "you may be as brave as you make believe you are.",
    "don’t let anyone ever make you feel like you don’t deserve what you want.",
    "carpe diem. seize the day, boys. make your lives extraordinary.",
    "we don't stop."
    "you're stronger, you're smarter, you're better. YOU ARE BETTER!",
    "aim for the moon, if you miss, you'll land among the stars.",
    "NEVER BACK DOWN NEVER WHAT?"
  ]

  content = message.content.lower()
  if any(word in content for word in sad_words):
    encouraging_quote = random.choice(encouraging_quotes)
    await message.channel.send(encouraging_quote)

  await bot.process_commands(message)

  if message.author.bot:
    return
  content = message.content.lower()
  if "hi pedrito" in content:
    greetings = [
        "hello!",
        "'sup  :sunglasses:",
        "heyyy!",
    ]
    response = random.choice(greetings)
    await message.channel.send(response)

#AGENT WHISKEY BEGINS HERE
  if "agent whiskey!" in content:
    # Replace with the actual file paths or URLs of your Whiskey images
    whiskey_data = [
        {"type": "quote", "content": "Hello gorgeous! I'm Jack, what's your name? How would you like to ride home on a real cowboy? I got a six pack of cold ones on ice and my roomie's out all night so you can scream my name as loud as you need to, sugar!"},
        {"type": "image", "path": 'images/whiskey/whiskey1.jpg'},
        {"type": "quote", "content": "Looks like we're hookin' up with a chick at a rock concert, my favourite kind of mission  :smirk:"},
        {"type": "image", "path": 'images/whiskey/whiskey2.jpg'},
        # Add more entries as needed
    ]

    selected_data = random.choice(whiskey_data)

    if selected_data["type"] == "quote":
       response = selected_data["content"]
    elif selected_data["type"] == "image":
      image_file = discord.File(selected_data["path"])
      response = "agent whiskey, as requested  :relieved:"
    # Use the response variable to send the message
    await message.channel.send(response, file=image_file if "image_file" in locals() else None)
#AGENT WHISKEY ENDS HERE

#QUENTIN BECK BEGINS HERE
  if "quentin!" in content:
    # Replace with the actual file paths or URLs of your Whiskey images
    quentin_data = [
        {"type": "quote", "content": "Don't ever apologize for being the smartest one in the room."},
        {"type": "image", "path": 'images/quentin/quentin1.jpg'},
        {"type": "quote", "content": "I created Mysterio to give the world someone to believe in. I control the truth; Mysterio *is* the truth!"},
        {"type": "image", "path": 'images/quentin/quentin2.jpg'},
        # Add more entries as needed
    ]

    selected_data = random.choice(quentin_data)

    if selected_data["type"] == "quote":
       response = selected_data["content"]
    elif selected_data["type"] == "image":
      image_file = discord.File(selected_data["path"])
      response = "<:QUENTIN:937177066372214814>"
    # Use the response variable to send the message
    await message.channel.send(response, file=image_file if "image_file" in locals() else None)
#QUENTIN BECK ENDS HERE



# Run the bot with your token
bot.run(
    '################################')
