# Mixed-SCD orbit integral rounding: exact flow, a low-component profile obstruction, and the surviving atlas gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad H=o(m),
\]

and consider the complete labelled coordinate orbit of product-SCD chain
occurrences.  The exact dynamic empty-rectangle theorem is a genuine
fractional theorem, but its integral content has to be divided into three
different assertions.

1. **One fixed radius rounds exactly.**  For
   \(h=m-2r\), the complete orbit of length-\(h\) product diagonals is the
   path set of one layered network.  Its uniform fractional flow of value
   \(N_r=\binom mr^2\) rounds by max-flow integrality to \(N_r\)
   owner-disjoint geodesics.  Thus there is no owner integrality gap in an
   unfiltered, splicing-closed radius slab.

2. **The natural all-radius problem is not the sum of those flows.**  Its
   exact-radius multiplicity is
   \[
     P_h=N_r-N_{r-1},                                      \tag{0.1}
   \]
   and the longer paths already occupy \(N_{r-1}\) owners on every layer
   of the radius-\(r\) slab.  If their insertion current in coordinate
   \(z\) is \(u_z^{>h}(r)\), then every residual integral length-\(h\)
   packing with endpoint leave \(\ell_0+\ell_h\) satisfies
   \[
    \left|n_z^{(h)}-\left({h\over m}N_r-u_z^{>h}(r)\right)\right|
       \le \ell_0+\ell_h.                                  \tag{0.2}
   \]
   If the desired residual stratum is required to retain the
   coordinate-balanced orbit marginal \(n_z^{(h)}=(h/m)P_h+o(P_h/H)\),
   then the preceding scales must deliver
   \[
      u_z^{>h}(r)={h\over m}N_{r-1}+o(P_h/H)                \tag{0.3}
   \]
   simultaneously for every coordinate and every Gaussian radius.  More
   generally, (0.2), together with the actual capacity of the residual
   safe paths which use \(z\), is the necessary cut.  The endpoint
   empty-rectangle inequalities imply neither statement.

3. **Owner integrality and the component bound still do not imply shadow
   coverage.**  There is an explicit, genuinely mixed-frame \(Q_4\)
   mosaic which partitions every middle owner exactly.  After subdividing
   its typical cells into \(Q_\ell\)'s and installing the recursive
   two-sided-rainbow factor, where
   \[
                     H=o(\ell),\qquad \ell=o(m),              \tag{0.4}
   \]
   it has
   \[
                     K\le {W\over2\ell}+e^{-cm}W
                       =o(W/H)                                \tag{0.5}
   \]
   safe components.  Nevertheless, at every fixed Gaussian depth
   \(q=\lfloor A\sqrt m\rfloor\), this atlas misses
   \[
    \left(c_A(1-e^{-3A^2})e^{-A^2}-o(1)\right)W              \tag{0.6}
   \]
   lower targets, and the same number of upper targets.  This is a
   profile Hall cut, not a BTK or one-fixed-pair cut.

Thus the requested atlas is **not** obtained by rounding the proved
empty-rectangle point.  The theorem sharply obstructs two natural
rounding mechanisms: independent fixed-radius flows and owner-preserving
rounding inside one mixed block mosaic.  It does not prove that the full
mixed-SCD orbit has no good integral atlas.  The precise surviving gate is
an all-radius, profile-moving integral chain cover which simultaneously
obeys the current cuts (0.2), crosses the Gaussian block-profile cuts, and is grouped into
\(o(W/H)\) full rotor components.

## 1. Exact positive theorem in one radius slab

Fix a split \(A\mathbin{\dot\cup}B=[2m]\), with
\(|A|=|B|=m\), and put \(h=m-2r>0\).  At phase \(t\) let

\[
 {\cal V}_t=\{S\mathbin{\dot\cup}T:
  S\subseteq A,\ |S|=r+t,
  T\subseteq B,\ |T|=m-r-t\}.                              \tag{1.1}
\]

An arc from phase \(t\) to phase \(t+1\) inserts one coordinate of
\(A\) and removes one coordinate of \(B\).  The full labelled orbit of
any product SCD contains every source-to-sink path in this network: the
two active words can be relabelled independently.

Write \(v_t=|{\cal V}_t|=\binom m{r+t}^2\) and
\(N_r=\binom mr^2\).  Every phase-\(t\) vertex has forward degree
\((r+h-t)^2\), and every phase-\((t+1)\) vertex has backward degree
\((r+t+1)^2\).  Give every phase-\(t\) vertex load

\[
                         \theta_t={N_r\over v_t}.              \tag{1.2}
\]

Splitting that load uniformly over outgoing arcs is conserved because

\[
 {v_{t+1}\over v_t}
   ={(r+h-t)^2\over(r+t+1)^2}.                               \tag{1.3}
\]

Since \(v_t\ge N_r\), all vertex loads are at most one, while both
endpoint layers have load one.

### Theorem 1.1 (fixed-radius integral orbit flow)

The complete length-\(h\) orbit contains \(N_r\) pairwise
owner-disjoint paths, covering both endpoint layers exactly.  The same is
true after arbitrary arc-local deletions whenever the deleted network
retains a fractional flow of that value.

#### Proof

Split each owner into an entrance and exit joined by a unit-capacity arc.
Equations (1.2)--(1.3) give a fractional flow of value \(N_r\).  The
vertex-split network has integral capacities, so max-flow integrality gives
an integral flow of the same value.  The network is acyclic, hence the
flow decomposes into owner-disjoint source-to-sink paths.  Arc deletion
does not change the argument. \(\square\)

This theorem is stronger than a nibble at one radius.  Its limitation is
not integrality but compatibility with the longer-radius paths and with
history-dependent, non-splicing filters.

## 2. Exact cross-radius current inherited by the residual slab

The number of paths of exact length \(h=m-2r\) in a product-SCD
resolution is (0.1), not \(N_r\).  Suppose an owner-disjoint family
\({\cal L}\) of \(N_{r-1}\) longer paths has already been installed and
crosses the whole radius-\(r\) slab.  For \(z\in A\), let
\(u_z^{>h}(r)\) be the number of those slab segments which insert \(z\).

### Theorem 2.1 (residual current identity)

Let \({\cal M}_h\) be any owner-disjoint length-\(h\) packing in the
physical-owner complement of \({\cal L}\).  If it misses
\(\ell_0,\ell_h\) owners on the two boundary layers and inserts \(z\) on
\(n_z^{(h)}\) paths, then (0.2) holds.  Moreover

\[
                    \sum_{z\in A}u_z^{>h}(r)=hN_{r-1}.         \tag{2.1}
\]

#### Proof

In the complete boundary layers, the number of owners containing \(z\)
increases by exactly \((h/m)N_r\) from low to high.  The longer paths
account for an increase \(u_z^{>h}(r)\).  The residual boundary
population difference is therefore

\[
                 {h\over m}N_r-u_z^{>h}(r).                   \tag{2.2}
\]

Every residual monotone path either leaves \(z\) unchanged or inserts it
once.  Removing the two endpoint leave sets perturbs (2.2) by at most
\(\ell_0+\ell_h\), proving (0.2).  Each longer slab segment has exactly
\(h\) insertion directions, so double counting gives (2.1). \(\square\)

The average value in (2.1) is \((h/m)N_{r-1}\), and subtracting it from
(2.2) leaves the natural balanced demand \((h/m)P_h\).  Therefore (0.3)
is the right coordinatewise accuracy when the residual stratum is also
required to retain that balanced orbit marginal.  It is a clean
sufficient dispersion condition, not an unconditional identity for every
possible integral atlas; the unconditional necessary statement is (0.2)
against the available residual direction capacity.

There is a sharp one-coordinate test.  If all residual paths are forced to
avoid one coordinate \(z\), then \(n_z^{(h)}=0\), whence

\[
 \ell_0+\ell_h\ge
 \left({h\over m}N_r-u_z^{>h}(r)\right)_+.                    \tag{2.3}
\]

If the longer current is absent, the right side is

\[
 {h\over m}N_r
   =\left({1\over4}+o(1)\right)P_h                            \tag{2.4}
\]

in the Gaussian range.  Thus a failure to propagate the ancestor current
creates a positive-density exact-radius loss despite asymptotically full
local option lists.  If the ancestor current is balanced, the residual
demand is only \((h/m)P_h\); this audit is why the overcomplete loss
(2.4) must not be summed across radii without the subtraction in (0.2).

The dynamic empty-rectangle theorem sees the large local safe-option
degree.  It does not see the signed boundary current (2.2), because that
current couples two endpoint layers and all previously selected radii.

### Corollary 2.2 (near-complete local lists can violate the current cut)

Orient the residual paths from their high endpoint to their low endpoint.
At a high endpoint containing a fixed \(z\in A\), put the one-label live
insertion support \(\{z\}\); at an endpoint not containing \(z\), use the
empty support, or pad it by an arbitrary currently present label if one
common queue-size type is required.  Every endpoint has a nonempty safe
orbit fibre.  On the \(z\)-containing shore the exact surviving fraction
of active alphabets is

\[
 {\binom{m-r-1}{h}\over\binom{m-r}{h}}
       =1-{h\over m-r}=1-O(m^{-1/2})                         \tag{2.5}
\]

in the Gaussian range, and each separate typed history-option block is
biregular.  Nevertheless every globally legal residual path preserves
membership of \(z\), so (2.3) applies.

This is an exact asymptotic obstruction to deducing integral grouping from
the empty-rectangle theorem, not merely a determinant-two gadget.  The
displayed endpoint histories are individually physical; the corollary
does not claim that an already constructed coherent preceding atlas must
generate this entire aligned family.  Ruling out such alignment for the
actual recursive histories is precisely part of the current-dispersion
gate.

## 3. A genuinely mixed-frame, low-component counteratlas

Partition \([2m]\) into \(b=m/2\) labelled four-blocks.  On each block,
partition its six two-subsets into the three Johnson edges

\[
  \{12,13\},\qquad \{14,24\},\qquad \{23,34\}.                \tag{3.1}
\]

Subsets of local sizes different from two are frozen.  Taking products
over the blocks partitions the whole middle layer into orientation cubes.
If an owner cell has \(s\) local two-set blocks, that cell is a physical
\(Q_s\).  The frames in (3.1) are incompatible and their union is already
connected in one four-block; this is not a fixed-pair atlas.

### Lemma 3.1 (typical cells have linear dimension)

There is an absolute \(c>0\) such that the total number of middle owners
lying in cells of dimension less than \(m/16\) is at most

\[
                              e^{-cm}W.                        \tag{3.2}
\]

#### Proof

Under the unbiased product measure on one four-block, local rank two has
probability \(6/16=3/8\).  Conditioning the independent block ranks on
their total being \(m\) gives the uniform measure on the middle layer.
The bivariate block enumerator

\[
 (1+4x+6yx^2+4x^3+x^4)^b                                  \tag{3.3}
\]

has its central saddle at \((x,y)=(1,1)\).  Applying the exponential
Markov bound with any fixed \(y<1\), and comparing its central coefficient
with \(\binom{2m}{m}\), gives exponential decay for
\(s\le m/16\), which is separated by a fixed linear distance from the
conditional mean \(3m/16\). \(\square\)

Choose a power of two \(\ell\) satisfying (0.4), and eventually
\(2H\le\ell<m/16\).  In every \(Q_s\) with \(s\ge\ell\), choose
\(\ell\) active directions, freeze the remaining \(s-\ell\) bits, and
thereby partition the cell into \(Q_\ell\)'s.  Put the recursive
two-sided-rainbow factor \(F_\ell\) in every such subcube.  Treat the
owners in the exceptional cells as residual singletons.

### Theorem 3.2 (exact owners and subcritical components)

The resulting atlas covers every middle owner exactly once.  Every bulk
component is an isometric \(C_{2\ell}\), is two-sided return-free through
depth \(H\), and the total component count satisfies (0.5).

#### Proof

The four-block cells partition owners, the frozen-bit subcubes partition
each bulk cell, and \(F_\ell\) partitions every subcube into cycles of
length \(2\ell\).  Its direction word is \(\pi\pi\); every interval of at
most \(\ell\) directions is repetition-free.  Hence it is safe through
\(H\le\ell/2\).  The bulk contributes exactly one component per
\(2\ell\) owners, while (3.2) bounds the singleton residual.  Equation
(0.5) follows, and it is \(o(W/H)\) by (0.4). \(\square\)

Thus mixed ownership, integrality, safety, and the component scale are
simultaneously attainable.  In particular, an \(O(H)\) compiler collar
per component has total cost \(O(HK)=o(W)\).

## 4. The same atlas has a linear Gaussian shadow deficit

For a rank-\((m-q)\) lower target in the four-block mosaic, let \(g\) be
its number of good singleton blocks and \(u\) its number of local two-set
blocks.  Fix all other block counts.  The graph from such targets to
compatible source owners is biregular, with degrees

\[
                         d_T=2^q\binom gq,
             \qquad     d_X=\binom{u+q}q.                      \tag{4.1}
\]

Consequently its exact source-to-target capacity ratio is

\[
                         R_q(g,u)
              ={2^q\binom gq\over\binom{u+q}q}.               \tag{4.2}
\]

Every owner supplies at most one directed depth-\(q\) occurrence,
irrespective of the factor installed inside its product cell.  Hence a
target type has at least

\[
                         (1-R_q(g,u))_+|{\cal A}_{g,u}|        \tag{4.3}
\]

holes.

At \(q=\lfloor A\sqrt m\rfloor\), the central conditional block profile
satisfies

\[
                         \log R_q(g,u)=-6A^2+o(1).             \tag{4.4}
\]

A fixed positive fraction \(c_A\) of the target layer lies in a small
Gaussian box on which \(R_q(g,u)\le e^{-3A^2}\).  Since

\[
                 \binom{2m}{m-q}=(e^{-A^2}+o(1))W,            \tag{4.5}
\]

summing the disjoint profile cuts (4.3) proves (0.6).  Complementation
gives the upper statement.

Subdividing a product cell into smaller cubes cannot improve this bound:
it only deletes possible target occurrences, while (4.3) already credits
every compatible source owner.  Therefore Theorem 3.2 is an explicit
integral low-component mixed-frame atlas with \(\Omega_A(W)\) missing
shadows.

This obstruction is stronger than a fixed BTK-frame counterexample.  Its
local frames vary with the owner, and all targets are potentially
reachable except an exponentially small set.  The failure is the frozen
global block profile.  A successful full-orbit rounding must move owners
between those profiles on a non-negligible mass; changing only recursive
orders or factors inside the installed cells cannot work.

## 5. Exact missing-shadow ledger

For one signed depth let \(L(T)\) be the number of selected certified
occurrences of target \(T\), let \(G=\sum_TL(T)\), and let \(N\) be the
number of targets.  Then

\[
 \boxed{
  \#\{T:L(T)=0\}
    =\sum_T(L(T)-1)_+-(G-N).}                                \tag{5.1}
\]

Indeed both sides equal \(N-|\{T:L(T)>0\}|\).  Thus correct fractional
load and even exact total occurrence count do not control holes.  At the
SCD load \(G=N\), holes equal repeat excess exactly.  For the weaker
multicover load \(G>N\), the deterministic surplus \(G-N\) must first be
subtracted from the repeat excess.

The empty-rectangle theorem supplies legal options and fractional mass.
It supplies neither the cross-profile injection needed to make the right
side of (5.1) small nor the ancestor currents in (0.3).  These are two
independent integral ledgers.

## 6. What is, and is not, obstructed

The usual determinant-two and odd-sector examples remain valid warnings,
but they are not coefficient-scale no-go theorems for the complete orbit.
In a complete safe sector, the exact pair-codegree calculation implies
that every owner set of size \(o(m^2)\) has a one-owner escape path.  The
only mod-two kernel is total sector parity, and a common forbidden support
of size \(O(H)=o(m)\) creates only \(2^{O(H)}=o(W/H)\) parity sectors.
Those lattice defects can therefore be placed in the permitted reserve.

The obstruction proved here is different:

* Theorem 2.1 is a macroscopic, cross-radius coordinate-current cut.
* Theorem 4 is a macroscopic Gaussian profile-capacity cut which survives
  exact owner tiling and the desired component count.

Neither theorem proves that every complete-orbit integral atlas fails.
They show that the exact biregular/fractional theorem omits two conditions
which are quantitatively necessary at coefficient one.

## 7. Precise surviving integral gate

A sufficient mixed-SCD orbit theorem must construct one integral family
of whole rotor packets and a structured residual such that:

1. every middle owner occurs exactly once;
2. the number of full components plus residual paths is \(o(W/H)\);
3. for every Gaussian radius and every coordinate, the inherited currents
   satisfy (0.2) against the actual residual safe-path capacities, with
   total endpoint leave \(o(W/H)\); the balanced form (0.3) is a clean
   sufficient version when the residual orbit marginals are retained;
4. the chosen packets cross the four-block and all analogous profile cuts,
   rather than remaining inside one owner-preserving mosaic; and
5. with the path-hitting definition of a shadow,
   \[
      \sum_{q\le H}(M_q^-+M_q^+)=o(W).                        \tag{7.1}
   \]

Items 1--2 are realized by Theorem 3.2, but that construction violates
items 4--5 linearly.  The fixed-radius orbit flow realizes the local form
of items 1 and 3, but not their nested all-radius form.  The complete
empty-rectangle theorem supplies the fractional entrance Hall inequalities
for item 3, but not the inherited currents or (5.1).

Accordingly the remaining problem is not ordinary hypergraph rounding and
not a return to a fixed BTK frame.  It is a **profile-moving, current-
balanced integral chain-cover theorem with whole-component variables**.
Proving that theorem would finish this mixed-SCD route; the present
fractional theorem alone does not.
