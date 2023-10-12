# get cluster credentials
gcloud container clusters get-credentials airflow-cluster --region "europe-west4"
# confirm cluster
kubectl config current-context

# create airflow namespace
kubectl create namespace airflow

# Add airflow chart
helm repo add airflow-stable https://airflow-helm.github.io/charts
helm repo update

# update values:
# release: airflow, values(file): airflow-values.yaml, \
# repo/chart: airflow-stable/airflow, namespace: airflow
helm upgrade --install airflow -f airflow-values.yaml airflow-stable/airflow --namespace airflow