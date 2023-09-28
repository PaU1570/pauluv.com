---
title: "Say hello to my server" 
date: 2023-05-27
author: "Paul U.V."
categories:
  - technology
tags: 
  - server
  - unraid
  - hardware
---

This is a slightly outdated overview of the server that hosts this website.

## Hardware
The hardware components are as follows (prices at the time of purchase, January 2022):

- **Intel Core i5-12500** (220€): It is the same as the i5-12400, which was a great bang for the buck, but with slightly higher core clocks (and better iGPU). For some reason, they were both the same price, so obviously I bought the faster one. I went with intel because, at the time, AMD's latest gen didn't have a similar budget option. I am using the included stock cooler because it works just fine, although that might change once I come around to building a cloud gaming setup.
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
The server is running [Unraid](https://unraid.net). It is not free like other NAS options, but it is very easy to use and has great community support. Most of the services run on docker containers, so here is a list that will hopefully explain what each of them does and how they work with each other (this list is outdated):

- **Utility/infrastructure**: These containers provide utilities or services for other applications on the network.
    - **mosquitto**: Mqtt broker, useful for many IoT things. I mainly use it to communicate with my 3D printer.
    - **chronos**: I use this to run certain python scripts periodically.
    - **ZeroTier**: Provides remote access to my Unraid machine through black magic or something. I learned about it when I was trying to set up a VPN for remote access and I found out that I could not open ports on my router due to it being behind a CG NAT (this is no longer the case, but, if it ain't broke don't fix it).
    - **OpenSpeedTest**: Self explanatory; nice to have :)
    - **rClone**: Backups!!!! Are you backing up your data? No? Go back your data up!
    - **hassConfigurator**: Makes editing and checking HomeAssistant configs easy.

- **Home Automation/Monitoring**:
    - **Home Assistant**: The one and only. You've probably heard of it if you have ever done anything with home automation.
    - **Frigate**: NVR with AI object detection. Works pretty well with our ReoLink camera, for the most part. I have not been able to get hardware h.265 decoding to work, although I have successfully tested it with other containers. At least I do have AI acceleration with OpenVINO.
    - **telegraf/InfluxDB/Grafana**: Classic trio to read, store, and display data, respectively, from our Victron solar inverter. Maybe I will write a blog post about this pipeline in the future.
    - **OctoPrint**: Because who would want to physically carry files back and forth on an SD card? You can also make the printer automatically turn off once it's finished printing, which is nice.

- **Media**:
    - **Plex**: I tried Jellyfin, but I just don't like the UI as much.
    - **PhotoPrism**: The best photo organizer app that I found. I particularly like the map view, although it does require your photos to be geotagged.

- **Web**: What I use to host this website.
    - **pauluv**: A custom docker container based on [this](https://hub.docker.com/r/tiangolo/meinheld-gunicorn-flask) that I use to run this website (Flask based). The source code is on my [GitHub](https://github.com/PaU1570/pauluv.com) page.
    - **SWAG**: nginx webserver and reverse proxy for my apps, as well as auto SSL certification, and fail2ban intrusion prevention. Nice all-in-one package to host a website on your Unraid server. I essentially use it as a reverse proxy for the **pauluv** container.
    - **duckdns**: To map my dynamic IP to a static domain.
    - **crowdsec**: Seemed like a good idea, not sure if I actually need it.

I also have an old Synology NAS, with two 4TB mirrored drives, where all the media for Plex and Photoprism is stored. I want to eventually consolidate everything onto GureServer, but I have not had the time or willingness to do so yet. Meanwhile, I simply mount the Synology NAS as a share on Unraid, and access everything from there.