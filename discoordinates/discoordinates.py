import os
import time
import tkinter
import keyboard
import pyperclip
import webbrowser

import tkinter.messagebox

from dotenv import load_dotenv
from dhooks import Webhook, Embed
from mojang import MojangAPI

globals()['posname'] = 'Position'

def send(author, url, parsed, ask_name):
    color = 0x00a5ff
    img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F7%2F76%2FImpulse_Command_Block.gif&f=1&nofb=1'

    if parsed['dimension'] == 'overworld':
        color = 0x00ff1b
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_de_gamepedia%2F7%2F7c%2FGrasblock.png&f=1&nofb=1'
        
        if float(parsed['y']) > 160:
            color = 0x9ffdfc
            img = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.imgur.com%2FFbd0j.png&f=1&nofb=1'

        if float(parsed['y']) < 17:
            color = 0x485f5f
            img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2Fb%2Fb5%2FDiamond_Ore_JE3_BE3.png&f=1&nofb=1'

    if parsed['dimension'] == 'the_nether':
        color = 0x8c1f26
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F0%2F02%2FNetherrack_JE4_BE2.png&f=1&nofb=1'
        
        if float(parsed['y']) < 23:
            color = 0x352723
            img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F4%2F4c%2FAncient_Debris_JE1_BE1.png&f=1&nofb=1'

        if float(parsed['y']) > 126:
            color = 0x353535
            img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2F6%2F68%2FBedrock_JE2_BE2.png&f=1&nofb=1'

    if parsed['dimension'] == 'the_end':
        color = 0xcecc8e
        img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fminecraft_gamepedia%2Fimages%2F4%2F43%2FEnd_Stone_JE3_BE2.png%2Frevision%2Flatest%2Fscale-to-width-down%2F1200%3Fcb%3D20200315175116&f=1&nofb=1'

        if float(parsed['x']) > 200.0 or float(parsed['x']) < -200.0 or float(parsed['z']) > 200.0 or float(parsed['z']) < -200.0:
            color = 0x52208d
            img = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2Fa%2Fa7%2FChorus_Plant_JE2_BE2.png&f=1&nofb=1'


    hook = Webhook(url)
    hook_name = hook.get_info().default_name

    def popup(full='off'):
        win = tkinter.Tk()
        win.title('DisCoordinates')
        win.geometry('400x300')

        if full == 'on':
            keyboard.press_and_release('Alt+Tab')

        time.sleep(0.3)

        # win.lift()
        # win.attributes('-topmost', True)
        # win.after(1, lambda: win.focus_force())
        # win.after_idle(win.attributes,'-topmost',False)
        # win.focus_set()

        def done(pos):
            position = pos.get()
            globals()['posname'] = position

            win.destroy()

            time.sleep(0.5)

            keyboard.press('alt')
            time.sleep(0.1)
            keyboard.press('tab')
            time.sleep(0.1)
            keyboard.release('alt')
            time.sleep(0.1)
            keyboard.release('tab')
            time.sleep(0.1)
            keyboard.press_and_release('esc')

            return

        tkinter.Label(text='Give your position a name:', font=('Arial', 20)).pack()

        pos = tkinter.Entry(font=('Arial', 20))
        pos.pack()

        pos.focus_force()
        
        btn = tkinter.Button(text='Send', width=30, command=lambda: done(pos=pos), font=('Arial', 13, 'bold'))
        btn.pack()

        tkinter.Label(text='A webhook about your position,\ndimension and more will be sent as:').pack()
        tkinter.Label(text=hook_name, font=('bold')).pack()

        # keyboard.add_hotkey('enter', lambda pos=pos: done(pos=pos))
        
        win.mainloop()

    if ask_name == 'YES':
        popup(full='off')

    if ask_name == 'FULL':
        popup(full='on')

    embed = Embed(
        title=globals()['posname'],
        description='New position created',
        color=color,
        timestamp='now',
        url='https://github.com/nsde/discoordinates'
    )

    embed.set_author(name=author)

    xyz = f"{parsed['x']} {parsed['y']} {parsed['z']}"
    embed.add_field(name='XYZ', value=xyz, inline=False)

    if parsed['dimension'] not in ['the_nether', 'the_end', 'world_the_nether', 'world_the_end']:
        nether_xyz = f"{round(parsed['x']/8)} {parsed['y']} {round(parsed['z']/8)}"
        embed.add_field(name='Nether XYZ', value=nether_xyz, inline=False)
    
    elif parsed['dimension'] in ['the_nether', 'world_the_nether']:
        overworld_xyz = f"{parsed['x']*8} {parsed['y']} {parsed['z']*8}"
        embed.add_field(name='Overworld XYZ', value=overworld_xyz, inline=False)

    embed.add_field(name='Dimension', value=parsed['dimension'], inline=False)
    embed.set_footer(text='Sent by DisCoordinates')
    embed.set_thumbnail(img)

    hook.send(embed=embed, username=hook_name + ' | DisCoordinates')

def parse(command):
    parsed = {}

    if command.startswith('/execute in minecraft:'):
        try:
            parsed['dimension'] = command.split('minecraft:')[1].split()[0]
            parsed['x'] = command.split('@s ')[1].split()[0]
            parsed['y'] = command.split()[7]
            parsed['z'] = command.split()[8]
            parsed['look_x'] = command.split()[9]
            parsed['look_y'] = command.split()[10]
        except:
            print('ERROR - The command could not be recognized')
    else:
        print('ERROR - The copied text is not a command')

    return parsed


load_dotenv()

try:
   open('.env')
except:
    try:
        open('discoordinates/.env')
    except:
        print('ERROR - No valid .env file.')

        win = tkinter.Tk()
        win.title('DisCoordinates Setup')

        def helpsetup():
            tkinter.messagebox.showinfo('Info', 'Please ignore the sections telling you to create a .env file if this is the first time you get this popup.\n\nThis is because this setup will automatically create such file.')
            webbrowser.open('https://github.com/nsde/discoordinates/blob/main/README.md')

        tkinter.Button(win, text='Help', command=helpsetup).pack()

        tkinter.Label(win, text='\nYour Minecraft name:').pack()

        mcname = tkinter.Entry(win)
        mcname.pack()

        tkinter.Label(win, text='Webhook URL:').pack()

        hurl = tkinter.Entry(win)
        hurl.pack()

        tkinter.Label(win, text='Popup Mode:').pack()

        pmode = tkinter.Entry(win)
        pmode.pack()

        def setup():
            if not MojangAPI.get_uuid(mcname.get()):
                tkinter.messagebox.showerror('Error', 'Please input a correct Minecraft username.')
                return

            if not hurl.get().startswith('https://discord.com/api/webhooks/'):
                if tkinter.messagebox.askyesno('Warning', 'The entered Webhook URL does not seem correct. Try again?'):
                    return
            
            if not pmode.get() in ['FULL', 'ON', 'OFF']:
                tkinter.messagebox.showerror('Error', 'Popup Mode can only be FULL or ON or OFF.')
                return

            open('.env', 'w').write(f'''AUTHOR={mcname.get()}\nWEBHOOK={hurl.get()}\nPOPUP={pmode.get()}''')
            win.destroy()

        tkinter.Button(win, text='OK', command=setup).pack()

        win.mainloop()

def run():
    author_name = os.getenv('AUTHOR')
    hook_url = os.getenv('WEBHOOK')
    ask_name = os.getenv('POPUP')

    command = pyperclip.paste()
    parsed = parse(command)
    send(author_name, hook_url, parsed=parsed, ask_name=ask_name)

while True:
    if keyboard.is_pressed('F3') and keyboard.is_pressed('C'):
        time.sleep(0.1)
        run()