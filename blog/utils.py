import random
import string
from django.utils.text import slugify
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=20)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def hashtag_generate(s):
    indice_t = []
    tags = []
    tmp_str = ''
    s = s.strip()
    for i in range(len(s)):
        if s[i] == "#":
            indice_t.append(i)
    for i in range(len(indice_t)):
        index = indice_t[i]
        if i == len(indice_t)-1:
            boundary = len(s)
        else:
            boundary = indice_t[i+1]
        index += 1
        while index < boundary:
            if s[index] in "`~!@#$%^&*()-_=+[]{}|\\:;'"",.<>?/ \n\t":
                tags.append(tmp_str)
                tmp_str = ''
                break
            else:
                tmp_str += s[index]
                index += 1
        if tmp_str != '':
            tags.append(tmp_str)
    return tags