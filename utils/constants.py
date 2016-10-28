class ContentTypes:
    ARTICLE = 1
    PHOTO = 2
    BULLSHIT = 3
    COMMENT = 4


CONTENT_TYPE_CHOICES = (
    (ContentTypes.ARTICLE, '文章'),
    (ContentTypes.PHOTO, '照片'),
    (ContentTypes.BULLSHIT, '闲扯'),
    (ContentTypes.COMMENT, '评论'),
)
