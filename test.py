def log_function_checker(request):
    if request.method == 'POST':
        csrf_token = request.POST.get("csrfmiddlewaretoken")
        log_code = request.POST.get('log_code')
        api_code = request.POST.get('api_code')
        dirname = os.path.dirname(__file__)
        log_filename = os.path.join(dirname, "playground/A9/main.py")
        api_filename = os.path.join(dirname, "playground/A9/api.py")
        f = open(log_filename,"w")
        f.write(log_code)
        f.close()
        f = open(api_filename,"w")
        f.write(api_code)
        f.close()
        # Clearing the log file before starting the test
        f = open('test.log', 'w')
        f.write("")
        f.close()
        url = "http://127.0.0.1:8000/2021/discussion/A9/target"
        payload={'csrfmiddlewaretoken': csrf_token }
        requests.request("GET", url)
        requests.request("POST", url)
        requests.request("PATCH", url, data=payload)
        requests.request("DELETE", url)
        f = open('test.log', 'r')
        lines = f.readlines()
        f.close()
        return JsonResponse({"message":"success", "logs": lines},status = 200)
    else:
        return JsonResponse({"message":"method not allowed"},status = 405)
