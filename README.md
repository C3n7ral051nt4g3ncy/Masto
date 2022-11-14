# **Masto OSINT Tool**

<img width="999" alt="Masto_logo" src="https://user-images.githubusercontent.com/104733166/200212151-c5eea622-adfe-4209-ad43-f667f743e5fd.png">

<br>

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![MIT License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/C3n7ral051nt4g3ncy/Masto/blob/master/LICENSE) 
<img src="https://img.shields.io/github/v/tag/C3n7ral051nt4g3ncy/Masto?color=bright%20green&label=Version&logo=github">
[![HitCount](http://hits.dwyl.com/C3n7ral051nt4g3ncy/Masto.svg)](http://hits.dwyl.com/C3n7ral051nt4g3ncy/Masto) 
<img src="https://img.shields.io/github/stars/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logo=github">
<img src="https://img.shields.io/github/forks/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logoColor=white&logo=github">
<img src="https://img.shields.io/github/last-commit/C3n7ral051nt4g3ncy/MAsto?color=bright%20green&label=Last%20commit">
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

</div>



## 🐘 **About Masto**

**Masto provides information/intelligence on [Mastodon.social](https://mastodon.social) users and instances (servers)** 
<br>
## 🚀 **Masto capabilities**
**Masto OSINT Tool** helps to:
- Find user ID
- Find exact username match across instances (the tool currently pulls 3 accounts with the username **```OSINT```** from 3 instances, whereas the mastodon.social search bar browser search returns one result, and returns many accounts that only start with ```osint```, such as ```osinttechnical```, but no exact match is found through a search done via browser.
- Find all (possible) accounts belonging to a user without logging in to Mastodon (**Mastodon requires users to log in and after the first 5 results you get**: ```401 Search queries pagination is not supported without authentication```
- Find username correlation (can't be found by searching on the Mastodon.social website)
- Check if the user is a bot 
- Check if the user has to approve followers manually
- Check if the account is a group
- Check if the account is locked
- Check if the user opted to be listed on the profile directory
- Get avatar link witn an **additional choice** of opening the avatar in your browser
- Get profile creation date
- Get number of followers & following
- Get number of posts
- Get user last message date 
- Get user's bio
- Get user's hashtags
- Get header image link
- Get link to followers and following
- Get user public key (PEM -Privacy-enhanced Electronic Mail) 

### **Additional instance (server) feature**
**This is a nice feature**, if you type ```social.network.europa.eu``` on [Mastodon.social](https://mastodon.social/search) , you won't get a result as the instance is set to ```not discoverable```. <br>

This function helps to:
- Get information on an instance
- Get instance Admin ID
- Get instance email 
- Get a short description
- Get server thumbnail link
- Get instance creation date 
- Get instance language used
- Get instance admin count of followers and following
- Get instance admin last status date
- Get header image link and avatar link
- Get instance display name
- Get admin url
- Get admin avatar
- Check if instance admin account is locked
- Check if registration is required and if the admin needs to approve the request
- Check if the admin is a bot 

## 🛠️ **Installation**

```git clone https://github.com/C3n7ral051nt4g3ncy/Masto```
<br>
<br>
```pip3 install -r requirements.txt```
<br>
<br>
```python3 masto.py```

## ⭐ **Tool (successful) use cases**

**Use case 1**: **Searching for a user and bypassing the profile directory option**:
- Tried searching via browser both terms `webbreacher` and `@Webbreacher`: **1 result** --> `@Webbreacher@mastodon.social`
- Searched `Webbreacher` on **Masto**: 2 results --> **`@Webbreacher@mastodon.social`** + **`@Webbreacher@counter.social`**
- On the counter.social profile, `@Webbreacher's` settings are --> user opted to be on the profile directory = `False`, this is why the browser search didn't find the counter.social profile!
- 🪄 **Masto successful outcome**: **Masto found both accounts**.

<br>

**Use case 2**: **Searching without getting a 401 error**:
- Many people don't want an account on Mastodon, if you don't have an account, you can search on Mastodon but you will only get 5 results. Clicking
on `load more` will give you a 401 error and request the user to log in.
- 🪄 **Masto successful outcome**: **You can use Masto without logging in to Mastodon**, you won't get a 401 error.

<br>

**Use case 3**: **Getting fully accurate username search results**:
- Tried searching `OSINT` and `@OSINT` via browser, Mastodon returned quite erratic results, with many accounts that just **begin with** `osint`, such as the user `@Osinttechnical`
- 🪄 **Masto successful outcome**: **Masto found 3 accurate `@osint`** user accounts from 3 instances.

<br>

**Use case 4**: **Getting information on locked instances**:
- Tried searching for the instance [0sint.social](https://0sint.social/about), there isn't much information via a browser search.
- 🪄 **Masto successful outcome**: **Masto found more information on the instance and on the admin, including email address.**


## ❌ **Tool (unsuccessful) use cases**

**Use case 1**: **Not finding an existing user**:
- Tried searching user `sector035` via browser, Mastodon returned no result. So far this is normal because `@sector035` has settings to --> user opted to be on the profile directory = `False`
- Tried searching with **Masto OSINT Tool**, no result either. The Mastodon API isn't 100% reliable. [See here for explanation](https://github.com/C3n7ral051nt4g3ncy/Masto#issues-with-not-finding-a-user)
- ❌ Masto unsuccessful outcome: **Masto found no user**, even though the user exists.
- 🔩 **Fix**: Working on a fix and a solution suggested by [@Webbreacher](https://github.com/WebBreacher)

## 🐘 **Mastodon.social understanding**
The **same username** can be found across different instances(servers):
- example: @osint@mastodon.social | @osint@mstdn.social | @osint@counter.social
- finding the same username on different instances does not prove it's the same person behind each account
- This may cause impersonation issues in the future, although each instance can only have **one unique username** in the server, and ALL users should verify their accounts with the `<a rel="me"` attribute which helps others identifying a scammer/impersonator. 

## 👥 **Testing on known users**

- For the 1st function, try: ```Gargron```, the founder of [Mastodon.social](https://mastodon.social), this pulls a wopping 11 accounts!!! (same username doesn't prove the 11 accounts belong to the Mastodon Developper).
- For the 2nd function, searching only on [Mastodon.social](https://mastodon.social), try: ```osint```
- For the 3rd function, searching only on [mstdn.social](https://mstdn.social), try: ```stux```
- For the 4th function, searching for instances, try: ```social.network.europa.eu```

## 🗒️ **Issues with not finding a user**
- You may know of a valid user & have the link to the user's profile, you input the username on Masto but get no result.
- I asked the Mastodon Team about this api issue, they replied:
> There is no global search, the server will reply with what it knows about. If it has not encountered the account, it will not return it in search results.

## 🙏 **Thanks**
- Thanks to [@Webbreacher](https://github.com/WebBreacher) for his input, help and ideas.
I learn a great deal from him, a great instructor and inspiring person.
- Thanks to [@Roman-Kasianenko](https://github.com/Roman-Kasianenko) for his help.



## 📝 **License**

[MIT License](https://opensource.org/licenses/MIT) <br>
*Tool made for the OSINT and Cyber community, feel free to contribute code.*

<img width="66" src="https://user-images.githubusercontent.com/104733166/200310377-be6d8187-8366-4968-b730-a5c215b310ec.png">
