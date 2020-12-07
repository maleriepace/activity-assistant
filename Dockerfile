ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --update python3-dev py3-pip expect \
    jpeg-dev zlib-dev gcc linux-headers musl-dev # to fix pillow error 


# pandas needs very long to intall over pip (has to be built)
# therefore install from package repo
# TODO remove --repository when this is in stable
RUN apk add py3-gunicorn py3-pandas py3-kiwisolver py3-scipy py3-scikit-learn py3-matplotlib --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

COPY build/prod/requirements.txt .
RUN pip3 install -r requirements.txt

ENV DJANGO_ENV='production'
ENV DJANGO_DEBUG=false
ENV PYTHONPATH=/etc/opt/activity_assistant:/opt/activity_assistant

# copy program files
COPY web/ /opt/activity_assistant/web/ 
COPY hass_api/ /opt/activity_assistant/hass_api/

#COPY web/frontend/static/ /var/cache/activity_assistant/static/
#COPY web/frontend/templates/ /var/cache/activity_assistant/static/templates/
COPY services/* /opt/activity_assistant/

# copy configuration files
COPY web/act_assist/settings.py web/act_assist/local_settings /etc/opt/activity_assistant/

# copy media files
COPY build/prod/db.sqlite3 /data/media/db.sqlite3

WORKDIR /home
COPY build/prod/start.sh build/prod/minimal.json ./
RUN chmod a+x start.sh

# copy static files
RUN mkdir -p /var/cache/activity_assistant/static/
RUN python3 /opt/activity_assistant/web/manage.py collectstatic

CMD [ "./start.sh" ]