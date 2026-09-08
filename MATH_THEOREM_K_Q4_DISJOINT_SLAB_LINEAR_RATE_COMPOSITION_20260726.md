# A linear-rate composition of syndrome `Q_4` braids on the same owners

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Result

The syndrome `Q_4` braid bank can be composed at positive linear
information rate on one and the same set of cube owners.  A particularly
clean composition uses disjoint two-phase slabs, while all of its
cycle-label matchings overlap globally.

Let `h=2^a>=4`, and use the parity-alternating syndrome factor of `Q_h`.
Its even coordinate positions have one common syndrome column.  Put

\[
 r={h\over4},\qquad
 \tau_j=(4j\;4j+2),\qquad
 \delta_j=e_{4j}+e_{4j+2}\qquad(0\le j<r).           \tag{0.1}
\]

There is a phase complement `K_0` of size

\[
                         N=|K_0|={2^h\over2h}.         \tag{0.2}
\]

For every `j`, choose an arbitrary bit field

\[
 \varepsilon_j:K_0/\langle\delta_j\rangle
                         \longrightarrow\mathbb F_2. \tag{0.3}
\]

All these fields are independent.  If `P` is the standard rooted
isometric `C_(2h)` and

\[
 \sigma_k=\prod_{j=0}^{r-1}
               \tau_j^{\varepsilon_j(k)},             \tag{0.4}
\]

then

\[
 \boxed{\mathcal F_\varepsilon
       =\{\sigma_kP+k:k\in K_0\}}                    \tag{0.5}
\]

is an exact factor of `Q_h` into isometric `C_(2h)`'s.  Every intermediate
factor obtained by installing the layers in any order is exact.  One layer
is literally the union of the two old and two new cycles on each actual
owner pair of cycle labels `{k,k+delta_j}`; it is not merely a permutation
of direction words.

The number of independent physical component bits is

\[
 \boxed{
 B=r{N\over2}
   ={h\over4}{2^h\over4h}
   ={2^h\over16}.}                                    \tag{0.6}
\]

All `2^B` states are distinct rooted exact factors.  Thus the information
rate is exactly one bit per sixteen cube owners.  A fixed cycle has a menu
of `2^(h/4)` direction permutations, and the menu value may vary with the
cycle label subject only to the literal pair ties in (0.3).

The layers genuinely overlap on owners: every layer uses all `2^h` owners
and every cycle label participates in every layer.  What makes the full
Cartesian product legal is that layer `j` changes the owner routing only
in the two first-half phase columns

\[
                         I_j=\{4j+1,4j+2\},           \tag{0.7}
\]

and their antipodes; the sets `I_j` are disjoint.  Hence every phasewise
owner map sees at most one independently controlled matching.

At full activation the direction successor differs from the standard
factor on exactly half of all owners.  Under independent fair component
bits, the expected changed-edge density is exactly `1/4`.  Consequently
the construction removes the former `O(1/h)` changed-edge-density ceiling
of a single braid bank.

There is nevertheless a real compatibility obstruction once two local
phase slabs overlap.  For two commuting disjoint-coordinate swaps whose
prefix intervals overlap, the exact two-layer condition on every
`<delta,gamma>` plane is

\[
 (\varepsilon(k)+\varepsilon(k+\gamma))
 (\beta(k)+\beta(k+\delta))=0.                        \tag{0.8}
\]

Thus the two fields may not both vary transversely on the same four-cycle.
Exactly twelve of the sixteen formal two-field states are legal on one
plane.  For adjacent noncommuting swaps the sharper ten-state law in
`MATH_THEOREM_K_SYNDROME_Q4_OVERLAPPING_BRAID_NETWORK_20260726.md`
applies.  The disjoint-slab construction avoids both collisions rather
than hiding them.

This proves the exact owner/factor composition gate at positive linear
rate.  It does not prove that some state balances all lower and upper
shadow targets: the complete occurrence action of the new bank remains to
be optimized.

## 1. The standard syndrome labels and a common phase

Let

\[
 V=\mathbb F_2^h,qquad A=\mathbb F_2^a,qquad |A|=h. \tag{1.1}
\]

In the parity-alternating syndrome presentation, the coordinate columns
satisfy

\[
                         \Psi(e_{2t})=z              \tag{1.2}
\]

for every even coordinate `2t`.  Hence all vectors `delta_j` in (0.1)
belong to `K=ker Psi`.  Their supports are disjoint, so they are linearly
independent.  Put

\[
                         D=\langle\delta_0,\ldots,
                                      \delta_{r-1}\rangle.       \tag{1.3}
\]

Every vector in `D` vanishes on all odd coordinates, whereas the all-one
vector does not.  Thus `1 notin D`.  Choose a linear functional

\[
 \eta:K\longrightarrow\mathbb F_2,qquad
 \eta(\mathbf1)=1,qquad \eta(D)=0,                 \tag{1.4}
\]

and put `K_0=ker eta`.  Then

\[
 K=K_0\oplus\langle\mathbf1\rangle,qquad
 D\subseteq K_0,qquad |K_0|={2^h\over2h}.           \tag{1.5}
\]

Write

\[
 p_i=e_0+e_1+\cdots+e_{i-1}\qquad(0\le i<h)        \tag{1.6}
\]

and let `P` have successive owners

\[
 p_0,p_1,\ldots,p_{h-1},
 \mathbf1+p_0,\ldots,\mathbf1+p_{h-1}.              \tag{1.7}
\]

The standard factor is `{P+k:k in K_0}`.  Its phase classes are
`p_i+K_0` and `1+p_i+K_0`.

For every permutation generated by the `tau_j`, the displacement of a
prefix lies in `D`.  Consequently every exact factor below has the one
common owner colouring

\[
 c(p_i+k)=i+h\eta(k)\pmod {2h}.                     \tag{1.8}
\]

In particular the phase-zero owner `k` and antipodal owner `k+1` of every
rooted row are fixed pointwise in every state.

## 2. The phasewise owner calculation

The transpositions in (0.1) have disjoint coordinate supports and hence
commute.  For a prefix `p_i`, the pair `{4j,4j+2}` is cut precisely when

\[
                         i\in I_j=\{4j+1,4j+2\}.     \tag{2.1}
\]

If the prefix contains neither or both pair coordinates, `tau_j` fixes it;
if it contains exactly one, `tau_j` adds `delta_j`.  Since the intervals
`I_j` are pairwise disjoint, (0.4) gives the exact formula

\[
 \sigma_kp_i+p_i=
 \begin{cases}
  \varepsilon_j(k)\delta_j,&i\in I_j,\\
  0,&i\notin\bigcup_jI_j.
 \end{cases}                                         \tag{2.2}
\]

Thus the phase-`i` owner in row `k` is `p_i+T_i(k)`, where

\[
 T_i(k)=
 \begin{cases}
  k+\varepsilon_j(k)\delta_j,&i\in I_j,\\
  k,&i\notin\bigcup_jI_j.
 \end{cases}                                         \tag{2.3}
\]

For `i in I_j`, the map in (2.3) acts separately on each pair
`{k,k+delta_j}`.  Pair constancy (0.3) makes it either fix both labels or
exchange them.  Hence every `T_i` is a permutation of `K_0`.  The same
formula holds in the antipodal half because every coordinate permutation
fixes `1`.

The phase classes partition `V`.  Since every `T_i` is bijective, the
cycles (0.5) contain every owner exactly once.  Moreover the direction
word in row `k` is

\[
 \sigma_k(0),\sigma_k(1),\ldots,\sigma_k(h-1),
 \sigma_k(0),\ldots,\sigma_k(h-1),                 \tag{2.4}
\]

a permutation repeated twice.  Every row is therefore an isometric
`C_(2h)`.  This proves exactness and physicality without any averaging or
word-only relaxation.

Finally, (2.2) lies in `D`, on which `eta` vanishes.  Formula (1.8) assigns
the same phase to every routed owner and advances by one along every row.

## 3. Each stage is a literal owner trade

It remains to verify that (0.5) can really be installed one braid layer at
a time.  Fix `j`, and suppose an arbitrary subfamily of the other layers
has already been installed.  Let

\[
 \rho_k=\prod_{\ell\ne j}
                 \tau_\ell^{\varepsilon_\ell(k)}.    \tag{3.1}
\]

At every phase in `I_j`, each earlier pair `{4ell,4ell+2}` with `ell<j`
is wholly contained in the prefix and each later pair with `ell>j` is
wholly outside it.  Therefore

\[
                         \rho_kp_i=p_i
                    \qquad(i\in I_j)                 \tag{3.2}
\]

for every row label `k`, independently of all other component bits.  The
same holds after adding `1` in the antipodal half.

Outside `I_j` and its antipode, `tau_j` fixes the current phase owner,
because it sees either neither or both of its coordinates.  Inside these
four phase columns the two old rows labelled `k,k+delta_j` contain

\[
                         p_i+k,qquad p_i+k+\delta_j, \tag{3.3}
\]

and the active new shore exchanges them.  Pair constancy of
`epsilon_j` makes the exchange simultaneous on the two rows.  Consequently

\[
 C_k^{\rm old}\mathbin{\dot\cup}C_{k+\delta_j}^{\rm old}
 =C_k^{\rm new}\mathbin{\dot\cup}C_{k+\delta_j}^{\rm new}       \tag{3.4}
\]

as literal `4h`-owner sets.

The changed joins are precisely the antipodally doubled `Q_4` joins which
exchange the directions `4j` and `4j+2`, with the intermediate direction
`4j+1` frozen.  Every other join is inherited.  Hence (3.4) is one genuine
syndrome `Q_4` braid component.  Components of one layer are owner-disjoint;
components from different layers overlap, but (3.2) shows that their
physical phase slabs commute.  This proves sequential realizability in
any layer order.

## 4. Entropy, cycle menus, and physical action

For each `j`, the matching `k <-> k+delta_j` has `N/2` pairs, and one bit
is freely chosen on every pair.  The choices for different `j` are
independent.  This proves (0.6).

Suppose two parameter states differ.  For some `j` and some label `k`,
their values `epsilon_j(k)` differ.  The disjoint transpositions `tau_j`
generate an elementary abelian group of rank `r`, so their final
permutations `sigma_k` differ.  Phase zero roots the corresponding row at
the same owner `k`; no row relabelling can identify the two factors.  Thus
all `2^B` states are distinct.

For fixed `k`, the `r` values `epsilon_j(k)` can be prescribed
independently, by setting the corresponding pair-coset bits.  Hence one
cycle has all `2^r=2^(h/4)` products of the disjoint swaps in its menu.
The choices on different cycles are not fully independent: a value in
coordinate `j` is tied between `k` and `k+delta_j`.  That tie is exactly
the two-cycle owner requirement and is already included in `B`.

One selected component in layer `j` changes two direction positions in
each half of each of its two rows.  It therefore changes eight directed
successor edges.  If `s_j` of the `N/2` components in layer `j` are
selected, the exact number of changed directed edges relative to the
standard factor is

\[
                         E(\varepsilon)=8\sum_js_j
                         =4\sum_{j,k}\varepsilon_j(k).           \tag{4.1}
\]

At full activation, `s_j=N/2` for every `j`, so

\[
 E_{\max}=8r{N\over2}=4rN=hN={2^h\over2}.            \tag{4.2}
\]

The factor has `2^h` directed successor edges, giving density `1/2`.
With independent fair component bits, the expected value is
`E_max/2=2^h/4`, giving expected density `1/4`.

This is the quantitative gain over one transposition bank.  One bank has
only `2^h/(4h)` bits and changes `O(2^h/h)` edges.  The composed bank has
`2^h/16` bits and can change `Theta(2^h)` edges while all cycles remain
long, exact, and isometric.

## 5. Exact obstruction when phase slabs overlap

The preceding independence is not automatic for arbitrary coordinate
pairs.  Let `tau_delta,tau_gamma` be two commuting transpositions on
disjoint coordinate pairs, with independent displacement vectors
`delta,gamma`.  Suppose a prefix phase cuts both pairs.  Let

\[
 \varepsilon(k+\delta)=\varepsilon(k),qquad
 \beta(k+\gamma)=\beta(k),                            \tag{5.1}
\]

and examine one affine plane `k+<delta,gamma>`.  Write its points as
`(x,y)`, where adding `delta` changes `x` and adding `gamma` changes `y`.
Then

\[
 \varepsilon(x,y)=A(y),qquad \beta(x,y)=B(x).        \tag{5.2}
\]

At the common cut phase the row-label map is

\[
                         F(x,y)=(x+A(y),\ y+B(x)).    \tag{5.3}
\]

No two points on one horizontal or vertical line collide under `F`.
The only possible collisions are the two diagonal pairs.  Both diagonal
collisions occur exactly when

\[
 A(0)+A(1)=1,qquad B(0)+B(1)=1.                    \tag{5.4}
\]

Therefore `F` is a permutation if and only if at least one transverse
difference in (5.4) vanishes.  This is (0.8).

There are four choices for `A` and four for `B`.  Eight states have `A`
constant and arbitrary `B`; four further states have `A` nonconstant and
`B` constant.  Hence exactly twelve of the sixteen formal pair-field
states are owner-legal on the plane.

This four-point calculation is a statewise owner invariant.  It shows why
one cannot simply multiply arbitrary braid banks whose active prefix
intervals overlap.  The construction in Sections 1--4 is a genuine tiling:
every prefix cuts at most one selected coordinate pair, so every local
Latin map is a single matching permutation and (5.4) never arises.

If the coordinate swaps themselves overlap, noncommutativity strengthens
the restriction.  For adjacent swaps `(a b),(b c)`, the exact classification
is ten legal states out of sixteen, as proved in
`MATH_THEOREM_K_SYNDROME_Q4_OVERLAPPING_BRAID_NETWORK_20260726.md`.

## 6. Exact boundary

Proved:

* `h/4` braid layers act on the same owners and compose with every
  `delta`-pair component bit independent;
* every intermediate state is a literal exact isometric factor;
* all states have one common phase colouring and fixed root/antipode ports;
* the bank has exactly `2^h/16` free component bits and `2^(h/4)` possible
  direction orders on a specified cycle;
* it supplies `Theta(2^h)` changed-edge action, with exact maximum density
  `1/2` and fair-bit mean density `1/4`; and
* overlapping prefix slabs obey the exact transverse-variation obstruction
  (0.8), rather than a Cartesian product law.

Not proved:

* arbitrary `S_(h/2)` direction permutations independently on every cycle;
* a Benes network with `Theta(2^h log h)` freely programmable owner switches;
* equality of complete lower/upper protected collars; or
* a choice of the `2^h/16` bits which gives coefficient-one shadow balance.

The former factor-composition gate is therefore positively closed at
linear owner rate.  The next gate is occurrence-level: compute and balance
the all-depth physical carrier of this dense, correlated bank.
