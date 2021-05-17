> **✅ StyxLauncher Support**

# DisCoordinates
Sends your Minecraft coordinates via key press to a Minecraft webhook.
This basically is just an updated version of my project https://github.com/nsde/MineCords

No mods, no client, no plugins, no resourcepack, no anything. Just this program and **Minecraft 1.13+** (lower versions don't work!).

# How to create a Discord webhook
1. Go to a Discord channel whose you have the permissions to add webhooks ("intergrations") to (to make sure, please test this out in a server where you have admin). I recommend creating a new channel and name it "mc-coordinates" or something like that, so the users know that the channel is about.

2. Go to the channel settings and you should have a **Intergrations** tab, if not, you don't have the permission to create webhooks (ask your server owner).

3. Click **View Webhooks** and **New webhook** at the top.

4. Give your Webhook a name (you can name it as your project) and make sure the correct channel is selected. You can also pick a image to make it look cooler. 


# How to install
1. Install the exe in the releases tab (recommended and easy) or a source code zip (experienced users only, you will need to install the pip packages listed in requirements.txt).

2. Create a `.env`-file in the same directory as the exe (if you downloaded a source zip, try to put it into the same folder as the `.py` files).

3. **For owners:**
If you are the owner of the Minecraft project or world and haven't already created a webhook, follow the tutorial above and make sure to copy the webhook URL!

    **For members:**
    Ask a owner for the webhook URL. 

4. Create a `.env`-file in the same directory as the code, or, it it doesn't work, the directory above with the following content (you need to change it, obviously):

***

```
AUTHOR=YOUR_MINECRAFT_NAME_HERE
WEBHOOK=YOUR_WEBHOK_URL_HERE
POPUP=FULL_OR_ON_OR_OFF
```


**AUTHOR**: your Minecraft username.

**WEBHOOK**: the Discord channel URL you just copied.

**POPUP**: the behaviour of the popup showed to name a position. It is recommended to turn this to full, so your friends know what location you just copied, but if you are really lazy, just turn it off. See below:

> `FULL`: focus the window. WINDOWS 10 ONLY!

> `ON`: open the popup in background

> `OFF`: don't ask for a position name 


**Example:**
```
AUTHOR=onlixx
WEBHOOK=https://discord.com/api/webhooks/000000000000000000/THIS_IS_JUST_AN_EXAMPLE_DONT_COPY_PASTE_THIS_ENV_CODE_IT_WONT_WORK__
POPUP=FULL
```

***

5. Save the `.env` file you just created & have fun!

# How to use

1. Run the exe (or if you are using the source zip, discoordinates/discoordinates.py)

2. Open up Minecraft if it's not opened up already, play any world or server you want to and press F3+C (only those keys, no other keys!). This should, depending on your env configuration, open up a popup (FULL), open a popup in the background (ON) or just set the name to "Position" (OFF).

    Make sure to select a name  if you didn't set the popup mode to OFF, because otherwise it won't send the message. Click the button saying "Send" (DONT USE ENTER IN THE PROGRAM, THIS MIGHT CRASH IT!).

3. Now, a message should be sent to a Discord webhook, and a message should appear in the connected channel displaying information about your current location and dimension.

# Help
If you have any problems, make sure you are using **Windows 10** (if you set the popup mode to FULL), and you didn't press the enter key in the popup (if you didn't set the popup mode to OFF). Additionally, **check your `.env`** file.

If your **game crashes** when pressing F3+C, check your Minecraft version is above 1.13! Check https://minecraft.fandom.com/wiki/Debug_screen#History for info.