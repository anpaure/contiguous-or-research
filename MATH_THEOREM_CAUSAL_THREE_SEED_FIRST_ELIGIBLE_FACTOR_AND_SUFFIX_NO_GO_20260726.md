# Causal three-seed first-eligible factors: exact packetization and the surviving suffix Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

There are two separate statements, one positive and one negative.

1. A seed may be chosen causally at every first-eligible stage.  More
   precisely, the requested one of the three cyclic `B_4` seeds may depend
   on every previously frozen block and on an arbitrary finite prefix state,
   provided that the transition after a successful block is independent of
   which of the four states of the chosen seed occurred.  The retained
   middle owners then split canonically into Cartesian `Q_2^r=Q_{2r}`
   packets.  The scan leave is exponentially small, and the recursive
   Hamming factor gives an exact integral physical cycle factor in every
   packet.
2. This causal freedom does not repair the fixed-atlas Gaussian Hall
   obstruction.  Almost every packet finds all `r=o(m)` selected blocks
   before a terminal positive-density suffix of the atlas.  Every component
   in such a packet freezes that suffix.  A hypergeometric threshold cut
   therefore forces `Omega(W)` missing lower targets and `Omega(W)` missing
   upper targets at every fixed Gaussian depth `q=A sqrt(m)`.

The negative statement is not the tempting comparison

\[
  4^s\binom{s}{k}\quad\hbox{versus}\quad
  4^s\binom{s}{k+q}.                                  \tag{0.1}
\]

That comparison is a genuine invariant census, but unequal shore sizes do
not by themselves imply uncovered vertices: several occurrences may share
one vertex on the smaller shore.  The valid obstruction below is stronger.
It bounds occurrence capacity by the number of middle owners in a suffix
event, and hence survives arbitrary cross-packet repetitions, integral
component mixing, and the corresponding fractional owner cover.

Thus a prefix automaton can give an exact factor, but it cannot make the
Gaussian signed Hall defect `o(W)` while all physical moves remain inside
one fixed ordered block atlas.  A successful construction must recouple
coordinates across the old `B_4` blocks and transport through every
positive-density suffix.

## 1. The three local seeds

On a four-set `B={1,2,3,4}`, let

\[
 \begin{aligned}
 M_0&=12\mid34,& \mathcal A_0&=\{13,14,23,24\},\\
 M_1&=13\mid24,& \mathcal A_1&=\{12,14,23,34\},\\
 M_2&=14\mid23,& \mathcal A_2&=\{12,13,24,34\}.
 \end{aligned}                                         \tag{1.1}
\]

Thus `A_c=binom(B,2)\setminus M_c`.  Orient the three physical squares as

\[
 \begin{aligned}
 C_0&=(13,14,24,23),\\
 C_1&=(14,12,23,34),\\
 C_2&=(12,13,34,24).
 \end{aligned}                                         \tag{1.2}
\]

In each cycle the four lower edge intersections are the four singletons
and the four upper edge unions are the four triples, each exactly once.
Also

\[
       |\mathcal A_c|=4,
       \qquad |\mathcal A_c\cap\mathcal A_d|=2
       \quad(c\ne d).                                  \tag{1.3}
\]

The overlap in (1.3) imposes a useful causality condition.

### Lemma 1.1 (the fresh-block seed is predictable)

Suppose a deterministic rule, after fixing the complete past, maps the
fresh local state `x subseteq B` either to `skip` or to a seed
`c in Z_3`.  Suppose selecting seed `c` creates a literal packet in which
`x` is subsequently allowed to vary through all of `A_c`, without changing
the selected index or the selected seed.  Then at most one seed can be
selected at the current scan state.  In particular that seed is determined
before the fresh block is exposed.

#### Proof

If both `c` and `d` could be selected, packet stability would force the rule
to equal `c` on all of `A_c` and to equal `d` on all of `A_d`.  Their
intersection is nonempty by (1.3), a contradiction.  \(\square\)

Thus causality does not mean that the seed word must be fixed in advance.
It may depend arbitrarily on the frozen prefix.  It only means that the
seed requested from the next fresh block is predictable.

## 2. A general causal scan and its exact packet partition

Partition the available coordinates, apart from an `o(m)` anchor and a
bounded remainder, into ordered four-blocks

\[
                         B_1<B_2<\cdots<B_b,
              \qquad b=(1/2+o(1))m.                 \tag{2.1}
\]

Let `S` be any state space.  At scan stage `j`, the current state is
`s in S`, and a seed

\[
                         \theta_j=\vartheta_j(s)\in\mathbb Z_3          \tag{2.2}
\]

is requested.  A fresh block with state `x` is selected precisely when
`x in A_{theta_j}`.  On failure, the state may be updated by an arbitrary
map

\[
                         s\longmapsto D_j(s,x).       \tag{2.3}
\]

On success, require only that the update

\[
                         s\longmapsto E_j(s)          \tag{2.4}
\]

is independent of the particular `x in A_{theta_j}`; then advance from
stage `j` to `j+1`.  This includes a `Z_3` prefix automaton, a hash of an
initial frozen anchor, or any deterministic finite-state combination of
the two.

Stop after `r` successful blocks.  For a retained owner `X`, write

\[
 I(X)=(i_1<\cdots<i_r),\qquad
 \theta(X)=(\theta_1,\ldots,\theta_r).               \tag{2.5}
\]

Freeze every coordinate outside the selected blocks, and inside selected
block `i_j` allow all four states of `A_{theta_j}`.  Denote the resulting
set by `P(X)`.

### Theorem 2.1 (causal context stability)

For every `Y in P(X)`,

\[
           I(Y)=I(X),\qquad \theta(Y)=\theta(X),
           \qquad P(Y)=P(X).                         \tag{2.6}
\]

Consequently the retained owners are partitioned into disjoint packets

\[
 P\cong
 \mathcal A_{\theta_1}\times\cdots\times
 \mathcal A_{\theta_r}\cong Q_2^r=Q_{2r}.          \tag{2.7}
\]

#### Proof

Proceed through the scan in chronological order.  Every skipped block is
frozen, so the failure transitions (2.3) and all states reached through
them remain unchanged.  At a selected block, every allowed replacement
still lies in the same requested square.  The success update (2.4) is
independent of the chosen member of that square, so the post-success state
is unchanged.  Induction over the `r` successes proves that the requested
seeds, selected indices, and all later scan states coincide.  The packet
definition then coincides as well.  \(\square\)

### Lemma 2.2 (adaptive eligibility is exactly Bernoulli)

Under independent fair coordinate bits, the success indicators on fresh
four-blocks are independent Bernoulli variables of parameter `1/4`, even
though the requested seeds are chosen adaptively from the past.

#### Proof

Conditional on every preceding exposure and state, the fresh block is
uniform on its sixteen subsets.  By Lemma 1.1 exactly one seed is requested,
and its support has four members.  Thus the conditional success probability
is always `1/4`.  Iterating conditional probabilities gives the product
law for every finite success/failure word.  \(\square\)

If `r=o(m)`, a Chernoff bound therefore gives probability
`exp(-Omega(m))` of finding fewer than `r` successes among the `Theta(m)`
fresh blocks.  Conditioning on total rank `m` costs at most

\[
                   {2^{2m}\over\binom{2m}{m}}=O(\sqrt m),        \tag{2.8}
\]

so the middle-layer leave is still

\[
                              e^{-\Omega(m)}W.        \tag{2.9}
\]

## 3. Exact physical cycles and the reservoir completion

Put `h=2r` and assume `h` is a power of two.  In each packet (2.7), use
the recursive exact Hamming `C_{2h}`-factor of `Q_h`, with the two
directions of each local square installed as sibling leaves.  Every
abstract edge is a physical Johnson edge by (1.2).  Hence:

### Theorem 3.1 (exact causal mixed-seed factor)

The retained middle owners have an exact integral owner-disjoint factor
into physical `C_{2h}=C_{4r}` cycles.  Every component has its ordinary
cyclic phase colouring, and for every `q<=r` both signed depth-`q` shadow
maps are injective inside each packet.

#### Proof

The packet partition is Theorem 2.1.  The exact Hamming factor partitions
each `Q_h`.  A window of at most `r` Hamming directions touches each local
sibling pair at most once.  On a touched block, (1.2) has four distinct
singleton lower labels and four distinct triple upper labels; on an
untouched block the middle state is recorded literally.  Either signed
target therefore recovers the starting owner inside the packet.  Orienting
each resulting physical cycle gives its phase colouring.  \(\square\)

There is also a genuine common-owner completion of the three local seed
choices.  Take a reservoir square `Y=Q_2` on four new coordinates and put

\[
                       \mathcal V=\binom B2\mathbin\square Y,
                       \qquad |\mathcal V|=24.        \tag{3.1}
\]

For seed `c`, the four fibres `C_c times {y}` and the two reservoir fibres
`{e} times Y` for `e in M_c` partition `V` into six physical `C_4`'s.
Tensoring `r` such carriers gives, for every causal seed word, an exact
resolution of the same `24^r` owners into `6^r` physical `Q_{2r}` cells.
Applying the preceding Hamming factor in every cell gives an exact retile.

No common four-colouring of owners is compatible with all three local
resolutions simultaneously: at a fixed reservoir state the three special
cycles force all six members of `binom(B,2)` to have different colours.
This does not obstruct a chosen causal resolution.  One colours the cycles
of that resolution cell by cell.  It only forbids treating all three
resolutions as simultaneous states of one common `Z_4`-coloured switch.

## 4. The true invariant: a frozen positive-density suffix

The exact factor above remains localized.  Let `R` be the union of the
terminal quarter of the ordered complete blocks.  In the four-block model,

\[
                         {|R|\over2m}\longrightarrow {1\over4}.          \tag{4.1}
\]

Call a packet normal if all its selected blocks precede `R`.

### Lemma 4.1 (almost every causal packet is normal)

For `r=o(m)`, the number `U_m` of middle owners which are in the scan leave
or in a nonnormal packet satisfies

\[
                              U_m=e^{-\Omega(m)}W.     \tag{4.2}
\]

#### Proof

Before the terminal quarter there remain `Theta(m)` fresh blocks.  By
Lemma 2.2 their success count is binomial with a positive linear mean,
whereas only `r=o(m)` successes are required.  Chernoff and (2.8) prove
the assertion.  Packet stability makes normality constant on each packet.
\(\square\)

The same statement holds for the 24-owner eight-coordinate carrier.  Its
common support has density `24/2^8=3/32` in a fresh eight-block, still a
fixed positive constant, so all `r=o(m)` carriers are found before the
terminal quarter except on `e^{-Omega(m)}W` owner mass.

### Lemma 4.2 (suffix conservation)

For every start `X` in a normal packet, every depth `q`, and both signs,

\[
             \tau_q^-(X)\cap R=X\cap R,
             \qquad
             \tau_q^+(X)\cap R=X\cap R.             \tag{4.3}
\]

#### Proof

All vertices of the component agree outside its selected blocks, and a
normal packet selects no coordinate of `R`.  Intersections and unions of
consecutive vertices retain the common restriction.  \(\square\)

This invariant is insensitive to the seed word, the prefix automaton, the
recursive direction order, the reservoir resolution, and integral or
fractional mixing of whole components inside normal packets.

## 5. The Gaussian suffix Hall cut

Write `s=|R|` and, for an integer `a`, define

\[
 \begin{aligned}
 \mathcal Z_{q,a}^-&=
 \{T\in\tbinom{[2m]}{m-q}:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+&=
 \{T\in\tbinom{[2m]}{m+q}:|T\cap R|\ge s-a\},\\
 B_a&=\bigl|\{X\in\tbinom{[2m]}m:|X\cap R|\le a\}\bigr|.
 \end{aligned}                                         \tag{5.1}
\]

By middle complementation, `B_a` is also the number of middle owners with
`|X cap R|>=s-a`.

### Proposition 5.1 (exact component-capacity inequality)

Every integral exact-owner selection of whole causal packet components
satisfies

\[
             M_q^\pm\ge |\mathcal Z_{q,a}^\pm|-B_a-U_m.          \tag{5.2}
\]

The same inequality holds for a fractional component cover whose total
weight at every retained owner is one.

#### Proof

For a normal lower occurrence, Lemma 4.2 says that membership in
`Z^-_{q,a}` is exactly the middle-owner event `|X cap R|<=a`.  Summing one
occurrence per owner therefore gives total capacity at most `B_a`.
For the upper sign use the complementary owner event.  Give every
exceptional owner the most favourable possible occurrence, adding at most
`U_m`.  Repeated occurrences of one target do not increase the number of
distinct targets hit.  In the fractional case, summing component weights
first gives the same identity because those weights total one at every
owner.  \(\square\)

Fix `A>0`, put `q=floor(A sqrt(m))`, and set

\[
                         v={3\over32},
 \qquad
                         a_m=\left\lfloor{s\over2}-x\sqrt{vm}\right\rfloor.
                                                               \tag{5.3}
\]

The hypergeometric central limit theorem gives

\[
 \begin{aligned}
 {B_{a_m}\over W}&\longrightarrow\Phi(-x),\\
 {|\mathcal Z_{q,a_m}^\pm|\over W}
 &\longrightarrow e^{-A^2}\Phi\bigl(A\sqrt{2/3}-x\bigr).
 \end{aligned}                                         \tag{5.4}
\]

Indeed the suffix has middle mean `s/2`, lower-layer mean
`s/2-(A/4+o(1))sqrt(m)`, and variance `(3/32+o(1))m`; the upper statement
is complementary.  Also

\[
               {\binom{2m}{m-q}\over\binom{2m}{m}}
                    \longrightarrow e^{-A^2}.         \tag{5.5}
\]

For sufficiently large fixed `x`, Mills' ratio gives

\[
 e^{-A^2}\Phi\bigl(A\sqrt{2/3}-x\bigr)>\Phi(-x).     \tag{5.6}
\]

Fix such an `x=x_A` and call the positive difference `kappa_A`.
Proposition 5.1 and (4.2) now prove:

### Theorem 5.2 (causal fixed-atlas no-go)

For every fixed `A>0`, at `q=floor(A sqrt(m))<=r`, every causal
three-seed first-eligible factor confined to the fixed block atlas has

\[
             \boxed{
             M_q^-\ge(\kappa_A-o(1))W,
             \qquad
             M_q^+\ge(\kappa_A-o(1))W.}             \tag{5.7}
\]

Thus no choice of prefix automaton makes the signed Gaussian Hall defect
`o(W)`.

## 6. Why the coarser rank census is not the proof

Every native `q`-window does preserve the following coarse data:

* the exact states of all even-rank blocks;
* the set `J` of odd-rank blocks; and
* if `K subseteq J` is the set of lower rank-three blocks, the transition
  `K subset K'` with `|K'\setminus K|=q`.

After forgetting all singleton/triple labels, the two target shores in
one such context have sizes

\[
              4^s\binom{s}{k},
              \qquad
              4^s\binom{s}{k+q},
              \qquad s=|J|.                         \tag{6.1}
\]

Seed mixing changes only the singleton-to-triple label permutation and
does not change (6.1).  Nevertheless, (6.1) alone is not a Hall
obstruction.  A bipartite graph with two vertices on one shore and one on
the other can cover all three vertices using two edges which share the
smaller-shore vertex.  Cross-packet physical shadow repetitions allow
exactly this phenomenon.  Refining by prefix states cannot cure the
logical gap; nor does merging them create an occurrence bound.

The suffix argument is valid because Proposition 5.1 supplies the missing
capacity statement: the exact owner cover contributes at most `B_a`
occurrences to the target event, independent of how often individual
targets repeat.

## 7. Quantitative escape condition

For an arbitrary exact middle cycle factor, call a depth-`q` start
`R`-exceptional when its consecutive middle vertices do not all have the
same restriction to `R`.  Let `E_{R,q}` count such starts.  Repeating the
proof of Proposition 5.1 gives

\[
             M_q^\pm\ge(\kappa_A-o(1))W-E_{R,q}.     \tag{7.1}
\]

If `T_R` transition positions change the restriction to `R`, then each is
contained in exactly `q` cyclic `q`-windows, so

\[
                         E_{R,q}\le qT_R.             \tag{7.2}
\]

Consequently `o(W)` defect at `q=Theta(sqrt(m))` requires

\[
                         T_R=\Omega(W/\sqrt m).       \tag{7.3}
\]

For a factor with `W/(2h)+o(W/h)` cycles this is

\[
              \Omega(h/\sqrt m)
\]

suffix-disturbing transition sites per cycle on average.  Internal seed
changes contribute zero to this count, even at density `Theta(h)`.

The exact remaining construction target is therefore not a stronger
prefix automaton.  It is a cross-`B_4` recoupling whose physical components
transport coordinates through every positive-density suffix while retaining
the exact owner partition and the long-cycle phase structure.
