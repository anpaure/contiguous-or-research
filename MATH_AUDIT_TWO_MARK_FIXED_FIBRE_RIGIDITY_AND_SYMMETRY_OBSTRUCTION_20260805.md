# Audit: two-mark fixed-fibre rigidity and symmetry obstruction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_TWO_MARK_FIXED_FIBRE_RIGIDITY_AND_SYMMETRY_OBSTRUCTION_20260805.md`  
**Method:** independent line-by-line symbolic audit; no computation or search  
**Verdict:** **PASS**, with the scope restrictions listed in Section 6.

## 1. FIFO formula audit

The synchronized-chain normal form gives

\[
 T_j=C\cup A\cup\{x_{j+1},\ldots,x_d\}
                 \cup\{b_1,\ldots,b_j\}.
\]

At `j=2` this is exactly

\[
 T_2=C\cup A\cup\{x_3,\ldots,x_d\}\cup\{b_1,b_2\}.
\]

The four endpoint role sets are pairwise disjoint.  Therefore
`T_2 cap B={b_1,b_2}`, and fixing `(mathfrak F,T_2,b_2)` fixes `b_1`.
This proves the main rigidity identity without a hidden genericity
assumption.

The punctured duplicate lift uses only `d-1` ordinary `b` labels and then a
private terminal label.  For `d>=3`, its first two levels have the same
formula, so the asymptotic application is unchanged.

## 2. Generator-invariant audit

Both generators in the cited synchronized-chain theorem are internal to one
graph `Z_d(X,B)`:

* a vertex splice exchanges suffixes of paths with the same endpoint fibre;
* a rank-cycle switch replaces layer edges but leaves `C,A,X,B` fixed.

Hence neither changes `B`, and the formula

\[
 b_1=((T_2\cap B)-\{b_2\})
\]

remains valid after every generator.  The theorem does not accidentally use
connectivity across different endpoint fibres.

The stronger owner-load-one claim is also correct: every path in the fibre
uses the same bottom and top vertices of `Z_d`, whose owner images are the
same two rank-`r` owners.  Two such paths cannot coexist in an
owner-bijective chronology.

## 3. Group-symmetry audit

The stabilizer of a fixed rank-`r` set `T` and a fixed member `b_2` contains
the full symmetric group on `T-{b_2}`.  It is transitive there.  For an
`S_k`-invariant construction law, all `r-1` conditional mark probabilities
are therefore equal, and their sum is one.  The displayed one-point law is
exact.

Conditioning on concrete owner banks is a genuine change of sigma-field.
The remaining stabilizer is the intersection with the bank stabilizer; no
transitivity follows.  Thus the source correctly avoids claiming a
bank-conditioned consequence.

## 4. Diagonal-coupling audit

Take

\[
 T_x=A+x,\ b_2^x=x,\qquad T_y=A+y,\ b_2^y=y,
\]

where `|A|=r-1`.  Both candidate sets are exactly `A`.  If one uniform
`Z in A` supplies both second marks, then each marginal is uniform, while

\[
 \Pr(b_1^x=z,b_1^y=z)=1/(r-1).
\]

The product target is `1/(r-1)^2`; the ratio is exactly `r-1`.  The two
owners are distinct.  Repetition of a coordinate mark across tasks is not
forbidden by the FIFO owner rules.  Hence this is a valid logical
counterexample to deriving the joint cylinder from one-point symmetry.

The example is used only as a probability-law obstruction; the source does
not claim that this isolated coupling has already been embedded in a full
owner-Hamilton construction.

## 5. Cylinder disintegration audit

For one-mark state `s`, fixed-fibre rigidity makes `b_1=phi_s(F_s)`.
For distinct states `s_i`,

\[
 \Pr(\hbox{all prescribed triples}\mid B_0,B_1)
 =\Pr(\hbox{all }s_i\mid B_0,B_1)
  \Pr(\phi_{s_i}(F_{s_i})=z_i\ \forall i
       \mid \hbox{all }s_i,B_0,B_1).
\]

Multiplying the one-mark cylinder

\[
 \left((1+o(1))H/(Wr)\right)^m
\]

by `(r-1)^(-m)` gives precisely

\[
 \left((1+o(1))H/(W(r)_2)\right)^m.
\]

Thus the proposed endpoint-kernel bound is an exact sufficient upgrade.
It is not asserted to be logically necessary when the one-mark event has
additional slack, and the theorem's wording is appropriately limited to the
factor needed to upgrade the existing bound at its stated scale.

## 6. Scope exclusions

The theorem proves none of the following:

1. nonexistence of a pre-reserved two-mark spread SDR;
2. nonexistence of endpoint-changing FIFO absorbers;
3. failure of a joint construction which selects endpoint fibres and owner
   SDRs simultaneously;
4. failure of an unconditioned two-mark cylinder under some stronger random
   construction law; or
5. a lower bound on the final OR-word length.

It proves only the sharp route obstruction:

\[
 \text{fixed-endpoint chain switches + one-point symmetry}
 \quad\not\Rightarrow\quad\text{bank-conditioned (C2)}.
\]

That conclusion is fully supported by the audited identities.
