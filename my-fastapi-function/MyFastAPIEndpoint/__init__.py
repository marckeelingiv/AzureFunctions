import azure.functions as func
from .addition import add
from .multiplication import multiply

def main(req: func.HttpRequest, res: func.Out[func.HttpResponse]) -> None:
    try:
        # Parse query parameters from the HTTP request
        request_type = req.params.get('request_type')
        a = int(req.params.get('a'))
        b = int(req.params.get('b'))

        # Validate and perform the requested operation
        if request_type == "multiply":
            result = multiply(a, b)
        elif request_type == "add":
            result = add(a, b)
        else:
            res.set(func.HttpResponse(
                "Invalid request_type. Use 'add' or 'multiply'.",
                status_code=400
            ))
            return

        # Set the response result
        res.set(func.HttpResponse(f"Result: {result}", status_code=200))

    except Exception as e:
        res.set(func.HttpResponse(
            f"Error processing request: {str(e)}",
            status_code=500
        ))
