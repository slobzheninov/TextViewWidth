# TextViewWidth

 
Text View Width is a Glyphs app palette plugin that allows you to set the Text View width either with a slider or relative to the width of a given glyph (20 times width of glyph H, for example). It helps to avoid reflowing of the text when you switch between masters.

![TextViewWidth](https://user-images.githubusercontent.com/60325634/126040629-1d7e1890-9a84-436c-bcf1-943570d3b08c.png)


## Usage

The plugin uses the following format of the input: '20 H' or '15 space' etc., which means 20 times width of glyph H or 15 times the width of the space glyph.
You can also change the with simply with the slider or input a number value.
To turn the plugin off, leave the input empty. When empty, it shows the current value as the placeholder.

<img width="300" alt="Screen Shot 2022-01-06 at 18 10 07" src="https://user-images.githubusercontent.com/60325634/148466397-f9b16192-05a9-408d-888c-26b64ca10f6e.png">


## Known issues

When you change masters, for a second you see an extra frame before it applies the new width. I don’t know exactly what causes it, seems like that’s how Glyphs applies changes.


# License

Copyright 2021 Alex Slobzheninov (@slobzheninov).

Based on code samples by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License"); you may not use the software provided here except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
