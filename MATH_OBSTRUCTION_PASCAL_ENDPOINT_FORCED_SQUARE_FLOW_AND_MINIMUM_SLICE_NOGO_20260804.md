# Forced Pascal endpoint flow, the minimum-slice no-go, and the sharp scalar repair

**Date:** 2026-08-04  
**Method:** pure mathematics; no search, solver, or finite computation  
**Status:** unconditional correction and exact reduction.  The endpoint
completion proposed in
`MATH_THEOREM_FACTOR_FIRST_TRACE_SLICE_PASCAL_CONNECTOR_REDUCTION_20260804.md`
cannot exist for its minimum-component slice forests once `m >= 4`.
The obstruction is already visible at trace rank two.  This note proves the
unique rank-by-rank cross-incidence flow, computes the least possible repair,
and states the corrected endpoint theorem.  It does **not** prove the remaining
occurrence-level matching or quotient-cycle assertion.

## 1. Notation

Use the difference-one coordinates of the factor-first reduction.  Put

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
\]

and

\[
 a_q=\binom{m-1}{q},\qquad a_{-1}=a_m=0.
\tag{1.1}
\]

Let `C_q` be the total number of components of the same-trace slice forests
whose external trace has size `q`, and let `R_q` be the number of unused lower
vertices whose external trace has size `q`.  The proved Pascal identity is

\[
 R_q-C_q=a_q^2-a_{q-1}^2.
\tag{1.2}
\]

Every selected residual incidence at a lower vertex of trace rank `q` has one
of two types:

* a `K`-step, ending at a component of owner-trace rank `q`;
* an `E`-step, ending at a component of owner-trace rank `q+1`.

Let `e_q` denote the total number of selected `E`-step incidences out of the
residual lower vertices of trace rank `q`.  Set `e_{-1}=e_m=0`.

## 2. The forced square-frontier flow

### Theorem 2.1 (unique rank flow)

In every physical endpoint completion,

\[
 \boxed{e_q=2a_q^2\qquad(0\le q\le m-1).}
\tag{2.1}
\]

Consequently, for every `q`,

\[
 \boxed{R_q\ge a_q^2,\qquad C_q\ge a_{q-1}^2.}
\tag{2.2}
\]

These are the same inequality after applying (1.2).

#### Proof

Every residual lower vertex has two connector incidences.  Hence the number
of its `K`-step incidences at rank `q` is `2R_q-e_q`.

Every component of owner-trace rank `q` has two endpoint slots.  They are
filled by the `E`-steps from residual rank `q-1` and the `K`-steps from
residual rank `q`.  Therefore

\[
 e_{q-1}+(2R_q-e_q)=2C_q,
\]

or

\[
 e_q-e_{q-1}=2(R_q-C_q).
\tag{2.3}
\]

Substitute (1.2) and telescope from rank zero:

\[
 e_q
 =2\sum_{j=0}^q(a_j^2-a_{j-1}^2)
 =2a_q^2.
\]

Since `e_q <= 2R_q`, the first inequality in (2.2) follows.  Equation
(1.2) gives the second.  \(\square\)

The theorem is occurrence-level.  It does not average over traces and it does
not assume any symmetry of the chosen saturating cycles.

### Corollary 2.2 (exact same-rank residue)

The number of selected `K`-step incidences at trace rank `q` is exactly

\[
 \boxed{2(C_q-a_{q-1}^2)=2(R_q-a_q^2).}
\tag{2.4}
\]

Thus equality in (2.2) forces every connector incidence at that rank to be an
`E`-step.  Any desired cross-rank traversal in the quotient needs positive
surplus over the square bound at one of its ranks.

## 3. The minimum-component construction is impossible

For one trace of size `q`, put

\[
 v_q=a_{q-1},\qquad l_q=a_q,
\]

and recall that the minimum-component slice forest has

\[
 b_q^{\min}=\max\{1,v_q-l_q\}.
\]

There are

\[
 \binom mq=a_{q-1}+a_q
\tag{3.1}
\]

traces.  Hence, writing `h=floor(m/2)`, its total component count is

\[
 C_q^{\min}=
 \begin{cases}
 a_{q-1}+a_q,&1\le q\le h,\\[2mm]
 a_{q-1}^2-a_q^2,&h<q\le m-1.
 \end{cases}
\tag{3.2}
\]

### Theorem 3.1 (rank-two no-go)

For every `m >= 4`, the minimum-component forests of the factor-first
reduction admit no endpoint matching, even before imposing a quotient cycle,
hinge chains, residence, or a common cap.

#### Proof

At `q=2`, (3.2) gives

\[
 C_2^{\min}=a_1+a_2=\binom m2.
\]

But Theorem 2.1 requires

\[
 C_2\ge a_1^2=(m-1)^2.
\]

Their difference is

\[
 a_1^2-C_2^{\min}
 =(m-1)^2-\frac{m(m-1)}2
 =\binom{m-1}{2}>0.
\tag{3.3}
\]

Equivalently, the minimum forests leave

\[
 R_2^{\min}
 =\binom m2\binom{m-2}{2}
 =a_2^2-a_2
\]

residual rank-two connectors, whereas (2.1) needs `2a_2^2` outgoing
`E`-incidences.  Their total capacity is only `2R_2^{min}`.  \(\square\)

This refutes the final ``Pascal endpoint-cycle theorem'' in the cited
factor-first note with the words ``choose the saturating slice forests of
Theorem 4.1''.  The earlier reduction and witness statements remain valid;
the minimum-component specialization of the remaining theorem does not.

## 4. Sharp scalar augmentation

Deleting one edge of a slice forest increases both its component count and
its residual-lower count by one.  Therefore the least number of such
deletions needed merely to satisfy all rank capacities is

\[
 \Delta_{\rm rank}(m)
 =\sum_{q=1}^{m-1}
   \bigl(a_{q-1}^2-C_q^{\min}\bigr)_+.
\tag{4.1}
\]

The top owner, of trace `E`, is a singleton component.  Its two endpoint slots
cannot use the same physical edge twice.  Hence its two `E`-incidences must
come from two distinct co-singleton residual lower vertices:

\[
 R_{m-1}\ge2,qquad
 C_{m-1}\ge a_{m-2}^2+1.
\tag{4.2}
\]

This costs one deletion beyond (4.1).  Thus define

\[
 \Delta_{\rm phys}(m)=\Delta_{\rm rank}(m)+1.
\tag{4.3}
\]

### Theorem 4.1 (closed form and scale)

For `m >= 4`, with `n=m-1` and `h=floor(m/2)`, one has

\[
 \boxed{
 \begin{aligned}
 \Delta_{\rm phys}(m)
 ={}&\sum_{q=2}^{h}
 \bigl(a_{q-1}^2-a_{q-1}-a_q\bigr)
 +\sum_{q=h+1}^{m-2}a_q^2+2\\
 ={}&\binom{2m-2}{m-1}
      -a_h^2
      -\sum_{q=2}^{h}(a_{q-1}+a_q).
 \end{aligned}}
\tag{4.4}
\]

In particular,

\[
 \boxed{
 \Delta_{\rm phys}(m)
 =\left(\frac12+o(1)\right)
   \binom{2m-1}{m}.}
\tag{4.5}
\]

So the correction is owner-linear.  It is neither `O(1)`, polynomial, nor
Catalan-scale `Theta(W/m)`.

#### Proof

For `2 <= q <= h`, (3.2) and (2.2) require

\[
 a_{q-1}^2-(a_{q-1}+a_q)
\]

additional components.  This is positive because

\[
 a_{q-1}+a_q=\frac m q a_{q-1}
 \quad\hbox{and}\quad
 \binom{m-1}{q-1}>\frac m q.
\]

At `q=1`, the `m` unavoidable singleton trace components already exceed the
square lower bound `a_0^2=1`.

For `h<q<=m-1`, (3.2) is short of the square bound by `a_q^2`.  At
`q=m-1`, this rank deficit is one and (4.2) adds one more, producing the
terminal `+2` in the first line of (4.4).

The square terms in that line contain every `a_j^2`, `0<=j<=m-1`, except
`a_h^2`; the endpoint squares `a_0^2=a_{m-1}^2=1` are the displayed `+2`.
Vandermonde's identity

\[
 \sum_{j=0}^{m-1}a_j^2=\binom{2m-2}{m-1}
\]

gives the second line.

The omitted central square is
`o(binomial(2m-2,m-1))`, and the linear binomial sum is at most `2^m`, also
`o(binomial(2m-2,m-1))`.  Finally,

\[
 \frac{\binom{2m-2}{m-1}}{\binom{2m-1}{m}}
 =\frac m{2m-1}\longrightarrow\frac12.
\]

This proves (4.5).  \(\square\)

The count is attainable as a **raw scalar forest count**: after starting
from minimum forests, delete exactly the required number of edges at each
rank.  There are enough edges because the repaired component bound never
exceeds the total number of owners.  This sentence does not assert that
the deletions preserve the distinguished `K union T` witness component.

## 5. The square repair and its exact boundary failures

Ignoring the terminal physical correction, the cleanest possible totals are

\[
 \boxed{R_q=a_q^2,qquad C_q=a_{q-1}^2.}
\tag{5.1}
\]

Then (2.4) vanishes: all residual incidences are `E`-steps.  This turns the
endpoint problem at boundary `q` into a 2-factor between `R_q` residual
connectors and `C_{q+1}` components, two equally large sets of size `a_q^2`.

There are three exact warnings.

1. **Rank one.**  There are `m` one-trace slices and each has its unique owner
   as a component, so `C_1=m`, not `a_0^2=1`.  The surplus produces exactly
   `2(m-1)` forced same-rank `K`-incidences.
2. **The top singleton.**  At `q=m-1`, (5.1) gives one residual connector.
   The full-trace singleton would use its unique edge to that connector twice.
   The physical repair is (4.2).
3. **Topology.**  If (5.1) held at every interior rank, every quotient cycle
   would stay between one residual rank and the next component rank.  The
   required nested cross-trace chains and one global quotient cycle need
   positive `K`-surplus at selected ranks.

There is also a tempting but invalid literal square.  Fix `e_* in E` and take

\[
 \{\ell(B,S):B\in\tbinom Kq,
                   S\in\tbinom{E\setminus\{e_*\}}q\}
\tag{5.2}
\]

as the residual set.  It has size `a_q^2`.  On the decreasing half this is a
valid **raw** forest census: use the empty forest in root-avoiding traces and a
label-saturating forest in root-containing traces.  On the increasing half it
is impossible, because every trace has the unavoidable residual count

\[
 l_q-v_q+1=a_q-a_{q-1}+1>0,
\]

whereas (5.2) assigns zero residuals to every root-containing trace.  Even on
the decreasing half, its empty forests do not provide the distinguished
same-trace witness `K union T`.  Thus (5.2) is not the desired solution.

## 6. Witness preservation has scalar room

The repair is large, but the target-witness requirement does not contradict
its counts.

### Lemma 6.1 (short rainbow exact-trace witness)

For every `2 <= q <= m-2` and every exact trace `T`, there is a same-trace
Johnson path on exactly `q` owners, using `q-1` distinct lower labels, whose
owner union is `K union T`.

#### Proof

Put `s=m-q>=2` and order

\[
 K=\{x_1,\ldots,x_{m-1}\}.
\]

For `0<=j<=q-1`, let

\[
 H_j=\{x_{j+1},\ldots,x_{j+s}\},
 \qquad A_j=K\setminus H_j.
\tag{6.1}
\]

Then `|A_j|=q-1`, consecutive `A_j` differ by one exchange, and their
union labels

\[
 B_j=A_{j-1}\cup A_j
     =K\setminus\{x_{j+1},\ldots,x_{j+s-1}\}
 \qquad(1<=j<=q-1)
\]

are distinct `q`-sets.  Moreover the sliding windows `H_j` cover `K`, so

\[
 \bigcap_{j=0}^{q-1}A_j=\varnothing.
\]

The actual owners are `(K setminus A_j) union T=H_j union T`; their union is
`K union T`.  \(\square\)

If the square total `C_q=a_{q-1}^2` is used, the total number of slice edges
remaining at rank `q` is

\[
 (a_{q-1}+a_q)a_{q-1}-a_{q-1}^2
 =a_{q-1}a_q.
\tag{6.2}
\]

Its average per trace is

\[
 \frac{a_{q-1}a_q}{a_{q-1}+a_q}
 =\frac q m a_q\ge q-1
 \qquad(2<=q<=m-2).
\tag{6.3}
\]

Thus there is enough scalar edge mass to retain one path from Lemma 6.1 in
every trace.  What remains unproved is a simultaneous rainbow-forest
extension of all these paths with the exact residual endpoint incidences.

## 7. Corrected endpoint theorem

The factor-first route must replace its old final statement by the following.

> **Square-compatible Pascal endpoint theorem.**  Choose witness-preserving
> same-trace linear forests with component totals satisfying
> `C_q >= a_(q-1)^2`, with the strict terminal condition
> `C_(m-1) >= a_(m-2)^2+1`.  Choose their endpoint occurrences so that the
> forced `2a_q^2` `E`-incidences at every boundary and the complementary
> `2(C_q-a_(q-1)^2)` `K`-incidences form a physical endpoint matching.  Add
> enough controlled `K`-surplus to carry the `m` hinge connectors and the
> `m` nested cross-trace chains, and choose the matching so that the quotient
> has the desired cycle partition.

Theorem 2.1 makes every number in this statement necessary.  Lemma 6.1 and
(6.3) show that exact-trace witness length is not a scalar obstruction.  The
unproved content is now precise:

1. rainbow extension of the short witness paths to the required forest
   counts;
2. occurrence-level endpoint Hall/Rado at the forced square frontier;
3. placement of controlled `K`-surplus for the hinge and nested chains;
4. quotient-cycle merging.

Residence and common-cap compatibility remain later, separate gates.

## 8. Scope

This note does not challenge the exact-trace coordinate law, the Pascal
identity, the GMM saturating-cycle input, or the deterministic target witnesses
in the factor-first reduction.  It corrects only the minimum-component
specialization of its final endpoint theorem.  In particular, no claim about
`nu(k)=B(k)+O(1)` follows from the scalar repair alone.
