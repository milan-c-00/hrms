# middleware.py

class ClearSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Get the requested URL path
        path = request.path

        # Check if the requested URL path is not documents/add
        if path != '/documents/add/':
            # Clear the session
            request.session['uploads_count'] = 0
