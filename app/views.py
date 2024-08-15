from django.shortcuts import render
from .forms import ContactForm, CommentForm
from django.views.generic.edit import FormView
from .models import Book, Gallery, About, PortfolioCategory, Portfolio, Blog, Category, Comment, SlideShow
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView,FormMixin
from django.urls import reverse


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"  # Home-page ga o'tish uchun

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for field in form.errors:
            form.fields[field].widget.attrs['placeholder'] = "xato"
        return self.render_to_response(self.get_context_data(form=form))


def home_view(request):
    slide = SlideShow.objects.all()
    context = {
        "slides": slide,
    }
    return render(request, "index.html", context)


class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'portfolios'
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context


def books_view(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'books.html', context)


def gallery_view(request):
    galleries = Gallery.objects.all()
    context = {
        "galleries": galleries,
    }
    return render(request, "gallery.html", context)

class SingleGalleryView(DetailView):
    model = Gallery
    template_name = 'gallery-single.html'
    context_object_name = 'gallery_item'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



def about_view(request):
    about = About.objects.all()
    context = {
        "abouts": about,
    }
    return render(request, "about.html", context)

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = "blog-masonry.html"
    paginate_by = 1

    def get_queryset(self):
        return Blog.objects.order_by('-created_date')
    
    def get_context_data(self, **kwargs):
        print(self.request.scheme)
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class BlogDetailView(FormMixin,DetailView):
    model = Blog
    template_name = "blog-single.html"
    context_object_name = "blog"
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(blog=context.get('blog'))
        context['comments_count'] = Comment.objects.filter(blog=context.get('blog')).count()

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.blog = self.object
        form.save()
        return super(BlogDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-single-page', kwargs={'pk': self.object.pk})


