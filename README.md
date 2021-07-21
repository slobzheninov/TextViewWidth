# TextViewWidth
 
Text View Width is a Glyphs app palette plugin that allows to set the Text View width relative to the width of a given glyph (20 times width of glyph H, for example). This means that the line breaks will appear about the same for all masters. The plugin dynamically updates the width.

![TextViewWidth](https://user-images.githubusercontent.com/60325634/126040629-1d7e1890-9a84-436c-bcf1-943570d3b08c.png)


## Usage

The plugin uses the following format of the input: '20 H' or '15 space' etc., which means 20 times width of glyph H or 15 times the width of the space glyph.

![image](https://user-images.githubusercontent.com/60325634/126040652-b8e1c324-b403-41e0-b6b3-3f8f49397dca.png)


You can also set the width in units (the same way as you do in Glyphs preferences), in this case simply insert a number.
To turn the plugin off, leave the input empty.


## Known issues

When you change masters, for a second you see an extra frame before it applies the new width. Which is of course annoying, WIP.


# License

Copyright 2021 Alex Slobzheninov (@slobzheninov).

Based on code samples by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License"); you may not use the software provided here except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
