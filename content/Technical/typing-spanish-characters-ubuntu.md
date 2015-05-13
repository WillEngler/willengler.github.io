---
layout: post
title: How to Type Spanish Accents on Ubuntu 14.04 (Trusty Tahr)
author: Will Engler
tags: español
date: 2015-05-08 10:08:30
---

Because I live on my computer, I want to type in Spanish as I learn.
I'm thinking of writing some Python scripts as little Spanish exercises, like a converter from integers to their Spanish representation.

But before I do fun Spanish computer things, I need to be able to type Spanish correctly!
Here is what I've figured out so far on Ubuntu 14.04, using the standard GNOME window manager.

### Changing The Keyboard

First, you need to select a keyboard with Spanish characters.
Go to system Settings -> Keyboard -> Typing -> Text Entry.
Or, if you have your keyboard layout in your upper status bar, click on it and select Text Entry Settings.
Then, under the "Input Sources to Use" box, click the + button and select English(US International with dead keys).

### Teclas Muertas

What is a dead key?
Under these settings, the apostrophe (') and backtick (`) become dead keys. 
So if you press one of these keys and then, say, the letter a, you will see á.

But how do you write backticks and apostrophes?
I'm sure there is an elegant way to do it, but I don't know how.
By default, typing '-' gives me a Spanish apostrophe (I think): ´.

To work around this, in Keyboard Settings -> Shortcuts, I set "Alternative Characters Key" to Right-Alt.
So if I want to enter an apostrophe, I type Right_Alt-'.
If I want to type a quotation mark, I type Right_Alt-Shift-".
It also gives me a way to enter accented characters without the dead keys.
For example, Right_Alt-a gives á.

### Can I Do Better?

Probably, but this will do for now.
I'll update later if I find something less janky.