OPTIONS (SKIP=1, ERRORS=10000)
LOAD DATA
INFILE 'superstore_clean.csv'
BADFILE 'superstore.bad'
DISCARDFILE 'superstore.dsc'
APPEND INTO TABLE superstore_raw
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
    row_id,
    order_id,
    order_date     DATE "MM/DD/YYYY",
    ship_date      DATE "MM/DD/YYYY",
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    sales          "TO_NUMBER(REPLACE(:sales,    ',', ''))",
    quantity       "TO_NUMBER(REPLACE(:quantity, ',', ''))",
    discount       "TO_NUMBER(REPLACE(:discount, ',', ''))",
    profit         "TO_NUMBER(REPLACE(:profit,   ',', ''))"
)