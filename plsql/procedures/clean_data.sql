-- =============================================
-- Procedure: clean_data
-- Purpose: Standalone procedure for data cleaning and basic validation
-- Used in Superstore Sales Analytics Project
-- =============================================

CREATE OR REPLACE PROCEDURE clean_data AS
    v_count NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== Starting Data Cleaning Procedure ===');

    -- Delete rows with invalid or missing critical data
    DELETE FROM superstore_raw 
    WHERE sales IS NULL 
       OR profit IS NULL 
       OR quantity <= 0 
       OR order_id IS NULL;

    v_count := SQL%ROWCOUNT;

    COMMIT;

    DBMS_OUTPUT.PUT_LINE('Data Cleaning Completed Successfully!');
    DBMS_OUTPUT.PUT_LINE('Rows removed due to invalid data: ' || v_count);
    DBMS_OUTPUT.PUT_LINE('Remaining records in raw table: ' || 
        (SELECT COUNT(*) FROM superstore_raw));

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error in clean_data procedure: ' || SQLERRM);
        ROLLBACK;
END clean_data;
/