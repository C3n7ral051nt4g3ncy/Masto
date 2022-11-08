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
    user_query = input("\033[1mUsername: \033[0m")
    url = f"https://mastodon.social/api/v2/search?q={user_query}"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.06)

    if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
        print(f"\n\033[1m\033[31muser [{user_query}] NOT found!\033[0m")
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
    user_query = input("\033[1mUsername: \033[0m")
    url = f"https://mastodon.social/@{user_query}.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if "error" in data and data["error"] == "Not Found":
        print(f"\n\033[1m\033[31muser [{user_query}] NOT found!\033[0m")
        return

    # Create a profile data dictionary
    profile_data ={"profile url": data["id"],
                   "is discoverable?": data["discoverable"],
                   "is human or bot?": data["type"],
                   "name": data["name"],
                   "preferred username": data["preferredUsername"],
                   "user approves followers manually?": data["manuallyApprovesFollowers"],
                   "public key": data["publicKey"],
                   "link to user followers": data["followers"],
                   "link to accounts user is following": data["following"]
                   }
    # Iterate over the profile data dictionary and print its keys and values
    for profile_key, profile_value in profile_data:
        print(f"{profile_key}: {profile_value}")

    basic_info = data["summary"]
    joined_date = data["published"]
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
                ]
    for bad_tag in bad_tags:
        basic_info = basic_info.replace(bad_tag, "")
    print("bio:", basic_info)


    bad_date_tag = ["T00:00:00Z"]
    for bad_date_tag in bad_date_tag:
        joined_date = joined_date.replace(bad_date_tag, "")
    print("joined mstdn on", joined_date)

    attachments = []
    for attachment in data.get("attachment", []):
        name = attachment.get("name")
        soup = BeautifulSoup(attachment.get("value"), "html.parser")
        a = soup.find("a")
        attachments.append(f'--> {name}: {a.get("href")}')

    print("sites found :")
    for attachment in attachments:
        print(f"\t {attachment}")

    tagsurl = f"https://mastodon.social/users/{user_query}/collections/tags.json"
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
    user_query = input("\033[1mUsername: \033[0m")
    url = f"https://mstdn.social/@{user_query}.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if "error" in data and data["error"] == "Not Found":
        print(f"\n\033[1m\033[31muser [{user_query}] NOT found!\033[0m")
        return

    # Create a profile data dictionary
    profile_data ={"profile url": data["id"],
                   "is discoverable?": data["discoverable"],
                   "is human or bot?": data["type"],
                   "name": data["name"],
                   "preferred username": data["preferredUsername"],
                   "user approves followers manually?": data["manuallyApprovesFollowers"],
                   "public key": data["publicKey"],
                   "link to user followers": data["followers"],
                   "link to accounts user is following": data["following"]
                   }
    # Iterate over the profile data dictionary and print its keys and values 
    for profile_key, profile_value in profile_data.items():
        print(f"{profile_key}: {profile_value}")

    basic_info = data["summary"]
    joined_date = data["published"]
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
                ]
    for bad_tag in bad_tags:
        basic_info = basic_info.replace(bad_tag, "")
    print("bio:", basic_info)


    bad_date_tag = ["T00:00:00Z"]
    for bad_date_tag in bad_date_tag:
        joined_date = joined_date.replace(bad_date_tag, "")
    print("joined mstdn on", joined_date)

    attachments = []
    for attachment in data.get("attachment", []):
        name = attachment.get("name")
        soup = BeautifulSoup(attachment.get("value"), "html.parser")
        a = soup.find("a")
        attachments.append(f'-->{name}: {a.get("href")}')

    print("sites found :")
    for attachment in attachments:
        print(f"\t {attachment}")


def instance_search():
    print("\n\n═══════════════════════════════════════")
    print("\033[32mFind information \033[1mon instance (server)\033[0m")
    print("\033[32mExample: social.network.europa.eu\033[0m")
    print("═══════════════════════════════════════")
    print("\nInput instance (server) name \033[1mWITHOUT the @ symbol\033[0m in front!")
    instance_query = input("\033[1mInstance: \033[0m")
    url = f"https://{instance_query}/api/v1/instance.json"
    try:
        response = requests.request("GET", url)
        data = json.loads(response.text)
    except Exception as e:
        data = {}

    for _ in tqdm(range(10)):
        time.sleep(0.03)

    if not data:
        print(
            f"\n\033[31minstance\033[1m [{instance_query}]\033[0m\033[31m NOT found!\033[0m"
        )
        return

    instance_data = {"instance (server)": data["uri"],
                     "title": data["title"],
                     "description": data["short_description"],
                     "instance email": data["email"],
                     "server thumbnail": data["thumbnail"],
                     "instance languages": data["languages"],
                     "registration needed?": data["registrations"],
                     "admin approval required?": data["approval_required"],
                     "invites enabled on instance?": data["invites_enabled"],
                     }
    for instance_key, instance_value in instance_data.items():
        print(f"{instance_key}: {instance_value}")
    pprint(data["contact_account"])
    print("\n")


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
