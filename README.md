# MARKET POINT OF INTEREST JOURNAL

This script is meant to aid in trade management/organization. It acts as a journal that simplifies
writing down points of interest in any market.

*POI = Point of Interest*

**NOTES:**
* Currently includes functionality for only the top 100 crypto coins as of October 20.

**Instructions:**
1. Run the script with the 'write' argument after the file name. You can then input which assets you would like to track
   alongside their corresponding point of interests (potential buying/selling zones).
2. Run the script with no argument (or with the optional 'read' argument). This will show your previously written POI's
   alongside a comparison with the current market price (this is accompanied with variables that state whether or not
   you are below bidPOI/above askPOI and whether you are within 3% of your point of interest).
3. Run the script with the 'update' argument whenever you would like to edit individual assets or add assets without changing
   yuor previously written Assets/POI's.


## Current functionality:
**READ MODE**: Reads out the POI's you have added previously to the script. Only works if you have
previously added POI's using this script. Will then compare your bidPOI's and askPOI's to the current price
and state whether you are below your bidPOI or above your askPOI and also whether you are within 3% of your stated POI's.

**UPDATE MODE**: Updates individual assets with new POI's and leaves the rest alone. If asset is not
found, you will be asked whether or not you would like to include the asset into your POI's.

**WRITE MODE**: Run this if you have never ran this script before. This mode lets you chose which assets
you would like to include and adds functionality for adding their POI's. If you already have POI's, this
mode will wipe your previous POI's and run the previously stated functionality. type 'q' to quit this mode.


**Incoming functionality:**
* Alert System (Will alert you if a certain threshold has been passed or if you are within a certain
percentage amount of a threshold.)


