from django.urls import path

from .views import (
    discussion_list_view,
    discussion_details_view,
    discussion_solutions_view,
    answer_upvote_view,
    answer_downvote_view,
    answer_update_view,
    answer_submit_view,
    answer_delete_view,

    discussion_create_view,
    discussion_update_view,
    discussion_delete_view,
)

urlpatterns = [
    path('', discussion_list_view, name="discussion-list"),
    path('<slug:discussion>/', discussion_details_view, name="discussion-details"),
    path('<slug:discussion>/answers', discussion_solutions_view, name='discussions-solutions-view'),
    path('<slug:answer_slug>/upvote', answer_upvote_view, name='answer-upvote'),
    path('<slug:answer_slug>/downvote', answer_downvote_view, name='answer-downvote'),
    path('create', discussion_create_view, name='discussion-create'),
    path('<slug:discussion>/update', discussion_update_view, name='discussion-update'),
    path('<slug:discussion>/delete', discussion_delete_view, name='discussion-delete'),

    path('<slug:discussion_slug>/submit_answer', answer_submit_view, name='submit-answer'),
    path('<slug:discussion_slug>/<slug:answer_slug>/edit', answer_update_view, name='answer-update'),
    path('<slug:discussion_slug>/<slug:answer_slug>/delete', answer_delete_view, name='answer-delete')

]
