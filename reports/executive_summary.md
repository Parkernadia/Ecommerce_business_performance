# Executive Summary

## Project Overview

This project examines the business performance and customer behaviour of Maven Fuzzy Factory, an e-commerce business. The analysis focuses on sales performance, website traffic, marketing sources, product revenue and customer refunds.

The objective was to use data analytics to identify performance patterns, highlight business gaps and provide recommendations to support decision-making.

## Tools and Methods

The analysis used Python and pandas for data inspection, validation and preparation, PostgreSQL for data storage and SQL-based business analysis and Microsoft Power BI for interactive visualisation.

The analysis covered six datasets: website sessions, website pageviews, orders, order items, order item refunds and products.

## Key Performance Results

| Metric | Result |
| --- | ---: |
| Total Orders | 32,313 |
| Total Revenue | $1,938,509.75 |
| Average Order Value | $59.99 |
| Website Sessions | 472,871 |
| Session-to-Order Conversion Rate | 6.83% |
| Total Refunds | 1,731 |
| Total Refund Value | $85,338.69 |

## Key Findings

1. **Product performance:** The Original Mr. Fuzzy generated $1,211,057.74 in revenue, making it the leading product and accounting for approximately 62.5% of total product revenue.

2. **Marketing acquisition:** Google Search (`gsearch`) generated 316,035 sessions, representing approximately 66.8% of all website sessions. However, traffic volume alone does not establish marketing profitability.

3. **Unattributed traffic:** 83,328 sessions, approximately 17.6% of total traffic, had no recorded UTM source. This limits the completeness of marketing attribution.

4. **Device usage:** Desktop accounted for 327,027 sessions (69.2%) while mobile accounted for 145,844 sessions (30.8%).

5. **Refunds:** The business recorded 1,731 refunds with a combined value of $85,338.69.

6. **Monthly revenue:** December 2014 recorded the highest monthly revenue at $144,823.02. March 2012 recorded the lowest at $2,999.40, although this was a partial month.

## Recommendations

- Review marketing performance using conversion and acquisition cost metrics rather than session volume alone.
- Improve UTM tracking and campaign tagging to reduce unattributed website traffic.
- Investigate mobile customer journeys and conversion performance to identify possible usability improvements.
- Examine refund patterns by product and order to identify potential areas for product or service improvement.
- Monitor the business's dependence on its leading product and assess opportunities to strengthen revenue from other products.

## Limitations

The products dataset did not contain product category or type information, preventing category-level performance analysis.

Missing UTM information limited the attribution of some website sessions. In addition, the available data covers March 2012 to April 2015, so the findings describe historical rather than current business performance.

## Conclusion

The analysis provides an overview of Maven Fuzzy Factory's historical sales, traffic, product and refund performance. The findings highlight the importance of reliable marketing attribution, product revenue monitoring and customer experience analysis in supporting evidence-based business decisions.
