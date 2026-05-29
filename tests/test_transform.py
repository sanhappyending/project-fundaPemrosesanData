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

from utils.transform import (
    transform_to_DataFrame,
    transform_data
)


class TestTransformData(unittest.TestCase):

    def setUp(self):

        self.sample_data = [
            {
                "Title": "T-shirt 2",
                "Price": "$100.00",
                "Rating": "Rating: ⭐ 4.5 / 5",
                "Colors": "3 Colors",
                "Size": "Size: M",
                "Gender": "Gender: Women",
                "Timestamp": "2025-01-01"
            }
        ]

        self.invalid_data = [
            {
                "Title": "Unknown Product",
                "Price": "Price Unavailable",
                "Rating": "Invalid Rating / 5",
                "Colors": "3 Colors",
                "Size": "Size: M",
                "Gender": "Gender: Women",
                "Timestamp": "2025-01-01"
            }
        ]

    def test_transform_to_dataframe(self):

        result = transform_to_DataFrame(
            self.sample_data
        )

        self.assertIsInstance(
            result,
            pd.DataFrame
        )

    def test_transform_data_success(self):

        df = pd.DataFrame(
            self.sample_data
        )

        result = transform_data(df)

        self.assertEqual(
            result["Price"].iloc[0],
            1600000.0
        )

        self.assertEqual(
            result["Rating"].iloc[0],
            4.5
        )

        self.assertEqual(
            result["Colors"].iloc[0],
            3
        )

        self.assertEqual(
            result["Size"].iloc[0],
            "M"
        )

        self.assertEqual(
            result["Gender"].iloc[0],
            "Women"
        )

    def test_transform_data_invalid(self):

        df = pd.DataFrame(
            self.invalid_data
        )

        result = transform_data(df)

        self.assertTrue(
            result.empty
        )


if __name__ == "__main__":
    unittest.main()