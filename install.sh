#!/bin/bash

echo "TODOWALP INSTALLER"
printf "\n"

echo "Before installing todowalp, you need to meet the following prerequisites:"
echo "  imagemagick - creates the wallpaper"
echo "  feh - sets the wallpaper"
printf "\n"

function install_dependencies() {
    printf "Select your distro"
    printf "\n"
    printf "1. Debian/Ubuntu based"
    printf "\n"
    printf "2. Arch Linux based"
    printf "\n"
    printf "3. Other"
    printf "\nEnter a number: "
    read -r distro_name
    if [ "$distro_name" == "1" ] ; then
        sudo apt-get install feh imagemagick
    elif [ "$distro_name" == "2" ]; then
        sudo pacman -S feh imagemagick
    elif [ "$distro_name" == "3" ]; then
        echo "Dependency installation step is skipped. You will have to manually install feh and imagemagick for todowalp to work."
    fi
}
install_dependencies

echo "Installing tw - TodoWalp"

echo "Cloning into the repository todowalp"
printf "\n"
git clone https://github.com/linuxdotexe/todowalp ~/.local/bin/todowalp

echo "Adding todowalp to the path"
printf "\n"

function add_to_path() {
    printf "Select your default shell"
    printf "\n"
    printf "1. bash"
    printf "\n"
    printf "2. zsh"
    printf "\n"
    printf "3. fish"
    printf "\n"
    read -r shell_name
    if [ "$shell_name" == bash ] ; then
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp' >> ~/.bashrc
    elif [ "$shell_name" == zsh ]; then
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp' >> ~/.zshrc
    elif [ "$shell_name" == fish ]; then
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp' >> ~/.config/fish/config.fish
    fi
}
add_to_path
printf "\n"
echo 'Try "tw -df" to verify installation'
