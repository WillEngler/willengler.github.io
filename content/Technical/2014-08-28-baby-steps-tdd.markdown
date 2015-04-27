---
layout: post
title: Baby Steps in Test Driven Development
date: 2014-08-28 9:07:30
tags: process
---

I Have a Tooling Problem
-----------------------------

Like most software developers, I’m picky about the tools I use. However, I tend to go too far. For example, I wanted to start a blog a year ago. Instead of finding the shortest path from A to B, I investigated many blogging solutions. Should I use Wordpress or should I exercise my coding skills by trying to build something myself? If I use Wordpress, do I arrange for hosting myself, or do I use an “all-in-one” provider? I spent so much time researching alternatives that I never wrote a blog.

This time, I was more pragmatic. The Computer Science Club’s web-savvy officers were using Jekyll for the club website, so I chose Jekyll for my personal site. Also, instead of styling the blog myself, I'm using an open source theme and only customizing the styling later if I feel the need. By dispensing with as many secondary technical concerns as possible, I can do what I set out to do: write.

Just Put on Your Shoes and Run
------------------------------

At my last job, I shared a cubicle with a [UX][uxdt] co-op named Laura. Just as I have a tooling problem, she has an exercise problem. When she wants to try a new sport, she researches it to death and never gets into it. I had mentioned my running habit to her and she wanted get started.

She researched extensively, watching Youtube videos on proper form, reading a guide to anatomy for runners, and buying new running gear. In my opinion, the _right_ way to start running is just to get out there and run. Run as far as you can until you’re too tired and then run a little farther the next time. Once you’re hitting 20 miles, you can start shopping for the funny water bottles that strap to your hands, but don’t overcomplicate matters by worrying about such details too soon. 

(Eventually, Laura did settle on a [program][zombies] that focused on incremntal improvement over doing everything at once.)

Getting Started with Test Driven Development
--------------------------------------------

I’ve been enamored with the idea of [Test Driven Development (TDD)][tdd] for a while now. For the uninitiated, the thrust of TDD is to write unit tests for your application code before you write the code itself. There are many benefits to this approach, but lots of people on the internet can [explain them][whytdd] better than I can.

I decided to use TDD for projects and examples in my Operating Systems class. I almost fell right into the trap of over-researching and under-executing. There are lots of frameworks out there, so I should find the best one for me, right?

Well, those frameworks are designed for professionals writing production-grade systems code. I am a student writing toy programs to better understand Linux. Starting out in TDD by adopting a full-featured framework would be like starting to run by waking up at 5 AM for a 10-mile uphill trail run. What I really need is a gentle jog around the block. I don’t need to do everything right; I just need to ease into the test-first mindset.

So, alongside my first Operating Systems programs, I’ll roll my own ultra-light-weight unit testing framework. I’ll only start considering other frameworks when I encounter problems that they solve. I’ll be sure to report here on how it turns out!

[uxdt]: http://en.wikipedia.org/wiki/User_experience_design
[zombies]: https://www.zombiesrungame.com/
[tdd]: http://en.wikipedia.org/wiki/Tdd
[whytdd]: http://martinfowler.com/bliki/TestDrivenDevelopment.html