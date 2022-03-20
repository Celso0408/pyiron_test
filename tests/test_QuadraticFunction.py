import pytest

# third party imports
import numpy as np

# local imports
from pyiron_base import Project

def test_QuadraticFunction():
    pr = Project("some_project_name")
    job = pr.create.job.QuadraticFunction("some_job_name",
                                    delete_existing_job=True)
    # Then you can view the default input by # job.input
    # you can change the value of the inputs by
    #print(job.input)
    job.input.a = 1
    job.input.b = 2
    job.input.c = 3
    job.input.x = [0, 1, 2, 3, 4, 5]

    # Then you can run the job by
    job.run()
    # The output would be available as a dictionary via
    output = job["output"].to_object().to_builtin()

    exact_result = job.input.a * np.multiply(job.input.x, job.input.x) +\
        job.input.a * job.input.x +\
        np.full_like(job.input.x, job.input.c)

    assert pytest.approx(output['f']) == exact_result


if __name__ == "__main__":
    test_QuadraticFunction()





