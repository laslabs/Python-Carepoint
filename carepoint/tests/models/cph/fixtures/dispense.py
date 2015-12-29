# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Vinnie Corcoran <vcorcoran@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from mixer.backend.sqlalchemy import mixer
from datetime import datetime, date

__model__ = 'carepoint.models.cph.dispense.Dispense'

dispense_default = mixer.blend(
    __model__,
    rx_id = 1,
    store_id = 1,
    disp_ndc = 'DispNdc',
    disp_drug_name = 'DispDrugName',
    prod_expire_date = dt_now,
    mfg = 'Mfg',
    orig_mfg = 'OrifMfg',
    pkg_size = 1,
    rxdisp_id = 1,
    fill_no = 1,
    dispense_date = dt_now,
    dispense_qty = 1,
    disp_days_supply = 1,
    sig_text = 'SigText',
    sched_of_admin_cn = 1,
    freq_of_admin = 1,
    units_per_dose = 1,
    lot_number = 'LotNumber',
    disp_awp = 1,
    disp_aac = 1,
    disp_mac = 1,
    disp_ful = 1,
    disp_udef = 1,
    tech_initals = 'TechInitials',
    rph_initials = 'RphInitials',
    cnsl_initials = 'CnslInitials',
    icd9 = 'Icd',
    daw_disp_cn = 1,
    level_of_service = 1,
    cmt = 'cmt',
    status_cn = 1,
    alt_pick_up_id = 1,
    alt_pick_up_cn = 1,
    clarification_fill = 1,
    trip_no = 1,
    gpi_disp = 1,
    label_3pty_yn = False,
    reject_3pty_yn = False,
    pay_type_cn = 1,
    price_differs_yn = False,
    pat_loc_cn = 1,
    billing_units = 'BillingUnits',
    price_table_id = 1,
    app_flags = 1,
    timestmp = dt_now,
    price_meth_cn = 1,
    uu = 'UU',
    p_tbl_override_yn = False,
    label_id = 1,
    billing_hold = 1,
    post_bal_yn = False,
    inv_no = 'InvNo',
    disp_qty_delta = 1,
    brand_med_nec_yn = False,
    Other_coverage_cd = 1,
    epsdt_yn = False,
    exempt_cd = 1,
    num_labels = 1,
    location = 'Location',
    qty_override = 1,
    dur_summary = 'DurSummary',
    cov_overrides = 1,
    use_secondary_ins_yn = False,
    hp_blnRxExtr = 1,
    item_id = 1,
    ud_override = 'UdOverride',
    disp_status_cn = 1,
    order_id = 1,
    sig_id = 1,
    counsel_yn = 1,
    processing_date = dt_now,
    hcpcs_mod_cn = 1,
    acct_id = 1,
    track_pat_resp_yn = 1,
    track_org_resp_yn = 1,
    label_fac_id = 1,
    extern_process_cn = 1,
    price_ovr_user_id = 1,
    price_ovr_reason_cn = 1,
    wf_status_cn = 1,
    verify_user_id = 1,
    verify_timestamp = dt_now,
    ar_hold = 1,
    disp_type_cn = 1,
    own_use_pricing_yn = 1,
    pos_processed_yn = 1,
    prescriber_cn = 1,
    visit_nbr = 'VisitNbr',
    disp_udef2 = 1,
    SecondaryICD9 = 'SecondaryIcd',
    uandc_pricing_used_yn = 1,
    special_pkg_ind_cn = 1,
    delay_reason_cn = 1,
    place_of_service_cn = 1,
    pat_residence_cn = 1,
    compound_type_cn = 1,
    pharmacy_service_type_cn = 1,
    admin_start_date = dt_now,
    ClariFill_2 = 1,
    ClariFill_3 = 1,
    other_coverage_cd_2 = 1,
    pat_assign_ind_yn = 1,
    prov_assign_ind_yn = 1,
    route_of_admin_ovr = 'RouteAdmin',
    csr_pickup_id = 1,
    icd10 = 'icd',
    secondaryicd10 = 'secondaryicd',
    add_user_id = 1,
    add_date = dt_now,
    chg_user_id = 1,
    chg_date = dt_now,
)

dispense_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)