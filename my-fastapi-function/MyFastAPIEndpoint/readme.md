az functionapp create --resource-group AzureFunctionsTest --consumption-plan-location westus --runtime python --functions-version 4 --name MyFastAPIEndpoint --storage-account marc20241013

func azure functionapp publish MyFastAPIEndpoint --python

navigated to https://myfastapiendpoint.azurewebsites.net/api/CalculateFunction?request_type=multiply&a=7&b=3

contents of `local.settings.json`
```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python"
    }
}
```

contents of `function.json
```json
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["get", "post"],
      "route": "CalculateFunction"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ]
}

```