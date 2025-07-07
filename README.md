# BRIDG3, aka the [Wright Channel](https://youtu.be/XZ81qaTwwkM?si=OyO69GG6fnEdHtEJ)

## Introduction
The aim of this project is to listen to the Telegram channels of student associations for event announcement messages and send a summary message with the necessary details to a second channel, i.e., the Wright Channel, to have only one channel to check for all the events. Of course, it can be modified to monitor any channel and collect all kinds of messages. This code was submitted as *Quantum Mesh Wizards*' response to the $2^{nd}$ task of the [BRIDG3 Hackathon](https://www.instagram.com/bridge.tampere/) held in December 2023, which was declared the winner solution!

Check out our pitch video [here](https://youtu.be/XZ81qaTwwkM?si=OyO69GG6fnEdHtEJ)!

Additionally, you can find out more about our team [here](https://www.linkedin.com/posts/activity-7139616011019886592-eZC_?utm_source=share&utm_medium=member_desktop&rcm=ACoAADVm4M0Bd7JQityYOVx5qGOdVS74AJPlGjU).

## Installation

First, you'll need to clone this repository to your local drive via the following command:
```shell
$ git clone https://github.com/Ali-Jedari/BRIDG3.git
```
And then:
```shell
$ cd BRIDG3
```

Alternatively, if `git` is not installed, you can download the zip file for this repository and then extract it.

## Requirements

This project is written in python 3 and requires Telethon, Pandas, and Numpy.

All the required libraries can be installed by running the following command:

```shell
$ pip install -r requirements.txt
```

If the command above results in an error, you can also try:

```shell
$ python -m pip install -r requirements.txt
```

## Usage

First, you'll need to update the indicated variables in `telegram_message.py`. You can find the official Telegram guide on how to obtain the necessary values for your application [here](https://core.telegram.org/api/obtaining_api_id).

Afterwards, you should run:

```shell
$ python telegram_message.py
```
