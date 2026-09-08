#!/usr/bin/env python3
"""Bounded independent proof check; performs no solver decision calls."""
import hashlib
import json
from pathlib import Path
import resource
import signal
import socket
import subprocess
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024**3, 1024**3))
signal.alarm(150)
base = Path('/home/amodo/exact-b-k17-unrestricted-triple-caps-20260908')
out = base / 'certificate_export_replay_flushed'
cnf = base / 'unrestricted_triple_caps.cnf'
proof = out / 'complete_solver_proof.drat.bin'
checker = Path('/home/amodo/exact-b-drat-trim-20260908/drat-trim')

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for data in iter(lambda: stream.read(1024**2), b''):
            h.update(data)
    return h.hexdigest()

assert sha(cnf) == '673d26f3dc605da62cdfa335953c1637eb1375f0fee82e85822b68ab4b8747ab'
assert sha(proof) == 'acfb05ad0054a4824fb3529865b12b7b35ae7c7f76741959ba786e3af6d477ea'
cmd = [str(checker), str(cnf), str(proof), '-i', '-t', '120',
       '-c', str(out/'verified_original_core.cnf'),
       '-L', str(out/'verified_proof.lrat')]

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))

started = time.monotonic()
with (out/'independent_drat_check.log').open('x') as stream:
    try:
        result = subprocess.run(cmd, stdout=stream, stderr=subprocess.STDOUT,
                                timeout=140, preexec_fn=limits)
        code = result.returncode
    except subprocess.TimeoutExpired:
        code = 'TIMEOUT'
log = (out/'independent_drat_check.log').read_text()
passed = code == 0 and 's VERIFIED' in log
report = dict(status='INDEPENDENT_DRAT_VERIFIED' if passed else 'NOT_VERIFIED',
              command=cmd, checker_source='https://github.com/marijnheule/drat-trim',
              checker_commit='2e3b2dc0ecf938addbd779d42877b6ed69d9a985',
              checker_sha256=sha(checker), returncode=code,
              cnf_sha256=sha(cnf), proof_sha256=sha(proof),
              elapsed_seconds=time.monotonic()-started,
              limits=dict(cpu_seconds=120, wall_seconds=150,
                          address_space_bytes=4*1024**3, single_file_bytes=1024**3))
if passed:
    report['derived_artifacts'] = {p.name: dict(bytes=p.stat().st_size, sha256=sha(p))
        for p in (out/'verified_original_core.cnf', out/'verified_proof.lrat')}
(out/'independent_drat_check_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(log)
print(json.dumps(report,indent=2),flush=True)
assert passed
