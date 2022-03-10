from pyiron_base import Project

pr = Project("some_project_name")
job = pr.create.job.TensileTest("some_job_name", delete_existing_job=True)
# Then you can view the default input by # job.input
# you can change the value of the inputs by
print(job.input)
job.input.height = 10
job.input.diameter = 2
job.input.displ = [0, -0.1, -0.25]
# job.input[key] = new_value
# Then you can run the job by
job.run()
# The output would be available as a dictionary via
print(job["output"].to_object().to_builtin())


