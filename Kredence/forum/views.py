from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
import string

from pip._vendor.requests import Response

from .models import (
    Discussion,
    Answer
)


@login_required
def discussion_create_view(request):
    context = {
        "title": "Create Discussion",
    }
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        body = request.POST.get('body')
        slug = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))

        Discussion.objects.create(
            user=user,
            title=title,
            body=body,
            slug=slug
        ).save()
        context['create'] = "Successful"

        return redirect('')

    return render(request, "forum/create.html", context)


def discussion_list_view(request):
    discussions = Discussion.objects.all()
    context = {
        "title": "Discussions",
        "discussions": discussions
    }

    return render(request, "forum/list.html", context)


def discussion_details_view(request, discussion):
    try:
        discussion = Discussion.objects.get(slug=discussion)
    except Discussion.DoesNotExist:
        return HttpResponse({'error': 'Discussion forum not found'})

    answers = Answer.objects.filter(discussion=discussion)

    context = {
        "title": discussion.title,
        "discussion": discussion,
        "answers": answers
    }

    return render(request, "forum/details.html", context)


def discussion_update_view(request, discussion):
    try:
        discussion = Discussion.objects.get(slug=discussion)
    except Discussion.DoesNotExist:
        return HttpResponse({'error': 'Discussion Not found'})

    if request.method == "POST":
        updated_title = request.POST.get('title')
        updated_body = request.POST.get('body')

        discussion.title = updated_title
        discussion.body = updated_body
        discussion.save()

    context = {
        "title": "Update answer",
        "discussion": discussion
    }
    return render(request, "forum/update_discussion.html", context)


def discussion_delete_view(request, discussion):
    try:
        body = Discussion.objects.get(slug=discussion)
    except Discussion.DoesNotExist:
        return HttpResponse({'error': 'Discussion not found'})

    operation = body.delete()

    return redirect(str('forum/' + discussion))


def answer_upvote_view(request, answer_slug):
    try:
        answer = Answer.objects.get(slug=answer_slug)
    except Answer.DoesNotExist:
        return HttpResponse({'error': 'Answer not found'})

    answer.votest += 1
    answer.update()

    return HttpResponse({'success:': 'Answer up-voted'})


def answer_downvote_view(request, answer_slug):
    try:
        answer = Answer.objects.get(slug=answer_slug)
    except Answer.DoesNotExist:
        return HttpResponse({'error': 'Answer not found'})

    answer.votest -= 1
    answer.update()

    return HttpResponse({'success:': 'Answer down-voted'})


def answer_submit_view(request, discussion_slug):
    if request.method == "POST":
        discussion = request.POST.get(slug=discussion_slug)
        user = request.user
        slug = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        answer = request.POST.get('answer')

        Answer.objects.create(
            discussion=discussion,
            user=user,
            slug=slug,
            answer=answer,
        ).save()
        return redirect(str('forum/' + discussion_slug))


def answer_update_view(request, answer_slug):
    try:
        answer = Answer.objects.get(slug=answer_slug)
    except Answer.DoesNotExist:
        return HttpResponse({'error': 'Answer Not found'})

    if request.method == "POST":
        updated_answer = request.POST.get('answer')

        answer.answer = updated_answer
        answer.save()

    context = {
        "title": "Update answer",
        "answer": answer
    }
    return render(request, "forum/update_answer.html", context)


def answer_delete_view(request, answer_slug):
    try:
        body = Answer.objects.get(slug=answer_slug)
    except Answer.DoesNotExist:
        return HttpResponse({'error': 'Answer not found'})

    operation = body.delete()
    return redirect(str('forum/' + answer_slug))
