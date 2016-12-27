disqus-python In Python3
########################

:date: 2016-12-27 02:03
:category: Python

disqus-python를 pip를 통해 설치할 경우,
제대로 최신 버전이 설치되지 않는다.
pypi의 패키지 관리를 제대로 안 하는 모양.

Python3에서 정상작동하지 않으므로,
언인스톨 후 github를 통해 다시 설치해야 한다.

.. code:: bash

  pip3 install git+git://github.com/disqus/disqus-python@master

