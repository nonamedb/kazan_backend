web: PYTHONPATH=$PYTHONPATH:/app:/app/kazan_backend gunicorn \
      --access-logfile - \
      --error-logfile - \
      --access-logformat "%(h)s %(l)s %(u)s %(t)s pid %(p)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\" %(l)s %(D)s µs" \
      "backend.application:init_app()"
