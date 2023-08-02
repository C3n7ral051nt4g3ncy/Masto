import time
import json
import argparse
import requests
from tqdm import tqdm
from w3lib.html import remove_tags
from bs4 import BeautifulSoup


class Masto:
    def __init__(self):
        pass
    
    # search mastodon instances (servers)
    def instance_search(self, instance):
        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en;q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
            "Chrome/104.0.0.0 Safari/537.36",
        }
        inst_url = f"https://{instance}/api/v1/instance"
        try:
            response = requests.request("GET", inst_url, headers=headers)
            inst_data = json.loads(response.text)
        except Exception as e:
            inst_data = {}

        if not inst_data:
            print(f"\nMastodon instance [{instance}] NOT found!")
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
    def username_search_api(self, username):
        url = f"https://mastodon.social/api/v2/search?q={username}"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        for _ in tqdm(range(10)):
            time.sleep(0.03)

        if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
            print(f"\nTarget username: [{username}] NOT found using the Mastodon API!")
            return
        time.sleep(1)

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
            print("user bio:\033[32m\033[1m", note)

            fields = []
            for field in intelligence.get("fields", []):
                name = field.get("name")
                value = field.get("value")

                if value and "</" not in value:
                    continue

                soup = BeautifulSoup(value, "html.parser")
                a = soup.find("a")
                if a:
                    fields.append(f'--> {name}: {a.get("href")}')
                    print(f"sites found :\033[32m\033[1m")
                else:
                    continue

                for field in fields:
                    print(f"\t {field}")

            print("\033[0muser's avatar link:", avatar)

    # username search with the Masto OSINT Tool servers database
    def username_search(self, username):
        print("\n")
        print("Now searching through the Masto OSINT tool instances database\n")
        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en;q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
            "Chrome/104.0.0.0 Safari/537.36",
        }

        response = requests.get(
            "https://raw.githubusercontent.com/C3n7ral051nt4g3ncy/Masto/master/fediverse_instances.json"
        )
        sites = response.json()["sites"]
        is_any_site_matched = False
        for site in sites:
            uri_check = site["uri_check"]
            site_name = site["name"]
            uri_check = uri_check.format(account=username)

            try:
                res = requests.get(uri_check, headers=headers)
                estring_pos = res.text.find(site["e_string"]) > 0
            except Exception as e:
                continue

            if res.status_code == 200 and estring_pos:
                is_any_site_matched = True
                print(f"[+] Target found ✓ on: \033[32m\033[1m{site_name}\033[0m")
                print(f"Profile URL: {uri_check}")

        if not is_any_site_matched:
            print(
                f"\nTarget username: [{username}] NOT found on the Masto OSINT Tool servers database!"
            )
        return is_any_site_matched


# Define main function in the module
def main():
    parser = argparse.ArgumentParser(description="Mastodon OSINT Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-user", help="Username to search")
    group.add_argument("-instance", help="Instance to search")

    args = parser.parse_args()

    masto = Masto()

    if args.instance:
        instance_data = masto.instance_search(args.instance)
        print(json.dumps(instance_data, indent=2))

    if args.user:
        user_data_api = masto.username_search_api(args.user)
        if user_data_api:
            print(json.dumps(user_data_api, indent=2))
        user_data_db = masto.username_search(args.user)
        print(user_data_db)


if __name__ == "__main__":
    main()