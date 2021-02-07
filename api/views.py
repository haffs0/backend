from rest_framework import generics, viewsets
from .models import Teachers, Student
from .serializers import TeachersSerializer, StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class TeachersAPIDetailView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class StudentWithTeacherListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Student.objects.all()
        staff_no = self.request.query_params.get('staff_no')
        print(staff_no)
        return queryset.filter(teacher__staff_no=staff_no)