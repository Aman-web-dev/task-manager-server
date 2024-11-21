import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only process JWT for /api/ endpoints
        if request.path.startswith('/api/'):
            token = None

            # Check if the Authorization header is present
            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']
                if auth_header.startswith("Bearer "):
                    token = auth_header.split(" ")[1]  # Extract token after "Bearer"
                else:
                    return JsonResponse({'error': 'Authorization token must be in Bearer format'}, status=400)

            # Proceed if token is found
            if token:
                try:
                    # Decode the JWT token
                    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                    username = decoded.get('username')  # Get username from decoded payload

                    # Retrieve the user object from the database
                    user = User.objects.filter(username=username).first()

                    # If user exists, attach it to the request
                    if user:
                        request.user = user
                    else:
                        return JsonResponse({'error': 'User not found'}, status=404)

                except jwt.ExpiredSignatureError:
                    return JsonResponse({'error': 'Token has expired'}, status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({'error': 'Invalid token'}, status=401)
            else:
                # If no token is found, set request.user to None or proceed as needed
                request.user = None

        return self.get_response(request)
