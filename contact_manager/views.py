import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import NamesMan, NamesWoman


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Получаем данные из POST-запроса и сериализуем в json
        contact_id = data.get('contact_id')
        contact_name = data.get('name')
        print(contact_name)
        # Проверяем имя в базе данных
        gender = None
        if NamesMan.objects.filter(name=contact_name).exists():
            gender = "Мужчина"
        elif NamesWoman.objects.filter(name=contact_name).exists():
            gender = "Женщина"

        if gender:

            # Обновляем контакт в Битрикс24 с учетом пола
            payload = {"contact_id": contact_id, "gender": gender}
            response = requests.post('https://your-bitrix24-domain/', data=payload) # вставить ссылку на bitrix
            if response.status_code == 200:
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "error", "message": "Ошибка при обновлении контакта в Битрикс24"})
        else:
            return JsonResponse({"status": "error", "message": "Имя не найдено в бд"})
    else:
        return JsonResponse({"status": "error", "message": "Убедитесь, что вы отправляете POST запрос"})
