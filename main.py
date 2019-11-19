import click
from github import Github, GithubException


@click.command()
@click.option('--token', required=True, help='personal access token with repo privilege')
@click.option('--repo-prefix', help='filter repos prefix')
@click.option('--branch', 'branch_to_check', help='branch to check', default='master')
def main(token, repo_prefix, branch_to_check):
    print(f'token: ***, repo prefix: {repo_prefix}, branch: {branch_to_check}')
    g = Github(login_or_token=token)
    for repo in g.get_user().get_repos():
        if repo_prefix and not repo.full_name.startswith(repo_prefix):
            continue
        try:
            branch = repo.get_branch(branch_to_check)
        except GithubException as e:
            if e.status == 404:
                print(f'branch {branch_to_check} is not found on repo {repo.full_name}')
        else:
            if not branch.protected:
                print(repo.full_name)


if __name__ == '__main__':
    main()
