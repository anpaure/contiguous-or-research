# Global maximal-erosion lift and the coarsened history gate

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot connector  
**Status:** exact source-address/history reduction; no all-dimensional owner
host, terminal compiler, or regeneration theorem is claimed.

## 0. Result

The source-address part of `PCPS(m,d)` is not another Catalan-scale Hall
problem once the final rooted full depth chronology has been chosen.  It has a
pointwise largest candidate, obtained by intersecting the depth cells whose
windows use each source address.  With occurrence caps and protected literal
pins included, existence of a global source antecedent is equivalent to three
explicit containment/coverage tests.  In the uncapped case these reduce to

1. every internal positive coordinate run of the full depth chronology has length
   at least `d+1`; and
2. every maximal erosion envelope is nonempty.

Thus residence plus nonempty maximal envelopes is the exact global
address/history lift of a fixed full depth word.  It also preserves the complete
upper interval deck: unions of consecutive depth cells are exactly unions of
the corresponding longer source intervals.

For a componentwise construction, all local source occurrences at the same
global address must first be consolidated.  Short components make these
constraints genuinely nonadjacent.  Their arity is nevertheless at most
`d+1`.  After consecutive components are coarsened into blocks contributing
at least `d` owner/nonowner cells, no two nonadjacent coarse blocks overlap;
pairwise seam consistency is then exact.  This does **not** make the original
component-order problem an ordinary Hall problem, because the legal coarse
states still depend jointly on all components inside the block.

The remaining direct existence clause can therefore be sharpened to:

> construct a full post-insertion depth chronology whose `W` owner cells form
> a rooted upper-exact Hamilton path containing the pivot collar, and for
> which the capped maximal-erosion tests, the endpoint aperture, the compiler
> pins, and the terminal regeneration row all pass.

This reduction concerns the **post-insertion** depth row.  It does not run
the monotone pivot theorem backwards.  A `PCPS` certificate must still mark
the inserted source address and choose the required pre-insertion crossing
sets and upper occurrence intervals.  Once chosen, their simultaneous
literal realization is exactly Theorem 1.2 below.

The new K17 `q1` trajectory is only owner-layer evidence.  The independently
certified three-hole state, and especially the reported stable one-hole state
with mask `32058`, do not enter any theorem here; the latter must first be
literally replayed.  Once an authenticated rooted full chronology is available,
the tests below audit its entire source-address/history lift deterministically.

## 1. The capped inverse problem

Let

\[
                    T=(T_0,\ldots,T_{N-1})                 \tag{1.1}
\]

be a nonempty set word on a finite universe `U`.  We seek a nonempty source
word

\[
                    A=(A_0,\ldots,A_{N+d-1})               \tag{1.2}
\]

with

\[
             T_i=\bigcup_{j=i}^{i+d}A_j
             \qquad(0\le i<N).                            \tag{1.3}
\]

In the `B+1` application, `T` is the **entire** post-insertion depth row:
`N=W+1`, exactly `W` cells are the rank-`m` Hamilton-owner subsequence, and
the remaining cell is the controlled boundary nonowner.  All run and
history assertions below refer to this full row, not merely to its owner
subsequence.

At source address `j`, let `P_j` be the set of coordinates forced present
and `C_j` the cap of coordinates allowed present.  Exact prescribed source
letters are encoded by `P_j=C_j`.  An unpinned address has `P_j=emptyset`
and `C_j=U`.

Put

\[
 I_j=\{i:0\le i<N,\ i\le j\le i+d\}
    =[\max(0,j-d),\min(N-1,j)]                            \tag{1.4}
\]

and define the **capped maximal erosion envelope**

\[
 E_j=C_j\cap\bigcap_{i\in I_j}T_i.                        \tag{1.5}
\]

Every source antecedent satisfying (1.3) and the cap has `A_j subset E_j`.

### Theorem 1.1 (exact capped maximal-erosion criterion)

There is a nonempty source word `A` satisfying

\[
       P_j\subseteq A_j\subseteq C_j\quad(0\le j<N+d)
       \qquad\hbox{and}\qquad D^d(A)=T                 \tag{1.6}
\]

if and only if

\[
\begin{aligned}
 &P_j\subseteq E_j &&(0\le j<N+d),                     \tag{1.7a}\\
 &E_j\ne\varnothing &&(0\le j<N+d),                   \tag{1.7b}\\
 &T_i\subseteq\bigcup_{j=i}^{i+d}E_j
          &&(0\le i<N).                                \tag{1.7c}
\end{aligned}
\]

When these conditions hold, the maximal word

\[
                             A_j=E_j                    \tag{1.8}
\]

is a witness.  In particular the feasible antecedents have a unique
pointwise maximum.

#### Proof

If `A` is feasible and `i in I_j`, then `A_j subset T_i` by (1.3), while
the cap gives `A_j subset C_j`.  Hence `A_j subset E_j`.  The lower pins,
nonemptiness of `A_j`, and (1.3) imply (1.7a), (1.7b), and (1.7c),
respectively.

Conversely set `A_j=E_j`.  Conditions (1.7a)--(1.7b) give the pin, cap and
nonemptiness rows.  If `j in [i,i+d]`, then `i in I_j`, so `E_j subset T_i`.
Therefore

\[
        \bigcup_{j=i}^{i+d}E_j\subseteq T_i.
\]

The reverse containment is (1.7c), proving (1.3).  Maximality follows from
the first paragraph.  `square`

This is a Boolean closure criterion, not a matching relaxation.  Source
coordinates have no unit capacity: one occurrence of a coordinate may serve
several overlapping owner cells.  Consequently the only uncoupled
"Hall rows" are the literal coverage rows (1.7c).

### Theorem 1.2 (arbitrary prescribed-window closure)

Let `J` be a finite source-address set and let `mathcal H` be any family of
nonempty subsets of `J`.  For every `H in mathcal H`, prescribe a target set
`R_H` and require

\[
                         \bigcup_{j\in H}A_j=R_H.       \tag{1.9}
\]

Keep the address bounds `P_j subset A_j subset C_j`, and define

\[
 E_j=C_j\cap\bigcap_{H\ni j}R_H,                       \tag{1.10}
\]

where an empty intersection contributes `U`.  A nonempty word satisfying
all these equations exists if and only if

\[
\begin{aligned}
 &P_j\subseteq E_j,qquad E_j\ne\varnothing &&(j\in J),\tag{1.11a}\\
 &R_H\subseteq\bigcup_{j\in H}E_j &&(H\in\mathcal H). \tag{1.11b}
\end{aligned}
\]

Again `A_j=E_j` is the unique pointwise maximum.

If an address `j` belongs to no prescribed row, then (1.10) gives
`E_j=C_j`; condition `E_j ne emptyset` remains necessary because source
letters are required to be nonempty.  In the PCPS application every source
address already lies in at least one post-insertion depth window.

#### Proof

Every feasible `A_j` lies in the cap and in every target union of a row
which contains `j`; hence `A_j subset E_j`.  This proves necessity.  For
`A=E`, (1.10) gives `union_(j in H) E_j subset R_H`, while (1.11b) gives
the reverse containment.  The address rows are (1.11a).  `square`

Theorem 1.1 is the special case whose rows are the consecutive depth
windows `[i,i+d]`.  More importantly for the pivot, Theorem 1.2 can impose
simultaneously:

* every post-insertion depth window;
* each pre-insertion crossing window `[i,i+d] setminus {h}` after deleting
  the marked star address `h`;
* one chosen preword interval occurrence for every required upper target;
* every literal collar and compiler interval pin.

Thus, after the desired old crossing **sets** and one occurrence interval
per upper target have been selected, their common physical realization is
decided exactly by (1.11).  If only the ranks of the old crossing cells are
specified, or the upper occurrence intervals have not been selected, those
choices remain an integral outer problem; the closure theorem does not make
them automatic.

## 2. Residence is exactly the uncapped dilation row

Take `C_j=U` and `P_j=emptyset`.  For a coordinate `x`, write

\[
                     t_i(x)=1_{\{x\in T_i\}}.             \tag{2.1}
\]

A positive run is **internal** when it is preceded and followed by zero in
this full finite depth trace.  Boundary runs are clipped.  In particular,
the boundary nonowner may turn a run that was clipped in the owner
subsequence into an internal run; it cannot be omitted from this test.

### Lemma 2.1 (one-coordinate erosion)

For a positive run `[a,b]` of `t(x)`, the source addresses at which `x`
belongs to the uncapped envelope are

\[
 \{j:x\in E_j\}=
 \begin{cases}
   [a+d,b],&0<a\le b<N-1,\\
   [0,b],&a=0<b<N-1,\\
   [a+d,N+d-1],&0<a\le b=N-1,\\
   [0,N+d-1],&a=0, b=N-1.
 \end{cases}                                            \tag{2.2}
\]

The first interval is empty precisely when the internal run has length at
most `d`.  Dilation by the windows `[i,i+d]` recovers the original run
exactly whenever it is nonempty.

#### Proof

By (1.5), `x in E_j` exactly when every depth-row index in `I_j` lies in the
run.  Solving that pair of endpoint inequalities gives (2.2).  A source
address in (2.2) lies in `[i,i+d]` exactly for the owner indices `i` in the
displayed run.  `square`

### Corollary 2.2 (exact uncapped global lift)

The word `T` has a nonempty source antecedent if and only if

1. every internal positive coordinate run in `T` has length at least
   `d+1`; and
2. every envelope `E_j=cap_(i in I_j) T_i` is nonempty.

When these conditions hold, `E=(E_j)` is the canonical maximal antecedent.

#### Proof

Lemma 2.1 says that the run condition is equivalent, coordinate by
coordinate, to

\[
                       T_i=\bigcup_{j=i}^{i+d}E_j.
\]

The second condition is exactly the nonempty-letter row (1.7b).  Apply
Theorem 1.1.  `square`

The two conditions are independent.  Residence does not force a common
coordinate in each `(d+1)`-fold owner intersection, so it does not imply
nonempty maximal envelopes.

For example, with `d=2`, `T_0={a}` and `T_1={b}`, both positive runs are
clipped boundary runs, but the middle envelope `T_0 cap T_1` is empty.
Conversely, for `T=({a},{a,b},{a})` every envelope is nonempty because it
contains `a`, but the internal one-run of `b` has length one and (1.7c)
fails for that coordinate.

### Corollary 2.3 (cyclic factor form)

Let `T` be cyclic of length `N>d`, with all indices modulo `N`, and put

\[
 E_j=C_j\cap\bigcap_{s=0}^{d}T_{j-s}.                  \tag{2.3}
\]

A nonempty cyclic source word `A` with

\[
 T_i=\bigcup_{s=0}^{d}A_{i+s},\qquad
 P_j\subseteq A_j\subseteq C_j                        \tag{2.4}
\]

exists if and only if the cyclic analogues of (1.7a)--(1.7c) hold.  In the
uncapped case this says that every nonconstant cyclic positive run has
length at least `d+1` and every `E_j` is nonempty.  The all-one coordinate
trace is allowed and contributes at every source address.

#### Proof

The proof of Theorem 1.1 is index-local and applies modulo `N`.  For one
coordinate, eroding a proper cyclic run removes its first `d` positions;
redilation recovers it exactly precisely at length at least `d+1`.  The
all-one trace has the full cyclic source support.  `square`

This is the exact source-antecedent test for a fixed full depth cycle or
cycle factor.  It does not choose a safe opening, merge factor components, or
preserve upper witnesses through those later operations.

### Corollary 2.4 (Johnson host envelopes are automatically nonempty)

Suppose the full linear depth row consists of a rank-`m` Johnson Hamilton
owner path and, possibly, one outer rank-`m-1` boundary cell `o` contained
in its incident endpoint owner.  If `m>d`, then every uncapped envelope has

\[
                              |E_j|\ge m-d>0.           \tag{2.5}
\]

Consequently, without extra literal caps, this full chronology has a source
antecedent if and only if its full coordinate traces are depth-`d`
resident.

#### Proof

An envelope intersects at most `d+1` consecutive depth cells.  If they are
all owners, begin with the first rank-`m` owner; each of the at most `d`
Johnson transitions deletes at most one of its elements, leaving at least
`m-d` common elements.  If the block contains `o`, it is a boundary block.
Start with the `m-1` elements of `o`.  The containment step to the endpoint
owner deletes none, and the remaining at most `d-1` Johnson transitions
delete at most `d-1`, again leaving at least `m-d`.  Apply Corollary 2.2.
`square`

The conclusion can fail after protected caps are imposed: one must then use
the capped tests (1.7), or the combined prescribed-window tests (1.11).

### Corollary 2.5 (sparse-cap halo)

Assume the uncapped word passes Corollary 2.2, and let

\[
 H=\{j:C_j\ne U\text{ or }P_j\ne\varnothing\}.         \tag{2.6}
\]

Then every new failure of (1.7a)--(1.7b) occurs at an address in `H`, and
every possible new failure of the coverage row (1.7c) occurs at a depth
index in

\[
 \Gamma_d(H)=\{i:[i,i+d]\cap H\ne\varnothing\}.         \tag{2.7}
\]

In particular

\[
                         |\Gamma_d(H)|\le(d+1)|H|.       \tag{2.8}
\]

#### Proof

Outside `H` the capped and uncapped envelopes agree and there is no lower
pin.  If `[i,i+d]` avoids `H`, every envelope in its coverage union is also
unchanged, so the uncapped equality still proves (1.7c).  Counting the at
most `d+1` affected depth starts per protected address gives (2.8).
`square`

Therefore an `O(d)`-address literal pivot collar creates only an `O(d^2)`
source-lift audit halo.  This localization concerns the depth/cap equations;
chosen long upper-witness intervals in Theorem 1.2 may create additional
nonlocal rows.

## 3. Upper decks transport automatically through an antecedent

### Lemma 3.1 (all-width interval identity)

If `D^d(A)=T`, then for every `0<=p<=q<N`,

\[
        \bigcup_{i=p}^{q}T_i
          =\bigcup_{j=p}^{q+d}A_j.                     \tag{3.1}
\]

#### Proof

Expand `T_i` by (1.3).  The union of the integer intervals `[i,i+d]` for
`p<=i<=q` is exactly `[p,q+d]`.  `square`

Hence every all-width upper witness expressed as a consecutive depth-row
interval is retained by **every** source antecedent, not merely the maximal
one.  The global lift cannot create an upper hole of this kind.  This does
not assert completeness of source intervals shorter than `d+1`, and it
does not supply the lower compiler matching.

## 4. Exact consolidation of component addresses

Suppose an ordered component construction assigns local source position
`u` of component `K_i` to the global address

\[
                         b_i+u,                         \tag{4.1}
\]

with `b_(i+1)-b_i=n_i+g_i` on the full-`d` overlap face.  A local occurrence
may export a lower requirement `P_(i,u)` and an upper cap `C_(i,u)`.
At global address `j`, consolidate all occurrences mapping to `j` by

\[
 P_j=\bigcup_{b_i+u=j}P_{i,u},\qquad
 C_j=\bigcap_{b_i+u=j}C_{i,u}.                          \tag{4.2}
\]

### Theorem 4.1 (global quotient reduction)

For a fixed component order and fixed local cap/pin records, a globally
consistent nonempty source antecedent exists if and only if the consolidated
data (4.2) satisfy (1.7a)--(1.7c).  Every source pin whose physical interval
address is required to be distinct must additionally be injective after the
same quotient map (4.1).

In particular, letter and cap consistency is decided at global addresses;
pairwise seam feasibility is not a substitute.  The pin-injectivity clause
is independent of set equality.

#### Proof

Any global letter at `j` must contain every local lower requirement and lie
inside every local cap, giving exactly (4.2).  Theorem 1.1 is then necessary
and sufficient for the full depth windows.  Equality of two named physical
interval addresses is unaffected by the chosen set letter, so pin
injectivity is a separate literal quotient test.  `square`

Because every component contributes at least one owner/nonowner depth cell,
at most `d+1` component source images can contain one global address.  Thus
the address constraints have arity at most `d+1`, even when the Catalan
forest has `Cat_m` components.

### Minimal obstruction to pairwise port Hall

Let `d=2` and take three consecutive one-owner components.  Their source
images have starts `0,1,2`, so all three contain global address `2`.
Put caps at their three local copies of that address equal to

\[
                         \{a\},\quad\{a,b\},\quad\{b\}. \tag{4.3}
\]

Each adjacent pair has a nonempty common cap, but the global cap is empty.
This refutes a port relation which existentially projects its seam letter
separately on each incident edge.  A port graph whose vertices contain one
complete exact source state for the middle block already binds that letter.
Equivalently, with literal letters fixed, place two distinct address-private
compiler pins in the first and third components on the same resulting
global interval: both adjacent ports pass while global pin injectivity
fails.  Therefore an ordinary port graph can contain its rooted Hamilton
path even though no globally addressed source exists.

This is the smallest possible phenomenon: two blocks are completely checked
by their one seam; three one-owner blocks first permit a nonadjacent
identification.

## 5. Coarsening makes seam locality exact

For the fixed component order, put `ell_i=n_i+g_i>=1`.  Partition consecutive
components into coarse blocks.  Let `L_h` be the sum of `ell_i` in coarse
block `h`.

### Lemma 5.1 (coarsened overlap locality)

If every interior coarse block has `L_h>=d`, then no source address belongs
to two nonadjacent coarse blocks.  If every coarse block already exports a
globally consolidated accepted source state, global consistency of the
coarse concatenation is therefore equivalent to pairwise consistency at
adjacent coarse seams, together with global pin-address injectivity for pins
whose intervals are allowed to leave a block.

Every order with total increment at least `d` admits a consecutive
partition in which every coarse block has increment at least `d`: greedily
accumulate `ell_i` until reaching `d` and merge a final short remainder into
its predecessor.  Since every `ell_i>=1`, this greedy partition uses at most
`d` original components in an ordinary block and at most `2d-1` in the one
block which absorbs the final remainder.

#### Proof

The source interval of coarse block `h` begins at `B_h` and ends at
`B_h+L_h+d-1`.  Block `h+2` begins at `B_h+L_h+L_(h+1)`.  These intervals
are disjoint when `L_(h+1)>=d`; more distant blocks are then also disjoint.
Thus every shared source address lies in one block or in one adjacent pair.
The partition assertion is the stated greedy construction.  `square`

The lemma gives a proof-safe pairwise dynamic-programming face, not a free
Hall theorem.  In the greedy partition a coarse state encodes the joint
choices of at most `2d-1` original components, including their internal
owner transitions.  Deciding
which components are consecutive and selecting those states remains the
owner/path correlation in `PCPS`.

### Theorem 5.2 (exact protected-fragment extension)

Let `B=(B_0,...,B_(n+d-1))` be a nonempty literal source fragment with
`n>=d` and depth row

\[
                         P=D^d(B)=(P_0,\ldots,P_{n-1}). \tag{5.1}
\]

Let an uncapped full chronology `T_0,...,T_(N-1)` contain this depth block
at positions `s,...,s+n-1`.  Assume `T` already has its uncapped maximal
antecedent `bar E`; for the intended Johnson host this is exactly full-row
residence by Corollary 2.4.  Force

\[
                          A_{s+u}=B_u
                    \qquad(0\le u<n+d).                \tag{5.2}
\]

Define `E^B` to equal `B_u` on those fixed addresses and `bar E` elsewhere.
Then a global antecedent satisfying (5.2) exists if and only if:

1. the two literal rails fit the global envelopes,
   \[
     B_u\subseteq\bar E_{s+u}
     \quad
     (0\le u<d\text{ or }n\le u<n+d);                 \tag{5.3}
   \]
2. the exterior depth cells whose windows meet the fragment remain covered,
   \[
     T_i\subseteq\bigcup_{j=i}^{i+d}E^B_j             \tag{5.4}
   \]
   for every valid
   \[
       i\in[s-d,s-1]\ \cup\ [s+n,s+n+d-1].            \tag{5.5}
   \]

Thus a fixed literal pivot fragment has at most `2d` rail-containment rows
and `2d` exterior-coverage rows.  No Catalan-scale source-address condition
remains.

#### Proof

At an interior fragment source address `s+u`, `d<=u<n`, every depth cell
using that address lies inside the displayed copy of `P`.  Since `B`
factors `P`, `B_u subset bar E_(s+u)` automatically.  Only the two boundary
rails are also used by exterior depth cells, giving exactly (5.3).

Every depth window inside `[s,s+n-1]` consists entirely of fixed letters
from `B` and has union `P_(i-s)=T_i`.  Every depth window at distance more
than `d` outside the block avoids all fixed addresses and is still covered
by `bar E`.  The only unverified windows are precisely (5.5), for which
Theorem 1.1 gives (5.4).  Nonemptiness is inherited from `B` on the fragment
and from `bar E` outside.  These observations prove necessity and
sufficiency.  `square`

For the split-core pivot, `n=3d+1` and `|B|=4d+1`, so Theorem 5.2 applies
literally.  It closes only the source factorization of a prospective host;
the exterior upper occurrence bank, endpoint aperture, collision with any
external named physical pin, common cap, and regeneration remain separate.

## 6. The sharpened PCPS interface

Call a full post-insertion depth chronology `T` **erosion-prepared** when:

1. exactly `W` of its `W+1` cells form the rooted Hamilton owner subsequence,
   it contains the prescribed pivot collar, and it satisfies the corrected
   omitted-root endpoint aperture; the remaining cell is the controlled
   boundary nonowner;
2. it is upper-exact at every required full-depth-row interval width;
3. its protected literal pins and caps satisfy (1.7a)--(1.7c), and their
   named physical addresses are injective;
4. every coordinate history of the full depth row is residence-accepting;
   and
5. its unique nonowner/aperture cell is at the declared boundary, so the
   source-length charge is one and every internal component join has full
   `d`-overlap.

When the pivot collar itself is claimed literally, all of its prescribed
source addresses are included as exact caps `P_j=C_j`.  A designated star
address may be treated the same way.

### Theorem 6.1 (erosion-prepared host implication)

An erosion-prepared rooted chronology has a globally addressed nonempty
source antecedent of length

\[
                          (W+1)+d=W+d+1=B+1.            \tag{6.1}
\]

The antecedent preserves the
complete post-insertion all-width upper witness bank and the pivot collar
literally.  What remains between this conclusion and `PCPS` is:

* existence of such an integral rooted upper-exact full chronology;
* the **temporal deletion row**: deleting the designated star source address
  must recover the prescribed pre-insertion crossing cells and their ranks;
* upper completeness of that pre-insertion word (post-insertion upper
  completeness does not imply this converse transport);
* the terminal common-cap/lower-compiler assignment not already encoded by
  the protected pins; and
* regeneration of the next prepared cut.

#### Proof

Theorem 1.1 constructs the source antecedent and enforces all literal caps
and pins.  The one-credit aperture law gives its length.  Lemma 3.1
transports every consecutive-depth-row upper witness.  Rooting of the owner
subsequence and residence of the full row
are hypotheses on the final chronology and therefore survive the lift.
`square`

This is strictly smaller than the earlier componentwise `GOP/PHWC` clause:
it removes state-by-state source-rail selection after a chronology is born.
It does **not** construct the chronology, reverse the pivot insertion, or
prove `PCPS(m,d)`, `B+1`, or `nu(k)=B(k)`.

### Corollary 6.2 (selected-occurrence prepared lift)

In addition to the erosion-prepared chronology, choose:

1. the exact old crossing sets required after deleting the marked star,
   with their required temporal ranks;
2. one interval of the deleted preword for every required upper target; and
3. any literal interval rows used by the protected compiler pins.

Form the one family `mathcal H` consisting of the post-insertion depth
windows, the deleted crossing windows, the chosen upper witness intervals,
and the compiler intervals.  If its consolidated envelopes pass
(1.11a)--(1.11b), then one literal source word simultaneously realizes the
post-insertion full depth chronology, the temporal deletion row, the complete
preword upper witness bank, and all selected interval pins.

#### Proof

Apply Theorem 1.2 to the displayed family.  Each demanded statement is one
of its prescribed union equations.  `square`

Thus the exact residual source-side choice is not a source-letter CSP.  It
is the outer selection of the old crossing sets and one witness interval per
upper target so that the deterministic closure inequalities (1.11) pass.
This selection remains correlated with the rooted owner subsequence and is
not proved here.

## 7. K17 replay interface

For any authenticated K17 rooted-path candidate, the source/history audit
needed here is deterministic:

1. replay the full depth chronology, its owner subsequence, and the corrected
   endpoint aperture;
2. consolidate every pivot/collar/compiler cap and pin by physical address;
3. compute all `E_j` from (1.5);
4. report empty addresses, violations of (1.7a), and uncovered owner
   coordinate incidences in (1.7c);
5. replay the full coordinate-run automaton; and
6. verify post-insertion upper targets using the owner-interval identity
   (3.1); select old crossing sets and preword upper occurrences; and apply
   the combined closure test (1.11).

The reported one-hole mask `32058` is not authenticated in this note.  A
successful `q1` replay would close only part of item 1 above; it would not
imply any of items 2--6.
