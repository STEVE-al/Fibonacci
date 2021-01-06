import setup tools
with open ('README.md','r') as f:
  long_desc=f.read()
setuptools.setup(name='Steve',
                 version='0.01',
                 author='steve',
                 author_email='s.smith200712@gmail.com',
                 description='generating fibonacci series',
                 long_description=long_desclong_description_content_type='tent/markdown' url='https://github.com/STEVE-al/Fibonacci',
                 packages=setuptools.find_package(),
                 classifiers=['programming language'::python::3,operating system::os independent,]
                 ,python_requires='>=3.6',)
