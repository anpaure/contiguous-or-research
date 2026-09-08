# Exact endpoint-alignment cuts for the unrestricted `k=11,n=465` forest

## Status

This note turns the inherited multi-rank endpoint-intersection counts into two
concrete central-schedule cuts.  They are globally WLOG and do not assume a
fixed derivative row or a connected central path.  They are not yet
implemented in `k11_forest_sat.cpp`.

At each of the two endpoint colours, every genuine length-465 solution has:

```text
at least 324 aligned endpoints with rank5 width>=1 and rank6 width>=2;
at least  24 aligned endpoints with rank5 width=2  and rank6 width=3.
```

Here width is physical interval length minus one.

## 1. Three-rank intersection

Choose one witness for every mask in ranks four, five, and six.  Within each
rank the selected left endpoints are distinct.  Their endpoint-set sizes are

\[
 {11\choose4}=330,
 \qquad {11\choose5}={11\choose6}=462.
\]

All lie in 465 physical positions, so

\[
 |L_4\cap L_5\cap L_6|
 \ge330+462+462-2\cdot465=324.                    \tag{1}
\]

At such a common left endpoint the three intervals are strictly nested in
rank order.  Hence their widths satisfy

\[
 w_4<w_5<w_6.
\]

Every selected rank-six witness has width at most three.  Therefore

\[
 w_5\ge1,
 \qquad w_6\ge2.                                  \tag{2}
\]

The same inclusion-exclusion and nesting argument applies to right endpoints.
This proves the 324 alignment cut in both endpoint colours.

## 2. Four-rank intersection

Add the 165 selected rank-three witnesses.  Four-set inclusion-exclusion gives

\[
 |L_3\cap L_4\cap L_5\cap L_6|
 \ge165+330+462+462-3\cdot465=24.                 \tag{3}
\]

At a common endpoint there are four nonempty intervals with strictly
increasing ranks and therefore strictly increasing widths.  Since the largest
width is at most three, the widths are forced exactly:

\[
 (w_3,w_4,w_5,w_6)=(0,1,2,3).                    \tag{4}
\]

Thus at least 24 physical left endpoints align a rank-five width-two witness
with a rank-six width-three witness.  The dual right-endpoint statement is
identical.

Equations (1)--(4) hold for arbitrary witness choices.  In particular, the
rank-three and rank-four schedules need not be represented explicitly in the
SAT model: their existence forces a property solely of the already-selected
rank-five and rank-six schedules.

## 3. Compact guarded encoding

The adjacent-shadow guard already defines exact rank-six summaries by
physical endpoint and width.  Add the analogous rank-five summaries only for
the needed width classes:

```text
L5pos[p] iff a selected rank-five interval starts at p with width 1 or 2,
R5pos[p] iff a selected rank-five interval ends   at p with width 1 or 2,
L52[p]   iff a selected rank-five interval starts at p with width 2,
R52[p]   iff a selected rank-five interval ends   at p with width 2.
```

Each is a bidirectional disjunction of the existing rank-five state literals;
endpoint injectivity makes the definition exact.

For every physical endpoint define conjunctions

```text
ZL324[p] = L5pos[p] AND (B6[p,2] OR B6[p,3]),
ZR324[p] = R5pos[p] AND (E6[p,2] OR E6[p,3]),

ZL24[p]  = L52[p] AND B6[p,3],
ZR24[p]  = R52[p] AND E6[p,3].
```

Then add exact cardinality cuts

```text
sum_p ZL324[p] >= 324,
sum_p ZR324[p] >= 324,
sum_p ZL24[p]  >= 24,
sum_p ZR24[p]  >= 24.
```

Binary population counters need only nine bits and can share the exact
increment template specified in
`K11_FOREST_JOINT_SHORT_CIRCUIT_DESIGN.md`.  Alternatively, because the
endpoint schedule has only three omissions, a specialized boundary/omission
circuit may be still smaller.  Either implementation must be guarded and
independently truth-table checked before deployment.

## 4. Exactness and scope

Soundness of the surrounding forest formula is unchanged: the new clauses
only constrain already-selected schedule states.  Completeness follows from
the arbitrary-witness endpoint theorems (1) and (3), so no genuine optimum is
removed.

These cuts do not prove SAT or UNSAT.  They expose multi-rank nesting directly
to propagation.  Any SAT candidate still requires both OR verifiers, and any
UNSAT result still requires an archived CNF/proof pair and independent proof
checking.
