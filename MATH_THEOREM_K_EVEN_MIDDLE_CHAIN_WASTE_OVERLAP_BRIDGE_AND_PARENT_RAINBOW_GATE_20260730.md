# Even middle-chain waste: exact inventory, overlap-bridge obstruction, and the parent-rainbow gate

Date: 2026-07-30

## 0. Verdict

Let

\[
 r=\left\lceil\frac k2\right\rceil,
 \qquad W=\binom kr,
 \qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and let (d) be the least nonnegative integer with

\[
 dW+\binom{d+1}{2}\geq\Lambda.
\]

This note audits the proposed parity-sensitive even-dimensional correction

\[
                  W+2^{d-1}
\tag{0.1}
\]

and the weaker binary-padding candidate

\[
 P(d):=2^{\lceil\log _2d\rceil}.
\tag{0.2}
\]

The outcome is sharp.

1. There is an exact, normalization-free first-middle-delivery inventory.
   For a universal word it canonically decomposes every unit of (L-W) into
   a stall, jump, flat duplicate, or ghost duplicate.  For an arbitrary word
   the missing-middle term is retained as in Theorem 1.1.  The retained even
   words have inventories

   \[
   \begin{array}{c|c}
   k& (\text{stall},\text{jump},\text{flat},\text{ghost})\\ \hline
   4&(1,0,0,0)\\
   6&(1,0,0,0)\\
   8&(2,0,0,0)\\
   10&(1,0,1,0)\\
   12&(1,0,1,0)\\
   14&(1,0,1,0)\\
   16&(0,0,3,1).
   \end{array}
   \tag{0.3}
   \]

   This is not the project's compiler short-cell waste and is not the
   elementary equal-OR boundary-event count.  A concurrent exact audit
   refutes the proposed (2^{d-1}) lower bound for elementary boundary
   events already at (k=14).  The only still-open interpretation is the
   unit-charge first-delivery inventory proved here.

2. Injecting Boolean signatures into arbitrary endpoint events is not a
   lower-bound proof.  In the exact endpoint ledger, a both-endpoint event
   has charge zero, left-only and right-only events are the two shores of
   one deficit, and a neither-endpoint event has charge one.  A valid
   injection must land in one fixed charged shore, or carry the exact
   weights.

3. All tested nontrivial even cases (k=4,6,\ldots,14) have (d\in\{1,2\}),
   where (2^{d-1}=P(d)=d).  Thus they do not test either new law.  The verified
   (k=16) word has length (W+4), but this is only an upper bound.

4. The strict two-block (d)-cell odd-to-even overlap has a genuine
   (+1) obstruction.  It can share all (d) parent tail cells, but if it
   also deletes the separate singleton-(z) bridge then it cannot realize
   ({z}).  Consequently that architecture needs length at least

   \[
                         2W_{\mathrm{parent}}+d+1.
   \tag{0.4}
   \]

   At (d=3), this is the observed even length (W_{\mathrm{even}}+4).  It is
   not a global lower bound: the proved six-piece braid escapes the strict
   architecture by creating an internal (z)-ear.

5. The retained (k=16) ghost is now explained literally.  Its middle
   value

   \[
                  0xc279=0x8000\cup0x4279
   \]

   is the marked lift of the repeated rank-seven parent interval
   (0x4279).  The parent occurrences are exactly

   \[
        [5290,5292],\ [6390,6392],
   \]

   and the two child first-middle occurrences are exactly

   \[
        [11727,11729],\ [12827,12829],
   \]

   with the common start displacement (6437).  Thus carried-shadow
   simplicity is a clean sufficient condition for removing this concrete
   ghost.  It becomes necessary only after one proves that the other
   first-delivery defects already consume the full baseline budget (d).

6. The data through (k=16) do not distinguish (2^{d-1}) from (P(d)).
   A proof of the former *via a free Boolean orbit* would require (d-1)
   independent switches; the latter requires only enough binary states to
   encode (d) seam residues.  No
   retained theorem supplies either free action.  In particular, the
   elementary-event version of (0.1) is false, the first-delivery version is
   not proved, and the exact bracket remains

   \[
                         12873\leq\nu(16)\leq12874.
   \tag{0.5}
   \]

7. A non-Johnson seam can algebraically trade one q1 repeat for one invalid
   q1 adjacency: exactly (H=p+D+R).  Within a one-seam, one-collar move,
   the minimal useful trade is not an arbitrary defect but a
   symmetric-difference-four, octahedral
   (J(4,2)) turn.  Its rank-((r-2)) core and rank-((r+2)) hull survive one
   three-state collar exactly when the collar state lies between them.
   After marking, it becomes a first-middle jump only if its two wing
   coordinates are introduced together.  An exposed common-(Q) port then
   co-locates that jump with the singleton witness.  This is the proved
   witness-level half of a conditional (d+1)-resource Pascal braid; the
   distributed topology that makes the port an already counted cell remains
   an explicit hypothesis.

   The proposed frozen rows 31--60 do not instantiate this atom.  Their
   direct seams have symmetric difference six and intersection rank five
   (the rank-six object is a q2 boundary hole).  The complete 60-row
   qualifying atlas has no symmetric-difference-four candidate.  Moreover
   every one of the thirty rows has a solver-free adjacent double-omission
   obstruction in its maximal compiler envelope.  Thus the repeat-to-defect
   identity is real, but this finite atlas is rigorously closed.

The proved advance is therefore an exact theorem for the strict overlap
lane, a complete realization criterion for a *fixed declared witness atlas*,
and a concrete parent-rainbow obstruction.  It is not a new global lower
bound.

## 1. Exact first-middle-delivery waste

Let (A=(A_0,\ldots,A_{L-1})) be any nonzero word.  For each left endpoint
(p), put

\[
 q(p)=\min\left\{q\geq p:
       \left|\bigcup_{i=p}^qA_i\right|\geq r\right\},
\tag{1.1}
\]

when this set is nonempty.

Classify (p) as follows.

* It is a **stall** if (q(p)) does not exist.
* It is a **jump** if (q(p)) exists but the union at (q(p)) has rank
  strictly greater than (r).
* Otherwise it **delivers** the middle target
  
  \[
            T(p)=\bigcup_{i=p}^{q(p)}A_i\in\binom{[k]}r.
  \]

For each delivered target (T), group its occurrences by their right
endpoint (q).  If the group sizes are (m_{T,q}>0), define

\[
 \begin{aligned}
 f&=\sum_{T,q}(m_{T,q}-1),\\
 g&=\sum_T\left(\#\{q:m_{T,q}>0\}-1\right).
 \end{aligned}
\tag{1.2}
\]

The first quantity is the number of **flat duplicate extras**: several left
chains terminate at the same right endpoint and deliver the same target.
The second is the number of **ghost duplicate extras**: the same target is
delivered at distinct right endpoints.

### Theorem 1.1 (exact waste identity)

Let (s,j) be the numbers of stalls and jumps, and let (h) be the number
of middle targets not delivered.  Then

\[
                \boxed{L=(W-h)+s+j+f+g.}
\tag{1.3}
\]

In particular, every universal word obeys

\[
                \boxed{L-W=s+j+f+g.}
\tag{1.4}
\]

#### Proof

Every left endpoint has exactly one of the three statuses stall, jump, or
delivery.  For a fixed delivered target (T), its total occurrence count is

\[
  1+\sum_q(m_{T,q}-1)+\left(\#\{q:m_{T,q}>0\}-1\right).
\]

Summing this over the (W-h) delivered targets and then adding stalls and
jumps counts the (L) left endpoints exactly once.

If a rank-(r) target occurs as the union of an interval beginning at (p),
then the first prefix of rank at least (r) has rank exactly (r) and,
being an equal-rank subset of the target, equals it.  Thus a universal word
has (h=0).  This proves both identities.  (square)

### Lemma 1.2 (monotone right endpoints)

Whenever both sides exist,

\[
                         q(p+1)\geq q(p).
\tag{1.5}
\]

If equality holds and both chains deliver middle targets, those targets are
equal.

#### Proof

Before (q(p)), every prefix from (p) has rank below (r).  Deleting its
leftmost letter cannot increase rank, so the chain from (p+1) cannot cross
earlier.  If both chains terminate at one (q), their unions are nested
rank-(r) sets and hence equal.  (square)

Thus (1.2) is canonical: flats are the same-height collisions, while ghosts
are the genuinely nonlocal repeated deliveries.

## 2. Retained-certificate census

The lightweight auditor reads the retained words, performs the scan (1.1),
checks (1.3), and separately checks the aligned deadline row.  Its exact
output is:

| (k) | (W) | (d) | (L-W) | first-delivery middle holes | stalls | jumps | flats | ghosts |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 6 | 20 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 8 | 70 | 2 | 2 | 0 | 2 | 0 | 0 | 0 |
| 10 | 252 | 2 | 2 | 0 | 1 | 0 | 1 | 0 |
| 11 | 462 | 3 | 3 | 0 | 3 | 0 | 0 | 0 |
| 12 | 924 | 2 | 2 | 0 | 1 | 0 | 1 | 0 |
| 13 | 1716 | 3 | 3 | 0 | 1 | 0 | 2 | 0 |
| 14 | 3432 | 2 | 2 | 0 | 1 | 0 | 1 | 0 |
| 15 | 6435 | 3 | 3 | 0 | 1 | 0 | 2 | 0 |
| 16 | 12870 | 3 | 4 | 0 | 0 | 0 | 3 | 1 |

The four (k=16) events are, with zero-based endpoints,

| type | target | right-endpoint groups |
|:---|:---|:---|
| flat | `0x4e71` | (6436:\{6433,6434\}) |
| flat | `0xcc63` | (12872:\{12870,12871\}) |
| flat | `0xce61` | (12873:\{12872,12873\}) |
| ghost | `0xc279` | (11729:\{11727\},\ 12829:\{12827\}) |

This is exact evidence that the verified (k=16) word spends four units.
It is not evidence that every (k=16) word must do so.

### 2.1 Four statistics called “waste” must be separated

For the same (k=16) word, four distinct ledgers are now authenticated.

1. **Compiler short-cell waste** is

   \[
      5844\ \text{duplicate-lower cells}
      +6443\ \text{nonlower short cells}=12287.
   \]

2. **Repeated middle-target excess** is five.  The repeated targets are
   
   ```text
   0x6879, 0x4e71, 0xcc63, 0xce61, 0xc279.
   ```

3. **Elementary equal-OR boundary events** are the four immediate
   containment equalities on

   ```text
   0x6879, 0x4e71, 0xcc63, 0xce61.
   ```

   The disjoint repeat `0xc279` is not elementary.  Moreover, the exact
   (k=14) word has only one such event although (d=2).  Therefore

   \[
      \#\{\text{elementary boundary events}\}\geq2^{d-1}
   \]

   is false.

4. **First-delivery unit waste**, the statistic of Theorem 1.1, consists
   of

   ```text
   0x4e71, 0xcc63, 0xce61, 0xc279.
   ```

   The target `0x6879` has an additional longer witness, but its shorter
   witness is already the first delivery from that left endpoint and hence
   the longer occurrence consumes no new left owner.  Conversely `0xc279`
   consumes a second left owner at a distinct height and is a genuine
   ghost.  This explains why both elementary-event count and first-delivery
   waste equal four at (k=16) while naming different fourth objects.

Thus handoff item 1997c decisively closes the naive elementary-signature
version.  It does not close a theorem formulated with the exact charged
set (s+j+f+g=L-W); that stronger theorem remains open.

There is also a normalization warning.  The aligned depth-(d) row is an
exact middle permutation for the retained (k=6,8,10,11,12,13,14,15)
words, but not for (k=4) or the (k=16) upper word.  At (k=8), the
aligned middle deck is complete but its chronology has two non-Johnson
transitions.  Hence neither central flatness nor a Johnson path can be
assumed in a global lower-bound proof.

## 3. The endpoint-event charge correction

There is a second four-state calculus, and it must not be conflated with
Section 1.

Choose one witness interval (I_T=[a_T,b_T]) for each middle target (T).
Equal-rank antichainness makes all (a_T) distinct and all (b_T) distinct:
two intervals sharing one endpoint would be nested, so their rank-(r)
labels would be equal.

At each physical position record whether it is a selected left and/or right
endpoint:

\[
 F=(1,1),\qquad J=(1,0),\qquad S=(0,1),\qquad G=(0,0).
\tag{3.1}
\]

### Theorem 3.1 (weighted endpoint ledger)

If (L=W+c), then

\[
 \boxed{|J|=|S|,\qquad
 c=|J|+|G|=|S|+|G|=\frac{|J|+|S|}{2}+|G|.}
\tag{3.2}
\]

#### Proof

Counting selected left and right endpoints gives

\[
 |F|+|J|=W=|F|+|S|.
\]

Also (L=|F|+|J|+|S|+|G|).  Subtracting (W) gives (3.2).
(square)

Consequently an injection of (q) signatures into arbitrary distinct
(F,J,S,G) positions does not prove (c\geq q).  An (F)-position has
charge zero; (J) and (S) are the two views of one deficit.  A correct
injection must land in one fixed shore

\[
              J\cup G\quad\text{or}\quad S\cup G,
\tag{3.3}
\]

or carry weights (0,\frac12,\frac12,1) and have total weight (q).
Any claimed seam-loss tokens must also be proved disjoint from this ledger.

For flat selected intervals (I_i=[i,i+d]),

\[
             |F|=W-d,\qquad |J|=|S|=d,\qquad |G|=0,
\tag{3.4}
\]

so the overhead is exactly (d), although there are (2d) distinct
nonflat endpoint positions.  The exact odd (d=3) certificates therefore
refute every parity-blind unweighted four-signature argument: (k=11) is
the smallest such authenticated example.

## 4. What complement symmetry does and does not force

For even (k=2m), complement acts within the middle layer.  If selected
witness intervals for (T) and (overline T) met at a physical position,
the nonzero letter there would be contained in

\[
                       T\cap\overline T=\varnothing,
\]

which is impossible.  Complementary selected witnesses are therefore
disjoint.

This does not orient endpoint deficits to one shore and does not create four
charged events at (d=3).  Two countermodels isolate the gap.

1. **Literal middle-only countermodel.**  List all middle sets as individual
   letters and append (d) copies of one singleton.  Every middle target is
   delivered once, the complement pairing is literal, and the only waste is
   (d) terminal stalls.  The word is not universal: it deliberately omits
   almost all lower and upper targets.

2. **Ordered-band countermodel.**  Pair middle labels (i\leftrightarrow
   i+W/2) by complement and take abstract selected intervals
   (I_i=[i,i+d]), with (W/2>d).  The endpoint monotonicity and width-band
   inequalities hold, complementary intervals are disjoint, and overlapping
   intervals never carry disjoint labels.  This checks pairwise
   complement/overlap compatibility; it does not
   assert coordinatewise source realization or the full run/pin system.  The
   endpoint overhead is still only (d).

Thus a valid even-only injection must use the full coordinatewise witness
realization, or simultaneous lower/upper compiler coupling.  Middle order,
band width, pairwise OR compatibility, and complement disjointness are
insufficient.

The odd escape is exact.  For (k=2m+1),

\[
 \overline{\binom{[k]}{m+1}}=\binom{[k]}m,
 \qquad
 \left|\binom{[k]}{m+1}\right|
 =\left|\binom{[k]}m\right|=W.
\tag{4.1}
\]

Complement moves a middle label to the immediate-lower derivative shore.
The authenticated odd q1-rainbow carriers and their boundary compilers do
discharge that resource; cardinality alone does not prove this for an
arbitrary odd word.  For even
(k=2m), by contrast,

\[
 \overline{\binom{[k]}m}=\binom{[k]}m,
 \qquad
 \left|\binom{[k]}{m-1}\right|=\frac m{m+1}W,
\tag{4.2}
\]

so the immediate-lower shore has Catalan deficit (W/(m+1)) and cannot be
an injective copy of the complement deck.  This is a real parity distinction,
but it does not prove an additive correction.

## 5. Exact fixed-witness marked-braid theorem

The full occurrence-level condition has a short exact form.

Let (X) be the old coordinate set and (z\notin X).  Fix one physical
witness

\[
                       w=(I_w,S_w,\eta_w)
\]

for every desired target, where (S_w\subseteq X) and
(eta_w\in\{0,1\}) says whether the target is (S_w) or
(S_w\cup\{z}).  For every position (p), define

\[
 Q_p=\bigcap_{w:p\in I_w}S_w,
 \qquad
 F=\bigcup_{\eta_w=0}I_w,
\tag{5.1}
\]

using (Q_p=X) when no chosen witness contains (p).

### Theorem 5.1 (common-(Q) marked realization)

There exists a nonzero word realizing all the chosen witnesses if and only
if the following three conditions hold.

1. For every (w) and every (x\in S_w), some (p\in I_w) has
   (x\in Q_p).
2. Every marked interval (I_w), (eta_w=1), meets the complement of
   (F).
3. If (Q_p=\varnothing), then (p\notin F).

When they hold, a maximal realization is

\[
 C_p=Q_p\cup
 \begin{cases}
 \{z\},&p\notin F,\\
 \varnothing,&p\in F.
 \end{cases}
\tag{5.2}
\]

#### Proof

Any old-coordinate letter at (p) must lie in every target whose witness
uses (p), hence in (Q_p).  Every coordinate required by a target must be
hit somewhere in its witness, proving condition 1.  An unmarked witness
forbids (z) at all its positions, so every marked witness needs a position
outside their union (F), proving condition 2.  If (Q_p=\varnothing) and
(p\in F), then both the old part and (z) are forbidden at (p), contrary
to nonzeroness.  This proves necessity.

For sufficiency use (5.2).  On (I_w), every (Q_p\subseteq S_w), while
condition 1 supplies every member of (S_w).  Thus the old-coordinate union
is exactly (S_w).  If (eta_w=0), its interval lies in (F), so it sees
no (z); if (eta_w=1), condition 2 supplies (z).  Condition 3 makes
every physical letter nonzero.  (square)

For the singleton ({z}), its old projection is empty.  Its witness
therefore contains an **exposed ghost port**

\[
                     Q_p=\varnothing,\qquad p\notin F.
\tag{5.3}
\]

This is the exact finite test for realizing the *declared* lower, upper,
middle, and singleton witnesses in one fixed atlas.  It does not forbid
unintended extra middle occurrences, enforce exact owner degrees, residence,
or prove that the chosen intervals form a legal braid topology.  Universality
still requires choosing one suitable witness for every target.

## 6. The strict (d)-overlap bridge obstruction

Let an odd parent have middle width (W), deadline (d), and word length
(N=W+d).  Literal doubling has the form

\[
                         A,\{z\},z+B
\tag{6.1}
\]

and length (2N+1=2W+2d+1).  If (t) parent cells are identified and the
separate bridge is absorbed with indicator (delta\in\{0,1\}), the length
is

\[
                    2W+2d+1-t-\delta.
\tag{6.2}
\]

Reaching the deadline target (2W+d) requires

\[
                           t+\delta=d+1.
\tag{6.3}
\]

In the strict shared-tail construction, central incidence forces exactly
(t=d): the first (d) projected cells of a dual source (B) are identified
with the last (d) cells of (A).  Thus exact length also requires
(delta=1), absorption of the singleton bridge.

Write

\[
 R_i=\bigcup_{j=0}^d B_{i+j},\qquad 0\leq i<W,
\tag{6.4}
\]

and suppose the (R_i) are consecutive distinct sets of one cardinality,
as required for the second half of the even middle deck.

### Lemma 6.1 (uniform dilation has no projected ghost)

If (W\geq d+2), every (B_p) is nonempty.

#### Proof

For (0\leq p<W-1), choose (x\in R_p\setminus R_{p+1}).  Every source
cell shared by the two windows is forbidden to contain (x) by the second
window, so (x) can occur only in (B_p).

For (W-1\leq p<W+d), put (i=p-d\).  Then (1\leq i<W).  Choose
(y\in R_i\setminus R_{i-1}).  Every earlier cell of the window for (R_i)
also occurs in the window for (R_{i-1}), so (y) can occur only in
(B_{i+d}=B_p).  (square)

### Theorem 6.2 (strict overlap needs the bridge)

Under the strict two-block hypotheses, deleting the singleton bridge makes
the word nonuniversal.  Hence every such universal lift has length at least

\[
                         \boxed{2W+d+1.}
\tag{6.5}
\]

#### Proof

Every cell in the marked sector has the form ({z}\cup B_p).  By Lemma
6.1 its old-coordinate projection is nonempty.  Every interval containing
(z) therefore contains an old coordinate, so no interval has union
({z}).  Thus (delta=1) in (6.3) is impossible in this architecture;
at most the (d) parent cells can be saved.  (square)

If the singleton bridge is retained, the word has length (2W+d+1).
Its marked targets are all realized exactly when the projected interval
family

\[
\begin{aligned}
 \mathcal M^+(A,B)=
 &\{\varnothing\}\\
 &\cup\left\{\bigcup_{j=s}^tB_j:d\leq s\leq t<N\right\}\\
 &\cup\left\{\bigcup_{i=s}^{N-1}A_i:0\leq s<N\right\}\\
 &\cup\left\{
   \left(\bigcup_{i=s}^{N-1}A_i\right)
   \cup\left(\bigcup_{j=d}^tB_j\right):
   0\leq s<N,\ d\leq t<N
   \right\}
\end{aligned}
\tag{6.6}
\]

equals (2^X).  The first family is the singleton bridge, the second comes
from intervals wholly in the marked (B)-sector (including those beginning
at the bridge), the third from (A)-suffixes ending at the bridge, and the
fourth from intervals crossing through the bridge into (B).  Thus (6.6)
is the exact simultaneous lower/upper marked-cover condition requested by
the overlap proposal.

The retained length-12,874 word has the same arithmetic as a
bridge-retaining depth-three overlap, but its distributed phase braid is not
claimed to be literally of the two-block form (6.1).  Theorem 6.2 therefore
explains one exact architecture, not that certificate's complete geometry.

The obstruction is strictly architecture-specific.  A six-piece braid can
put a marked ear of length (d+1) between two unmarked pieces.  Its
depth-(d) erosion has one singleton-(z) slot, while two additional cuts
restore the two lost upper colours.  Exact (d=2) even optima already use
this escape.  Thus the bridge is not globally unmergeable.

## 7. The carried-shadow collision lemma and the (0xc279) ghost

The new literal seed identifies what the fourth (k=16) unit is in the
retained braid.

### Lemma 7.1 (a carried parent repeat becomes even waste)

Let two distinct parent intervals (J_1,J_2) have the same old-coordinate
union (L) of rank (r-1).  Suppose a marked lift sends them to two
distinct child first-delivery occurrences (J'_1,J'_2) of
({z}\cup L).

* If the child right endpoints are equal, they contribute a flat duplicate.
* If the child right endpoints are distinct, they contribute a ghost
  duplicate.

More generally, let (C_{\rm carry}) be the carried parent collision excess,
and let (a) collision units be neutralized by suppression, reassignment,
or coalescence to one child occurrence.  If (B_{\rm other}) other
first-delivery waste units are proved disjoint from the surviving carried
collisions, then every target-overhead-(d) lift necessarily obeys

\[
             C_{\rm carry}-a\leq d-B_{\rm other}.
\tag{7.0}
\]

#### Proof

Both child intervals deliver the same middle target.  The two cases are
exactly the two summands in (1.2).  Suppression, reassignment, or coalescence
is precisely what removes a collision unit.  Adding the separately disjoint
bank (B_{\rm other}) and applying (1.4) proves (7.0).  (square)

For the retained words, exact replay gives

\[
 \begin{array}{c|c|c}
 &\text{target}&\text{occurrences}\\ \hline
 k=15&0x4279&[5290,5292],\ [6390,6392]\\
 k=16&0xc279&[11727,11729],\ [12827,12829].
 \end{array}
\tag{7.1}
\]

The two child starts are the corresponding parent starts plus (6437), and

\[
                         0xc279=0x8000\cup0x4279.
\tag{7.2}
\]

This proves that the nonlocal child ghost is inherited from a parent
immediate-lower repeat; it is not a numerical coincidence.

The following is therefore a clean sufficient parent property for avoiding
inherited carried-shadow waste.

> **Carried-shadow simplicity.**  On the parent rank-((r-1)) intervals
> transported into the marked middle shore, the target map is injective
> after deleting the bounded occurrence family explicitly consumed by
> cross-seam supplies.

For a one-cross-seam design this is “rainbow up to the one seam occurrence.”
Parent universality and all-depth coverage alone do not imply it.  Simplicity
is necessary only when a separate theorem gives (B_{\rm other}=d).
In the collision notation of the positive-density compiler, carried parent
rank-((r-1)) collisions map into the child's middle-rank term (R_=) only
when their transported child intervals lie in the short family defining
that term.  Without that length hypothesis they still enter the
first-delivery ledger, but not automatically (R_=).

### 7.2 All-depth lower-intersection path conservation

There is a genuine algebraic alternative to a repeated q1 colour, and its
counting law extends to every depth.  Let the odd parent ground set have size
(2r-1), put (W=\binom{2r-1}{r}), and let

\[
                  T_0,T_1,\ldots,T_{W-1}
\]

be a permutation of its rank-(r) layer.  For (1\leq q\leq r-1), set

\[
             C_i^{(q)}=\bigcap_{j=0}^qT_{i+j},
             \qquad 0\leq i<W-q.
\tag{7.3}
\]

Let (D_q) count the indices for which (|C_i^{(q)}|\ne r-q).  Among the
valid rank-((r-q)) values, let (R_q) be duplicate excess and (H_q) the
number of holes in the complete rank-((r-q)) deck.

#### Theorem 7.2 (all-depth defect conservation)

For every (1\leq q\leq r-1),

\[
 \boxed{
 H_q-R_q=\binom{2r-1}{r-q}-W+q+D_q.}
\tag{7.4}
\]

In particular, at (q=1),

\[
                         \boxed{H_1=1+D_1+R_1.}
\tag{7.5}
\]

More generally, for a path cover with (p) paths, the q1 identity is

\[
                         \boxed{H_1=p+D_1+R_1.}
\tag{7.6}
\]

#### Proof

There are (W-q-D_q) valid windows in (7.3).  They realize

\[
       \binom{2r-1}{r-q}-H_q
\]

distinct colours and have duplicate excess (R_q).  Equating occurrence
counts gives

\[
 W-q-D_q=\binom{2r-1}{r-q}-H_q+R_q,
\]

which is (7.4).  At (q=1), the two adjacent odd layers have the same size,
giving (7.5).  A cover by (p) paths has (W-p) rather than (W-1)
adjacencies, giving (7.6).  (square)

The authenticated winning K15 chronology has

\[
 (p,D_1,R_1,H_1)=(1,0,1,2),
\]

with unique repeat `0x4279`, while every row 31--60 has

\[
 (p,D_1,R_1,H_1)=(1,1,0,2).
\tag{7.7}
\]

Thus one repeated Johnson turn and one defective non-Johnson turn are
literally interchangeable in the q1 count.  Since `0x4279` is the source
of child ghost `0xc279`, this is exactly the proposed ghost-for-defect
conversion at palette level.  The theorem says nothing yet about residence,
upper shadows, or literal compiler feasibility.

### 7.3 The minimal useful defect is an octahedral paired turn

Let (U,V) be rank-(r) states and write

\[
 Q=U\cap V,\qquad R=U\cup V,\qquad |Q|=r-q.
\tag{7.8}
\]

Then (|R|=r+q).  Thus the two-cell seam itself realizes an upper target of
rank (r+q).  In a prescribed (q+1)-state shadow window, it retains the same
lower target (Q) exactly when every other state contains (Q), and it retains
the same upper target (R) exactly when every other state is contained in
(R).

For (q=2), a third rank-(r) state (N) therefore preserves both sides
exactly when

\[
                           Q\subseteq N\subseteq R.
\tag{7.9}
\]

Write (U=Q\cup A) and (V=Q\cup B), where (A,B) are disjoint two-sets.
The six rank-(r) states between (Q) and (R) form the octahedron
(J(4,2)).  Any

\[
                  N=Q\cup\{a,b\},qquad a\in A, b\in B,
\]

satisfies

\[
 U\cap N\cap V=Q,qquad U\cup N\cup V=R,
\tag{7.10}
\]

and both (U-N) and (N-V) are Johnson edges.  Move (N) from between (U,V)
to the adjacent outside collar.  Either three-owner rotation

\[
                  U-N-V\longmapsto N-U-V
                  \quad\hbox{or}\quad
                  U-N-V\longmapsto U-V-N
\]

keeps all three middle owners, creates the one logical seam (U|V), and
retains the same triple intersection (Q) and triple union (R).  This
octahedral rotation is the smallest non-Johnson Pascal-braid atom, within the
class of one direct defective seam and one adjacent collar state, capable of
carrying the missing even-depth unit.  It is not a necessity theorem for an
arbitrary multi-seam braid.

The atom is not by itself a completed factor switch.  It retains all three
middle owners and the paired q2 window, but changes an external block
adjacency and every longer window through the rotation; those resources must
be restored, and the literal common-Q pins must pass.  Conversely, if
(q\geq3), every triple spanning (U|V) has intersection rank at most
(r-3) and union rank at least (r+3).  Such a seam can supply neither member
of a paired q2 turn.  This already excludes the frozen rows 31--60 from the
desired role.

### 7.4 Marked-lift trichotomy and bridge--jump fusion

The palette identity does not determine the child first-delivery type.
After marking a rank-((r-2)) core (Q), the partial child union

\[
                         Q\cup\{z\}
\]

has rank (r-1).  A next cell contributing one new old coordinate gives an
ordinary middle delivery; a cell contributing at least two new old
coordinates gives a jump; and a collar that never supplies a new coordinate
remains short or stalls.  The collar increment, not the rank of (Q), is
decisive.

The common-Q theorem gives an exact sufficient fusion condition.  Retain the
fixed witness atlas of Section 5 and its sets (Q_j,F), and suppose its three
realization conditions hold.  Assume there are (p<t), a set (C) of rank
(r-2), and distinct coordinates (u,v\notin C) such that

\[
 \begin{aligned}
 Q_p&=\varnothing,\qquad p\notin F,\\
 \bigcup_{j=p}^{t-1}Q_j&=C,\\
 \bigcup_{j=p}^{t}Q_j&=C\cup\{u,v\}.
 \end{aligned}
\tag{7.11}
\]

#### Theorem 7.3 (fixed-atlas bridge--jump fusion)

Under (7.11), the maximal realization (5.2) simultaneously:

1. realizes every declared witness;
2. realizes the singleton ({z}) on the one-cell interval ([p,p]); and
3. makes the chain beginning at (p) jump at (t) from rank at most (r-1)
   to rank (r+1), with no intervening middle delivery.

#### Proof

The first assertion is Theorem 5.1.  Since (Q_p=\varnothing) and
(p\notin F), the maximal letter at (p) is exactly ({z}), proving the
second assertion.  Before (t), the old-coordinate union is contained in
(C), so every prefix from (p) has rank at most (1+|C|=r-1).  At (t),
both new coordinates appear and the union becomes
(C\cup\{u,v,z\}), of rank (r+1).  This is the first crossing and hence a
jump.  (square)

This theorem proves co-location of the singleton witness and jump start.  It
does not itself delete or identify a physical cell.  If a separate
topological braid places (p) in an already counted overlap cell, keeps the
octahedral states consecutive as in Section 7.3, and preserves the
cut-kernel witnesses, then (7.11) is the exact witness-level condition needed
for the missing (d+1)-st saving.  This must be a distributed, non-strict
braid: Lemma 6.1 forbids the exposed empty old projection in the strict
shared-tail architecture.

There is an important accounting caveat.  If Lemma 7.1 transports the parent
repeat to a child flat/ghost and Theorem 7.3 transports the parent defect to
a child jump, then the conversion
(R_1=1,D_1=0\to R_1=0,D_1=1) is neutral in (1.4).  The parent values
(R_1,D_1) alone do not determine child charges.  Even under the stated
transport hypotheses, the length saving occurs only when the exposed port
also absorbs the otherwise separate singleton bridge.  An equality lift
must additionally prove that all other first-delivery charges fit within the
remaining (d-1) units.  Neither defect conservation nor the octahedron alone
does that.

### 7.5 Exact closure of the frozen rows 31--60

The exhaustive frozen two-cycle atlas tested (2,300,400) directed pairs.
Exactly (60) passed its residence, all-upper, ordinary-Hall, and boundary
filters: thirty have symmetric difference two and thirty have symmetric
difference six.  There is no symmetric-difference-four candidate, hence no
rank-((r-2)) seam, in this complete qualifying atlas.

The thirty non-Johnson rows are fifteen chronologies and their reversals.
Every direct seam joins rank-eight states at symmetric difference six, so
its intersection has rank five, **not rank six**.  Each chronology has:

* exactly two q1 holes and no q1 duplicate;
* exactly one q2 hole of rank six;
* no lower hole at any deeper depth;
* zero residence violations and zero arbitrary-width upper holes;
* ordinary Hall deficiency zero and a three-target boundary SDR.

The rank-six object is the missing q2 boundary target, not the direct seam
intersection.  For row 31, explicitly,

\[
 \begin{aligned}
 U&=\texttt{0x3ac6},\qquad V=\texttt{0x319e},\\
 U\cap V&=\texttt{0x3086},\qquad |U\cap V|=5,\\
 \text{q1 holes}&=\{\texttt{0x3a86},\texttt{0x318e}\},\\
 \text{q2 hole}&=\texttt{0x3186}.
 \end{aligned}
\tag{7.12}
\]

The compiler failure has a two-cell solver-free certificate.  Its maximal
envelope tail is

\[
 P_{6435}=\texttt{0x1986},\quad
 P_{6436}=\texttt{0x3986},\quad
 P_{6437}=\texttt{0x398e}.
\tag{7.13}
\]

The containment candidate sets for the right q1 hole (L) and q2 hole (K)
are

\[
 \operatorname{Cand}(L)=\operatorname{Cand}(\texttt{0x318e})=\{6437\},
 \qquad
 \operatorname{Cand}(K)=\operatorname{Cand}(\texttt{0x3186})
   =\{6436,6437\}.
\tag{7.14}
\]

One target per cell therefore forces

\[
 A_{6437}=\texttt{0x318e},qquad
 A_{6436}=\texttt{0x3186}.
\]

But then

\[
 A_{6436}\cup A_{6437}=\texttt{0x318e}
 \ne
 \texttt{0x398e}=P_{6436}\cup P_{6437}.
\tag{7.15}
\]

The missing bit `0x0800` is present in **both** adjacent envelope cells and
omitted by both forced literals.  Thus (\mathscr DA=\mathscr DP) fails:
this is an adjacent double-omission/common-pin obstruction, not merely a
Hall deficit.

Rows 31--45 have the same two-position forced pattern at the right boundary;
rows 46--60 have its reversal at the left boundary.  The masks rotate, and
the common pin runs through every one of the fifteen coordinates exactly
twice.  Hence all thirty exact
statuses

```text
FIXED_OPENING_ADAPTIVE_CORE_INFEASIBLE
```

follow from the same local certificate.  Ordinary Hall is (4946/4946) in
every row, so marginal palette supply cannot see the obstruction.

Therefore the frozen atlas proves both a scoped absence theorem and the
shape of the next move.  A live construction must alter the parent factor or
use a multi-seam braid that creates a symmetric-difference-four octahedral
turn, routes its displaced middle owner, exposes (7.11), and passes full
`COMP_3`.  The no-go does not apply to such a different carrier or atlas.

## 8. Exponential signatures versus binary padding

The elementary-boundary-event interpretation of both laws is already
refuted by the (k=14) census in Section 2.1.  This section concerns only a
hypothetical injection into the unit-charge first-delivery ledger, or a
construction whose seam-state count is charged injectively to that ledger.

The two proposed functions agree only at the presently tested deadlines:

| (d) | (2^{d-1}) | (P(d)=2^{\lceil\log_2d\rceil}) | (d+1) overlap resources |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 3 |
| 3 | 4 | 4 | 4 |
| 4 | 8 | 4 | 5 |
| 5 | 16 | 8 | 6 |
| 6 | 32 | 8 | 7 |

For even dimensions, the first occurrences of successive deadlines are

\[
 \begin{array}{c|rrrrrr}
 d&1&2&3&4&5&6\\ \hline
 \text{first even }k&4&8&16&32&52&78.
 \end{array}
\tag{8.1}
\]

Hence (k=16) cannot distinguish exponential signatures, binary padding,
or the architecture-specific (d+1) resource count.  At (k=32) they
predict respectively (8,4,5).

There is one rigorous binary-padding statement.

### Lemma 8.1 (free Boolean seam orbit)

Suppose a legal seam-state component carries a free action of
((\mathbb Z/2\mathbb Z)^t), and one orbit must contain (d) distinct
logical seam residues.  Then that orbit has at least

\[
                         P(d)=2^{\lceil\log_2d\rceil}
\tag{8.2}
\]

states.

#### Proof

A free orbit has size (2^t).  Since it contains (d) distinct residues,
(2^t\geq d), and the least possible power of two is (8.2).  (square)

To turn this into a length lower bound, the orbit states must inject into
distinct unit-charge events from Theorem 1.1, or into one fixed endpoint
deficit shore from (3.3).  Neither property is known.  Merely having (d)
states does not force closure to a Boolean orbit.

A derivation of the exponential law (2^{d-1}) from the free-orbit
mechanism would require (d-1) independent free switches, not merely enough
bits to encode (d) residues.  The numerical law might conceivably have a
different proof.  No Pascal, PBBS, complement, or retained seam theorem
currently supplies the free switches.  Since

\[
 P(d)<2d=O(\sqrt k),
 \qquad
 2^{d-1}=\exp(\Theta(\sqrt k)),
\]

the distinction is also asymptotically substantive.

## 9. Exact remaining gates

### For the global (k=16) lower bound

It would suffice to prove the following (d=3) distributed-ear alternative.

> Every length-(W+3) even universal word either lies in the strict
> two-block overlap lane, which Theorem 6.2 excludes, or its full witness
> system has a fourth unit-charge first-middle event forced by failure of
> carried-shadow simplicity or by the absence of an exposed common-(Q)
> ghost port.

No theorem presently proves this normalization or alternative.  The exact
six-piece braid shows why it must include deep-shadow and compiler
compatibility, not just local (z)-run geometry.

Theorems 7.2 and 7.3 give a second possible equality architecture: replace a
carried q1 repeat by one octahedral rank-((r-2)) seam, route the displaced
middle owner, and fuse its atomic-wing jump with the exposed singleton port.
The rows 31--60 no-go shows that the required hypothesis must include the
literal common-pin equations of full `COMP_d`; residence, all upper shadows,
ordinary Hall, and a boundary SDR are not enough.  In fact that frozen atlas
contains no rank-((r-2)) seam at all.

### For an all-even binary-padding theorem

One must prove three separate statements:

1. at least (d) logically distinct seam residues survive physical
   lower/upper witness realization;
2. legal Pascal exchanges close those residues into one free Boolean orbit;
3. its orbit states consume distinct charged middle-chain owners.

The common-(Q) theorem exactly verifies the fixed-witness realization part
of statement 1 and the nonzero-word part of statement 3.  Choosing a legal
braid atlas, Boolean closure, and owner-disjointness remain open.

### For a reusable odd-to-even braid

The parent must supply simultaneously:

* universality and the protected all-depth tower;
* residence in both carried shores;
* either carried rank-((r-1)) simplicity modulo explicit cross-seam supply,
  a proved collision budget of the form (7.0), or a compiler-feasible
  octahedral (R\to D) turn satisfying Sections 7.3--7.4;
* an exposed singleton-(z) ghost port satisfying Theorem 5.1;
* restoration of every upper colour cut by the distributed ear.

This is the concrete Pascal/braid gate exposed by the (0x4279\mapsto0xc279)
certificate.  In its weakest exact form, the one missing lemma is:

> **Octahedral exposed-port lemma.**  Some protected K15 parent factor and
> fixed witness atlas contain a symmetric-difference-four seam (U|V), a
> sandwich state (Q\subseteq N\subseteq R) routing its paired q2 turn, and
> an exposed atomic-wing port satisfying (7.11); a distributed braid keeps
> the three states consecutive, places that port in an already counted
> overlap cell, and preserves every cut-kernel witness and the remaining two
> baseline charges.

That lemma would supply the missing fourth saving in this Pascal architecture.
The current frozen factor refutes it only for its complete one-seam atlas.
The all-r induction asks for the same statement in every odd parent
(2r-1), with `COMP_d` and the corresponding protected all-depth tower in
place of the K15 objects.

## 10. Audit artifacts and scope

The new lightweight artifacts are:

* `scratch/audit_middle_chain_waste_inventory_20260730.py`, SHA-256
  `5ef523356eee1aabd622662b2d4e1bd0c4172e070a83bc439e47ec4da6d18c33`;
* `scratch/middle_chain_waste_inventory_k04_k16_20260730.audit.json`,
  SHA-256
  `f555439ae1f32f0e9d44a6877fd1af1dcff0c062cb3f030baa78affd6ce8c551`;
* `scratch/audit_k15_k16_ghost_lift_20260730.py`, SHA-256
  `b98e6bc8f0ecf5b8cdd480018bbcd02dce2083620f3a058df5eea7e7f8a81b6f`;
* `scratch/k15_k16_ghost_lift_20260730.audit.json`, SHA-256
  `6d6ad7ac2ce429cc05c9f922ea6cf42d252d01b90c078c361995afab48733d1e`.
* `scratch/audit_k15_nonjohnson_seam_defect_trade_20260730.py`, SHA-256
  `8ceab014b90cc3538c4813df9c72ee0885abee0136b80c5f34b5a27142dc51d9`;
* `scratch/k15_nonjohnson_seam_defect_trade_20260730.audit.json`, SHA-256
  `ec744b1a99f55dae06d42aaf7f0628c50652edffac2d5b4e5e63cd938befc0ae`,
  payload
  `9f08debc2d0b4d9f1c30514a97c47b2f7dea76f45456ee10738e7af9c8f57095`.

The authenticated frozen-atlas inputs to the last audit are:

* `scratch/k15_fixed_matching_pbbs_resident_20260729/arbitrary_seams.audit.json`,
  SHA-256
  `99da4b8528f9845ee159618790d13f009bdb062af7ccace64c65e3e843b2c5fc`;
* `scratch/search_k15_two_cycle_arbitrary_seam_20260729.py`, SHA-256
  `2ea16f34e61feb508d0ec496de61a8168c76e56c9f7d79703032ab180ac04f08`;
* `scratch/k15_rank6_arbitrary_seam_rows_20260730/rank6_rows30.audit.json`,
  SHA-256
  `56c1c403eaa58448b5770a0c30272e90a60c19ed79e8c40a01a23bdf0c4b843f`,
  payload
  `2fedfc332b17e8784708a0df9147474b1db98fdd30e9a16addda0b387bae2ccd`.

The independent retained-normal-form cross-checks are
`scratch/raw_optimal_k01_k14_compiler_normal_form_audit.json`, SHA-256
`33457ecdd9c96bc78eac7f2e2f35dc408315d986ea90ed3bd94d3d8b7527c913`,
and `scratch/raw_answer_symmetry_k01_k14.json`, SHA-256
`7a9ab729e2b1336b712d05c2dd2cf461ef38ff70cae60728b1edf0df626651ba`.

The independent elementary-event counteraudit is
`THREAD_D_EVEN_DEPTH_BOUNDARY_SIGNATURE_COUNTEREXAMPLE_20260730.md`, SHA-256
`dc8ed68ccaa2b5f01e4fc5df6fba5cfb894088f55de654ebe7bde9b0c64e3b70`;
its exact JSON has SHA-256
`85a34db167bf4945f335c7d267321d281e5c75b28722fd740530976d1f4f9b1d`
and payload
`606d6d1610960b32cefcdb3e7f7fe46ecedcbf0db86ffc756c31dff4e3b2f32e`.

The retained word hashes used by the audit are recorded inside the JSON.
In particular,

\[
 \begin{aligned}
 \operatorname{SHA}(k15)&=
 \texttt{f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b},\\
 \operatorname{SHA}(k16\text{ upper})&=
 \texttt{631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e}.
 \end{aligned}
\]

The strict-overlap theorem reuses the independently audited source theorem
`MATH_ODD_EVEN_SHARED_TAIL_LIFT_20260727.md`; the distributed escape is the
finite theorem in `MATH_ODD_EVEN_SIX_PIECE_LIFT_20260728.md`.  The endpoint
band inequalities are those of
`MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`.

No new SAT, exhaustive search, web access, or remote computation was run for
this note.  Section 7.5 explicitly reuses the authenticated prior exhaustive
atlas and its thirty exact compiler decisions.  The new local audit is
solver-free: it rebuilds the factor chronology and maximal envelope, checks
the exhaustive-census metadata, and verifies all thirty adjacent common-pin
certificates in under one second.  The other local scripts perform only
linear occurrence replay.  The only unconditional numerical conclusion
remains (0.5).
