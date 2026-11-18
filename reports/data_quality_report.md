# Data Quality Report

## E-commerce Business Performance and Customer Behaviour Analysis

### 1. Overview

This report documents the data quality assessment conducted on the Maven Fuzzy Factory e-commerce datasets before analysis. The assessment covered dataset structure, missing values, duplicate records, data types, primary and foreign key integrity, value validity and business-rule consistency.

### 2. Dataset Overview

| Dataset | Rows | Columns |
| --- | ---: | ---: |
| website_sessions | 472,871 | 9 |
| website_pageviews | 1,048,575 | 4 |
| orders | 32,313 | 8 |
| order_items | 40,025 | 7 |
| order_item_refunds | 1,731 | 5 |
| products | 4 | 3 |
| Data dictionary | 36 | 3 |

### 3. Data Quality Findings

#### 3.1 Missing Values

Missing values were identified in the following fields:

| Dataset | Column | Missing Values |
| --- | --- | ---: |
| website_sessions | utm_source | 83,328 |
| website_sessions | utm_campaign | 83,328 |
| website_sessions | utm_content | 83,328 |
| website_sessions | http_referer | 39,917 |

The three UTM fields have missing values in the same 83,328 sessions. Of these sessions, 43,411 have an HTTP referer while 39,917 do not.

The available referer URLs correspond to gsearch, bsearch and socialbook. Missing UTM values will therefore be retained rather than automatically replaced or treated as invalid records.

#### 3.2 Duplicate Records

No duplicate full rows were identified in any of the seven datasets.

No duplicate primary key values were identified in the six business tables.

#### 3.3 Data Types and Date Validation

Date fields were initially imported as strings. All six business tables passed date parsing validation with zero invalid dates.

The observed date ranges extend from March 2012 to April 2015.

Date fields will be converted to appropriate datetime types during data preparation.

#### 3.4 Primary and Foreign Key Integrity

All primary keys passed uniqueness checks.

All eight foreign key relationships tested returned zero unmatched records. Refund records were also checked against their corresponding order items, with no order inconsistencies identified.

#### 3.5 Value Validation

The binary fields `is_repeat_session` and `is_primary_item` contain only 0 and 1.

The `device_type` field contains desktop and mobile values.

No negative values were identified in order quantities, prices, costs or refund amounts.

#### 3.6 Business-Rule Validation

The following checks were completed:

| Validation | Result |
| --- | --- |
| Order item counts against recorded quantities | No mismatches |
| Order revenue against order item totals | No mismatches |
| Total absolute revenue difference | $0.00 |
| Refund amounts against item prices | No excessive refunds |
| Order item dates against order dates | No inconsistencies |
| Refund dates against order item dates | No inconsistencies |

### 4. Data Preparation Decisions

Based on the assessment:

- Retain records with missing marketing attribution.
- Do not automatically assign missing UTM values to a marketing channel.
- Preserve the existing primary and foreign key relationships.
- Convert date fields to datetime types during preparation.
- Retain all records unless subsequent analysis identifies a specific issue requiring treatment.
- Document any additional transformations applied during preparation.

### 5. Limitations

The assessment establishes structural integrity and checks selected business rules. It does not establish that every business event was captured in the source systems or that the available marketing attribution represents all traffic sources.

The missing UTM values also limit the ability to attribute every website session to a named marketing channel.

### 6. Conclusion

The datasets passed the structural, relationship and business-rule checks performed. No duplicate records, unmatched relationships or reconciliation discrepancies were identified in the checks completed.

The datasets are suitable to proceed to the preparation stage, with missing marketing attribution retained and documented.
