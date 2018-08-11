#!/bin/bash

git remote add heroku-dev https://git.heroku.com/$HEROKU_APP_NAME.git
ssh-keyscan -H heroku.com >> ~/.ssh/known_hosts

wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
sudo mkdir -p /usr/local/lib /usr/local/bin
sudo tar -xvzf heroku-linux-amd64.tar.gz -C /usr/local/lib
sudo ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku

cat > ~/.netrc << EOF

machine api.heroku.com
  login $HEROKU_LOGIN
  password $HEROKU_API_KEY
EOF

machine git.heroku.com
  login $HEROKU_LOGIN
  password $HEROKU_API_KEY
EOF