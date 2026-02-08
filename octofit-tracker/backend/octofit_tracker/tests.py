from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, timedelta
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com',
            team='Test Team'
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@hero.com')
        self.assertEqual(self.user.team, 'Test Team')
        self.assertIsNotNone(self.user.created_at)
    
    def test_user_str(self):
        """Test the string representation of user"""
        self.assertEqual(str(self.user), 'Test Hero')
    
    def test_email_unique(self):
        """Test that email field is unique"""
        with self.assertRaises(Exception):
            User.objects.create(
                name='Another Hero',
                email='test@hero.com',
                team='Another Team'
            )


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A team for testing'
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A team for testing')
        self.assertIsNotNone(self.team.created_at)
    
    def test_team_str(self):
        """Test the string representation of team"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@hero.com',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            date=date.today()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_email, 'test@hero.com')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 300)
        self.assertIsNotNone(self.activity.created_at)
    
    def test_activity_str(self):
        """Test the string representation of activity"""
        self.assertEqual(str(self.activity), 'test@hero.com - Running')


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='test@hero.com',
            user_name='Test Hero',
            team='Test Team',
            total_calories=1000,
            total_activities=5,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.entry.user_name, 'Test Hero')
        self.assertEqual(self.entry.total_calories, 1000)
        self.assertEqual(self.entry.total_activities, 5)
        self.assertEqual(self.entry.rank, 1)
        self.assertIsNotNone(self.entry.updated_at)
    
    def test_leaderboard_str(self):
        """Test the string representation of leaderboard entry"""
        self.assertEqual(str(self.entry), '1. Test Hero - 1000 cal')


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A workout for testing',
            activity_type='Weightlifting',
            difficulty='Intermediate',
            estimated_calories=400,
            duration=45
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.activity_type, 'Weightlifting')
        self.assertEqual(self.workout.difficulty, 'Intermediate')
        self.assertEqual(self.workout.estimated_calories, 400)
        self.assertEqual(self.workout.duration, 45)
        self.assertIsNotNone(self.workout.created_at)
    
    def test_workout_str(self):
        """Test the string representation of workout"""
        self.assertEqual(str(self.workout), 'Test Workout')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.user_data = {
            'name': 'API Hero',
            'email': 'api@hero.com',
            'team': 'API Team'
        }
        self.user = User.objects.create(**self.user_data)
    
    def test_get_users_list(self):
        """Test retrieving list of users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_user(self):
        """Test creating a new user"""
        new_user = {
            'name': 'New Hero',
            'email': 'new@hero.com',
            'team': 'New Team'
        }
        response = self.client.post('/api/users/', new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
    
    def test_filter_users_by_team(self):
        """Test filtering users by team"""
        response = self.client.get('/api/users/by_team/?team=API Team')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['team'], 'API Team')


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='API Team',
            description='Team for API testing'
        )
    
    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_team(self):
        """Test creating a new team"""
        new_team = {
            'name': 'New Team',
            'description': 'A new team for testing'
        }
        response = self.client.post('/api/teams/', new_team, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@hero.com',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            date=date.today()
        )
    
    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_activity(self):
        """Test creating a new activity"""
        new_activity = {
            'user_email': 'new@hero.com',
            'activity_type': 'Swimming',
            'duration': 45,
            'calories_burned': 400,
            'date': str(date.today())
        }
        response = self.client.post('/api/activities/', new_activity, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 2)
    
    def test_filter_activities_by_user(self):
        """Test filtering activities by user email"""
        response = self.client.get('/api/activities/by_user/?email=test@hero.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='test@hero.com',
            user_name='Test Hero',
            team='Test Team',
            total_calories=1000,
            total_activities=5,
            rank=1
        )
    
    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_leaderboard_ordering(self):
        """Test that leaderboard is ordered by rank"""
        Leaderboard.objects.create(
            user_email='another@hero.com',
            user_name='Another Hero',
            team='Test Team',
            total_calories=800,
            total_activities=4,
            rank=2
        )
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 2)
    
    def test_filter_leaderboard_by_team(self):
        """Test filtering leaderboard by team"""
        response = self.client.get('/api/leaderboard/by_team/?team=Test Team')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A workout for testing',
            activity_type='Weightlifting',
            difficulty='Intermediate',
            estimated_calories=400,
            duration=45
        )
    
    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_workout(self):
        """Test creating a new workout"""
        new_workout = {
            'name': 'New Workout',
            'description': 'A new workout for testing',
            'activity_type': 'Running',
            'difficulty': 'Beginner',
            'estimated_calories': 300,
            'duration': 30
        }
        response = self.client.post('/api/workouts/', new_workout, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 2)
    
    def test_filter_workouts_by_difficulty(self):
        """Test filtering workouts by difficulty"""
        response = self.client.get('/api/workouts/by_difficulty/?difficulty=Intermediate')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_filter_workouts_by_type(self):
        """Test filtering workouts by activity type"""
        response = self.client.get('/api/workouts/by_type/?type=Weightlifting')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_root_redirects_to_api(self):
        """Test that root URL redirects to API"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(response.url.endswith('/api/'))
    
    def test_api_root_accessible(self):
        """Test that API root is accessible"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that all expected endpoints are present
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
