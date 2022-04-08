from django.http import JsonResponse
from db_utils import connection

# Create your views here.

client_error = 400


def index(request) -> JsonResponse:
    return JsonResponse({"message": "Congratulations, This is working!"})


def skills(request) -> JsonResponse:
    with connection() as con, con.cursor() as cur:
        cur.execute("select skill_id, title from skills")
    skillList = cur.fetchall()
    return JsonResponse({"skills": skillList})


def register(request) -> JsonResponse:
    if not request.POST:
        print("A Post Request was expected.")
        return JsonResponse({'error': "A POST Request was expected."}, status=client_error)
    print(request.name)
    return JsonResponse({"message": "working"})


def login(request) -> JsonResponse:
    return JsonResponse({'message': "working"})
