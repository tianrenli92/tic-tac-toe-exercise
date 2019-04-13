from django.template.defaulttags import register


# reference:
#   https://stackoverflow.com/questions/8000022/django-template-how-to-look-up-a-dictionary-value-with-a-variable
#   https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#writing-custom-template-filters
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
