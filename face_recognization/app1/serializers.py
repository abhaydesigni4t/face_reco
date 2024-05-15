from rest_framework import serializers
from .models import UserEnrolled,Asset,Site,Notification,Upload_File,Turnstile_S,Orientation

class UserEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = '__all__'


class ActionStatusSerializer(serializers.Serializer):
    status = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class UserEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = ['name','company_name','job_role','mycompany_id','tag_id','job_location','orientation','status']
       

class UserEnrolledSerializer1(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = ['mycompany_id','tag_id']
       

class UserEnrolledSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = ['mycompany_id','orientation']



class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        exclude = ['id']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['subject', 'description', 'username']

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_File
        fields = '__all__'

class TurnstileSerializer(serializers.ModelSerializer):
    safety_confirmation = serializers.SerializerMethodField()

    def get_safety_confirmation(self, obj):
        return 1 if obj.safety_confirmation else 0

    class Meta:
        model = Turnstile_S
        fields = ['turnstile_id', 'location', 'safety_confirmation']


class AssetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['asset_id', 'status','location']


class facialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = ('mycompany_id', 'facial_data')


class OrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientation
        fields = '__all__'

        

from rest_framework import serializers


class LoginSerializerApp(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        user = UserEnrolled.objects.filter(email=email, password=password).first()
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        return data


from rest_framework import serializers
from .models import UserEnrolled

class signup_app(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolled
        fields = ['name', 'email', 'password']
