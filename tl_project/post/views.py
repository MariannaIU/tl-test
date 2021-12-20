from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from members.models import Member
import requests
from django.views.generic import TemplateView, ListView
from django.db.models import Q

import json

# Create your views here.

def upload_user(request):
    user_obj = requests.get('http://jsonplaceholder.typicode.com/users')
    user_json = user_obj.json()

    user_count = 0
    for user in user_json:
        member_id = user.get('id')
        member_name = user.get('name')
        user_name = user.get('username')
        email = user.get('email')
        address_street = user.get('address').get('street')
        address_suite = user.get('address').get('suite')
        address_city = user.get('address').get('city')
        address_zipcode = user.get('address').get('zipcode')
        address_geo_lat = user.get('address').get('geo').get('lat')
        address_geo_lng = user.get('address').get('geo').get('lng')
        phone = user.get('phone')
        website = user.get('website')
        company_name = user.get('company').get('name')
        company_catchPhrase = user.get('company').get('catchPhrase')
        company_bs = user.get('company').get('bs')

        exist_user = Member.objects.filter(id=member_id).first()
        if not exist_user:
            user_data = {
                'id': member_id,
                'name': member_name,
                'user_name': user_name,
                'email': email,
                'street':address_street,
                'suite':address_suite,
                'city': address_city,
                'zipcode': address_zipcode,
                'geo_lat': address_geo_lat,
                'geo_lng': address_geo_lng,
                'phone': phone,
                'website': website,
                'company_name': company_name,
                'company_catchPhrase': company_catchPhrase,
                'company_bs': company_bs,
            }
            Member.objects.create(**user_data)
            user_count += 1


    #data = f'New user object has been created with id {member_obj.id}'
    return render(request, 'post/post/user_added.html',{'user_count': user_count})

def upload_post(request):
    post_obj = requests.get('http://jsonplaceholder.typicode.com/posts')
    post_json = post_obj.json()

    post_count = 0
    for post in post_json:
        post_id = post.get('id')
        author = post.get('userId')
        title = post.get('title')
        body = post.get('body')
        member = Member.objects.get(id=author)

        exist_post = Post.objects.filter(id=post_id).first()
        if not exist_post:
            post_data = {
                'id': post_id,
                'author': member,
                'title': title,
                'body': body,

            }
            Post.objects.create(**post_data)
            post_count += 1


    #data = f'New user object has been created with id {member_obj.id}'
    return render(request, 'post/post/post_added.html', {'post_count': post_count})

def post_list(request, **kwargs):
    query = request.GET.get('q')
    if query:
        filtered_posts = Post.objects.filter(Q(author__name__icontains=query) | Q(title__icontains=query) | Q(body__icontains=query))
        return render(request, 'post/post/list.html', {'posts': filtered_posts, 'query':query})
    else:
        posts = Post.objects.all()
        return render(request, 'post/post/list.html', {'posts': posts})


