from django.conf import settings
from django.http import HttpResponse, Http404
import os
path = r'D:\Temp\TxGameDownload\MobileGamePCShared\com.activision.callofduty.shooter.zip'

def up(request):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    with open(r'D:\Temp\TxGameDownload\MobileGamePCShared\com.activision.callofduty.shooter.zip','rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

