from app.internal.services.user_service import try_get_user_by_param
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.contrib import messages
from app.internal.models.family_role import FamilyRole


class JWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/'] or request.path.startswith('/schedule/'):
            try:
                id = request.COOKIES.get('id')
                if not id:
                    return redirect('/auth')
                
                user = try_get_user_by_param('id', id)
                if user is None:
                    return redirect('/auth')

                if not hasattr(request, 'custom_user'):
                    request.custom_user = None
                
                request.custom_user = user
            except Exception as e:
                print(f"Exception occurred: {e}")
                return redirect('/auth')
            
        if request.path.startswith('/schedule/'):
            try:
                family_id = request.COOKIES.get('family')
                family_role = FamilyRole.objects.filter(family__id=family_id, app_user=request.custom_user).first()
                request.family = family_role.family
                
            except Exception as e:
                messages.error(request, 'Семья не выбрана') 
                return redirect('/')