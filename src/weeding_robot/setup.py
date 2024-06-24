from setuptools import setup

package_name = 'weeding_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kawai',
    maintainer_email='kawai@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "sensor = weeding_robot.sensor:main",
            "camera_detection = weeding_robot.camera_detection:main",
            "detection_client = weeding_robot.detection_client:main",
            "weeding_motor = weeding_robot.weeding_motor:main",
            "driving_motor = weeding_robot.driving_motor:main"
        ],
    },
)
