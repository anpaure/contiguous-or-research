# Buffered Pascal braids and the exact fixed-depth/Gaussian divide

Date: 2026-07-25

This note gives a positive arbitrary-fixed-depth extension of the depth-two
braid in `TRANSLATION_PACKET_MULTIDEPTH_RAINBOW_LEMMA_20260725.md`.  The
extension is literal: its pieces are genuine move-to-front state paths.  It
also identifies a sharp reason why this theorem cannot simply be evaluated
at depth (A\sqrt m): one radius-(H) packing can cover at most (N_H)
middle owners, which is only (e^{-A^2+o(1)}W).  A Gaussian-depth theorem
therefore needs a simultaneous mixture of all radii, not a stronger
single-radius saturating cycle.

Throughout Sections 1--5 the ambient cube is (B_{2m}),

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\]

## 1. A deterministic Pascal-braid identity

Let

\[
 S_{i+1}=S_i-\{p_i\}+\{q_i\},\qquad |S_i|=r,
\tag{1.1}
\]

be a Johnson walk.  Call a transition interval **support-separated** when
the two-element supports

\[
 D_i=\{p_i,q_i\}
\tag{1.2}
\]

are pairwise disjoint throughout that interval.

For (h\ge0), define the forward union windows

\[
 B_i^h=S_i\cup S_{i+1}\cup\cdots\cup S_{i+h}.
\tag{1.3}
\]

### Theorem 1 (buffered Pascal braid)

Suppose the transitions from (i) through (i+h+q-1) are
support-separated.  Then

\[
 |B_i^h|=r+h,
\tag{1.4}
\]

and, for (0\le q\le h),

\[
 \boxed{
 \bigcap_{j=0}^{q}B_{i+j}^{h}=B_{i+q}^{h-q}.}
\tag{1.5}
\]

For every (q\ge0) for which the displayed transitions are
support-separated,

\[
 \boxed{
 \bigcup_{j=0}^{q}B_{i+j}^{h}=B_i^{h+q}.}
\tag{1.6}
\]

In particular, put (r=m-H) and

\[
 T_i=B_i^H\in\binom{[2m]}m.
\tag{1.7}
\]

If every (2H) consecutive transition supports are disjoint, then for
every (0\le q\le H),

\[
 \boxed{
 \bigcap_{j=0}^{q}T_{i+j}=B_{i+q}^{H-q},\qquad
 \bigcup_{j=0}^{q}T_{i+j}=B_i^{H+q}.}
\tag{1.8}
\]

Thus one support-separated rank-((m-H)) path carries an exact two-sided
depth-(H) Pascal tower.  No separate higher-shadow factorization identity
is needed.

#### Proof

On a support-separated interval, each transition removes a different
coordinate already present at the beginning of the interval and inserts a
different coordinate absent at the beginning.  Hence

\[
 B_i^h=S_i\cup\{q_i,q_{i+1},\ldots,q_{i+h-1}\},
\tag{1.9}
\]

which proves (1.4).

Consecutive windows satisfy the two Pascal identities

\[
 B_i^h\cap B_{i+1}^h=B_{i+1}^{h-1},
\qquad
 B_i^h\cup B_{i+1}^h=B_i^{h+1}.
\tag{1.10}
\]

Indeed, the first window has the unique endpoint coordinate (p_i) which
the second lacks, while the second has the unique endpoint coordinate
(q_{i+h}) which the first lacks; their common part is precisely the union
of (S_{i+1},\ldots,S_{i+h}).  Iterating the intersection identity gives
(1.5), and iterating the union identity gives (1.6).  Equation (1.8) is the
specialization (h=H).  \(\square\)

The support-separated hypothesis is stronger than necessary, but has two
advantages: it is transparent and it is exactly what a no-repeated-direction
arc in an orientation cube supplies.  The identities themselves remain
valid under the weaker two-sided residence hypotheses of the canonical MTF
realization theorem.

The same conclusion has a useful purely recursive formulation which starts
directly from Lemma 19 of the translation-packet note.

### Corollary 1A (iterated two-sided-rainbow lift)

Let \(P^0\) be a linear path system in rank \(r\).  On every component,
define recursively

\[
 S_i^{t+1}=S_i^t\cup S_{i+1}^t.
\tag{1.11}
\]

Suppose that through level \(2d\):

1. every \(S_i^t\) has size \(r+t\); and
2. all \(S_i^t\)'s at a fixed level are globally distinct.

Then \(P^t=(S_i^t)\) is a simple Johnson path system at every level and

\[
 S_i^t\cap S_{i+1}^t=S_{i+1}^{t-1}.
\tag{1.12}
\]

Taking \(P^d\) as the middle system, its \(q\)-fold consecutive
intersections and unions are

\[
 \boxed{
 \bigcap_{j=0}^{q}S_{i+j}^{d}=S_{i+q}^{d-q},\qquad
 \bigcup_{j=0}^{q}S_{i+j}^{d}=S_i^{d+q}}
 \quad(0\le q\le d).
\tag{1.13}
\]

If \(P^0\) has \(J\) components, the lower identity omits at most
\(2qJ\) endpoint vertices of \(P^{d-q}\), while the upper identity uses all
vertices of \(P^{d+q}\).  Thus the complete deterministic loss of an
iterated braid is a \(2q\)-per-component fringe; all other loss is already
present in the levelwise vertex systems.  For cyclic components, interpreted
with cyclic indices, this fringe is zero.

#### Proof

At level \(t\), the two consecutive unions in (1.11) are distinct
rank-\((r+t)\) supersets of \(S_{i+1}^{t-1}\), so their intersection is
exactly that common facet.  This proves (1.12) and permits induction on
\(t\).  Iterating intersection and union gives (1.13).

For a component with \(\ell+1\) base vertices, level \(t\) has indices
\(0,\ldots,\ell-t\).  The lower \(q\)-windows at level \(d\) map to the
indices \(q,\ldots,\ell-d\) of level \(d-q\), omitting \(q\) indices at
each end.  The upper \(q\)-windows map bijectively to all indices
\(0,\ldots,\ell-d-q\) of level \(d+q\).  Summing over components proves the
ledger.  \(\square\)

For \(d=1\), this is exactly the facet braid; the first nontrivial lower
iteration is Theorem 20.  For arbitrary fixed \(d\), the hypotheses can be
encoded by finitely many rainbow/path conflicts.  At \(d=A\sqrt m\), they
form one growing coupled conflict system; applying a separate saturating
cycle at every rank does not meet (1.11).

## 2. Literal MTF realization and exact reset ledger

For a fixed radius (d), suppose a path interval has (\ell+2d)
pairwise-disjoint transition supports and take the (\ell) central starts.
At a start (t), remove the next (d) departure coordinates and adjoin the
previous (d) departure coordinates.  This is the saturated symmetric
chain

\[
 \mathcal C_t^{(d)}:
 S_t-\{p_t,\ldots,p_{t+d-1}\}
 \subset\cdots\subset S_t
 \subset\cdots\subset
 S_t+\{p_{t-1},\ldots,p_{t-d}\}.
\tag{2.1}
\]

Support separation gives the exact consecutive-shadow interpretation

\[
 S_t-\{p_t,\ldots,p_{t+q-1}\}
   =\bigcap_{j=0}^{q}S_{t+j},
\qquad
 S_t+\{p_{t-1},\ldots,p_{t-q}\}
   =\bigcup_{j=0}^{q}S_{t-j}
\tag{2.1a}
\]

for every \(q\le d\).  Thus the chain exposed at a start is precisely the
two-sided tower of consecutive intersections and unions of the same middle
Johnson walk.

The canonical MTF state from the long-run atom theorem begins with

\[
 \bigl(
 L_t,\{p_{t+d-1}\},\ldots,\{p_t\},
 \{p_{t-1}\},\ldots,\{p_{t-d}\},\mathcal R_t
 \bigr),
\tag{2.2}
\]

where (L_t=S_t-\{p_t,\ldots,p_{t+d-1}\}), and appending (L_{t+1})
performs the next MTF update.  Initializing (2.2) costs at most (2d+2)
nonempty entries; every later chain costs one entry.  Consequently:

### Corollary 2 (literal buffered atom)

The (\ell) central starts form a genuine nonzero contiguous-OR word of
length at most

\[
 \boxed{\ell+2d+1}
\tag{2.3}
\]

which exposes all (\ell(2d+1)) members of their radius-(d) chains.
Those Boolean masks are pairwise distinct.

The distinctness is the long-run atom argument: for two starts, the first
transition direction separating them is empty in the earlier lower flag
and split in the later one; dually the last separating direction is full
in the later upper flag and split in the earlier one.

Thus (J) buffered path components carrying (M) middle starts cost

\[
 \boxed{M+(2d+1)J}
\tag{2.4}
\]

literal entries.  The sharp reset target is therefore (J=o(W/d)).

### Lemma 2A (tight completion of every buffered segment)

Let (n=2m+1).  Every Johnson path

\[
 S_0,S_1,\ldots,S_\ell\in\binom{[n]}m,
 \qquad \ell\le m,
\tag{2.5}
\]

whose transition supports are pairwise disjoint is a segment of one genuine
cyclic-window row.  More precisely, there is a cyclic order
(x_0,\ldots,x_{n-1}) such that

\[
 \boxed{S_i=\{x_i,x_{i+1},\ldots,x_{i+m-1}\}}
 \qquad(0\le i\le\ell).
\tag{2.6}
\]

#### Proof

Write (S_{i+1}=S_i-p_i+q_i).  Disjoint transition supports imply that
the (p_i)'s are distinct members of (S_0), the (q_i)'s are distinct
members of its complement, and no (p_i) equals a (q_j).  Put

\[
 x_i=p_i,\qquad x_{m+i}=q_i\qquad(0\le i<\ell).
\]

Fill (x_\ell,\ldots,x_{m-1}) with the unused members of (S_0), and
fill the remaining positions with its unused complement.  Then the initial
length-(m) window is (S_0), and shifting it once removes (p_i=x_i)
and inserts (q_i=x_{m+i}).  Induction proves (2.6).  \(\square\)

There is also an exact cyclic converse.

### Lemma 2B (maximal residence characterizes wreaths)

Let (S_0S_1\cdots S_{n-1}S_0) be a Johnson (n)-cycle on
(\binom{[n]}m).  Suppose no coordinate occurs in two transition supports
at cyclic distance at most (m-1).  Then the cycle is exactly the family
of length-(m) windows of a cyclic order of ([n]).

#### Proof

There are (2n) coordinate occurrences among the (n) transition
supports.  Every coordinate which changes on the cycle changes an even
positive number of times.  If some coordinate were constant, fewer than
(n) coordinates would change, and another coordinate would change at
least four times.  Two of those changes would have cyclic distance at most
(\lfloor n/4\rfloor<m), contrary to the hypothesis.  Hence every one of
the (n) coordinates changes exactly twice.

The two cyclic gaps between its changes are both at least (m), and sum
to (2m+1), so they are (m) and (m+1).  Its membership word therefore
has one run of ones, of length either (m) or (m+1).  Summing membership
over all coordinates and all states gives (nm); since every run has
length at least (m), every one has length exactly (m).  At each
transition exactly one such run ends and one begins.  Ordering coordinates
by their run starts now makes (S_i) the (i)-th length-(m) cyclic
window.  \(\square\)

Lemma 2A is useful for the packet programme: buffered atoms are not merely
abstract MTF paths; every atom of length at most (m) is literally a
segment of a cyclic order.  Lemma 2B says that a length-(n) saturating
cycle with maximal residence would already be a wreath, so the desired
``tight saturating-cycle theorem'' is exactly a long-residence refinement,
not an additional hidden geometry condition.

## 3. An explicit orbit of atoms

Fix integers (d,\ell\ge1).  For (m\ge\ell+2d), choose disjoint pairs

\[
 \{a_j,b_j\},\qquad -d\le j\le\ell+d-1,
\]

a common set (C) of size (m-(\ell+2d)), and a disjoint unused set of
the same size.  Start with

\[
 S_{-d}=C\cup\{a_j:-d\le j\le\ell+d-1\}
\]

and successively exchange (a_j\) for (b_j).  The (\ell) starts
(S_0,\ldots,S_{\ell-1}) give the literal radius-(d) atom above.

Let (\mathcal A_{m,d,\ell}) be the orbit of its set of
(\ell(2d+1)) Boolean targets under all coordinate permutations.  Regard
this orbit as a uniform hypergraph on

\[
 \mathcal V_{m,d}=\bigcup_{q=-d}^{d}\binom{[2m]}{m+q}.
\tag{3.1}
\]

Every orbit edge contains exactly (\ell) vertices in each rank.

### Lemma 3 (degree and codegree audit)

For fixed (d,\ell), the atom hypergraph is asymptotically regular and has
small relative pair codegree:

\[
 \frac{\max_v d(v)}{\min_v d(v)}=1+O_{d}(m^{-1}),
\tag{3.2}
\]

\[
 \frac{\Delta_2(\mathcal A_{m,d,\ell})}
 {\min_v d(v)}=O_{d,\ell}(m^{-1})=o(1).
\tag{3.3}
\]

Moreover the minimum degree tends to infinity.

#### Proof

If (|\mathcal A|) is the orbit size, double counting incidences in rank
(m+q) gives the exact degree

\[
 D_q=\frac{|\mathcal A|\ell}{\binom{2m}{m+q}}.
\tag{3.4}
\]

For fixed (d), all central binomial coefficients in (3.4) have ratio
(1+O_d(m^{-1})), proving (3.2).

Fix a target (X) and one template position mapped to it.  For another
distinct template position (Y_0), its image under a uniformly random
permutation conditioned on the first image is uniform on the orbit of
(Y_0) under the stabilizer of (X).  That orbit has size

\[
 \binom{|X|}{|X_0\cap Y_0|}
 \binom{2m-|X|}{|Y_0|-|X_0\cap Y_0|}.
\tag{3.5}
\]

Distinct targets in this fixed template differ in at least one and only
(O_{d,\ell}(1)) coordinates.  Hence (3.5) is
(\Omega_{d,\ell}(m)).  Summing over the bounded number of ordered template
position pairs proves (3.3).  Varying even one of the special coordinates
shows that the degree tends to infinity.  \(\square\)

## 4. A literal arbitrary-fixed-depth theorem

### Theorem 4 (fixed-depth central band at coefficient one)

For every fixed (d\ge0), there is a nonzero contiguous-OR word of length

\[
 \boxed{W+o(W)}
\tag{4.1}
\]

covering every Boolean mask in all (2d+1) ranks

\[
 m-d,m-d+1,\ldots,m+d.
\tag{4.2}
\]

The word is a concatenation of genuine support-separated MTF atoms.  Its
number of path components is (o(W/d)) (with the evident convention for
(d=0)).

#### Proof

First fix (d) and (\ell).  Lemma 3 and the fixed-uniformity
Pippenger--Spencer matching theorem give a matching in
(\mathcal A_{m,d,\ell}) covering all but (o_{d,\ell}(W)) vertices of
(\mathcal V_{m,d}).  Concatenate the literal atom words from Corollary 2,
then append every uncovered band mask literally.

Since each selected atom has (\ell) middle targets, the number of atoms is
at most (W/\ell).  The total length is therefore

\[
 W+\frac{2d+1}{\ell}W+o_{d,\ell}(W).
\tag{4.3}
\]

Choose (\ell=\ell(m)\to\infty) sufficiently slowly that the fixed-
uniformity conclusion remains valid.  Equation (4.3) becomes (4.1), and
the number of components is at most (W/\ell=o(W/d)).  \(\square\)

This theorem recovers depth two and extends it to every prescribed finite
depth.  Unlike a marginal shadow statement, it already includes literal
factorability, two-sided shadows, and long coordinate residence.

The same diagonal argument gives a modest but fully physical growing-band
corollary: there is some (d(m)\to\infty) for which (4.1)--(4.2) hold.
Indeed, successively freeze (d=j), choose (\ell_j/j\to\infty), and wait
until the fixed-uniformity matching error is at most (W/j).  This gives no
useful numerical growth rate for (d(m)); in particular it does not reach a
fixed Gaussian window.

## 5. The sharp Gaussian obstruction to a one-radius lift

The fixed-depth proof uses the fact that

\[
 N_d=W-o(W)\qquad(d\text{ fixed}).
\tag{5.1}
\]

At Gaussian depth this ceases to hold.  If (H=A\sqrt m+O(1)), then

\[
 \frac{N_H}{W}=e^{-A^2+o(1)}.
\tag{5.2}
\]

Every vertex-disjoint family of radius-(H) symmetric-chain atoms has at
most (N_H) chains, because every chain has a distinct rank-((m-H))
minimum.  Hence it covers at most (N_H) middle owners.  Its unavoidable
middle defect is

\[
 \boxed{
 W-N_H=(1-e^{-A^2}+o(1))W.}
\tag{5.3}
\]

Thus neither Theorem 18, Theorem 20, nor Theorem 4 can be pushed to a fixed
Gaussian window by strengthening one saturating cycle or one-radius
matching.  A Gaussian theorem must mix the exact symmetric-chain radius
counts

\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),\qquad c_H=N_H,
 \qquad \sum_{d=q}^{H}c_d=N_q.
\tag{5.4}
\]

This gives the precise recursive tower target.

### Multiradius buffered-tower gate

For (0\le d\le H), select support-separated radius-(d) atom paths which
jointly contain \(c_d+\varepsilon_{m,d}\) middle starts, where
\(\sum_{d\le H}|\varepsilon_{m,d}|=o(W)\), so that:

1. atoms of all radii are mutually disjoint as Boolean chains;
2. their rank-((m\pm q)) vertices cover all but (o(W)) targets in total
   for every (q\le H);
3. if (J_d) is the number of radius-(d) paths, then

   \[
   \boxed{\sum_{d\le H}dJ_d=o(W).}
   \tag{5.5}
   \]

By Corollary 2, this gate immediately gives a literal word of length
(W+o(W)) for the whole fixed Gaussian band.  The symmetric orbit measure
of the atom families gives an exact fractional solution with masses
(c_d).  Explicitly, if every radius-(d) atom has (\ell_d) starts and orbit
(\mathcal A_d), assign every orbit atom weight

\[
 w_d=\frac{c_d}{\ell_d|\mathcal A_d|}.
\tag{5.5a}
\]

A fixed rank-((m\pm q)) target lies in exactly
(|\mathcal A_d|\ell_d/N_q) radius-(d) atoms, for (d\ge q).  Its total
fractional load is therefore

\[
 \sum_{d=q}^{H}w_d\frac{|\mathcal A_d|\ell_d}{N_q}
 =\frac1{N_q}\sum_{d=q}^{H}c_d=1.
\tag{5.5b}
\]

Thus the fractional solution is exact at every rank simultaneously.
Theorem 4 proves the integral statement after truncating to any fixed
radius.  What remains is precisely the simultaneous growing-radius
integral resolution.

There is ample local room for (5.5): long-run Gray cycles permit atom paths
of length (\Theta(m)) uniformly for (d=O(\sqrt m)), and then the formal
reset ledger is at most

\[
 \frac1m\sum_{d\le H}d c_d
 =\frac1m\sum_{q=1}^{H}N_q
 =O(W/\sqrt m)=o(W).
\tag{5.6}
\]

So the obstruction is not coordinate residence, path length, or literal
initialization.  It is the one remaining high-degree resolution: choose the
different radii integrally and disjointly while retaining their symmetric
fractional shadow balance.

## 6. Exact status

Proved here:

- the all-depth Pascal intersection/union identities (1.5)--(1.8);
- exact literal MTF realization with reset cost (2.4);
- an explicit symmetric orbit of buffered atoms with fixed-parameter
  codegree (o(D));
- a literal (W+o(W)) theorem for every prescribed finite central band;
- the constant Gaussian middle defect (5.3) for every one-radius tower;
- the exact multiradius radius ledger (5.4)--(5.6).

Still open:

- the multiradius buffered-tower gate at (H=A\sqrt m);
- any integral growing-uniformity theorem strong enough to round its exact
  symmetric fractional solution;
- the corresponding zero-voltage/cyclic packet resolution in odd
  dimension.

The positive frontier is therefore sharper than “iterate the depth-two
braid”: fixed-depth iteration is valid and literal, but Gaussian depth
requires simultaneous radius mixing.  That is the exact place where a
recursive saturating-cycle tower must do new work.

The exact balanced first-shadow Hamilton cycle from Proposition 18A and the
abstract balanced nested extension around its saturating core do not by
themselves invoke Theorem 1: their chosen deletion flags are not known to
occur as sliding windows of the Hamilton transition sequence.  Conversely,
the buffered atoms here are physical sliding towers, but their Gaussian-
radius integral packing is not known.  The missing fusion is therefore
precisely “balanced core extension + sliding recurrence (1.11),” rather
than another marginal quota theorem.
