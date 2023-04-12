# yufine-training

## Github Codespaces setup

1. Create a feature branch in github and open codespaces for that branch
https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository
2.  Install flask and run 
```
pip install flask

export FLASK_APP=helloworld.py
export FLASK_ENV=development
flask run
```
3. Visit your site at the printed URL in your terminal. For ex:
* Running on http://127.0.0.1:5000

4. To use external applications to query your application, select the antenna on the lower left corner of Codespaces, and right click the port.
    Change port visibility to public.

## Windows setup from scratch

### Development Environment

1. Install WSL (Windows Subsystem for Linux)
    - Open powershell and run `wsl --install`
    - https://learn.microsoft.com/en-us/windows/wsl/install
2. Restart machine and set your password for your Linux subsystem
3. Install Homebrew https://brew.sh/
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`


```
📝 The following commands will all be in WSL. If you've closed WSL, open again by typing WSL in your windows menu, or by hitting windows+r and running `wsl`)
```


4. Complete brew setup
```sh
==> Next steps:
- Run these three commands in your terminal to add Homebrew to your PATH:
    echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /home/tae/.profile
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/tae/.profile
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
- Install Homebrew's dependencies if you have sudo access:
    sudo apt-get install build-essential
  For more information, see:
    https://docs.brew.sh/Homebrew-on-Linux
- We recommend that you install GCC:
    brew install gcc
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh
 ```
 5. Install and configure git
    - `brew install git`
    - `git config --global user.email "you@example.com"`
    - `git config --global user.name "Your Name"`
 6. Install an Integrated Development Environment (code editor)
    - I recommend VS Code as a good starting point
    - https://code.visualstudio.com/
 7. Setup github and ssh keys
    - Assuming there are no preexisting SSH keys, setup is as follows:
    - Create an ssh key in your WSL terminal: `ssh-keygen -t ed25519 -C "your_email@example.com"`
        - Make sure to replace your email in the above command.
        - You can enter a passphrase if you'd like, but skipping the prompts is fine.
    - Copy the SSH key you've just made, which you can output with the following command: `cat  ~/.ssh/id_ed25519.pub`
    - Enter the key into your github account settings: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

    - Reference: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

 8. Clone this repository:
    - Navigate to https://github.com/Snowrries/yufine-training
    - Click the green `Code` button
    - On the SSH tab, copy the topmost text:
    - git@github.com:Snowrries/yufine-training.git
    - In WSL, navigate to where you'd like this folder to be created. If you don't have a preference, the root directory is fine (`~/`)
    - Clone with the following command:
        - `git clone git@github.com:Snowrries/yufine-training.git`
 9. Open this repository in VS Code!
    - An easy way to locate the folder in your windows system:
        - Navigate into your code folder: `cd yufine-training`
        - Open in code: `code .`
        - This should open VS code with the workspace rooted at your current directory, which should show where exactly this repo lives in your windows filesystem. If you had cloned your repo at root, it is likely located at: `\\wsl.localhost\Ubuntu\home\{your username}\yufine-training`

At this point, you should be set up to start writing code.

 ### Local development

 #### Prerequisites
    - virtualenvironment
    - python

Install Flask

https://flask.palletsprojects.com/en/2.2.x/installation/
- Ensure you have Python 3.7 or newer

Install a python environment manager and its dependencies
https://github.com/pyenv/pyenv/wiki/common-build-problems
```
brew install pyenv openssl
```

Make sure you complete openssl setup:
```
echo 'export PATH="/home/linuxbrew/.linuxbrew/opt/openssl@3/bin:$PATH"' >> ~/.profile
```

```
sudo apt-get update
sudo apt install python3 python3-pip ipython3
sudo apt install python3-flask
```

Run the app:
```
export FLASK_APP=helloworld.py
export FLASK_ENV=development
flask run
```

A