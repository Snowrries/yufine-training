# yufine-training

## Windows setup from scratch

### Development Environment

1. Install WSL
    - Open powershell and run `wsl --install`
    - https://learn.microsoft.com/en-us/windows/wsl/install
2. Restart machine and set your password for your Linux subsystem
3. Install Homebrew https://brew.sh/
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
4. Complete brew setup:
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
 5. Install git
    - `brew install git`
 6. Install an Integrated Development Environment (code editor)
    - I recommend VS Code as a good starting point
