PS C:\Users> kubectl exec -it timescaledb-access-0 -- psql -U postgres
psql (12.3 (Debian 12.3-1.pgdg100+1))
Type "help" for help.

postgres=# ALTER USER postgres PASSWORD 'myPassword';
create database cryptoanalysis;
\c cryptoanalysis
cryptoanalysis=# select * from exchanges;

### Use above
NOTES:
# This file and its contents are licensed under the Apache License 2.0.
# Please see the included NOTICE for copyright information and LICENSE for a copy of the license.

TimescaleDB can be accessed via port 5432 on the following DNS name from within your cluster:
timescaledb.default.svc.cluster.local

To get your password for superuser run:

    # superuser password
    PGPASSWORD_SUPERUSER=$(kubectl get secret --namespace default timescaledb -o jsonpath="{.data.password-superuser}" | base64 --decode)

    # admin password
    PGPASSWORD_ADMIN=$(kubectl get secret --namespace default timescaledb -o jsonpath="{.data.password-admin}" | base64 --decode)

To connect to your database:

1. Run a postgres pod and connect using the psql cli:
    # login as superuser
    kubectl run -i --tty --rm psql --image=postgres \
      --env "PGPASSWORD=$PGPASSWORD_SUPERUSER" \
      --command -- psql -U postgres \
      -h timescaledb.default.svc.cluster.local postgres

    # login as admin
    kubectl run -i -tty --rm psql --image=postgres \
      --env "PGPASSWORD=$PGPASSWORD_ADMIN" \
      --command -- psql -U admin \
      -h timescaledb.default.svc.cluster.local postgres