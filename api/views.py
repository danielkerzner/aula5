from rest_framework import generics

from movies.models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class MovieList(generics.ListCreateAPIView):               # modifique esta linha
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):  # modifique esta linha
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewList(generics.ListCreateAPIView):              # modifique esta linha
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): # modifique esta linha
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer