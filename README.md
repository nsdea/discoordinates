# DisCoordinates
Sends your Minecraft coordinates via key press to a Minecraft webhook.

# How to get started
1. Install the exe in the releases tab (recommended and easy) or a source code zip (python programming experienced users only, you will need to install the pip packages listed in requirements.txt).

2. Create a `.env`-file in the same directory as the exe (if you downloaded a source zip, try to put it into the same folder as the `.py` files).

3. Go to a Discord channel whose you have the permissions to add webhooks ("intergrations") to (to make sure, please test this out in a server where you have admin). I recommend creating a new channel and name it "mc-coordinates" or something like that, so the users know that the channel is about.

4. Go to the channel settings and you should have a **Intergrations** tab, if not, you don't have the permission to create webhooks (ask your server owner).

5. Click **View Webhooks** and **New webhook** at the top.

6. Give your Webhook a name and make sure the correct channel is selected. You can also pick a image to make it look cooler. 

7. Copy the webhook URL and paste it in the `.env`-file just like this:

```
AUTHOR=YOUR_MINECRAFT_NAME_HERE
WEBHOOK=YOUR_WEBHOK_URL_HERE
ASK_NAME=YES_OR_NO
```
**AUTHOR** is your Minecraft username.
**WEBHOOK** is the Discord channel URL you just copied.
**ASK_NAME** wether or not to ask for a name every single time for a position name. It is recommended to turn this on, so your friends know what location you just copied, but if you are really lazy, just turn it off.

Example:
```
AUTHOR=onlixx
WEBHOOK=https://discord.com/api/webhooks/000000000000000000/THIS_IS_JUST_AN_EXAMPLE_DONT_COPY_PASTE_THIS_ENV_CODE_IT_WONT_WORK__
```

8. Save the env and run the exe (or if you are using the source zip, discoordinates/discoordinates.py)