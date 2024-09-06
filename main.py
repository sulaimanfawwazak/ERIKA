import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import re
import random

emoji_begin = '\U0001F680'
emoji_error = '\U0001F4A5'
emoji_warning = '\U0001F6A8'
emoji_hint = '\U0001F4A1'
emoji_saving = '\U0001F4BE'
emoji_debug = '\U0001f514'
emoji_finish = '\U0001F3C1'
emoji_time = '\U0000231B'
emoji_chat = '\U0001F4AC'
emoji_calendar = '\U0001F4C5'
emoji_clock = '\U0001F550'
emoji_chart = '\U0001F4CA'
emoji_bye = '\U0001F44B'

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Reset to default color

# Find the .env file
load_dotenv('./.env')

# Load the token from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set the bot intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
client = commands.Bot(command_prefix="!", intents=intents)

# Event when the bot is ready
@client.event
async def on_ready():
  print(f'{GREEN}The bot is now ready for use! {emoji_begin}{RESET}')

# Pre-defined response lists
response_patterns = {
  r'\b(hello|hi|good morning|good afternoon|good night|excuse me)\b': [
    "Hello, how can I help you?",
    "Hi, there! How can I help you?",
    "Hello! How can I assist you today?"
  ],
  r'.*\b(game|product|board|beejoy)\b.*': [
    "BEEJoy is an interactive Snakes & Ladders board game designed to help parents interact with children."
  ],
  r'.*\b(rules|play)\b.*': [
    "Players roll the dice and move their tokens on the board. If they land on a BEE or JOY tile, they pick a corresponding card and start a conversation based on the card's prompt."
  ],
  r'.*\b(age|suitable|old)\b.*': [
    "The game is designed for children aged 4-12 years old or equivalent to elementary school."
  ],
  r'.*\b(appropriate|material|taboo|curriculum|syllabus)\b.*': [
    "We have been working together with a psychologist and practitioner in this field to develop and validate the syllabus to ensure it is appropriate for children."
  ],
  r'.*\b(how much|cost|price)\b.*': [
    "The board game is priced at IDR 550K."
  ],
  r'why .*\b(expensive|pricey)\b.*': [
    "The board game is crafted with high quality and premium materials to ensure it is safe for children and durable."
  ],
  r'.*\b(where|buy|purchase)\b.*': [
    "You can purchase the game through https://tokopedia.link/QKTdYNqwDMb or https://shopee.co.id/edusindonesia?categoryId=100639&entryPoint=ShopByPDP&itemId=28704565168."
  ],
  r'.*\b(bee|joy)\b.*(cards|card)\b.*': [
    "BEE Cards have conversation starters for child-parent interaction, while JOY Cards have prompts for educational conversation."
  ],
  r'.*super.*\b(bee|joy)\b.*': [
    "Super BEE and Super JOY are random challenges that can be accessed through https://edusindonesia.com as motoric exercises."
  ],
  r'.*(feature|features|anything else|another)\b.*': [
    "BEEJoy has numerous features, such as BEE Card, JOY Card, Super BEE, and Super JOY."
  ],
  r'.*what.*edus.*': [
    "Edus is an online-based parenting platform that helps parents prepare their children for a brighter future. Edus provides online video learning, articles, and online consultations with professionals that can be accessed through http://edusindonesia.com."
  ],
  r'.*(consult|consultation|consultations)\b.*': [
    "Book a consultation with professionals through http://wa.me/+6281225146029."
  ],
  r'.*(article|articles)\b.*': [
    "Access numerous articles written by professionals through https://edusindonesia.com."
  ],
  r'.*(video)\b.*': [
    "Access numerous online educational videos to improve parenting skills by subscribing through https://edusindonesia.com."
  ],
  r'.*(thanks|thank you|thankyou)\b.*': [
    "It's a pleasure! Anything else I can help with?",
    "You're welcome! Don't forget to follow our Instagram at @edus.id for daily parenting content."
  ],
  r'.*(bye|goodbye|ok|ty|cool|good|nice|great)\b.*': [
    f"Feel free to ask anything again {emoji_bye}",
    f"See you later! {emoji_bye}",
    f"Thank you! {emoji_bye}"
  ],
  r'.*help.*': [
    "I'm here to help! What do you need assistance with?"
  ],
  r'.*(hours|availability|when)\b.*': [
    "Our support team is available 24/7. How can we assist you today?"
  ],
  r'.*return.*': [
    "For return inquiries, please visit our returns page or contact customer support at our website page."
  ],
  r'.*shipping.*': [
    "We offer various shipping options. You can check our shipping policy on our website or contact us for more details."
  ],
  r'.*contact.*': [
    "You can reach us through our contact form on the website."
  ],
  r'.*/b(social media|instagram)/b.*': [
    "Find us on instagram at @edus.id"
  ],
  r'.*faq.*': [
    "You can find answers to frequently asked questions on our website page."
  ],
  r'.*website.*': [
    "Visit our website at https://www.edusindonesia.com/."
  ],
  r'\b!start\b': [""]
}


# `Else` Response lists
confused = ["I'm so sorry, but we currently don't have the information you're requesting. Anything else?", "Can you explain further?", "Sorry, could you please elaborate that?", "Sorry, what do you mean by that?", "I'm sorry I don't quite catch that", "I'm sorry, could you please elaborate it more?", "Sorry I don't quite understand, could you please elaborate it?", "Sorry, could you please rephrase it?", "I'm a little bit confused, what do you mean by it?", "Sorry, a little bit quite confused there. Would you please elaborate it more?"]

# Event listener for all messages
@client.event
async def on_message(message):
  # Checks if the message if from the bot itself or not to avoid loop
  if message.author == client.user:
    return
  
  print(f'[{emoji_chat}] DEBUG: {message.content}')
  
  pattern_matched = False
  for pattern, responses in response_patterns.items():
    if re.search(pattern, message.content, re.IGNORECASE):
      # Send the first matching response
      await message.channel.send(random.choice(responses) if isinstance(responses, list) else responses)
      pattern_matched = True
      break # Exit the loop once a match is found
    
  if not pattern_matched:
    await message.channel.send(random.choice(confused))
    # break
  
  # Make sure commands are still processed
  await client.process_commands(message)

client.run(BOT_TOKEN)
