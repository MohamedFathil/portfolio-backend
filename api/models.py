from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'} ({self.created_at.strftime('%d %b %Y')})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    emoji = models.CharField(max_length=10, default='💻')
    project_type = models.CharField(max_length=100, default='Personal Project')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend & Frameworks'),
        ('database', 'Database'),
        ('cms', 'CMS & eCommerce'),
        ('tools', 'Tools & DevOps'),
        ('concepts', 'Concepts'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='🎓')
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='certications/', blank=True) #new

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} — {self.issuer}"
