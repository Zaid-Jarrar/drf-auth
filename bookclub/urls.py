from django.urls import path
from .views import BooksListView, BooksDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('books-list', BooksListView.as_view(), name='books_list'),
    path('book-detail/<int:pk>', BooksDetailView.as_view(), name='book_detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk5NDA0OSwiaWF0IjoxNjUzOTA3NjQ5LCJqdGkiOiJhMDJmMDY5ODExYjQ0ODZjYjcyNmJjZTNkMjBiMjFkNCIsInVzZXJfaWQiOjF9.PKLVyloY2jdJfLWa2ldP7XKEEU_2cql3TEEiQg2Hcfc",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTA3OTQ5LCJpYXQiOjE2NTM5MDc2NDksImp0aSI6IjYxMjVlYWQ5NzA2ZjQwZWJhMDNkNTFiZGEyNzM1MGNiIiwidXNlcl9pZCI6MX0.lRJzLCIih0V2z5Fww7u8s6ZWQdJC181KGsC8nxA_JIA"
# }