# Certified improvement: `nu(14) <= 3675`

Date: 2026-07-27

The file

`scratch/k14_completed_3675_newprefix.word`

contains 3,675 nonzero masks on 14 coordinates.  Every one of the 16,383
nonzero masks occurs as the bitwise OR of a contiguous interval.  Therefore

\[
                         \boxed{\nu(14)\le 3675}.
\]

Together with the rank-count lower bound, the current certified range is

\[
                         \boxed{3434\le\nu(14)\le3675}.
\]

## Construction provenance

The 3,434-entry prefix is the compiler-in-the-loop central-path certificate

`scratch/k14_compilable_descent.word`

with SHA-256

`5f49ac3cb0e136e0e41f826a930caf8f48e27a82a4294989e5fc0603b4399ff7`.

It misses 251 masks: 229 of rank 9 and 22 of rank 10.  Starting from the old
242-entry suffix `k14_append_242.txt`, replace its 45th entry (one-based)
`13283` by `9211`, then delete its 103rd entry `10172`.  The resulting suffix
has length 241, giving total length `3434+241=3675`.

## Independent verification

Run

```text
python3 scratch/verify_k14_completed_3675.py
```

The verifier checks the certificate SHA-256, entry range, length, exhaustive
coverage, and then recomputes one stored interval witness for every nonzero
14-bit mask.  Expected output:

```text
PASS k=14 length=3675 covered=16383/16383 sha256=ee5722d7a4f0bc04e953ad397ad3cb0d16ca69b0572094e5b38b9a1e347bccc7
```

The full-word SHA-256 is

`ee5722d7a4f0bc04e953ad397ad3cb0d16ca69b0572094e5b38b9a1e347bccc7`.

An independently found ordering of the same one-deletion/one-replacement
repair is stored as `scratch/k14_complete_3675_oneedit.word`, SHA-256
`cc9a41fb9a732900186c28e6c0a5dfba8a18ca5108c6a18c6739ff37c0e9167f`.
Its 241-entry suffix is
`scratch/k14_compilable_append241_oneedit.txt`, SHA-256
`babf0c6442c7344c88eaa8a78fd93036c97d44a54e3850e0f346511cb0bccfc6`.
Independent C++ exhaustive verifiers also report 16,383/16,383 coverage for
that certificate.
