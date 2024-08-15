from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, PortfolioListView,  books_view, gallery_view, SingleGalleryView, about_view, BlogListView,  BlogDetailView,ContactFormView

urlpatterns = [
    path('',home_view,name='home-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('books/',books_view,name='books-page'),
    path('gallery/', gallery_view, name='gallery-page'),
    path('gallery/<slug:slug>/', SingleGalleryView.as_view(), name='single_gallery'),
    path('about/',about_view,name='about-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name="blog-single-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)