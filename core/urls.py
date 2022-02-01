from django.urls import path
from core.views import index, article, privacy, terms, signup, login


urlpatterns = [
    path('index.html', index, name='index'),
    path('article-details.html', article, name='artigo'),
    path('privacy-policy.html', privacy, name='privacidade'),
    path('terms-conditions.html', terms, name='termos'),
    path('log-in.html', login, name='login'),
    path('sign-up.html', signup, name='signup')

]