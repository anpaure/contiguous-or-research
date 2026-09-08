# Audit of Claude's wedge/SPILL ledger and the fixed-width ray absorber

Date: 2026-07-30  
Lane: AD  
Status: theorem/counterexample audit complete.  The local wedge identity is
correct.  The unrestricted rank-`(r+2)` kill-shape and degree-one killer
injection are false.  Under fixed-width support the correct killers are
arbitrary-depth outward rays.  Independently of any strict dispersion
inequality, an explicit literal ray list repairs all old upper losses at cost
at most `b(k-r-1)` for `b` wedge-opened components.

## 1. Definitions and exact scope

Let

\[
 C=(A_0,\ldots,A_{N-1}),\qquad A_i\in\binom{[k]}r,
\]

be a directed simple Johnson cycle, with cyclic edge
`e_i=A_i A_(i+1)`.  A directed `q`-edge witness of a target `Y` is

\[
 A_s,A_{s+1},\ldots,A_{s+q},\qquad
 Y=\bigcup_{j=0}^q A_{s+j},\qquad |Y|=r+q.       \tag{1.1}
\]

Here `q<N`, so the witness uses `q+1` distinct cyclic vertices and `q`
distinct internal edges.  The rank equality itself forces this in every
application below: a full turn would revisit the initial vertex and could
not introduce a fresh coordinate on the closing transition.

The rank equality in (1.1) means that every transition introduces one
coordinate not seen earlier in that interval; call such a witness
**fixed-width** or **geodesic**.

A wedge at `A_i` is the equality

\[
 A_{i-1}\cup A_i=A_i\cup A_{i+1}=:U_i.          \tag{1.2}
\]

For an arbitrary target `Y`, its old-witness kernel on `C` is the
intersection of the internal edge spans of all directed cyclic intervals
whose union is `Y`.  An edge in this intersection is killed by `Y` when the
cycle is opened there.

The fixed-width support hypothesis used below is literal:

> **(FW).** Every target of rank `r+q` has at least one actual directed
> `q`-edge witness on some declared component of the factor.

It is stronger than arbitrary-width upper support.  It does not assert two
witnesses, componentwise support, residence, seam legality, or lower
compiler feasibility.

## 2. What is genuinely proved in the LEDGER

### Lemma 2.1 (wedge equals distance-one duplicate)

For a simple Johnson cycle of length at least three, (1.2) holds if and only
if there is a unique coordinate

\[
 x\notin A_i,\qquad x\in A_{i-1}\cap A_{i+1}.     \tag{2.1}
\]

In that case both flank unions equal `A_i union {x}` and have multiplicity
at least two.

#### Proof

If (2.1) holds, each neighbour is obtained from `A_i` by deleting one
element and inserting `x`, so both unions are `A_i union {x}`.  Conversely,
let the two unions in (1.2) equal `U`.  Each is an `(r+1)`-set containing
`A_i`; hence `U\A_i={x}`.  Both neighbours are distinct `r`-facets of `U`
and contain `x`.  Uniqueness follows from `|U\A_i|=1`. QED.

The displayed sentence in Claude's `LEDGER.md` which writes
`A_(i+/-1)=(A_i\{a,b}) union {x}` has a harmless typo: each neighbour
deletes one element, not two.

### Lemma 2.2 (exact depth-two compression)

Let `|Y|=r+2`.  Every interval of Johnson vertices contained in `Y` whose
union is `Y` contains three consecutive vertices whose union is `Y`.

#### Proof

Write `P_j=Y\A_j`.  The `P_j` are 2-subsets of `Y`, and consecutive
distinct ones intersect in one element.  If every consecutive triple of
the `P_j` had nonempty intersection, the singleton
`P_j intersect P_(j+1)` would propagate from one overlapping triple to the
next; every `P_j` would contain the same element.  Their total intersection
would then be nonempty, contradicting that the union of the `A_j` is `Y`.
Thus some consecutive triple of complements has empty intersection, which
is exactly the desired three-vertex union. QED.

### Corollary 2.3 (the correct one-sided three-OR criterion)

For a wedge at `A_i`, the right flank `e_i` is killed by a rank-`(r+2)`
target if and only if

\[
 R_i=A_i\cup A_{i+1}\cup A_{i+2}                 \tag{2.2}
\]

has rank `r+2` and is the unique cyclic three-vertex window with value
`R_i`.  The mirrored assertion holds on the left.

#### Proof

Any witness avoiding `e_i` contains, by Lemma 2.2, a three-vertex witness
avoiding `e_i`.  Of the two three-vertex windows containing `e_i`, the
centered one `A_(i-1),A_i,A_(i+1)` has union `U_i` of rank `r+1`; only
(2.2) can witness a rank-`(r+2)` target through that flank.  Therefore all
witnesses contain `e_i` exactly when (2.2) is the unique three-window value.
QED.

This corollary is exact only for depth two.  It is not an all-depth SPILL
criterion.

## 3. Two decisive counterexamples

### 3.1 Higher-depth killers exist at odd middle rank

The already frozen cycle

```text
12389,12489,13489,13589,15689,15789,12789
```

lies in `J(9,5)`.  Coordinate 3 gives a wedge at `12489`.  The rank-eight
target

```text
12345689
```

has exactly two witnesses, with edge spans `{0,1,2,3}` and `{1,2,3}`.
Its kernel is therefore `{1,2,3}` and contains the right wedge flank.  Its
rank is `r+3`, not `r+2`.  Adding `r-5` common and `r-5` unused coordinates
suspends the example to `J(2r-1,r)` for every `r>=5`.

Thus local wedge algebra proves only `Y superset U_i`; it does not prove
`|Y|=r+2`.  Claude's unrestricted “killers per wedge at most two” and full
SPILL equivalence do not survive.

### 3.2 The proposed killer-to-wedge injection is false even at depth two

In `J(7,4)` take the cycle

```text
1347,1237,1247,2457,1457,1567,1367.
```

It has wedges at `1237` (missing coordinate 4) and `2457` (missing
coordinate 1).  All four labelled flanks are killed by only three rank-six
targets:

\[
\begin{array}{c|c}
Y&K(Y)\\ \hline
123467&\{e_6,e_0\}\\
123457&\{e_1,e_2\}\\
124567&\{e_3,e_4\}.
\end{array}                                      \tag{3.1}
\]

The middle target has one geodesic three-window and kills one flank of each
wedge.  Hence every wedge in this cycle is depth-two useless.  Adding
`r-4` common and `r-4` unused coordinates suspends the example to every
`J(2r-1,r)`, `r>=4`.

This example is neither spanning nor protected nor equivariant.  It proves
that no local odd-middle theorem, and no degree-one injection from killer
values to wedges, can establish a good wedge.  A unique geodesic
three-window can be outward for at most two wedges, one at each endpoint;
degree two is sharp.

More exactly, if `w` is the number of wedge centers, `u` is the number of
unique full-rank outward three-window occurrences, and `delta` is the
number whose two endpoint centers are both wedges, then the number of bad
labelled depth-two flanks is

\[
                         B_2=u+\delta.              \tag{3.2}
\]

A depth-two-good wedge is forced precisely when `B_2<2w`.  Neither this
strict inequality nor the claimed special case `delta=0` is known for all
protected factors.

## 4. Correct fixed-width outward-ray theorem

### Theorem 4.1 (arbitrary-depth outward rays)

Assume a target `Y`, `|Y|=r+q`, has a fixed-width `q`-edge witness on `C`.
If the left wedge flank `e_(i-1)` belongs to its full old-witness kernel,
then

\[
 Y=\bigcup_{j=i-q}^{i}A_j.                           \tag{4.1}
\]

If the right flank `e_i` belongs to the kernel, then

\[
 Y=\bigcup_{j=i}^{i+q}A_j.                           \tag{4.2}
\]

No such target has both wedge flanks in its kernel.

#### Proof

A fixed-width `q`-edge interval introduces one fresh coordinate on every
transition.  An interval containing both wedge transitions cannot be
geodesic: the second transition inserts the same wedge coordinate already
seen on the first side.  Thus a fixed-width witness through one flank
excludes the other.  Among directed `q`-edge intervals containing the left
flank but not its successor, only the interval ending at `A_i` is possible;
this gives (4.1).  The right statement is symmetric.  If both flanks lay in
the kernel, every fixed-width witness would contain both, a contradiction.
QED.

This is the exact replacement for the false rank-`(r+2)` shape.  Killers
may occur at every depth `q>=2`.

## 5. A solver-free literal absorber

The next theorem makes strict zero-spill dispersion unnecessary whenever an
`O(k)` literal append is affordable.

### Theorem 5.1 (general cut-arc absorber)

Let a factor consist of `b` directed cycles.  Assume (FW), and assign each
rank-`(r+q)` target one fixed-width provider witness.  Cut one edge `e_a` in
each component.  For a cut edge, list every fixed-width `q`-edge interval
containing it whose union has rank `r+q`, for `1<=q<=k-r`, and append each
distinct listed union as one literal letter.

Only depths `q<N_a` can contribute on a component of length `N_a`; this is
automatic whenever the assigned fixed-width witness exists there.

Every target which lost all old component-interior witnesses is on this
list.  The list has size at most

\[
 b\sum_{q=1}^{k-r}q
   =b\binom{k-r+1}{2}.                               \tag{5.1}
\]

#### Proof

If a target loses every old witness, its assigned witness is cut on its
provider component.  For a fixed cut edge there are exactly `q` directed
`q`-edge intervals containing it, hence at most `q` possible target unions
at depth `q`.  Summing gives (5.1).  Appending a listed mask realizes it as
a singleton literal interval and cannot destroy any existing witness. QED.

### Theorem 5.2 (wedge-ray absorber)

If every chosen cut is a wedge flank, omit depth one and list only the
single outward ray (4.1) or (4.2) at each depth `2<=q<=k-r` whose union has
rank `r+q`.  Then every lost old upper target is restored and

\[
        |\mathcal R|\le b(k-r-1).                   \tag{5.2}
\]

For odd middle rank `k=2m+1`, `r=m+1`, this is exactly

\[
        |\mathcal R|\le b(m-1).                     \tag{5.3}
\]

#### Proof

Theorem 4.1 leaves at most one candidate at each depth.  At depth one the
cut union `U_i` retains the opposite wedge flank as a second one-edge
witness, so it is not lost.  Summing the remaining depths proves (5.2).
Literal appending proves restoration. QED.

The list can be formed without computing kernels: append every maximal-rank
outward ray, whether or not it was actually lost.  Deduplication can only
improve (5.2).

The declared cut set must be the actual cut set of the final linear
chronology.  If components are first socketed into a new cycle and a new seam
is then deleted to linearize it, that additional deletion needs its own safe
cut proof or absorber ledger.

### Corollary 5.3 (coefficient-one interface)

Suppose `d=d(k)=o(W)`, and the independent joining/lower-compiler interface
supplies a literal word of length `W+d+o(W)` by opening each old component
at exactly the one declared wedge edge.  Assume it already covers the lower
and middle masks, every old upper interval not crossing a declared cut is
unchanged, and every upper loss is therefore among the declared cut losses.
If the construction uses `b` components with `bk=o(W)`, wedge-ray appending
yields a universal word of length

\[
                        W+d+o(W)+O(bk)=W+o(W).       \tag{5.4}
\]

In particular `b=O(1)` suffices.  This is not the sharp equality
`nu(k)=W+d`: the append may cost up to (5.3), and component joining,
residence, middle ownership, and the lower compiler remain independent.

## 6. The exact remaining zero-spill lemma

For sharp length with no literal append, let `D` be the number of labelled
wedge flanks lying in at least one higher-target kernel.  The exact
one-component existence condition is `D<2w`.  A convenient sufficient
locked-ray condition is

\[
 \Lambda<2w,                                        \tag{6.1}
\]

where `Lambda` counts locked triples `(wedge,side,q)` over **all** depths
`q>=2`.  Since several depths may charge the same dangerous flank,
`D<=Lambda`; (6.1) is sufficient, not necessary.  For several components
and a jointly admissible opening atlas, the exact condition is avoidance of
the union of the product kernel boxes; a sufficient probabilistic form is

\[
 \Phi=\sum_Y\prod_{a\in S(Y)}\Pr(e_a\in K_a(Y))<1. \tag{6.2}
\]

Fixed-width existence gives one witness, not the recurrence needed to make
(6.1) or (6.2) strict.  Residence also does not imply them: the protected
outward-ray report constructs arbitrarily resident cycles with a flank
carrying linearly many locked geodesic rays.  Thus the exact remaining
lemma must use the global PBBS/protected-factor distribution, or replace
zero spill by Theorem 5.2.

## 7. Independent finite replay

The authenticated optimal words reconstruct the following exact middle
paths:

\[
\begin{array}{c|r|r|r}
k&W&\text{internal wedges}&\text{adjacent equal-union pairs}\\ \hline
7&35&7&7\\
9&126&20&20\\
11&462&44&44\\
13&1716&118&118\\
15&6435&329&329.
\end{array}                                         \tag{7.1}
\]

The wedge theorem has zero discrepancies.  The factor-level reconstruction
gives:

\[
\begin{array}{c|c|c|c}
k&\text{component lengths}&\text{wedges}&
 \#\text{wedges with 0/1/2 marked q2 sides}\\ \hline
13&1547+169&104+13&(65,39,0)+(0,13,0)\\
15&6390+45&330+0&(270,45,15)+(0,0,0).
\end{array}                                         \tag{7.2}
\]

Thus Claude's `k=13:104` count is the large component only; the complete
factor has 117 wedges.  The `104/104` and `315/330` large-component
three-OR diagnostics reproduce exactly, but remain depth-two measurements.
Their uniqueness counters are component-local; an occurrence on another
component can only add a surviving global provider and make the full factor
safer.

The winner-path and factor counts must not be conflated.  The retained
`k9_cycle.json` has 18 wedges, while the separately authenticated dead QRTR
factor has zero; the `k=9` winner has 20.  The retained
`k11_repo_cycle.json` has 44 wedges and matches the winner cycle, while
`k11_cycle.json` is a different 33-wedge cycle.

The remote dead-factor certificates are

```text
/dev/shm/k15_frr_h60/qrtr9_all.json
  4ea4249ad817cea1594a85b66954478f21e7a679255d2bacae4092ecdda5dfd9
/dev/shm/qrtr9_factor.json
  1e451a46b3b5cceead9ca4c924cd6e7cda30c42047ff0c5ef19a38bc4be5d1bf
```

They encode cyclic Johnson components of lengths `18,99,9`, all with zero
wedges.

The named Claude scripts were not present in the repository or the local
`Downloads/work` directory.  Remote volatile copies were later located,
but their scopes confirm the theorem boundary: `killerthm.py` scans the
largest component, rank `r+2`, and bounded windows; `spillfinal.py` evaluates
the three-OR predicate rather than all higher kernels; `wedgeaudit.py` uses
a bounded window and a live glob.  Their counts are useful measurements, not
a proof of (6.1).

The located volatile script hashes are `absruns.py` `5487c890...`,
`killerthm.py` `60f53b3b...`, `spillfinal.py` `6c2cca86...`, and
`wedgeaudit.py` `ce1de643...`.  They were not copied into this report as
theorem sources; the independent local replay above is the frozen
certificate.

## 8. Frozen artifacts

The independent replay is

```text
scratch/audit_ad_wedge_spill_ray_socket_20260730.py
  2029e7df58204133df291f9f10f6b7b4792c2ac9140edc7126080b1c7f954b7e
scratch/ad_wedge_spill_ray_socket_20260730.audit.json
  e6298b23401c077834d7139832c2c21f61fa4dee1a6092f5f85f4c76483cf6a1
payload
  efc5eae904742e1b13705c6ed62c0e868732d95efe6f9e9d1693cbd706284d59
```

The JSON status is

```text
PASS_SCOPED_FIXED_WIDTH_RAY_AND_SOCKET_AUDIT
```

and its internal payload hash is recorded in that file.  No SAT, exhaustive
subset search, web access, or sustained local computation was used.

Claude's parent `LEDGER.md` was actively appended during the audit, so the
certificate binds to the relevant section between the `ABSENCE-RUN` and
`PURE-BRAID` headings, SHA
`1f37e9d7a5c0159a185f3d0d9065235c215f2684addfbe73c121f322d216c172`.
The separately frozen `WEDGE_SPILL_NOTES_20260730.md` has SHA
`bdcc69f8b049b97e51a45f22d879b7953eccfe259c8f9dd8ef78df8e43454f84`,
and the protected outward-ray theorem SHA
`1aab18f0e6e7d66e975456561d7986685ad97d5d9594407fd12a682c7a587013`.

The decisive proved boundary is:

* local wedge equality: proved;
* one-sided three-OR: exact for `q=2` only;
* arbitrary-depth fixed-width killers: outward rays;
* zero-spill orbit dispersion: still open for the protected factor family;
* literal upper repair: proved with exact cost `b(k-r-1)`.
