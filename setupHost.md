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
              location /game {
                 include proxy_params;
                 proxy_set_header X-Real-IP  $remote_addr;
                 proxy_set_header X-Forwarded-For $remote_addr;
                 proxy_set_header Host $host;
                 proxy_headers_hash_max_size 1024;
                 proxy_headers_hash_bucket_size 256;
                 proxy_pass http://127.0.0.1:5000/;
        }
       }

ctrl x to exit and agree to save

# activate site

service nginx restart

# open port 81 on gcp portal

# wait a few mins
