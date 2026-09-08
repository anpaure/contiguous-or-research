# The `k=16` certificate is an exact facet/owner rank exchange

Date: 2026-07-31  
Status: independent theorem and raw-certificate replay; a reusable local
rank-exchange lemma is proved, but no all-`k` even lift is claimed

## 0. Result

Let

\[
 T=D^3(\texttt{answers/k15.word}),\qquad
 R^q=D^q(\texttt{answers/k16.word}),\qquad z=2^{15}.
\]

The previously observed `49`-slot bridge has a stronger description than an
arbitrary containment matching.

* `T[0:6390]` and `T[6390:6435]` are lower-rainbow Johnson cycles.
* The 49 substituted facets are exactly four consecutive edge facets of the
  large cycle and every edge facet of the 45-cycle.
* Each substituted facet is canonically matched to its **successor** owner.
  Thus the 49-by-49 matching is supplied by the oriented factor itself; no
  Hall choice is needed.
* The substitution is an exact exchange between adjacent derivative rows:
  owner mode serves a marked facet in `D^2` and its marked owner in `D^3`,
  whereas facet mode serves the marked facet in `D^3` and reconstructs its
  marked owner in `D^4`.

Numerically the two complete decks split as

\[
\begin{array}{c|ccc}
\text{deck}&\text{lower row}&\text{upper row}&\text{overlap}\\ \hline
z+\binom{[15]}7&D^2:6388&D^3:49&2\\
z+\binom{[15]}8&D^3:6386&D^4:50&1.
\end{array}                                             \tag{0.1}
\]

Both row unions have size `6435`.  This is the exact Pascal mechanism hidden
in the nonflat `k=16` carrier.

The main conceptual refinement is that **a facetified component need not be
small**.  Any complete lower-rainbow Johnson component can be exchanged
slot-for-slot at the two-deck level.  The size 45 is a property of this
certificate and its seam geometry, not a hypothesis of the algebraic lemma.

## 1. The facet/owner exchange lemma

Let

\[
 C=(V_0,V_1,\ldots,V_{s-1})
\]

be an oriented Johnson cycle of rank-`r` sets and put

\[
                         F_i=V_i\cap V_{i+1},        \tag{1.1}
\]

with indices modulo `s`.  Assume the edge facets `F_i` are distinct.  This is
exactly the lower-rainbow condition on the component.

### Lemma 1.1 (rank exchange)

For every `i`,

\[
 F_{i-1}\cup F_i=V_i.                               \tag{1.2}
\]

Consequently, after adjoining a new coordinate `z`,

\[
 (z\cup V_i)\cap(z\cup V_{i+1})=z\cup F_i,          \tag{1.3}
\]

\[
 (z\cup F_{i-1})\cup(z\cup F_i)=z\cup V_i,         \tag{1.4}
\]

and the typed cross-shore seam satisfies

\[
                       V_i\cup(z\cup F_i)=z\cup V_i.\tag{1.5}
\]

#### Proof

Both `F_(i-1)` and `F_i` are rank-`r-1` subsets of `V_i`.  They are distinct
by hypothesis, so each omits a different element of `V_i`; their union is
therefore `V_i`.  Equations (1.3)--(1.5) follow immediately.  \(\square\)

Now let an OR-derivative array satisfy

\[
                  R^{q+1}_j=R^q_j\cup R^q_{j+1}.    \tag{1.6}
\]

There are two modes for the marked copy of a component.

* **Owner mode:** place `z+V_i` in row `q`.  The owner is delivered there,
  while the facet `z+F_i` can be delivered one row below between consecutive
  owners.
* **Facet mode:** place `z+F_i` in row `q`.  The facet is delivered there,
  while (1.4) delivers `z+V_i` one row above automatically.

There is an important asymmetry.  Facet mode implies its upper-owner
delivery solely from (1.6).  Owner mode does **not** force its lower-facet
delivery from row `q` alone: it additionally requires the tight erosion

\[
                        R^{q-1}_{j+1}=z\cup F_i.     \tag{1.7}
\]

This tight-erosion condition is one of the genuine unsolved interfaces in a
uniform lift.

### Corollary 1.2 (complete-component facetification)

Rotate an unmarked copy of `C` so that it ends at `V_0`, and follow it by

\[
                    z\cup F_0,z\cup F_1,\ldots,z\cup F_{s-1}.\tag{1.8}
\]

The `s` facet entries in (1.8) deliver every marked facet directly.  The
cross-shore seam and the `s-1` internal unions deliver

\[
                    z\cup V_0,z\cup V_1,\ldots,z\cup V_{s-1} \tag{1.9}
\]

one row above.  Thus a whole component can change from owner mode to facet
mode without changing its number of marked slots.

No bound on `s` occurs in this statement.  Smallness may be needed for a
physical braid, residence, or the lower compiler, but it is not needed for
the rank exchange itself.

## 2. Literal five-block identity at `k=16`

Index the two parent components as

\[
 C_0=T[0:6390],\qquad C_1=T[6390:6435],             \tag{2.1}
\]

and define each `F_i` using the cyclic successor inside its own component.
The 6435 facets are distinct and are every rank-seven set on `[15]`.

The complete `D^3` row of the `k=16` answer is literally the following five
blocks:

\[
\begin{split}
R^3={}&zT[5113:6390]\ zT[0:5109]\\
 &\;zF[5108:5112]\\
 &\;T[5112:6390]\ T[0:5112]\\
 &\;T[6426:6435]\ T[6390:6426]\\
 &\;zF[6425:6435]\ zF[6390:6425].                 \tag{2.2}
\end{split}
\]

Here juxtaposition denotes concatenation, and `zX` means adjoining `z` to
every set in `X`.  The block lengths are

\[
                         6386, 4, 6390, 45, 45. \tag{2.3}
\]

Thus the unmarked shore is the entire parent carrier, with each component
independently rotated.  On the marked shore:

* the large component stays in owner mode except for owners
  `5109,5110,5111,5112`;
* facets `F_5108,F_5109,F_5110,F_5111` replace those four owners;
* the complete 45-component moves to facet mode.

The bridge-to-owner bijection is not merely a computed matching.  It is

\[
                         F_i\longmapsto T_{i+1}     \tag{2.4}
\]

inside the appropriate cyclic component.  On the large path this maps the
four facets to `T_5109,...,T_5112`; on the small cycle it maps its 45 facets
bijectionally to all 45 owners.

The exact equality

\[
                         49=4+45                    \tag{2.5}

is therefore proved directly.  In this certificate `4=d(16)+1`; the local
rank-exchange lemma itself does not assert that a uniform lift must always
choose `d+1` path facets.

## 3. The two deck partitions

Let `S_q` be the marked rank-eight values in `D^q A16`.  The audit proves

\[
 |S_2|=6388,\qquad |S_3|=49,qquad |S_2\cap S_3|=2, \tag{3.1}
\]

and

\[
                    S_2\cup S_3=z+\binom{[15]}7.   \tag{3.2}

In parent edge indices,

\[
 S_2=\{F_i:i\in[0,6390)\setminus\{5109,5110,5111\}\}
       \cup\{F_{6424}\},                            \tag{3.3}

\[
 S_3=\{F_{5108},F_{5109},F_{5110},F_{5111}\}
       \cup\{F_i:6390\le i<6435\}.                 \tag{3.4}

The two repeated boundary facets are `F_5108` and `F_6424`.

Similarly, let `O_q` be the marked rank-nine values in `D^q A16`.  Then

\[
 |O_3|=6386,\qquad |O_4|=50,qquad |O_3\cap O_4|=1, \tag{3.5}

and

\[
                    O_3\cup O_4=z+\binom{[15]}8.   \tag{3.6}

Here

\[
 O_3=\{zT_i:0\le i<6390,\ i\notin[5109,5113)\},    \tag{3.7}

\[
 O_4=\{zT_i:5108\le i<5113\}
       \cup\{zT_i:6390\le i<6435\}.               \tag{3.8}

The sole repeated boundary owner is `T_5108`.

Equations (3.1)--(3.8) are stronger than the rank census of `D^3`: they show
exactly how the two adjacent rows compensate each other.

## 4. What this does and does not generalize

The clean reusable object is a lower-rainbow Johnson 2-factor together with
a choice of owner-mode and facet-mode arcs.  The algebra gives three facts
for free:

1. every fully facetified component is slot preserving;
2. the missing-owner matching is its oriented successor map;
3. marked middle and marked owner decks exchange between adjacent rows.

This removes two unnecessary requirements from a prospective even theorem:
one does not need an arbitrary 49-by-49 Hall argument, and one does not need
a universally bounded small component merely to balance the two decks.

It leaves the genuinely global requirements untouched.

1. **Parent supply.**  One needs a parent factor whose edge facets form the
   complete lower rainbow, with recursive cut data.
2. **Tight erosion.**  Owner-mode edges need (1.7); this is not implied by
   the middle trace.
3. **Physical realizability.**  The mixed owner/facet row must be `D^d` of a
   nonempty word of the exact child length and satisfy residence.
4. **Depth changes.**  In general `d(2r)` need not equal `d(2r-1)`; the
   `D^3` anatomy of `15 -> 16` does not by itself handle a depth drop.
5. **Other ranks.**  The lemma closes only the marked middle/facet and owner
   decks.  Deep upper shadows and every lower target still need proof.
6. **Integral compiler.**  The erosion envelopes must admit one common Hall
   matching after all seams are fixed.
7. **Linear boundaries.**  The repeated facets and owner in (3.1),(3.5) are
   paid by the particular endpoint geometry.  A recurrence must construct
   compatible endpoints rather than assume them.

Accordingly, the strongest honest general target is a **mixed-mode
facet/owner braid theorem**: choose componentwise and pathwise modes in a
lower-rainbow parent factor, realize the resulting staircase as a physical
word, and prove simultaneous deep-shadow and lower-compiler feasibility.

The promoted `k=16` word proves that this target is nonempty in the first
even depth-three case.  It does not prove the all-`k` target.

## 5. Independent audit

Run

```text
python3 scratch/audit_k16_facet_owner_rank_exchange_20260731.py
```

It uses only the two word files and writes

```text
scratch/k16_facet_owner_rank_exchange_20260731.audit.json
```

The audit verifies the complete literal sequence (2.2), the canonical
successor matching, every identity (3.1)--(3.8), and the positional
facet/facet and typed-seam reconstructions in `D^4`.
