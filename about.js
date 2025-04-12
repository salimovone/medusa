let parsed_sigma_rule = {
    'title': 'Potential Download/Upload Activity Using Type Command',
    'id': 'aa0b3a82-eacc-4ec3-9150-b5a9a3e3f82f',
    'status': 'test',
    'description': 'Detects usage of the "type" command to download/upload data from WebDAV server',
    'references': ['https://mr0range.com/a-new-lolbin-using-the-windows-type-command-to-upload-download-files-81d7b6179e22'],
    'author': 'Nasreddine Bencherchali (Nextron Systems)',
    'date': datetime.date(2022, 12, 14),
    'tags': ['attack.command-and-control', 'attack.t1105'],
    'logsource': {
        'product': 'windows',
        'category': 'process_creation'
    },
    'detection': {
        'selection_upload': {
            'CommandLine|contains|all': ['type ', ' > \\\\\\\\']
        },
        'selection_download': {
            'CommandLine|contains|all': ['type \\\\\\\\', ' > ']
        },
        'condition': '1 of selection_*'
    },
    'falsepositives': ['Unknown'],
    'level': 'medium'
}

let detection = {
    'selection_upload':{
        'CommandLine|contains|all': ['type ', ' > \\\\\\\\']
    },
    'selection_download': {
        'CommandLine|contains|all': ['type \\\\\\\\', ' > ']
    }
}