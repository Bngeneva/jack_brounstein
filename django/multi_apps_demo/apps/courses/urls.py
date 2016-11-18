from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^new/$", views.new, name="new"),
	url(r"^create/$", views.create, name="create"),
	url(r"^add_student_page/$", views.add_student_page, name="add_student_page"),
	url(r"^add_student_to_course/$", views.add_student_to_course, name="add_student_to_course"),
	url(r"^show/(?P<course_id>\d+)/$", views.show, name="show"),
	url(r"^destroy/$", views.destroy, name="destroy"),
]