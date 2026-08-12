# Independent audit of the single-switch / portal proposal

## Verdict

The proposal contains a useful and arithmetically correct way of spending the
rank-count defect, but its advertised `k=11` realization is impossible under
its own row-saturation requirements.

More precisely:

* the canonical single-switch interval schedule is a valid instance of the
  unrestricted monotone-band normal form;
* all displayed `k=11` row counts, the `369+93` split, the `39`-component
  forest count, and the Catalan length identities are arithmetically correct;
* the broad **Single-Switch Saturated Braid Conjecture** remains a conjecture;
* the more specific `k=11` plan with `330` rank-seven Johnson edges and `38`
  rank-eight distance-two edges is **false**: the saturated lower rows permit
  at most one such rank-eight internal portal;
* the Portal Absorption and Pascal Fusion statements are not consequences of
  the counts.  They omit the main compatibility conditions: overlap ranks,
  derivative factorability, endpoint stitching, lower-row distinctness, and
  coordinate pin survival.

The no-go result below does **not** refute every possible single-switch word.
It refutes the proposed clean row grading and its `330+38+1` upper-portal
architecture.

## 1. Arithmetic defect and the canonical schedule

Let

\[
 M=\binom kr,\qquad
 L=\sum_{s=1}^{r-1}\binom ks,\qquad
 n=M+d,
\]

where `d` is the least integer for which

\[
 L\le dM+\binom{d+1}{2}.
\]

Put

\[
 \sigma=dM+\binom{d+1}{2}-L.
\]

The number of physical intervals of lengths at most `d` is indeed

\[
 \sum_{q=1}^d(n-q+1)
 =dn-\binom d2
 =dM+\binom{d+1}{2}
 =L+\sigma.                                      \tag{1.1}
\]

Assume `0<=sigma<=M`.  The proposed rank-`r` witnesses

\[
 I_i=\begin{cases}
 [i,i+d-1],&1\le i\le\sigma,\\
 [i,i+d],&\sigma<i\le M
 \end{cases}                                      \tag{1.2}
\]

are non-nested.  Their left endpoints are `1,...,M`; their right endpoints
are

\[
 d,d+1,\ldots,\sigma+d-1,
 \sigma+d+1,\ldots,M+d.
\]

They omit exactly the `d` right endpoints

\[
 1,2,\ldots,d-1,\quad \sigma+d.
\]

In monotone-band notation

\[
 I_i=[i+\alpha_i,i+\beta_i],
\]

this is simply

\[
 \alpha_i=0,\qquad
 \beta_i=\begin{cases}d-1&i\le\sigma,\\d&i>\sigma.
 \end{cases}
\]

Thus (1.2) is fully compatible with the normal form.  It is a particularly
special normal form: all left offsets are zero and there is only one right
offset switch.

There are two qualifications.

1. Minimality of `d` gives only `sigma<M+d`; it does not by itself give
   `sigma<=M`.  For the favored maximizing ranks in all cases under discussion
   this inequality holds.  It is not proved in the proposal as an all-`k`
   theorem.  There is already a harmless small tie at `k=3`: the maximizing
   choice `r=3` has `(M,d,sigma)=(1,3,3)`, whereas the favorable maximizing
   choice `r=2` has `(3,1,1)`.
2. A shortened central witness makes its containing length-`d+1` interval
   available for other work, but does not make its OR a strict superset
   automatically.  At `k=3`, the canonical word
   `[5,1,2,4]` has the shortened rank-two witness `[1,1]`, while its alleged
   portal `[1,2]` also has OR `5`.  In the `k=4` sanity word
   `[5,9,10,1,2,4,8]`, two portal cells have the same OR
   (`R_2(2)=R_2(3)=11`).  Hence “portal” must mean a free physical cell, not a
   guaranteed new upper-mask value.

The rank-count theorem proves only that the short band has `sigma` cells left
after choosing witnesses for the `L` lower masks.  It does **not** prove that
those cells can be made distinct rank-`r` values.  That is exactly the new
conjectural content.

## 2. The `k=11` bookkeeping is exact

For `k=11`, `r=6`, one has

\[
 M=462,\qquad d=3,\qquad L=1023,\qquad \sigma=369.
\]

The proposed central schedule is therefore

\[
 [i,i+2]\quad(1\le i\le369),
 \qquad
 [i,i+3]\quad(370\le i\le462).                    \tag{2.1}
\]

The displayed row counts are all correct:

\[
\begin{array}{c|c|c}
\text{rows}&\text{number of cells}&\text{proposed labels}\\ \hline
1,2&465+464=929&561\text{ masks of ranks }1\ldots4
                      +368\text{ rank-five masks}\\
3&463&94\text{ rank-five masks}+369\text{ rank-six masks}\\
4&462&93\text{ rank-six}+330\text{ rank-seven}
                      +39\text{ rank-eight}.
\end{array}
\]

Write `R_q(i)` for the length-`q` OR-window and put

\[
 P_i=R_3(i)\quad(1\le i\le369).
\]

Then, without any assumption,

\[
 R_4(i)=P_i\cup P_{i+1}\qquad(1\le i\le368).       \tag{2.2}
\]

The seam cell is

\[
 R_4(369)=R_3(369)\cup R_3(370).                   \tag{2.3}
\]

Thus the claimed `38` internal rank-eight portals plus one seam portal really
would total `39`; there is no off-by-one error there.

Likewise, if

\[
 H_j=R_3(369+j)\quad(1\le j\le94),\qquad
 Q_j=R_4(369+j)\quad(1\le j\le93),
\]

then

\[
 Q_j=H_j\cup H_{j+1}.
\]

If all `H_j` are distinct rank-five masks and all `Q_j` are distinct rank-six
masks, the `Q_j` automatically form a Johnson path and

\[
 Q_j\cap Q_{j+1}=H_{j+1}\qquad(1\le j\le92).
\]

Consequently the `92` internal intersections plus endpoint facets `H_1,H_94`
do give `94` rank-five values.  This part of the proposed lower-facing block
is set-theoretically consistent.

## 3. No-go theorem for the proposed `330+38` upper block

The following contradiction uses only the stated grading of rows one through
three.  It does not invoke pinning or any SAT ansatz.

### Theorem 3.1

There is no array of length `465` satisfying all of the following:

1. all OR-values of windows of lengths one, two, and three are mutually
   distinct;
2. the singleton and adjacent-pair values consist of every mask of ranks one
   through four together with `368` rank-five masks;
3. `R_3(1),...,R_3(369)` are distinct rank-six masks;
4. `R_3(370),...,R_3(463)` are distinct rank-five masks;
5. among `R_4(1),...,R_4(368)`, at least two values have rank eight.

In particular, the proposed block with `38` internal rank-eight portals does
not exist.

### Proof

First, no singleton entry can have rank five.  If `A_j` had rank five, choose
an adjacent pair containing it.  Its OR contains `A_j`, has rank at most five
by hypothesis 2, and therefore equals `A_j`.  This duplicates a short-window
value, contradicting hypothesis 1.

Hence all `368` rank-five values in rows one and two must be adjacent-pair
ORs.

For every pair position `t=370,...,464`, the pair `R_2(t)` lies in a rank-five
triple:

* if `370<=t<=463`, then `R_2(t) subset R_3(t)`;
* if `t=464`, then `R_2(464) subset R_3(463)`.

Since all short-window values are distinct, `R_2(t)` cannot equal that
rank-five triple.  It follows that

\[
 |R_2(t)|\le4\qquad(370\le t\le464).                \tag{3.1}
\]

All `368` rank-five pair values must therefore occur among the `369` slots

\[
 R_2(1),R_2(2),\ldots,R_2(369).                    \tag{3.2}
\]

At most one slot in (3.2) has rank at most four.

For `1<=i<=368`, the shared pair lies in both consecutive `P` vertices:

\[
 R_2(i+1)\subseteq P_i\cap P_{i+1}.                \tag{3.3}
\]

If `R_4(i)=P_i union P_{i+1}` has rank eight, then two rank-six sets satisfy

\[
 |P_i\cap P_{i+1}|=6+6-8=4.
\]

Equation (3.3) then forces `|R_2(i+1)|<=4`.  Distinct rank-eight internal
portals require distinct shared-pair positions, while (3.2) contains at most
one lower-rank position.  Hence at most one of

\[
 R_4(1),\ldots,R_4(368)
\]

can have rank eight.  This contradicts hypothesis 5.  ∎

### Consequences

The proposal requires exactly `38` of these `368` internal cells to be
rank-eight bridge colors, so it violates Theorem 3.1 by a factor of `38`.
The sentence saying that the remaining `38` rank-five pair values can be put
in the “fringe and Q-region” is also false under the stated grading: no
Q-region pair `R_2(370),...,R_2(464)` can have rank five.  At most the single
left fringe pair `R_2(1)` is available outside the shared internal positions.

The obstruction has a useful general form.  For consecutive shortened
central windows

\[
 S_i=R_d(i),\qquad S_{i+1}=R_d(i+1),
\]

their overlap contains

\[
 O_i=R_{d-1}(i+1)\subseteq S_i\cap S_{i+1}.
\]

If both `S_i,S_{i+1}` have rank `r`, then their portal satisfies

\[
 |R_{d+1}(i)|=|S_i\cup S_{i+1}|
 \le 2r-|O_i|.                                    \tag{3.4}
\]

Thus a portal of rank `r+h` consumes an overlap cell of rank at most `r-h`.
The short-row rank distribution controls portal heights.  The scalar number
`sigma` alone does not.

## 4. Audit of the graph interpretation

Ignoring Theorem 3.1, the isolated graph arithmetic is correct:

* a Johnson edge between two rank-six sets has a rank-seven union;
* a distance-two Johnson-graph pair has intersection rank four and union rank
  eight;
* a spanning linear forest on `369` vertices with `330` edges would have
  `369-330=39` components;
* joining `39` path components needs `38` additional edges.

Several necessary conditions are missing from the proposal even at this
isolated level:

1. the `330` colored edges must form a **linear** forest, not just a forest;
2. every bridge must join endpoints of two components; arbitrary component
   vertices would create degree three;
3. the `38` bridge unions must be distinct;
4. the resulting mixed-rank row must factor as `R_3=D^2A`; equivalently, every
   internal coordinate 1-run in that row must have length at least three;
5. it must factor through the prescribed distinct pair and singleton rows;
6. the lower labels must survive the exact coordinatewise pin test.

No existence proof for item 1 or 2 is given, and items 4--6 are not encoded by
the colored forest at all.  Theorem 3.1 shows that, with the proposed lower
rows, item 5 actually forbids the `38` distance-two bridges.

## 5. What survives of the broad single-switch conjecture

The no-go theorem does not contradict the first four clauses of the broad
Single-Switch Saturated Braid Conjecture.  Those clauses do not insist that
all `94` residual triple windows have rank five, nor that rank-eight masks be
represented immediately in row four.

In fact, under just the first four clauses at `k=11`, a similar containment
count shows that at least `93` of the `94` residual triples must have rank
five.  Therefore almost all internal `P` transitions are still forced to be
Johnson transitions.  Rank-eight and higher masks would have to be supplied
mostly by longer windows rather than by `38` distance-two portal edges.

Accordingly, a corrected construction target would have to couple:

* the rank distribution of every overlap row;
* the portal-height inequality (3.4);
* the factorization/run condition;
* exact lower pinning; and
* longer upper shadows.

The slogan “one unit of short-cell slack equals one arbitrary upper portal” is
false.  A more accurate slogan is:

> one unit of slack makes one length-`d+1` cell available, but the rank that
> cell can attain is limited by the lower label in its overlap.

The Portal Absorption Conjecture (`q<=sigma` implies repair of `q` missing
upper masks) therefore has no present proof.  The inequality is only a count;
it ignores portal heights and simultaneous pin survival.  The known `13<=369`
and `260<=392` comparisons are suggestive but not sufficient.

## 6. Checks at `k=9` and `k=14`

### `k=9`

There are two central maximizing-rank presentations.  Choosing the upper one,

\[
 r=5,\quad M=126,\quad d=2,\quad L=255,\quad\sigma=0,
\]

is correct.  It forces the `255` singleton/pair cells to represent precisely
the lower ranks and makes all `126` triple cells the rank-five row.  This
matches the rigid shape of the known optimum.  The tied lower choice `r=4`
has `sigma=126=M`; hence “the `k=9` defect is zero” is true only after choosing
the upper maximizing rank.

### `k=14`

The figures

\[
 r=7,\quad M=3432,\quad d=2,\quad L=6475,
 \quad\sigma=2M+3-L=392
\]

are correct.  A canonical single switch would put `392` rank-seven masks in
pair cells and the remaining `3040` in triple cells.  This saturates the known
short-cell count and coincides numerically with the `392` unused containment
slots in the current fixed-delay object.

It does not follow that the `392` cells can absorb the `260` current upper
omissions.  For `d=2`, consecutive shortened rank-seven pair windows share a
singleton, and (3.4) again couples the attainable triple-portal rank to that
singleton.  Moreover the current Hall matching is not a pin-surviving
labeling.  The `392>260` comparison establishes capacity only, not a
deformation theorem.

## 7. Pascal decomposition and length identities

The `k=9` to `k=11` Pascal count is correct:

\[
 \binom{11}{6}
 =\binom96+2\binom95+\binom94
 =84+126+126+126=462.
\]

The three tagged pieces have `378=3*126` vertices, and

\[
 369=378-9,\qquad93=84+9.
\]

This is clean numerology, but the proposal gives no operation proving that
the nine transferred masks repair all derivative rows and pin sets.

The one-coordinate length identities are also exact.  With

\[
 W_k=\binom{k}{\lfloor k/2\rfloor},\qquad d_k=B(k)-W_k,
\]

one has

\[
 W_{2m+1}=2W_{2m}-\operatorname{Cat}_m,
 \qquad \operatorname{Cat}_m={1\over m+1}\binom{2m}{m},
\]

and

\[
 W_{2m+2}=2W_{2m+1}.
\]

Therefore

\[
 B(2m+1)
 =2B(2m)-\bigl(\operatorname{Cat}_m+2d_{2m}-d_{2m+1}\bigr),
\]

\[
 B(2m+2)
 =2B(2m+1)-\bigl(2d_{2m+1}-d_{2m+2}\bigr).
\]

These are algebraic identities, not recursive constructions.  Existing
Catalan compression of a middle-layer order does not by itself compress a
common factor, preserve all lower witnesses, or preserve coordinate pins.
The proposed Pascal Fusion Conjecture is exactly the missing theorem, and is
not made more likely merely by the equality of target lengths.

## 8. Final status ledger

| Statement | Status after audit |
|---|---|
| Short-band count `L+sigma` | proved |
| Canonical schedule (1.2) is non-nested and monotone-band | proved, assuming `0<=sigma<=M` |
| Each shortened witness creates an available length-`d+1` cell | proved as a statement about physical cells |
| Each such cell is automatically a strict upper mask | false; small explicit counterexamples |
| All short cells can be labeled by all lower masks plus `sigma` rank-`r` masks | conjectural |
| `k=11` row cardinalities | correct |
| `369` vertices, `330` forest edges implies `39` components | correct conditional arithmetic |
| `38` distance-two internal bridges fit the saturated lower rows | false by Theorem 3.1 |
| Q-path gives `92+2=94` rank-five facets | correct conditional set identity |
| `q<=sigma` implies portal absorption | conjectural and unsupported by counting alone |
| `k=14` has `sigma=392`; `k=9,r=5` has `sigma=0` | correct |
| Catalan and odd/even `B` identities | proved algebraically |
| Single-switch braids are closed under Pascal fusion | conjectural |
| General identity `nu(k)=B(k)` | unresolved |

The proposal's big-picture instinct remains useful: unrestricted optima should
spend rank-count defect rather than force every central witness into one fixed
row.  The concrete lesson of this audit is that defect must be allocated
through the entire derivative triangle.  Portal cells cannot be designed
independently of the lower overlap cells that bound their ranks.
