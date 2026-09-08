# The oriented two-hex `T2` relay has an internal support-monotone phase-clock lift for every clock depth

**Date:** 2026-08-13  
**Status:** unconditional finite-base and all-`h` theorem for intervals
contained in one oriented z-free path.  The orientation is the one induced,
up to global reversal, by the fixed complementary closure after the two
hexagons.  No statement is made here about an interval crossing the
z-present return or the final lifted cyclic closure.

## 1. The five affected canonical paths

Use the five semilength-six Dyck roots

```text
x0  = 111111000000,
x2  = 111110010000,
x1  = 111110100000,
x62 = 110101110000,
x11 = 111100110000.
```

Their canonical owner paths, from forward endpoint `F` (position zero) to
reverse endpoint `R` (position six), are

```text
x0:
111111000000 101111000001 101011000101 101010010101
101000110101 100000111101 000000111111

x2:
111110010000 101110010001 101110000101 101010001101
101001001101 100001101101 000001101111

x1:
111110100000 101110100001 101010100101 101001100101
101001010101 100001011101 000001011111

x62:
110101110000 110100110001 110100100101 110100001101
110000001111 100010001111 001010001111

x11:
111100110000 101100110001 101001110001 100011110001
100011100101 100011001101 000011001111.
```

Order the affected paths as

\[
                         (x0,x2,x1,x62,x11).          \tag{1.1}
\]

Orient `x0,x1` from `R` to `F` and the other three from `F` to `R`.
Equivalently, relative to the forward orientations, use reversal mask

\[
                         00101_2=5.                  \tag{1.2}
\]

The global reverse orientation is mask

\[
                         11010_2=26.                 \tag{1.3}
\]

All unaffected paths may be oriented arbitrarily but identically in the
two states.

After the two frozen hexagons, the five new z-free paths have endpoint
pairs

\[
 F_0F_{11},\quad F_2R_{62},\quad F_1R_0,\quad
 F_{62}R_{11},\quad R_1R_2.                        \tag{1.4}
\]

Alternating these with the fixed complementary closure pairs `F_xR_x`
gives one lifted cycle.  Its traversal is

\[
 F_0,F_{11},R_{11},F_{62},R_{62},F_2,R_2,R_1,
 F_1,R_0,F_0.                                       \tag{1.5}
\]

Thus `(1.3)`, or its global reverse `(1.2)`, is precisely the orientation
forced by the actual merged lifted cycle.  The five reversals are not
independent artificial choices.

## 2. Phase clock

The union of the oriented old and new owner adjacencies is bipartite.  Fix
one common phase map

\[
                         \epsilon:V\longrightarrow\{0,1\}.     \tag{2.1}
\]

For `h>=2`, let

\[
 D_t=\{u_t,u_{t+1},\ldots,u_{t+h-1}\}
       \subseteq\mathbb Z_{2h}.                    \tag{2.2}
\]

Replace an owner occurrence `v` by the clock block

\[
 \Gamma_v=
 \begin{cases}
 (V_v+D_0,V_v+D_1,\ldots,V_v+D_h),&\epsilon(v)=0,\\
 (V_v+D_h,V_v+D_{h+1},\ldots,V_v+D_{2h}),&\epsilon(v)=1,
 \end{cases}                                       \tag{2.3}
\]

where `D_(2h)=D_0`; a common fixed core may be adjoined throughout.  Join
consecutive blocks at their common antipodal anchor as in the phase-clock
dilation theorem.

Let `Deck_h^-(P)` and `Deck_h^+(P)` be the supports of literal unions of
all nonempty intervals of lifted owners which are contained in one old or
new lifted z-free path, respectively.

## 3. Finite stratified certificate

For an oriented base owner interval

\[
                         I=(v_i,\ldots,v_j),          \tag{3.1}
\]

put

\[
 T(I)=\bigcup_{t=i}^jV_{v_t},qquad s(I)=j-i+1.     \tag{3.2}
\]

Retain the following finite signature:

\[
 \sigma(I)=
 \begin{cases}
 (T(I),s(I),\epsilon(v_i),\ldots,\epsilon(v_j)),&s(I)\le2,\\
 (T(I),s(I)),&s(I)\ge3.
 \end{cases}                                       \tag{3.3}
\]

### Lemma 3.1 (exact finite support certificate)

For the orientations `(1.2)` (and therefore `(1.3)`), every old signature
in `(3.3)` occurs in the new paths.

More exactly, the finite supports have sizes

```text
stratified signatures: old 2382, new 2404, loss 0, birth 22;
oriented two-block signatures (A union B, epsilon(A)):
                       old 792,  new 792,  loss 0, birth 0.
```

The owner singleton row is identical because the rethread changes no
owner.  The five changed oriented two-block unions, all beginning in phase
zero, are merely permuted:

```text
old x0  : 101010010101 -> 101011000101, OR 101011010101
old x2  : 101010001101 -> 101001001101, OR 101011001101
old x1^R: 100001011101 -> 101001010101, OR 101001011101
old x62 : 100010001111 -> 001010001111, OR 101010001111
old x11 : 100011001101 -> 000011001111, OR 100011001111

new path 1: 100011001101 -> 101011000101, OR 101011001101
new path 2: 101010001101 -> 001010001111, OR 101010001111
new path 3: 101010010101 -> 101001010101, OR 101011010101
new path 4: 100010001111 -> 000011001111, OR 100011001111
new path 5: 100001011101 -> 101001001101, OR 101001011101.
```

Every unlisted oriented edge is literal in both states.

### Proof

The singleton and two-block statements follow directly from the displayed
owner lists and five-edge ledger.  Exhaustive enumeration of every base
owner interval gives the quoted stratified counts.  This is a finite exact
certificate, independently replayed on H100. `square`

## 4. All-depth support theorem

### Theorem 4.1

For every `h>=2`,

\[
             \boxed{Deck_h^-(P)\subseteq Deck_h^+(P).}          \tag{4.1}
\]

Thus the oriented `T2` relay has a two-sided depth-`h` phase-clock lift
which loses no old literal owner-union value on intervals contained in one
z-free path.

### Proof

Take a lifted old interval `J`.  Let `I` be the base owner interval formed
by the clock blocks met by `J`, and let `s=s(I)`.

If `s=1`, Lemma 3.1 supplies the same owner in the new state.  Use the same
two endpoint offsets in its clock block.  The base union and literal clock
union are identical.

If `s=2`, Lemma 3.1 supplies a new oriented edge with the same owner union
and the same ordered phase word.  Use the same start/end offsets.  Formula
`(2.3)` then gives the same literal clock union, and the number of lifted
owners is unchanged.

Suppose `s>=3`.  The interval contains every owner of each block strictly
between its first and last blocks.  In particular it contains one complete
clock block.  For either phase,

\[
                 \bigcup_{t=0}^{h}D_t
                  =\bigcup_{t=h}^{2h}D_t
                  =\mathbb Z_{2h}.                 \tag{4.2}
\]

Hence the clock contribution of `J` is the full clock ground, independent
of its endpoint phases and offsets.  Lemma 3.1 supplies a new base interval
with the same `T(I)` and the same number `s` of blocks.  If the old endpoint
offsets are `a,b`, choose any new endpoint offsets with the same sum
`a+b`; for example reuse `a,b`.  Both lifted intervals then have the same
number

\[
                         (s-2)(h+1)+(h+1-a)+(b+1)   \tag{4.3}
\]

of owners, the same base union, and by `(4.2)` the same full clock union.
This constructs a same-width mate in every case and proves `(4.1)`.
`square`

The argument works even when `J` starts or ends at a block boundary: with
at least three distinct met blocks, every block strictly between the first
and last is still complete.

## 5. Independent H100 replay

The script

```text
scratch/audit_msw_t0_relay_phase_endpoint_refinement.py
```

reconstructs the complete canonical semilength-six factor, performs the
two literal hexagons, derives the common phase map, searches all orientation
masks of the five affected old/new path banks, and enumerates exact lifted
support fibers `(base union, lifted width, literal clock union)`.

For masks `5` and `26`, the exact counts are

```text
h= 2: old  13626, new  13702, loss 0, birth  76
h= 3: old  21822, new  21925, loss 0, birth 103
h= 4: old  31734, new  31864, loss 0, birth 130
h= 5: old  43362, new  43519, loss 0, birth 157
h= 6: old  56706, new  56890, loss 0, birth 184
h= 7: old  71766, new  71977, loss 0, birth 211
h= 8: old  88542, new  88780, loss 0, birth 238
h= 9: old 107034, new 107299, loss 0, birth 265
h=10: old 127242, new 127534, loss 0, birth 292
h=11: old 149166, new 149485, loss 0, birth 319
h=12: old 172806, new 173152, loss 0, birth 346.
```

These finite replays check the implementation; Theorem 4.1 is the symbolic
all-`h` proof.

## 6. Exact scope

### Width indexing

If a depth-`d` source is written in the convention that one base owner is
the union of `d+1` consecutive source letters, then an interval of `s`
consecutive base owners is the union of `d+s` consecutive source letters.
A window of `q` consecutive q1 incidence colours spans `q+1` base owners,
and therefore corresponds to source width

\[
                              d+q+1.                \tag{6.1}
\]

In particular the ordinary q2 turn (`q=2` q1 colours, three owner blocks)
lies at source width `d+3`, not `d+2`.  The proof of Theorem 4.1 directly
enumerates owner intervals and is unaffected by this change of indexing.

Proved:

* the orientation is globally legal and is the actual fixed-closure
  orientation of the merged lifted component;
* the phase clock gives both positive and zero runs at least `h`, by the
  general phase-clock theorem;
* every old lifted interval contained in one z-free path retains a
  same-width, same-value new witness for every `h`.

Not proved here:

* support of intervals crossing into a z-present complementary return;
* support of arbitrary cyclic intervals of the complete lifted odd wreath;
* a resident lifted realization of those z-present returns;
* the prepared `1100` annulus module or its recursive planting; or
* the final exterior/cap/compiler interfaces.
