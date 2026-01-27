#!/bin/bash

USERNAME="rapidascent"
PASSWORD="default"

useradd -m -s /bin/bash $USERNAME

echo "$USERNAME:$PASSWORD" | chpasswd

# get UID
UID_NUM=$(id -u $USERNAME)

echo "User created successfully"
echo "Username: $USERNAME"
echo "UID: $UID_NUM"
