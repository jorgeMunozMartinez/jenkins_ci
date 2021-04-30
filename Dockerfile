FROM php:7-fpm
ADD script.sh /
ENTRYPOINT ["/bin/bash", "/script.sh"]
