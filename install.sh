#!/bin/bash

echo "Installing tw - TodoWalp"

echo "Cloning into the repository todowalp"
printf "\n"
git clone https://github.com/linuxdotexe/todowalp ~/.local/bin/todowalp/

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
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp/tw' >> ~/.bashrc
    elif [ "$shell_name" == zsh ]; then
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp/tw' >> ~/.zshrc
    elif [ "$shell_name" == fish ]; then
        echo 'export PATH=$PATH:$HOME/.local/bin/todowalp/tw' >> ~/.config/fish/config.fish
    fi
}
add_to_path
printf "\n"
echo "Try pressing tw and see if it works"
