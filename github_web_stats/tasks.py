from celery import shared_task
import requests
from .models import Repository, CommitActivity, CodeFrequency, Participation

@shared_task
def fetch_and_store_github_data():
    repositories = Repository.objects.all()
    for repo in repositories:
        # Fetch commit activity
        commit_activity_response = requests.get(f'https://api.github.com/repos/{repo.full_name}/stats/commit_activity')
        if commit_activity_response.status_code == 200:
            for week_data in commit_activity_response.json():
                CommitActivity.objects.update_or_create(
                    repository=repo,
                    week=week_data['week'],
                    defaults={'commits': week_data['total']}
                )
        # Fetch code frequency
        code_frequency_response = requests.get(f'https://api.github.com/repos/{repo.full_name}/stats/code_frequency')
        if code_frequency_response.status_code == 200:
            for week_data in code_frequency_response.json():
                CodeFrequency.objects.update_or_create(
                    repository=repo,
                    week=week_data[0],
                    defaults={'additions': week_data[1], 'deletions': week_data[2]}
                )
        # Fetch participation
        participation_response = requests.get(f'https://api.github.com/repos/{repo.full_name}/stats/participation')
        if participation_response.status_code == 200:
            participation_data = participation_response.json()
            Participation.objects.update_or_create(
                repository=repo,
                week=week_data['week'],
                defaults={
                    'all_commits': participation_data['all'],
                    'owner_commits': participation_data['owner']
                }
            )
