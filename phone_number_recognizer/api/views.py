from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.request_processors import RecognizePhoneRequestProcessor


class RecognizePhoneView(APIView):
    def post(self, request):
        processor = RecognizePhoneRequestProcessor(dict(request.data))
        errors = processor.check()
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(processor.process())
