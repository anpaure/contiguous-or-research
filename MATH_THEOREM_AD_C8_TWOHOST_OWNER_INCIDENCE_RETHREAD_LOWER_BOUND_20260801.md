# Folded C8 two-host planting has an exact linear owner-rethread floor

Date: 2026-08-01  
Lane: AD, folded-octagon owner/legal-host closure  
Status: unconditional source-to-owner incidence theorem; exact all-`d`
application to the quotient-folded C8 owner bank; independently replayed
strict-upper and terminal-birail ledgers.  Exterior planting, a nonflat
deadline-`d+2` compiler, and a new owner bank remain open.  No
`B(k)+O(1)` conclusion is claimed.

## 0. Sharp verdict

The terminal two-ray Hall problem is no longer the obstruction.  Its two
marginals are

\[
        \{0^{d-1},1,\ldots,d-1\},
\]

so `N=2d-2`, `E_L=E_R=d-1`, and antitone pairing has deficiency zero.
The isolated two-host word even exhibits a literal diagonal matching of all
`2d-2` ray tasks.

The physical internal-host row has a sharp linear obstruction.  Suppress a
fixed core `K` and write the active labels as `z,a_0,a_1,a_2,a_3`.  Both
required hosts contain

\[
                              A=\{a_1,a_3\}.             \tag{0.1}
\]

In the entire simple quotient-folded owner bank there is exactly one owner
containing `A`.  An internal depth-`d` source letter occurs in `d+1` owner
windows.  If the two full hosts are planted at the two aligned anchor
addresses, which are a distance `d` apart, their incidence intervals overlap
once and require

\[
                              2d+1                       \tag{0.2}
\]

owner rows containing `A`.  Consequently:

* the unchanged folded owner multiset admits **no** internal occurrence of
  even one host;
* one internal host requires at least `d` new/nonretained owner occurrences;
* two internal full hosts fixed at the aligned distance-`d` addresses require
  at least

\[
                              \boxed{2d}                 \tag{0.3}
\]

  new/nonretained owner occurrences (and hence replacements when the final
  owner word has the same length).

Thus no bounded-support flat internal rethread can physicalize even one full
host as `d` grows.  The `2d` statement is specifically an owner-occurrence
bound for the distance-`d` aligned placement; it is not a bound on source
edits, Johnson-edge edits, or every relocated/exterior design.  The theorem
does not rule out a linear-support but zero-net-length rethread, an exterior
occurrence, or the audited nonflat full-block lift.

There is a separate strict-upper obstruction.  An upper-support-safe folded
path has `8d+23` edges but rank only `16` in the upper-colour partition
matroid, hence nullity `8d+7`.  Any route insisting that this literal path
lie in an upper-rainbow Catalan forest must replace at least `8d+7` of its
edges.  Support-surjectivity is not upper-rainbow exactness.

Finally, planting the isolated hosts does not make the move regenerative.
For the canonical aligned upper-15 source pair, the composed signed graded
residue has one unit on each shore at every width

\[
                         2d+5,\ldots,5d+12,              \tag{0.4}
\]

and graded `L1=6d+16`.  On the simultaneously aligned and
upper-support-safe face, the exact residual is larger: a capped-triangular
profile of per-sign mass `9d+24`, hence `L1=18d+48`.  Common exterior screens
do not cancel either profile.  The exact remaining object is therefore a
nonliteral owner/upper rethread with a phase-sensitive context transporter,
not another terminal Hall argument.

## 1. General owner-incidence theorem

Let `Q=(Q_0,...,Q_(M+d-1))` be a source word and let

\[
                    T_i=\bigcup_{j=i}^{i+d}Q_j
                    \qquad(0\le i<M)                    \tag{1.1}
\]

be its depth-`d` owner chronology.  For a label set `A` and a source
position `p`, define the clipped incidence interval

\[
 I_d(p)=\{i:0\le i<M,\ i\le p\le i+d\}.
                                                               \tag{1.2}
\]

### Theorem 1.1 (source support forces an owner interval)

If `A subseteq Q_p`, then

\[
                         A\subseteq T_i
                         \quad(i\in I_d(p)).             \tag{1.3}
\]

For a set `P` of source positions satisfying `A subseteq Q_p`, every
resulting owner word has at least

\[
                         \left|\bigcup_{p\in P}I_d(p)\right|  \tag{1.4}
\]

occurrences containing `A`.

#### Proof

For `i in I_d(p)`, the union in (1.1) includes the term `Q_p`, hence includes
`A`.  Taking the union of the forced index sets proves (1.4).  \(\square\)

To count rethread cost without fixing an order or requiring equal lengths,
let `m_T(X)` be the multiplicity of owner value `X`, and put

\[
 h^+(T,T')=|T'|-\sum_X\min\{m_T(X),m_{T'}(X)\}.        \tag{1.5}
\]

This is the number of occurrences of `T'` which cannot be retained from
`T` after arbitrary reordering.  For equal lengths it is the minimum number
of replacements; for a longer word it also counts newly inserted owners.

### Corollary 1.2 (multiset edit lower bound)

Let

\[
 n_A(T)=\sum_{X:\,A\subseteq X}m_T(X).                 \tag{1.6}
\]

If `T'` is induced by a source having `A` at every position in `P`, compute
`I_d(p)` from (1.2) with the owner length `|T'|`.  Then

\[
 h^+(T,T')\ge
 \left|\bigcup_{p\in P}I_d(p)\right|-n_A(T).           \tag{1.7}
\]

#### Proof

At most `n_A(T)` of the required `A`-containing occurrences can be retained
from the old multiset.  Every other required occurrence contributes one to
(1.5).  \(\square\)

More generally, if `p<q` are internal and `h=q-p<=d`, then

\[
 \left|I_d(p)\cup I_d(q)\right|=d+1+h,\qquad
 h^+(T,T')\ge d+h\quad\text{when }n_A(T)=1.            \tag{1.8}
\]

For `h>=d+1` the intervals are disjoint and the corresponding bound is
`2d+1`.  In particular, if `q=p+d`, then

\[
 I_d(p)=[p-d,p],\qquad I_d(p+d)=[p,p+d],               \tag{1.9}
\]

so their intersection is `{p}` and their union has size `2d+1`.

## 2. Exact folded-owner pair census

Let `F={f_0,...,f_(d+1)}`.  Quotienting the literal four-block bank by owner
value gives `8d+24` owners.  The active parts of these owners belong to the
fixed sixteen-element template

\[
\begin{split}
 &\{za_i:0\le i<4\}\ \cup\ \{a_i:0\le i<4\}\ \\
 &\quad\cup\ \{a_0a_1,a_1a_2,a_2a_3,a_0a_3\}\ \\
 &\quad\cup\ \{za_0a_2,za_1a_3,a_0a_1a_2,a_0a_2a_3\}.
                                                               \tag{2.1}
\end{split}
\]

This list is obtained directly from the eight active octagon vertices, the
seven intersection/union screens, and the four Klein relabellings.  It is
independent of `d`.  Only one template contains both `a_1` and `a_3`, namely
`za_1a_3`; it occurs at one union screen, with filler part `F[1,d]`.
Therefore, in either phase,

\[
 \{T\text{ in the folded bank}:\{a_1,a_3\}\subseteq T\}
 =\{K\cup\{z,a_1,a_3\}\cup F[1,d]\}.                  \tag{2.2}
\]

In particular `n_A(T)=1` for the simple Hamilton owner cycle or any of its
openings.

The two isolated ray hosts are

\[
\begin{aligned}
 X_L&=K\cup\{z,a_1,a_3,f_1\},\\
 X_R&=K\cup\{z,a_1,a_3,f_d\}.                          \tag{2.3}
\end{aligned}
\]

For completeness, let the one-sided prefix and suffix anchors be at `p<q`.
Their owner-incidence intervals overlap in `d-(q-p)+1` rows when `q-p<=d`;
every overlapping row contains both `a_1,a_3`.  Equations (2.1)--(2.2) and
owner simplicity therefore give `q-p>=d`.  The common cross-host interval
has width `q-p+1` and deadline `d+1`, giving `q-p<=d`.  Hence their aligned
addresses are forced to differ by `d`.  If the full
hosts are planted at those two addresses, Theorem 1.1 and (2.2) show that
the old owner multiset cannot realize either host internally.  Corollary 1.2
gives `d+1-1=d` new/nonretained occurrences for one host and
`2d+1-1=2d` for the distance-`d` pair.  This proves (0.3) for every `d` in
the aligned-address placement.  Relocating a full host, clipping it at an
exterior boundary, or overlapping addresses in a quotient weave changes the
two-host formula and is not excluded; the one-host linear obstruction still
holds for every internal full host.

The count is an incidence lower bound, not an existence theorem.  The
natural whole-host insertion attains the same order of changed incident
rows but creates two rank-`r+1` owners.  On the independently audited
aligned face (`5<=d<=12`), the natural paired-base insertion keeps rank `r`
and residence but creates a triple stutter, changes the owner and lower-q1
counters between phases, and leaves `8d-16` source-deck values each way.
Neither is a flat factor move.  The all-`d` conclusion needed here is the
incidence floor, not an extrapolation of that finite paired-base ledger.

## 3. The strict-upper row is a different obstruction

The exact folded upper-load lemma from
`MATH_THEOREM_HA_C8_FOLDED_TWO_RAY_COMMONCAP_HALL_AND_UPPER_GATE_20260801.md`
gives, for this signature, the cycle load

\[
                              1^8(d+2)^8.               \tag{3.1}
\]

and, after a support-safe cut, the path load

\[
                         1^8(d+1)^1(d+2)^7.             \tag{3.2}
\]

The lemma is all-`d`: at `d=2` the sixteen classes split into eight
singletons and eight load-four classes, and increasing `d` extends each of
the latter eight rails by one edge without changing the binary choices.
The path therefore has `8d+23` edges in only sixteen upper-colour classes.
Its rank in the upper partition matroid is `16`, and its nullity is

\[
                         (8d+23)-16=8d+7.               \tag{3.3}
\]

Any upper-rainbow edge set retains at most one member of each class, so it
can retain at most sixteen edges of the path.  This proves the replacement
floor.

Equation (3.3) applies only to the strict upper-exact forest subclass.  A
literal contiguous-OR word may use repeated immediate upper colours if
other intervals supply the global targets.  Such a construction must prove
the complete target-cell Hall condition directly; it cannot cite the folded
path as an upper-rainbow factor.

## 4. Why the obvious coordinated embeddings still fail

The following failures are now separate and exact.

1. **One split.**  Splitting one internal source letter creates `d`
   decomposition-independent owner windows contained in intersections of
   adjacent rank-`r` owners, hence of rank at most `r-1`.
2. **Two natural hosts.**  Retaining the two whole hosts creates two
   rank-`r+1` rows.  Pairing their phase bases instead creates the triple
   stutter and the deck/palette discrepancy recorded above.
3. **Staggered pair-shared tags.**  For the four `K_(2,2)` tags
   `t_02,t_03,t_12,t_13`, each phase-sensitive width-`d` window forces the
   hit tags to be a matching, whereas the intervening owner-width
   `d+1` window requires a nonmatching.  Three consecutive sensitive
   windows give a contradiction.  Arbitrary staggered supports do not
   remove the four-copy multiplicity.
4. **Quotient folding.**  Folding does solve the central owner/lower-q1/
   Hamilton/residence rows, but (0.3), (3.3), and the graded residue (0.4)
   remain.  It is a physical central comparator, not a closed regenerative
   edge.

The quotient fold is therefore the correct coordinated multi-position
rethread of the literal four-copy bank, while internal host planting itself
provably needs linear support.

## 5. What the birail theorem does close

For the canonical ray marginals,

\[
 N=2d-2,\qquad E_L=E_R=d-1,
 \qquad(E_L+E_R-N)_+=0.                                \tag{5.1}
\]

Thus any physical state which exposes freely pairable ray endpoints has no
terminal scalar Hall defect.  The isolated two-host packet is stronger: its
`2d-2` side cells already form a diagonal matching.  After fixing those
cells, exact ambient completion is ordinary Hall on the remaining target
bank, in one shared deadline/cap state.

This conclusion is conditional on actual host occurrences.  It does not
turn an isolated provider gadget into a contextual relation.  For the
canonical aligned upper-15 fold and opposite two-host word, the residual
signed graded deck has `3d+8` entries on each shore, one at every width in
(0.4).  The aligned upper-support-safe face instead has per-sign mass
`9d+24`.  Pointwise-common exterior screens preserve rather than cancel
these internal residues by the exact screen-additivity lemma.

The nonflat escape is also sharply scoped.  A full-block lift of every old
crossing owner uses `d+2` source letters and preserves the old owner order,
values, and residence.  It is a valid deadline-`+1` interface, not a flat
depth-`d` source, and it does not by itself recycle the graded residue.

## 6. Exact remaining positive theorem

A sufficient physical comparator must now provide one of the following.

* **Flat linear rethread:** replace at least the owner incidences forced by
  (0.3), retain a simple lower-rainbow owner factor, and either replace the
  strict-upper dependence in (3.3) or certify all upper targets by literal
  longer intervals.
* **Exterior/nonflat transport:** move the hosts to clipped endpoint
  intervals or use the `d+2` lifts, while transporting the two rays into one
  matching-closed common-cap state.

In either case it must also supply a phase-sensitive collar which cancels
the full graded residue (0.4), and must conjugate the prepared state to each
adjacent birail obligation without paying fresh length per comparator.

This is compatible with `B(k)+O(1)`: a linear-support exchange may still be
length-neutral if all support is recycled.  What is ruled out is the much
stronger claim that the present folded path admits an `O(1)`-support flat
internal host closure.

## 7. Independent audit

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_ad_c8_twohost_owner_incidence_rethread_lower_bound_20260801.py \
  --write
```

For `2<=d<=12` the replay independently checks:

* `8d+24` folded owner values and the unique owner (2.2);
* all sixteen lower-rainbow degree-two selections in each phase;
* the two upper-support-complete cycles per phase;
* load formulas (3.1)--(3.2) and nullity (3.3);
* the exact `2d+1` two-host incidence union and `2d` edit floor; and
* the zero terminal-birail deficiency.

The finite range is a regression audit.  The active-template proof of (2.2)
and Theorem 1.1 prove the owner bound for every `d`.

Frozen replay hashes at writing time:

```text
scratch/audit_ad_c8_twohost_owner_incidence_rethread_lower_bound_20260801.py
  SHA 1279c9715afaa6bae03c611f179c1a67799fcc4ad86f4082600fa748bf687168

scratch/ad_c8_twohost_owner_incidence_rethread_lower_bound_20260801.audit.json
  SHA e5be57acd4526333c99f1d53e44384f73f5e8f62cdf3e7887bb62f115a400895
  payload a910734adebc669bce87adc1eeb7cdd11eef34c34da3ea89d345ca5afdac130f
```
