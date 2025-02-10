import datetime

def simpleMiddle(get_response):
    def middleware(request):
        print(f"Before request [{datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')}] Request URL: {request.path}")
        response = get_response(request)
        print(f"After Request [{datetime.datetime.now().strftime('%y/%m/%d %S:%M:%H')}] Response Status: {response.status_code}")
        return response
    return middleware