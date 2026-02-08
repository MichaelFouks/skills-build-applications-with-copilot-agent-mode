from django.core.management.base import BaseCommand
from datetime import date, timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Delete existing data
        self.stdout.write('Deleting existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes unite to push their limits and achieve greatness!'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='The World\'s Greatest Super Heroes combining strength and determination!'
        )

        # Create Users (Superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'team': 'Team Marvel'},
        ]

        dc_heroes = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'Team DC'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'Team DC'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'Team DC'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'team': 'Team DC'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'team': 'Team DC'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'team': 'Team DC'},
        ]

        users = []
        for hero in marvel_heroes + dc_heroes:
            user = User.objects.create(**hero)
            users.append(user)

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weightlifting', 'Martial Arts', 'Yoga']
        
        for i, user in enumerate(users):
            for day in range(7):
                activity_date = date.today() - timedelta(days=day)
                activity_type = activity_types[day % len(activity_types)]
                duration = 30 + (i * 5) + (day * 2)
                calories = duration * 8
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=activity_date
                )

        # Create Leaderboard
        self.stdout.write('Creating leaderboard...')
        leaderboard_data = []
        for user in users:
            activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(a.calories_burned for a in activities)
            total_activities = activities.count()
            
            leaderboard_data.append({
                'user': user,
                'total_calories': total_calories,
                'total_activities': total_activities
            })

        # Sort by calories and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_calories'], reverse=True)
        
        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_email=data['user'].email,
                user_name=data['user'].name,
                team=data['user'].team,
                total_calories=data['total_calories'],
                total_activities=data['total_activities'],
                rank=rank
            )

        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'Intense full-body workout inspired by Captain America\'s regiment',
                'activity_type': 'Weightlifting',
                'difficulty': 'Advanced',
                'estimated_calories': 450,
                'duration': 60
            },
            {
                'name': 'Web-Slinger Circuit',
                'description': 'High-intensity agility and strength training',
                'activity_type': 'Martial Arts',
                'difficulty': 'Intermediate',
                'estimated_calories': 380,
                'duration': 45
            },
            {
                'name': 'Asgardian Endurance Run',
                'description': 'Long-distance running for stamina building',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'estimated_calories': 500,
                'duration': 60
            },
            {
                'name': 'Bat-Cave Strength Session',
                'description': 'Bruce Wayne\'s legendary strength training routine',
                'activity_type': 'Weightlifting',
                'difficulty': 'Advanced',
                'estimated_calories': 480,
                'duration': 75
            },
            {
                'name': 'Kryptonian Power Training',
                'description': 'Maximum strength and power development',
                'activity_type': 'Weightlifting',
                'difficulty': 'Expert',
                'estimated_calories': 550,
                'duration': 90
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Combat-focused training from Themyscira',
                'activity_type': 'Martial Arts',
                'difficulty': 'Advanced',
                'estimated_calories': 420,
                'duration': 60
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Ultra-fast interval training for maximum speed',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'estimated_calories': 400,
                'duration': 30
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Underwater endurance and strength training',
                'activity_type': 'Swimming',
                'difficulty': 'Intermediate',
                'estimated_calories': 350,
                'duration': 45
            },
            {
                'name': 'Zen Master Flow',
                'description': 'Flexibility and mindfulness practice',
                'activity_type': 'Yoga',
                'difficulty': 'Beginner',
                'estimated_calories': 200,
                'duration': 45
            },
            {
                'name': 'Hero Endurance Cycle',
                'description': 'Long-distance cycling for cardiovascular fitness',
                'activity_type': 'Cycling',
                'difficulty': 'Intermediate',
                'estimated_calories': 450,
                'duration': 60
            }
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
