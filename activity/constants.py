class ActivityTypes:
    ARTICLE = 1
    PHOTO = 2
    COMMENT = 3
    BULLSHIT = 4


ACTIVITY_TYPE_CHOICES = (
    (ActivityTypes.ARTICLE, '发布了文章'),
    (ActivityTypes.PHOTO, '发布了照片'),
    (ActivityTypes.COMMENT, '添加了评论'),
    (ActivityTypes.BULLSHIT, '闲扯了几句'),
)
