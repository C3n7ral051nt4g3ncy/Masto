#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code style         : Black
# Tool name          : Masto
# File name          : masto.py
# Author             : C3n7ral051nt4g3ncy(@OSINT_Tactical)

import time
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import webbrowser
import re
import urllib.request
import urllib.parse
from pprint import pprint

print(
    """\033[34m
███╗   ███╗ █████╗ ███████╗████████╗ ██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗
██╔████╔██║███████║███████╗   ██║   ██║   ██║
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██║   ██║
██║ ╚═╝ ██║██║  ██║███████║   ██║   ╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝v0.1\033[0m"""
)
print("Mastodon OSINT Tool")
print("by @C3n7ral051nt4g3ncy ")
print(
    "https://ko-fi.com/tacticalintelanalyst\n"
    "BTC: bc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde"
)

headers = {
    "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "en-US;q=0.9,en,q=0,8",
    "accept-encoding": "gzip, deflate",
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/104.0.0.0 "
    "Safari/537.36",
}


def status():
    url = "https://mastodon.social/api/v2/search?q=mastodon"
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
    url = f"https://mastodon.social/api/v2/search?q={user}"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.06)

    if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        print("try below searching only on Mastodon.social")
        return
    time.sleep(1)

    data = filter(lambda x: x.get("username").lower() == user.lower(), data["accounts"])
    for index, intelligence in enumerate(list(data), start=1):

        print("\n\n══════════")
        print(f"\033[1mAccount: {index}\033[0m")
        print("══════════\n")

        # Create a user data dictionary
        user_data = {"user ID": intelligence["id"],
                     "profile url": intelligence["url"],
                     "account locked": intelligence["locked"],
                     "username": intelligence["username"],
                     "account": intelligence["acct"],
                     "display name": intelligence["display_name"],
                     "profile creation date": intelligence["created_at"],
                     "user is a bot?": intelligence["bot"],
                     "user opted to be listed on the profile directory?": intelligence["discoverable"],
                     "followers": intelligence["followers_count"],
                     "following": intelligence["following_count"],
                     "number of posts": intelligence["statuses_count"],
                     "user last message date": intelligence["last_status_at"],
                     "user is a group?": intelligence["group"],
                     }
        # Iterate over the dictionary, and print its keys, and values
        for user_key, user_value in user_data.items():
            print(f"{user_key}: {user_value}")

        # Had to exclude note and avatar from the user_data dictionary
        # Thought it might cause some issues
        note = intelligence["note"]
        avatar = intelligence["avatar"]
        bad_tags = ["<p>",
                        "</p>",
                        "</a>",
                        "</span>",
                        "<span>",
                        "<a href",
                        '"',
                        "<",
                        ">",
                        "class=",
                        "rel=tag",
                        "=",
                        "relnofollow",
                        "noopener",
                        "noreferrer",
                        "target_blankspan",
                        "target_blank",
                        "span",
                        "invisible",
                        "\u003e\u003c/a\u003e.",
                        "\u003cbr",
                        ]
        for bad_tag in bad_tags:
            note = note.replace(bad_tag, "")
        print("user bio:", note)
        print("user's avatar link:", avatar)

        choice = input("\033[1mopen avatar in browser | Y or N: \033[0m")
        if choice in ["y", "Y", "YES", "yes"]:
            webbrowser.open(avatar)
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
    url = f"https://mastodon.social/@{user}.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if "error" in data and data["error"] == "Not Found":
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        return

    proflink = data["id"]
    name = data["name"]
    persbot = data["type"]
    profdisc = data["discoverable"]
    prefuser = data["preferredUsername"]
    basicinfo = data["summary"]
    jdate = data["published"]
    fwersapprove = data["manuallyApprovesFollowers"]
    pubkey = data["publicKey"]
    fwerslink = data["followers"]
    fwinglink = data["following"]

    print("\nprofile url:", proflink)
    print("profile discoverable:", profdisc)
    print("person or bot:", persbot)
    print("name:", name)
    print("preferred username:", prefuser)

    bad_tags = [
        "<p>",
        "</p>",
        "</a>",
        "</span>",
        "<span>",
        "<a href",
        '"',
        "<",
        ">",
        "class=",
        "rel=tag",
        "=",
    ]
    for bad_tag in bad_tags:
        basicinfo = basicinfo.replace(bad_tag, "")
    print("bio:", basicinfo)

    bad_date_tag = ["T00:00:00Z"]
    for bad_date_tag in bad_date_tag:
        jdate = jdate.replace(bad_date_tag, "")
    print("joined Mastodon on:", jdate)
    print("user approves followers manually:", fwersapprove)
    print("public key:", pubkey)
    print("link to user followers:", fwerslink)
    print("link to accounts user is following:", fwinglink)

    attachments = []
    for attachment in data.get("attachment", []):
        name = attachment.get("name")
        soup = BeautifulSoup(attachment.get("value"), "html.parser")
        a = soup.find("a")
        attachments.append(f'--> {name}: {a.get("href")}')

    print(f"sites found :")
    for attachment in attachments:
        print(f"\t {attachment}")

    tagsurl = f"https://mastodon.social/users/{user}/collections/tags.json"
    resp = requests.request("GET", tagsurl)
    tags_data = json.loads(resp.text)
    htags_numb = tags_data["totalItems"]
    items = " | ".join([t.get("name") for t in tags_data.get("items", [])])
    print("number of Hashtags found:", htags_numb)
    print(f"hashtags found --> {items}")


def mstdn_search():
    print("\n\n════════════════════════════════════")
    print("\033[35m\033[1mhttps://mstdn.social\033[0m")
    print("\033[35mSearch for user \033[1mONLY on mstdn.social\033[0m")
    print("\033[35mCan provide additional info\033[0m")
    print("════════════════════════════════════")
    print("\nInput username \033[1mWITHOUT the @ symbol\033[0m in front!")
    query = input("\033[1mUsername: \033[0m")
    user = query
    url = f"https://mstdn.social/@{user}.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if "error" in data and data["error"] == "Not Found":
        print(f"\n\033[1m\033[31muser [{user}] NOT found!\033[0m")
        return

    proflink = data["id"]
    name = data["name"]
    persorbot = data["type"]
    profdisc = data["discoverable"]
    prefuser = data["preferredUsername"]
    basicinfo = data["summary"]
    jdate = data["published"]
    fwersapprove = data["manuallyApprovesFollowers"]
    pubkey = data["publicKey"]
    fwerslink = data["followers"]
    fwinglink = data["following"]

    print("\nprofile url:", proflink)
    print("profile discoverable:", profdisc)
    print("person or bot:", persorbot)
    print("name:", name)
    print("preferred username:", prefuser)

    bad_tags = [
        "<p>",
        "</p>",
        "</a>",
        "</span>",
        "<span>",
        "<a href",
        '"',
        "<",
        ">",
        "class=",
        "rel=tag",
        "=",
    ]
    for bad_tag in bad_tags:
        basicinfo = basicinfo.replace(bad_tag, "")
    print("bio:", basicinfo)

    bad_date_tag = ["T00:00:00Z"]
    for bad_date_tag in bad_date_tag:
        jdate = jdate.replace(bad_date_tag, "")
    print("joined mstdn on:", jdate)
    print("user approves followers manually:", fwersapprove)
    print("public key:", pubkey)
    print("link to user followers:", fwerslink)
    print("link to accounts user is following:", fwinglink)

    attachments = []
    for attachment in data.get("attachment", []):
        name = attachment.get("name")
        soup = BeautifulSoup(attachment.get("value"), "html.parser")
        a = soup.find("a")
        attachments.append(f'-->{name}: {a.get("href")}')

    print(f"sites found :")
    for attachment in attachments:
        print(f"\t {attachment}")


def instance_search():
    print("\n\n═══════════════════════════════════════")
    print("\033[32mFind information \033[1mon instance (server)\033[0m")
    print("\033[32mExample: social.network.europa.eu\033[0m")
    print("═══════════════════════════════════════")
    print("\nInput instance (server) name \033[1mWITHOUT the @ symbol\033[0m in front!")
    query = input("\033[1mInstance: \033[0m")
    instance = query
    url = f"https://{instance}/api/v1/instance.json"
    try:
        response = requests.request("GET", url)
        data = json.loads(response.text)
    except Exception as e:
        data = {}

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if not data:
        print(
            f"\n\033[31minstance\033[1m [{instance}]\033[0m\033[31m NOT found!\033[0m"
        )
        return

    name = data["uri"]
    print("\ninstance (server): " + name)

    title = data["title"]
    print("title: ", title)

    descript = data["short_description"]
    print("description: ", descript)

    e_mail = data["email"]
    print("instance email: ", e_mail)

    thumb = data["thumbnail"]
    print("server thumbnail:", thumb)

    lang = data["languages"]
    print("instance languages: ", lang)

    reg = data["registrations"]
    print("registation needed: ", reg)

    reg_approve = data["approval_required"]
    print("admin approval required: ", reg_approve)

    invites = data["invites_enabled"]
    print("invites enabled on instance: ", invites)

    account_data = data["contact_account"]
    pprint(account_data)


def main():
    status()
    all_servers_search()
    mastodon_search()
    mstdn_search()
    instance_search()


if __name__ == "__main__":
    while True:
        main()

        choice = input("\033[1m\nsearch for another user | Y or N: \033[0m")
        if choice in ["y", "Y", "YES", "yes"]:
            continue
        if choice in ["n", "N", "NO", "no"]:
            print("\n\033[35mBye-Bye 👋")
            break
