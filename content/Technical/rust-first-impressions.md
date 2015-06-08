---
layout: post
title: My First Step in OSS: Improving Rust's Regular Expressions
author: Will Engler
tags: rust
status: draft
date: 2015-06-05 13:00:30
---

> As a user, you don't care if it's regular, nonregular, irregular, or incontinent.
>> Jeffrey E. F. Friedl in _Mastering Regular Expressions_ on how NFA regex engines with backreferences aren't - mathematically speaking - regular.

I've been itching for a while to contribute to an OSS project that I can get fired up about.
Over the last year, Rust has caught my attention.
So when Rust hit 1.0 last month, I decided it was time to make my mark.

Stepping into an OSS project is intimidating, so I thought it might be helpful for other newcomers and even project maintainers if I record my impressions along the way.

### Step 1: Find Somewhere to Start

I poked around some issues on Github and came across [this one](https://github.com/rust-lang/regex/issues/66).
I've been curious to learn more about regexes and automata, it was unclaimed, and improving the regex library could make a lot of programs more efficient.
So rust-lang/regex #66 it is.

I emailed [Andrew Gallant aka BurntSushi](http://blog.burntsushi.net/) - who has written much of the regex library - and he was very helpful in pointing me in the right direction.
Both he and [Carl Lerche](https://github.com/carllerche/), another Rustacean working on automata, kindly offered to field any questions via IRC.
The Rust community's reputation of being welcoming to newcomers has been borne out by my experience so far.

### Step 2: Get Some Context (Why Do We Want a DFA Matcher?)

The issue's title reads "Implement a DFA matcher."
Andrew has already implemented an NFA engine.
While I recalled the correspondence between regular languages and finite automata from university,
I didn't understand why we might prefer DFA's in some cases and NFA's in others.

I started with [_Mastering Regular Expressions_](http://regex.info/book.html).
It was a good refresher on regexes from a user's perspective.
It's overview of the differences in behavior between NFA and DFA engines was particularly helpful.
For example, I did not know about the "Longest-Leftmost" rule
(that DFA engines and POSIX-compliant NFA engines will always match the longest possible substring).

To get a little background on the implementation of regex engines, I consulted ["The Dragon Book"](http://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools).
I didn't read too deeply into the algorithms for DFA construction, but now I know where I can look.

My favorite resource so far is one that Andrew has highlighted on his blog: [a series of blog posts by Russ Cox on implementing fast regex matchers](https://swtch.com/~rsc/regexp/).
Russ implemented the [C++ RE2](https://github.com/google/re2) engine that Rust's regex engine is modeled after.
(I'd )