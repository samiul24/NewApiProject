"""
Django settings for ApiProject project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR) # Main project directory is the base directory

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-5y8p)r()+)8msmrez-a287e48w96q=%&i)v^r=lv30wt*+2sho'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = []

# Read environment variables
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=list,
)
print(type(env))

env_file_path = os.path.join(BASE_DIR, '.env')
print(env_file_path)
environ.Env.read_env(env_file_path) # read .env file and override env variables


DEBUG = env('DEBUG')
print(DEBUG)
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt',
]

LOCAL_APPS = [ 
    'ApiApp'
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

