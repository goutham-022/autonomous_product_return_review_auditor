"""
Database Seeding Script for Autonomous Product Return & Review Auditor.

Populates PostgreSQL with curated synthetic test fixtures:
- High-trust VIP Customers (Pooja Sharma)
- High-velocity Serial Returners (Rahul Verma - 80% return velocity)
- Target Products (Defective Dress, Earbuds, High-Value OLED TV)
- Order history with exact delivery dates calibrated for return window tests.
"""

from datetime import datetime, timezone, timedelta
from src.database.connection import SessionLocal, init_db, engine
from src.database.models import Customer, Product, Order, ReturnRecord


def seed_database(reset: bool = False):
    print("🔄 Ensuring schema and pgvector extension are initialized...")
    init_db()

    with SessionLocal() as db:
        if reset:
            print("⚠️ Reset flag provided: Purging existing records...")
            db.query(ReturnRecord).delete()
            db.query(Order).delete()
            db.query(Product).delete()
            db.query(Customer).delete()
            db.commit()

        # Check if already seeded (Idempotency check)
        existing_customers = db.query(Customer).count()
        if existing_customers > 0 and not reset:
            print(f"ℹ️ Database already contains {existing_customers} customers. Seeding skipped.")
            print("💡 Tip: Run with seed_database(reset=True) or execute with '--reset' to re-seed.")
            return

        print("🌱 Seeding Curated Synthetic Data for Return Auditor...")

        # ----------------------------------------------------------------------
        # 1. CUSTOMERS
        # ----------------------------------------------------------------------
        customers = [
            Customer(
                customer_id="CUST_1001",
                name="Pooja Sharma",
                email="pooja.sharma@example.com",
                customer_tier="Platinum",
                total_orders_count=45,
                total_returns_count=2,
                lifetime_spend=124500.00,
            ),
            Customer(
                customer_id="CUST_1002",
                name="Rahul Verma",
                email="rahul.verma@example.com",
                customer_tier="Standard",
                total_orders_count=10,
                total_returns_count=8,  # 80% return velocity -> Triggers Fraud Hard Gate!
                lifetime_spend=14800.00,
            ),
            Customer(
                customer_id="CUST_1003",
                name="Ananya Iyer",
                email="ananya.iyer@example.com",
                customer_tier="Gold",
                total_orders_count=22,
                total_returns_count=3,
                lifetime_spend=58200.00,
            ),
            Customer(
                customer_id="CUST_1004",
                name="Vikram Malhotra",
                email="vikram.m@example.com",
                customer_tier="Silver",
                total_orders_count=8,
                total_returns_count=1,
                lifetime_spend=21000.00,
            ),
        ]
        db.add_all(customers)
        db.flush()

        # ----------------------------------------------------------------------
        # 2. PRODUCTS
        # ----------------------------------------------------------------------
        products = [
            Product(
                product_id="PROD_DRESS_01",
                product_name="Silk Embroidered Anarkali Dress",
                category="Apparel",
                price=3499.00,
                warranty_days=15,  # 15-day return window
            ),
            Product(
                product_id="PROD_AUDIO_02",
                product_name="Noise-Cancelling Wireless Earbuds",
                category="Electronics",
                price=2999.00,
                warranty_days=7,  # 7-day replacement only
            ),
            Product(
                product_id="PROD_TV_03",
                product_name="Smart 4K Ultra HD OLED TV 55-inch",
                category="Electronics",
                price=54999.00,  # Exceeds Rs 5,000 autonomous refund cap -> Must Escalate!
                warranty_days=365,
            ),
            Product(
                product_id="PROD_SHOES_04",
                product_name="Running Trail Performance Shoes",
                category="Apparel",
                price=4200.00,
                warranty_days=30,
            ),
            Product(
                product_id="PROD_COOK_05",
                product_name="Hard Anodized Non-Stick Cookware Set",
                category="Home",
                price=3899.00,
                warranty_days=60,
            ),
        ]
        db.add_all(products)
        db.flush()

        # ----------------------------------------------------------------------
        # 3. ORDERS (Dynamically calibrated relative to current date)
        # ----------------------------------------------------------------------
        now = datetime.now(timezone.utc).replace(tzinfo=None)

        orders = [
            # Pooja's Active Order: Delivered 8 days ago -> INSIDE 15-day window for PROD_DRESS_01
            Order(
                order_id="ORD_9001",
                customer_id="CUST_1001",
                product_id="PROD_DRESS_01",
                order_date=now - timedelta(days=12),
                delivery_date=now - timedelta(days=8),
                unit_price=3499.00,
                order_status="Delivered",
            ),
            # Pooja's Past Order: Delivered 35 days ago -> OUT OF 7-day window for PROD_AUDIO_02
            Order(
                order_id="ORD_9002",
                customer_id="CUST_1001",
                product_id="PROD_AUDIO_02",
                order_date=now - timedelta(days=40),
                delivery_date=now - timedelta(days=35),
                unit_price=2999.00,
                order_status="Delivered",
            ),
            # Rahul's Order (Serial Returner): Delivered 6 days ago -> INSIDE 30-day window
            Order(
                order_id="ORD_9003",
                customer_id="CUST_1002",
                product_id="PROD_SHOES_04",
                order_date=now - timedelta(days=10),
                delivery_date=now - timedelta(days=6),
                unit_price=4200.00,
                order_status="Delivered",
            ),
            # Ananya's High-Value TV Order: Delivered 3 days ago -> Exceeds Rs 5,000 Cap
            Order(
                order_id="ORD_9004",
                customer_id="CUST_1003",
                product_id="PROD_TV_03",
                order_date=now - timedelta(days=6),
                delivery_date=now - timedelta(days=3),
                unit_price=54999.00,
                order_status="Delivered",
            ),
            # Vikram's Cookware Order: Delivered 15 days ago -> INSIDE 60-day window
            Order(
                order_id="ORD_9005",
                customer_id="CUST_1004",
                product_id="PROD_COOK_05",
                order_date=now - timedelta(days=20),
                delivery_date=now - timedelta(days=15),
                unit_price=3899.00,
                order_status="Delivered",
            ),
        ]
        db.add_all(orders)
        db.flush()

        # ----------------------------------------------------------------------
        # 4. HISTORICAL RETURNS (Baseline returns for audit history)
        # ----------------------------------------------------------------------
        historical_returns = [
            ReturnRecord(
                return_id="RET_3001",
                order_id="ORD_9002",
                product_id="PROD_AUDIO_02",
                customer_id="CUST_1001",
                claim_date=now - timedelta(days=32),
                return_reason="Left earbud stopped charging after 3 days.",
                customer_reported_condition="Defective",
                return_status="APPROVE_REPLACEMENT_ONLY",
                audit_notes="Eligible for manufacturer warranty replacement.",
            ),
            ReturnRecord(
                return_id="RET_3002",
                order_id="ORD_9003",
                product_id="PROD_SHOES_04",
                customer_id="CUST_1002",
                claim_date=now - timedelta(days=5),
                return_reason="Size slightly tight around the toes.",
                customer_reported_condition="Opened",
                return_status="PENDING",
                audit_notes="Customer return velocity: 80%. High fraud risk.",
            ),
        ]
        db.add_all(historical_returns)
        db.commit()

        print("✅ Successfully seeded PostgreSQL:")
        print(f"   • Customers: {len(customers)}")
        print(f"   • Products:  {len(products)}")
        print(f"   • Orders:    {len(orders)}")
        print(f"   • Returns:   {len(historical_returns)}")


if __name__ == "__main__":
    import sys
    reset_flag = "--reset" in sys.argv
    seed_database(reset=reset_flag)
