# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        DateTime,
                        ForeignKey,
                        )


class OrderLine(Carepoint.BASE):
    __tablename__ = 'CsOmLine'
    __dbname__ = 'cph'

    line_id = Column(Integer, primary_key=True)
    order_id = Column(
        Integer,
        ForeignKey('CsOm.order_id'),
    )
    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    line_state_cn = Column(Integer)
    line_status_cn = Column(Integer)
    hold_yn = Column(Boolean)
    add_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    chg_date = Column(DateTime)
