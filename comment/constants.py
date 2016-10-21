class CommentTypes:
    ARTICLE = 1
    PHOTO = 2
    BULLSHIT = 3


COMMENT_TYPE_CHOICES = (
    (CommentTypes.ARTICLE, '文章'),
    (CommentTypes.PHOTO, '照片'),
    (CommentTypes.BULLSHIT, '闲扯'),
)
