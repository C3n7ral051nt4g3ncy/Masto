#!/usr/bin/python
# -*- coding: utf-8 -*-
# Tool name          : Masto
# File name          : masto.py
# Author             : C3n7ral051nt4g3ncy(@OSINT_Tactical)

import time
import requests
import json
from tqdm import tqdm
import sys
import webbrowser
import re
import urllib.request
import urllib.parse

print("""\033[35m
███╗   ███╗ █████╗ ███████╗████████╗ ██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗
██╔████╔██║███████║███████╗   ██║   ██║   ██║
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██║   ██║
██║ ╚═╝ ██║██║  ██║███████║   ██║   ╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝v0.1\033[0m""")
print("Mastodon OSINT Tool")
print("by @C3n7ral051nt4g3ncy ")
print("https://ko-fi.com/tacticalintelanalyst\n"
      "BTC: bc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde")

headers = {
        "Accept": 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        "accept-language": "en-US;q=0.9,en,q=0,8",
        "accept-encoding": "gzip, deflate",
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/104.0.0.0 "
        "Safari/537.36", }


def status():
    url = 'https://mastodon.social/api/v2/search?q=mastodon'
    request = requests.get(url)
    if request.status_code == 200:
        print("\n\033[32m\033[1mMastodon API is ready to rooooooll!\033[0m")
    else:
        print("\n\033[31m\033[1mserver response failed, try again later\033[0m")
        return


def all_servers_search():
    print("\nInput username \033[1mWITHOUT the @ symbol\033[0m in front!")
    query = input("\033[1mUsername: \033[0m")
    user = query
    url = f'https://mastodon.social/api/v2/search?q={user}'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.06)

    if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        print("try below searching only on Mastodon.social")
        return
    time.sleep(1)

    data = filter(lambda x: x.get('username').lower() == user.lower(), data['accounts'])
    for index, intelligence in enumerate(list(data), start=1):

        print("\n\n══════════")
        print(f"\033[1mAccount: {index}\033[0m")
        print("══════════\n")

        identity = intelligence['id']
        lock = intelligence['locked']
        pro_url = intelligence['url']
        username = intelligence['username']
        account = intelligence['acct']
        dispn = intelligence['display_name']
        creation_date = intelligence['created_at']
        bot = intelligence['bot']
        dscvr = intelligence['discoverable']
        fwers = intelligence['followers_count']
        fwing = intelligence['following_count']
        posts = intelligence['statuses_count']
        lastm = intelligence['last_status_at']
        group = intelligence['group']
        note = intelligence['note']
        avt = intelligence['avatar']

        print("user ID:", identity)
        print("account locked:", lock)
        print("profile url:", pro_url)
        print("username:", username)
        print("account:", account)
        print("display Name:", dispn)
        print("profile creation date:", creation_date)
        print("user is a bot:", bot)
        print("user opted to be listed on the profile directory:", dscvr)
        print("followers:", fwers)
        print("following:", fwing)
        print("number of posts:", posts)
        print("user last message date:", lastm)
        print("user is a group:", group)

        bad_tags = ['<p>', '</p>', '</a>', '</span>', '<span>', '<a href', '"', '<', '>', 'class=', 'rel=tag', '=',
                    'relnofollow', 'noopener', 'noreferrer', 'target_blankspan', 'target_blank', 'span', 'invisible']
        for bad_tag in bad_tags:
            note = note.replace(bad_tag, '')
        print("user bio:", note)
        print("user's avatar link:", avt)

        choice = input("\033[1mopen avatar in browser | Y or N: \033[0m")
        if choice in ["y", "Y", "YES", "yes"]:
            webbrowser.open(avt)
        if choice in ["n", "N", "NO", "no"]:
            continue

def mastodon_search():
    print("\n\n═══════════════════════════════════════")
    print("\033[34m\033[1mhttps://mastodon.social\033[0m")
    print("\033[34mSearch for user \033[1mONLY on Mastodon.social\033[0m")
    print("═══════════════════════════════════════")
    print("\nInput username \033[1mWITHOUT the @ symbol\033[0m in front!")
    query = input("\033[1mUsername: \033[0m")
    user = query
    url = f'https://mastodon.social/@{user}.json'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if 'error' in data and data['error'] == 'Not Found':
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        return

    proflink = data['id']
    name = data['name']
    persbot = data['type']
    profdisc = data['discoverable']
    prefuser = data['preferredUsername']
    basicinfo = data['summary']
    jdate = data['published']
    fwersapprove = data['manuallyApprovesFollowers']
    pubkey = data['publicKey']
    fwerslink = data['followers']
    fwinglink = data['following']
    icon = data['icon']
    img = data['image']

    print("\nprofile url:", proflink)
    print("profile discoverable:", profdisc)
    print("person | bot:", persbot)
    print("name:", name)
    print("preferred username:", prefuser)

    bad_tags = ['<p>', '</p>', '</a>', '</span>', '<span>', '<a href', '"', '<', '>', 'class=', 'rel=tag', '=']
    for bad_tag in bad_tags:
        basicinfo = basicinfo.replace(bad_tag, '')
    print("bio:", basicinfo)

    bad_date_tag = ['T00:00:00Z']
    for bad_date_tag in bad_date_tag:
        jdate = jdate.replace(bad_date_tag, '')
    print("joined Mastodon on:", jdate)
    print("user approves followers manually:", fwersapprove)
    print("public key:", pubkey)
    print("link to user followers:", fwerslink)
    print("link to accounts user is following:", fwinglink)

    attachment = ' | '.join([s.get('value') for s in data.get('attachment', [])])

    b_tags = ['<p>', '</p>', '</a>', '</span>', '<span>', '<a href', '"', '<', '>', 'class=', 'rel=tag', '=',
              'target=_blank', 'target=_blank', 'rel=nofollow', 'noopener', 'noreferrer', 'span',
              'invisible', '=', 'spanme', '<>', 'me"><span', 'target_blank', 'relnofollow', 'me https://www.']

    for b_tag in b_tags:
        attachment = attachment.replace(b_tag, '')
    print(f"sites found --> {attachment}")

    print("profile image info:", icon)
    print("header image info:", img)

    tagsurl = f'https://mastodon.social/users/{user}/collections/tags.json'
    resp = requests.request("GET", tagsurl)
    tags_data = json.loads(resp.text)
    htags_numb = tags_data['totalItems']
    items = ' | '.join([t.get('name') for t in tags_data.get('items', [])])
    print("number of Hashtags found:", htags_numb)
    print(f"hashtags found --> {items}")


def mstdn_search():
    print("\n\n════════════════════════════════════")
    print("\033[35m\033[1mhttps://mstdn.social\033[0m")
    print("\033[35mSearch for user \033[1mONLY on mstdn.social\033[0m")
    print("Can provide additional info")
    print("════════════════════════════════════")
    print("\nInput username \033[1mWITHOUT the @ symbol\033[0m in front!")
    query = input("\033[1mUsername: \033[0m")
    user = query
    url = f'https://mstdn.social/@{user}.json'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if 'error' in data and data['error'] == 'Not Found':
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        return

    proflink = data['id']
    name = data['name']
    persorbot = data['type']
    profdisc = data['discoverable']
    prefuser = data['preferredUsername']
    basicinfo = data['summary']
    jdate = data['published']
    fwersapprove = data['manuallyApprovesFollowers']
    pubkey = data['publicKey']
    fwerslink = data['followers']
    fwinglink = data['following']
    icon = data['icon']
    img = data['image']


    print("\nprofile url:", proflink)
    print("profile discoverable:", profdisc)
    print("person | bot:", persorbot)
    print("name:", name)
    print("preferred username:", prefuser)

    bad_tags = ['<p>', '</p>', '</a>', '</span>', '<span>', '<a href', '"', '<', '>', 'class=', 'rel=tag', '=']
    for bad_tag in bad_tags:
        basicinfo = basicinfo.replace(bad_tag, '')
    print("bio:", basicinfo)

    bad_date_tag = ['T00:00:00Z']
    for bad_date_tag in bad_date_tag:
        jdate = jdate.replace(bad_date_tag, '')
    print("joined mstdn on:", jdate)
    print("user approves followers manually:", fwersapprove)
    print("public key:", pubkey)
    print("link to user followers:", fwerslink)
    print("link to accounts user is following:", fwinglink)

    attachment = ' | '.join([s.get('value') for s in data.get('attachment', [])])

    b_tags = ['<p>', '</p>', '</a>', '</span>', '<span>', '<a href', '"', '<', '>', 'class=', 'rel=tag', '=',
              'target=_blank', 'target=_blank', 'rel=nofollow', 'noopener', 'noreferrer', 'span',
              'invisible', '=', 'spanme', '<>', 'me"><span', 'target_blank', 'relnofollow', 'me https://www.']

    for b_tag in b_tags:
        attachment = attachment.replace(b_tag, '')
    print(f"sites found --> {attachment}")

    print("profile image info:", icon)
    print("header image info:", img)



def main():
    status()
    all_servers_search()
    mastodon_search()
    mstdn_search()


if __name__ == '__main__':
    while True:
        main()

        choice = input("\033[1m\nsearch for another user | Y or N: \033[0m")
        if choice in ["y", "Y", "YES", "yes"]:
            continue
        if choice in ["n", "N", "NO", "no"]:
            print("\n\033[35mBye-Bye 👋")
            break
