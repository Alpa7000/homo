#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   at l4a msg
modify  record  :   2019-05-25 create file
"""

at_l4a_msg_enum_table = {
0x00011001 : "ID_MSG_L4A_MODE_IND",
0x00011002 : "ID_MSG_L4A_READ_CEREG_CNF",
0x00011003 : "ID_MSG_L4A_CGANS_IND",
0x00011004 : "ID_MSG_DIAG_PSTRANS_REQ",
0x00011005 : "ID_MSG_DIAG_PSTRANS_CNF",
0x00011006 : "ID_MSG_DIAG_PSTRANS_IND",
0x00011007 : "ID_MSG_L4A_CSQ_INFO_REQ",
0x00011008 : "ID_MSG_L4A_CSQ_INFO_CNF",
0x00011009 : "ID_MSG_L4A_RSSI_IND",
0x0001100A : "ID_MSG_L4A_ANLEVEL_IND",
0x0001100B : "ID_MSG_L4A_ANQUERY_INFO_REQ",
0x0001100C : "ID_MSG_L4A_ANQUERY_INFO_CNF",
0x0001100D : "ID_MSG_L4A_LWCLASHQRY_REQ",
0x0001100E : "ID_MSG_L4A_LWCLASHQRY_CNF",
0x0001100F : "ID_MSG_L4A_LWCLASH_IND",
0x00011010 : "ID_MSG_L4A_CERSSI_REQ",
0x00011011 : "ID_MSG_L4A_CERSSI_CNF",
0x00011012 : "ID_MSG_L4A_CERSSI_IND",
0x00011015 : "ID_MSG_L4A_CELL_ID_REQ",
0x00011016 : "ID_MSG_L4A_CELL_ID_CNF",
0x00011017 : "ID_MSG_L4A_LTE_TO_IDLE_REQ",
0x00011018 : "ID_MSG_L4A_LTE_TO_IDLE_CNF",
0x00011019 : "ID_MSG_L4A_LW_THRESHOLD_REQ",
0x0001101A : "ID_MSG_L4A_LW_THRESHOLD_CNF",
0x0001101B : "ID_MSG_L4A_FAST_DORM_REQ",
0x0001101C : "ID_MSG_L4A_FAST_DORM_CNF",
0x00011020 : "ID_MSG_L4A_CELL_INFO_REQ",
0x00011021 : "ID_MSG_L4A_CELL_INFO_CNF",
0x00011022 : "ID_MSG_L4A_CELL_INFO_IND",
0x00011023 : "ID_MSG_L4A_LTE_CS_REQ",
0x00011024 : "ID_MSG_L4A_LTE_CS_CNF",
0x00011025 : "ID_MSG_L4A_IND_CFG_REQ",
0x00011026 : "ID_MSG_L4A_CERSSI_INQ_REQ",
0x00011027 : "ID_MSG_L4A_CERSSI_INQ_CNF",
0x00011028 : "ID_MSG_L4A_ISMCOEXSET_REQ",
0x00011029 : "ID_MSG_L4A_ISMCOEXSET_CNF",
0x00011030 : "ID_MSG_L4A_RADVER_SET_REQ",
0x00011031 : "ID_MSG_L4A_RADVER_SET_CNF",
0x00011032 : "ID_MSG_L4A_LCACELLQRY_REQ",
0x00011033 : "ID_MSG_L4A_LCACELLQRY_CNF",
0x00011034 : "ID_MSG_L4A_LCACELL_IND",
}

def get_at_l4a_msg_str( MsgId):
    for MsgIdIndex in at_l4a_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_l4a_msg_enum_table[MsgIdIndex]

    return "none"