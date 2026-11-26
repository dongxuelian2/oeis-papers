#!/usr/bin/env python3
"""Produce a compact summary while retaining the complete per-cut certificate."""
import hashlib,json
from pathlib import Path
here=Path(__file__).resolve().parent
full=here/'late-prefix-10000-certificate.json'
certificate=json.loads(full.read_text())
summary=dict(certificate['summary'])
summary['full_certificate_file']=full.name
summary['full_certificate_sha256']=hashlib.sha256(full.read_bytes()).hexdigest()
summary['full_certificate_bytes']=full.stat().st_size
summary['locally_surviving_cut_min']=min(r['k'] for r in certificate['local_survivor_branch_certificates'])
summary['locally_surviving_cut_max']=max(r['k'] for r in certificate['local_survivor_branch_certificates'])
summary['locally_surviving_cut_count']=len(certificate['local_survivor_branch_certificates'])
summary['all_digit_gap_cut_count']=sum(all(b['kind']=='digit_gap' for b in r['branches']) for r in certificate['local_survivor_branch_certificates'])
summary['artifact_sha256']={}
for name in ('verify_late_prefix_candidates.py','LATE_PREFIX_POINTWISE_ENUMERATION.md','LATE_PREFIX_INDEPENDENT_AUDIT.md'):
    path=here/name
    if path.exists():summary['artifact_sha256'][name]=hashlib.sha256(path.read_bytes()).hexdigest()
(here/'late-prefix-10000-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
