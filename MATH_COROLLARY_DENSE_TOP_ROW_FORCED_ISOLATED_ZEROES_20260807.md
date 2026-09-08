# Johnson-adjacent dense top owners force exactly \(d\) isolated target zeroes per endpoint

**Date:** 2026-08-07  
**Parent theorem:**
`MATH_THEOREM_DENSE_TOP_ROW_DELAYED_ATOM_BLOCK_QUEUE_NORMAL_FORM_20260807.md`  
**Status:** unconditional sharp local obstruction.  A dense top row may
have the positive residence needed for delayed-atom reconstruction, and
its source/owner chronology may be bi-resident, but the top-target
membership words themselves can never be bi-resident when \(d\ge2\).

## 1. Exact isolated-zero identity

Let

\[
 S_e\in{[n]\choose m-d-1}
 \qquad(e\in\mathbb Z_L)
\tag{1.1}
\]

and put

\[
 O_e=S_{e-1}\cup S_e.
\tag{1.2}
\]

Assume every \(O_e\) has rank \(m\) and consecutive owners are distinct
Johnson neighbours.  Equivalently, with

\[
 L_e=S_{e-1}\setminus S_e,
 \qquad
 R_e=S_{e+1}\setminus S_e,
\tag{1.3}
\]

the dense top-row normal form gives

\[
 |L_e|=|R_e|=d+1,
 \qquad
 |L_e\cap R_e|=d.
\tag{1.4}
\]

### Theorem 1.1 (forced isolated zeroes)

For every endpoint \(e\), exactly \(d\) coordinates have membership
pattern

\[
 \boxed{
 {\mathbf 1}_{x\in S_{e-1}},
 {\mathbf 1}_{x\in S_e},
 {\mathbf 1}_{x\in S_{e+1}}
 =1,0,1.}
\tag{1.5}
\]

They are precisely the coordinates in

\[
 C_e:=(S_{e-1}\setminus S_e)
       \cap(S_{e+1}\setminus S_e),
 \qquad |C_e|=d.
\tag{1.6}
\]

Consequently the cyclic top-target membership words contain exactly
\(dL\) isolated-zero occurrences, counted by their zero positions.  In
particular, for \(d\ge2\) the top-target sequence is not bi-resident to
depth \(d\).

#### Proof

A coordinate has the pattern (1.5) at \(e\) if and only if it lies in
both differences in (1.3), namely if and only if it lies in \(C_e\).
Equation (1.4) gives \(|C_e|=d\).  Each cyclic zero-run of length one has
a unique zero position, so summing over \(e\) counts every isolated-zero
run once and gives \(dL\).  A depth-\(d\) negative-residence condition
would require every zero-run to have length at least \(d\), which is
impossible when \(d\ge2\). \(\square\)

This is not merely an artefact of the explicit block queue.  It follows
from the two target ranks, owner rank, and owner Johnson adjacency alone.

## 2. Why there is no conflict with the positive construction

The delayed-intersection reconstruction

\[
 B_p=\bigcap_{j=0}^{d-1}S_{p+j},
 \qquad
 S_e=\bigcup_{p=e-d+1}^{e}B_p
\tag{2.1}
\]

requires exactly that every **positive** target run have length at least
\(d\).  It imposes no lower bound on zero-runs.  Thus Theorem 1.1 does not
conflict with literal common history.

Likewise, residence is attached to different membership words at the
other interfaces:

* source-letter residence concerns the antecedent word \((B_p)\), not the
  target word \((S_e)\);
* owner residence concerns \((O_e)\); and
* target positive residence concerns \((S_e)\) and is the one-sided
  condition used by the top-row reconstruction theorem.

For the weight-\((d+1)\) block queue, the target words have the forced
isolated zeroes of Theorem 1.1 and positive runs of length at least \(d\),
while every noncore owner coordinate has a gap of length \(d+1\) and a
positive run of length \((d+1)^2\).  Hence the owner sequence is genuinely
bi-resident.  There is no contradiction because the two residence claims
refer to different rows.

## 3. Consequence for the adaptive merged-chart gate

The explicit top-row common-history theorem
`MATH_THEOREM_PBBS_SCD_COMMON_HISTORY_TOP_ROW_RESIDENCE_AND_RANDOM_BTK_NOGO_20260807.md`
uses only positive runs of the rank-\((t-1)\) target words.  The moving-bank
carousel note likewise identifies positive-run residence as the exact
condition needed for the odd depth-\(d\) literal antecedent.  Therefore the
forced one-zero runs do not obstruct that stated top-row gate.

The phrase “all residence rows” in a later global chart theorem must,
however, keep the row labels explicit.  If it were strengthened to demand
negative depth-\(d\) residence of the same dense target sequence, then
Theorem 1.1 would be an immediate no-go.  Any downstream construction that
needs complementary or two-sided residence must instead obtain it from a
separate dual chronology, from the owner row, or from an additional lift;
it cannot be imposed on these \(S_e\)'s while retaining rank-\(m\)
Johnson-adjacent central owners.

Thus the exact scope is:

\[
\boxed{
 \text{dense top normal form}
 \Longrightarrow
 \text{positive target residence is possible, negative target residence is impossible,}
}
\tag{3.1}
\]

while source or owner biresidence remains independently possible.
