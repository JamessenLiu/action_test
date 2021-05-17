from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class ActionView(APIView):
    def get(self, request):

        url = "https://dev-v2.bundleb2b.net/api/api/v2/stores/currencies?storeHash=1i6zpxpe3g"

        resp = requests.get(url)

        data = {
            "code": 200, "message": "success",
                "data": resp.json().get("data")}

        return Response(data)
