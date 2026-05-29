import os
import sys
import unittest

import pandas as pd

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from utils.load import (
    store_to_csv,
    store_to_postgre
)


class TestLoadData(unittest.TestCase):

    def setUp(self):

        self.sample_df = pd.DataFrame([
            {
                "Title": "T-shirt 2",
                "Price": 1600000.0,
                "Rating": 4.5,
                "Colors": 3,
                "Size": "M",
                "Gender": "Women",
                "Timestamp": "2025-01-01"
            }
        ])

    def test_store_to_csv(self):

        store_to_csv(
            self.sample_df
        )

        self.assertTrue(
            os.path.exists(
                "fashion_product.csv"
            )
        )

    def test_store_to_postgre_invalid_connection(self):

        result = store_to_postgre(
            self.sample_df,
            "postgresql://invalid:invalid@localhost/test"
        )

        self.assertFalse(
            result
        )


if __name__ == "__main__":
    unittest.main()