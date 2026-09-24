from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'kotoba_search.urls'

DEBUG = os.getenv('DEBUG', 'False') == 'False'

allowed_hosts_env = os.getenv('ALLOWED_HOSTS')
if allowed_hosts_env:
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(',')]
else:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '160.251.213.22', 'kotoba-search.net', 'www.kotoba-seaarch.net']

# ドメインを取得したら 'https://your-domain.com' を追加
# Django 4.0以降、フォーム送信（POST）のCSRFチェックで必須
CSRF_TRUSTED_ORIGINS = [
    'http://160.251.213.22',
    'https://160.251.213.22',
    # ドメインを取得したら以下も追加（例）
    # 'https://your-domain.com',
]



SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError('SECRET_KEYが設定されていません')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGIN_REDIRECT_URL = '/'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
