#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code style         : Black
# Tool name          : Masto (v2.0)
# File name          : masto.py
# Author             : C3n7ral051nt4g3ncy(@OSINT_Tactical)


# Modules
import time
import json
from tqdm import tqdm
import sys
import webbrowser
import requests
import argparse
from w3lib.html import remove_tags
from bs4 import BeautifulSoup
import asyncio
import aiohttp


# banner
print(
    """\033[34m
███╗   ███╗ █████╗ ███████╗████████╗ ██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗
██╔████╔██║███████║███████╗   ██║   ██║   ██║
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██║   ██║
██║ ╚═╝ ██║██║  ██║███████║   ██║   ╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝v2.0\033[0m"""
)
print("\033[34m\033[1mMastodon OSINT Tool\033[0m")
print("by @C3n7ral051nt4g3ncy ")
print(
    "https://ko-fi.com/tacticalintelanalyst\n"
    "BTC: bc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde\n"
)

# search mastodon instances (servers)
async def instance_search(instance, session):
    headers = {
        "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "en-US;q=0.9,en,q=0,8",
        "accept-encoding": "gzip, deflate",
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
        "Chrome/104.0.0.0 Safari/537.36",
    }
    inst_url = f"https://{instance}/api/v1/instance"
    try:
        async with session.get(inst_url, headers=headers, timeout=10) as response:
            inst_data = await response.json()
    except Exception as e:
        inst_data = {}

    if not inst_data:
        print(
            f"\n\033[31mMastodon instance\033[1m [{instance}]\033[0m\033[31m NOT found!\033[0m"
        )
        return

    name = inst_data["uri"]
    print("\ninstance (server): ", name)
    title = inst_data["title"]
    print("title: \033[32m\033[1m", title)
    s_description = inst_data["short_description"]
    s_description = remove_tags(s_description)
    print("\033[0mdescription: ", s_description)
    det_descript = inst_data["description"]
    det_descript = remove_tags(det_descript)
    print("detailed description: ", det_descript)
    e_mail = inst_data["email"]
    print("\ninstance email: \033[32m\033[1m", e_mail)
    thumb = inst_data["thumbnail"]
    print("\033[0mserver thumbnail:", thumb)
    lang = inst_data["languages"]
    print("instance languages: ", lang)
    reg = inst_data["registrations"]
    print("registration needed: ", reg)
    reg_approve = inst_data["approval_required"]
    print("admin approval required: ", reg_approve)
    print("\ninstance admin information:")
    admin_data = inst_data["contact_account"]
    for key in [
        "id",
        "username",
        "acct",
        "display_name",
        "followers_count",
        "following_count",
        "statuses_count",
        "last_status_at",
        "locked",
        "bot",
        "discoverable",
        "group",
        "created_at",
        "url",
        "avatar",
        "header",
    ]:
        print(f"{key}: {admin_data[key]}")


# search username with Mastodon API
async def username_search_api(username, session):
    url = f"https://mastodon.social/api/v2/search?q={username}"
    async with session.get(url, timeout=10) as response:
        data = await response.json()
        text = await response.text()

    if text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
        print(
            f"\n\033[1m\033[31mTarget username: [{username}] NOT found using the Mastodon API!\033[0m"
        )
        return

    data = filter(
        lambda x: x.get("username").lower() == username.lower(), data["accounts"]
    )
    for index, intelligence in enumerate(list(data), start=1):

        print("\n\n══════════")
        print(f"\033[32m\033[1mAccount: {index}\033[0m")
        print("══════════\n")

        identity = intelligence["id"]
        lock = intelligence["locked"]
        pro_url = intelligence["url"]
        target_username = intelligence["username"]
        account = intelligence["acct"]
        display = intelligence["display_name"]
        creation_date = intelligence["created_at"]
        bot = intelligence["bot"]
        discov = intelligence["discoverable"]
        fwers = intelligence["followers_count"]
        fwing = intelligence["following_count"]
        posts = intelligence["statuses_count"]
        laststatus = intelligence["last_status_at"]
        group = intelligence["group"]
        note = intelligence["note"]
        note = remove_tags(note)
        avatar = intelligence["avatar"]

        print("user ID:\033[32m\033[1m", identity)
        print("\033[0mprofile url:", pro_url)
        print("account locked:", lock)
        print("username:", target_username)
        print("\033[0maccount:\033[32m\033[1m", account)
        print("\033[0mdisplay Name:\033[32m\033[1m", display)
        print("\033[0mprofile creation date:", creation_date)
        print("user is a bot:", bot)
        print("user opted to be listed on the profile directory:", discov)
        print("followers:", fwers)
        print("following:", fwing)
        print("number of posts:", posts)
        print("user last message date:", laststatus)
        print("user is a group:", group)
        print("user bio:", note)

        fields = []
        for field in intelligence.get("fields", []):
            name = field.get("name")
            value = field.get("value")

            if value and '</' not in value:
                continue                                                 

            soup = BeautifulSoup(value, "html.parser")
            a = soup.find("a")
            if a:
                fields.append(f'--> {name}: {a.get("href")}')
                print(f"sites found :")
            else:
                continue

            for field in fields:
                print(f"\t {field}")


        print("user's avatar link:", avatar)
        print(
            f"\nPreparing to scan for target -->\033[32m\033[1m {username}\033[0m on the \033[32m\033[1m"
            f"Masto OSINT Tool servers database\033[0m\033[0m\n"
        )


async def username_search(username, session):
    headers = {
        "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "en-US;q=0.9,en,q=0,8",
        "accept-encoding": "gzip, deflate",
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
        "Chrome/104.0.0.0 Safari/537.36",
    }

    async with session.get(
        "https://raw.githubusercontent.com/C3n7ral051nt4g3ncy/Masto/master/fediverse_instances.json",
        timeout=10
    ) as response:
        text = await response.text()
        sites = json.loads(text)["sites"]

    # Create tasks for all site checks
    async def check_site(site):
        uri_check = site["uri_check"].format(account=username)
        try:
            async with session.get(uri_check, headers=headers) as res:
                text = await res.text()
                if res.status == 200 and text.find(site["e_string"]) > 0:
                    print("\033[32m-" * 77)
                    print(
                        f"\033[32m[+] \033[1mTarget found\033[0m\033[32m ✓ on:\033[1m{site['name']}\033[0m"
                    )
                    print(f"\033[32m[+] Profile URL:\033[1m{uri_check}\033[0m")
                    print("\033[32m\033[1m-\033[0m" * 77)
                    return True
        except Exception:
            pass
        return False

    # Run all site checks concurrently
    results = await asyncio.gather(*[check_site(site) for site in sites])
    
    is_any_site_matched = any(results)
    if not is_any_site_matched:
        print(
            f"\n\033[1m\033[31mTarget username: [{username}] NOT found on the Masto OSINT Tool servers database!\033[0m"
        )
    return is_any_site_matched


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Masto OSINT Tool help --> "
        "\033[32m\033[1m[For username]\033[0m: input without @ symbol |"
        "\033[32m\033[1m [For server]\033[0m: input without https in"
        " front | example: \033[35m\033[1minfosec.exchange\033[0m"
    )

    parser.add_argument(
        "-u",
        "--username",
        help="\033[32m\033[1m\ntarget username search across hundreds of Mastodon instances\033[0m",
    )

    parser.add_argument(
        "-i",
        "--instance",
        help="\033[32m\033[1m\ninstance (server)\033[0m",
    )

    args = parser.parse_args()

    if len(sys.argv) == 1:
        print(
            "You did not pass an argument | For Help --> \033[32m\033[1mpython3 masto.py -h\033[0m"
        )
        sys.exit(1)

    async def main(instance, username):
        if instance:
            while True:
                async with aiohttp.ClientSession() as session:
                    instance_found = await instance_search(instance, session)

                yes_no = input("\nCheck another instance? [yes|no]: ")
                if yes_no.lower() == "no":
                    break
                else:
                    instance = input("type new instance: ")

        if username:
            while True:
                async with aiohttp.ClientSession() as session:
                    await asyncio.gather(
                        username_search_api(username, session),
                        username_search(username, session)
                    )

                yes_no = input("\nTry another username? [yes|no]: ")
                if yes_no.lower() == "no":
                    break
                else:
                    username = input("Type new username: ")

    asyncio.run(main(args.instance, args.username))
                