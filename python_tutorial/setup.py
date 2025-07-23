from setuptools import find_packages, setup

package_name = 'python_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Graeme Best',
    maintainer_email='graeme.best@uts.edu.au',
    description='Template code for python tutorial',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'python_tutorial = python_tutorial.python_tutorial:main'
        ],
    },
)
