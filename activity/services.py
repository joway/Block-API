from activity.models import Activity
from utils.constants import ContentTypes


class ActivityService(object):
    @classmethod
    def create_activity(cls, user, obj, type):
        if type == ContentTypes.ARTICLE:
            description = '发表了文章 << %s >>' % obj.title
        elif type == ContentTypes.BULLSHIT:
            description = '闲扯了几句'
        elif type == ContentTypes.COMMENT:
            description = '在 [ %s ] 下发表了评论' % obj.target
        elif type == ContentTypes.PHOTO:
            description = '发表了新相片'
        else:
            raise Exception('无效 type ')
        obj = Activity.objects.create(owner=user, description=description, type=type)
        obj.save()
        return obj
