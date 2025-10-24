# Twitch Gifted Sub Organizer

#### A lightweight Python GUI tool that helps Twitch moderators organize incoming gifted subscriptions for giveaways that use a wheelspin. Copy the output and place it into any online wheelspinner!

#### Needs a specific format of gifted subs that are in a different file to intake properly. Chatterino has filters to create the specific format needed of incoming gifted subs that can then be used for this program. 

## Features:
* Parses a text file that contains the gifted subs messages.

* Lets user define how many gifted subs = 1 giveaway entry.

* Displays the usernames on seperate lines in a scrollable window. Each username is written the appropriate amount of times for entry weights.

* Optional buildable as a standalone `.exe` for non-technical users.


### Example Input (In Seperate File):
```
alex_jazzy is gifting 10 Tier 1 Subs to KaiCenat's community! They've gifted a total of 16 in the channel!
brandono760 is gifting 5 Tier 1 Subs to KaiCenat's community! They've gifted a total of 17 in the channel!
bigashnotthelittleone is gifting 5 Tier 1 Subs to KaiCenat's community! They've gifted a total of 5 in the channel!
```

### Example Output (5 Gifted = 1 Entry Here)

```
alex_jazzy
alex_jazzy
brandono760
bigashnotthelittleone
```

### Requirements:
* Python 3.9+
* Tkinter (Already built into Python)

* To install dependencies: `pip install -r requirements.txt`

### How to Run For Experienced Users:

```
python main.py
```

### For Non-Tech Users: Build as EXE

```
pip install pyinstaller
pyinstaller --noconsole --onefile main.py
```
### License
Distributed under the MIT License. See `LICENSE` for more information.









