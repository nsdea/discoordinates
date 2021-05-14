import os
import time
import tkinter
import keyboard
import pyperclip

from dotenv import load_dotenv
from dhooks import Webhook, Embed

def send(author, url, parsed, ask_name):
    author = author

    if parsed['dimension'] == 'overworld':
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_de_gamepedia%2F7%2F7c%2FGrasblock.png&f=1&nofb=1'
    
    elif parsed['dimension'] == 'the_nether':
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F0%2F02%2FNetherrack_JE4_BE2.png&f=1&nofb=1'
    
    elif parsed['dimension'] == 'the_end':
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fminecraft_gamepedia%2Fimages%2F4%2F43%2FEnd_Stone_JE3_BE2.png%2Frevision%2Flatest%2Fscale-to-width-down%2F1200%3Fcb%3D20200315175116&f=1&nofb=1'

    else:
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F7%2F76%2FImpulse_Command_Block.gif&f=1&nofb=1'

    hook = Webhook(url)

    def popup():
        win = tkinter.Tk()
        win.title('DisCoordinates')
        win.geometry('200x100')

        def done(pos):
            position = pos.get()
            win.destroy()
            globals()['posname'] = position
            return

        tkinter.Label(text='Give your position a name:').pack()

        pos = tkinter.Entry()
        pos.pack()
        
        tkinter.Button(text='Done', command=lambda: done(pos=pos)).pack()
        
        win.mainloop()

    globals()['posname'] = 'Position'

    if ask_name:
        popup()

    embed = Embed(
        description=globals()['posname'],
        color=0x00a5ff,
        timestamp='now'
    )

    embed.set_author(name=author)

    xyz = f"{parsed['x']} {parsed['y']} {parsed['z']}"

    embed.add_field(name='XYZ', value=xyz, inline=False)
    embed.add_field(name='Dimension', value=parsed['dimension'], inline=False)
    embed.set_footer(text='Sent by github.com/nsde/discoordinates')
    embed.set_thumbnail(img)

    hook.send(embed=embed)

def parse(command):
    parsed = {}

    parsed['dimension'] = command.split('minecraft:')[1].split()[0]
    parsed['x'] = command.split('@s ')[1].split()[0]
    parsed['y'] = command.split()[7]
    parsed['z'] = command.split()[8]
    parsed['look_x'] = command.split()[9]
    parsed['look_y'] = command.split()[10]

    return parsed

if __name__ == '__main__':
    load_dotenv()


    def run():
        author_name = os.getenv('AUTHOR')
        hook_url = os.getenv('WEBHOOK')
        ask_name = bool(os.getenv('ASK_NAME') == 'YES')

        command = pyperclip.paste()
        parsed = parse(command)
        send(author_name, hook_url, parsed=parsed, ask_name=ask_name)

    while True:
        keyboard.wait('F3+C')
        time.sleep(0.1)
        run()