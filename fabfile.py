from fabric.api import task
from tools.tasks.server import server, createuser

@task
def run():
	server()


@task
def createuse():
	createuser()

