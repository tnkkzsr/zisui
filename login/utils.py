from blog.models import ZisuiPost

def get_user_posts(user):
    """
    ユーザーの投稿一覧を取得する関数

    return:
        all_record_list:すべての作成した順に並べたもの
        post_with_image_list:画像がある投稿をPKの降順に並べたもの

    """

    zisui_list = ZisuiPost.objects.filter(author=user)
    all_record_list = zisui_list.order_by("created")
    post_with_image_list = zisui_list.exclude(image = "images/1087_01.jpg").order_by("-pk")

    return all_record_list,post_with_image_list