# Coloured hub reset: a literal necklace and an exact protected owner matching

**Date:** 2026-08-05  
**Method:** explicit Boolean windows, the protected middle-level two-factor
theorem, and alternating parity; no computation  
**Status:** unconditional coloured embedding of the \(O(d)\) holonomy-reset
bank and unconditional extension of its coatom--owner incidences to a
one-copy owner matching.  Residual lower-chain construction and global
chronology fusion remain open.

## 0. Outcome

Put \(k=2r-1\), let \(d\ge1\), and write

\[
                         n=d+1.
\]

For every \(L>n\) satisfying the coordinate aperture below, there is an
explicit cyclic source of length \(L\) with all of the following properties.

1. Its length-\(n\) windows are \(L\) distinct rank-\(r\) owners.
2. At every width \(1\le q\le d\), its \(L\) windows are \(L\) distinct
   named strict-lower targets.
3. The targets at different widths are disjoint because they have different
   ranks.  Thus the source carries \(Ld\) required lower targets exactly
   once.
4. The rank-\((r-1)\) top targets and the owners form one alternating
   \(2L\)-cycle in the middle-levels incidence graph.
5. If \(2L\le r-2\), either alternating parity of that cycle extends to a
   perfect matching of *all* rank-\((r-1)\) targets to *all* rank-\(r\)
   owners.
6. If \(L\ge2(d+1)\), every noncore coordinate has both its owner run and
   its owner gap of length at least \(d+1\).

Consequently the short hub reset needed to remove the age-rotation residue
can be fully named: its owners and all of its lower targets are literal and
collision-free, and its owner assignments do not obstruct the remaining
coatom--owner bijection.

The theorem separates the two label systems exactly.  The explicit necklace
fixes the payload labels.  The protected-factor argument extends only the
owner labels.  It does not construct the residual lower chains or serialize
their literal states.

## 1. The literal hub necklace

Choose disjoint coordinate sets

\[
 K,\ Z=\{z_0,\ldots,z_{L-1}\}\subseteq[k],
 \qquad |K|=r-n=r-d-1,                               \tag{1.1}
\]

where subscripts on the \(z\)'s are read modulo \(L\).  This is possible
precisely when

\[
                         |K|+L=r-n+L\le2r-1.          \tag{1.2}
\]

Define the cyclic source letters

\[
                         A_t=K\cup\{z_t\}
                         \qquad(t\in\mathbb Z_L).      \tag{1.3}
\]

For \(1\le q\le n\), put

\[
 S_{t,q}
   =A_t\cup A_{t+1}\cup\cdots\cup A_{t+q-1}
   =K\cup\{z_t,z_{t+1},\ldots,z_{t+q-1}\}.            \tag{1.4}
\]

### Theorem 1.1 (exact coloured necklace)

Assume \(L>n\).  Then:

\[
                         |S_{t,q}|=r-n+q;             \tag{1.5}
\]

for every fixed \(q\le n\), the \(L\) values \(S_{t,q}\) are pairwise
distinct; and all values over \(1\le q\le d\) are pairwise distinct.

In particular,

\[
                         T_t:=S_{t,n}                 \tag{1.6}
\]

are \(L\) distinct rank-\(r\) owners, while

\[
                         Q_t:=S_{t,d}                 \tag{1.7}
\]

are \(L\) distinct rank-\((r-1)\) targets.  Every chain

\[
 S_{t,1}\subset S_{t,2}\subset\cdots\subset S_{t,d}
 \subset T_t                                             \tag{1.8}
\]

is literal, and the \(L\) chains are target-disjoint.

#### Proof

Equation (1.5) is immediate from the disjointness of \(K\) and \(Z\).
Because \(q<L\), two cyclic intervals of \(Z\) of length \(q\) are equal
only when they have the same initial index.  Hence the values are distinct
at fixed \(q\).  Values belonging to different \(q\)'s have different
ranks, proving the remaining assertions. \(\square\)

The age composition at every owner window is

\[
                         H=(r-d,1,\ldots,1).           \tag{1.9}
\]

The common set \(K\) is the permanent current core; the current \(z\)-label
is the remaining age-zero element.  Since the source is cyclic, the labelled
age state returns after exactly \(L\) transitions.  Thus this is a literal
identity-holonomy hub circuit, not merely a rank-marginal construction.

Each \(z_t\) belongs to exactly the \(n=d+1\) consecutive owners whose
length-\(n\) windows contain it, and is absent from the other \(L-n\)
owners.  Hence \(L\ge2n\) gives both positive and zero owner residence at
least \(n\).

## 2. The protected middle-level cycle

Consecutive owners satisfy

\[
 \begin{aligned}
 T_t\cap T_{t+1}
   &=K\cup\{z_{t+1},\ldots,z_{t+n-1}\}\\
   &=Q_{t+1}.                                        \tag{2.1}
 \end{aligned}
\]

Therefore

\[
 P=
 \{\,Q_{t+1}T_t,\ Q_{t+1}T_{t+1}:t\in\mathbb Z_L\,\} \tag{2.2}
\]

is the alternating cycle

\[
 T_0,Q_1,T_1,Q_2,\ldots,T_{L-1},Q_0,T_0              \tag{2.3}
\]

in the middle-levels incidence graph

\[
 {\rm ML}_r:
 { [2r-1]\choose r-1}\longleftrightarrow
 { [2r-1]\choose r}.                                  \tag{2.4}
\]

It has \(2L\) edges and maximum degree two.

### Theorem 2.1 (protected owner extension)

If

\[
                         2L\le r-2,                   \tag{2.5}
\]

then each of the two parity matchings

\[
 M^-=\{Q_{t+1}T_t:t\in\mathbb Z_L\},
 \qquad
 M^+=\{Q_tT_t:t\in\mathbb Z_L\}                       \tag{2.6}
\]

extends to a perfect matching of \({\rm ML}_r\).

#### Proof

The frozen small protected-factor theorem says that every subgraph of
\({\rm ML}_r\) with maximum degree at most two and at most \(r-2\) edges is
contained in a spanning two-factor.  By (2.2) and (2.5), there is such a
two-factor \(F\) containing \(P\).

Every vertex of \(P\) already has degree two in \(P\).  Hence no edge of
\(F-P\) meets a vertex of \(P\), and \(P\) is an entire cycle component of
\(F\).  Choose the desired alternating parity \(M^-\) or \(M^+\) on that
component, and choose either alternating parity independently on every
other cycle of \(F\).  Their union is a perfect matching of
\({\rm ML}_r\) containing the selected hub parity. \(\square\)

### Corollary 2.2 (owner and payload labels decouple on the hub bank)

Fix the literal payload chains (1.8), and select \(M^+\).  Then chain \(t\)
is assigned to its declared owner \(T_t\), while every remaining
rank-\((r-1)\) target is bijectively assigned to a remaining rank-\(r\)
owner.

Thus, if the remaining strict-lower targets have already been partitioned
into nested chains whose maxima are precisely the remaining coatoms, the
hub chains together with those residual chains form an exact one-copy
owner--payload table.  No reassignment of a hub target is required.

The hypothesis after “if” is the residual chainization theorem; it is not
proved here.  The perfect matching controls owner labels only.

### Corollary 2.3 (a fixed bank of coloured reset and canonical necklaces)

Take \(h\) necklace cycles of the form above, with a common core \(K\) and
pairwise disjoint cyclic label banks \(Z_1,\ldots,Z_h\).  Let their lengths
be \(L_1,\ldots,L_h>d+1\).  Then all their owner and coatom vertices are
pairwise distinct.  If

\[
                         2\sum_{j=1}^hL_j\le r-2,     \tag{2.7}
\]

all cycles, with either prescribed matching parity on each, extend
simultaneously to one perfect matching of \({\rm ML}_r\).

#### Proof

Different label banks give different noncore parts, so the protected cycles
are vertex-disjoint.  Their union is 2-bounded and has
\(2\sum_jL_j\) edges.  Apply the protected-factor theorem and choose the
prescribed parity independently on each resulting protected component.
\(\square\)

For example, \(L=2(d+1)\) is a flat canonical hub necklace: its rotating
age voltage is zero, its owners are distinct, and every noncore coordinate
has run and gap exactly \(d+1\).  Hence any fixed number of canonical
necklaces may be planted alongside the one exceptional residue-reset
necklace for all sufficiently large \(r\).  This remains a fixed protected
bank theorem, not a decomposition of the exponentially many residual
owners into such necklaces.

## 3. Choosing the residue-reset length

Let

\[
                         s=W\bmod n,
 \qquad W={2r-1\choose r}.                            \tag{3.1}
\]

If \(s=0\), no exceptional hub reset is needed.  If \(1\le s<n\), choose

\[
                         L=2n+s.                      \tag{3.2}
\]

Then

\[
                         W-L\equiv0\pmod n,            \tag{3.3}
\]

and

\[
                         2n+1\le L\le3n-1.            \tag{3.4}
\]

The slightly larger choice (3.2), rather than \(n+s\), has two useful
features: \(L>n+1\), so the immediate upper colours

\[
                         T_t\cup T_{t+1}
 =K\cup\{z_t,\ldots,z_{t+n}\}                        \tag{3.5}
\]

are also pairwise distinct; and the hub remains of size \(O(d)\).

The coordinate and protected-factor hypotheses are

\[
 r-n+L\le2r-1,
 \qquad
 2L\le r-2.                                          \tag{3.6}
\]

They hold for all sufficiently large \(r\), since \(n=d+1=O(\sqrt r)\).

### Corollary 3.1 (the \(O(d)\) coloured holonomy reset is owner-safe)

Under (3.6), reserve the \(L\) literal hub chains (1.8) and use
Theorem 2.1 to extend their declared owner incidences.  Their age-state
holonomy is the identity, and the remaining owner count \(W-L\) is divisible
by \(d+1\).

Consequently the forced positive-rotor residue \(W\bmod(d+1)\) can be
removed by an \(O(d)\) bank which simultaneously has:

* distinct named owners;
* distinct named lower targets at every depth;
* distinct immediate lower and upper colours; and
* an owner assignment extendable to a global coatom--owner bijection.

No scalar, containment-Hall, or owner-label obstruction remains for this
exceptional bank.

## 4. Exact remaining coloured gate

The theorem does **not** yet round the full fractional pull clock.  Three
rows remain separate.

1. **Residual chainization.**  After deleting the \(Ld\) reserved hub
   targets, partition every other required strict-lower target into
   \(W-L\) legal depth-\(d\) chains with the remaining coatoms as maxima.
2. **Functional predecessor compatibility.**  Choose literal tails and
   heads for those residual chains so their state boundary balances and
   their owner colour is the owner selected by the perfect matching.
3. **One Euler component.**  Fuse the residual state cycles to the protected
   hub component without changing the named owner or payload rows.
4. **Linear opening.**  The object above is cyclic.  A final linear word
   must open it at a protected cut or recreate the \(O(d)\) wrap
   occurrences in the exterior chronology.

The gain is that the age-rotation voltage is no longer part of those rows.
The entire voltage correction has been realized by one protected literal
necklace and extended through the owner matching exactly.
