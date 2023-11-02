curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

sudo apt-get update

sudo apt-get install -y unixodbc-dev libgssapi-krb5-2

ACCEPT_EULA=Y sudo apt-get install -y msodbcsql18
ACCEPT_EULA=Y sudo apt-get install -y mssql-tools18

echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
# source ~/.bashrc