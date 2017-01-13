from setuptools import setup


setup(name='brutils',
      version='1.0.0',
      license='BSD 3-Clause License',
      author='Luiz Berti',
      url='https://github.com/luizfb/brutils',
      description='Provides validation and other tools for Brazilian document numbers.',
      keywords='cpf cnpj document validation brazil brazilian',
      packages=['brutils'],
      zip_safe=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Office/Business',
          'Topic :: Software Development :: Internationalization',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Natural Language :: English',
          'Natural Language :: Portuguese',
          'Natural Language :: Portuguese (Brazilian)'
      ])

