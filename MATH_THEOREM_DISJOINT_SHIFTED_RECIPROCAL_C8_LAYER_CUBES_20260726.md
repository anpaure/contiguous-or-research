# Disjoint shifted reciprocal-\(C_8\) layers: exact cubes, collisions, and the remaining sign gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 B=C_s=\operatorname {Cat}_s,
 \qquad n=2s+1,
\]

and fix \(u\) pairwise disjoint four-coordinate slots in a Dyck root.
At slot \(j\), use the certified endpoint-inert rectangle

\[
                    1100\longleftrightarrow1010.      \tag{0.1}
\]

The slots may be consecutive; their interiors must be disjoint.  A shared
boundary state is harmless because every rectangle fixes both boundary
states.

There is no switch-stability or component-size obstruction for fixed
\(u\).

1. Every layer contains exactly \(C_{s-2}\) reciprocal rectangles,
   independently of its slot position.
2. Any chosen layers are simultaneously exact.  Their partial root
   involutions commute, preserve one another's eligibility, and the full
   \(X/Y\) overlay components are literal cubes of size at most \(2^u\).
3. For any specified \(h\) layers, the common root support has the exact
   size
   \[
                           2^h C_{s-2h}.              \tag{0.2}
   \]
   In particular two layers meet in \(4C_{s-4}\) roots, arranged into
   \(C_{s-4}\) commuting squares.
4. If all \(u\) layers are installed and a root is eligible in exactly
   \(r\) of their slots, its rooted edit distance is exactly \(2r\) and
   its full component has size \(2^r\).  Consequently
   \[
   \boxed{
   \Xi_u={4\over C_s}\sum_{h=1}^u
       \binom uh h2^h C_{s-2h}}
   \longrightarrow
   \boxed{{u\over2}\left({9\over8}\right)^{u-1}}.   \tag{0.3}
   \]
   Thus every fixed \(4\le u\le7\) has \(\Xi_u=O(1)=o(\sqrt s)\),
   despite the overlaps.
5. The total marked first-boundary supply is exactly
   \[
                              uC_{s-2}.               \tag{0.4}
   \]
   Hence the raw scalar demand \(\delta_\theta C_s\) asks for
   \[
       u\ge
       \left\lceil\delta_\theta{C_s\over C_{s-2}}\right\rceil
       =\lceil16\delta_\theta+o(1)\rceil,            \tag{0.5}
   \]
   which ranges from four to seven.

The combinatorial layer problem is therefore positive: seven disjoint
shifted layers exist for every \(s\ge14\), are jointly exact, and have
full components of size at most \(128\).

What does **not** follow is a coefficient-one repair.  Each layer has the
same favourable **local/tagged** sign \(e_3-e_2\).  For odd-start slots
this is a physical even-to-odd transfer on a distinct adjacent coordinate
pair.  It is a common favourable sign only for a consumer which charges
all these transported local pairs with the same orientation.  The global
first-insertion cell sees only the first slot, and an arbitrary untagged
carrier/collar push-forward can identify a positive target from one
context with a negative target from another.

For the actual common canonical base there is a stronger negative answer.
Every odd-start layer uses one generator
\((2i\ 2i+1)\) of the even-pair coordinate group.  Its exact multirank
column is a boundary \(\partial_{2i,2i+1}z\), and therefore has zero total
on every target orbit of that group.  This remains true after all physical
target collisions and all mixed-window interactions.  In particular the
fatal parent pair \(\{2,3\}\) retains its full canonical mass, giving an
\(\Omega(C_s)\) PCap lower bound.  Hence four to seven such layers do
**not** have a common favourable untagged PCap orientation.  Escaping
requires a non-coordinate packet which crosses the even-pair target
orbits.

There is also a sharp projection no-go.  Although the factor-space
component may have \(u\) cube directions, one fixed consecutive
intersection window sees at most the two rectangle bits at its two
boundaries.  Every strictly interior rectangle cancels by the octahedral
triple-intersection identity.  Hence four to seven disjoint layers cannot
give four to seven independent repairs of one physical carrier
occurrence; their supply (0.4) is genuinely an all-start/tagged sum.

## 1. Fixed slots and partial involutions

Choose integers

\[
 0\le a_1<a_1+4\le a_2<\cdots<a_u+4\le2s.           \tag{1.1}
\]

Slot \(j\) is the interval

\[
 I_j=\{a_j+1,a_j+2,a_j+3,a_j+4\}.                   \tag{1.2}
\]

A root \(x\in D_s\) is **\(j\)-eligible** when its restriction to
\(I_j\) is \(1100\) or \(1010\).  Define the partial involution
\(\tau_j\) by interchanging these two words and leaving every other bit
fixed.

Both local words are balanced nonnegative excursions.  Hence deleting an
eligible block from a Dyck word leaves a Dyck word, and inserting either
block at the same gap in a shorter Dyck word produces a Dyck word.  It
follows at once that \(\tau_j\) maps \(D_s\) to itself on its domain.

### Lemma 1.1 (commuting eligibility)

For \(i\ne j\), \(\tau_i\) and \(\tau_j\) commute wherever both are
defined, and \(\tau_i\) preserves \(j\)-eligibility.

#### Proof

The two maps change disjoint sets of four bit positions.  In particular,
neither changes the four-bit word inspected by the other.  Their two bit
substitutions therefore commute literally. \(\square\)

This is stronger than preservation of Dyck legality: the complete set of
eligible layer indices is constant on every orbit of the partial
involutions.

## 2. Exact support and collision counts

### Lemma 2.1 (multi-slot insertion bijection)

For every specified set \(T\subseteq[u]\), \(|T|=h\), the number of
Dyck roots eligible at every slot in \(T\) is

\[
                          \boxed{2^h C_{s-2h}}.        \tag{2.1}
\]

#### Proof

Delete the four bits in every slot in \(T\), from right to left.  Every
deleted word is one of two balanced nonnegative excursions, so the result
is a Dyck word of semilength \(s-2h\).  Record the binary choice
\(1100/1010\) at each deleted slot.

Conversely, insert the recorded excursions from left to right at the
adjusted gaps.  Inserting a balanced nonnegative excursion at any gap of a
Dyck word preserves all prefix heights.  These two operations are inverse.
There are \(C_{s-2h}\) reduced roots and \(2^h\) orientation choices.
\(\square\)

For \(h=1\), the two orientations pair, so one layer has exactly

\[
                              C_{s-2}                 \tag{2.2}
\]

rectangle edges and \(2C_{s-2}\) active roots.  For two layers, their
common support has \(4C_{s-4}\) roots.  For each reduced root, the four
orientations form one square, whose two opposite-edge matchings are the
two layer involutions.  Thus the layers have no common edge and exactly
\(C_{s-4}\) square collisions.  More generally an \(h\)-fold collision
is one \(h\)-cube for each reduced root in \(D_{s-2h}\).

The union of the layer supports has the exact size

\[
 R_u=\sum_{h=1}^u(-1)^{h+1}\binom uh2^hC_{s-2h},     \tag{2.3}
\]

and hence, for fixed \(u\),

\[
                  {R_u\over C_s}\longrightarrow
                  1-\left({7\over8}\right)^u.        \tag{2.4}
\]

For \(u=4,5,6,7\), these limiting active-root fractions are respectively

\[
 1-(7/8)^4,\quad1-(7/8)^5,\quad1-(7/8)^6,\quad1-(7/8)^7.          \tag{2.5}
\]

They are approximately \(0.414,0.487,0.551,0.607\).

## 3. Simultaneous physical exactness

The root involutions alone are not enough: one must check the factor
ledgers after several layers share rows.  The endpoint-inert nature of the
rectangle supplies the missing statement.

### Theorem 3.1 (disjoint-slot tensorization)

Let every slot be a literal rooted-tree/forest context for the certified
reciprocal rectangle.  Installing any subset of the \(u\) complete layers
produces an anchored exact \(D_s\)-port factor.  The order of installation
does not matter.

#### Proof

One elementary rectangle replaces two local row segments by the reciprocal
segments with the same two entrance states, the same two exit states, the
same six middle-state tokens, and the same four adjacent-union colours.
It therefore preserves both local ownership ledgers and fixes its boundary
states.

Two slot interiors are disjoint.  If they lie on different rows, their old
token sets are disjoint because the starting factor is exact.  If they lie
on the same row, the first replacement returns to its original boundary
state before the second slot begins.  It changes neither the second local
segment nor its exterior state.  Adjacent slots may share their common
boundary state, but both replacements fix it.  Hence the second rectangle
remains literally alternating and ledger-balanced after the first, and
the two replacements commute.

Induct on the number of installed slots.  At every step all middle-state
and adjacent-union tokens are still owned exactly once, every root label is
unchanged, and every row still ends at its prescribed complement.  This is
an anchored exact factor. \(\square\)

This theorem uses genuinely disjoint rooted contexts.  Merely selecting
two four-coordinate sets without proving that their canonical row
segments are disjoint would not suffice.

## 4. Complete full-overlay components

For a root \(x\), let

\[
 J(x)=\{j:x\text{ is }j\text{-eligible}\}.           \tag{4.1}
\]

By Lemma 1.1, \(J(x)\) is constant under every allowed toggle.  All bits
outside the eligible slots are also fixed.  Thus its root orbit is

\[
              \{\tau_Tx:T\subseteq J(x)\},           \tag{4.2}
\]

and has size \(2^{|J(x)|}\).

### Theorem 4.1 (the full components are exactly the root cubes)

Compare the original factor with the factor obtained by installing all
\(u\) layers.  The roots in (4.2) form one component of the full
state-and-colour ownership overlay, and every full component is obtained
this way.

#### Proof

Every new row is assembled solely from old row segments whose roots differ
by toggles in \(J(x)\).  Hence no ownership edge leaves (4.2).

For each \(j\in J(x)\), the local rectangle exchanges a nonempty middle
segment between the two roots \(y\) and \(\tau_jy\).  A state or colour in
that segment gives a cross-owner overlay edge between these two root
vertices.  Such edges form every coordinate edge of the cube (4.2), so
the induced overlay is connected.  This uses both state and colour
tokens, and therefore proves the assertion for the full overlay. \(\square\)

For a fixed subset \(J\subseteq[u]\), \(|J|=r\), the number of roots
whose eligibility set is exactly \(J\) is

\[
 N_J=\sum_{h=0}^{u-r}(-1)^h\binom{u-r}{h}
                  2^{r+h}C_{s-2r-2h}.               \tag{4.3}
\]

Consequently the number of \(r\)-cube components with that particular
eligibility set is \(N_J/2^r\).  For fixed \(u\), the asymptotic root
distribution is binomial:

\[
 {1\over C_s}\sum_{|J|=r}N_J
       \longrightarrow
       \binom ur\left({1\over8}\right)^r
                    \left({7\over8}\right)^{u-r}.   \tag{4.4}
\]

In particular the largest component has \(2^u\) roots.  For seven layers
this is \(128\), independent of \(s\).

## 5. Exact edit moment

One elementary reciprocal rectangle makes one adjacent transposition in
the deletion order and one in the insertion order of each of its two
rows.  Its rooted distance is therefore two.  In disjoint slots these
inversion pairs are disjoint, so for a root with \(|J(x)|=r\),

\[
                              d(x)=2r.                \tag{5.1}
\]

Its full component has size \(2^r\).  Hence

\[
 C_s\Xi_u=
       \sum_{x\in D_s}2^{|J(x)|}\,2|J(x)|.           \tag{5.2}
\]

Introduce the eligibility polynomial

\[
 Z_u(t)=\sum_{x\in D_s}t^{|J(x)|}.
\]

Inclusion-exclusion in the equivalent form
\(t^{|J|}=\sum_{T\subseteq J}(t-1)^{|T|}\), together with Lemma 2.1,
gives

\[
 Z_u(t)=\sum_{h=0}^u\binom uh
             \bigl(2(t-1)\bigr)^h C_{s-2h}.         \tag{5.3}
\]

Equations (5.2)--(5.3) give

\[
 \Xi_u={4Z_u'(2)\over C_s}
       ={4\over C_s}\sum_{h=1}^u
             \binom uh h2^hC_{s-2h},                \tag{5.4}
\]

which is (0.3).  Since \(C_{s-2h}/C_s\to16^{-h}\) for fixed \(h\),

\[
 \Xi_u\longrightarrow
 4\sum_{h=1}^u\binom uh h8^{-h}
 ={u\over2}\left({9\over8}\right)^{u-1}.           \tag{5.5}
\]

For \(u=4,5,6,7\), the limits are

\[
 {729\over256},\qquad
 {32805\over8192},\qquad
 {177147\over32768},\qquad
 {3720087\over524288},                              \tag{5.6}
\]

approximately \(2.848,4.005,5.406,7.095\).  All are constant, so all
four candidate layer counts pass \(\Xi=o(\sqrt s)\).

For growing \(u\), formula (5.5) suggests the separate necessary scale
\(u(9/8)^u=o(\sqrt s)\) whenever the fixed-\(u\) Catalan ratios remain
uniform.  No growing-\(u\) uniformity is asserted here.

## 6. Supply, orientation, and maximum layer count

Suppressing a common exterior from one rectangle gives the marked
first-boundary ledger

\[
                              e_3-e_2.                \tag{6.1}
\]

Therefore every layer supplies one oriented unit per rectangle and the
tagged sum of \(u\) layers is exactly \(uC_{s-2}\), proving (0.4).  The
supports may overlap in roots, but their marked occurrences lie in
different slot interiors and hence remain distinct.  Root collisions do
not reduce the tagged count.

If slot \(j\) begins at an odd physical coordinate \(k_j\), then in the
suppressed coordinate-label projection (6.1) is the literal transfer

\[
                         e_{k_j+2}-e_{k_j+1},         \tag{6.2}
\]

from an even coordinate to its following odd coordinate.  Choosing

\[
                         k_j=4j-3                    \tag{6.3}

makes the \(u\) slots disjoint and gives the coherently oriented pairs

\[
           (2,3),(6,7),(10,11),\ldots,(4u-2,4u-1).   \tag{6.4}

Thus every score which assigns the same favourable orientation to these
transported local pairs sees all \(u\) layers with one sign.  The exact
raw scalar threshold is (0.5).  Since
\(\delta_\theta\in[1/4,7/16)\), it asks for four through seven layers for
all sufficiently large \(s\).

At the level of literal slots, the only packing restriction is

\[
                              2u\le s.                \tag{6.5}

Thus \(u_{\max}=\lfloor s/2\rfloor\), and every one of the requested
values is available once \(s\ge14\).

There are, however, two exact sign qualifications.

1. The distinguished **global** first insertion of a Dyck root occurs
   before every later slot.  A later rectangle does not change it.  Hence
   only the slot at the first boundary can repair a demand concentrated
   on that single occurrence; the other \(u-1\) layers are useful only in
   the all-start or context-tagged parent ledger.
2. Under a physical carrier map a local target has the form
   \[
             \Gamma_{j,C}(a)=O_{j,C}\mathbin{\dot\cup}\{k_j+a-1\}.
                                                               \tag{6.6}
   \]
   Distinct active coordinates do not alone prevent
   \(\Gamma_{j,C}(3)=\Gamma_{j',C'}(2)\), because the two exterior collars
   may differ by exchanging those coordinates.  Tagged signs therefore
   survive automatically, but untagged physical signs require either an
   injective/private-anchor condition on the collars or a direct
   collision ledger.

The initially apparent next lemma would ask these four to seven columns to
retain a common favourable projection after physical aggregation.  Section
8 proves that lemma false for the canonical common base: every column is
trapped in the zero-sum subspace of the even-pair target orbits.  The next
constructive lemma must instead include at least one non-coordinate packet
whose physical carrier crosses those orbits, while retaining the bounded
cube/component ledger proved above.

## 7. Exact maximum seen by one physical window

Let one elementary rectangle replace the middle state \(M\) between its
unchanged neighbours \(L,R\) by \(M'\).  The octahedral set identity is

\[
                         L\cap M\cap R
                         =L\cap M'\cap R.             \tag{7.1}
\]

### Theorem 7.1 (two-boundary projection)

For the disjoint-slot construction, fix any consecutive intersection
window in any affected row.  Its physical target depends on at most two
of the \(u\) layer choices, namely the choices at the two boundary phases
of the window.  It therefore assumes at most four values.

#### Proof

If a switched middle state lies strictly inside the window, the window
also contains its two immediate neighbours.  The slots are disjoint and
endpoint-inert, so those neighbours remain unchanged even after all other
layers are installed.  Replacing \(L,M,R\) by \(L,M',R\) leaves the
window intersection unchanged by (7.1).  A switch outside the window is
irrelevant.  Only a switch at either boundary can survive, giving at most
two Boolean choices. \(\square\)

Thus there are two different exact maxima:

\[
 \boxed{u_{\rm exact}=\lfloor s/2\rfloor}
 \qquad\text{but}\qquad
 \boxed{u_{\rm visible\ per\ window}\le2}.           \tag{7.2}
\]

The first number controls factor legality and the full ownership cube;
the second controls a single physical carrier target.  In particular,
the quantity \(uC_{s-2}\) can meet \(\delta_\theta C_s\) only when the
consumer legitimately sums the distinct marked starts supplied by the
different slots.  It cannot be used as four-to-sevenfold supply for one
fixed parent-window occurrence.

## 8. Full four-arm columns and the orbit obstruction

Fix a protected rank and put \(\ell=s-q-1\).  For a rectangle occurrence
\(e\) in layer \(j\), let \(\beta_j,\gamma_j\) be its fixed active
coordinate pair and write

\[
 \partial_j K=e_{K\cup\{\gamma_j\}}
                    -e_{K\cup\{\beta_j\}}.           \tag{8.1}
\]

After rotating the local omitted word, let
\(\mathsf E_e,\mathsf O_e\) be its two common parity tails.  The exact
isolated full column is

\[
 d_{q,e}=\partial_j\bigl(
       \operatorname {suf}_{\ell}(\mathsf O_e)
      +\operatorname {suf}_{\ell}(\mathsf E_e)
      -\operatorname {pre}_{\ell}(\mathsf E_e)
      -\operatorname {pre}_{\ell}(\mathsf O_e)
                         \bigr).                      \tag{8.2}
\]

Thus the complete isolated column of layer \(j\) is exactly

\[
 \boxed{
 D_{j,q}=\partial_j Z_{j,q},\qquad
 Z_{j,q}=\sum_{e\in\mathcal E_j}
       \bigl(\operatorname {suf}_{\ell}\mathsf O_e
             +\operatorname {suf}_{\ell}\mathsf E_e
             -\operatorname {pre}_{\ell}\mathsf E_e
             -\operatorname {pre}_{\ell}\mathsf O_e\bigr).}       \tag{8.3}
\]

For proper nonboundary ranks the four cores of one occurrence are
distinct, so \(\|d_{q,e}\|_1=8\).  Formula (8.3), rather than its one
marked suffix arm, is the actual layer column.

Let

\[
 H_s=\langle(2\ 3),(4\ 5),\ldots,(2s-2\ 2s-1)\rangle             \tag{8.4}
\]

act on physical targets, with every exterior collar transported along
with its local target.  For an \(H_s\)-orbit \(\mathcal O\), define the
orbit-sum projection

\[
                         \Pi_{\mathcal O}(v)
                         =\sum_{T\in\mathcal O}v(T).   \tag{8.5}
\]

### Theorem 8.1 (all-rank orbit cancellation)

For every odd-start shifted layer, every protected rank, and every target
orbit \(\mathcal O\),

\[
                         \boxed{\Pi_{\mathcal O}(D_{j,q})=0.}       \tag{8.6}
\]

The same identity holds for the actual simultaneous final-minus-base
column, including all mixed-window interaction terms.

#### Proof

In (8.1), the two targets differ by the generator
\((\beta_j\ \gamma_j)\in H_s\), and hence belong to the same orbit.
Every elementary boundary therefore has orbit sum zero.  Sum (8.2) over
the layer to obtain (8.6).

For the simultaneous statement, install the layers sequentially.  At
each step, on a packet with roots \(P,\tau_jP\), the two new rows are
\(\tau_j\) applied to the two old rows in the opposite root order:
\[
 \omega_{\rm new}(P)=\tau_j\omega_{\rm old}(\tau_jP),
 \qquad
 \omega_{\rm new}(\tau_jP)=\tau_j\omega_{\rm old}(P).
\]
Thus there is a start-preserving bijection from the complete old
two-row pointed-window multiset to the new one, and coordinate
equivariance sends every target to another target in the same orbit.
Summing packets and then inducting over the layers proves the claim
without assuming additivity of their isolated columns.  Equivalently,
on a Boolean root cube one may reindex roots by the chosen coordinate
product \(h\); the new complete target multiset is \(h_*\) of the old
one.
\(\square\)

This is the separating invariant requested by the four-arm formula.  It
is targetwise stronger than cancellation of the tagged scalar sum, and
physical collisions cannot violate it.

### Corollary 8.2 (fatal-pair PCap obstruction)

Embed the \(D_s\) factor in its standard one-step parent and inspect the
distinguished pair of parent boundary-occurrence families.  Write
\(\mu^\circ\) for this marked two-boundary subledger.  Its canonical
loads on the orbit
\(\mathcal O_1=\{2,3\}\) are

\[
                         d=C_s,qquad e=C_{s-1}.       \tag{8.7}
\]

Transport these two canonical marked occurrence families through the
packet bijections in the proof of Theorem 8.1.  They remain distinct
physical occurrences, and after any sequence of the disjoint odd-start
layers their transported subledger satisfies

\[
                \mu^\circ(2)+\mu^\circ(3)=d+e.       \tag{8.8}
\]

For cap \(p=d/\theta\), \(4\le\theta<16\), their contribution to the
cap excess is therefore at least

\[
 \boxed{
  (\mu^\circ(2)-p)_++(\mu^\circ(3)-p)_+
       \ge d+e-2p
       =d\left(1+{s+1\over2(2s-1)}-{2\over\theta}\right)
       =\Omega(d).}                                  \tag{8.9}
\]

Equivalently,

\[
 \max\{\mu^\circ(2),\mu^\circ(3)\}
 \ge {d+e\over2}
 =d\,{5s-1\over4(2s-1)}>p.                           \tag{8.10}
\]

The complete physical loads dominate this transported marked subledger
coordinatewise, so the same lower bound holds a fortiori for their PCap
contribution, even in the presence of arbitrary nonnegative background
occurrences.

Thus the later shifted pairs do not amplify the first
\(2\leftrightarrow3\) split: they act in other \(H_s\)-orbits, while the
first layer can only redistribute the fixed mass inside
\(\mathcal O_1\).  The untagged physical PCap gate is rigorously closed
for this whole coordinate-layer class.

## 9. Mixed-window collision and Gram boundary

The orbit obstruction does not require the isolated columns to add.
Nevertheless their interaction has a useful exact bound.  At one depth,
a consecutive window depends on at most its two boundary switches.  Hence
the simultaneous-minus-isolated remainder has no interactions of order
three or higher:

\[
 \mathcal R_q=D_q^{\rm simultaneous}-\sum_{j=1}^uD_{j,q}
             =\sum_{1\le i<j\le u}\mathcal R_{ij,q}. \tag{9.1}
\]

Only roots eligible in both slots can contribute to
\(\mathcal R_{ij,q}\); there are exactly \(4C_{s-4}\) such roots.  For
one root, at most one cyclic window of the fixed length has the two
switched phases as its boundaries.  Its Boolean mixed difference has
\(L^1\)-norm at most four.  Therefore

\[
 \boxed{
 \|\mathcal R_{ij,q}\|_1\le16C_{s-4},\qquad
 \|\mathcal R_q\|_1
       \le16\binom u2 C_{s-4}.}                      \tag{9.2}
\]

This bound is constant-density, not \(o(C_s)\), for fixed \(u\):
\(C_{s-4}/C_s\to1/256\).  Thus root-cube boundedness alone does not make
the untagged columns asymptotically orthogonal.

For the isolated aggregate columns, the four-arm formula gives the
unconditional estimates

\[
 \|D_{j,q}\|_1\le8C_{s-2},qquad
 |\langle D_{i,q},D_{j,q}\rangle|
       \le8C_{s-2}^2,                                \tag{9.3}
\]

the second following from
\(\|D_{j,q}\|_\infty\le C_{s-2}\).  No sign follows from (9.3).
Indeed the tagged four-arm module has a one-for-one locked collateral:
the desired suffix arm and the other suffix arm in (8.2) have the same
coefficient, while both prefix arms have the opposite coefficient.  A
common orientation multiplies all four together.  Other disjoint layers
cannot cancel that collateral in the tagged direct sum; only explicit
untagged physical target collisions could do so, and Theorem 8.1 shows
that such collisions still cannot move mass across an \(H_s\)-orbit.

The rigorous distinction is therefore:

* **all-start tagged coherence:** yes; all \(uC_{s-2}\) local marked arms
  have the same chosen orientation;
* **simultaneous physical exactness and bounded components:** yes, by
  Theorems 3.1 and 4.1;
* **untagged physical PCap coherence on the canonical base:** no, by the
  orbit invariant and (8.9).
