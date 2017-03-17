# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2007-Now Mick Tseng(<suncombo@gmail.com>).

{
    'name': '台灣會計科目表',
    'version': '1.0',
    'category': 'Localization',
    'author': 'suncombo@gmail.com',
    'maintainer': 'suncombo@gmail.com',
    'website': 'https://github.com/micktseng/l10n_tw',
    'description': """
        台灣會計科目表
    """,
    'depends': ['base', 'account'],
    'data': [
        'data/l10n_tw_chart_data.xml',
        'data/account_chart_template_data.yml',
        'data/res_country_state_data.xml',
    ],
    'license': 'GPL-3',
    'installable': True,
}
