# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.patient.Patient'


patient_default = mixer.blend(
    __model__,
    pat_id=1,
    cmt_id=1,
    pat_status_cn=1,
    pat_type_cn=1,
    nh_pat_id='NhPatId',
    chart_id='ChartId',
    lname='LName',
    lname_sdx='LNameSdx',
    mname='Mname',
    title_lu='TitleLu',
    suffix_lu='SuffixLu',
    alias='Alias',
    mmname='MmName',
    alt1_id='AltId',
    pref_meth_cont_cn='PrefMeth',
    best_cont_time='BestCon',
    ssn='Social',
    dln='Dln',
    dln_state_cd='DlnStateCd',
    email='Email',
    gender_cd='Gender',
    birth_date=dt_now,
    death_date=dt_now,
    no_safety_caps_yn=False,
    generics_yn=False,
    label_style_cn=1,
    primary_md_id=1,
    secondary_md_id=1,
    edu_level_cn=1,
    ethnicity_cd='Ethnicity',
    marital_status_cd='MaritalStatus',
    religion_cn=1,
    name_spouse='NameSpous',
    primary_lang_cd='PrimaryLang',
    rec_release_status_cn=1,
    rec_release_date=dt_now,
    hh_relation_cn=1,
    hh_pat_id=1,
    fam_relation_cn='FamRelation',
    fam_pat_id=1,
    primary_store_id=1,
    bad_check_yn=False,
    price_formula_id=1,
    cmt='Cmt',
    status_cn=1,
    facility_pat_yn=False,
    conv_code='ConvCode',
    app_flags=1,
    timestmp=dt_now,
    comp_cn=1,
    hp_blnAdmExt=1,
    hp_ExtAtt=1,
    user_def_1='UserDef',
    user_def_2='UserDef',
    user_def_3='UserDef',
    user_def_4='UserDef',
    sc_pat_id=1,
    resp_party_id=1,
    auto_refill_cn=1,
    fill_yn=False,
    fill_stop_date=dt_now,
    fill_resume_date=dt_now,
    fill_stop_reason_cn=1,
    fill_stop_user_id=1,
    registration_date=dt_now,
    anonymous_yn=False,
    market_yn=False,
    representative='Represent',
    discharge_date=dt_now,
    do_not_resuscitate_yn=False,
    discharge_exp_date=dt_now,
    pat_loc_cn=1,
    rx_priority_default_cn=1,
    ship_cn=1,
    residence_cn=1,
    add_user_id=1,
    add_date=dt_now,
    chg_user_id=1,
    chg_date=dt_now,
)


def patient_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
