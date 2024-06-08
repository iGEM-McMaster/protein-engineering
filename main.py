import vina
import matplotlib
import numpy
import sklearn
import pandas
import scipy

if __name__ == "__main__":
    v = vina.Vina(sf_name='vina')

    v.set_receptor('data/1iep_receptor.pdbqt')

    v.set_ligand_from_file('data/1iep_ligand.pdbqt')
    v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])

    energy = v.score()
    print(f"Score before minimization: {energy[0]:.3f} kcal/mol")

    energy_optimized = v.optimize()
    print(f"Score after minimization: {energy_optimized[0]:.3f} kcal/mol")
    v.write_pose('data/1iep_ligand_minimized.pdbqt', overwrite=True)

    v.dock(exhaustiveness=32, n_poses=20)
    v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=5, overwrite=True)