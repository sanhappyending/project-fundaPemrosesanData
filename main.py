from utils.extract import scrape_store_products
from utils.transform import (
    transform_to_DataFrame,
    transform_data
)
from utils.load import (
    store_to_csv,
    store_to_postgre
)

def main():
    """
        Fungsi utama ETL fashion product
    """

    BASE_URL = "https://fashion-studio.dicoding.dev/"

    try:

        # Extract
        print("Memulai proses extract")

        raw_data = scrape_store_products(
            BASE_URL
        )

        if not raw_data:
            print("Data tidak ditemukan")
            return

        print(f"Total data berhasil diambil: {len(raw_data)}")

        # Transform
        print("Memulai proses transform")

        df = transform_to_DataFrame(
            raw_data
        )

        if df is None:
            print("Gagal membuat DataFrame")
            return

        clean_df = transform_data(
            df
        )

        if clean_df is None:
            print("Gagal membersihkan data")
            return

        print("Transformasi data berhasil")

        # Load CSV
        print("Memulai penyimpanan CSV")

        store_to_csv(
            clean_df
        )

        # Load PostgreSQL
        print("Memulai penyimpanan PostgreSQL")

        db_url = (
            "postgresql+psycopg2://postgres:"
            "12345@localhost:5432/fashiondb"
        )

        store_to_postgre(
            clean_df,
            db_url
        )

        print("Proses ETL selesai")

    except Exception as e:
        print(f"Terjadi kesalahan pada proses ETL: {e}")


if __name__ == "__main__":
    main()