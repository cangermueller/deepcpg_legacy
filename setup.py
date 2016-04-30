from setuptools import setup
from pip.req import parse_requirements
import os


def abspath(fname):
    return os.path.join(os.path.dirname(__file__), fname)


def read(fname, split=False):
    with open(abspath(fname)) as f:
        lines = f.read()
    if split:
        lines = lines.splitlines()
    return lines


def requirements(fname='requirements.txt'):
    return [str(r.req) for r in parse_requirements(abspath(fname))]


setup(name='DeepCpG',
      version='0.0.1',
      description='Deep neural network for predicting single-cell ' +
                  'methylation states',
      author='Christof Angermueller',
      author_email='cangermueller@gmail.com',
      license = "BSD",
      install_requires=requirements()
      )
