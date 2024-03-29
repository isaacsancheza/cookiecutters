import aws_cdk as cdk

from stack import Stack


region = '{{ cookiecutter.region }}'
account = '{{ cookiecutter.account }}'
stack_name = '{{ cookiecutter.stack_name }}'

app = cdk.App()
env = cdk.Environment(region=region, account=account)
stack = Stack(
    app, 
    'Stack',
    env=env, 
    stack_name=stack_name, 
)

cdk.Tags.of(stack).add('stack-name', stack_name)
app.synth()
