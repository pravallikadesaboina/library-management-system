from django.urls import path
from . import views
from .views import LibraryRecordListCreateView, LibraryRecordDetailView

urlpatterns = [
    # Library Record APIs
    path('', LibraryRecordListCreateView.as_view(), name='library-record-list-create'),
    path('library-records/', views.LibraryRecordListCreateView.as_view(), name='library-record-list-create'),
    path('library-records/<int:pk>/', views.LibraryRecordDetailView.as_view(), name='library-record-detail'),
]
