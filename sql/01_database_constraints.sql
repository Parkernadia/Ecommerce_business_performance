
-- ================================================================
-- E-COMMERCE BUSINESS PERFORMANCE AND CUSTOMER BEHAVIOUR ANALYSIS
-- DATABASE CONSTRAINTS
-- ================================================================

-- 1. PRIMARY KEYS

ALTER TABLE website_sessions
ADD CONSTRAINT pk_website_sessions
PRIMARY KEY (website_session_id);

ALTER TABLE website_pageviews
ADD CONSTRAINT pk_website_pageviews
PRIMARY KEY (website_pageview_id);

ALTER TABLE orders
ADD CONSTRAINT pk_orders
PRIMARY KEY (order_id);

ALTER TABLE order_items
ADD CONSTRAINT pk_order_items
PRIMARY KEY (order_item_id);

ALTER TABLE order_item_refunds
ADD CONSTRAINT pk_order_item_refunds
PRIMARY KEY (order_item_refund_id);

ALTER TABLE products
ADD CONSTRAINT pk_products
PRIMARY KEY (product_id);


-- 2. FOREIGN KEYS

ALTER TABLE website_pageviews
ADD CONSTRAINT fk_pageviews_sessions
FOREIGN KEY (website_session_id)
REFERENCES website_sessions (website_session_id);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_sessions
FOREIGN KEY (website_session_id)
REFERENCES website_sessions (website_session_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id)
REFERENCES orders (order_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_products
FOREIGN KEY (product_id)
REFERENCES products (product_id);

ALTER TABLE order_item_refunds
ADD CONSTRAINT fk_refunds_order_items
FOREIGN KEY (order_item_id)
REFERENCES order_items (order_item_id);

ALTER TABLE order_item_refunds
ADD CONSTRAINT fk_refunds_orders
FOREIGN KEY (order_id)
REFERENCES orders (order_id);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_products
FOREIGN KEY (primary_product_id)
REFERENCES products (product_id);
