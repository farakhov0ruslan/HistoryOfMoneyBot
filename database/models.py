from sqlalchemy import String, Text, DateTime, func, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class EraInfo(Base):
    __tablename__ = 'erainfo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)


class ContentItem(Base):
    __tablename__ = 'content_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    era_id: Mapped[int] = mapped_column(ForeignKey('erainfo.id'))
    order: Mapped[int] = mapped_column(Integer)  # для сохранения последовательности
    type: Mapped[str] = mapped_column(String(50))  # 'text' или 'image'
    content: Mapped[str] = mapped_column(Text)

    era = relationship("EraInfo", back_populates="items")


EraInfo.items = relationship("ContentItem", order_by=ContentItem.order, back_populates="era")
