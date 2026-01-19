"""
Test script to verify all required packages are installed correctly.
Run this after setting up your environment to ensure everything works.
"""


def test_packages():
    """Test that all required packages can be imported."""
    results = []

    # Core scientific computing
    print("Testing core scientific packages...")
    try:
        import numpy as np

        results.append(("numpy", np.__version__, "OK"))
    except ImportError as e:
        results.append(("numpy", None, f"FAILED: {e}"))

    try:
        import pandas as pd

        results.append(("pandas", pd.__version__, "OK"))
    except ImportError as e:
        results.append(("pandas", None, f"FAILED: {e}"))

    try:
        import scipy

        results.append(("scipy", scipy.__version__, "OK"))
    except ImportError as e:
        results.append(("scipy", None, f"FAILED: {e}"))

    # Visualization
    print("Testing visualization packages...")
    try:
        import matplotlib

        results.append(("matplotlib", matplotlib.__version__, "OK"))
    except ImportError as e:
        results.append(("matplotlib", None, f"FAILED: {e}"))

    try:
        import seaborn as sns

        results.append(("seaborn", sns.__version__, "OK"))
    except ImportError as e:
        results.append(("seaborn", None, f"FAILED: {e}"))

    # Machine learning
    print("Testing machine learning packages...")
    try:
        import sklearn

        results.append(("scikit-learn", sklearn.__version__, "OK"))
    except ImportError as e:
        results.append(("scikit-learn", None, f"FAILED: {e}"))

    # Deep learning
    print("Testing deep learning packages...")
    try:
        import torch

        cuda_status = "CUDA available" if torch.cuda.is_available() else "CPU only"
        results.append(("torch", f"{torch.__version__} ({cuda_status})", "OK"))
    except ImportError as e:
        results.append(("torch", None, f"FAILED: {e}"))

    try:
        import torchvision

        results.append(("torchvision", torchvision.__version__, "OK"))
    except ImportError as e:
        results.append(("torchvision", None, f"FAILED: {e}"))

    try:
        import transformers

        results.append(("transformers", transformers.__version__, "OK"))
    except ImportError as e:
        results.append(("transformers", None, f"FAILED: {e}"))

    # Reinforcement learning
    print("Testing reinforcement learning packages...")
    try:
        import gymnasium

        results.append(("gymnasium", gymnasium.__version__, "OK"))
    except ImportError as e:
        results.append(("gymnasium", None, f"FAILED: {e}"))

    # Optimization and graphs
    print("Testing optimization packages...")
    try:
        import networkx as nx

        results.append(("networkx", nx.__version__, "OK"))
    except ImportError as e:
        results.append(("networkx", None, f"FAILED: {e}"))

    try:
        from ortools.sat.python import cp_model

        import ortools

        results.append(("ortools", ortools.__version__, "OK"))
    except ImportError as e:
        results.append(("ortools", None, f"FAILED: {e}"))

    try:
        import pyswarms

        results.append(("pyswarms", pyswarms.__version__, "OK"))
    except ImportError as e:
        results.append(("pyswarms", None, f"FAILED: {e}"))

    # Datasets
    print("Testing dataset packages...")
    try:
        import datasets

        results.append(("datasets", datasets.__version__, "OK"))
    except ImportError as e:
        results.append(("datasets", None, f"FAILED: {e}"))

    # Jupyter
    print("Testing Jupyter packages...")
    try:
        import jupyter

        results.append(("jupyter", jupyter.__version__, "OK"))
    except ImportError as e:
        results.append(("jupyter", None, f"FAILED: {e}"))

    try:
        import ipykernel

        results.append(("ipykernel", ipykernel.__version__, "OK"))
    except ImportError as e:
        results.append(("ipykernel", None, f"FAILED: {e}"))

    return results


def print_results(results):
    """Print test results in a formatted table."""
    print("\n" + "=" * 60)
    print("PACKAGE TEST RESULTS")
    print("=" * 60)

    max_name_len = max(len(r[0]) for r in results)
    max_ver_len = max(len(str(r[1])) if r[1] else 4 for r in results)

    passed = 0
    failed = 0

    for name, version, status in results:
        ver_str = version if version else "N/A"
        status_marker = "[OK]" if status == "OK" else "[FAIL]"
        print(f"  {name:<{max_name_len}}  {ver_str:<{max_ver_len}}  {status_marker}")
        if status == "OK":
            passed += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"Total: {passed + failed} | Passed: {passed} | Failed: {failed}")
    print("=" * 60)

    if failed == 0:
        print("\nAll packages installed successfully!")
    else:
        print(f"\n{failed} package(s) failed to import. Please check your installation.")

    return failed == 0


def main():
    """Run package tests."""
    print("AI Algorithms Base Environment - Package Test")
    print("-" * 60)
    results = test_packages()
    success = print_results(results)
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
