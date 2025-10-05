def function_cicd(request):
    """Responds to any HTTP request."""
    
    # Handle GET requests (e.g., from browser)
    if request.method == 'GET':
        message = request.args.get('message')
        return message if message else 'Function - 1 with V1.0 with CI/CD Pipeline'

    # Handle POST requests with JSON
    if request.headers.get('Content-Type') == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and 'message' in request_json:
            return request_json['message']
        else:
            return 'No message found in JSON payload'
    
    # Fallback for unsupported content types
    return 'Unsupported Media Type', 415