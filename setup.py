from distutils.core import setup

setup(name='python_moztelemetry',
      version='1.0.0',
      author='Roberto Agostino Vitillo',
      author_email='rvitillo@mozilla.com',
      description='Spark bindings for Mozilla Telemetry',
      url='https://github.com/vitillo/python_moztelemetry',
      packages=['moztelemetry'],
      package_dir={'moztelemetry': 'moztelemetry'})
