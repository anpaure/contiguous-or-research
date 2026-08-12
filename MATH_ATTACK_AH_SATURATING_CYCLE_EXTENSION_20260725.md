# Saturating Johnson cycle: exact abstract extension and the first released-owner cut

Date: 2026-07-25

Method: pure mathematics only.

> **Correction notice (2026-07-25).**  The claims in Result item 2 and
> Sections 3--4 that the omitted-only depth-one Hall cut is unresolved are
> retracted.  Every lower set on the saturating cycle has two distinct used
> middle supersets.  Hence it has at most \(m\) omitted middle supersets, and
> double-counting facets gives
> \(|\partial\mathcal A|\ge|\mathcal A|\) for every
> \(\mathcal A\subseteq E\).  Thus the omitted owners do have an SDR and
> already give exact depth-one balance.  Moreover, for \(m\ge37\), every
> resulting high set has an abstract balanced extension through depth two,
> and the same argument propagates to every
> \(q\le(1/2-\varepsilon)\log_2m\) for fixed \(\varepsilon>0\).
> The corrected proof, including all Gale cuts and exact threshold
> arithmetic, is in
> `MATH_ATTACK_A_JOHNSON_OMITTED_OWNER_CUT_AUDIT_20260725.md`.
> The common core-flow theorem in Section 1 and the physical-scope warning
> in Section 6 are unaffected.  Sections 3--4 below must not be cited as an
> obstruction.

## 0. Result

Let

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 N_q=\binom n{m-q},\qquad
 d=W-N_1=\frac{2W}{m+2}.
\]

The saturating-cycle theorem supplies a simple Johnson cycle on a set
\(U\subseteq\binom{[n]}m\) of \(N_1\) middle owners and a bijection

\[
 \phi:U\longrightarrow V_1:=\binom{[n]}{m-1},
 \qquad \phi(X)\subset X,
\tag{0.1}
\]

whose values are the consecutive lower intersection colours.  Put
\(E=V_0\setminus U\), so \(|E|=d=O(W/m)\).

Two exact conclusions follow.

1. The \(N_1\) cycle owners admit one common integral nested extension
   through every depth \(H<m\), with optimally balanced multiplicity for
   total mass \(N_1\), while preserving (0.1) exactly.  Thus no
   Boolean-cut obstruction occurs below rank \(m-1\) for the
   **core-total** quotas.

2. To place the same core inside the original \(W\)-mass balanced quotas
   while releasing only the omitted owners, the very first transition
   requires

   \[
   \boxed{|\partial\mathcal A|\ge|\mathcal A|
   \qquad(\mathcal A\subseteq E).}
   \tag{0.2}
   \]

   Equivalently, the omitted middle sets must have distinct
   rank-\((m-1)\) facets.  Although the saturating-cycle theorem itself gives
   no structural information about the omitted family, its cardinality is
   small enough that Lovasz--Kruskal--Katona implies (0.2) automatically for
   every \(m\ge6\); see Theorem 3.2 below.  If extra cycle owners with colour set
   \(Q\subseteq V_1\) are also released, the exact first-transition cut is

   \[
   \boxed{
   |\mathcal A|
   \le |\partial\mathcal A\cap Q|
      +|\partial\mathcal A\cap H_1|
   \quad
   (\mathcal A\subseteq E\cup\phi^{-1}(Q)),
   }
   \tag{0.3}
   \]

   for some \(H_1\subseteq V_1\) of size \(d\).  Here \(Q\) supplies the
   missing baseline slots and \(H_1\) the \(d\) high-quota slots.

Consequently the desired \(O(W/m)\)-owner release passes its exact first
transition with \(Q=\varnothing\).  The remaining abstract question is the
simultaneous continuation of those released owner copies inside the
original \(W\)-mass floor/ceiling capacities; the remaining physical
question is the tight/rotor realization of the large cycle core.

At the literal level an additional, logically prior issue remains.  The
saturating Johnson cycle physically realizes only the middle targets and
their first lower colours.  The deeper nested extension proved here is an
abstract flow; a general Johnson cycle is not a tight-window/MTF
trajectory, so its depth-\(q\), \(q\ge2\), flags are not yet physical
contiguous-OR witnesses.

## 1. Balanced extension of the \(N_1\)-owner core

Fix \(1\le H<m\).  For \(1\le q\le H\), put

\[
 \lambda_q^{\rm core}=\frac{N_1}{N_q},
 \qquad
 c_q^{\rm core}=\left\lfloor\lambda_q^{\rm core}\right\rfloor.
\tag{1.1}
\]

Since \(N_q\le N_1\) for \(q\ge1\), every
\(c_q^{\rm core}\ge1\).

### Theorem 1.1 — exact common-owner core extension

There are maps

\[
 L_q:U\longrightarrow V_q,\qquad1\le q\le H,
\]

such that

\[
 L_1(X)=\phi(X),\qquad
 L_{q+1}(X)\subset L_q(X),\quad
 |L_q(X)\setminus L_{q+1}(X)|=1,
\tag{1.2}
\]

and every \(S\in V_q\) has fibre size

\[
 |\{X\in U:L_q(X)=S\}|
 \in
 \left\{
 \left\lfloor\frac{N_1}{N_q}\right\rfloor,
 \left\lceil\frac{N_1}{N_q}\right\rceil
 \right\}.
\tag{1.3}
\]

In particular every lower target through depth \(H\) occurs in at least
one core flag.

#### Proof

Use the layered inclusion network on

\[
 V_1,V_2,\ldots,V_H.
\]

Every \(S\in V_q\) has a split node whose internal arc has integral bounds

\[
 c_q^{\rm core}
 \le f(S)\le c_q^{\rm core}+1.
\tag{1.4}
\]

At the top layer \(V_1\), impose throughput exactly one at every node.
Put an unbounded downward arc on every facet inclusion and send total mass
\(N_1\) to the bottom.

There is a symmetric fractional flow: every depth-\(q\) node has
throughput \(N_1/N_q\), divided equally among its \(m-q\) facets.  Indeed,
the usual binomial ratio gives conservation at the next layer.  This flow
respects (1.4), and its top throughput is \(N_1/N_1=1\).

After the standard lower-bound reduction, network integrality gives an
integral flow.  Decompose it into \(N_1\) unit paths, one from every
\(S\in V_1\).  Assign the path rooted at \(S\) to the unique cycle owner
\(\phi^{-1}(S)\).  Equations (1.2)--(1.3) follow. \(\square\)

Thus the complete family of Boolean Hall inequalities below depth one is
automatically satisfied for these core-total capacities.  Notice that no
property of the order of the Johnson cycle is needed after its exact
rainbow bijection (0.1).

### Corollary 1.2 -- a full-owner abstract flag family with weighted spill
\(o(W)\)

Fix \(A>0\) and \(H\le A\sqrt m\).  For all sufficiently large \(m\), the
core flags in Theorem 1.1 can be augmented by one arbitrary nested deletion
flag for every omitted owner in \(E\), giving a common-owner integral flag
family \(\widetilde L\) on all \(W\) middle sets such that

\[
 \sum_{q=1}^H\frac{O_q(\widetilde L)}{c_q}
 \le d\sum_{q=1}^H\frac1{c_q}
 \le dH=O_A(W/\sqrt m)=o(W).                 \tag{1.5}
\]

Here \(O_q(\widetilde L)\) is balanced overload of the depth-\(q\) load
vector and \(c_q=\lfloor W/N_q\rfloor\).

#### Proof

Let \(a_q\) be the balanced core load from Theorem 1.1.  Its total mass is
\(N_1=W-d\).  Since \(q\le A\sqrt m\), the central binomial ratios give
\(d/N_q=O_A(1/m)<1\) for all sufficiently large \(m\).

We first claim that there is a balanced \(W\)-mass quota vector \(b_q\)
with

\[
 b_q(S)\ge a_q(S)\qquad(S\in V_q).             \tag{1.6}
\]

Write \(p=\lfloor N_1/N_q\rfloor\) and
\(c=\lfloor W/N_q\rfloor\).  The inequality \(0<d/N_q<1\) implies
\(c\in\{p,p+1\}\).  If \(c=p+1\), every full quota is at least \(p+1\),
whereas every core load is at most \(p+1\), so (1.6) is automatic.  If
\(c=p\), the number of \((p+1)\)-entries in the full balanced vector is
exactly \(d\) larger than in the core vector.  Choose its high set to
contain the core high set and any further \(d\) core-low coordinates.  This
proves (1.6).

Let \(e_q\) be the load contributed by the arbitrary flags of the \(d\)
omitted owners.  Then \(e_q\ge0\) and \(\sum_S e_q(S)=d\).  For the full
load \(\mu_q=a_q+e_q\),

\[
 \sum_S(\mu_q(S)-b_q(S))_+
 =\sum_S(e_q(S)-(b_q(S)-a_q(S)))_+
 \le\sum_S e_q(S)=d.
\]

Minimizing over balanced quotas gives \(O_q(\widetilde L)\le d\).
Weighting and using \(c_q\ge1\) proves (1.5). \(\square\)

Thus all marginal, integrality, nesting, common-ownership, and weighted
overload requirements are simultaneously solved around the saturating
cycle core.  What is not solved is chronology: the core paths furnished by
the flow need not be the consecutive sliding flags of the Johnson cycle.

## 2. Cost of releasing the omitted owners

For the original \(W\)-mass fixed-window weights

\[
 c_q=\left\lfloor\frac W{N_q}\right\rfloor\ge1,
\]

releasing \(E\) permanently has the elementary tail-area bound

\[
 \sum_{q=1}^H\frac{|E|}{c_q}
 \le dH
 =O\left(\frac Wm\sqrt m\right)
 =O(W/\sqrt m)
 =o(W)
\tag{2.1}
\]

when \(H=O(\sqrt m)\).

Therefore cardinality and weighted cost are already at the correct scale.
The issue is feasibility of the original \(W\)-mass residual quotas, not
the size of the release.

## 3. The exact first released-owner Hall cut

Freeze the cycle assignment \(\phi\) on every owner in \(U\).  Its
depth-one load is exactly one at every \(S\in V_1\).

For the original total mass \(W\),

\[
 \frac W{N_1}=\frac{m+2}{m},
\]

so every balanced depth-one load is one or two, and exactly

\[
 d=W-N_1
\tag{3.1}
\]

targets have load two.  Let \(H_1\subseteq V_1\), \(|H_1|=d\), be those
high targets.

The released roots \(E\) must be assigned bijectively to the \(d\) bonus
copies in \(H_1\), along facet inclusions.  Hall's theorem therefore gives:

### Theorem 3.1 — omitted-only release criterion at \(q=1\)

The frozen cycle core extends through the first transition to a balanced
\(W\)-owner load if and only if the omitted family \(E\) has a system of
distinct facet representatives.  Equivalently,

\[
 \boxed{
 |\partial\mathcal A|\ge|\mathcal A|
 \qquad(\mathcal A\subseteq E).
 }
\tag{3.2}
\]

When (3.2) holds, take the distinct representatives as \(H_1\).

#### Proof

The residual parent side consists of one copy of every root in \(E\).
The residual child side consists of one bonus copy at every member of
\(H_1\).  Their adjacency is exactly facet inclusion.  Hall is precisely
(3.2), with \(H_1\) chosen as the image of a saturating matching.
\(\square\)

The elementary biregular flag count gives only

\[
 m|\mathcal A|
 \le(m+2)|\partial\mathcal A|,
\qquad
 |\partial\mathcal A|
 \ge\frac m{m+2}|\mathcal A|.
\tag{3.3}
\]

This falls short of (3.2) by an order-\(|\mathcal A|/m\) term, but it is not
the sharp estimate for a family as small as \(E\).

### Theorem 3.2 -- the omitted family always has a facet SDR

For every \(m\ge6\), every family

\[
 \mathcal A\subseteq E
\]

satisfies \(|\partial\mathcal A|\ge|\mathcal A|\).  Hence the omitted-only
release criterion of Theorem 3.1 always holds.

#### Proof

Put \(a=|\mathcal A|\).  For \(a>0\), choose the unique real \(x\ge m\)
such that

\[
 a=\binom{x}{m}.
\]

The Lovasz form of the Kruskal--Katona theorem gives

\[
 |\partial\mathcal A|\ge\binom{x}{m-1}.
\]

Moreover

\[
 \frac{|E|}{\binom{2m-1}{m}}
 =\frac{2W/(m+2)}{\binom{2m-1}{m}}
 =\frac{4(2m+1)}{(m+1)(m+2)}\le1
\]

for \(m\ge6\).  Thus \(a\le|E|\le\binom{2m-1}{m}\), so monotonicity of
the real binomial coefficient gives \(x\le2m-1\).  Consequently

\[
 \binom{x}{m-1}
 =\binom{x}{m}\frac{m}{x-m+1}
 \ge\binom{x}{m}=a.
\]

The case \(a=0\) is trivial.  Hall's theorem now supplies distinct facets
for all members of \(E\). \(\square\)

## 4. Exact cut after releasing additional cycle owners

Let \(Q\subseteq V_1\).  Release, in addition to \(E\), the unique cycle
owner \(\phi^{-1}(S)\) for every \(S\in Q\).  The released root family is

\[
 R(Q)=E\cup\phi^{-1}(Q),
\qquad |R(Q)|=d+|Q|.
\tag{4.1}
\]

The frozen depth-one load is one on \(V_1\setminus Q\) and zero on \(Q\).
For a high set \(H_1\subseteq V_1\), \(|H_1|=d\), the exact residual child
multiplicity is

\[
 r_1(S)=\mathbf1_Q(S)+\mathbf1_{H_1}(S).
\tag{4.2}
\]

The two terms may overlap, correctly giving two residual copies.

### Theorem 4.1 — first-cut criterion with recourse

The released roots \(R(Q)\) can be routed to the balanced depth-one load
with frozen core \(U\setminus\phi^{-1}(Q)\) if and only if

\[
 \boxed{
 |\mathcal A|
 \le
 |\partial\mathcal A\cap Q|
 +|\partial\mathcal A\cap H_1|
 \quad
 (\mathcal A\subseteq R(Q)).
 }
\tag{4.3}
\]

#### Proof

Clone a residual child \(S\) according to (4.2).  A root \(X\in R(Q)\)
is adjacent to every clone of each facet \(S\subset X\).  The neighborhood
of a root family \(\mathcal A\) therefore has exactly the right side of
(4.3) clones.  Hall proves the equivalence. \(\square\)

Theorem 3.2 settles this criterion with

\[
 Q=\varnothing,
 \qquad H_1=\text{the image of a facet SDR of }E.
\]

More generally, if one later needs recourse among cycle owners, the exact
positive target is

\[
 \boxed{
 \exists Q,H_1\subseteq V_1,\quad
 |Q|=O(d),\quad |H_1|=d,\quad\text{such that (4.3) holds.}
 }
\tag{4.4}
\]

Its release cost is \(O(dH)=O(W/\sqrt m)=o(W)\).

No such extra recourse is needed at the first transition.  Formula (4.3)
is retained because it is the exact interface for any later construction
that deliberately releases additional cycle owners.

## 5. A weaker unconditional first-depth profile

Before Theorem 3.2, the degree count (3.3) already gave the following weaker
capacity-two assignment of the omitted roots.  It remains useful as a
robust profile if one imposes extra restrictions on the representative
facets.  Indeed,

\[
 2|\partial\mathcal A|\ge|\mathcal A|
\qquad(\mathcal A\subseteq E)
\]

for \(m\ge2\).  Hall after cloning every lower target twice therefore
assigns every omitted root to a facet with at most two omitted roots per
facet.

Adding these assignments to the one-per-target cycle load gives:

\[
 \boxed{
 1\le\mu_1(S)\le3
 \quad(S\in V_1),\qquad
 \sum_S\mu_1(S)=W.
 }
\tag{5.1}
\]

All first-lower targets remain covered.  This does not give exact balanced
overload \(o(W)\) by itself: a capacity-two matching may use only
\(\lceil d/2\rceil\) distinct facets, allowing \(O(d)=O(W/m)=o(W)\)
third copies.  It does, however, give the unconditional bound

\[
 O_1=O(d)=O(W/m)=o(W)
\tag{5.2}
\]

for this non-wreath q=1 construction.

## 6. Physical scope

The cycle word obtained from the lower colours physically covers:

* every \(S\in V_1\), literally as a colour entry;
* every used middle owner \(X\in U\), as a union of two consecutive colour
  entries;
* the omitted \(d\) middle owners after \(d\) literal append entries.

Its length is \(W+O(1)\).  Thus the first band is literal at coefficient
one.

The paths in Theorem 1.1 are not physical subwords of this cycle.  A
general Johnson cycle changes one middle set by an arbitrary Johnson
exchange; it is not a tight cyclic-window trajectory whose successive
lower cores expose a depth-\(H\) same-start flag.  Initializing the
abstract path of every used owner separately would cost
\(\Theta(HN_1)=\Theta(HW)\), while initializing only the omitted owners
costs

\[
 O(dH)=O(W/\sqrt m)=o(W).
\]

Therefore the omitted-owner ledger and every abstract Boolean cut can be
made small, but the main \(N_1\)-owner core still lacks a literal
multidepth realization.  The next theorem must be a tight/rotor
realization of the extended core paths, not another marginal-flow theorem.
