
# third party imports
import numpy as np

# local imports
from pyiron_base import Project

def test_FEniCS_elasticity():
    pr = Project("some_project_name")
    job = pr.create.job.FEniCSElasticity("some_job_name",
                                    delete_existing_job=True)
    # Then you can view the default input by # job.input
    # you can change the value of the inputs by
    #print(job.input)
    job.input.height = 0.1
    job.input.area = 0.1 #automatically computes the diameter
    job.input.E = 10
    job.input.nu = 0
    job.input.mesh_density = 10
    job.input.displ = [0, -1, -2]
    # job.input[key] = new_value
    # Then you can run the job by
    job.run()
    # The output would be available as a dictionary via
    #print(job["output"].to_object().to_builtin())
    output = job["output"].to_object().to_builtin()

    # print("number of dofs", output['nDOF'])
    # This is due to the fact that the round circle is not exactly
    # round due to the linear geometry modelling in FEniCS
    scaling_factor = .9892183817163186
    #print("stress", output['stress'])

    exact_output_stress = scaling_factor*(
            job.input.E/job.input.height) *\
            np.array(job.input.displ)
    np.testing.assert_array_almost_equal(output['stress'],
                                         exact_output_stress, 8)

    #print("force", output['force'])
    exact_output_force = scaling_factor*(
            job.input.E*job.input.area/job.input.height) *\
            np.array(job.input.displ)
    np.testing.assert_array_almost_equal(output['force'], exact_output_force, 8)


if __name__ == "__main__":
    unittest.main()





