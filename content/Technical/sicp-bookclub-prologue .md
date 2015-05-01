---
layout: post
title: SICP Book Club: Prologue (Hello, Scheme!)
author: Will Engler
tags: sicp
date: 2015-04-30 09:48:32
---

>People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells.
>> SICP Chapter 1

Damn. That sentence gets to the heart of what fires me up about programming.
You type some cryptic nonsense and direct a machine to do your bidding.

Today I'm going to pause at the introduction to make sure we know how to issue our spells.

### Installing Scheme

I just used my Linux distro's package manager: `sudo apt-get install mit-scheme`.

### Running Scheme

After installation, you can start up a REPL in your terminal with the `scheme` command.
That isn't terribly exciting.
To be true LISP wizards, we'll need to learn some dark magic.

### Down the Rabbit Hole with Emacs

Uh-oh, are we using Emacs?
The crazy person's text editor with the infamous squiggly learning curve?

![Because I must.](http://mrozekma.com/editor-learning-curve.png)

Well, I'll be trying it out.
Here's why:

* It was made in LISP, for LISP.
It's regarded as _the_ development environment for LISP.

* I like the REPL state of mind.
To my understanding, a big reason why LISP programmers are productive in Emacs is that it lets them write some code, evaluate an expression real quick to get the lay of the land, and keep going.
I really like REPL-heavy workflows.
I find writing Python more pleasurable when I'm bouncing back and forth between an iPython notebook and my editor.
The biggest selling point of Emacs for me is that it was designed for this type of development.

### How Do I Emacs?

I lack the hubris to write my own Emacs tutorial.
Instead, I'll point you to [one by Jess Hamrick that I found really helpful](http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/).

I'm using the [Prelude](https://github.com/bbatsov/prelude) setup. 
Supposedly it adds lots of good defaults, but I don't know enough about what's going on to appreciate Prelude's choices.
But it does give me a really nice color scheme!
Coding in style is _vital_, dear reader.


In large part for my own reference, here's how I get a session started:

* `emacs my-file.scm &` to open emacs in a background process.
* If I have a .scm file opened, Emacs knows to enter scheme mode.
* `C-x 3` to make a second window, split vertically.
* Then I need to start a REPL like so: `M-x run-scheme`.

And here are some of the commands I've learned so far that are a little less common than say, opening a file or copying and pasting.

* `C-x o` to switch to the **o**ther window.
* `C-c C-l` to **l**oad the scheme file I'm editing into the REPL.
* `C-x C-e` to **e**xecute the nearest expression in the REPL. (This command is gold!)
* `C-M-f, C-M-b` move **f**orwards and **b**ackwards over sexps.
  
It's humbling to struggle with a text editor.
I hope it pays off.