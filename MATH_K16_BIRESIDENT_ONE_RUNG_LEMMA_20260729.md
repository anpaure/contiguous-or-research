# The bi-resident one-rung lemma

This note records a sufficient (k=15\to16) construction that is much
smaller than the general dual-rail cut/rung master.  The statement is given
for every odd parent size.

Let (k=2m+1), (r=m+1), and let

\[
F=(F_0,F_1,\ldots,F_{W-1}),\qquad W=\binom{k}{r},
\]

be a Hamilton cycle of (J(k,r)).  Put

\[
\lambda_i=F_i\cap F_{i+1},\qquad U_i=F_i\cup F_{i+1},
\]

with cyclic indices.  Assume:

1. the \(\lambda_i\) enumerate \(\binom{[k]}{r-1}\) exactly;
2. the \(U_i\) cover \(\binom{[k]}{r+1}\);
3. for every old coordinate, both its cyclic 1-runs and 0-runs in \(F\)
   have length at least \(d(k+1)+1\).

Introduce a new point (z).  The two middle-layer rails of
(J(k+1,r)) are

\[
A_i=F_i,\qquad B_i=\{z\}\cup\overline{F_i},
\]

where the complement is inside ([k]).

## Colour-aware square

Choose an A-edge (e), a B-edge indexed by (f), and orientations of
their endpoints so that

\[
R:=\lambda_e\in\{\overline{F_f},\overline{F_{f+1}}\},
\qquad
P:=\overline{\lambda_f}\in\{F_e,F_{e+1}\}.
\]

Then (R\subset P), so

\[
P\longleftrightarrow \{z\}\cup R
\]

is a Johnson edge.  Delete (A_eA_{e+1}) and (B_eB_{e+1}) (with the
second index understood as (f)), orient the resulting A path to end at
(P), orient the resulting B path to start at \(\{z\}\cup R\), and join
them by this one rung.  Two cycles lost two edges and gained one, hence the
result is a Hamilton path through all \(\binom{k+1}{r}\) child middle sets.

## Exact palette calculation

The four child (q=1) palettes split according to the presence of (z).

* A-intersections are the \(\lambda_i\).  Deleting (e) loses
  \(\lambda_e\), and the rung restores exactly (R=\lambda_e\).
* B-unions are \(\{z\}\cup\overline{\lambda_i}\).  Deleting (f) loses
  \(\{z\}\cup\overline{\lambda_f}\), and the rung restores exactly
  \(\{z\}\cup P\).
* A-unions are the \(U_i\).  Therefore (U_e) must have another A
  provider.
* B-intersections are \(\{z\}\cup\overline{U_i}\).  Therefore (U_f)
  must have another B provider.

Consequently both child (q=1) palettes are complete whenever

\[
\mu_U(U_e)\ge2,\qquad \mu_U(U_f)\ge2.
\]

This is an exact calculation, not a heuristic.

## Residence collar

All internal runs away from the rung are inherited from a cyclic 1-run or
0-run of (F), and are safe by bi-residence.  The only new condition is at
the rung.  For every old coordinate (x), let (a_x) be the terminal
1-run length at the oriented A endpoint and (b_x) the initial 1-run
length at the oriented B endpoint.  The necessary and sufficient seam
condition is

\[
a_x+b_x\in\{0\}\cup[d(k+1)+1,\infty).
\]

The new coordinate (z) is absent on the entire A rail and present on the
entire B rail; its only 1-run reaches the right boundary and is therefore
free in the linear carrier.

Thus a colour-aware square satisfying the two duplicate rows and this
finite collar test produces a fully resident, both-(q=1)-complete child
carrier.  No 77,000-variable master is needed for those three carrier
gates.  This does not settle q2 or deeper upper support, the singleton-`z`
compiler port, or unrestricted `COMP_3`; those remain separate checks.

## Executable certificate

[`scratch/audit_k16_biresident_one_rung_splice_20260729.py`](scratch/audit_k16_biresident_one_rung_splice_20260729.py)
independently verifies all parent hypotheses, enumerates every such square,
constructs each child path, and exhaustively checks the child middle layer,
Johnson adjacency, both (q=1) palettes, and residence.  It emits a child
carrier only after every check passes.

This lemma does **not** prove that every bi-resident parent has a safe
square.  That is now a small finite gate: at (k=15), a future birail PASS
can be screened immediately before invoking any general master.

The exact square normal form, the reduction from fifteen collar rows to
six, the coordinatewise `11110000` obstruction to automatic seam safety,
and the necessary-and-sufficient fixed-candidate theorem are proved in
`THREAD_A_K16_ONE_RUNG_SQUARE_CORNER_SPLICE_THEOREM_20260729.md`.

## Implementation warning found during the audit

The first version of Claude's `dualrail.py` used (c_A,c_B) in its
subtour boundary row even though (c=1) means that the rail edge is cut.
For a current component those crossing cut variables are already 1, so the
row was vacuous.  The sound row uses retained indicators (1-c_A,1-c_B)
plus outward rung variables.  The implementation was patched on
2026-07-29 and also given independent input/output gate audits.  No earlier
PASS depended on the bug because no dualrail PASS had yet occurred.
