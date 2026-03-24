FROM openresty/openresty:alpine-fat

RUN opm get ledgetech/lua-resty-http
RUN opm get jkeys089/lua-resty-hmac  
RUN opm get openresty/lua-resty-string
RUN opm get cdbattags/lua-resty-jwt
RUN opm get openresty/lua-resty-limit-traffic

# Copy nginx config and lua scripts
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY env.conf /usr/local/openresty/nginx/conf/env.conf   
COPY lua/jwt_validator.lua /usr/local/openresty/nginx/lua/jwt_validator.lua

EXPOSE 80
CMD ["openresty", "-g", "daemon off;"]