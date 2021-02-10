# change to correct site folder

cd /etc/nginx/sites-enabled

# create site file

nano player

# paste following into file

server {
       listen 81;
       listen [::]:81;

       server_name player2.acgtest.info;

       root /var/www/player;
       index index.html;

       location / {
               try_files $uri $uri/ =404;
       }
}

ctrl x to exit and agree to save

# activate site

service nginx restart

# open port 81 on gcp portal

# wait a few mins
