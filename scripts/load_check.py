import time
import pandas as pd

RAW = "raw"

tables = {
    "aisles": dict(aisle_id="int16", aisle="string"),
    "departments": dict(department_id="int8", department="string"),
    "products": dict(product_id="int32", product_name="string",
                     aisle_id="int16", department_id="int8"),
    "orders": dict(order_id="int32", user_id="int32", eval_set="category",
                   order_number="int16", order_dow="int8",
                   order_hour_of_day="int8", days_since_prior_order="float32"),
    "order_products__train": dict(order_id="int32", product_id="int32",
                                  add_to_cart_order="int16", reordered="int8"),
    "order_products__prior": dict(order_id="int32", product_id="int32",
                                  add_to_cart_order="int16", reordered="int8"),
}

for name, dtypes in tables.items():
    t0 = time.time()
    df = pd.read_csv(f"{RAW}/{name}.csv", dtype=dtypes)
    mem_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"\n=== {name} ===")
    print(f"rows: {len(df):,} | columns: {df.shape[1]} | memory: {mem_mb:,.0f} MB")
    nulls = df.isna().sum()
    print("nulls:", nulls[nulls > 0].to_dict() or "none")
    print("duplicate rows:", f"{df.duplicated().sum():,}")
    print(f"time: {time.time() - t0:.1f}s")
    del df
