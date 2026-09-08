#!/usr/bin/env python3
"""Bounded certificate-export repair, using the identical immutable CNF.

This is one additional decision call, not a new cap instance or seed.
The original solver result and truncated proof remain untouched.
All mathematical execution is restricted to h100/arboghast.
"""
import hashlib
import ctypes
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import socket
import subprocess
import time

assert socket.gethostname().split('.')[0] == 'arboghast'
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024**3, 1024**3))
signal.alarm(90)
BASE = Path('/home/amodo/exact-b-k17-unrestricted-triple-caps-20260908')
OUT = BASE / 'certificate_export_replay_flushed'
OUT.mkdir(exist_ok=False)
CNF = BASE / 'unrestricted_triple_caps.cnf'
EXPECTED = '673d26f3dc605da62cdfa335953c1637eb1375f0fee82e85822b68ab4b8747ab'
CHECKER = Path('/home/amodo/exact-b-drat-trim-20260908/drat-trim')
from pysat.solvers import Cadical195

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024**2), b''):
            h.update(chunk)
    return h.hexdigest()

def complete_binary(path):
    data = path.read_bytes()
    offset = steps = empty_additions = 0
    while offset < len(data):
        op = data[offset]
        assert op in (ord('a'), ord('d')), (offset, op)
        offset += 1
        literal_count = 0
        while True:
            value = shift = 0
            while True:
                assert offset < len(data), 'Truncated binary proof'
                byte = data[offset]
                offset += 1
                value |= (byte & 127) << shift
                if byte < 128:
                    break
                shift += 7
            if value == 0:
                break
            literal_count += 1
        steps += 1
        empty_additions += op == ord('a') and literal_count == 0
    return dict(bytes=len(data), operations=steps,
                empty_additions=empty_additions, complete=True)

def flush_then_capture(solver, path):
    # Flush the actual C stdio streams while their descriptors are alive.
    # Python prfile.flush() does not flush a separate native FILE buffer;
    # solver.delete() alone also failed the tiny export regression.
    libc = ctypes.CDLL(None)
    libc.fflush.argtypes = [ctypes.c_void_p]
    libc.fflush.restype = ctypes.c_int
    assert libc.fflush(None) == 0
    solver.prfile.seek(0)
    with path.open('xb') as dest:
        shutil.copyfileobj(solver.prfile, dest, 1024**2)
    solver.delete()

# A tiny proof-export regression check precedes the identical-formula replay.
# This toy is not a cap-search instance.
toy_cnf = OUT / 'export_regression.cnf'
toy_proof = OUT / 'export_regression.drat.bin'
toy_cnf.write_text('p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n')
toy = Cadical195(with_proof=True)
for clause in ([1, 2], [1, -2], [-1, 2], [-1, -2]):
    toy.add_clause(clause)
assert toy.solve() is False
flush_then_capture(toy, toy_proof)
toy_parse = complete_binary(toy_proof)
toy_check = subprocess.run([str(CHECKER), str(toy_cnf), str(toy_proof), '-i'],
                           capture_output=True, text=True, timeout=10)
(OUT / 'export_regression_check.log').write_text(toy_check.stdout + toy_check.stderr)
assert toy_check.returncode == 0 and 's VERIFIED' in toy_check.stdout

assert sha(CNF) == EXPECTED
started = time.monotonic()
solver = Cadical195(use_timer=True, with_proof=True)
solver.configure({'seed': 0})
with CNF.open() as stream:
    for line in stream:
        if line[0] in 'cp':
            continue
        clause = list(map(int, line.split()))
        assert clause.pop() == 0
        solver.add_clause(clause)
result = solver.solve()  # Exactly one replay of the unchanged cap formula.
stats = solver.accum_stats()
assert result is False, 'Unexpected result: retain artifacts without promotion'
proof = OUT / 'complete_solver_proof.drat.bin'
flush_then_capture(solver, proof)
parsed = complete_binary(proof)
assert parsed['empty_additions'] > 0
report = dict(status='REPLAYED_UNSAT_AWAITING_INDEPENDENT_PROOF_CHECK',
              purpose='Repair truncated proof export; identical immutable CNF and seed',
              cnf_sha256=EXPECTED, solver='Cadical195', seed=0,
              additional_cap_formula_decision_calls=1,
              toy_export_regression_decision_calls=1,
              native_c_stdio_flushed_before_read=True,
              solver_stats=stats, proof_sha256=sha(proof), proof_parse=parsed,
              toy_proof_parse=toy_parse, toy_independent_check_passed=True,
              replay_elapsed_seconds=time.monotonic()-started,
              cpu_limit_seconds=60, wall_limit_seconds=90,
              address_space_limit_bytes=4*1024**3)
(OUT / 'replay_report.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2), flush=True)
