# The MMM defect has an exact nine-turn recurrence, and private packet
# lifting is a second Hall problem

Date: 2026-08-01  
Lane: K / bounded-defect noncanonical route  
Status: independent symbolic audit, exact private-socket lifting theorem,
exact finite-state physical induction criterion, and a sharp capacity
obstruction to scaling pairwise-private translated packets.  A uniform
bounded leave is not proved.

## 0. Outcome

The standard lexical/MMM turn defect is now characterized exactly.  With
paper parameter `n`, its common lower/upper defect order is

\[
 D_n={2n+1\over3}[z^{n-1}](C(z)-1)^3
     ={2n+1\over n-1}{2n-2\choose n-4}.              \tag{0.1}
\]

This is the same number as the lexical missing-turn count audited in
`MATH_AUDIT_K_R_LEXICAL_GMN_UPPER_OBSTRUCTION_20260801.md`.  The first
values are

\[
                         D_4=3,\qquad D_5=22,\qquad D_6=117.          \tag{0.2}
\]

A padded `Q9` block consists of three lower and three upper defects and is
recognized intrinsically by a five-part partition.  If `nu_n` is the
maximum number of pairwise defect-disjoint blocks, then

\[
                              \rho_n=D_n-3\nu_n                     \tag{0.3}
\]

is the exact balanced service leave.  Thus "all but `O(1)` defects pack"
is exactly `rho_n=O(1)`.

The currently proved finite data are

\[
                              \rho_4=0,\qquad \rho_5=1,
                              \qquad \rho_6\ge6.                    \tag{0.4}
\]

They neither prove nor refute a bounded leave.

There is, however, a decisive asymptotic restriction on the most literal
implementation.  If the translated `Q9` packets are pairwise private in
their negative turn resources, then their leave is not bounded: it is
asymptotically at least two thirds of the raw defect bank.  Even dropping
negative-resource privacy while retaining vertex-disjoint literal cubes
leaves a positive fraction for all sufficiently large `n`.  Thus any
bounded-leave construction must use macroscopic collateral recycling,
physical overlap, a more efficient atom, or a normalized recursive state.

This note adds the exact physical lifting interface.  After a block matching
is chosen, assigning its blocks to pairwise resource-disjoint guarded
translated-`C10` sockets is ordinary Hall.  This is a second, independent
matching row.  A finite residual-state induction gives a literal
`B+O(1)` central palette theorem if both the block transition matching and
this socket Hall row hold at every step.  Neither row is presently proved
uniformly for the standard MMM endpoint family.

Consequently the answer to the requested test is:

\[
 \boxed{\begin{gathered}
 \text{exact recurrence and exact conditional }O(1)\text{ theorem: yes;}\\
 \text{pairwise-private padded cubes: asymptotically impossible;}\\
 \text{globally coupled bounded packing: open.}
 \end{gathered}}                                                   \tag{0.5}
\]

## 1. Exact raw-defect recurrence

The raw missing turns are cyclic words

\[
                              1a1b1c,                              \tag{1.1}
\]

where `a,b,c` are three nonempty Dyck words with total semilength `n-1`.
Writing `E=C-1=zC^2`, double-counting a missing cyclic word with one of its
three separators distinguished gives

\[
                         3D_n=(2n+1)[z^{n-1}]E^3.                  \tag{1.2}
\]

Lagrange inversion yields (0.1).  Equivalently,

\[
 D_n=(2n+1){(n-2)(n-3)\over(n+1)(n+2)}
                    \operatorname {Cat}_{n-1}.                    \tag{1.3}
\]

Direct cancellation gives the exact recurrence

\[
 {D_{n+1}\over D_n}
 = {2(2n-1)(2n+3)(n-1)
          \over(n-3)(n+3)(2n+1)}.                                \tag{1.4}
\]

In particular,

\[
 D_{n+1}-4D_n
 =D_n{-4n^2+58n+42\over(n-3)(n+3)(2n+1)}.                        \tag{1.5}
\]

The factor in (1.5) is `-2/n+O(n^-2)`, so its absolute value is unbounded.
Therefore the child defect cannot be four disjoint tagged parent copies plus
or minus only `O(1)` targets.  A successful recursion must rebundle a
macroscopic cross-sector bank or carry a normalized state whose defect is
not the raw four-copy lift.

Peak insertion into any of the three Dyck components gives a raw-defect
embedding from `n` to `n+1`; deleting a peak from a component of semilength
at least two reverses it.  This is a grammar morphism only.  It does not say
that the defect set of a separately Hamiltonized child endpoint is the
literal padded image of its parent.

## 2. The exact padded-block hypergraph

Let `Omega` have order `2n+1`.  Complement the upper defect shore so both
shores consist of `(n-1)`-sets.  A block is exactly a partition

\[
 \Omega=H\mathbin{\dot\cup}G\mathbin{\dot\cup}
              Q_0\mathbin{\dot\cup}Q_1\mathbin{\dot\cup}Q_2,
 \qquad |H|=|G|=n-4,\quad |Q_i|=3,                               \tag{2.1}
\]

using

\[
             H\cup Q_0,H\cup Q_1,H\cup Q_2                       \tag{2.2}
\]

on the lower shore and

\[
             G\cup Q_0,G\cup Q_1,G\cup Q_2                       \tag{2.3}
\]

on the complemented upper shore.  Complementing (2.3) back gives the three
pairwise unions of (2.2), so this is equivalent to the intrinsic `Q9`
recognition rule.

For the unrestricted two complete shores, the block hypergraph has

\[
 |\mathcal B_n^{\rm all}|
 ={(2n+1)!\over(n-4)!^2(3!)^3 3!}                                \tag{2.4}
\]

edges and degree

\[
 d_n=10{n-1\choose3}{n+2\choose6}
     ={1\over2}{n-1\choose3}^2{n+2\choose3}.                      \tag{2.5}
\]

Its maximum normalized codegree is `O(n^-3)`.  These ambient parameters do
not pass automatically to the endpoint-induced defect hypergraph: the
audited `n=6` instances already have block-isolated vertices.  Hence a
regular-hypergraph nibble cannot be applied without a new induced
supersaturation theorem.

### Proposition 2.1 (exact bounded-leave alternatives)

Either of the following is sufficient for `rho_n<=b`.

1. Every balanced block-free induced subbank has order at most `b` on each
   shore.
2. There is a block matching whose balanced leave has order at most `b`.

The first condition makes every inclusion-maximal block matching satisfy the
second.

#### Proof

A block removes three targets on each shore, so every matching leave is
balanced.  The leave of a maximal matching contains no block.  This proves
the first implication; the second is the definition (0.3). \(\square\)

Condition 1 is a genuine induced expansion statement.  Ambient degree and
codegree alone do not imply it.

### Theorem 2.2 (pairwise-private packet capacity obstruction)

Put

\[
 N_n={2n+1\choose n},\qquad P_n={2n+1\choose n-1}.                 \tag{2.6}
\]

Here `N_n` is the number of turn occurrences on either rail and `P_n` is
the turn-palette order.  Since exactly `P_n-D_n` colours occur, the total
surplus-occurrence reserve on either shore is

\[
 S_n=\sum_c(\mu(c)-1)^+
     =N_n-(P_n-D_n)
     =D_n+{2P_n\over n}.                                          \tag{2.7}
\]

Suppose `p` translated `Q9` packets are pairwise private in their negative
turn resources.  Then

\[
 9p\le S_n,\qquad
 \rho_n=D_n-3p\ge D_n-3\left\lfloor{S_n\over9}\right\rfloor.      \tag{2.8}
\]

Before rounding, this gives

\[
 \rho_n\ge {2D_n+P_n-N_n\over3}
 =P_n{(n-1)(n-8)\over3n(2n-1)}.                                  \tag{2.9}
\]

In particular the lower bound is positive for `n>=9` and

\[
              {\rho_n\over D_n}\longrightarrow {2\over3}.        \tag{2.10}
\]

Even without negative-resource privacy, pairwise vertex-disjoint literal
packets obey

\[
 15p\le N_n,\qquad
 \rho_n\ge D_n-3\left\lfloor{N_n\over15}\right\rfloor.            \tag{2.11}
\]

The unfloored right side of (2.11) is

\[
 P_n{n^2-31n+34\over10n(2n-1)},                                  \tag{2.12}
\]

which is positive for every `n>=30` and is asymptotic to `P_n/20`.

#### Proof

The exact ratios

\[
 {P_n\over N_n}={n\over n+2},\qquad
 {D_n\over P_n}={(n-2)(n-3)\over2n(2n-1)}                       \tag{2.13}
\]

give (2.7).  One authenticated translated packet is three
vertex-disjoint `C10` switches.  Each switch uses five rail occurrences,
has three negative and three positive turn tokens on each shore, and
repairs one lower and one upper defect.  Thus one packet consumes fifteen
rail occurrences and nine private negative tokens while repairing three
defects.  Summing these disjoint consumptions proves (2.8) and (2.11).
Substitution of (2.7) and (2.13), followed by cancellation, gives
(2.9) and (2.12).  \(\square\)

The first two exact calibrations are

\[
\begin{array}{c|rrrr|r}
n&N_n&P_n&D_n&S_n&\text{private leave floor}\\ \hline
8&24310&19448&2431&7293&1\\
9&92378&75582&10374&27170&1320.
\end{array}                                                       \tag{2.14}
\]

For a desired leave `rho`, (2.8) also forces at least

\[
 \bigl[3(D_n-\rho)-S_n\bigr]_+
   =\bigl[2D_n-(N_n-P_n)-3\rho\bigr]_+                           \tag{2.15}
\]

negative-token uses to be supplied by cross-packet circulation.  Thus the
private-packet theorem below remains exact for a fixed bounded catalogue,
but it cannot be the bulk all-`n` mechanism.

### Proposition 2.3 (two failed scalar recursion shortcuts)

First, marked peak insertion obeys

\[
 \sum_{w\in\mathcal D_{n+1}}p(w)=(2n+1)D_n,\qquad
 { (2n+1)D_n\over D_{n+1}}
 ={(2n+1)^2(n-3)(n+3)\over
   2(2n-1)(2n+3)(n-1)}\sim {n\over2}.                             \tag{2.16}
\]

Hence raw defects have many admissible parents; a glued endpoint must
recurse the full turn-load vector and the signed glue derivatives, not only
its hole set.

Second, fix a coordinate `x` and take, on each complemented shore, all raw
defects containing `x`.  This is a balanced block-free pair of banks of
order

\[
 {n-1\over2n+1}D_n={2n-2\choose n-4}.                            \tag{2.17}
\]

Indeed, within a `Q9` block the incidence count of `x` across either
three-set shore is `(3,0)`, `(0,3)`, or `(1,1)` according as `x` lies in
`H`, `G`, or a `Q_i`; it is never `(3,3)`.  Thus bounded balanced
independence cannot prove the desired packing.  This does not obstruct a
near-perfect matching in the full block hypergraph; it closes only that
proposed supersaturation shortcut.

## 3. Private translated packets require a second Hall theorem

One abstract `Q9` block is physically serviced by a translated rank-tight
cube of three `C10` switches.  Its full resource footprint includes the old
and new factor edges, both signed turn banks, the augmented linkage module,
topology ports, run boundary, deeper providers, and compiler guards.

Fix a defect-disjoint block matching `M`.  Let `S` be a predeclared family
of pairwise resource-disjoint physical sockets.  For every `B in M`, let
`L(B) subseteq S` be the sockets in which a literal guarded translated cube
realizes exactly the six defect colours of `B`.  A socket realization is
required to keep its complete footprint inside that socket and to have a
legal Boolean cube of subset states.

### Theorem 3.1 (private-socket Hall theorem)

All blocks of `M` can be realized simultaneously by pairwise private
translated cubes if and only if

\[
                  \left|\bigcup_{B\in X}L(B)\right|\ge |X|
                              \qquad(X\subseteq M).                 \tag{3.1}
\]

Under (3.1), toggling all selected cubes repairs exactly the `3|M|`
defects on each shore and preserves every declared guard.

#### Proof

Condition (3.1) is Hall's theorem for the bipartite graph `M--S`.  A
matching assigns distinct sockets to all blocks.  Socket disjointness makes
the complete physical footprints disjoint, so signed derivatives,
augmenting modules, subset topology and guards superpose.  Each cube repairs
its three lower and three upper block colours.  Conversely, any private
simultaneous realization uses a distinct socket for every block and gives
the Hall matching. \(\square\)

This theorem is exact only after the block matching `M` is fixed.  Choosing
the blocks and sockets simultaneously is a packing problem on atoms
`(B,s)` with six defect resources plus one socket resource; ordinary Hall
on the projected defect graph is not sufficient.

The theorem also separates **service** from **physical privacy**.  Crown
containment gives a palette service matching inside every abstract block,
but does not place its three `C10` circuits in the current factor, make their
augmenting routes disjoint, or preserve downstream guards.

## 4. Exact finite-state physical induction

Fix an absolute integer `b` and a finite state set `Sigma`.  A state
`sigma in Sigma` contains

* balanced lower/upper residual banks of order at most `b`;
* their `F_3` incidence syndrome;
* the bounded augmented-linkage, topology, residence, deeper-provider, and
  compiler boundary data; and
* a bank of declared pairwise private sockets.

### Theorem 4.1 (bounded physical regeneration)

Suppose that at every transition `n->n+1` and for every reachable state
`sigma`:

1. lifted parent blocks remain literal legal blocks;
2. the newly born defect bank together with the lifted old residual has a
   block matching leaving a residual state `sigma' in Sigma`;
3. the chosen block matching satisfies the private-socket Hall condition
   (3.1); and
4. the installed cubes export exactly the guarded boundary state declared
   by `sigma'`.

Then every descendant has a physical repair packet leaving at most `b`
turn defects per shore and bounded exported guard state.

#### Proof

Induct on the dimension.  Lift the parent's installed block cubes and its
residual state.  Item 2 partitions the complementary birth/residual bank
into new blocks and the next bounded leave.  Theorem 3.1 realizes those
blocks in disjoint sockets.  Items 1 and 4 make the old and new physical
supports compatible and identify their union with the declared next state.
The leave and every exported coordinate are bounded by the finite state
definition. \(\square\)

If the remaining bounded turn defects can be appended or repaired by a
bounded terminal catalogue, Theorem 4.1 supplies the **central palette**
part of a `B(k)+O(1)` recurrence.  It does not by itself bound middle-owner,
deep-shadow, residence, or common-cap/compiler defects unless those are
explicit coordinates of `Sigma`.

## 5. Exact obstructions and finite boundary data

The following are proved and prevent a stronger conclusion.

1. Equation (1.5) rules out four tagged parent copies plus bounded scalar
   correction.
2. At `n=5`, only six of the 112 Hamilton gluing-tree endpoints admit seven
   disjoint blocks.  Each leaves one nonnested defect pair.  A crossed crown
   closes its service Hall, but not a universal literal padded packet.
3. At `n=6`, the canonical endpoint has 117 defects, block-isolated vertices,
   and no 38-block packing.  The best audited one-glue neighbour retains an
   isolated pair and also has no 38-block packing.  No 37-block witness is
   frozen, so only `rho_6>=6` is authoritative.
4. The reduced crossed-rerouter coordinate types at `n=5` and `n=6` are
   distinct.  One fixed padded residual gadget is not a closed basis.
5. Root-level palette service does not imply physical packet availability.
   In the audited `n=5`/`ML(11)` factor, every crossed rerouter has a required
   service pair absent from the root-alternating `C10` catalogue.  Longer or
   state-dependent compounds remain possible.
6. Every block has zero syndrome

   \[
          \sum_{A\in B^-}{\mathbf1}_A-
          \sum_{C\in B^c}{\mathbf1}_C=0
                         \quad\hbox{in }\mathbb F_3^\Omega.          \tag{5.1}
   \]

   Hence the residual state must carry the full-bank syndrome.  Count
   congruence and syndrome are necessary but not sufficient: at `n=6` they
   permit a three-pair leave while the exact 38-block packing is absent.

These are scoped obstructions to the stateless standard endpoint and the
declared packet catalogues.  They do not refute a nonstandard prospectively
selected factor, a relational packet family with varying active coordinates,
or a stateful normalized recursion.

## 6. Sharp remaining theorem

The weakest exact positive alternatives are now:

1. construct a prospectively selected endpoint whose normalized defect bank
   is already bounded;
2. construct a finite residual-state transition table satisfying Theorem
   4.1 with macroscopic collateral recycling between its packets; or
3. prove bounded containment-matching deficiency and realize its bounded
   augmenting paths by guarded physical packets after a globally coupled
   bulk circulation.

The private-socket Hall row (3.1) remains the exact terminal interface for
any bounded residual catalogue, but Theorem 2.2 rules it out as the private
bulk mechanism.  Otherwise an abstract `Q9` matching is only a palette
assignment.  No unconditional `B+O(1)` or `nu=B` conclusion is claimed.
