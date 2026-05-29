import pandas as pd
from sqlalchemy import create_engine, text


def store_to_csv(df):
    """
        Menyimpan data ke CSV
    """

    try:

        print("Menyimpan data ke CSV")

        df.to_csv(
            "fashion_product.csv",
            index=False
        )

        print("Data berhasil disimpan ke CSV")

        return True

    except Exception as e:

        print(f"Error menyimpan data ke CSV: {e}")

        return False


def store_to_postgre(df, db_url):
    """
        Menyimpan data ke PostgreSQL
    """

    try:

        engine = create_engine(db_url)

        with engine.connect() as connection:

            print("Berhasil terhubung ke database")

            create_table_query = text("""
                CREATE TABLE IF NOT EXISTS fashion_product (
                    id SERIAL PRIMARY KEY,
                    "Title" TEXT NOT NULL,
                    "Price" FLOAT NOT NULL,
                    "Rating" FLOAT NOT NULL,
                    "Colors" INTEGER NOT NULL,
                    "Size" TEXT NOT NULL,
                    "Gender" TEXT NOT NULL,
                    "Timestamp" TIMESTAMP NOT NULL
                );
            """)

            connection.execute(create_table_query)

            print("Tabel fashion_product berhasil dibuat")

            required_columns = [
                "Title",
                "Price",
                "Rating",
                "Colors",
                "Size",
                "Gender",
                "Timestamp"
            ]

            if not all(
                column in df.columns
                for column in required_columns
            ):
                raise ValueError(
                    "Kolom DataFrame tidak sesuai dengan tabel PostgreSQL"
                )

            print("Menyimpan data ke PostgreSQL")

            df.to_sql(
                "fashion_product",
                con=connection,
                if_exists="append",
                index=False
            )

            connection.commit()

            print("Data berhasil disimpan ke PostgreSQL")

            return True

    except Exception as e:

        print(f"Terjadi kesalahan saat menyimpan data: {e}")

        return False