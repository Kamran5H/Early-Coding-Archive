import py_compile
import unittest
from pathlib import Path
from boiling_point_ml_model import predict_boiling_point


class TestEarlyCodingArchive(unittest.TestCase):
    def test_boiling_point_prediction(self):
        bp = predict_boiling_point(60.0)
        self.assertAlmostEqual(bp, 64.59, places=2)

    def test_all_python_scripts_compile(self):
        root = Path(__file__).resolve().parent.parent
        for py_file in root.glob("*.py"):
            py_compile.compile(str(py_file), doraise=True)


if __name__ == "__main__":
    unittest.main()
