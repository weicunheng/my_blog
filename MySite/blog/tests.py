from django.test import TestCase

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySite.settings")
    import django
    django.setup()
    from blog import models
    ret = models.Article.objects.filter(created_time__year=2018,
                                    created_time__month=4)
    #2018-04-28 11:52:13.000000
    # print(ret[0].created_time.month)
    print(ret)