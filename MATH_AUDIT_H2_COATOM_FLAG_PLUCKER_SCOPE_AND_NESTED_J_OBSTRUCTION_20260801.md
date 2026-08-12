# Referee audit: the coatom Pluecker lattice is signed and marginal; nested flags retain a first bidegree invariant

Date: 2026-08-01  
Status: independent proof audit and exact scoped obstruction.  No global
safe-carrier reachability or compiler theorem is claimed.

## 0. Verdict

The integer-generation claims in
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
are correct in their stated marginal, signed scope.

At depth two the packet action is exactly

\[
 [Haf_1]+[Hbf_d]-[Hbf_1]-[Haf_d],                 \tag{0.1}
\]

and all relabellings give every short Pluecker square.  These squares
generate the full integer kernel of the point-degree map.  This does not
make them a nonnegative Markov basis.

Nor does the maximal-chain theorem make the coupled packet actions a
Markov basis.  Even on marginal occurrence vectors, reflected depths retain
a quadratic pair-degree difference.  On occurrence-coupled nested flag
tables there is a still finer conditioned terminal-degree invariant, already
at depth three, which is not visible in any separate depth marginal.  Varying
the filler permutation changes which conditioned block is acted on; it does
not mix the blocks.  The finer invariant disappears only after one
deliberately forgets, or freely re-pairs, the incidence between consecutive
depths.

## 1. Exact action

With `n=d+2`, write

\[
 P_q=\{f_1,\ldots,f_{n-q-1}\},\qquad
 S_q=\{f_q,\ldots,f_{n-2}\}.
\]

After removing the common set `G=K+{infinity,c}`, the old-to-new action is

\[
 (P_q+b)+(S_q+a)\longmapsto(P_q+a)+(S_q+b).       \tag{1.1}
\]

At `q=2`, `P_2-S_2={f_1}` and `S_2-P_2={f_d}`.  Hence (1.1) is (0.1),
with

\[
 H=G+\{f_2,\ldots,f_{d-1}\}.
\]

For `r>=d+4` this uses an arbitrary common `(r-4)`-set.  Four further
coordinates, namely the two unused active labels and the two endpoint
fillers, are needed outside the square.  Thus the literal realization of
every square has the exact ambient condition `|Omega|-r>=4`.

## 2. Why the signed depth-two lattice is complete

Let `partial_s` be the point-incidence map on rank-`s` sets.  A standard
binary-matrix alternating-cycle argument generates `ker_Z(partial_s)` by
the general symmetric exchanges

\[
 [P+x]+[Q+y]-[P+y]-[Q+x].                            \tag{2.1}
\]

Choose a path `P=P_0,...,P_l=Q` in the Johnson graph on the
`(s-1)`-sets avoiding `x,y`.  Then

\[
 \rho(P,Q;x,y)=\sum_i\rho(P_i,P_{i+1};x,y).          \tag{2.2}
\]

Every summand in (2.2) is a short square with a common `(s-2)`-core, hence
is a relabelled copy of (0.1).  This proves equality over the integers.
It also independently explains why no lattice-index or congruence
qualification is needed.

The proof is signed.  The telescoping intermediates need not be present in
a nonnegative table.

### 2.1 The first marginal all-depth invariant

For an occurrence vector `mu_q` on depth `q`, put

\[
 D_q^{(2)}(x,y)=\sum_{R\supseteq\{x,y\}}\mu_q(R).
\]

If `t=d+1-q`, the only nonzero pair changes in (1.1) are

\[
 \Delta D_q^{(2)}(a,f_i)
  =1_{i\le t}-1_{i>d-t},
 \qquad
 \Delta D_q^{(2)}(b,f_i)=-\Delta D_q^{(2)}(a,f_i).
\]

Replacing `q` by `d+2-q` replaces `t` by `d-t` and leaves this expression
unchanged.  Hence every serial walk preserves

\[
 D_q^{(2)}(x,y)-D_{d+2-q}^{(2)}(x,y).               \tag{2.3}
\]

This independently verifies the reflected-pair theorem in
`MATH_THEOREM_COATOM_NESTED_FLAG_PLUCKER_AND_REFLECTION_INVARIANT_20260801.md`.
It is the first extra additive invariant on the marginal all-depth state:
the depth-two Pluecker theorem does not remove correlations forced between
different depths.

## 3. The first nested invariant

Let a depth-`d` flag be

\[
 T_2\supset T_3\supset\cdots\supset T_d,
 \qquad |T_q-T_{q+1}|=1.
\]

Its deletion word is

\[
 w(T)=(x_2,\ldots,x_{d-1}),\qquad
 \{x_q\}=T_q-T_{q+1}.                                \tag{3.1}
\]

For the packet's prefix and suffix flags the two words are reversals:

\[
 (f_{d-1},\ldots,f_2),\qquad(f_2,\ldots,f_{d-1}).    \tag{3.2}
\]

Consequently, for a reversal class `[w]={w,w^rev}`, every coupled packet
preserves

\[
 J_{[w],i}(z)=
 \sum_{T:\,[w(T)]=[w]}z_T\,1_{\{i\in T_d\}}.        \tag{3.3}
\]

Indeed, (1.1) exchanges `a,b` between the two terminal profiles in the
same reversal class, so their combined incidence vector is unchanged.

At `d=3`, both flags delete the same central filler `x=f_2`.  Formula
(3.3) becomes the particularly transparent bidegree

\[
 J_{x,i}(z)=\sum_{T:T_2-T_3=\{x\}}z_T,1_{\{i\in T_3\}}. \tag{3.4}
\]

Separate coordinate degrees determine only the deletion marginal

\[
 \mu_x=D_{2,x}-D_{3,x},\qquad
 \sum_i J_{x,i}=|T_3|\mu_x,                         \tag{3.5}
\]

not the individual entries of (3.4).

At this depth the marginal reflected-pair invariant is exactly the
symmetrization

\[
 D_2^{(2)}(x,i)-D_3^{(2)}(x,i)=J_{x,i}+J_{i,x}.       \tag{3.6}
\]

Thus (3.4) also retains the directed/antisymmetric information which every
separate-depth occurrence vector forgets.

## 4. Minimal two-flag obstruction

Let `C` be any common three-set.  Consider the two tables

\[
\begin{array}{c|cc}
 &\text{first flag}&\text{second flag}\\ \hline
X&C12\supset C1&C34\supset C3\\
Y&C14\supset C1&C23\supset C3.
\end{array}                                           \tag{4.1}
\]

Both have the same rank-five coordinate degrees at depth two and the same
rank-four coordinate degrees at depth three.  Their deletion marginals are
also the same: one deletion of `2` and one deletion of `4`.  But

\[
\begin{aligned}
X:&\quad J_{2,1}=J_{4,3}=1,\\
Y:&\quad J_{4,1}=J_{2,3}=1.
\end{aligned}                                         \tag{4.2}
\]

Thus they cannot be joined even in the signed lattice of coupled nested
packet actions.  Removing the common suspension gives the smallest abstract
example, on four points with two flags of ranks `2 -> 1`.  One flag cannot
give a counterexample because its two degree rows recover the flag; hence
mass two is minimal.

The conditioned invariant is genuinely finer than all marginal occurrence
vectors, not merely finer than coordinate degrees.  On the same common
suspension, compare the two directed three-cycles

\[
\begin{aligned}
X'&=\{C12\supset C2,\ C23\supset C3,\ C13\supset C1\},\\
Y'&=\{C12\supset C1,\ C23\supset C2,\ C13\supset C3\}.
\end{aligned}                                        \tag{4.3}
\]

Their complete depth-two multisets are both `{C12,C23,C13}`, and their
complete depth-three multisets are both `{C1,C2,C3}`.  Thus every marginal
invariant, including (2.3), agrees.  But their nonzero conditioned entries
are respectively

\[
 (J_{1,2},J_{2,3},J_{3,1})=(1,1,1),\qquad
 (J_{2,1},J_{3,2},J_{1,3})=(1,1,1).                 \tag{4.4}
\]

They are distinct flag tables and cannot be connected.  Three flags are
minimal once the entire pair of depth marginals is fixed: a nontrivial
re-pairing cycle in a bipartite incidence table has length at least three
(a two-cycle only exchanges two identical flag records).

There is also a purely nonnegative obstruction after forgetting nesting.
For rank `s>=3`, let `C` have size `s-3`.  The two tables

\[
 [C123]+[C456],\qquad [C124]+[C356]                  \tag{4.5}
\]

have the same point degrees.  Each supported pair intersects in only
`s-3`, whereas a positive short square requires intersection `s-2`.
Hence both are isolated under positive coatom-square moves.  This is the
smallest mass-two signed-versus-Markov separation.

## 5. Exact scope reconciliation

The maximal-chain theorem works in

\[
 \bigoplus_{t=1}^{d-1}\mathbb Z^{\binom Ft},          \tag{5.1}
\]

which records the separate layer marginals.  It does not record which
rank-`t` and rank-`t-1` entries belong to the same physical lower flag.
Passing from a nested table to (5.1) quotients out (3.3); in that quotient,
varying all filler permutations gives exactly the theorem's saturated
fixed-filler maximal-chain lattice.  It does not quotient out the separate
cross-depth marginal invariant (2.3) after arbitrary labels and filler sets
are embedded globally.

Therefore there is no conflict:

* **GO:** full signed Pluecker lattice at `q=2`, and the stated saturated
  marginal maximal-chain lattice for fixed filler set and active pair;
* **NO-GO:** depth-independent marginal Markov connectivity because of
  (2.3), positive Markov connectivity even at one depth, or Markov
  connectivity of occurrence-coupled nested flag tables without an
  additional flag re-pairing actuator;
* **OPEN:** whether physical safe carriers supply such re-pairing through
  outside witnesses, and whether positive planted moves reach bounded
  terminal compiler defect.

## 6. Replay

The dependency-free replay checks the symbolic action for `2<=d<=32`, the
reversal law, layerwise degree preservation, and (4.1)--(4.2):

```text
scratch/audit_h2_coatom_q2_plucker_and_nested_J_invariant_20260801.py
scratch/h2_coatom_q2_plucker_and_nested_J_invariant_20260801.audit.json
```

It reports

```text
PASS_Q2_PLUCKER_NORMAL_FORM_AND_NESTED_J_OBSTRUCTION
```

with canonical payload SHA-256

```text
5005c8d647666920a015ef681f2e0de7f8d8a0a3dba54f4280c267210c9a62c0
```
