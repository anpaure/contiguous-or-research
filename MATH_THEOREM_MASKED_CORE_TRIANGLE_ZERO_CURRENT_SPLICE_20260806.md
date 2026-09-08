# A masked core triangle gives a zero-current cross-core splice

## Status

The common-core Boolean-C6 collar has two complementary limitations: an
isolated port loses six immediate-upper occurrences, and serial
orientation reversal remains trapped in one invariant-core fibre.  Both
limitations disappear if the three input rings rotate their invariant
cores instead of sharing one.

This note gives an explicit three-ring port.  The rings have cores

\[
                         J+c_0,\quad J+c_1,\quad J+c_2,
\]

and ring `t` places the next core label `c_(t+1)` at its cut.  That one
letter masks the change from core `J+c_t` to core `J+c_(t+1)`.  Cyclically
rejoining the three tails then preserves **every** crossing interval union
of width at most the ring period, at the same typed address.  In
particular it preserves the complete owner, immediate-lower, and
immediate-upper rows with zero seam current, changes core, merges three
components, and is biresident.

The full-period symmetric construction works at every period

\[
                         2h\le \ell\le q+h-2.           \tag{0.1}
\]

and a local-collar variant permits the three input periods to differ in
that same range.  Thus the two consecutive near-maximal periods
`q+h-3,q+h-2` can be joined by one port and remain available for exact
scalar scheduling.  This is a literal local theorem;
it does not prove an integral one-copy packing of the owner shore by these
triples or a globally sealed loose connector tree.  No computation or
search is used.

## 1. Three adjacent invariant cores

Let the moving ground set `R` have size `2q-1`.  Assume

\[
 h\ge2,\qquad q\ge h+2,
 \qquad 2h\le\ell\le q+h-2.                            \tag{1.1}
\]

Choose a disjoint decomposition

\[
 R=J\mathbin{\dot\cup}\{c_0,c_1,c_2\}
      \mathbin{\dot\cup}G\mathbin{\dot\cup}Z,          \tag{1.2}
\]

where

\[
 |J|=q-h-1,\qquad |G|=\ell-1,
 \qquad |Z|=q+h-\ell-2.                                \tag{1.3}
\]

The last quantity is nonnegative by (1.1).  Give `G` a fixed order

\[
                         G=(g_0,\ldots,g_{\ell-2}).     \tag{1.4}
\]

For `t in Z/3Z`, put

\[
 \begin{aligned}
 K_t&=J\cup\{c_t\},\\
 F_t&=G\cup\{c_{t+1}\},\\
 U_t&=Z\cup\{c_{t+2}\}.
 \end{aligned}                                         \tag{1.5}
\]

These are respectively the invariant core, moving set, and unused set of
ring `t`, with sizes

\[
                         q-h,\qquad\ell,
             \qquad q+h-\ell-1.                        \tag{1.6}
\]

Order the moving set cyclically as

\[
 f_0^t=g_0,\ldots,f_{\ell-2}^t=g_{\ell-2},
 \qquad f_{\ell-1}^t=c_{t+1},                         \tag{1.7}
\]

and take the source word

\[
                         C_s^t=K_t\cup\{f_s^t\}.
                                                               \tag{1.8}
\]

Open every ring between phases `ell-1` and `0`, immediately after its
special marker `c_(t+1)`.

Every width-`h` source interval in ring `t` is a rank-`q` owner, every
width-`(h-1)` interval is a rank-`(q-1)` root, and every width-`(h+1)`
interval is a rank-`(q+1)` immediate-upper occurrence.

## 2. The masking identity

For `1<=i,j` with `i+j<=ell`, the cumulative left and right profiles at
cut `t` are

\[
 \begin{aligned}
 L_i^t
   &=K_t\cup\{c_{t+1}\}
       \cup\{g_{\ell-i},\ldots,g_{\ell-2}\},\\
 R_j^t
   &=K_t\cup\{g_0,\ldots,g_{j-1}\}.
 \end{aligned}                                         \tag{2.1}
\]

The suffix in the first line is empty when `i=1`.  The two displayed
`G`-intervals are disjoint because `i+j<=ell`.

Reconnect the left side of ring `t` to the right side of ring `t+1`.

### Theorem 2.1 (addresswise full-tensor preservation)

At every crossing address in (2.1), the new interval has exactly the old
value:

\[
 \boxed{
       L_i^t\cup R_j^{t+1}=L_i^t\cup R_j^t.}           \tag{2.2}
\]

Both sides equal

\[
 J\cup\{c_t,c_{t+1}\}
 \cup\{g_{\ell-i},\ldots,g_{\ell-2}\}
 \cup\{g_0,\ldots,g_{j-1}\},                          \tag{2.3}
\]

and have rank

\[
                         q-h+i+j.                       \tag{2.4}
\]

#### Proof

The left profile contains both `c_t` and `c_(t+1)`.  The old right core
adds only `c_t`, while the new right core adds only `c_(t+1)`; both are
therefore masked.  All other right markers are the same ordered prefix of
`G`.  This proves (2.2)--(2.3).  The two `G` pieces are disjoint and have
total size `(i-1)+j`, so (1.3) gives

\[
 (q-h-1)+2+(i-1)+j=q-h+i+j,
\]

which is (2.4). \(\square\)

### Corollary 2.2 (zero owner/root/upper current)

The three-way splice preserves the complete crossing OR deck through
width `ell`.  In particular:

1. width `h-1` roots remain rank `q-1` and unchanged;
2. width `h` owners remain rank `q` and unchanged;
3. width `h+1` immediate-upper values remain rank `q+1` and unchanged;
4. the signed immediate-upper seam current is exactly zero.

All noncrossing intervals are literally unchanged.  Since two consecutive
cuts in the fused word are `ell` source positions apart, an interval of
width at most `ell` meets at most one changed arc, so the assertion holds
for the whole three-component bank.

The identity is stronger than the orientation-reversal telescope: it is
addresswise, needs no backup upper provider, and changes the invariant core
across the seam.

## 3. Exact resource simplicity

### Theorem 3.1 (the three immediate rows are one-copy)

Before and after the splice, all `3ell` values in each of the widths

\[
                         h-1,\quad h,\quad h+1           \tag{3.1}
\]

are distinct.  More generally, for every fixed `1<=w<ell`, the `3ell`
width-`w` interval values in the input bank are distinct.

#### Proof

Inside ring `t`, a width-`w` interval has value `K_t` plus a proper cyclic
marker interval.  Distinct proper cyclic intervals of one fixed width in
a cyclic order of distinct markers have distinct sets.

Across rings, inspect the intersection with `{c_0,c_1,c_2}`.  A value from
ring `t` has one of the two active signatures

\[
                         \{c_t\},qquad
                         \{c_t,c_{t+1}\},               \tag{3.2}
\]

according as its marker interval avoids or contains the special phase.
The three singleton signatures and the three cyclic two-subsets are six
different sets.  Hence values from different rings cannot coincide.
Corollary 2.2 preserves every changed value addresswise, proving the
post-splice assertion at the three immediate widths. \(\square\)

Ranks at different proper widths are `q-h+w`, so the complete deck through
width `ell-1` is also value-simple across widths.  At width `ell`, every
cyclic interval in one input ring is the same full-ring union and hence has
multiplicity `ell`; Theorem 2.1 still preserves those crossing values, but
no simplicity assertion is made there.

## 4. Topology and residence

### Theorem 4.1 (one zero-charge cross-core component)

The cyclic tail reassignment `left(t)->right(t+1)` merges the three rings
into one source component of length `3ell` without inserting or deleting a
source position.  The fused owner chronology is biresident at deadline
`h-1`.

#### Proof

The tail permutation is the three-cycle on the input components, hence it
produces one component and has zero length charge.

Every coordinate of `J` is constantly present and every coordinate of `Z`
is constantly absent.  A marker `g in G` occurs once at the same phase of
each ring.  In the fused order its consecutive source occurrences are
exactly `ell` positions apart.  Its owner run has length `h` and its zero
gap has length `ell-h`, both at least `h` by `ell>=2h`.

Fix `c_t`.  It is present in the last source letter of ring `t-1` and in
every source letter of ring `t`; those pieces are consecutive after the
splice.  Thus its source-positive block has length `ell+1`, while its
source-zero block has length `2ell-1`.  Passing to width-`h` owner windows
gives a positive run of length `ell+h` and a zero gap of length
`2ell-h`.  Both are at least `h`.  These cases exhaust `R`, proving
biresidence at deadline `h-1`. \(\square\)

The same construction is phase-correct when the compiler row is the root
row rather than the owner row, because both widths are preserved
simultaneously.

## 5. The core-transition hypergraph is connected

Let `s=q-h`.  Regard the `s`-subsets of `R` as possible invariant cores.
Put a hyperedge on

\[
                         J+c_0,\quad J+c_1,\quad J+c_2  \tag{5.1}
\]

for every `(s-1)`-set `J` and three distinct labels outside `J`.

### Corollary 5.1 (no core-fibre connectivity obstruction)

The two-section of this `3`-uniform core-transition hypergraph is the
Johnson graph `J(2q-1,s)` and is therefore connected.  Every one of its
hyperedges has a literal zero-current port of Theorems 2.1--4.1 at every
period in (0.1).

#### Proof

Two `s`-sets are adjacent in the Johnson graph exactly when they share an
`(s-1)`-set `J`; any third label outside their union completes them to a
triple (5.1).  Conversely every pair in (5.1) differs by one exchange.
The Johnson graph is connected.  The literal realization is the preceding
construction. \(\square\)

Thus the exponential invariant-core lower bound for the old common-core
C6 family does not apply to the masked-core port.

## 6. Near-maximal periods and exact remaining gate

The two periods

\[
                         \ell_-=q+h-3,qquad
                         \ell_+=q+h-2                  \tag{6.1}
\]

are consecutive, lie in (0.1) whenever `q>=h+3`, and have Frobenius number
`ell_- ell_+ - ell_- - ell_+`.  Since the central width

\[
                         W_q=\binom{2q-1}{q}
\]

is exponentially larger, there are nonnegative integers `u,v` with

\[
                         W_q=u\ell_-+v\ell_+.           \tag{6.2}
\]

The resulting scalar number of scheduled rings is still

\[
                         u+v=(1+o(1)){W_q\over q}.      \tag{6.3}
\]

Unlike the former `q+h-2,q+h-1` schedule, every scheduled ring now has at
least one unused coordinate and therefore admits the masked-core local
model.

What remains is integral and global:

1. decompose the complete owner/root shores into one-copy rings of the two
   periods in (6.1), with cores and unused coordinates arranged in masked
   triangles;
2. plant collar-disjoint instances whose auxiliary hypergraph contains a
   loose tree spanning all but at most one ring component;
3. retain the named lower/compiler tickets and arbitrary-width upper
   witnesses outside the changed arcs, and pass the serial capped-age
   tests when a ring carries two ports.

No immediate-upper backup assignment is needed for these ports.  The
former six-versus-four seam budget and the invariant-core connectivity
obstruction are both absent.  The remaining theorem is a protected
integral ring cover-down with a masked-core loose connector tree.

## 7. Mixed-period local collars

The full common moving set `G` made Theorem 2.1 transparent but is not
needed for the three immediate rows.  We now allow arbitrary periods

\[
             2h\le\ell_t\le q+h-2
             \qquad(t\in\mathbb Z/3\mathbb Z).         \tag{7.1}
\]

Choose the same `J,c_0,c_1,c_2` as before and disjoint common collar banks

\[
 P=\{\rho_1,\ldots,\rho_h\},\qquad
 \Lambda=\{\lambda_1,\ldots,\lambda_{h-1}\}.          \tag{7.2}
\]

The remaining coordinates form a bank `D` of size

\[
 |D|=(2q-1)-(q-h-1)-3-(2h-1)=q-h-2.                  \tag{7.3}
\]

Give `D` a fixed order.  For ring `t`, let `D_t` be its initial segment of
size

\[
                         |D_t|=\ell_t-2h,               \tag{7.4}
\]

put

\[
 K_t=J\cup\{c_t\},\qquad
 F_t=P\cup\Lambda\cup D_t\cup\{c_{t+1}\},            \tag{7.5}
\]

and leave `c_(t+2)` and `D-D_t` unused.  Order the moving markers from the
cut as

\[
 \rho_1,\ldots,\rho_h,\quad D_t,\quad
 \lambda_{h-1},\ldots,\lambda_1,\quad c_{t+1},       \tag{7.6}
\]

where `D_t` carries the inherited order.  The count in (7.6) is
`h+(ell_t-2h)+(h-1)+1=ell_t`.

### Theorem 7.1 (mixed-period zero-current port)

Open each ring after its final special marker and reconnect
`left(t)->right(t+1)`.  Then:

1. every crossing interval of width at most `h+1` has exactly its old
   value and rank;
2. the complete width-`h-1`, width-`h`, and width-`h+1` rows are simple
   before and after the splice;
3. the three components merge at zero source-length charge; and
4. the fused owner chronology is biresident at deadline `h-1`.

#### Proof

For `1<=i,j<=h`, the cumulative profiles are

\[
 \begin{aligned}
 L_i^t&=J\cup\{c_t,c_{t+1}\}
          \cup\{\lambda_1,\ldots,\lambda_{i-1}\},\\
 R_j^t&=J\cup\{c_t\}
          \cup\{\rho_1,\ldots,\rho_j\}.
 \end{aligned}                                         \tag{7.7}
\]

Therefore, whenever `i+j<=h+1`,

\[
                    L_i^t\cup R_j^{t+1}
                    =L_i^t\cup R_j^t,                  \tag{7.8}
\]

and the common rank is `q-h+i+j`.  This proves item 1, including all
crossing roots, owners, and immediate uppers.

Within one ring, every one of these widths is strictly below its period,
so its cyclic marker intervals are distinct.  Across rings, the active
signature is again either `{c_t}` or `{c_t,c_(t+1)}`; the six possibilities
are distinct.  This proves item 2.  The tail permutation is a three-cycle,
which proves item 3.

For residence, every common collar marker occurs at a fixed distance from
the beginning or end of each ring segment in which it appears.  A member
of `D` is placed at the same inherited offset whenever it is used.  Hence
successive source occurrences of any nonactive moving coordinate are
separated by at least `min_t ell_t>=2h`; its owner runs and gaps are at
least `h`.  Coordinate `c_t` is present in the last source letter of ring
`t-1` and throughout ring `t`, giving a source-positive block of length
`ell_t+1`.  Its source-zero block has length

\[
                         \ell_{t+1}+\ell_{t-1}-1,
\]

so its owner zero gap has length
`ell_(t+1)+ell_(t-1)-h>=3h`; its positive owner run has length
`ell_t+h`.  Coordinates of `J` are constant positive, and unused
coordinates have still longer gaps.  This proves item 4. \(\square\)

The theorem protects exactly the rows needed for the owner/root factor and
the immediate-upper seam ledger.  Intervals wider than `h+1` can meet the
period-dependent remote blocks `D_t`; their values are not claimed to be
transported.  Arbitrary-width upper targets therefore still need retained
witnesses away from these cuts or a longer common local collar.

In particular, one port may contain any mixture of the two periods in
(6.1).  The scalar representation (6.2) no longer creates a separate
period-class connectivity gate.

### Corollary 7.2 (wide-upper damage localizes to a bounded terminal bridge)

Assume that, inside each of the two period classes in (6.1), the selected
rings admit a loose tree of the equal-period full-tensor ports from
Theorem 2.1.  Compress the two classes separately.  Each class then leaves
at most two components, according to its C6 parity.  At most one
mixed-period port from Theorem 7.1 reduces any three of the at most four
terminal components to one, leaving at most two components overall.

Consequently all but at most one port in this two-stage compression
preserve crossing interval values through the *full ring period*.  Only
the bounded terminal mixed-period bridge can disturb upper witnesses of
width greater than `h+1`.

#### Proof

A loose tree of three-way tail cycles merges an odd number of components
to one and leaves at most two in either parity.  Apply this independently
to the two period classes.  If at least three terminal components remain,
one mixed-period three-way splice merges three of them; otherwise no mixed
port is needed.  The equal-period ports have Theorem 2.1's full tensor,
whereas Theorem 7.1 claims only the common local tensor, proving the final
statement. \(\square\)

This is conditional on the two occurrence-resolved equal-period loose
trees.  It does not by itself supply backup witnesses at the bounded
terminal bridge; if its premise held, it would remove wide-upper damage from the
`Theta(W_q/q)`-port bulk.

The hypothesis is attractive but the present full-tensor port cannot
satisfy it on the whole owner shore.  There is a second exact fibre
invariant.

### Theorem 7.3 (regenerated full-tensor filler-fibre obstruction)

Fix a period `ell` and an ordered filler bank `G` of size `ell-1`.  A
full-tensor masked state has the form

\[
                         (K,x;G),                       \tag{7.9}
\]

where `|K|=s=q-h`, `K\cap G=\varnothing`, and
`x\notin K\cup G`; its moving set is `G\cup\{x\}`.  Every output seam of
a full-tensor masked port has that same ordered bank `G`.  Consequently a
serial chain which uses an output seam of each port as the regenerated
shared input of the next port remains in one `G`-fibre.

Put

\[
                         a=(2q-1)-(\ell-1)=2q-\ell.    \tag{7.10}
\]

Then one ordered filler fibre contains at most

\[
                         N_G=\binom{a}{s}(a-s)          \tag{7.11}
\]

ring states and hence at most `ell N_G` distinct owner occurrences.  An
exact factor of the whole owner shore therefore needs at least

\[
             \boxed{
             {\binom{2q-1}{q}\over
               \ell\binom{a}{s}(a-s)}}                \tag{7.12}
\]

different full-tensor filler fibres.

For the periods in (6.1), these fibre capacities are polynomial:

\[
 \begin{array}{c|c|c}
 \ell & a & N_G\\ \hline
 q+h-2 & s+2 & (s+2)(s+1),\\
 q+h-3 & s+3 & 3\binom{s+3}{3}.
 \end{array}                                           \tag{7.13}
\]

Thus (7.12) is exponential at critical width.  Regenerated-hub
equal-period full-tensor chains alone cannot compress a complete one-copy
factor to `O(1)` components, and the premise of Corollary 7.2 is not
presently available from that serial mechanism.

#### Proof

In Theorem 2.1 the complete left and right cumulative profiles list every
member of `G` in its fixed cyclic order.  The masked splice changes only
the core and the special marker; each output state has moving set
`G\cup\{x'\}` with `x'` as its new terminal marker.  Its filler bank after
deleting that marker is therefore still `G`.  Induction proves invariance
of `G` under output-seam regeneration.

The complement of `G` has size `a`.  Choose the `s`-set core `K` there and
then the special marker `x` from its `a-s` remaining labels, proving
(7.11).  A period-`ell` state supplies only `ell` owners, so (7.12)
follows even if every possible state in a fibre is used.

For `ell=q+h-2`, equation (7.10) gives `a=q-h+2=s+2`, and

\[
 \binom{s+2}{s}\,2=(s+2)(s+1).
\]

For `ell=q+h-3`, it gives `a=s+3`, and

\[
 \binom{s+3}{s}\,3=3\binom{s+3}{3}.
\]

This proves (7.13) and the claimed asymptotic obstruction. \(\square\)

One may choose a different cut inside the already fused component, thereby
changing the distinguished marker and its filler description.  But that
new full collar overlaps old seams, and no theorem presently says that all
intervals meeting both collars are transported.  Such a cut relocation is
therefore a possible escape, not a counterexample to the regenerated-hub
statement.

Accordingly, arbitrary-width upper preservation still has three viable
routes: prove an overlap-safe cut-relocation theorem, construct a
zero-charge port which changes the ordered filler fibre while transporting
the long tensor, or use the local mixed/filler-changing ports at growing
scale and protect a complete upper-witness bank away from their cuts.  A
bounded number of mixed bridges does not follow from the present
regenerated full-tensor normal form.

## 8. Owner-invisible thinning

The use of the full core in every source letter is convenient but not
forced.  It can be thinned at all but a sparse set of phases without
changing any assertion above at the three immediate widths.

### Lemma 8.1 (literal thinning freedom)

In each input ring choose a set `S_t` of phases such that:

1. phases `0` and `ell_t-1` belong to `S_t`; and
2. every cyclic interval of `h-1` phases meets `S_t`.

At a phase `s in S_t`, retain the full letter

\[
                         K_t\cup\{f_s^t\}.
\]

At every other phase replace it by

\[
                         H_s^t\cup\{f_s^t\},
                         \qquad H_s^t\subseteq K_t,     \tag{8.1}
\]

with arbitrary `H_s^t` (possibly empty).  Then all cumulative profiles in
the protected port, every width-`h-1`, width-`h`, and width-`h+1` value,
the masking identity, topology, and owner-level biresidence are unchanged.

#### Proof

Every interval of any of the three displayed widths contains a phase of
`S_t`, so its union contains the whole core `K_t`.  The remaining letters
add only subsets of that already present core, while their distinct moving
markers are unchanged.  Hence all three rows have exactly their old
values.  At a cut, the first right letter and last left letter are full-core
by item 1, so every nonempty cumulative left or right profile in (7.7)
also has exactly its old value.  The masking identity and splice topology
therefore persist.  Finally the owner row itself is unchanged, so its
coordinate runs and gaps, and hence biresidence, are unchanged. \(\square\)

Such a phase set always exists: start with `0`, advance in steps of
`h-1`, and add `ell_t-1`.  Thus only `O(ell_t/h)` full-core phases are
needed.  The arbitrary subsets in (8.1) are a genuine lower/compiler
decoration bank.  This lemma does not assert that they can be chosen to
cover all named lower targets; it proves only that doing so is no longer
locally obstructed by the masked-core port.

## 9. Full-block top-complement reduction

Although filler-fibre changes still expose one-seam upper cells, intervals
meeting two or more block seams have a very small target alphabet.

### Theorem 9.1 (every multi-seam value is within two of the top)

Let a source chronology be assembled from complete near-maximal ring
blocks of periods in (6.1).  The support of one block is

\[
                         R-U,
\]

where `|U|=1` for period `q+h-2` and `|U|=2` for period `q+h-3`.
Every contiguous interval which contains one whole block therefore has
complement contained in `U` and rank at least `2q-3`.

In particular, any interval meeting at least two distinct block-boundary
seams contains a whole intermediate block.  Its value belongs to

\[
 \mathcal T_{\le2}
   =\{R-X:X\subseteq R,\ |X|\le2\},                   \tag{9.1}
\]

whose exact size is

\[
        |\mathcal T_{\le2}|
          =1+(2q-1)+\binom{2q-1}{2}
          =2q^2-q+1.                                  \tag{9.2}
\]

#### Proof

The union of all source letters of a ring is its core union moving set,
namely `R-U`.  Any larger interval contains that set, so its complement is
a subset of `U`.  In a concatenation of whole blocks, an interval crossing
two different boundaries contains every position of the block between
them.  Equations (9.1)--(9.2) follow. \(\square\)

Thus every non-top upper casualty is a **one-seam** casualty.  This is the
exact decomposition of the arbitrary-width gate:

1. local tensors control intervals meeting one changed seam;
2. one protected occurrence of each member of `mathcal T_(<=2)` controls
   every interval meeting multiple seams.

The second bank has only `2q^2-q+1` tickets, polynomial against the exact
exponential upper surplus.  Its occurrence-level availability is still a
named provider condition, not a consequence of the scalar count.

### Proposition 9.2 (one terminal mixed port has only quadratic raw debt)

For an input ring of period `ell_t`, the number of crossing addresses of
width strictly greater than `h+1` and at most `ell_t` is

\[
 D(\ell_t)
   =\sum_{w=h+2}^{\ell_t}(w-1)
   ={\ell_t(\ell_t-1)-h(h+1)\over2}.                  \tag{9.3}
\]

Hence one mixed-period three-way port has at most

\[
                         \sum_{t=0}^2D(\ell_t)=O(q^2)  \tag{9.4}
\]

unprotected negative one-seam occurrences beyond its exact local tensor.
A bounded number of terminal mixed ports would therefore require only a
polynomial raw provider bank, in addition to (9.2).

#### Proof

A width-`w` interval crossing one fixed cut has exactly `w-1` positive
left/right splits.  Theorem 7.1 already protects every split through width
`h+1`; summing the rest gives (9.3), and three cuts give (9.4). \(\square\)

The filler-fibre obstruction in Theorem 7.3 is precisely why (9.4) is not
yet the global answer: the current full-tensor ports cannot reduce the
number of filler-changing ports to a constant.  Theorem 9.1 nevertheless
removes all multi-seam complexity.  The remaining upper theorem is a
one-seam witness-avoidance or provider-Hall statement for a growing family
of filler transitions.
