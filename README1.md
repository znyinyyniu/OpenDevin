1. after merge from main branch

      mamba activate
      export INSTALL_DOCKER=n
      make build
      poetry lock --no-update

2. pip install too slow

      pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
      pip install name -i https://mirrors.aliyun.com/pypi/simple                (The download speed is very slow.)
      pip install name -i https://pypi.tuna.tsinghua.edu.cn/simple              (The download speed is very fast.)
      pip install name                  (The download speed is unstable.)
