from dotenv import load_dotenv
import os
#TODO: change it into a class --> properties will be fine I believe

load_dotenv()


class ServerEvents:
    # maybe they will be necessary later on
    token: int = os.getenv('TOKEN')
    # does not work as an environment variable
    channel_id: int = os.getenv('CHANNEL_ID')
    guild: str = os.getenv('DISCORD_GUILD')

    def return_on_ready(bot, guild, channel_id):
        channel = bot.get_channel(channel_id)
        return channel.send (f'''Hi Everyone! {bot.user} has just connected to {guild}
Below you will find a list of commands that you can use:
showevents: returns a list of actions
showcommands: returns a list of commands''')

    def return_on_message(message):
        if message.content.startswith('showevents'):
            #TODO: after finishing complete the list
            list_of_actions = ['encourage', 'disappoint']
            return message.channel.send(list_of_actions)
        
        if message.content.startswith('showcommands'):
            #TODO: after finishing complete the list
            list_of_commands = '''A list of commands
'''
            return message.channel.send(list_of_commands)
        
        if message.content.startswith('$'):
            choices = ['encourage', 'disappoint']
            return message.channel.send(choices)
        
        if message.content.startswith('?'):
            return message.channel.send('Hello!')
        
    def return_on_editing(old_message, new_message, user):
        return new_message.channel.send(f'{user} has edited the message')
                                        
    def return_on_typing(channel, user, when):
        return channel.send(f'Hi {user}! How can I help you?')
      
    