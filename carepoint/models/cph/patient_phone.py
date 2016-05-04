# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from carepoint.models.phone_mixin import PhoneMixin
from sqlalchemy import (Column,
                        Integer,
                        )


class PatientPhone(PhoneMixin, Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'cppat_phone'
    pat_id = Column(Integer, primary_key=True)
