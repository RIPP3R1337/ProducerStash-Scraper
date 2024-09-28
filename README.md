# ProducerStash-Scraper
Python scripts which will scrape the websites pages and download links.


## How does it work? 

It scans all url pages (as of currently what the website has to offer) and then proceeds to save those urls in a .txt files. Running the second python script will also scrape the mega download links from the website.

You could edit the script yourself too to your own liking. I'll probably update this till i can't or for when the website goes down. There might be a possibility that when it goes down the MEGA files go with it (But lets hope it wont) 

**Q: Why did you make this?**
- **A: Because i wanted the download links before the website might face a DMCA. Probably wont but you never know:)**
  
**Q: Do you take suggestions?**
- **A: Ofcourse! I would love suggestions i could add to this script**
  
---

### How do i use it?

1. Really simple! Now i'm not sure a default windows version without python would be able to run these but just in case download for windows: [Python](https://www.python.org/downloads/) here. MacOS here: [PythonMacOS](https://www.python.org/downloads/macos/)
2. Either download this repo as .zip or open your CMD/Powershell wherever you like and paste this:
```
git clone https://github.com/RIPP3R1337/ProducerStash-Scraper.git
```
4. Open CMD / Powershell in the directory these scripts are located.
5. pip3 install -r requirements.txt Just so we're making sure you have everything installed!
6. Type: `python3 scraper.py` and when that one is done do `python3 download-scraper.py`
7. These 2 should generate .txt files within the same directory. You're probably more interested in the download links .txt :)


If you really don't know what's going on, here a video:

[Tutorial](https://youtu.be/eJweV8OVT2E?si=8fKTurffVKdsOEW9) This should be almost identical to macOS / Linux.


---

**Planning to add:**
- Make it so we have one script rather than 2
- When you already did a scan and new stuff gets added to the website it will pull that rather than the files you've already scraped.
- ~~Dynamically search for website pages rather than hardcoding the pages urls~~


That should be all, enjoy these kits <3!
