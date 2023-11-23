
# Sidekick Pro Booster

Currently, when a referrer invites 20 new Sidekick signups, the referrer will receive the Pro plan forever.  This is a tool to help upgrade your Sidekick account to Pro plan for free.

## How to Use

### Option A: Standalone binaries

1. Go to [Releases page](https://github.com/anhdung98/sidekick-pro-booster/releases), then download the version suitable for your operating system.
2. Run following command in Command Prompt (Windows) or Terminal (MacOS):
```
./<execute-file-name> -c [INVITE_CODE]
```
with:
&nbsp;&nbsp;&nbsp;&nbsp;`<execute-file-name>` is the name of execute file downloaded in step 1
&nbsp;&nbsp;&nbsp;&nbsp;`INVITE_CODE` _(without square brackets)_ is the invitation code needed to boost.
> You can run command `./<execute-file-name> --help` to view all configure arguments.

### Option B: Build  Python application yourself
#### Prerequisites
You must installed **Python 3** and `pip` package manager before.
#### Guide
1. Clone this repository.
2. Install requirement packages by following command:
```
pip install requirements.txt
```
3. Run `main.py`:
```
python ./main.py
```