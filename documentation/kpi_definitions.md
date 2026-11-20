# KPI Definitions

## Overview

This document defines the key performance indicators used in the E-commerce Business Performance and Customer Behaviour Analysis.

| KPI | Definition | Calculation |
| --- | --- | --- |
| Total Orders | Total number of unique orders placed | Distinct count of `order_id` |
| Total Revenue | Total revenue generated from orders | Sum of `orders.price_usd` |
| Total Refunds | Total monetary value refunded to customers | Sum of `refund_amount_usd` |
| Average Order Value | Average revenue generated per order | Total order revenue / total orders |
| Website Sessions | Total number of unique website sessions | Distinct count of `website_session_id` |
| Conversion Rate | Percentage of website sessions that resulted in an order | Sessions with orders / total website sessions × 100 |

## Supporting Measures

- **Product Revenue:** Sum of `order_items.price_usd`, grouped by product.
- **Marketing Sessions:** Count of website sessions grouped by `utm_source`. Missing sources are classified as Unattributed.
- **Device Sessions:** Count of website sessions grouped by device type.
- **Monthly Revenue:** Sum of order revenue grouped by order month.
- **Refund Count:** Distinct count of refund records.

## Data Considerations

- Missing marketing attribution is retained and classified as Unattributed rather than assigned to a marketing source.
- Product category performance could not be assessed because the products dataset does not contain a category or product type field.
- March 2012 represents a partial month because the available data begins on 19 March 2012.
- Refund value represents recorded refunds and should not be interpreted as a refund rate without an appropriate denominator and matching time period.
