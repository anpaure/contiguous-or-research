# Independent audit: twisted four-run `C8` unit pump

**Date:** 2026-08-02  
**Verdict:** `PASS` for the theorem's literal packet scope.

**Minimality correction:** the audited `C8` remains valid, but the
phase-split three-run quotient construction gives a smaller `C6` with the
same `+/-1` conclusion.  This audit makes no `C6` no-go or first-actuator
claim.  See `MATH_AUDIT_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_20260802.md`.

## 1. Independently checked identities

The audit reconstructs the packet only from `d` and the nonnegative slack
`s`.  It does not read a stored word or a theorem-side table.

For

\[
 h=d+1,quad r=4h+1+s,quad n=2r-1,
\]

it verifies:

1. the four alternating one/zero block pairs have total lengths `r,r-1`;
2. the four run-start-to-run-end swaps send `A` exactly to `tau A`;
3. all `4n` developed rank-`r` roots are distinct;
4. every consecutive pair is a Johnson edge, including the developed
   closing edge;
5. all `4n` physical lower intersections are distinct;
6. all `4n` physical upper unions are distinct;
7. every coordinate has exactly eight cyclic trace changes;
8. minimum zero and one run lengths exceed the depth-`d` threshold; and
9. complete reversal has exactly the same lower/upper occurrence counters.

The voltage is read from the literal lift: three quotient edges end in
their chosen representatives and the fourth ends at `tau R_0`.  Hence it is
`+1`; reversal is `-1`.  This is valid for composite odd `n` because
`gcd(n,1)=1`.

## 2. Replay

Run:

```text
python3 scratch/audit_k_twisted_four_run_c8_unit_pump_20260802.py
```

Frozen output:

```text
PASS_TWISTED_FOUR_RUN_C8 cases= 48
formula n=8(d+1)+1+2*slack; voltage=+1 reverse=-1
last (12, 8, 121, 61, [51, 52])
```

The 48 cases are `1<=d<=12` crossed with slack values `0,1,3,8`.  The last
tuple is `(d,slack,n,r,[minimum-zero-run,minimum-one-run])`.

## 3. Scope audit

The replay authenticates occurrence-labelled roots and immediate palettes,
not only quotient orbit counts.  Cutting one physical closing edge is then
safe for internal history because every newly shortened run meets an
endpoint.

It does not test or assert an ambient owner-factor extension, an exterior
history socket, source factorization, upper ranks beyond edge unions,
exterior cross-windows, or compiler/common-cap matching.  The atomic
`(z,b)=(0,0)` cap statement uses the simultaneous alternating-circuit
semantics; a fictional serial deletion-before-addition ordering is not part
of the packet.
