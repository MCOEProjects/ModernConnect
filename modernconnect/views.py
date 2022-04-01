from django.http import JsonResponse
from db_utils import connection


# Create your views here.

def index(request) -> JsonResponse:
    return JsonResponse({"message": "Congratulations, This is working!"})


def skills(request) -> JsonResponse:
    with connection() as con, con.cursor() as cur:
        cur.execute("select skill_id, title from skills")
    skillList = cur.fetchall()
    return JsonResponse({"skills": skillList})