# Two-sided (H)-safety and the stateful fusion correction

Date: 2026-07-26

## 0. Outcome

For a directed Johnson path

\[
 X_{t+1}=X_t-a_t+b_t,
 \qquad a_t\in X_t,quad b_t\notin X_t,              \tag{0.1}
\]

the lower and upper trace conditions through depth (H) have an exact
finite-memory characterization.

* Lower safety forbids an inserted coordinate from being removed again
  within the next (H) transitions.
* Upper safety forbids a removed coordinate from being inserted again
  within the next (H) transitions.
* Simultaneous lower and upper safety is equivalent to saying that no
  physical coordinate is toggled twice in any (H)-edge window.

Thus a two-sided fusion process has a single queue of the coordinate
labels used in the preceding (H-1) edges.  A proposed Johnson edge is
legal precisely when both of its labels are absent from that queue.

This corrects the static endpoint-forest formulation in
`MATH_THEOREM_ONE_SIDED_PRODUCT_SCD_FLAG_FUSION_AND_RESIDENCE_DICHOTOMY_20260726.md`:
pairwise safe seams are not transitive through short intermediate paths.
The global fusion problem is a path-cover problem in an (H)-memory
state graph, not an ordinary graph on atomic path endpoints.

## 1. Exact lower and upper criteria

For a (q)-edge window starting at (t), put

\[
 L_q(t)=\bigcap_{j=0}^{q}X_{t+j},
 \qquad
 U_q(t)=\bigcup_{j=0}^{q}X_{t+j}.                  \tag{1.1}
\]

### Lemma 1.1 (lower residence)

For every available window of (q) edges,

\[
 |L_q(t)|=m-q                                      \tag{1.2}
\]

if and only if there do not exist (t\le i<j<t+q) with

\[
                         b_i=a_j.                  \tag{1.3}
\]

#### Proof

The intersection loses one element for every removal which deletes a
coordinate present at the beginning of the window and not already
deleted.  A removal fails to make such a new loss exactly when its label
was inserted earlier in the same window.  This is (1.3). \(\square\)

### Lemma 1.2 (upper residence)

For every available window of (q) edges,

\[
 |U_q(t)|=m+q                                      \tag{1.4}
\]

if and only if there do not exist (t\le i<j<t+q) with

\[
                         a_i=b_j.                  \tag{1.5}
\]

#### Proof

Complement every state.  The complemented edge removes (b_i) and
inserts (a_i), while

\[
 \left(\bigcup_{j=0}^{q}X_{t+j}\right)^c
 =\bigcap_{j=0}^{q}X_{t+j}^c.                     \tag{1.6}
\]

Apply Lemma 1.1 to the complemented path. \(\square\)

### Theorem 1.3 (two-sided distinct-direction criterion)

The path has both correct lower and upper traces through depth (H) if
and only if, in every (H)-edge window, the (2H) labels

\[
 a_t,b_t,a_{t+1},b_{t+1},\ldots,a_{t+H-1},b_{t+H-1} \tag{1.7}
\]

are pairwise distinct.

#### Proof

If a coordinate occurs on two different edges, its membership must
alternate: after it is removed it cannot be removed again before an
insertion, and after it is inserted it cannot be inserted again before a
removal.  Therefore every repeated label supplies either (1.3) or (1.5).
Conversely either residence repeats its coordinate label. \(\square\)

This is exactly the physical repeated-direction criterion used by the
diverse-order compiler.

## 2. Correct stateful fusion automaton

At a live endpoint store the ordered queue

\[
 Q_t=((a_i,b_i):t-H+1\le i<t),                    \tag{2.1}
\]

truncated at the beginning of a component.  The transition
(X_t\to X_t-a+b) is two-sided legal if

\[
                         \{a,b\}\cap\operatorname{supp}Q_t
                         =\varnothing.             \tag{2.2}
\]

After the transition, delete the expired pair and append ((a,b)).
For lower-only fusion one may store only recent insertion labels and
forbid their later removal; for upper-only fusion use the complementary
queue.

An oriented atomic path block induces a partial deterministic map on
these memory states.  A global fusion is valid precisely when the
composition of its block maps and seam maps is defined throughout.

## 3. Pairwise safety is not transitive

Take (H\ge3) and three successive transitions

\[
 \begin{array}{c|cc}
   &\text{remove}&\text{insert}\\ \hline
 e_1&a&x\\
 e_2&b&c\\
 e_3&x&d
 \end{array}                                             \tag{3.1}
\]

with all displayed labels distinct except for (x), and start from an
owner containing (a,b) but not (x,c,d).  The two-edge words
(e_1e_2) and (e_2e_3) are lower-safe: the first contains no removal
of an inserted label, while in the second (x) is already present at
the start.  But (e_1e_2e_3) has the positive residence
(b_1=a_3=x), so its depth-three intersection has size (m-2), not
(m-3).

Consequently a static graph whose edges test only two adjacent atomic
blocks does not certify a long fusion when the blocks may have length
less than (H).  A static endpoint graph is sufficient only when every
intermediate block already has length at least (H), so that earlier
history expires before the next seam, or when its vertex state has been
expanded to include (2.1).

## 4. Complement-equivariant two-sided reduction

For every path (P=(X_0,\ldots,X_s)), let

\[
                         P^c=(X_0^c,\ldots,X_s^c). \tag{4.1}
\]

Then lower flags of (P^c) are complements of upper flags of (P),
and upper flags of (P^c) are complements of lower flags of (P).
Therefore any stateful fusion construction closed under complementation
and having (o(W)) lower holes automatically has (o(W)) upper holes as
well.  The seam paired with

\[
 X\longrightarrow X-a+b
\]

is

\[
 X^c\longrightarrow X^c-b+a.                       \tag{4.2}
\]

There are no fixed middle owners under complementation.  A path component
may be mapped to itself with reversed orientation, but this causes no
fixed-vertex exception; it must simply be routed as one orbit of the
involution in the stateful path-cover problem.

## 5. Exact surviving theorem

The corrected product-SCD fusion target is:

> Construct a complement-equivariant, owner-disjoint path/cycle cover of
> the oriented atomic product-SCD blocks in the state graph (2.1), using
> all but (o(W/H)) owners, with (o(W/H)) final components and (o(W))
> aggregate prefix-port changes.

The local zero-loss seam theorem remains valid for one fusion with its
full incoming history fixed.  What fails is only the inference that an
ordinary low-weight forest of pairwise-compatible seams can be composed
without carrying that history.

