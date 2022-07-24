import mlflow
mlflow.start_run()

# Log a parameter (key-value pair)
mlflow.log_param("param1", 100)

# Log a metric; metrics can be updated throughout the run
mlflow.log_metric("foo", 2, step=1)
mlflow.log_metric("foo", 4, step=2)
mlflow.log_metric("foo", 6, step=3)

# Log an artifact (output file)
with open("output.txt", "w") as f:
    f.write("Hello world!")
mlflow.log_artifact("output.txt")

mlflow.end_run()