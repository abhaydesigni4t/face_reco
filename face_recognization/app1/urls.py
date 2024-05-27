from django.urls import path
from . import views
from .views import UserEnrolledListCreateView,UserEnrolledRetrieveUpdateDestroyView,get_data,create_data,UpdateData,TaskDeleteView,DownloadDatabaseView,ActionStatusAPIView,ChangeDetectionView,LoginAPIView,AssetCreateAPIView,AssetListAPIView,UserEnrollListCreateAPIView,UserEnrollDetailAPIView,SiteListAPIView,SiteUpdateView,SiteDeleteView,CompanyUpdateView,CompanyDeleteView,NotificationList,FileUploadView,edit_timeschedule,delete_timeschedule,TurnstileUpdateView,Turnstile_API,Turnstile_get_single_api,ChangeAssetStatus,FacialDataApi,UpdateTagIDAPIView,UpdateOrientationAPIView,LoginAPIApp,PreShiftListCreateAPIView,ToolBoxListCreateAPIView,UserProfileCreateAPIView,OrientationCreateView,UserComplyAPIView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.login_view,name='login'),
    #path('login1/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path("check/", views.check_data, name="check"),
    path('api_user_enro/', UserEnrolledListCreateView.as_view(), name='user_enro1'),
    path('api_user_enro/<int:pk>/', UserEnrolledRetrieveUpdateDestroyView.as_view(), name='user_enro2'),
    path('get_all/',get_data.as_view(),name='get_all'),
    path('create/',create_data.as_view(),name='create'),
    path('notification/',views.post_notification, name='notification'),
    path('upload/', views.upload_file, name='upload'),
    path('report/', views.report_view, name='report'),
    path('update/<int:pk>/', UpdateData.as_view(), name='user_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('app2_login/',views.login_view,name='app2_login'),
    path('sites/',views.site_view,name='sites'),
    path('app2logout/',views.app2_logout,name='app2logout'),
    path('management/',views.management_view,name='management'),
    path('worker_edit/',views.edit_worker,name='worker_edit'),
    path('asset_manage/',views.asset_management,name='asset_manage'),
    path('asset_site/',views.asset_site,name='asset_site'),
    path('add_asset/',views.add_asset,name='add_asset'),
    path('update_asset/<int:asset_id>/', views.update_asset, name='update_asset'),
    path('asset_details/<int:asset_id>/', views.asset_details, name='asset_details'),
    path('download-db/', DownloadDatabaseView.as_view(), name='download-db'),  # download in sqlite3 that is binary
    path('detect_changes/', ChangeDetectionView.as_view(), name='detect-changes'),
    path('exit/',views.exit,name='exit'),
    path('setting_t/',views.setting_turn,name='setting_t'),
    path('action_status/', ActionStatusAPIView.as_view(), name='action_status'),
    path('login_api/', LoginAPIView.as_view(), name='api-login'),
    path('users/', UserEnrollListCreateAPIView.as_view(), name='user-enroll-list-create'),
    path('users/<int:tag_id>/', UserEnrollDetailAPIView.as_view(), name='user-enroll-detail'), 
    path('get_assets_api/', AssetListAPIView.as_view(), name='asset-list'),
    path('asset_api/', AssetCreateAPIView.as_view(), name='asset-create'),
    path('exits/', views.ExitListCreateAPIView.as_view(), name='exit-list-create'),
    path('exits/<int:asset_id>/', views.ExitDetailAPIView.as_view(), name='exit-detail'),
    path('sites_api/', SiteListAPIView.as_view(), name='site-list'),
    path('add_site/', views.add_site, name='add_site'),
    path('edit_site/<int:pk>/', SiteUpdateView.as_view(), name='edit_sites'),
    path('delete_site/<int:pk>/', SiteDeleteView.as_view(), name='delete_sites'),
    path('company/', views.company_view, name='company'),
    path('add_company/', views.add_company_data, name='add_company'),
    path('edit_company/<int:pk>/', CompanyUpdateView.as_view(), name='edit_company'),
    path('delete_company/<int:pk>/', CompanyDeleteView.as_view(), name='delete_company'),
    path('time/', views.timesche, name='time'),
    path('notification_api/', NotificationList.as_view(), name='notification-list'),
    path('success/', views.success_page, name='success'),
    path('file_upload_api/', FileUploadView.as_view(), name='file-upload'),
    path('timeshe/', views.add_timesh, name='timeshe'),
    path('edit_time/<int:id>/', edit_timeschedule, name='edit_timeschedule'),
    path('delete_time/<int:id>/', delete_timeschedule, name='delete_timeschedule'),
    path('add_turnstile/', views.add_turnstile, name='add_turnstile'),
    path('delete_selected/', views.delete_selected, name='delete_selected'),
    path('edit_turnstile/<int:pk>/', TurnstileUpdateView.as_view(), name='turnstile_edit'),
    path('turnstile_api/', Turnstile_API.as_view(), name='turnstile_api'),
    path('change_status/<int:asset_id>/', ChangeAssetStatus.as_view(), name='change_asset_status'),
    path('delete_selected1/', views.delete_selected1, name='delete_selected1'),
    path('turnstile/<int:turnstile_id>/', Turnstile_get_single_api.as_view(), name='turnstile-detail'),
    path('delete_selected2/', views.delete_selected2, name='delete_selected2'),
    path('notification1/', views.notification_view, name='notification1'),
    path('orientation/', views.orientation_task, name='orientation'),
    path('delete_selected3/', views.delete_selected3, name='delete_selected3'),
    path('delete_selected4/', views.delete_selected4, name='delete_selected4'),
    path('update_safety_confirmation/', views.update_safety_confirmation, name='update_safety_confirmation'),
    path('sort_data/', views.sort_data, name='sort_data'),
    path('make_inactive_selected/', views.make_inactive_selected, name='make_inactive_selected'),
    path('get_orientation_api/', views.OrientationListView.as_view(), name='orientation_api'),
    path('post_tagid/', UpdateTagIDAPIView.as_view(), name='post_tagid'),
    path('post_orientation/', UpdateOrientationAPIView.as_view(), name='post_orientation'),
    path('face_api/', FacialDataApi.as_view(), name='face_api'),
    path('loginapi/', LoginAPIApp.as_view(), name='loginapi'), 
    path('signupapi/', views.signup_api_app, name='signupapi'),
    path('site_docu/',views.site_document,name='site_docu'),
    path('preshift/',views.preshift,name='preshift'),
    path('add_preshift/', views.add_preshift, name='add_preshift'),
    path('edit_preshift/<int:pk>/', views.edit_preshift, name='edit_preshift'),
    path('delete_preshift/<int:pk>/', views.delete_preshift, name='delete_preshift'),
    path('toolbox/',views.toolbox,name='toolbox'),
    path('add_toolbox/', views.add_toolbox, name='add_toolbox'),
    path('edit_toolbox/<int:pk>/', views.edit_toolbox, name='edit_toolbox'),
    path('delete_toolbox/<int:pk>/', views.delete_toolbox, name='delete_toolbox'),
    path('preshift_api/', PreShiftListCreateAPIView.as_view(), name='preshift_api'),
    path('toolbox_api/', ToolBoxListCreateAPIView.as_view(), name='toolbox_api'),
    path('user_profile_api/', UserProfileCreateAPIView.as_view(), name='user_profile_api'),
    path('user/<int:user_id>/', views.show_facial_data_images, name='show_facial_data_images'),
    path('post_orientation_sheet/', OrientationCreateView.as_view(), name='post_orientation_sheet'),
    path('attachment/<int:attachment_id>/', views.view_attachment, name='view_attachment'),
    path('mycomply_api/', UserComplyAPIView.as_view(), name='mycomply_api'),
    path('filter_preshift/',views.PreShiftfilterdata ,name='filter_preshift'),
    path('filter_toolbox/',views.toolboxfilterdata ,name='filter_toolbox'),
    path('delete_facial_data_image/<int:user_id>/<str:filename>/', views.delete_facial_data_image, name='delete_facial_data_image'),
    path('upload_facial_data_image/<int:user_id>/', views.upload_facial_data_image, name='upload_facial_data_image'),
  



] 





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)