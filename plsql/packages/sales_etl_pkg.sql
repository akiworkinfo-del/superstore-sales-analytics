-- =============================================
-- Package: sales_etl_pkg
-- Purpose: ETL operations for Superstore Sales Analytics Project
-- =============================================

CREATE OR REPLACE PACKAGE sales_etl_pkg AS

    PROCEDURE run_full_etl;
    PROCEDURE clean_and_transform;

END sales_etl_pkg;
/

CREATE OR REPLACE PACKAGE BODY sales_etl_pkg AS

    PROCEDURE run_full_etl IS
    BEGIN
        DBMS_OUTPUT.PUT_LINE('=== Starting Full ETL Process ===');
        clean_and_transform;
        DBMS_OUTPUT.PUT_LINE('=== Full ETL Process Completed Successfully! ===');
    END run_full_etl;

    PROCEDURE clean_and_transform IS
    BEGIN
        -- Clear previous transformed data
        DELETE FROM superstore_clean;

        -- Transform and insert data
        INSERT INTO superstore_clean 
        SELECT 
            row_id,
            order_id,
            order_date,
            ship_date,
            ship_mode,
            customer_id,
            customer_name,
            segment,
            country,
            city,
            state,
            region,
            product_id,
            category,
            sub_category,
            product_name,
            sales,
            quantity,
            discount,
            profit,
            (sales - profit) AS cost,
            ROUND(CASE WHEN sales = 0 THEN 0 ELSE (profit / sales) * 100 END, 2) AS profit_margin,
            EXTRACT(YEAR FROM order_date) AS sales_year,
            EXTRACT(MONTH FROM order_date) AS sales_month,
            CASE 
                WHEN profit > 0 THEN 'Profitable' 
                WHEN profit < 0 THEN 'Loss Making' 
                ELSE 'Break Even' 
            END AS profit_flag
        FROM superstore_raw 
        WHERE sales IS NOT NULL 
          AND quantity > 0;

        COMMIT;
        
        DBMS_OUTPUT.PUT_LINE('=== Data Transformation Completed Successfully! ===');
        DBMS_OUTPUT.PUT_LINE('Records Transformed: ' || SQL%ROWCOUNT);
        
    EXCEPTION 
        WHEN OTHERS THEN 
            DBMS_OUTPUT.PUT_LINE('Error during transformation: ' || SQLERRM);
            ROLLBACK;
    END clean_and_transform;

END sales_etl_pkg;
/