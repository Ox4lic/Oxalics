import requests
import syncio
import socket
import asyncio
import ssl
import logging
from concurrent.futures import ThreadPoolExecutor
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# Discord bot token
TOKEN = 'MTExNDg0MjcxNDYxNDI4ODQ3NA.Gb-rBH.18MI8FqqErJfpZEssm8oJahXw5CEhELgpLEDqg'

# Define the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 936619743392459%7C3cdb3f896252a1db29679cb4554db266&message=%7B%22app_id%22%3A%22936619743392459%22%2C%22app_uid%22%3A%22299191629%22%2C%22app_ver%22%3A%221.0.0%22%2C%22claims%22%3A%5B%22hmac.AR0T0Gsp8VzrAUtsZ-GlgYV_dxsINWHJN3nkAVeEikqs38bO%22%5D%2C%22data%22%3A%5B%7B%22extra%22%3A%7B%22reason%22%3A%22autoplay%22%2C%22seq_num%22%3A9%2C%22time%22%3A0%2C%22m_pk%22%3A%223343823361413428125_47307390712%22%2C%22a_i%22%3A%22organic%22%2C%22a_pk%22%3A%2247307390712%22%2C%22is_dash_eligible%22%3A1%2C%22nav_chain%22%3A%22PolarisFeedRoot%3AfeedPage%3A1%3Avia_cold_start%22%2C%22pk%22%3A%22299191629%22%2C%22playback_format%22%3A%22progressive%22%2C%22time_spent_id%22%3A%22k4bufb%22%2C%22tracking_token%22%3A%22eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTc4Zjg4ZTAyZWI5NGU1ZmE1ZGE2NjhlMTI3NjQ3YTQzMzQzODIzMzYxNDEzNDI4MTI1Iiwic2VydmVyX3Rva2VuIjoiMTcxMjkzMjQ4MTc5MXwzMzQzODIzMzYxNDEzNDI4MTI1fDI5OTE5MTYyOXxkMzFiYmE5MzYyZTQ4MTc3YmZkN2ViZjlkZjJmYjk0ZWFjYjRiOTA0OGRjM2EzYWUyZTA5NzYwODYzYjdkMDc1In0sInNpZ25hdHVyZSI6IiJ9%22%7D%2C%22name%22%3A%22video_should_start%22%2C%22time%22%3A1712932683.74%2C%22module%22%3A%22feed_timeline%22%7D%2C%7B%22extra%22%3A%7B%22follow_status%22%3A%22not_following%22%2C%22loop_count%22%3A0%2C%22m_ts%22%3A1712834869%2C%22playing_audio%22%3A1%2C%22radio_type%22%3A%22none-none%22%2C%22seq_num%22%3A10%2C%22timeAsPercent%22%3A0%2C%22m_pk%22%3A%223343823361413428125_47307390712%22%2C%22a_i%22%3A%22organic%22%2C%22a_pk%22%3A%2247307390712%22%2C%22is_dash_eligible%22%3A1%2C%22nav_chain%22%3A%22PolarisFeedRoot%3AfeedPage%3A1%3Avia_cold_start%22%2C%22pk%22%3A%22299191629%22%2C%22playback_format%22%3A%22progressive%22%2C%22time_spent_id%22%3A%22k4bufb%22%2C%22tracking_token%22%3A%22eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTc4Zjg4ZTAyZWI5NGU1ZmE1ZGE2NjhlMTI3NjQ3YTQzMzQzODIzMzYxNDEzNDI4MTI1Iiwic2VydmVyX3Rva2VuIjoiMTcxMjkzMjQ4MTc5MXwzMzQzODIzMzYxNDEzNDI4MTI1fDI5OTE5MTYyOXxkMzFiYmE5MzYyZTQ4MTc3YmZkN2ViZjlkZjJmYjk0ZWFjYjRiOTA0OGRjM2EzYWUyZTA5NzYwODYzYjdkMDc1In0sInNpZ25hdHVyZSI6IiJ9%22%7D%2C%22name%22%3A%22video_buffering_started%22%2C%22time%22%3A1712932683.742%2C%22module%22%3A%22feed_timeline%22%7D%5D%2C%22device_id%22%3A%223BA7953B-BDFD-47F2-97CB-031D6399C0E0%22%2C%22log_type%22%3A%22client_event%22%2C%22seq%22%3A8%2C%22session_id%22%3A%22%3A8w99c6%3Ak4bufb%22%7D',
    'Cookie': 'sessionid=299191629%3ANQlXfROnb4Q59t%3A18%3AAYcmG7Tn__pSe7fuv0T1QFlK1UJKF3J7f3N0TnNZOA',
    'Referer': 'https://help.instagram.com/contact/1784471218363829',
    'Origin': 'https://www.instagram.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    # Add other headers as needed
}

# Define the base data for the form
base_data = {
    'name': 'Oxalic Media Agency',
    'support_form_id': '1784471218363829',  # This might change, check the actual value
    'support_form_locale_id': 'en_US',  # This might change, check the actual value
    # Add other form fields as needed
}

# Define the number of submissions for each country
submissions_per_country = {'UAE': 1000, 'France': 500}

# Function to submit the form
def submit_form(username, email, country):
    # Update the base data with user-specific information
    base_data['username'] = username
    base_data['email'] = email
    
    # Update the country-specific data
    country_data = {
        'Field236858559849125_iso2_country_code': 'AE' if country == 'UAE' else 'FR',
        'Field236858559849125': country,
        # Add other country-specific data here
    }
    
    # Merge base data with country-specific data
    data = {**base_data, **country_data}
    
    
    # Define the URL for the request
    url = 'https://help.instagram.com/ajax/help/contact/submit/page'
    
    try:
        # Send the POST request
        response = requests.post(url, headers=headers, data=data)

        # Check if the request was successful
        if response.status_code == 200:
            return True
        else:
            return False

    except Exception as e:
        print(f"Error submitting form for {country}: {e}")
        return False

# Discord bot command
@bot.command()
async def submit_form(ctx, username, email, country):
    # Submit the form
    success = submit_form(username, email, country)
    
    if success:
        await ctx.send(f"Form submitted successfully for {username} with email {email}!")
    else:
        await ctx.send("Failed to submit the form. Please try again later.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!submit_form'):
        # Extract username, email, and country from the user's message
        try:
            _, username, email, country = message.content.split()
        except ValueError:
            await message.channel.send("Invalid format! Please provide your username, email, and country.")
            return
        
        # Submit the form
        success = await submit_form(username, email, country)
        
        if success:
            await message.channel.send("Form submitted successfully!")
        else:
            await message.channel.send("Failed to submit the form. Please try again later.")

@bot.event
async def on_ready():
    print(f' Activated {bot.user}')

# Run the Discord bot
bot.run(TOKEN)