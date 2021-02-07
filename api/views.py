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

class StudentWithTeacherListAPIView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        pk = self.kwargs['pk']
        print(pk)
        return Student.objects.filter(teacher__pk=pk)