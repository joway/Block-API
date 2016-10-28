from rest_framework import routers

from activity.apis import ActivityViewSet
from analysis.apis import PageViewViewSet
from article.apis import ArticleViewSet
from comment.apis import CommentViewSet
from oauth.apis import OauthViewSet
from social.apis import SocialAuthViewSet
from user.apis import ProfileViewSet, AuthViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"user", ProfileViewSet, base_name="user")
router.register(r"auth", AuthViewSet, base_name="auth")
router.register(r"social", SocialAuthViewSet, base_name="social")
router.register(r"oauth", OauthViewSet, base_name="oauth")
router.register(r"article", ArticleViewSet, base_name="article")
router.register(r"comment", CommentViewSet, base_name="comment")
router.register(r"activity", ActivityViewSet, base_name="activity")
router.register(r"pv", PageViewViewSet, base_name="pv")
