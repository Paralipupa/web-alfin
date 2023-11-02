sudo apt install curl
sudo apt install gnupg2
sudo curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
sudo curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt update
sudo apt install msodbcsql18
sudo apt install mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# source ~/.bashrc

# sqlcmd -S tcp:<ip_adress> -d <db_name> -U <login> -P <password>
