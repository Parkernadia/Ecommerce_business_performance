-- ================================================================
-- E-COMMERCE BUSINESS PERFORMANCE ANALYSIS
-- ================================================================

-- 1. TOTAL NUMBER OF UNIQUE ORDERS

SELECT
    COUNT(DISTINCT order_id) AS total_unique_orders
FROM orders;
-- 2. TOTAL REVENUE GENERATED

SELECT
    ROUND(CAST(SUM(price_usd) AS numeric), 2) AS total_revenue_usd
FROM orders;
-- 3. TOP FIVE PRODUCTS BY REVENUE

SELECT
    p.product_name,
    ROUND(CAST(SUM(oi.price_usd) AS numeric), 2) AS total_revenue_usd
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_revenue_usd DESC; 
LIMIT 5;
-- 4. PRODUCT CATEGORY / TYPE PERFORMANCE
-- Not available for analysis because the products table
-- does not contain a category or product_type column.
-- 5. WEBSITE SESSIONS BY MARKETING SOURCE

SELECT
    COALESCE(utm_source, 'Unattributed') AS marketing_source,
    COUNT(*) AS total_sessions
FROM website_sessions
GROUP BY utm_source
ORDER BY total_sessions DESC;
-- 6. WEBSITE SESSIONS BY DEVICE TYPE

SELECT
    device_type,
    COUNT(*) AS total_sessions
FROM website_sessions
GROUP BY device_type
ORDER BY total_sessions DESC;
-- 7. WEBSITE SESSION-TO-ORDER CONVERSION RATE

SELECT
    COUNT(DISTINCT o.website_session_id) AS sessions_with_orders,
    COUNT(DISTINCT ws.website_session_id) AS total_sessions,
    ROUND(
        CAST(
            COUNT(DISTINCT o.website_session_id) * 100.0
            / COUNT(DISTINCT ws.website_session_id)
            AS numeric
        ),
        2
    ) AS conversion_rate_pct
FROM website_sessions ws
LEFT JOIN orders o
    ON ws.website_session_id = o.website_session_id;
    -- 8. TOTAL REFUNDS AND REFUND VALUE

SELECT
    COUNT(DISTINCT order_item_refund_id) AS total_refunds,
    ROUND(
        CAST(SUM(refund_amount_usd) AS numeric),
        2
    ) AS total_refund_value_usd
FROM order_item_refunds;
-- 9. HIGHEST AND LOWEST REVENUE MONTHS

WITH monthly_revenue AS (
    SELECT
        CAST(DATE_TRUNC('month', created_at) AS date) AS revenue_month,
        ROUND(CAST(SUM(price_usd) AS numeric), 2) AS monthly_revenue_usd
    FROM orders
    GROUP BY DATE_TRUNC('month', created_at)
)

SELECT
    'Highest revenue month' AS performance,
    revenue_month,
    monthly_revenue_usd
FROM monthly_revenue
WHERE monthly_revenue_usd = (
    SELECT MAX(monthly_revenue_usd)
    FROM monthly_revenue
)

UNION ALL

SELECT
    'Lowest revenue month' AS performance,
    revenue_month,
    monthly_revenue_usd
FROM monthly_revenue
WHERE monthly_revenue_usd = (
    SELECT MIN(monthly_revenue_usd)
    FROM monthly_revenue
);
-- 10. AVERAGE ORDER VALUE

SELECT
    ROUND(
        CAST(AVG(price_usd) AS numeric),
        2
    ) AS average_order_value_usd
FROM orders;