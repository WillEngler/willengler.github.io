---
layout: post
title: SICP Book Club: 4.1 (How Does An Interpreter Work?)
author: Will Engler
tags: sicp
date: 2015-05-25 15:00:30
---

> The metacircular representation of truth might not be the same as that of the underlying Scheme.
> In this case, the language being implemented and the implementation language are the same. 
> Contemplation of the meaning of `true?` here yields expansion of consciousness without the abuse of substance.
>> Abelson & Sussman

I've been dying to see how an interpreter works, so when this happened...

![Interpreter Output](/images/sicp/victory.png)

... I pumped my fists in the air and hollered.
This confused the other guests at the fine Hostel Mamallena in Boquete, Panama.

I annotated the code provided in the text with comments to make sure I knew what was going on at each step. 
(You can check it out [here](https://github.com/WillEngler/sicp-solutions/blob/master/C4/book-interpreter.scm).)

I only encountered a few hiccups when I tried to get it running.
You can't load the procedures in the order they're presented in the text.
Most notably, you need to load in something like 
`(define apply-in-underlying-scheme apply)(define apply-in-underlying-scheme apply)`
early on so that you can use the underlying Scheme's `apply` after you clobber it with your own.
Not knowing which `apply` was in play led to some interesting debugging.

Understanding a working interpreter was the takeaway I most wanted out of SICP.
So I'm going to give the rest of Chapter 4 and Chapter 5 the same cursory treatment I gave Chapters 2 and 3.
I could easily pour a few weeks into all of the exercises and I'm sure I'd get a ton out of it.
But I'm too hype to write some Rust to focus on SICP for too long.