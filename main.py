from pyiron_base import Project

pr = Project("some_project_name")
job = pr.create.job.tensiletest("some_job_name")
# Then you can view the default input by # job.input
# you can change the value of the inputs by
print(job.input)
# job.input[key] = new_value
# Then you can run the job by
job.run()
# The output would be available as a dictionary via
job["output"].to_object().to_builtin()


