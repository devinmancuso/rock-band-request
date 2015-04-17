## rock-band-request

**What**

Python Selenium script that votes for a song for the next Rock band. User specifies song, artist and number of times to vote


**Why**

2. Why not

**Dependencies**

* Python 2.7
* [Click](http://click.pocoo.org/)
* Selenium WebDriver
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

**How**

1. Download script
2. Install dependencies

```bash
pip install selenium click 
```

You'll have to grab ChromeDriver and Python 2.7 manually.

3. Run the program

To run the program

`python voter.py`

You will be prompted to enter three pieces of information.

1. the number of times you want the bot to vote
2. the song name
3. the artist name

Spaces in song and artist names are fine. 

You can include these details as options to avoid having to fill them in each time. For example to start active players for the next week including today.

`python voter.py --votes=700 --song=Dont Go Breaking My Heart --artist=Elton John and Kiki Dee`

use `--help` for help documentation.

**To-Do**

- [ ] Try / Excepts for key UI elements to ensure Selenium can find them before we click them.
- [ ] Put more asserts in places to tighten it all up

**Contribute**

If you think this is a cool idea, but kind of inefficient, please submit a PR and let's make this better.

© 2015, Devin Mancuso · MIT License you know the deal. DBAD License superseeds
