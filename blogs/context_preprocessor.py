from blogs.models import category

def get_category(request):
    categories= category.objects.all()
    return dict(categories=categories)