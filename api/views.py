from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict

from .models import ContactMessage, Project, Skill, Certification
from .serializers import (
    ContactMessageSerializer,
    ProjectSerializer,
    CertificationSerializer,
)


class ContactView(APIView):
    """
    POST /api/contact/
    Saves the message to the DB and (optionally) sends an email notification.
    """

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            message_obj = serializer.save()

            # Email notification (works when EMAIL_BACKEND is set to SMTP)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {message_obj.subject or 'New message'} from {message_obj.name}",
                    message=(
                        f"Name: {message_obj.name}\n"
                        f"Email: {message_obj.email}\n"
                        f"Subject: {message_obj.subject}\n\n"
                        f"Message:\n{message_obj.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'portfolio@example.com',
                    recipient_list=['mohamedfathil0057@gmail.com'],
                    fail_silently=True,
                )
            except Exception:
                pass  # Don't break if email fails

            return Response(
                {"success": True, "message": "Message received! I'll get back to you soon."},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProjectListView(APIView):
    """GET /api/projects/ — returns all featured projects ordered by `order`."""

    def get(self, request):
        projects = Project.objects.filter(is_featured=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class SkillListView(APIView):
    """
    GET /api/skills/
    Returns skills grouped by category:
    [{ category: 'Frontend', skills: ['HTML5', 'CSS3', ...] }, ...]
    """

    def get(self, request):
        skills = Skill.objects.all()
        grouped = defaultdict(list)
        for skill in skills:
            grouped[skill.get_category_display()].append(skill.name)

        data = [{"category": cat, "skills": names} for cat, names in grouped.items()]
        return Response(data)


class CertificationListView(APIView):
    """GET /api/certifications/ — returns all certifications."""

    def get(self, request):
        certs = Certification.objects.all()
        serializer = CertificationSerializer(certs, many=True, context={'request': request})
        return Response(serializer.data)


class PortfolioSummaryView(APIView):
    """
    GET /api/summary/
    Returns a combined snapshot: counts + key info for the hero card.
    """

    def get(self, request):
        data = {
            "name": "Mohamed Fathil",
            "title": "Junior Web Developer | Python Django Developer | WordPress Developer",
            "location": "Salem Street, Abu Dhabi, UAE",
            "email": "mohamedfathil0057@gmail.com",
            "phone": "+971 521973379",
            "availability": "Immediate",
            "visa": "Employment (2 Years Validity)",
            "stats": {
                "projects": Project.objects.filter(is_featured=True).count() or 4,
                "certifications": Certification.objects.count() or 6,
                "gfg_solved": 200,
                "leetcode_solved": 50,
            },
            "social": {
                "github": "https://github.com/",
                "linkedin": "https://linkedin.com/in/",
            },
        }
        return Response(data)