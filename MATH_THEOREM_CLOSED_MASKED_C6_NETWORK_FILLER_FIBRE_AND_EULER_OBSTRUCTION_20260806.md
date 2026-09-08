# Closed masked-C6 networks: exact current telescoping and the filler-fibre obstruction

## Status

This note answers the proposed closed-network escape from the
full-tensor filler-fibre obstruction.

A balanced directed network of masked `C6` ports does make its signed
crossing-deck current telescope exactly: every output state used once as a
later input cancels once with the same typed address.  However, equality of
a **full** typed seam state determines the period, terminal marker, and
complete ordered nonterminal filler bank.  Every masked port preserves that
bank on all three outputs.  Hence the filler label is constant on every
weak component of the port network.

Consequently no connected closed network made only from same-seam
full-tensor masked toggles can change filler fibre.  Since a complete owner
shore requires exponentially many such fibres at the two near-maximal
periods, this mechanism cannot produce one factor component.  Recombining
ports in a directed `3`-regular circuit does not evade the invariant.

There is also the familiar Euler parity: every local tail switch is a
3-cycle, so the parity of the number of physical components is invariant.
This parity can be arranged correctly by choosing an odd initial ring
count; unlike the filler invariant it is not the decisive obstruction.

The theorem is deliberately scoped to **full all-width state wiring at the
same seam**.  Recutting a fused component changes the distinguished marker
and can change the filler description, but intervals meeting both cuts are
then outside the transported tensor.  A filler-changing local port or an
overlap-safe cut-relocation theorem remains a valid escape.

No computation or search is used.

## 1. Full seam states and their current

Fix a period `ell` masked ring state

\[
                         S=(K,F,U;x),                  \tag{1.1}
\]

where `x in F` is the terminal marker and

\[
                         G=F-\{x\}                    \tag{1.2}
\]

is supplied with its inherited cyclic order

\[
                         G=(g_0,\ldots,g_{\ell-2}).   \tag{1.3}
\]

At the opened seam its complete cumulative profiles can be written

\[
 \begin{aligned}
 L_i(S)&=K\cup\{x\}
       \cup\{g_{\ell-i},\ldots,g_{\ell-2}\},\\
 R_j(S)&=K\cup\{g_0,\ldots,g_{j-1}\},
 \end{aligned}                                        \tag{1.4}
\]

for all nonempty admissible left and right lengths.  Empty end intervals
may be included formally as `L_0=R_0=K`; equivalently, `K,F,U,x` are part
of the typed literal state.

A three-way port has input states `S_0,S_1,S_2`.  With cyclic indices, its
full crossing-deck current is

\[
 \partial P
   =\sum_{t\in\mathbb Z/3\mathbb Z}
      \sum_{i,j}
       \left(
       [L_i(S_t)\cup R_j(S_{t+1})]
       -[L_i(S_t)\cup R_j(S_t)]
       \right),                                      \tag{1.5}
\]

where the inner sum ranges over the protected typed addresses.  For the
equal-period masked triangle of
`MATH_THEOREM_MASKED_CORE_TRIANGLE_ZERO_CURRENT_SPLICE_20260806.md`,
every summand in (1.5) is already zero.  The network argument below also
applies to a more general port whose output values merely become later
input values.

## 2. Balanced state wiring telescopes exactly

Let a finite directed port network consist of port vertices with three
input and three output seam-state occurrences at every vertex.  A wire
from an output occurrence to an input occurrence is **full typed** when it
identifies

* the period and every left/right address;
* both cumulative profiles at each address;
* the physical or accepted occurrence ticket;
* the cap, side, and residence state needed by later uses.

### Theorem 2.1 (network Stokes identity)

If every output occurrence is wired to exactly one equal typed input
occurrence and every input occurrence has exactly one predecessor, then

\[
                  \boxed{\sum_P\partial P=0}          \tag{2.1}
\]

in the free abelian group on typed crossing-deck occurrences.  In
particular every target-value current at every width is zero.

#### Proof

Expand the left side of (2.1).  Every output term occurs once with positive
sign.  Its wire identifies it with one input term of the same typed address,
which occurs once with negative sign.  The wiring is a bijection, so these
pairs exhaust all terms. \(\square\)

Thus current cancellation itself is not the obstruction.  It is the
ordinary zero-divergence/Euler-circuit identity.

If one identifies only target values, rather than complete typed states,
the same proof holds in the coarser free abelian group on values.  Such a
coarse cancellation does **not** allow the second port to be planted: it
does not transport its literal prefix/suffix profiles, occurrence tickets,
or capped ages.

## 3. A full state reconstructs its filler fibre

### Lemma 3.1 (state reconstruction)

The full typed state (1.4) determines `ell`, `K`, `x`, and the ordered list
`G=(g_0,...,g_(ell-2))`.

Even the address-labelled full crossing tensor determines the ordered
successive filler increments; adjoining the endpoint partition data
determines the initial increment as well.

#### Proof

The number of available cumulative addresses determines `ell`.  From the
typed endpoint profiles,

\[
             K=L_1\cap R_1,\qquad
             \{x\}=L_1-K,qquad
             \{g_0\}=R_1-K.                           \tag{3.1}
\]

For `j>=1`,

\[
                  \{g_j\}=R_{j+1}-R_j.                \tag{3.2}
\]

The left differences recover the same list from the opposite end and
certify its cyclic orientation.  Hence the whole ordered filler is
reconstructed.

Alternatively fix the minimal left address in the crossing tensor.  The
successive differences

\[
 (L_1\cup R_{j+1})-(L_1\cup R_j)                     \tag{3.3}
\]

recover all noninitial right increments.  The typed endpoint partition
separates the remaining marker/core increment, giving (3.1). \(\square\)

### Corollary 3.2 (wires preserve filler)

Every full typed output-to-input wire joins states having the same period
and the same ordered filler `G`.

This is stronger than equality of owner/root/upper values: it uses the
all-width seam state requested by the closed-network proposal.

## 4. One masked port also preserves the filler

Write a port's active labels as

\[
                         u\in K,\qquad x\in F,
                         \qquad y\in U,                \tag{4.1}
\]

and put `H=K-u`, `G=F-x`, `Z=U-y`.  Its three inputs are

\[
 \begin{array}{c|c|c}
 K&F&U\\ \hline
 H+u&G+x&Z+y\\
 H+x&G+y&Z+u\\
 H+y&G+u&Z+x.
 \end{array}                                           \tag{4.2}
\]

After the cyclic tail splice, its three output seams, read from their new
right-core sides, are

\[
 \begin{array}{c|c|c|c}
 K'&F'&U'&\text{terminal marker}\\ \hline
 H+x&G+u&Z+y&u\\
 H+y&G+x&Z+u&x\\
 H+u&G+y&Z+x&y.
 \end{array}                                           \tag{4.3}
\]

### Lemma 4.1 (portwise filler conservation)

Every one of the six states in (4.2)--(4.3) has the same ordered
nonterminal filler `G`.

#### Proof

Delete the displayed terminal marker from the moving cell of every row.
The remainder is `G`, with the inherited order, in all six cases. \(\square\)

At the three-bin projection the port performs useful exchanges among
`K,F,U`.  The point is that the apparently moved label is always promoted
to the new terminal-marker role; the long ordered bank left after deleting
that role never moves.

## 5. The closed-network no-go

Label every seam-state occurrence by its pair `(ell,G)`.  Form the weak
underlying graph whose vertices are all port and state occurrences and whose
edges are port incidences and output-to-input wires.

### Theorem 5.1 (filler-fibre conservation on arbitrary networks)

The label `(ell,G)` is constant on every weak component of a full typed
masked-port network.

Consequently:

1. a connected network uses one period and one ordered filler fibre;
2. no directed `3`-regular circuit of these ports can change filler fibre;
3. closing every current by Theorem 2.1 does not alter this conclusion; and
4. physical ring components belonging to distinct filler fibres cannot be
   joined by this network.

#### Proof

Along an incidence through one port, Lemma 4.1 preserves `(ell,G)`.  Along
an output-to-input wire, Corollary 3.2 preserves it.  Every walk in the weak
network alternates these two types of steps, so the label is constant along
the walk.  This proves all four statements. \(\square\)

This is a genuine conservation law, not a shortage estimate.  Increasing
the number of ports, using a nonplanar `3`-regular wiring, or choosing an
Euler circuit only adds more edges on which the same label is conserved.

## 6. Component parity is a secondary Euler obstruction

Cut every affected physical component at the port seams and record the
successor permutation of the resulting segments.  A masked `C6` toggle
multiplies that successor permutation by a 3-cycle.

### Proposition 6.1 (component parity)

Every collection or serial composition of masked `C6` toggles preserves
the parity of the number of physical factor components.  In particular an
even number of initial ring components cannot become one component using
only these toggles.

#### Proof

A 3-cycle is even, so the sign of the segment-successor permutation is
unchanged.  For a permutation on `N` segments with `c` cycles, its sign is

\[
                         (-1)^{N-c}.                   \tag{6.1}
\]

The number `N` is fixed, hence `c` has invariant parity. \(\square\)

When the initial number is odd, this parity is not an obstruction: a loose
tree of `m` three-way ports merges `2m+1` components to one.  The scalar
schedule can also be chosen with either ring-count parity.  The filler law
of Theorem 5.1 remains even after that parity choice.

## 7. Quantitative consequence for near-maximal rings

Let `s=q-h`.  In one period-`ell` ordered filler fibre, the complement of
`G` has size

\[
                         a=2q-\ell.                    \tag{7.1}
\]

There are at most

\[
                         N_G=\binom as(a-s)             \tag{7.2}
\]

ring states, and hence at most `ell N_G` owner occurrences.  Therefore a
complete owner shore of size

\[
                         W=\binom{2q-1}q               \tag{7.3}
\]

requires at least

\[
 \boxed{
 F_{\min}=\left\lceil
 {W\over \ell\binom as(a-s)}
 \right\rceil}                                        \tag{7.4}
\]

occupied full-tensor filler fibres.

For the two periods

\[
                 \ell_+=q+h-2,\qquad
                 \ell_-=q+h-3,                        \tag{7.5}
\]

the fibre state capacities are respectively

\[
             (s+2)(s+1),qquad
             3\binom{s+3}3,                            \tag{7.6}
\]

which are polynomial in `q`, while `W` is exponential.  Hence `F_min` is
exponential.

If both periods are used, the uniform lower bound is

\[
 F_{\min}^{\rm mix}=
 \left\lceil {W\over
 \max\left\{
  \ell_+(s+2)(s+1),
  \ell_-\,3\binom{s+3}3
 \right\}}\right\rceil,                                \tag{7.7}
\]

which is still exponential.  Since a full typed wire preserves the period
as well as `G`, fibres from the two period classes cannot be identified.

### Corollary 7.1 (no one-component all-width factor by closed wiring)

Starting from complete near-maximal ring blocks, a network made only from
same-seam full-tensor masked ports and full typed output-input wires leaves
at least `F_min^(mix)` physical components.  Here every later use of a
physical ring is required to pass through its designated wired seam; no
independent recut is allowed.  In particular the network cannot yield one
component, even though its complete crossing-deck current may be exactly
zero.

#### Proof

Every initial ring belongs to one filler fibre.  By Theorem 5.1 no port
network component contains rings from two fibres.  Ports may merge all
admissible rings inside one fibre (subject to Proposition 6.1), but they
cannot merge two occupied fibres.  Equation (7.4) proves the lower bound.
For the mixed schedule use (7.7). \(\square\)

## 8. Exact escape routes

The no-go uses both words **full** and **same-seam**.  It leaves exactly
three possible escapes.

1. **Filler-changing port.**  Construct a zero-charge local trade whose
   output moving bank minus its terminal marker is not the input `G`, while
   transporting the complete all-width tensor.
2. **Overlap-safe cut relocation.**  Recut an already fused ring at a new
   terminal marker and prove that every interval meeting both the old and
   new collars retains a provider.  The new cut may have
   `G'=F-{x'}`.
3. **Local tensor plus protected witnesses.**  Use the mixed-period or
   filler-changing `h+1` collar, abandon full-width state equality, and
   keep one protected occurrence of every nonlocal upper target away from
   the changed seams.

Value-only current cancellation is not a fourth escape unless it is upgraded
to one of these literal mechanisms: equal target values at two different
cells do not make an output state a legal later input state.

Thus the proposed closed directed network proves an exact algebraic
telescoping theorem but does not remove the global upper-provider gate.  It
reduces the next target to a filler-changing or overlap-safe local theorem;
there is no remaining benefit in searching for a more complicated closed
`3`-regular wiring inside the same full-state category.
