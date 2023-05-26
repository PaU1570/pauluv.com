---
title: "Say hello to my server" 
date: 2023-05-22
author: "Paul U.V."
categories:
  - technology
tags: 
  - server
  - unraid
  - hardware
---

As the first blog post on this website, I thought it would be fitting for it to be about the infrastructure on which everything runs. From the hardware to the software and everything in between, this post is a comprehensive guide to the inner and outer workings of this server, henceforth to be referred to as GureServer (Basque for 'OurServer', _USSR anthem softly plays in the background_). Let's get started, shall we?

## Hardware
This server, far from being some fancy homelab with server-grade hardware, is actually quite basic and affordable. For its current duties, it is more than enough, and it will probably still be for a while unless somehow this blog becomes insanely popular. The components are as follows (prices at the time of purchase, January 2022):

- **Intel Core i5-12500** (220€): It is the same as the i5-12400, which was a great bang for the buck, but with slightly higher core clocks. For some reason they were both the same price, so obviously I bought the faster one. I went with intel because, at the time, AMD's latest gen didn't have a similar budget option. I am using the included stock cooler because it works just fine, although that might change once I come around to building a cloud gaming setup.
- **Asus Prime B660M-K D4** (116€): This one is very simple to explain. It was one of the cheapest motherboards I found with the B660 chipset, which is the lowest tier that supports dual-channel memory. Other than that, the choice of motherboard doesn't really affect performance, and this one has all the expansion I need (for now). I also wasn't willing to spend the extra money to go with DDR5 (this was in the early days of DDR5, when it was quite expensive).
- **Crucial Ballistix Red 2x16GB 3200 MHz CL16** (97€): I think it was on sale or something. In any case, good enough for me, and I'm glad I went with 32GB instead of 16GB.
- **Corsair TX650M 650W 80+ Gold PSU** (70€): I think this one was also on sale, because at the time of writing this it is listed for 95€ on the same store. Anyway, a decent PSU from a reputable brand. It is 650W to possibly accomodate a GPU in the future.
- **UNYKAch UK 4129 Rack-mount case** (92€): No, I hadn't heard of that brand before either. I just wanted a rack-mount case, and this is what I found. It's pretty damn big, I will say that.
- **2x120mm + 2x80mm Noctua fans** (80€): I include them in the list for completeness.

Originally I was using three old [HDD drives](https://en.wikipedia.org/wiki/RAS_syndrome) and a 500GB SSD, all of which I had already. More on how and why they are used once we get to the software part. Later, I bought a couple more drives:

- **WD Red SN700 500GB** (60€): NAS grade drive, a safe bet.
- **WD Black SN770 1TB** (66€): I was wary at first because reddit seems to hate DRAM-less drives, but after looking at some reviews I decided to give it a try. I still haven't used it for what I originally bought it for (gaming), so the performance remains to be seen.

Total cost of the server: 801€. It could have definitely been cheaper (I didn't realize I spent 80€ on fans until I checked to write this list), but I am happy with it.

## Software
I am running the [Unraid](https://unraid.net) operating system. It is not free like other NAS options, but it is very easy to use and has great community support. Most of the services run on docker containers, so here is a list that will hopefully explain what each of them does and how they work with each other:
