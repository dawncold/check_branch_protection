import click
from github import Github, GithubException


@click.command()
@click.option('--token', required=True, help='personal access token with repo privilege')
@click.option('--repo-prefix', help='filter repos prefix')
@click.option('--branch', 'branch_to_check', help='branch to check', default='master')
@click.option('--setup', 'setup_protection', is_flag=True,
              help='setup basic branch protection (disable force push)')
@click.option('--delete', 'delete_protection', is_flag=True, help='delete branch protection')
def main(token, repo_prefix, branch_to_check, setup_protection, delete_protection):
    if setup_protection and delete_protection:
        print('choose setup or delete, not both')
        exit(-1)
    print(f'token: ***, repo prefix: {repo_prefix}, branch: {branch_to_check}, '
          f'setup protection: {setup_protection}, delete protection: {delete_protection}')
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
                if setup_protection:
                    try:
                        branch.edit_protection()
                    except GithubException as e:
                        print(f'failed setup branch protection for {repo.full_name}, msg: {e.data["message"]}')
                    else:
                        print(f'{repo.full_name} {branch_to_check} branch protection setup')
                else:
                    print(repo.full_name)
            elif delete_protection:
                try:
                    branch.remove_protection()
                except:
                    pass
                else:
                    print(f'{repo.full_name} {branch_to_check} branch protection removed')


if __name__ == '__main__':
    main()
