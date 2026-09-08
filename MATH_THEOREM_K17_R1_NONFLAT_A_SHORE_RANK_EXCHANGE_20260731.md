# The improved r1 parent under the nonflat owner/cofacet zipper

Date: 2026-07-31  
Status: exact local theorem and literal audit; no global K17 word claimed

## 0. Verdict

The nonflat owner/cofacet zipper applies cleanly to the newly frozen `r1`
`K15 -> K17` child, but it exposes an important distinction which is hidden
by the occurrence-independent parent census.

* The `135` packets forced by unique rank-six colours lie in exactly `105`
  residual macros.  Their exact four-edge actuator number is also `105`, one
  internal actuator in each selected macro.  Advancing those macros has
  independent blockwise phase debt

  \[
                         105-1=104.
  \]

  This is a strict improvement over the old parent's `108` modules and debt
  `107`.

* The exact minimum occurrence transversal has `150` surviving packets.
  Those packets lie in `119` macros, and their exact actuator number is
  `119`, again one internal actuator per macro.  The corresponding independent
  phase debt is

  \[
                         119-1=118.
  \]

  Thus the `15` cross-coordinate packets add `14` new modules.  For the
  **actual frozen occurrence choice**, r1 is eleven phase units worse than the
  old forced-bank benchmark `107`, despite being three units better on the
  occurrence-independent forced bank.

All selected lower-facet and upper-cofacet palettes are literal and simple:

| bank | A owners | lower facets | distinct lower | internal cofacets | distinct upper |
|---|---:|---:|---:|---:|---:|
| 135 forced packets | 1111 | 1216 | 1216 | 1006 | 1006 |
| 150 exact survivors | 1237 | 1356 | 1356 | 1118 | 1118 |

Every local mixed module passes the depth-two and depth-three strict internal
residence tests, and every source `0,111,0` packet is replayed as four
consecutive positive cofacet outputs.

Consequently, r1 supplies a smaller **unavoidable** phase-sharing instance,
but not a smaller **complete** instance once the integral occurrence tax is
included.  This is direct evidence that the general construction must choose
the occurrence transversal and the phase-sharing/zipper modules jointly;
optimizing their marginal counts in sequence is not sound.

## 1. Literal zipper identity

In one selected residual macro let

\[
                    V_0,V_1,\ldots,V_{q-1}
\]

be its consecutive A-shore rank-nine owners, and let `L,R` be the two incident
rank-eight seam facets.  The mixed depth-two module is

\[
                    L,V_0,V_1,\ldots,V_{q-1},R.
\]

Its derivative is exactly

\[
 V_0,\;V_0\cup V_1,\;\ldots,\;V_{q-2}\cup V_{q-1},\;V_{q-1}.
\]

Hence an internal A-shore coordinate trace `0,1,1,1,0` becomes four positive
rank-ten outputs.  The audit checks this identity from the literal `r1` flow
and child cycle for all `135` forced packets and all `150` packets in the
minimum occurrence witness.

## 2. Exact bank arithmetic

For the forced bank the componentwise packet/actuator counts are

\[
 (75,45,15,0)\quad\hbox{packets},\qquad
 (45,45,15,0)\quad\hbox{actuators}.
\]

The selected-macro packet profile is

\[
                         1^{90}3^{15}.
\]

For the exact survivor bank they are

\[
 (90,45,15,0)\quad\hbox{packets},\qquad
 (59,45,15,0)\quad\hbox{actuators},
\]

with selected-macro packet profile

\[
                         1^{103}2^1 3^{15}.
\]

For proper circular four-edge packets the usual anchor-and-right-endpoint
greedy algorithm is exact: some point of the first interval belongs to an
optimum; after conditioning on that point, the remaining circular intervals
become ordinary intervals and greedy by right endpoint is optimal.  The
script applies this proof componentwise.  In both banks every chosen actuator
is internal to one macro, the actuator macros equal the packet macros, and
each selected macro receives exactly one actuator.

## 3. What this proves and what it does not

It proves:

1. the exact local rank exchange on the improved r1 parent;
2. exact actuator minima `105` and `119` for the two stated banks;
3. exact selected macro counts and literal simple lower/upper palettes;
4. zero local depth-two/depth-three residence defect; and
5. phase debts `104` and `118` under independent blockwise installation.

It does **not** prove that the modules can share phases globally, that their
palettes remain complete after insertion in one chronology, that a common-cap
compiler exists, or that a `K17` word exists.  Coupled phase sharing could be
strictly cheaper than the independent debt.  Conversely, the local audit
does not erase the thousands of nonlocal upper/deeper-shadow defects of the
raw r1 carrier.

## 4. Frozen artifacts

Audit program:

```text
scratch/audit_k17_r1_nonflat_a_shore_rank_exchange_20260731.py
SHA-256 606444fb8e131857a78ed5c6a6f96fcc803b5e4f6f2166d7af0cc8fd9d916e92
```

Audit result:

```text
scratch/k17_r1_nonflat_a_shore_rank_exchange_20260731.audit.json
SHA-256 eb004c29c2504a5244a3e286a01babae94ee730be97839072cae72b703888ba8
```

The result records hashes of the r1 parent, exact occurrence witness, r1 flow,
and literal K17 cycle, as well as every module row and selected macro id.
