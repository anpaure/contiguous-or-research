# One-step facet rings remove the parity split and reduce q1 rounding to rainbow clique factors

## Status

This note corrects an artificial parity restriction in the short-ring
packet language.  The restriction that the source period be even is needed
only when a cyclic word is partitioned into disjoint **shift-two,
two-owner** macros.  A trace in the actual order-`d` de Bruijn graph moves
by one source letter.  Consequently a whole cyclic source ring is balanced
for every period.

Taking the period `L=d+2` therefore gives the same facet-block packet for
both parities of `d`.  Its owner blocks are complete `L`-sets of facets and
choosing its q1 roots is exactly choosing a Hamilton cycle in a clique.
For an owner-block packing, simultaneous q1-disjoint cyclic orders are
equivalent to a global rainbow Hamilton-cycle factor in a properly
edge-coloured disjoint union of cliques.  Exact colour-multiplicity and
fractional-slack ledgers are derived below.

The theorem is a reduction, not an integral factor theorem.  Moreover the
facet period has a sharp immediate-upper defect: every transition in one
packet has the same rank-`r+1` union.  Thus the packet is useful for the
owner/immediate-lower factor, but it cannot be an upper-complete carrier
without a linear-scale rethreading.  It does not prove the required rainbow
factor, upper completion, the deeper named-target decoration, or
`nu(k)<=B(k)+O(1)`.

## 1. Natural one-step trace balance

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+1=d+2,\qquad c=r-D.
\tag{1.1}
\]

Throughout the packet and clique statements assume `d>=1`, equivalently
`L>=3`.  (The depth-zero problem has no genuine q1 row and the two-vertex
``cycle'' would count its sole root twice.)

Choose

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+1,
\tag{1.2}
\]

and cyclically order

\[
 F=H-K=\{f_0,\ldots,f_{L-1}\}.
\tag{1.3}
\]

Use the cyclic source word

\[
                         A_t=K\cup\{f_t\}.
\tag{1.4}
\]

### Theorem 1.1 (all-parity facet ring)

For every `d>=1` and `L=D+1`, irrespective of the parity of `L`, the
word (1.4) is one balanced order-`d` trace component.  Its resources are

\[
 O_t=H-\{f_{t-1}\},\qquad
 Q_t=H-\{f_{t-1},f_t\},\qquad t\in\mathbb Z_L.
\tag{1.5}
\]

Thus it uses every owner in the facet block

\[
                         \mathcal O(H,K)=\{H-f:f\in F\}
\tag{1.6}
\]

once, and its q1 roots are the colours on one Hamilton cycle through those
facets.  Every proper fixed-width source interval is named-distinct.

#### Proof

In the order-`d` de Bruijn graph a length-`D` word is a directed edge from
its first `d` letters to its last `d` letters.  The successive length-`D`
windows of any cyclic source word therefore form a directed circulation
under the one-letter shift; no parity condition occurs.

A length-`D=L-1` window in (1.4) contains `K` and all private labels except
one, which proves the owner formula.  Two consecutive owners omit two
consecutive private labels, giving the root formula.  Proper cyclic
intervals of distinct private labels recover their start phase, proving
named distinctness.  \(\square\)

### Remark 1.2 (where evenness really enters)

If one insists on treating a component as a disjoint set of macros each
containing two consecutive owners, the macro starts advance by two.  An
odd period then visits every phase and counts every owner twice.  That is a
restriction on the two-owner macro packaging, not on the literal source
ring or on trace-Euler balance.  Whole-ring packet rounding may therefore
use Theorem 1.1 for both parities; a theorem whose atoms must remain
two-owner hinge roles may not.

### Proposition 1.3 (sharp immediate-upper collapse)

Every consecutive-owner upper colour in a facet ring is the same set:

\[
                         O_t\cup O_{t+1}=H.                 \tag{1.7}
\]

Consequently, a packing of `M=(W-u)/L` facet rings supplies at most `M`
distinct rank-`r+1` upper targets, whereas the full upper shore has size

\[
             \binom{2r-1}{r+1}={r-1\over r+1}W.           \tag{1.8}
\]

Even if every packet top `H` is different, the missing immediate-upper
count is at least

\[
             {r-1\over r+1}W-{W-u\over L}=\Theta(W).       \tag{1.9}
\]

Replacing `s` packet transitions by external seams can create at most `s`
additional upper colours.  Hence an `O(1)`- or `o(W)`-seam fusion cannot
turn the facet-ring packing into an upper-complete carrier.

#### Proof

Equation (1.5) gives

\[
 (H-f_{t-1})\cup(H-f_t)=H,
\]

proving (1.7).  Count one possible packet top per selected packet and use
(1.8); the seam statement is immediate because one replaced adjacency
creates only one new consecutive-owner union.  \(\square\)

The correct shortest **upper-rich** one-step ring has period `D+2`, not
`D+1`: with two private holes, consecutive owners have union `K` plus a
cyclic `(D+1)`-interval, and these `D+2` upper colours are distinct.  The
one-step language therefore still removes the parity restriction, but a
full owner/lower/upper packet should use the two-hole (`a=2`) family for
both parities.

## 2. Exact packet regularity

Regard an unoriented cyclic order in (1.3) as a packet.  Let

\[
 \mathcal O={ [n]\choose r},\qquad
 \mathcal Q={ [n]\choose r-1},\qquad
 W=|\mathcal O|=|\mathcal Q|.
\tag{2.1}
\]

### Theorem 2.1 (common owner/root degree)

Every owner and every root occurs in exactly

\[
 \boxed{
 D_0=(r-1){r\choose D}{D!\over2}
     ={r\choose2}{r-1\choose D-1}(D-1)! }
\tag{2.2}
\]

facet-ring packets.  Uniform packet weight `1/D_0` is an exact fractional
perfect factor on the combined owner/root shore.

For every incident pair `Q subset O`,

\[
 {d(O,Q)\over D_0}={2\over r}.
\tag{2.3}
\]

#### Proof

For a fixed owner `O`, choose `H-O` in `r-1` ways, choose the core
`K subset O` in `binom(r,D)` ways, and cyclically order the `L=D+1`
private labels in `D!/2` unoriented ways.

For a fixed root `Q`, choose the two labels of `H-Q` in `binom(r,2)`
ways, choose `K subset Q` in `binom(r-1,D-1)` ways, and require the two
new labels to be adjacent in the cycle.  Contracting their ordered pair
gives `(D-1)!` unoriented choices.  The two expressions agree by direct
cancellation.

If `O=Q+x`, choose `H-O`, choose `K subset Q`, and require `x` to be
adjacent to `H-O`.  This gives

\[
 (r-1){r-1\choose D-1}(D-1)!,
\]

whose ratio to (2.2) is `2/r`.  \(\square\)

The pair-codegree table is therefore the `a=1` table of the
parity-unified two-owner calculation for every `d`; only its macro
interpretation changes.

## 3. The rainbow clique equivalence

Let `mathcal M` be an owner-block matching: its members are pairs `(H,K)`
whose facet sets (1.6) are pairwise disjoint.  For every block `B=(H,K)`,
make a clique `C_B` on the `L` owner vertices `H-f`, `f in F`.  Colour the
edge joining `H-f` and `H-g` by

\[
                         \kappa_B(fg)=H-\{f,g\}\in\mathcal Q.
\tag{3.1}
\]

Let `G_M` be the disjoint union of these cliques.

### Lemma 3.1 (the colouring is proper)

Every colour class of `G_M` is a matching.

#### Proof

Inside one clique, distinct edges incident with `H-f` omit distinct
pairs, so their root colours differ.  If two edges in different cliques
had the same colour `Q` and a common owner endpoint, then that owner would
belong to both owner blocks, contradicting that `mathcal M` is a matching.
Equivalently, every edge of colour `Q` pairs two distinct owners from the
`r`-set of owners incident with `Q`, and the block matching makes those
pairs disjoint.  \(\square\)

### Theorem 3.2 (packet ordering equals a rainbow Hamilton factor)

Choosing one cyclic order for every owner block in `mathcal M` so that no
q1 root is repeated is equivalent to choosing one Hamilton cycle in every
clique `C_B` such that the union of all chosen cycles is rainbow in the
colouring (3.1).

If the owner-block matching leaves exactly `u` owners, then a rainbow
choice uses `W-u` roots and leaves exactly `u` roots.

#### Proof

A cyclic order `f_0,...,f_(L-1)` of `F` orders the clique vertices
`H-f_t`.  Its consecutive clique edges have colours
`H-{f_t,f_(t+1)}`, exactly the q1 roots in (1.5).  This is a bijection
between unoriented cyclic packet orders and Hamilton cycles of `C_B`.
Across blocks, root-disjointness is precisely rainbowness.  Each selected
cycle has `L` edges, the same as the number of covered owners in its block,
which proves the leave identity.  \(\square\)

This reduction removes state balance from the q1 rounding problem: state
balance is automatic inside each clique packet.  The remaining q1 issue is
a rainbow factor in a proper edge-colouring.

## 4. Exact colour-load ledger

For a root colour `Q`, let

\[
 t_Q=|\{B\in\mathcal M:Q\text{ colours an edge of }C_B\}|.
\tag{4.1}
\]

### Proposition 4.1

The colour multiplicities satisfy

\[
 t_Q\le {r\over2},
\qquad
 \sum_{Q\in\mathcal Q}t_Q
             ={(W-u)(L-1)\over2}.
\tag{4.2}
\]

Hence their average is

\[
                         \bar t={L-1\over2}\left(1-{u\over W}\right).
\tag{4.3}
\]

#### Proof

Every occurrence of colour `Q` pairs two of the `r` owners containing
`Q`; Lemma 3.1 makes these pairs disjoint, proving the first bound.  Every
one of the `(W-u)/L` cliques contributes `binom(L,2)` coloured edges.
Double count colour occurrences to obtain (4.2)--(4.3).  \(\square\)

There is a sharp natural slack scale.  Since `L` is even or odd according
to `D+1`, suppose first that `L` is even and put

\[
                         h={L-2\over2}.
\tag{4.4}

Ignoring block divisibility for one line, the threshold value is

\[
                         u={W\over L-1}
\tag{4.5}

and then `bar t=h`.  An actual block packing also requires

\[
                         u\equiv W\pmod L.                 \tag{4.5a}
\]

Accordingly, let `u_*` be the least integer satisfying (4.5a) and
`u_*>=W/(L-1)`.  Then

\[
                  {W\over L-1}\le u_*<{W\over L-1}+L.     \tag{4.5b}
\]

A packing with `u=u_*` and `t_Q<=h` has the exact colour-deficit ledger

\[
 \sum_Q(h-t_Q)={ (L-1)u_*-W\over2}=O(L^2).                \tag{4.5c}
\]

Thus the optimally balanced profile is `h` everywhere apart from only
`O(L^2)` units of total rounding deficit.  If the unrounded value (4.5)
already obeys (4.5a), the deficit in (4.5c) is zero.

For such a balanced packing, assigning weight

\[
                         {2\over L-1}
\tag{4.6}

to every edge of every clique gives degree two at every covered owner and
colour load at most

\[
                         {2h\over L-1}={L-2\over L-1}<1.
\tag{4.7}

It is therefore an exact fractional rainbow 2-factor with precisely the
`u` units of global root slack required by Theorem 3.2.

For odd `L`, `(L-1)/2` is already integral.  Subject to the necessary
block divisibility `L|W`, one may take `u=0` and the perfectly balanced
profile

\[
                         t_Q=(L-1)/2.
\]

Without `L|W`, the scalar minimum is instead the least nonnegative
`u congruent W (mod L)`; in particular `u<L`.  This is only an `O(L)`
divisibility residue and is unrelated to source-state parity.

Thus the two parities merely have different optimal leave arithmetic:
odd `L` permits zero scalar leave, while even `L` naturally exposes the
`W/(L-1)` reserve in (4.5).  Neither is a source-state obstruction.

## 5. Exact surviving integral theorem

The all-parity owner/immediate-lower factor can now be attacked in two
explicit stages.

1. **Balanced facet-block packing.**  Choose pairwise owner-disjoint facet
   blocks covering all but `O(W/d)` owners and with every colour
   multiplicity `t_Q=O(L)` (ideally the sharp profile in Section 4).
2. **Rainbow clique factor.**  In the resulting properly edge-coloured
   disjoint union of `K_L`'s, choose one Hamilton cycle per clique with no
   repeated colour, leaving the same `O(W/d)` roots.

The uniform packet fractional factor proves the joint fractional version
of these rows, but it does not prove either integral assertion.  A random
choice of Hamilton cycles has approximately Poisson colour load and hence
does not suffice.  A proof needs alternating colour switchers or a robust
rainbow-factor theorem at the threshold multiplicity `Theta(L)`.

After this owner/lower-q1 rounding, one must still overcome Proposition
1.3, install the pure pull decorations for all deeper named targets, and
fuse the packet cycles.  The benefit of the reduction is exact but scoped:
the old `a=1/a=2` parity split is gone from trace balance, and lower-q1
rounding is now a concrete rainbow Hamilton-factor problem rather than an
opaque `2L`-resource packet matching.  For a full upper-rich packet factor,
the all-parity `a=2` one-step family is the appropriate replacement.
