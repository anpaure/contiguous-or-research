# Genuine four-filter K16 seam braid gate

Date: 2026-07-31  
Scope: the authenticated natural lift and endpoint-preserving edge exchanges
only; no seed0-derived target order is used below.

## 1. Authenticated chronology

Let `W[0..6437]` be
`scratch/K15_FOURFILTER_SEED_20260731.word`, with SHA-256

`51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4`.

Put

\[
D_2(i)=\bigvee W[i..i+2],\qquad D_3(i)=\bigvee W[i..i+3],
\qquad z=\mathtt{0x8000}.
\]

There is one deficient three-cell row,

\[
D_2(6390)=\mathtt{0x13c8},\qquad |D_2(6390)|=6;
\]

the other 6,435 values of `D2` are the 6,435 distinct rank-seven masks, and
the 6,435 values of `D3` are all rank-eight masks on the old fifteen
coordinates.  The genuine natural K16 order is

\[
T=R_0+A+R_1
 =\operatorname{rev}(z\vee D_2[0..6389])
  +D_3[0..6434]
  +\operatorname{rev}(z\vee D_2[6391..6435]).
\]

Its block lengths are `6390,6435,45`, and its canonical newline-terminated
SHA-256 is

`0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c`.

## 2. The three block boundaries

The two linear seams and the outer endpoint pair are as follows.

| boundary | endpoint masks | union | rank |
|---|---:|---:|---:|
| `R0 | A` | `c3cc,43ce` | `c3ce` | 9 |
| `A | R1` | `738c,b38c` | `f38c` | 9 |
| outer pair `R1 | R0` | `b1cc,d38c` | `f3cc` | 10 |

The first two seam colours are redundant: each has multiplicity two in the
linear q1 edge multiset.  The outer pair is not a linear interval and
`f3cc` is consequently absent from the upper tower.

More generally, the internal edges of `R0` have colours

\[
z\vee D_3(i),\qquad 0\le i\le6388,
\]

and those of `R1` have colours

\[
z\vee D_3(i),\qquad6391\le i\le6434.
\]

The two linear seams merely repeat the endpoint colours
`z|D3(0)` and `z|D3(6434)`.  Hence the two omitted marked q1 colours are
exactly

\[
P=z\vee D_3(6389)=\mathtt{0xd3cc},\qquad
Q=z\vee D_3(6390)=\mathtt{0xb3cc}.
\]

This is the symbolic source of the q1 defect: deleting the deficient
`D2(6390)` target removes the two consecutive marked `D3` transitions, while
the two block seams spend their q1 load on duplicates.

## 3. Exact upper defect packet

A complete interval-OR scan gives precisely

\[
\{\mathtt{b3cc},\mathtt{d3cc},\mathtt{d3ce},
  \mathtt{dbce},\mathtt{f3cc},\mathtt{fbce}\}.
\]

Their ranks are `9,9,10,11,10,12`.  The containment diagram consists of

\[
\mathtt{d3cc}<\mathtt{d3ce}<\mathtt{dbce}<\mathtt{fbce},
\]

and

\[
\mathtt{b3cc}<\mathtt{f3cc}<\mathtt{fbce},\qquad
\mathtt{d3cc}<\mathtt{f3cc}.
\]

For every displayed missing mask `S`, every maximal contiguous run of
rank-eight facets contained in `S` has union of rank at most `rank(S)-1`.
The maxima are respectively `8,8,9,10,9,11`.  Thus each failure is literally
a one-coordinate-short run obstruction, rather than an omission from the
rank-eight layer.

The natural order is already scalar-dead for every three-hole depth-three
P/Q schedule: maximum selected area `25744`, optimistic capacity `25753`,
against required lower mass `26332`.

## 4. Exact three-cut obstruction

Any q1 repair must add an edge between two facets of `P` and an edge between
two facets of `Q`.  Each hole has nine facets and hence 36 possible unordered
facet edges.  For every pair of forced facet edges, assign each of its four
endpoint degree deficits to an incident old edge.  Retain assignments using
exactly three distinct cuts; the two remaining endpoint deficits force the
third new edge.  Degree replay and traversal decide whether the result is one
path with the two original global endpoints.

The exact census is:

- 16,384 incident-cut assignments;
- 671 assignments use three distinct cuts;
- 222 distinct degree-compatible three-edge exchanges;
- all 222 cut the unique q1 edge at cut `12779`, whose colour is `73cc`;
- after installing `P,Q`, the residual q1-hole counts are
  `3^160, 2^58, 1^4, 0^0`;
- 104 exchanges are connected paths, with residual counts
  `3^84, 2^19, 1^1, 0^0`.

Therefore no connected endpoint-preserving three-cut exchange completes q1.
The obstruction is sharper than a raw census: sharing one cut between the
two forced facet edges forces deletion of the sole `73cc` occurrence, and no
possible forced third edge restores `73cc`.

The unique connected exchange with only one residual q1 hole cuts

\[
(6389,12779,12824)
\]

and has order

\[
R_0+\operatorname{rev}(A[0..6389])
   +\operatorname{rev}(A[6390..6434])+R_1.
\]

Its new seam colours are

\[
\mathtt{d3cc},\quad\mathtt{73ce}\ (\text{rank }10),
\quad\mathtt{b3cc}.
\]

It leaves exactly the upper holes `{73cc,7bce}` and has all-schedule maximum
selected area `32047`, optimistic capacity `32056`, attained at

\[
X=(12781,12783,12872),\qquad Y=(0,1,6388).
\]

## 5. Unique minimal q1-complete braid

The analogous four-cut enumeration (unrestricted endpoint pairing, but with
the two global endpoints preserved) has 46,461 distinct degree-compatible
exchanges.  Their residual q1-hole distribution is

\[
4^{21307},\quad3^{19481},\quad2^{5242},\quad1^{421},\quad0^{10}.
\]

Nine of the ten q1-complete exchanges are disconnected.  The unique
connected one cuts

\[
(6389,12779,12780,12824)
\]

and has order

\[
R_0+\operatorname{rev}(A[0..6389])
   +A[6391..6434]+A[6390]+R_1.                 \tag{5.1}
\]

Its four new seam colours are

\[
\mathtt{d3cc},\quad
\mathtt{73ce}\ (\text{rank }10),\quad
\mathtt{73cc},\quad
\mathtt{b3cc}.
\]

The canonical word determined by (5.1) has SHA-256

`287b72a55e3c80174a1931fc9252da185816c4fbcbcff5c7b6f6b21f9ede5907`.

It is q1-complete and its only arbitrary-width upper hole is
`fbce` (rank twelve).  It supplies the five other old holes at intervals

```text
b3cc  [12824,12825]
d3cc  [6389,6390]
d3ce  [6388,6390]
dbce  [6389,6392]
f3cc  [12823,12825]
```

Its exact all-schedule P/Q maximum is selected area `32044`, optimistic
capacity `32053`, attained at

\[
X=(12780,12826,12827),\qquad Y=(0,1,6388).
\]

Thus four cuts are necessary and sufficient for endpoint-preserving connected
q1 completion in this forced-edge exchange class, and (5.1) is the unique
minimal connected braid.  Endpoint-changing reassemblies are outside this
census.  It is a strong carrier lead, not a K16 word: `fbce`, lower Hall,
simultaneous capped-envelope realization, and literal replay remain open.

## 6. Next connector gate

From (5.1), a q1-safe single-reversal screen aimed at `fbce` has 107
reversals that create an `fbce` interval.  Ten are fully upper-complete.  The
shortest has cuts `(6392,7052)`, span 660, removes colours `5b0f,69cd`, adds
`7bce,7b8f`, and has canonical SHA-256

`3b2cee2853fffdf30343118de268444f350ac3772495fdee2b3a86a8b206065c`.

This last row is only a carrier-order lead.  Its all-schedule P/Q and lower
Hall audits were not completed here, so it must not be promoted to a literal
compiler candidate without those checks.
