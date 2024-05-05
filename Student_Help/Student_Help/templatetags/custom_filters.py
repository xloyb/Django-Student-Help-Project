from django import template

register = template.Library()

@register.filter(name='check_post_type')
def check_post_type(post):
    if post.logement:
        return "logement"
    elif post.transport:
        return "transport"
    elif post.stage:
        return "stage"
    elif post.evenement:
        return "evenement"
    elif post.recommandation:
        return "recommandation"
    else:
        return "unknown"
