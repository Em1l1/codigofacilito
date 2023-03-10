ssh-copy-id eduardo@ip

# root
ssh-copy-id root@ip

# Autenticate for ssh-public
sudo nvim /etc/ssh/sshd_config

# line
# PasswordAuthentication yes = no >PasswordAuthentication

sudo service ssh restart
