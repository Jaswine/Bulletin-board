from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View

from base.utils.token_auth_middleware import TokenAuthMiddleware

from base.service.advertisement_services import AdvertisementService
from base.utils.advertisement_utils import AdvertisementUtil


class AdvertisementListView(View):
    @method_decorator(TokenAuthMiddleware.token_required)
    def get(self, request):
        print(request)
        advertisements = AdvertisementService.find_all()
        response = AdvertisementUtil.list(advertisements)
        return JsonResponse(response, safe=False, status=200)


class AdvertisementDetailView(View):
    @method_decorator(TokenAuthMiddleware.token_required)
    def get(self, request, advertisement_id):
        advertisement = AdvertisementService.find_by_id(advertisement_id)
        if not advertisement:
            return JsonResponse({
                'message': 'Advertisement not found',
            }, status=404)

        response = AdvertisementUtil.detail(advertisement)
        return JsonResponse(response, status=200)

