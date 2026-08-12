# The static lower-ideal gate, separated from arrival-clock chronology

Date: 2026-07-27

## 1. Authoritative linear statement

Put

\[
r=\lceil k/2\rceil,\qquad
W=\binom{k}{r},\qquad
\Lambda=\sum_{j=1}^{r-1}\binom{k}{j},
\]

and let `d=d(k)` be the least integer such that

\[
dW+\binom{d+1}{2}\geq \Lambda.
\]

Thus

\[
e=dW+\binom{d+1}{2}-\Lambda.
\tag{1.1}
\]

The exact **linear static chain-anchor problem** is to partition the
nonempty lower ideal

\[
\mathcal L_k=\{S\subseteq[k]:1\leq |S|<r\}
\]

among the following labelled bins.

1. For every `T in binom([k],r)`, one anchored chain `C_T` of length at
   most `d`, with every member of `C_T` contained in `T`.
2. `d` unanchored boundary chains of capacities

   \[
   d,d-1,\ldots,1.
   \]

Every occupied bin is strictly increasing under inclusion.  The total
number of unused slots is then automatically the exact slack `e` in (1.1).

This is the correct static object for a **linear** word.  The cyclic object
with only the `W` anchored chains has capacity `dW`, not
`dW+binom(d+1,2)`.  In particular it is arithmetically impossible at

\[
k=6:\quad dW-\Lambda=20-21=-1,
\]

and

\[
k=9:\quad dW-\Lambda=252-255=-3.
\]

The boundary staircase is therefore structural; it is not optional
bookkeeping.

## 2. Exact interface with arrival clocks

Fix one middle anchor `T` and a depth `d`.  A local arrival label

\[
a:T\longrightarrow\{0,1,\ldots,d\}
\]

produces the threshold chain

\[
S_t=\{x\in T:a(x)\leq t\},\qquad 0\leq t<d.
\tag{2.1}
\]

Conversely, every weak chain

\[
S_0\subseteq S_1\subseteq\cdots\subseteq S_{d-1}\subseteq T
\]

is locally realized by

\[
a(x)=\min\{t:x\in S_t\},
\]

with `a(x)=d` when `x` never enters.  A strict chain of length at most `d`
is realized by placing its members at increasing thresholds and using
repetitions or empty threshold cells in the remaining slots.  Those
non-new cells are exactly what the static hole count records.

Therefore the static chain-anchor condition is precisely the **columnwise**
part of the arrival-clock formulation.  It does not encode the global
countdown law

\[
x\in T_i\cap T_{i+1},\quad a_i(x)>0
\quad\Longrightarrow\quad
a_{i+1}(x)=a_i(x)-1.
\tag{2.2}
\]

Nor does it choose the chronology `(T_i)`.  The boundary chains arise only
after a linear cut and lie outside the cyclic `W`-column clock system.

Hence:

\[
\boxed{\text{static feasibility is necessary but strictly weaker than
arrival-clock feasibility.}}
\]

## 3. Every antichain-capacity obstruction vanishes

Let the capacity multiset be

\[
\underbrace{d,\ldots,d}_{W\text{ times}},d,d-1,\ldots,1.
\]

For a partition into chains with these upper bounds, a necessary condition
is

\[
\max\{|A_1\cup\cdots\cup A_t|:A_i\text{ antichains}\}
\leq \sum_j\min(t,c_j).
\tag{3.1}
\]

The lower Boolean ideal is strongly Sperner, so the left side is the sum of
its `t` largest ranks:

\[
\sum_{j=0}^{t-1}\binom{k}{r-1-j}
\]

until every rank has been used.  If `t<=d`, this is at most `tW`, while the
anchored bins alone contribute `tW` to the right side of (3.1).  If `t>d`,
the right side is the full capacity `Lambda+e`, at least the size `Lambda`
of the poset.  Thus (3.1) holds for every `t`.

This proves that there is **no scalar/strong-Sperner obstruction** to the
static problem.  It does not prove the partition exists: the inequalities
do not simultaneously manufacture chains of the prescribed capacities,
and they contain no information about the anchor labels.

The anchoring condition has its own Hall obstruction in general.  For
example, at `k=7,r=4`, there are 22 lower masks containing a fixed element
`x`, but only 20 middle four-sets containing `x`.  Any prescribed list of
21 chain maxima chosen from that lower star cannot be matched to distinct
middle anchors.  A successful chain construction must balance its maxima;
anchoring cannot simply be appended to an arbitrary chain partition.

## 4. Independent exact finite certificates

The exact SAT encoding assigns every lower mask to one labelled slot,
enforces at-most-one mask per slot, strict inclusion inside every occupied
bin, and containment in the labelled middle anchor.  It contains no word,
chronology, derivative, or arrival-clock recurrence.

The following instances were independently verified.

| `k` | `r` | `W` | `Lambda` | `d` | `e` | anchored length histogram | occupied boundary lengths | method |
|---:|---:|---:|---:|---:|---:|---|---|---|
| 3 | 2 | 3 | 3 | 1 | 1 | `0:1, 1:2` | `1` | SAT |
| 4 | 2 | 6 | 4 | 1 | 3 | `0:3, 1:3` | `1` | SAT |
| 5 | 3 | 10 | 15 | 2 | 8 | `1:5, 2:5` | `0,0` | SAT |
| 6 | 3 | 20 | 21 | 1 | 0 | `1:20` | `1` | SAT |
| 7 | 4 | 35 | 63 | 2 | 10 | `1:10, 2:25` | `2,1` | SAT |
| 8 | 4 | 70 | 92 | 2 | 51 | `0:6, 1:36, 2:28` | `0,0` | SAT |
| 9 | 5 | 126 | 255 | 2 | 0 | `2:126` | `2,1` | two matchings |
| 10 | 5 | 252 | 385 | 2 | 122 | `0:42, 1:35, 2:175` | `0,0` | two matchings |
| 11 | 6 | 462 | 1023 | 3 | 369 | `1:66, 2:231, 3:165` | `0,0,0` | three matchings |
| 15 | 8 | 6435 | 16383 | 3 | 2928 | `1:939, 2:1044, 3:4452` | `0,0,0` | three matchings |

### The explicit `k=9` construction

Reserve the boundary chains

\[
\{1\}\subset\{1,2\},\qquad \{3\}.
\]

The remaining 126 masks of ranks one through three have a perfect
containment matching into the 126 four-sets.  Independently, the 126
four-sets have a perfect containment matching into the 126 five-set
anchors.  Composing them gives 126 anchored two-chains, and all 255 lower
masks occur exactly once.  This also makes transparent why the three
boundary cells are essential at this zero-slack case.

### The explicit `k=11` construction

1. Match all 165 three-sets injectively into distinct four-sets.
2. Treat the resulting 165 pairs, the other 165 four-sets, and all 66
   one/two-sets as 396 predecessor chains.  A perfect containment matching
   assigns their maxima to 396 distinct five-sets.
3. The other 66 five-sets are singleton lower chains.  Match all 462
   five-sets bijectively to the 462 six-set anchors.

This gives 165 anchored chains of length three, 231 of length two, and 66
of length one.  It uses all 1023 lower masks exactly once and leaves

\[
3\cdot462+6-1023=369
\]

slots unused.  In particular, the static lower-ideal/anchor gate is **not**
the obstruction at the first difficult case `k=11`; the missing work is
entirely in finding one chronology whose clocks realize these columns (or
some other feasible static tableau) while satisfying (2.2).

### The explicit `k=15` construction

The same static gate remains tractable well beyond the solved finite
frontier.  Three ordinary containment matchings give a certificate at the
exceptional next target `k=15`:

1. match all 5005 rank-six masks injectively into rank seven;
2. match every mask of ranks one through five to either one of those 5005
   rank-six slots or one of the 1430 unused rank-seven slots;
3. match all 6435 rank-seven masks bijectively to the rank-eight anchors.

The resulting anchored-chain histogram is

```text
length 1: 939
length 2: 1044
length 3: 4452
```

and all 16383 lower masks occur exactly once.  The 2928 unused cells equal
the scalar slack, including the six empty boundary-staircase cells.  This
proves that the attractive `k=15` PBBS/orbit-trade lane has no independent
static Hall obstruction; its remaining gate is again the global countdown
compatibility with the selected middle chronology.

The independently checked certificate is
`scratch/sigma_calibration_static_chain_k15.certificate.json`, SHA-256
`17cb6649b0a32a56df042dba9f8352c8c782f152733de22cbe80e3cb0df9e2a9`.

Reproduction:

```sh
for k in 3 4 5 6 7 8; do
  python3 scratch/sigma_calibration_static_chain_sat.py --k "$k"
done
python3 scratch/sigma_calibration_static_k9_matching.py
python3 scratch/sigma_calibration_static_k10_matching.py
python3 scratch/sigma_calibration_static_k11_matching.py
python3 scratch/sigma_calibration_static_k15_matching.py
```

Certificates are written to
`scratch/sigma_calibration_static_chain_k*.certificate.json`.

## 5. Literature boundary

The exact general static statement is not being claimed here.  It resembles
equitable-chain questions, but it is one-sided and additionally anchor
labelled, so no equivalence is asserted.

Füredi's stronger-looking full-lattice conjecture asks for a partition of
`2^[n]` into the minimum number of chains whose sizes differ by at most one;
it remains open.  Tomon proved rank-symmetric chains of size
`Theta(sqrt(n))`, and Sudakov--Tomon--Wagner proved an asymptotically
uniform decomposition in which all but an
`n^{-1/8+o(1)}` proportion of chains have near-average length.  Neither
result supplies this exact finite capacity vector or the distinct middle
anchors.

Primary sources:

- Istvan Tomon, *Decompositions of the Boolean Lattice into Rank-symmetric
  Chains*, EJC 23(2), P2.53 (2016):
  https://doi.org/10.37236/5328
- Benjamin Sudakov, Istvan Tomon, and Zsolt Wagner, *Uniform chain
  decompositions and applications*, arXiv:1911.09533:
  https://arxiv.org/abs/1911.09533

## 6. Precise remaining theorem

The static question has passed every tested finite case, including `k=11`,
and all strong-Sperner capacity tests.  The unresolved general static
statement is:

> For every `k`, does the linear capacity vector in Section 1 admit a
> partition of `L_k` into anchor-labelled and boundary chains?

Even a positive answer would leave the genuinely global theorem:

> Can the `W` anchored chains be ordered by their distinct middle anchors
> and padded to depth `d` so that the corresponding labels satisfy the
> countdown recurrence (2.2), with the boundary staircase supplied by one
> linear cut?

The first is a static capacitated chain/Hall problem.  The second is the
arrival-clock rotor problem.  The computations show decisively that they
should no longer be conflated.
