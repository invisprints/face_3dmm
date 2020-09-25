# AUTOGENERATED! DO NOT EDIT! File to edit: utils.ipynb (unless otherwise specified).

__all__ = ['test', 'test_eq', 'simplify_qd']

# Cell
import open3d as o3d
import operator
import numpy as np

# Cell
def test(a,b,cmp,cname=None):
    if cname is None: cname=cmp.__name__
    assert cmp(a,b),f"{cname}:\n{a}\n{b}"

def test_eq(a,b): test(a,b,operator.eq,'==')

# Cell
def simplify_qd(verts, faces, target_number_of_triangles):
    mesh = o3d.geometry.TriangleMesh()
    mesh.triangles = o3d.utility.Vector3iVector(faces)
    mesh.vertices = o3d.utility.Vector3dVector(verts)
    mesh_smp = mesh.simplify_quadric_decimation(target_number_of_triangles)
    return np.asarray(mesh_smp.vertices), np.asarray(mesh_smp.triangles)