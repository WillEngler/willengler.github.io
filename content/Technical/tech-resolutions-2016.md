---
layout: post
title: 2016 Technical Resolutions
author: Will Engler
tags: goals
date: 2016-01-02 14:40:30
---

Exercise more, learn a musical instrument, write better documentation.
New Years resolutions tend to slip, but I still like making them.
To help my follow-through, I'll set some tangible milestones.
I'll also identify what I can give up on to make room for the new commitments.

Here are my technical resolutions for 2016:

### 1: Attack My Ignorance

I've been in my new job as the lead engineer of [Plenario](plenar.io) for 4 months now.
There's nothing like a new job to show you how little you know.
I've been picking up a lot on these topics on the job, but I'd like to take a more proactive approach.
Here are three areas where I feel particularly weak and how I intend to improve.

#### (1) Databases (SQL and otherwise)

Plenario is a database-intensive application, so I've been picking up a lot about PostgreSQL, PostGIS, and relational databases in general in order to move the project forward. However, it would be great to dive deeper into the internals of relational databases to better understand how different schema designs and queries impact performance.

Also, because I hang around in an office where people yammer on about "big data" all day, I can't help but be curious about NoSQL databases, of which my ignorance is vast.

Fortunately, a professor I work with is letting me sit on [a database course](https://mpcs-courses.cs.uchicago.edu/2015-16/winter/courses/53003) she teaches that covers precisely these topics!

#### (2) System administration and operations

This is a classic knowledge gap for CS graduates in their first "real" job.
I'm no exception.
While I came in with a half-decent sysadmin toolset, I've had to pick up lots more, especially when it comes to DBA tasks and AWS administration.

One of my biggest frustrations with Plenario right now is a lack of automation.
To deploy, I run our functional test suite on my dev machine, merge into master and push, shell into our servers to pull down the new code, and then click around on the production site to make sure I didn't break anything that I couldn't catch locally.
Clearly, there's a lot of room for improvement here.

I listened to Matthew Makai get interviewed on _Talk Python to Me_ about deploying Python web applications and rushed online to buy [his book](http://www.deploypython.com/).
My first concrete task in improving my ops skills will be following along with his book to get a foundation on automating deployments.
Then I'll be ready to set up a build process for Plenario with automated testing on Travis CI and code deployment to our EC2 servers.

#### (3) Frontend organization and tooling

I pride myself on being able to write clean, testable Python for our backend.
JavaScript is another matter.
I don't have experience keeping a large-ish frontend codebase manageable. (Here I take large-ish to be the point where a bunch of JQuery callbacks and dumping libraries into a resource folder stops scaling.)

If I want to get better, I'll need a frontend side project that I want to build. Probably something with data visualization, because I do like playing with D3 and I happen to know of a lot of really cool public datasets...

#### What to give up?

To make room for these technical goals, I'll dial back my fixation with shiny new programming languages.
Also, I've taken the radical step of blocking my favorite technical distraction (HackerNews) from my laptop and phone browser.

### 2: Contribute More to the Community

I only got "radicalized" in tech when I found a like-minded group of nerds in Pittsburgh to hold events and talk shop with.
The tech scene in Chicago is awesome too, and I want to be more involved.
So I resolve to volunteer as a mentor for Chicago Python's Spring mentorship program.
I wish I'd done the Fall program. :/

Second, I want to contribute back to the open source community that creates the tools and documentation I love.
I made an earnest attempt at making my first big OSS contribution in 2015, but I bit off too much at once - new language, new domain, huge new feature.
Better to pick a library I already use, start with documentation fixes, and then pick off a ticket.

### 3: Grow as a Technical Leader

This one is the toughest.
I can take on projects to improve my tech skills.
I can volunteer for pre-existing organizations to get more active in the community.
But how to improve my "soft skills"?

The coolest and most challenging part of my new job is the number of stakeholders I work with.
I talk to my bosses to understand our priorities, I talk to our users to understand their needs, I talk to individual contributors to understand their skills, and I talk to domain experts to understand implementation challenges.
So much of my job hinges on how well I can listen to everyone and synthesize what I've heard into code.

So how do I grow as a listener, a communicator, a leader?
One way is actively seeking feedback from the people I work with.
How am I doing?
Are you getting all the information you need from me?
What would you be doing differently if you were in my role?

This will be the toughest resolution. I'll keep thinking on how to attack it.
