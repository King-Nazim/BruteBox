#!/bin/bash
pkgs=(python python2)
for i in "${pkgs[@]}"; do
if ! hash $i > /dev/null 2>&1; then
printf "\033[1;35mPKG: \033[33m${i} not found! \033[32mInstalling....\033[00m\n"
pkg install $i -y
fi
done
pips=(user_agent mechanize logging proxylist argparse requests bs4 secure-smtplib colorama pyfiglet zipfile brute unrar tqdm)
for j in "${pips[@]}"; do
printf "\033[1;35mPIP: \033[33m${j} \033[32mInstalling....\033[00m\n"
if [[ $j == "zipfile" ]]; then
pip2 install $j
else
pip install $j
fi
done
