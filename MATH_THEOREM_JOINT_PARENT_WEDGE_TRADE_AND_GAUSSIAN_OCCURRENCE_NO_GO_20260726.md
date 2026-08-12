# A genuinely joint-parent wedge trade, and the Gaussian occurrence-efficiency no-go

Date: 2026-07-26

Method: pure mathematics only.  The affine moving-frame system and its
quadratic parent invariants are those of
`MATH_THEOREM_CRITICAL_AFFINE_MOVING_FRAME_ATLAS_AND_CROSS_PARENT_NO_GO_20260726.md`.

**Successor correction.**  Section 7 below originally isolated a
\(\Theta(\sqrt m)\)-edge, \(\Theta(\sqrt m)\)-port wide factor as a possible
remaining gate.  The successor note
`MATH_THEOREM_LOWER_FIBRE_EARTHMOVER_BARRIER_AND_WIDE_FACTOR_NO_GO_20260726.md`
closes that gate: exact lower-colour preservation gives
\(h\rho\le2t\), so Gaussian distance and \(\Theta(\sqrt m)\) useful ports
require \(t=\Omega(m)\).  The wedge construction and bounded-width no-go in
this note remain valid; the positive interpretation of Section 7 is
retracted.

## 0. Outcome

The affine parent invariant is not an invariant of the full lower-neutral
trade lattice.  There is an explicit six-coordinate trade \(z_\wedge\) with
the following properties.

1. It deletes six Johnson edges and adds six Johnson edges on the same ten
   middle owners.
2. It preserves every middle-owner degree and every lower colour exactly.
3. Its negative and positive factors are each unions of four paths, so an
   occurrence is a literal finite physical factor, not a formal upper-load
   vector.
4. Its squarefree upper change is
   \[
   \boxed{
     e_{235}+e_{134}+e_{456}
       -e_{136}-e_{345}-e_{245}.}                   \tag{0.1}
   \]
5. When the six active coordinates are embedded in affine general position,
   a suitable affine-line invariant \(F_c\) changes by exactly one.  Thus
   this trade is genuinely jointly neutral across several parents; it is not
   a serial sum of trades already neutral inside each affine parent.

This keeps the moving-frame fallback alive algebraically.  It does not solve
the Gaussian occurrence problem.  The primitive has upper-support diameter
three.  If a directly applicable bank has pairwise disjoint deleted physical
edges and its aggregate switch lowers repeat excess by \(h\) across a
repeat--hole gap \(\rho\), then

\[
 \boxed{
                         h\rho\le {3W\over2}.}       \tag{0.2}
\]

The factor \(3W/2\) can be replaced by \(3M/2\) when only \(M\) cycle edges
are exposed to the bank.  In particular, for \(\rho=\Theta(\sqrt m)\), even
the impossible best case in which the entire Hamilton cycle is packed by
wedge occurrences gives only

\[
                         h=O(W/\sqrt m)=o(W).        \tag{0.3}
\]

Serially chaining the wedges does not improve this one-pass ledger: every
intermediate cancellation still pays its local transport work.  More
precisely, repairing \(h=\Theta(W)\) defects across
\(\rho=\Theta(\sqrt m)\) requires

\[
                         g\ge {h\rho\over9}
                         =\Omega(W\sqrt m)            \tag{0.4}
\]

wedge applications.  A serial implementation must therefore rewrite a
cycle edge \(\Omega(\sqrt m)\) times on average.  More
generally, a connected growing-diameter factor of size \(t\) which exposes
only \(O(1)\) noncancelled terminal upper units has owner-disjoint total
descent \(O(W/t)\).  Hence the surviving construction must be a **wide**
joint factor: at diameter \(\Theta(\sqrt m)\), each occurrence must have
\(\Theta(\sqrt m)\) simultaneously useful negative-repeat and positive-hole
ports, not one transported port.

There is a second exact shortage.  Trades which keep the two lower incidences
at every owner fixed and merely re-pair incidences inside repeated lower
stars can touch at most \(2E=O(W/m)\) cycle edges, where

\[
                         E=W-\binom n{m-1}.          \tag{0.5}
\]

Thus a successful wide factor must change the owner--lower incidence
assignment itself.  The exact remaining occurrence theorem is stated in
Section 7.  No positive-density physical occurrence theorem for those wide
factors is proved here; the note gives a genuine invariant-breaking atom and
a quantitative no-go for every bounded-width or single-channel composition
of such atoms.

## 1. A general wedge construction

Let \(D\) be a coordinate set, let \(K\) be an \((m-2)\)-set disjoint from
\(D\), and let \(\sigma,\tau\) be permutations of \(D\) such that

\[
 i,\sigma(i),\tau(i)\quad\text{are distinct for every }i\in D. \tag{1.1}
\]

For each \(i\in D\), define a positive Johnson edge \(e_i^+\) by

\[
\begin{aligned}
 L(e_i^+)&=K\cup\{i\},\\
 U(e_i^+)&=K\cup\{i,\sigma(i),\tau(i)\},\\
 e_i^+&=\bigl\{
 K\cup\{i,\sigma(i)\},
 K\cup\{i,\tau(i)\}
 \bigr\},
\end{aligned}                                                   \tag{1.2}
\]

and a negative edge \(e_i^-\) by

\[
\begin{aligned}
 L(e_i^-)&=K\cup\{i\},\\
 U(e_i^-)&=K\cup\{i,\sigma^{-1}(i),\tau^{-1}(i)\},\\
 e_i^-&=\bigl\{
 K\cup\{i,\sigma^{-1}(i)\},
 K\cup\{i,\tau^{-1}(i)\}
 \bigr\}.
\end{aligned}                                                   \tag{1.3}
\]

Put

\[
                         z_{\sigma,\tau}
            =\sum_{i\in D}(e_i^+-e_i^-).            \tag{1.4}
\]

### Theorem 1.1 (wedge neutrality)

The trade (1.4) satisfies

\[
                         B_-z_{\sigma,\tau}=0,
 \qquad
                         B_0z_{\sigma,\tau}=0.       \tag{1.5}
\]

#### Proof

For each lower target \(K\cup\{i\}\), exactly one positive and one negative
edge occur, proving the first identity.

Fix a middle owner \(K\cup\{a,b\}\).  Its positive multiplicity is

\[
 \mathbf1_{\{b\in\{\sigma(a),\tau(a)\}\}}
 +\mathbf1_{\{a\in\{\sigma(b),\tau(b)\}\}}.        \tag{1.6}
\]

Its negative multiplicity is

\[
 \mathbf1_{\{b\in\{\sigma^{-1}(a),\tau^{-1}(a)\}\}}
 +\mathbf1_{\{a\in\{\sigma^{-1}(b),\tau^{-1}(b)\}\}}.       \tag{1.7}
\]

The first indicator in (1.6) equals the second inverse indicator in (1.7),
and the second equals the first.  Hence the two multiplicities agree at
every owner. \(\square\)

The construction is global across the parents containing its several
exchange pairs.  Neither the owner nor the lower ledger need vanish after
restricting (1.4) to one exchange-pair parent.

## 2. An explicit six-coordinate invariant breaker

Take \(D=\{1,2,3,4,5,6\}\) and

\[
 \sigma=(1\ 2\ 3\ 4\ 5\ 6),
 \qquad
 \tau=(1\ 3)(2\ 5\ 4\ 6).                          \tag{2.1}
\]

The positive upper triples are

\[
 123,\ 235,\ 134,\ 456,\ 456,\ 126,                \tag{2.2}
\]

and the negative upper triples are

\[
 136,\ 126,\ 123,\ 345,\ 245,\ 456.                \tag{2.3}
\]

Cancelling equal upper colours proves (0.1).

The six negative edges, with the common core \(K\) suppressed, are

\[
 16{-}13,quad 12{-}26,quad 23{-}13,quad
 34{-}45,quad45{-}25,quad56{-}46,                 \tag{2.4}
\]

while the positive edges are

\[
 12{-}13,quad23{-}25,quad34{-}13,quad
 45{-}46,quad56{-}45,quad16{-}26.                 \tag{2.5}
\]

Both factors use exactly the owner set

\[
 \{12,13,16,23,25,26,34,45,46,56\},                 \tag{2.6}
\]

with degree two at owners \(13,45\) and degree one at the other eight
owners.  Each factor is a union of four paths.  Thus this is a literal
port-identical path-factor replacement.

### Theorem 2.1 (affine invariant breaking)

Embed the six active coordinates as six affine-plane points with no three
collinear.  Let the line weighting \(c\) give weight one to the line through
coordinates \(2,3\), and zero to every other line.  Then

\[
                         \langle F_c,B_+z_{\sigma,\tau}\rangle=1.           \tag{2.7}
\]

#### Proof

For this weighting,

\[
                         F_c(U)=\binom{|U\cap\ell(2,3)|}{2}.   \tag{2.8}
\]

Because no third active coordinate lies on \(\ell(2,3)\), an active upper
triple contributes one precisely when it contains the pair \(23\).  Among
the six terms of (0.1), only the positive triple \(235\) contains that pair.
The common core contributes equally to the positive and negative sides by
the zero-mass and zero-point-margin identities.  Hence the difference is
one. \(\square\)

Six points in affine general position exist for every sufficiently large
affine-plane order.  Equation (2.7) proves that the joint-parent toll from
the preceding note can be nonzero in an actual finite Johnson edge trade.

## 3. Exact upper-hole score and Hamilton legality

Let the three positive targets in (0.1) be \(P\) and the three negative
targets be \(N\).  If the negative factor (2.4) occurs in a Hamilton cycle
\(C\), the exact repeat change after the replacement is

\[
 R^+(C+z_\wedge)-R^+(C)
   =|P\setminus\mathcal H(C)|-|N\cap\mathcal R(C)|. \tag{3.1}
\]

Thus the switch has margin-three descent when all three negative targets
are repeated and all three positive targets are holes.  This is actual
missing-shadow descent, not merely invariant breaking.

Degree and lower-colour legality follow from Theorem 1.1.  Simplicity first
requires

\[
 F^-\subset E(C),
 \qquad
 F^+\cap(E(C)\setminus F^-)=\varnothing.             \tag{3.2}
\]

Hamiltonicity then has one further exact condition.  Delete the six negative edges from \(C\),
contract each resulting path component to a vertex, and insert the six
positive edges.  The replacement is Hamilton precisely when the resulting
quotient is connected; since every quotient vertex has degree two, this is
equivalent to the quotient being one cycle.  The port condition is not
automatic from (1.5).

## 4. Why a dense wedge bank still fails at Gaussian depth

Every target in (0.1) has common outside core \(K\) and local rank three.
Therefore

\[
                         \operatorname {diam}_J
                         \operatorname {supp}(B_+z_\wedge)\le3.           \tag{4.1}
\]

Consider any collection of wedge occurrences whose deleted edge sets are
pairwise disjoint subsets of a Hamilton cycle.  If there are \(g\)
occurrences, then

\[
                         6g\le W.                   \tag{4.2}
\]

After all cancellations between their upper changes, write the aggregate
change as \(\delta\).  The earthmover inequality gives

\[
                         h\rho
 \le\|\delta\|_{\rm EM}
 \le3\sum_{j=1}^g\|(B_+z_j)^+\|_1
 =9g.                                               \tag{4.3}
\]

Combining (4.2)--(4.3) proves (0.2).

This argument allows arbitrary overlap and cancellation among intermediate
upper targets.  It even grants that every packed occurrence passes the
Hamilton quotient test.  Hence failure at \(\rho=\Theta(\sqrt m)\) is an
efficiency obstruction, not an occurrence-probability estimate.

More generally, let elementary directly applicable factors have upper
diameter at most \(D\), total positive masses \(s_j\), and pairwise disjoint
deleted physical edge sets.  Since \(s_j\) is at most the number of deleted
edges,

\[
                         h\rho\le D\sum_js_j\le DW.  \tag{4.4}
\]

Thus every one-pass atlas with \(D=o(\sqrt m)\) has only \(o(W)\) descent
across a Gaussian gap, even if its physical occurrence density is maximal.

## 5. Narrow long factors also have sublinear capacity

One might concatenate \(L=\Theta(\sqrt m)\) wedges and cancel all but a
constant number of terminal upper targets.  The next elementary bound shows
why this remains too narrow.

Let \(z\) be a connected physical trade.  Form its augmented support graph
whose vertices are changed Johnson edges, joining two when they share a
middle owner or have the same lower colour.  Edges sharing an owner have
upper targets at Johnson distance at most one; edges with the same lower
colour have upper targets at distance at most two.  Hence a connected
component containing \(t\) changed edges has upper diameter at most
\(2(t-1)\).  In particular a connected trade of upper diameter \(\rho\)
contains at least \(\rho/2+1\) changed edges.  Owner neutrality makes the
positive and negative edge counts equal, so a squarefree occurrence deletes
at least \(\rho/4\) edges.

### Proposition 5.1 (single-channel packing no-go)

Suppose every occurrence in an owner-disjoint bank has at least \(c\rho\)
deleted edges and improves repeat excess by at most \(b\), where \(b,c>0\)
are independent of \(m\).  Then the total improvement of the bank is at
most

\[
                         {bW\over c\rho}.            \tag{5.1}
\]

In particular it is \(o(W)\) for \(\rho=\Theta(\sqrt m)\).

#### Proof

At most \(W/(c\rho)\) occurrences fit into pairwise disjoint deleted edge
sets.  Multiply by the per-occurrence improvement bound \(b\). \(\square\)

Therefore a growing-diameter occurrence must be wide: its useful descent
must be proportional to its deleted factor size.  A long factor with one or
finitely many terminal ports cannot close coefficient one.

## 6. The repeated-lower-star bank is also sublinear

There is a superficially dense jointly neutral operation which must be
excluded separately.  For a lower target \(S\), all middle supersets
\(S\cup\{a\}\) form a clique.  If two current cycle edges have lower colour
\(S\), their four owner incidences can be re-paired inside this clique.  The
operation automatically preserves owner degrees and the lower load.

Let \(\ell(S)\) be the lower load of a lower-complete Hamilton cycle, and
write

\[
                         \ell(S)=1+h(S),
 \qquad
                         \sum_Sh(S)=E=W-|\mathcal L|.           \tag{6.1}
\]

The total number of cycle edges whose lower colour is repeated is

\[
\begin{aligned}
 \sum_{S:\ell(S)\ge2}\ell(S)
 &=|\{S:h(S)>0\}|+\sum_Sh(S)\\
 &\le2E.                                             \tag{6.2}
\end{aligned}
\]

For \(n\in\{2m,2m+1\}\), one has \(E=O(W/m)\).  Hence every atlas which
keeps the owner--lower incidence assignment fixed and only re-pairs
incidences at lower stars has physical support \(O(W/m)=o(W)\).

This proves that the required wide trade cannot be obtained from repeated
lower colours.  It must change which lower target is incident with a given
owner, while cancelling all lower degrees only across the whole factor.

## 7. The exact surviving occurrence theorem

The owner--lower inclusion graph gives a canonical formulation.  Its left
vertices are middle owners \(X\in\binom{[n]}m\), its right vertices are
lower targets \(S\in\binom{[n]}{m-1}\), and \(X\) is adjacent to \(S\) when
\(S\subset X\).

A Hamilton cycle \(C\) determines two used owner--lower incidences at every
owner and \(2\ell(S)\) used incidences at every lower target, paired at
\(S\) into the cycle edges of lower colour \(S\).  Every lower- and
owner-neutral physical factor is equivalently:

1. an alternating reassignment of these incidence tokens preserving degree
   two at every affected owner and degree \(2\ell(S)\) at every affected
   lower target;
2. a new pairing of the reassigned incidences at each lower target;
3. a port quotient which is one cycle after insertion into \(C\).

For coefficient one, the missing theorem must produce owner-disjoint
components \(Q\) of this reassignment with

\[
\begin{aligned}
 |E^-(Q)|&=\Theta(\sqrt m),\\
 -\Delta R^+(Q)&=\Theta(\sqrt m),\\
 \sum_Q|E^-(Q)|&=\Omega(W),                          \tag{7.1}
\end{aligned}
\]

and with positive targets concentrated on current holes and negative targets
on current repeated upper colours.  The components must also pass the
Hamilton quotient test.

The wedge trade proves that alternating incidence reassignments can break
the affine parent invariants.  Equations (4.4), (5.1), and (6.2) prove that
bounded-diameter atoms, single-channel chains, and repeated-star re-pairings
cannot supply (7.1).  A wide \(\Theta(\sqrt m)\)-port incidence factor is the
minimal remaining moving-frame object; proving its statewise occurrence, or
exhibiting a Hall cut in this incidence reassignment problem, is now the
exact unresolved gate.
