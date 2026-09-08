# Ballot forests, excess designs, and the upper-shadow dual

This note records an exact structure theorem for the odd central path.  It
starts with the already verified one-hole lower-rainbow hypothesis and shows
that the *entire* immediate upper-load vector is equivalent to a weighted
design on one smaller rank.  It also gives an all-depth moment identity which
explains why the known exact words have such rigid-looking derivative rows.

Everything through Section 6 is proved.  Section 7 is a proposed construction
target, not a theorem.

## 1. Setup

Put

\[
 K=2r-1,\qquad M=\binom{K}{r},\qquad
 T_0,T_1,\ldots,T_{M-1}\in\binom{[K]}r .
\]

Assume that the `T_i` form a Hamilton path in the Johnson graph and that the
`M-1` colours

\[
 C_i=T_i\cap T_{i+1}\in\binom{[K]}{r-1}
\]

are distinct, omitting exactly one colour `C_*`.  For an upper colour
`U in binom([K],r+1)`, write

\[
 \mu(U)=\#\{i:T_i\cup T_{i+1}=U\}.
\tag{1.1}
\]

For a set `Q`, let `z_Q` be the number of maximal nonempty path blocks all of
whose vertices avoid `Q`.  We set `z_emptyset=1`.

The previously proved ballot-block theorem says that the number `b_Q` of
maximal blocks all of whose vertices contain a fixed `t`-set `Q` is

\[
 b_Q=\frac tr\binom{2r-1-t}{r-t}
      +\mathbf 1_{Q\subseteq C_*}.
\tag{1.2}
\]

## 2. The excess-design normal form

Let `Cat_j=(j+1)^{-1} binom(2j,j)`.  Complement every upper colour and put

\[
 w(A):=\mu([K]\setminus A)-1,
 \qquad A\in\binom{[K]}{r-2}.
\tag{2.1}
\]

Thus `w=-1` marks a missing upper colour, `w=0` a colour used once, `w=1` a
colour used twice, and so on.

### Theorem 2.1 (affine excess design)

The weight has the forced total mass

\[
 \boxed{\sum_A w(A)=\operatorname{Cat}_r-1.}
\tag{2.2}
\]

For every `t`-set `Q`, `0<=t<=r-2`,

\[
 \boxed{
 z_Q=
 \binom{K-t}{r}-\binom{K-t}{r+1}
 -\sum_{\substack{A\supseteq Q\\|A|=r-2}}w(A).}
\tag{2.3}
\]

#### Proof

There are `M-1` path edges and

\[
 \binom K{r+1}=M\frac{r-1}{r+1}.
\]

Consequently

\[
 \sum_Aw(A)=M-1-\binom K{r+1}
 =\frac{2M}{r+1}-1=\operatorname{Cat}_r-1.
\]

The vertices avoiding `Q` form an induced path forest.  It has
`binom(K-t,r)` vertices.  Its internal edges are precisely the path edges
whose upper colour avoids `Q`, so their number is

\[
 \sum_{U\cap Q=\varnothing}\mu(U)
 =\binom{K-t}{r+1}+\sum_{A\supseteq Q}w(A).
\]

Components equal vertices minus edges, proving (2.3).  QED.

Equation (2.3) is the useful strengthening of the original disjointness
transform: the upper deviations are not an arbitrary vector.  They are a
single weighted `(r-2)`-design, and every zero-section count is one of its
upper degrees.

At the top section order this becomes especially transparent.  If
\(A\in\binom{[K]}{r-2}\) and \(U=[K]\setminus A\), then

\[
 \boxed{\mu(U)=r+1-z_A.}
\tag{2.4}
\]

Thus immediate upper coverage is *exactly* the assertion \(z_A\le r\) for
every complementary \((r-2)\)-section.  A hole is a section with
\(z_A=r+1\); loads one and two are sections with \(z_A=r\) and \(z_A=r-1\).
This is not merely an averaged duality: it is a pointwise equivalence.

If every upper colour is covered and no colour is used more than twice, then
`w=1_D` for a family

\[
 D\subseteq\binom{[K]}{r-2},\qquad |D|=\operatorname{Cat}_r-1,
\tag{2.5}
\]

and (2.3) becomes

\[
 z_Q=Z_{r,t}-\deg_D(Q),\qquad
 Z_{r,t}:=\binom{K-t}{r}-\binom{K-t}{r+1}.
\tag{2.6}
\]

Thus perfect immediate-upper balance is equivalent to an unweighted excess
design `D`; simultaneous balance of all coordinate sections is exactly
simultaneous balance of all inclusion degrees of `D`.

## 3. CPCR is the factorial energy of the excess design

Since the upper mean lies strictly between one and two for `r>=4`, its CPCR
is

\[
 \Phi^+=\sum_U(\mu(U)-1)(\mu(U)-2).
\]

### Corollary 3.1

\[
 \boxed{\Phi^+=\sum_Aw(A)(w(A)-1).}
\tag{3.1}
\]

In particular,

\[
 \Phi^+=2\,\#\{U:\mu(U)=0\}
 +\sum_{\mu(U)\ge3}(\mu(U)-1)(\mu(U)-2).
\tag{3.2}
\]

Hence `Phi^+=0` if and only if every upper load is one or two.  At the top
section level, `|A|=r-2`, equation (2.3) reads

\[
 \mu([K]\setminus A)=r+1-z_A,
\]

and therefore

\[
 \boxed{\Phi^+=\sum_{|A|=r-2}(r-z_A)(r-1-z_A).}
\tag{3.3}
\]

This explains the finite CPCR table without residue: `k=7` has two
triple-loaded colours and CPCR `4`; `k=9` has seven and CPCR `14`; the stored
`k=11` path has twelve holes and eighteen triple loads, giving
`2*12+2*18=60`.

There is also a useful stability statement.  Put

\[
 H=\#\{A:w(A)=-1\},\qquad
 P=\sum_A(w(A)-1)_+.
\]

Then

\[
 \Phi^+\ge2(H+P).
\tag{3.4}
\]

Clipping the weights into \(\{0,1\}\) costs \(H+P\) in \(\ell_1\), and
correcting the resulting cardinality costs at most another \(H+P\).
Consequently there is a family
\(D\subseteq\binom{[K]}{r-2}\), \(|D|=\operatorname{Cat}_r-1\), such that

\[
 \boxed{\|w-\mathbf1_D\|_1\le\Phi^+.}
\tag{3.5}
\]

Thus the \(O(r)\) CPCR values in the known words mean something stronger
than small quadratic error: their upper profiles are only \(O(r)\) unit
moves from genuine excess designs of the forced Catalan cardinality.

## 4. Boolean duality and automatic first-order regularity

For `Q subseteq [K]`, define the upper incidence degree

\[
 d^+(Q)=\sum_{U\supseteq Q}\mu(U).
\]

### Theorem 4.1 (Boolean block-degree transform)

For every `Q`,

\[
 \boxed{
 d^+(Q)=\binom{K-|Q|}{r-|Q|}
 -\sum_{P\subseteq Q}(-1)^{|P|}z_P.}
\tag{4.1}
\]

Equivalently,

\[
 \boxed{
 z_Q=\binom{K-|Q|}{r}
 -\sum_{P\subseteq Q}(-1)^{|P|}d^+(P),}
\tag{4.2}
\]

where `d^+(emptyset)=M-1`.

#### Proof

For an upper colour `U`, inclusion-exclusion gives

\[
 \mathbf1_{Q\subseteq U}
 =\sum_{P\subseteq Q}(-1)^{|P|}\mathbf1_{U\cap P=\varnothing}.
\]

Summing with multiplicity `mu(U)` and using

\[
 \sum_{U\cap P=\varnothing}\mu(U)
 =\binom{K-|P|}{r}-z_P
\]

proves (4.1); Boolean inversion gives (4.2).  QED.

The singleton specialization is unexpectedly rigid.  A binary word has
`(# one-blocks)-(# zero-blocks)=start+end-1`.  Combining this with (1.2)
gives

\[
 z_{\{x\}}=\operatorname{Cat}_{r-1}+1
 +\mathbf1_{x\in C_*}
 -\mathbf1_{x\in T_0}-\mathbf1_{x\in T_{M-1}}.
\tag{4.3}
\]

Consequently every one-hole lower-rainbow path, regardless of how poor its
individual upper loads are, has the exact upper vertex-degree formula

\[
 \boxed{
 d^+(x)=(r+1)\operatorname{Cat}_{r-1}
 +\mathbf1_{x\in C_*}
 -\mathbf1_{x\in T_0}-\mathbf1_{x\in T_{M-1}}.}
\tag{4.4}
\]

Thus the upper multihypergraph is automatically vertex-balanced to within
two.  If `w=1_D`, then its complementary excess design satisfies

\[
 \boxed{
 \deg_D(x)=\frac{2(r-2)}{r+1}\operatorname{Cat}_{r-1}-1
 -\mathbf1_{x\in C_*}
 +\mathbf1_{x\in T_0}+\mathbf1_{x\in T_{M-1}}.}
\tag{4.5}

The first-order balance needed by a recursive construction is therefore not
an additional theorem: it is forced by the lower-rainbow endpoint data.

## 5. The affine hierarchy

Write

\[
 E_Q:=\sum_{U\cap Q=\varnothing}\mu(U)
      =\binom{K-|Q|}{r}-z_Q.
\]

Double counting extensions of `Q` gives, for `|Q|=t<=r-2`,

\[
 \boxed{
 \sum_{x\notin Q}E_{Q\cup\{x\}}=(r-2-t)E_Q,}
\tag{5.1}
\]

and therefore

\[
 \boxed{
 \sum_{x\notin Q}z_{Q\cup\{x\}}
 =\binom{K-t}{r}+(r-2-t)z_Q.}
\tag{5.2}
\]

This is an exact affine harmonicity law for the full zero-block triangle.
At level `r-2`, the values `z_A` recover the upper loads pointwise, and
(5.2) propagates all of their lower marginals.  There are not separate
balance problems at every section order; there is one top profile viewed
through successive down operators.

The second moments also have an exact positive-kernel form.  With
`nu(A)=mu([K]setminus A)`,

\[
 \boxed{
 \sum_{|Q|=t}E_Q^2
 =\sum_{A,B}\nu(A)\nu(B)\binom{|A\cap B|}{t}.}
\tag{5.3}
\]

Thus every section-energy is a Johnson-scheme quadratic form of the same
excess design.

### Theorem 5.2 (block starts form an oriented ballot design)

Orient every path edge from \(T_i\) to \(T_{i+1}\).  For a \(t\)-set \(Q\),
let \(\operatorname{in}(Q)\) be the number of directed edges which enter the
family of vertices containing \(Q\), and let \(\operatorname{out}(Q)\) be the
number which leave it.  Then

\[
 \boxed{
 \begin{aligned}
 \operatorname{in}(Q)
 &=B_{r,t}+\mathbf1_{Q\subseteq C_*}
   -\mathbf1_{Q\subseteq T_0},\\
 \operatorname{out}(Q)
 &=B_{r,t}+\mathbf1_{Q\subseteq C_*}
   -\mathbf1_{Q\subseteq T_{M-1}}.
 \end{aligned}}
\tag{5.4}
\]

Indeed, every containing block except a block beginning at the first path
vertex has one entering edge, and every block except one ending at the last
vertex has one leaving edge.  Equation (1.2) then gives (5.4).

More concretely, write a directed transition as

\[
 T_i\longrightarrow T_{i+1}
 =(T_i\setminus\{a_i\})\cup\{b_i\}.
\]

It enters the \(Q\)-section exactly when
\(b_i\in Q\subseteq T_{i+1}\), and leaves it exactly when
\(a_i\in Q\subseteq T_i\).  Therefore (5.4) says that the arrival and
departure tableaux are simultaneous ballot designs at *every* order \(t\),
with the only discrepancies being the three endpoint cliques \(C_*\),
\(T_0\), and \(T_{M-1}\).  This is the oriented-edge interpretation of the
ballot-block theorem.

### Corollary 5.3 (the exact critical mean)

For \(Q\not\subseteq C_*\), the total length of its containing blocks is

\[
 V_Q=\binom{2r-1-t}{r-t},
\]

while (1.2) gives \(b_Q=(t/r)V_Q\).  Therefore

\[
 \boxed{\text{mean length of a \(Q\)-containing block}=\frac rt.}
\tag{5.5}
\]

For \(Q\subseteq C_*\), the extra terminal component changes the mean to
\(V_Q/(tV_Q/r+1)\), the only exception.

This identifies an exact critical product.  If the compiler needs windows of
length \(q+1\), then the critical section order is

\[
 tq\asymp r.
\tag{5.6}
\]

In particular, for the natural delay \(q\asymp\sqrt r\), the critical
section order is also \(t\asymp\sqrt r\).  A hard requirement that *every*
\(t\)-section block have length greater than \(q\) is arithmetically
impossible once \(t>r/q\); at \(t=r/q\) it consumes the entire available
length with no slack.

## 6. The all-depth moment bridge

The block *counts* above have a length-refinement which directly measures
all deeper derivative rows.

Fix `q>=1`.  For a set `Q`, let `Z_Q` be the collection of maximal blocks of
vertices avoiding `Q`, and let `ell(B)` be a block length.  A window
`T_i,...,T_{i+q}` has union avoiding `Q` exactly when it lies in one such
block.  Hence

\[
 \boxed{
 F_q(Q):=\#\{i:(T_i\cup\cdots\cup T_{i+q})\cap Q=\varnothing\}
 =\sum_{B\in Z_Q}(\ell(B)-q)_+.}
\tag{6.1}
\]

Summing over all `t`-sets `Q` yields

\[
 \boxed{
 \sum_{|Q|=t}F_q(Q)
 =\sum_{i=0}^{M-1-q}\binom{K-|T_i\cup\cdots\cup T_{i+q}|}{t}.}
\tag{6.2}
\]

If

\[
 \delta_i^+(q):=r+q-|T_i\cup\cdots\cup T_{i+q}|,
\]

then the right side is

\[
 \sum_i\binom{r-1-q+\delta_i^+(q)}t.
\tag{6.3}
\]

Dually, let `B_Q` be the maximal blocks of vertices containing `Q`.  Then

\[
 \boxed{
 \sum_{|Q|=t}\sum_{B\in B_Q}(\ell(B)-q)_+
 =\sum_i\binom{|T_i\cap\cdots\cap T_{i+q}|}{t}.}
\tag{6.4}
\]

Writing

\[
 \delta_i^-(q):=|T_i\cap\cdots\cap T_{i+q}|-(r-q),
\]

the right side is `sum_i binom(r-q+delta_i^-(q),t)`.

Equations (6.2)--(6.4) say that the full binomial-moment sequence of every
deeper rank defect is exactly the truncated local-time sequence of the
ballot forests.  The familiar `t=1` identity (short zero-runs equal upper
rank deficit, short one-runs equal lower rank excess) is only the first
moment of this stronger transform.

The Boolean inversion survives unchanged at every depth, even when the
window unions have nonconstant rank.  Define

\[
 d_q^+(Q):=\#\{i:Q\subseteq T_i\cup\cdots\cup T_{i+q}\}.
\]

Then inclusion-exclusion on each individual window gives

\[
 \boxed{
 d_q^+(Q)=\sum_{P\subseteq Q}(-1)^{|P|}F_q(P),
 \qquad
 F_q(Q)=\sum_{P\subseteq Q}(-1)^{|P|}d_q^+(P).}
\tag{6.5}
\]

For \(q=1\), this is Theorem 4.1.  For larger \(q\), equations (6.1) and
(6.5) show that the complete higher-union incidence hierarchy is the
Boolean transform of the truncated avoidance-excursion hierarchy.  No
constant-rank assumption and no independent depthwise choice are involved.

For fixed `V_Q=binom(K-|Q|,r)` and `z_Q` one also has the sharp extremal
bounds

\[
 (V_Q-qz_Q)_+\le F_q(Q)
 \le(V_Q-z_Q+1-q)_+.
\tag{6.6}
\]

The lower bound is attained by distributing block lengths as evenly as the
cap `q` permits; the upper bound by concentrating all excess length in one
block.  This makes precise why exact Catalan block *counts* are not yet the
whole theorem: the missing datum is the block-length law.

There is a sharper guide to what that law should be.  If all \(q\)-step
intersections have the ideal size \(r-q\), then after averaging over all
\(t\)-sets,

\[
 \frac{\sum_Q\sum_{B\in B_Q}(\ell(B)-q)_+}
      {\sum_Q\sum_{B\in B_Q}\ell(B)}
 =
 \frac{M-q}{M}\frac{\binom{r-q}{t}}{\binom rt}.
\tag{6.7}
\]

When \(q,t=o(r)\) and \(qt/r\) is bounded, this ratio is
\(\exp(-qt/r+o(1))\).  A geometric block-length distribution of mean \(r/t\)
has exactly this residual-life profile.  Thus at the critical scale
\(t,q\asymp\sqrt r\), equal block lengths are actually the wrong model:
simultaneous ideal shadows ask for an approximately memoryless tail.

This has a natural transition interpretation.  Conditional on a path vertex
containing \(Q\), a perfectly balanced deletion rule removes one of the
\(t\) members of \(Q\) with hazard \(t/r\); its survival time is geometric
with mean \(r/t\), exactly (5.5).  The recursive chronology should therefore
be sought as a deterministic low-discrepancy **hazard schedule**, not as an
equal-block schedule.

## 7. A corrected recursive target (conjectural)

The identities isolate two coupled objects.

1. **Static excess design.**  Make `w` nearly `0/1` (ideally `w=1_D`) and
   make the inclusion degrees of `D` capacity-ordered across the section
   levels that the compiler uses.  Vertex balance is already automatic by
   (4.5); only higher degrees remain.
2. **Chronological realization.**  Realize the forced ballot component
   counts (1.2) with a low-discrepancy hazard schedule: for each \(t\)-section,
   departure hazard approximately \(t/r\), hence the geometric truncated
   local-time profile (6.7).  By (6.2)--(6.5), one chronological condition
   controls all deeper rank moments simultaneously.

A useful theorem to seek is therefore not an independent balancing lemma at
every depth.  It is a **Catalan-design path theorem**: an endpoint-rooted
one-hole lower-rainbow Hamilton path whose excess weight has small factorial
energy and whose ballot forests have uniformly controlled truncated local
times.  Such a theorem would turn the all-depth problem into one static
design plus one interval scheduling statement.

This target is consistent with the known exact words:

* their lower section component counts are forced exactly by (1.2);
* their immediate upper CPCR is only `O(r)`, so `w` is already almost a
  genuine design rather than a generic integer weight;
* the successful factorable words differ from the nonfactorable overlay not
  in component count but in minimum block length, exactly the datum retained
  by (6.1).

What is **not** proved here is existence of the Catalan-design path.  In
particular, balanced upper inclusion degrees do not by themselves enforce
the chronological truncated-local-time bounds.
