async def log_requests(request, call_next):
    print(f"Request received: {request.url}")
    response = await call_next(request)
    return response