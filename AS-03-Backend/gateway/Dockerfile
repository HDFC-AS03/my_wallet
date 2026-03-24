FROM openresty/openresty:alpine-fat

RUN opm get ledgetech/lua-resty-http
RUN opm get jkeys089/lua-resty-hmac  
RUN opm get openresty/lua-resty-string
RUN opm get cdbattags/lua-resty-jwt
RUN opm get openresty/lua-resty-limit-traffic

COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY lua/jwt_validator.lua /usr/local/openresty/nginx/lua/jwt_validator.lua

EXPOSE 80
CMD ["openresty", "-g", "daemon off;"]