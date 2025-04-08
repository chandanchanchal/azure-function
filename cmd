wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt

https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python


Create:
Database name: TravelDB
Container name: Bookings
Partition key: /id
Leave throughput default for now.

pip install azure-functions azure-cosmos
mkdir -p TravelFunctionApp/BookingsFunction

# Create empty files
     touch BookingsFunction/__init__.py
     touch BookingsFunction/function.json
     touch host.json
     touch local.settings.json
     touch requirements.txt
     touch .funcignore
mkdir .venv
sudo snap install tree
az login --use-device-code

