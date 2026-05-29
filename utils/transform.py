import pandas as pd

def transform_to_DataFrame(data):

    try:
        df = pd.DataFrame(data)
        return df

    except Exception as e:
        print(f"Error transforming data to DataFrame: {e}")
        return None


def transform_data(df):

    if df.empty:
        print("Input DataFrame kosong")
        return df

    try:

        # Filter data invalid
        df_clean = df[
            ~df.apply(
                lambda row:
                row["Title"] == "Unknown Product" or
                row["Rating"] in ["Invalid Rating / 5", "Not Rated"] or
                row["Price"] == "Price Unavailable",
                axis=1
            )
        ]

        # Hapus duplicate dan null
        df_clean = df_clean.drop_duplicates().dropna()

        # PRICE
        df_clean["Price"] = (
            df_clean["Price"]
            .astype(str)
            .str.replace('$', '', regex=False)
        )

        df_clean["Price"] = (
            pd.to_numeric(df_clean["Price"], errors='coerce')
            * 16000
        ).astype(float)

        # RATING
        df_clean["Rating"] = (
            df_clean["Rating"]
            .astype(str)
            .str.extract(r'(\d+\.\d+)')[0]
        )

        df_clean["Rating"] = pd.to_numeric(
            df_clean["Rating"],
            errors='coerce'
        ).astype(float)

        # COLORS
        df_clean["Colors"] = (
            df_clean["Colors"]
            .astype(str)
            .str.extract(r'(\d+)')[0]
        )

        df_clean["Colors"] = pd.to_numeric(
            df_clean["Colors"],
            errors='coerce'
        ).astype('int64')

        # TITLE
        df_clean["Title"] = df_clean["Title"].astype(str)

        # SIZE
        df_clean["Size"] = (
            df_clean["Size"]
            .astype(str)
            .str.replace("Size:", "", regex=False)
            .str.strip()
        )

        # GENDER
        df_clean["Gender"] = (
            df_clean["Gender"]
            .astype(str)
            .str.replace("Gender:", "", regex=False)
            .str.strip()
        )

        # Hapus NaN lagi
        df_clean = df_clean.dropna()

        # Reset index
        df_clean = df_clean.reset_index(drop=True)

        print(df_clean.info())

        # Reset index
        df_clean = df_clean.reset_index(drop=True)

        # Preview data
        print("\nPreview Data:")
        print(df_clean.head())

        return df_clean

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None