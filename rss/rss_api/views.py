from django.views import View
from django.http import JsonResponse
import feedparser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import RSSFeed
from datetime import datetime
import time

@method_decorator(csrf_exempt, name='dispatch')
class AddRSSFeedView(View):
    def post(self, request):
        website_url = request.POST.get('website_url')

        # Obtener feeds RSS del sitio web
        parsed_feed = feedparser.parse(website_url)

        # Lista para almacenar los feeds agregados
        added_feeds = []

        # Guardar los feeds RSS en la base de datos
        for entry in parsed_feed.entries:
            published_date = entry.get('published_parsed', None)
            if published_date:
                # Convierte la fecha a un formato estándar antes de analizarla
                formatted_date = datetime.fromtimestamp(time.mktime(published_date))
                rss_feed = RSSFeed(
                    title=entry.get('title', ''),
                    link=entry.get('link', ''),
                    description=entry.get('summary', ''),
                    pub_date=formatted_date
                )
                rss_feed.save()
                added_feeds.append({
                    'title': rss_feed.title,
                    'link': rss_feed.link,
                    'description': rss_feed.description,
                    'pub_date': rss_feed.pub_date.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                # Si no hay fecha válida, puedes manejarlo de acuerdo a tus necesidades
                pass

        # Devolver la respuesta con los feeds agregados
        response_data = {
            'message': 'Feeds RSS agregados correctamente',
            'added_feeds': added_feeds
        }
        return JsonResponse(response_data, status=200)
