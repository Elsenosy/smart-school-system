from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers import UserSerializer, AdminSerializer, \
                            StudentSerializer, ParentSerializer, \
                            TeacherSerializer

class UserCreate(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        # Get basic user data 
        username    = request.data.get("username")
        first_name = request.data.get("first_name")
        last_name  = request.data.get("last_name")
        email      = request.data.get("email")
        password   = request.data.get("password")
        address    = request.data.get("address")
        phone      = request.data.get("phone")
        birth_date = request.data.get("birth_date")
        user_type  = request.data.get("user_type")
        # Append the data in a JSON based format
        user_data = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'address': address,
            'phone': phone,
            'birth_date': birth_date,
            'user_type': user_type,
        }
        # Create user serializer to save user's data
        # Then check user type 
        serializer = UserSerializer(data=user_data)
        
        # Check validaty of user data  
        if serializer.is_valid():
            # Check user type to add Students, Teachers, Parents, Admins
            if user_type == 'ADM':
                job_title = request.data.get('job_title')

                user = serializer.save()
                
                admin_data = {
                    'user_id': user.id,
                    'job_title': job_title
                }

                serializer = AdminSerializer(data=admin_data)
                if serializer.is_valid():
                    return Response(admin_data, status=status.HTTP_201_CREATED)
                else:
                    # Delete user if the data in invalid
                    user.delete()
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif user_type == 'STD':
                admin_id = request.data.get('admin_id')
                stage_id = request.data.get('stage_id')

                user = serializer.save()
                
                student_data = {
                    'user_id': user.id,
                    'added_by_id': admin_id,
                    'stage_id': stage_id,
                }

                serializer = StudentSerializer(data=student_data)
                if serializer.is_valid():
                    return Response(student_data, status=status.HTTP_201_CREATED)
                else:
                    # Delete user if the data in invalid
                    user.delete()
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif user_type == 'PAR':
                admin_id = request.data.get('admin_id')
                job = request.data.get('job')

                user = serializer.save()
                
                parent_data = {
                    'user_id': user.id,
                    'job': job,
                    'added_by_id': admin_id,
                }

                serializer = ParentSerializer(data=parent_data)
                if serializer.is_valid():
                    return Response(parent_data, status=status.HTTP_201_CREATED)
                else:
                    # Delete user if the data in invalid
                    user.delete()
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif user_type == 'TECH':
                admin_id = request.data.get('admin_id')
                hire_date = request.data.get('hire_date')
                category_id = request.data.get('category_id')

                user = serializer.save()
                
                teacher_data = {
                    'user_id': user.id,
                    'hire_date': hire_date,
                    'category_id': category_id,
                    'added_by_id': admin_id,
                }

                serializer = TeacherSerializer(data=teacher_data)
                if serializer.is_valid():
                    return Response(teacher_data, status=status.HTTP_201_CREATED)
                else:
                    # Delete user if the data in invalid
                    user.delete()
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("UNKNOWN USER!")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)