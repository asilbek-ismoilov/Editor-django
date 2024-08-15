from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='Images/gallery') 
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)   
    slug = models.SlugField(unique=True, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
     
class Book(models.Model):
    spine_image = models.ImageField(upload_to='Books/spinel')
    cover_image = models.ImageField(upload_to='Books/coverl')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    about = models.TextField()
    by_name = models.CharField(max_length=100)
    data = models.CharField(max_length=12)
    pages = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} {self.name} "

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    image = models.ImageField(upload_to='Images/portfolio')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class About(models.Model):
    image = models.ImageField(upload_to='Images/about') 
    content = RichTextField()
    name = models.CharField(max_length=50, default='Asilebk')
    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Images/blog')
    created_date = models.DateTimeField(auto_now=True)
    content = RichTextField()

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        title = self.title[:10]
        return f"{title}"
    
class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.message} by {self.full_name}"
    
class SlideShow(models.Model):
    image = models.ImageField(upload_to='Images/slide')
    name = models.CharField(max_length=50)
    tilte = models.CharField(max_length=50)