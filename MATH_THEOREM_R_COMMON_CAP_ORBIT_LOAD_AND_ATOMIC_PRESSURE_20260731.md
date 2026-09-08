# Common-cap existence: orbit-normalized load and atomic-pressure barriers

Date: 2026-07-31  
Lane: R  
Status: unconditional abstract theorems; quantified PBBS/Pascal gate and
counterexamples; no all-\(k\) existence claim

## 1. Outcome

There are two valid quantitative routes from a structured candidate atlas to
a common-cap compiler.

1. Construct a middle-realizing guard word \(Q\), retain the incidences it
   already realizes, and prove a normalized cell-load bound.  In an
   equivariant atlas this reduces exactly to a transportation problem on
   target and cell orbits.
2. Choose candidates independently and verify the complete atomic lopsided
   pressure, including same-cell collisions and all common-cap conflicts.

The first route is strictly better suited to a deadline-dense compiler.  The
uniform atomic profile already fails on the complete near-square injection
graph because collision pressure is too large, even though normalized load
is exactly feasible.  For the PBBS stable-composition bank, an explicit
all-arity pressure bound is available under an alternative-bucket estimate,
but current PBBS/Pascal support theorems do not supply that estimate or the
required post-closure list scale.

Thus bounded physical span is not the missing theorem.  The exact
quantitative alternatives are:

\[
 \text{orbit transportation for a guarded bank},
 \qquad\text{or}\qquad
 \text{summable full alternative-bucket pressure}.
\]

## 2. Guard-word candidate graph

Use the interval compiler setup with physical positions \(P\), maximal
envelopes \(E_p\), exact middle rows \((T_i,I_i)\), lower targets
\({\cal L}\), physical cells \({\cal C}\), and a sound marginal candidate
graph \(G\subseteq{\cal L}\times{\cal C}\).

A **guard word** is a sequence

\[
 \varnothing\ne Q_p\subseteq E_p,\qquad
 \bigvee_{p\in I_i}Q_p=T_i\quad\text{for every }i.       \tag{2.1}
\]

Retain the incidences literally realized by \(Q\):

\[
 H_Q=\left\{(S,C)\in G:\bigvee_{p\in C}Q_p=S\right\}.    \tag{2.2}
\]

The exact guard-word theorem proves that \(H_Q\) is Cartesian and that \(Q\)
is a common-cap compiler exactly when \(H_Q\) has a matching saturating
\({\cal L}\).

## 3. Normalized guarded load

For \(S\in{\cal L}\), put

\[
 m_Q(S)=\deg_{H_Q}(S).
\]

For a cell \(C\), define its normalized guarded load

\[
 \ell_Q(C)=
 \sum_{S:(S,C)\in H_Q}\frac1{m_Q(S)}.                  \tag{3.1}
\]

### Theorem 3.1 (normalized-load common-cap theorem)

If

\[
 m_Q(S)>0\quad(S\in{\cal L}),\qquad
 \ell_Q(C)\le1\quad(C\in{\cal C}),                     \tag{3.2}
\]

then \(Q\) is a literal common-cap compiler after choosing distinct lower
cells.

#### Proof

Give every edge \((S,C)\in H_Q\) weight \(1/m_Q(S)\).  The weights incident
with each target sum to one, and (3.2) says the weights incident with each
cell sum to at most one.  For every \(X\subseteq{\cal L}\),

\[
 |X|
 =\sum_{S\in X}\sum_{C:(S,C)\in H_Q}\frac1{m_Q(S)}
 \le\sum_{C\in N_{H_Q}(X)}\ell_Q(C)
 \le|N_{H_Q}(X)|.
\]

Hall gives a target-saturating matching in \(H_Q\), and every selected edge
is already realized by \(Q\). \(\square\)

More generally, any nonnegative edge weights with target sums one and cell
sums at most one suffice.  The normalized load in (3.1) is the canonical
uniform-on-each-target choice, not a necessary condition.

## 4. Exact orbit transportation theorem

Let a finite group \(\Gamma\) act on coordinates, physical positions,
middle rows, lower targets, and cells.  Assume it preserves \(G\), the
envelopes, and the guard word:

\[
 E_{\gamma p}=\gamma E_p,\qquad
 Q_{\gamma p}=\gamma Q_p.                              \tag{4.1}
\]

Then \(H_Q\) is \(\Gamma\)-invariant.  Let
\({\cal L}_\alpha\) be its target orbits and
\({\cal C}_\beta\) its cell orbits.  Join orbit nodes \(\alpha,\beta\) when
the block

\[
 H_{\alpha\beta}
 =H_Q\cap({\cal L}_\alpha\times{\cal C}_\beta)
\]

is nonempty.

### Theorem 4.1 (orbit-flow factorization)

The graph \(H_Q\) has a fractional matching saturating every lower target if
and only if there are numbers \(z_{\alpha\beta}\ge0\), supported on the
nonempty orbit blocks, such that

\[
 \sum_\beta z_{\alpha\beta}=|{\cal L}_\alpha|
 \quad(\alpha),\qquad
 \sum_\alpha z_{\alpha\beta}\le|{\cal C}_\beta|
 \quad(\beta).                                         \tag{4.2}
\]

Whenever (4.2) holds, \(H_Q\) has an integral target-saturating matching and
\(Q\) is a common-cap compiler.

#### Proof

For a nonempty block \(H_{\alpha\beta}\), invariance and transitivity on the
two vertex orbits give constant left and right degrees
\(d_{\alpha\beta}\) and \(e_{\beta\alpha}\), with

\[
 |{\cal L}_\alpha|d_{\alpha\beta}
 =|{\cal C}_\beta|e_{\beta\alpha}.                     \tag{4.3}
\]

Given (4.2), put on every edge of this block the weight

\[
 x_e=\frac{z_{\alpha\beta}}
 {|{\cal L}_\alpha|d_{\alpha\beta}}.                   \tag{4.4}
\]

The contribution of the block at each target is
\(z_{\alpha\beta}/|{\cal L}_\alpha|\), so target sums are one.  By (4.3),
its contribution at each cell is
\(z_{\alpha\beta}/|{\cal C}_\beta|\), so cell sums are at most one.
Theorem 3.1's fractional-Hall proof gives an integral matching.

Conversely, average any saturating fractional matching over \(\Gamma\), and
let \(z_{\alpha\beta}\) be its total weight in the block.  The averaged
target and cell constraints give (4.2). \(\square\)

By max-flow/min-cut, (4.2) is equivalent to the weighted orbit-cut family

\[
 \sum_{\alpha\in A}|{\cal L}_\alpha|
 \le
 \sum_{\beta\in N(A)}|{\cal C}_\beta|
 \qquad
 (A\text{ a set of target-orbit nodes}).                \tag{4.5}
\]

This is the weakest per-cut test for the fixed equivariant guard word \(Q\).
Without passing to orbits, the same statement is

\[
 |N_G(X)\setminus N_{H_Q}(X)|
 \le |N_G(X)|-|X|
 \qquad(X\subseteq{\cal L}),                            \tag{4.6}
\]

the exact guard-loss inequality.  Under equivariance, (4.5) is a sufficient
and necessary compression of Hall in \(H_Q\); no label-blind cut condition
in the unguarded graph can replace it.

Hence a single transitive target orbit and a single transitive cell orbit
need only satisfy

\[
 |{\cal L}|\le|{\cal C}|
\]

and have at least one retained incidence.  In general, the complete
fractional-Hall problem collapses to a transportation flow on the orbit
incidence graph.  This is a genuine quotient theorem, but it applies to one
physical guarded atlas; averaging unrelated relabelled factors does not
literalize a word.

### Theorem 4.2 (seam-deletion stability)

Let \(x\) be fractional matching weights on a guarded bank \(H\), with
target sums one and cell loads at most \(1-\varepsilon\).  Delete any edge
set and call the retained bank \(H'\).  Suppose every target retains
\(x\)-mass at least \(1-\eta\), where

\[
 0\le\eta\le\varepsilon<1.                              \tag{4.7}
\]

Then \(H'\) still has a target-saturating matching.

#### Proof

For target \(S\), let

\[
 r_S=\sum_{e\in H'(S)}x_e\ge1-\eta
\]

and put \(x'_e=x_e/r_S\) on its retained edges.  Target sums become one.
At any cell,

\[
 \sum_{e\ni C}x'_e
 \le\frac1{1-\eta}\sum_{e\ni C}x_e
 \le\frac{1-\varepsilon}{1-\eta}\le1.
\]

Thus \(x'\) is a saturating fractional matching, and Hall gives an integral
one. \(\square\)

If a target orbit has \(m\) uniformly weighted incidences and a seam collar
deletes at most \(b\) of them for each target, then \(\eta\le b/m\).  Hence

\[
 \boxed{\frac bm\le\varepsilon}                         \tag{4.8}
\]

is a sufficient seam-survival inequality.  This is the normalized form of
the required boundary dispersion: the number of changed cells is not enough;
one needs a lower bound on distributed guarded degree relative to the
fractional cell slack.

### Corollary 4.3 (orbit-transport omission bound)

Suppose an optimal-length carrier and guard word realize every middle and
upper target, and Theorem 4.1 supplies all lower targets outside a family
\({\cal O}\).  Appending one literal letter for each member of
\({\cal O}\) gives

\[
 \nu(k)\le B(k)+|{\cal O}|.                              \tag{4.9}
\]

When orbit transportation is used, \({\cal O}\) must be a union of orbits
for the chosen group.  Otherwise one must refine to its stabilizer (down to
singleton orbits if necessary) and recompute (4.5); the old quotient cannot
be reused unchanged.

## 5. Sharp normalized-load obstruction

The all-width owner-bit family gives a quantitative obstruction.  Fix
\(d,r\ge1\), take \(r\) disjoint middle rows of length \(d+1\), give every
position the envelope

\[
 \Omega=\{o,a,x_1,\ldots,x_{dr}\},
\]

take targets \(S_0=\{o\}\), \(S_j=\{o,x_j\}\), and join them completely to
all \((d+1)r\) singleton cells.

Every incidence is individually sound, every position has permanent owner
\(o\), and the marginal graph is complete.  Nevertheless every
middle-realizing guard word \(Q\) has an \(a\)-bearing position in each row.
No such singleton cell belongs to \(H_Q\), because every lower target omits
\(a\).  Therefore

\[
 |N_{H_Q}({\cal L})|\le dr<dr+1=|{\cal L}|.             \tag{5.1}
\]

If every target degree in \(H_Q\) is positive, then

\[
 \sum_C\ell_Q(C)=|{\cal L}|=dr+1.
\]

Since at most \(dr\) cells have positive load, some cell satisfies

\[
 \boxed{\ell_Q(C)\ge\frac{dr+1}{dr}
 =1+\frac1{dr}.}                                       \tag{5.2}
\]

Otherwise some target has degree zero.  Thus every guard word fails one of
the two normalized-load requirements, quantitatively.  This proves that
interval width \(d\), permanent owners, complete marginal neighborhoods,
and marginal expansion approaching \(1+1/d\) do not imply (3.2).

### 5.1 Equivariant marginal-load no-go

Even symmetry and arbitrarily small load in the **marginal** graph do not
help.  Fix \(h\ge1\), use positions
\(-h-1,\ldots,h+1\), and put

\[
 \Omega=\{o,a,b,x,y\}.
\]

One global middle row has label \(\Omega\).  Singleton middle rows force

\[
 E_p=\{x\}\quad(-h\le p\le-1),\qquad
 E_p=\{y\}\quad(1\le p\le h),
\]

while \(E_0=E_{-h-1}=E_{h+1}=\Omega\).  Take targets

\[
 A=\{x,o,a\},\qquad B=\{y,o,b\},
\]

and cells

\[
 A_j=[-j,0],\qquad B_j=[0,j]\quad(1\le j\le h),
\]

with the \(A\)-target incident to all \(A_j\) and the \(B\)-target incident
to all \(B_j\).

Each incidence is individually sound: the extreme \(\Omega\)-positions
preserve the global row, and its selected interval has the assigned OR.
Reflection, together with \(A\leftrightarrow B\),
\(x\leftrightarrow y\), and \(a\leftrightarrow b\), is an automorphism.
The marginal uniform load of every cell is only \(1/h\).

Yet every saturating matching chooses some \(A_j\) and \(B_t\).  Their caps
meet at position \(0\), where the common letter is only \(\{o\}\).
The \(A_j\)-cell then has OR \(\{x,o\}\), missing \(a\), and the
\(B_t\)-cell has OR \(\{y,o\}\), missing \(b\).  Thus no common cap exists.

This example proves that symmetry, interval geometry, owners, marginal
expansion, and even vanishing marginal normalized load do not suffice.
The load theorem must be applied inside one guard-realized or
Cartesian-guarded bank, not in \(G\).

## 6. Atomic LLL collision barrier

Now choose one candidate independently for each target.  Include a bad event
whenever two targets choose the same cell.  Consider the complete graph
\(K_{L,N}\) and the uniform law on its \(N\) candidates per target.

For a fixed candidate \(e=(S,C)\), the alternative bucket used by the atomic
lopsided criterion contains

\[
 \widetilde D_2(e)=(N-1)(L-1)                          \tag{6.1}
\]

collision events: choose an alternative cell for \(S\), then one of the
other \(L-1\) targets at that same cell.

### Theorem 6.1 (uniform atomic-profile no-go)

The uniform atomic product criterion

\[
 \left(1-\left(\frac cN\right)^2\right)^{(N-1)(L-1)}
 \ge\frac1c,\qquad 1<c<N,                              \tag{6.2}
\]

fails for every \(c\) whenever

\[
 \frac{(N-1)(L-1)}{N^2}\ge\frac1{2e}.                  \tag{6.3}
\]

In particular it fails for every square \(K_{N,N}\), \(N\ge2\).

#### Proof

For \(0<u<1\), \(\log(1-u)<-u\), so the logarithm of the left side of
(6.2) is less than

\[
 -\frac{(N-1)(L-1)}{N^2}c^2.
\]

The function \(c^2/\log c\) on \(c>1\) has minimum \(2e\), attained at
\(c=\sqrt e\).  Under (6.3), the displayed quantity is at most
\(-\log c\), strictly, so the left side is smaller than \(1/c\).
For \(L=N\ge2\),
\((N-1)^2/N^2\ge1/4>1/(2e)\). \(\square\)

This is a no-go only for the uniform specialization of the atomic
lopsided criterion.  It does not refute asymmetric product laws or the
general atomic theorem.  It does show that an independent-choice LLL is
poorly matched to a near-square injection problem: same-cell collisions
already exhaust its pressure.  Fractional Hall or a matching-supported law
should remove collisions before common-cap conflicts are charged.

## 7. A quantitative all-arity pressure hypothesis

After exact unit closure, suppose choices remain independent, every residual
target list has size at least \(M\), and a candidate \(e\) has at most

\[
 \widetilde D_j(e)\le RQ^{j-1}\qquad(2\le j\le d+1)     \tag{7.1}
\]

opposing atomic events of size \(j\).  Here opposing means that the event
prescribes an alternative value in the target part of \(e\), not merely
that it contains \(e\).  Same-cell collision events must be included in
this profile unless the retained candidate system is literally
cell-disjoint; one may not condition on a matching and then use this
independent-product proposition.

### Proposition 7.1 (geometric atomic-pressure bound)

Let \(1<c<M\), put

\[
 u=\frac cM,\qquad \alpha=Qu.
\]

If \(\alpha<1\) and

\[
 \boxed{
 \frac{Ru\alpha}{(1-u^2)(1-\alpha)}\le\log c,}          \tag{7.2}
\]

then the complete event family satisfying (7.1) passes the additive atomic
lopsided criterion and has a conflict-free selector.

#### Proof

The full alternative pressure at \(e\) is at most

\[
 \sum_{j=2}^{d+1}
 RQ^{j-1}\frac{u^j}{1-u^j}.
\]

Since \(u^j\le u^2\) and
\(\sum_{j=2}^{d+1}Q^{j-1}u^j
\le u\sum_{h\ge1}\alpha^h=u\alpha/(1-\alpha)\),
the pressure is bounded by the left side of (7.2).  The atomic lopsided
criterion applies. \(\square\)

For example, if \(\alpha\le1/2\) and \(u\le1/2\), it is enough that

\[
 \frac{8}{3}\frac{Rc^2Q}{M^2}\le\log c.                \tag{7.3}
\]

The condition \(\alpha\le1/2\) itself requires

\[
 M\ge2cQ.                                               \tag{7.4}
\]

For the displayed PBBS stable-coordinate banks,

\[
 Q=2^{\,r-2d-2}-1
\]

for singleton anchors, with the analogous
\(Q_S=2^{|U|}-1\) for a general one-position anchor.  Proposition 7.1 shows
exactly what must be proved: after closure, the relevant auxiliary target
parts need spread scale larger than \(Q\), and the **complete opposing**
chart multiplicity \(R\) must be bounded.  Raw conflict degree is not the
right parameter.

The existing tagged-bank theorem bounds the number of charts through an
anchor and makes one internal unique-disagreement matrix zero.  It does not
bound \(\widetilde D_j(e)\) for every alternative candidate \(e\), because
untagged charts and external conflicts may prescribe other values in the
same target part.  Therefore one may not insert \(R=2k\) into (7.2) without
a new external-contamination theorem.

## 8. PBBS/Pascal verification audit

The current PBBS/Pascal theory supplies the following inputs.

1. Physical lower cells have bounded length and middle rows have one larger
   span in the fixed-depth compiler.
2. On one strict depth-\(d\) resident chronology, mandatory-core pruning
   \(F(I)\subseteq S\) allows a permanent owner
   \(o_p\in F_p\) wherever \(F_p\ne\varnothing\) is certified.  Raw PBBS
   support alone does not preserve this after arbitrary openings or seams.
3. The PBBS all-depth support theorem provides canonical target witnesses
   with bounded load.
4. Before a linear opening and exceptional pins, the PBBS factor has cyclic
   equivariance.
5. Stable-coordinate charts give the exact exponential parameter \(Q\) and
   bounded anchor-internal tagged-chart multiplicity.  Their untagged and
   external alternative buckets are not bounded.

There is one exact negative verification on the native unpruned atlas.  With

\[
 Q=2^{\,r-2d-2}-1,
\]

the stable-coordinate construction gives, for every admissible arity,

\[
 D_j(V_{\{x\}})\ge |V_{\{x\}}|(Q)_{j-1}.               \tag{8.1}
\]

At deadline scale this implies \(D_4>M^2/16\) eventually whenever the
minimum full-list size \(M\) is positive.  Therefore the old raw-degree
quadratic/symmetric LLL test is false for the native PBBS/Pascal atlas.
This does not refute the alternative-bucket criterion: tagged events which
agree on their pivot assignment are lopsided nonneighbors, and the
uncontrolled term is their external contamination.

These facts do **not** verify either existence theorem above.

- Canonical all-depth support gives a witness, not a middle-realizing guard
  word \(Q\) for which every lower target has positive degree in \(H_Q\).
- Permanent owners prevent empty letters but do not protect middle bits or
  assigned-lower bits.
- A linear opening, omitted starts/deadlines, reroot seams, and singleton or
  facet pins break the uncut cyclic action.  The orbit-flow theorem applies
  only after those physical choices have been included in the group action
  or absorbed literally first, with every induced cap and cross-boundary
  middle/prepin equality included in the residual envelopes and guard word.
- Arbitrary seam or pin deletions are not unions of full \(\Gamma\)-orbits.
  Theorem 4.2 therefore requires a literal target-by-target retained-mass
  audit, possibly under the smaller stabilizer or trivial action; orbit
  averaging before the opening is insufficient.
- The sufficient seam estimate (4.8) would require a distributed guarded
  degree \(m\) and fractional slack \(\varepsilon\) with
  \(b/m\le\varepsilon\).  Current support theorems bound canonical witness
  load but do not give this lower degree; scalar deadline surplus is not an
  orbitwise fractional-slack certificate.
- Bounded canonical witness load is not the normalized guarded load
  \(\ell_Q(C)\).
- The stable-bank theorem does not give the complete alternative-bucket
  bound (7.1), a post-closure list scale \(M\ge2cQ\), or a
  deletion-stable matching measure.
- The Pascal odd/even lift preserves ownership identities but has not been
  proved to preserve a guard word, the orbit transportation inequalities,
  or the complete atomic pressure.

Consequently neither (3.2), (4.2), nor (7.2) is currently verified for a
single all-\(k\) PBBS/Pascal compiler atlas.

## 9. Exact remaining theorem

A genuine all-\(k\) common-cap theorem would follow from either one of the
following nonformal inputs.

1. **Equivariant guarded-load theorem.**  After all seams, pins, and unit
   closure, construct one middle-realizing PBBS/Pascal guard word \(Q\) and
   solve the orbit transportation system (4.2) for \(H_Q\), with boundary
   orbits included literally.
2. **Pressure theorem.**  Either prove (7.1)--(7.2) for the full independent
   atomic profile, including same-cell collisions, or first construct a
   spread matching measure and then use a separate matching-supported
   alteration theorem with bounded permanent-minor distortion and external
   stable-chart contamination.  Proposition 7.1 itself is not valid after
   conditioning on a matching law.

The complete-graph obstruction in Section 5 and the collision theorem in
Section 6 show why neither input follows from bounded span, permanent owner
bits, marginal Hall, or raw PBBS support load alone.

## 10. Source theorems used

- MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md.
- MATH_AUDIT_COMMON_CAP_CARTESIAN_AND_ATOMIC_LLL_EXISTENCE_20260731.md.
- MATH_THEOREM_R_ALLK_MATCHING_SUPPORTED_CLUSTER_EXPANSION_AND_OPPOSING_DESCENT_20260730.md.
- MATH_THEOREM_R_ALLK_PBBS_SHALLOW_UNIT_CASCADE_PERMANENT_SWITCHING_AND_CAPPED_RUN_GUARD_20260730.md.
- MATH_AUDIT_R_COMMON_CAP_OWNER_EXPANSION_COUNTEREXAMPLE_20260731.md.
