"""
Management command to seed the database with Mohamed Fathil's portfolio data.
Run: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from api.models import Project, Skill, Certification


class Command(BaseCommand):
    help = 'Seed portfolio data into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding portfolio data...')

        # ── Projects ──────────────────────────────────────────────
        Project.objects.all().delete()
        projects = [
            {
                'title': 'Restaurant Management System',
                'description': 'A full-stack Django web application featuring Menu management, Orders, Billing, and User Management modules with role-based authentication and automated order handling.',
                'tech_stack': ['Django', 'Python', 'MySQL', 'HTML/CSS', 'Role-based Auth'],
                'highlights': ['4 Core Modules', 'MySQL Integration', 'Role-Based Auth', 'Automated Orders'],
                'emoji': '🍽️',
                'project_type': 'Personal Project',
                'order': 1,
            },
            {
                'title': 'WooCommerce Grocery Store',
                'description': 'Full eCommerce solution with product catalog, pricing variations, payment gateway integration, and SEO-optimized structure built on WordPress.',
                'tech_stack': ['WordPress', 'WooCommerce', 'Elementor', 'Payment Gateway', 'SEO'],
                'highlights': ['20+ Products', 'Payment Integration', '30% Faster Load', 'Mobile Responsive'],
                'emoji': '🛒',
                'project_type': 'Professional Work',
                'order': 2,
            },
            {
                'title': 'Car Rental Platform',
                'description': 'Custom WooCommerce-based car rental website with service catalog, booking workflows, checkout optimization, and responsive Elementor design.',
                'tech_stack': ['WordPress', 'WooCommerce', 'Elementor', 'Custom Theme', 'CSS'],
                'highlights': ['Booking Flow', 'Custom Theme', 'Responsive UI', 'SEO Ready'],
                'emoji': '🚗',
                'project_type': 'Professional Work',
                'order': 3,
            },
            {
                'title': 'Number Plate Verification System',
                'description': 'Python-based vehicle verification automation system that processes 20+ vehicle records, validates insurance/registration, and generates non-compliance alerts.',
                'tech_stack': ['Python', 'Automation', 'Data Validation', 'Alert System'],
                'highlights': ['20+ Records', 'Insurance Check', 'Alert Flags', 'Accuracy Optimized'],
                'emoji': '🚔',
                'project_type': 'Academic Project',
                'order': 4,
            },
        ]
        for p in projects:
            Project.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'  ✓ Created {len(projects)} projects'))

        # ── Skills ────────────────────────────────────────────────
        Skill.objects.all().delete()
        skills = [
            # Frontend
            ('HTML5', 'frontend', 1), ('CSS3', 'frontend', 2),
            ('JavaScript', 'frontend', 3), ('React JS', 'frontend', 4),
            ('Three.js', 'frontend', 5), ('Responsive Design', 'frontend', 6),
            # Backend
            ('Python', 'backend', 1), ('Django', 'backend', 2),
            ('REST APIs', 'backend', 3), ('MVC Pattern', 'backend', 4),
            ('CRUD Operations', 'backend', 5), ('ML Basics', 'backend', 6),
            # Database
            ('MySQL', 'database', 1), ('MongoDB', 'database', 2),
            ('Database Integration', 'database', 3),
            # CMS
            ('WordPress', 'cms', 1), ('WooCommerce', 'cms', 2),
            ('Elementor', 'cms', 3), ('Theme Customization', 'cms', 4),
            ('Payment Gateways', 'cms', 5), ('SEO', 'cms', 6),
            # Tools
            ('VS Code', 'tools', 1), ('Git', 'tools', 2),
            ('PyCharm', 'tools', 3), ('Postman', 'tools', 4),
            ('Power BI', 'tools', 5), ('Excel', 'tools', 6),
            # Concepts
            ('Debugging', 'concepts', 1), ('Deployment', 'concepts', 2),
            ('Data Analytics', 'concepts', 3), ('SEO Optimization', 'concepts', 4),
        ]
        for name, cat, order in skills:
            Skill.objects.create(name=name, category=cat, order=order)
        self.stdout.write(self.style.SUCCESS(f'  ✓ Created {len(skills)} skills'))

        # ── Certifications ────────────────────────────────────────
        Certification.objects.all().delete()
        certs = [
            ('Crash Course on Python', 'Coursera', '🐍', 1),
            ('React JS for Beginners', 'Udemy', '⚛️', 2),
            ('Python Problem Solving Levels 1 & 2', 'CodeChef', '🏆', 3),
            ('Data Analytics', 'NoviTech Pvt. Ltd', '📊', 4),
            ('SQL BootCamp', 'LetsUpgrade', '🗄️', 5),
            ('Machine Learning with Python', 'IBM', '🤖', 6),
        ]
        for title, issuer, icon, order in certs:
            Certification.objects.create(title=title, issuer=issuer, icon=icon, order=order)
        self.stdout.write(self.style.SUCCESS(f'  ✓ Created {len(certs)} certifications'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Portfolio data seeded successfully!'))
