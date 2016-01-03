---
layout: post
title: My First Step in OSS: Improving Rust's Regular Expressions
author: Will Engler
tags: rust
date: 2015-06-06 17:00:30
---

I've been itching for a while to contribute to an OSS project that I can get fired up about.
Over the last year, Rust has caught my attention.
So when Rust hit 1.0 last month, I decided it was time to make my mark.

Stepping into a big project is intimidating, so I thought it might be helpful for other newcomers and project maintainers if I record my impressions along the way.

### Step 1: Find Somewhere to Start

I poked around some issues on Github and came across [this one](https://github.com/rust-lang/regex/issues/66).
I've been curious to learn more about regexes and automata, it was unclaimed, and improving the regex library could make a lot of programs more efficient.
So rust-lang/regex #66 it is.

I emailed [Andrew Gallant aka BurntSushi](http://blog.burntsushi.net/) - who has written much of the regex library - and he was very helpful in pointing me in the right direction.
Both he and [Carl Lerche](https://github.com/carllerche/), another Rustacean working on automata, kindly offered to field any questions via IRC.
The Rust community's reputation of being welcoming to newcomers has been borne out by my experience so far.

### Step 2: Get Some Context (Why Do We Want a DFA Matcher?)

The issue's title reads "Implement a DFA matcher."
Andrew has already implemented an NFA matcher.
While I recalled the correspondence between regular languages and finite automata from university,
I didn't understand why we might prefer DFA's in some cases and NFA's in others.

I started with [_Mastering Regular Expressions_](http://regex.info/book.html).
It was a good refresher on regexes from a user's perspective.
It's overview of the differences in behavior between NFA and DFA engines was particularly helpful.
For example, I did not know about the "Longest-Leftmost" rule
(that DFA engines and POSIX-compliant NFA engines will always match the longest possible substring).

To get a little background on the implementation of regex matchers, I consulted ["The Dragon Book"](http://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools).
It was a big help later on.

Another helpful resource is [a series of blog posts by Russ Cox on implementing fast regex matchers](https://swtch.com/~rsc/regexp/).
Cox implemented the C++ "RE2" engine that Rust's regex engine is modeled after.
Cox makes a strong case for using a non-backtracking (two-stack) implementation for NFA simulators.
Andrew has already implemented the NFA simulation algorithm that Cox recommends.
Cox goes on to explain how using a lazily constructed DFA when appropriate can yield more performance improvements.
Best of all, he walks through some implementation details and RE2 is [open source](https://github.com/google/re2). 
Gold mine!

### Step 3: Code Archaeology

Convinced that a DFA matcher is a good thing to have in a regex library, I needed to come up with an implementation strategy.
Andrew recommended I start by taking a look at Carl Lerche's [automaton library](https://github.com/carllerche/automaton).
Carl had already implemented DFA construction, so maybe we could reuse his code.
I needed to get the lay of the land of both libraries and see if I could bridge them.
Thankfully, Andrew and Carl write clean code, so it was straightforward to navigate.

I came to the conclusion that reusing Carl's code was not the way to go (at the moment).
To keep with the design decisions of the library so far, I'll need to reimplement the lazy DFA construction of RE2.
I'll point you [here](https://github.com/rust-lang/regex/issues/66#issuecomment-110025224) if you want the gory algorithmic details.

### Step 4: Start Coding

Well, not quite.
I need to take a closer look at Cox's implementation of the lazy DFA matcher and at the existing rust-lang/regex code.
Then once I have a better idea of what I need to write, I can get cracking on writing a simple match-only DFA engine to start.

As Andrew has noted, this is an ambitious project for a Rust newbie.
So it should be a fun adventure!