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

az functionapp create \
  --resource-group MyResourceGroup \
  --os-type Linux \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name my-new-func-app \
  --storage-account mystorageaccount123


curl -X POST "https://travel-func-app.azurewebsites.net/api/bookings?code=abc123XYZ==" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "B001",
    "customerName": "Ravi Sharma",
    "destination": "Goa",
    "date": "2025-04-10",
    "status": "Confirmed"
  }'

curl -X POST "https://travel-func-app.azurewebsites.net/api/bookings?code=6UjvDp" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "B002",
    "customerName": "Anjali Mehta",
    "destination": "Manali",
    "date": "2025-04-12",
    "status": "Pending"
  }'

curl -X GET "https://travel-func-app.azurewebsites.net/api/bookings?id=B001&code=6Ujv"


curl -X PUT "https://travel-func-app.azurewebsites.net/api/bookings?id=B001&code=6UjvDpBt" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Confirmed",
    "date": "2025-04-15"
  }'

curl -X DELETE "https://travel-func-app.azurewebsites.net/api/bookings?id=B001&code=6UjvD"

