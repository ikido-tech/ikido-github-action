import os
import zipfile
from src.github import GitHub
from src.output import Output
from src.templates import base_report, risk_table_report, check_output


def unzip_result():
    zipfile_path = os.path.abspath('./result.zip')
    if os.path.exists(zipfile_path):
        with zipfile.ZipFile(zipfile_path, 'r') as zip_file:
            zip_file.extractall(os.path.abspath('./result'))


if __name__ == '__main__':
    unzip_result()
    github = GitHub()
    output = Output('./ikido_output.txt', './result/insights.csv')
    short_report = base_report(output, github.sender_login, github.commit_url, github.commit_sha)
    github.post_pr_comment(short_report)
    check_name = 'IKIDO'
    title = 'IKIDO check finished successfully'
    status = 'completed'
    if not output.high_count:
        text = 'There are no high risk items'
        check_data = check_output(title, short_report, text)
        conclusion = 'success'
    else:
        text = risk_table_report(output)
        check_data = check_output(title, short_report, text)
        conclusion = 'failure'
    check_id = github.post_check(check_name, status, conclusion, check_data)
    if github.parents_sha:
        for sha in github.parents_sha:
            github.post_check(check_name, status, conclusion, check_data, sha)
