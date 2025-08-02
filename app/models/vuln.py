from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.helper.model import Base, id_key


class VulnerailitySeverity(str, Enum):
    LOW = 'low'
    MEDUIM = 'meduim'
    HIGH = 'high'
    CRITICAL = 'critical'


class Department(Base):
    __tablename__ = 'sys_departments'

    id: Mapped[id_key] = mapped_column()
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
