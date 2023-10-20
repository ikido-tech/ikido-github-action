import requests
import os
import logging

_logger = logging.getLogger(__name__)


class GitHub:
    def __init__(self):
        self.github_token = os.environ['GITHUB_TOKEN']
        self.repo = os.environ['GITHUB_REPOSITORY']
        self.pr_number = os.environ["GITHUB_PR_NUMBER"]
        self.sender_login = os.environ["GITHUB_SENDER_LOGIN"]
        self.repo_html = os.environ["GITHUB_REPO_HTML_URL"]
        self.branch = os.environ["GITHUB_BRANCH"]
        self.headers = {
            'Authorization': f'Bearer {self.github_token}',
            'Accept': 'application/vnd.github+json'
        }
        self.commit_sha, self.parents_sha = self.get_commits_sha()
        self.commit_url = f'{self.repo_html}/commit/{self.commit_sha}'

    def get_commits_sha(self):
        url = f'https://api.github.com/repos/{self.repo}/commits/{self.branch}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            branch_data = response.json()
            _logger.warning(branch_data)
            try:
                commit_sha = branch_data['commit']['sha']
                return commit_sha, None
            except KeyError:
                commit_sha = branch_data['sha']
                parent1_sha, parent2_sha = branch_data['parents'][0]['sha'], branch_data['parents'][1]['sha']
                return commit_sha, (parent1_sha, parent2_sha)
        else:
            _logger.warning('Failed to get branch')
            raise Exception(f'Status code: {response.status_code}\n'
                            f'Response body: {response.json()}')

    def post_pr_comment(self, msg):
        url = f'https://api.github.com/repos/{self.repo}/issues/{self.pr_number}/comments'

        data = {
            'body': msg
        }

        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            _logger.info('Status code successful')
        else:
            _logger.warning('Failed to post comment')
            raise Exception(f'Status code: {response.status_code}\n'
                            f'Response body: {response.json()}')

    def post_check(self, name, status, conclusion, output, commit_sha=None):
        commit_sha = self.commit_sha if not commit_sha else commit_sha
        url = f'https://api.github.com/repos/{self.repo}/check-runs'
        data = {
            'name': name,
            'head_sha': commit_sha,
            'status': status,
            'conclusion': conclusion,
            'output': output
        }
        response = requests.post(url, json=data, headers=self.headers)
        json = response.json()
        if response.status_code == 201:
            _logger.info('Status code successful')
            check_id = json['id']
            return check_id
        else:
            _logger.warning('Failed to post check')
            raise Exception(f'Status code: {response.status_code}\n'
                            f'Response body: {json}'
                            f'Request body: {data}')
