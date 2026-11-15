from datetime import datetime, timezone
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    customer_tier: Mapped[str] = mapped_column(String(20), default="Standard")  # Standard, Silver, Gold, Platinum
    total_orders_count: Mapped[int] = mapped_column(Integer, default=0)
    total_returns_count: Mapped[int] = mapped_column(Integer, default=0)
    lifetime_spend: Mapped[float] = mapped_column(Float, default=0.0)


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    product_name: Mapped[str] = mapped_column(String(150), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Apparel, Electronics, Home
    price: Mapped[float] = mapped_column(Float, nullable=False)
    warranty_days: Mapped[int] = mapped_column(Integer, default=30)


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    customer_id: Mapped[str] = mapped_column(String(50), ForeignKey("customers.customer_id"), nullable=False)
    product_id: Mapped[str] = mapped_column(String(50), ForeignKey("products.product_id"), nullable=False)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    delivery_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    order_status: Mapped[str] = mapped_column(String(30), default="Delivered")  # Delivered, Shipped, Processing, Cancelled


class ReturnRecord(Base):
    __tablename__ = "returns"

    return_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    order_id: Mapped[str] = mapped_column(String(50), ForeignKey("orders.order_id"), nullable=False)
    product_id: Mapped[str] = mapped_column(String(50), ForeignKey("products.product_id"), nullable=False)
    customer_id: Mapped[str] = mapped_column(String(50), ForeignKey("customers.customer_id"), nullable=False)
    claim_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    return_reason: Mapped[str] = mapped_column(Text, nullable=False)
    customer_reported_condition: Mapped[str] = mapped_column(String(50), default="Unopened")  # Unopened, Opened, Defective, Damaged
    return_status: Mapped[str] = mapped_column(String(50), default="PENDING")  # PENDING, APPROVE_INSTANT_REFUND, ESCALATE, etc.
    audit_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
