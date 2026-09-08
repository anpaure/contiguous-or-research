# Gate C: the mesoscopic parity ledger and an exact staircase orbit

**Status (2026-08-22).**  Every assertion below is proved.  The sharp
coefficient-one-compatible replacement for the impossible `q-O(b)` target
is a parity bandwidth
\[
 K=a_b\sqrt b,\qquad a_b\longrightarrow\infty,
 \qquad a_b=o(\sqrt b).
\]
Such a band contains all but `o(N)` middle targets, while `N/q` tours
losing `O(bK)` flags each have only `o(N)` aggregate defect.

We also give an exact balanced parity-word orbit with `4j` same-parity
Hamilton edges whose coherent windows reach every split layer
`|2a-b|<=2j+1`.  Its complete flag degrees are explicit.  Odd-indexed
staircase orbits admit a nonnegative, asymptotically lossless *marginal*
fractional cover of every complete flag in the corresponding band.

This does not yet cover a fixed central factor efficiently.  Uniformly
labelling any such parity orbit gives only `O(1)` expected hits in a fixed
factor per phase support, so a factor-uniform orbit mixture has support
mass `Omega(N)`, rather than the required `Theta(N/q)`.  The remaining
problem is therefore a factor-adapted selection of highly atypical
coordinate labellings, followed by integral rankwise packing.

Throughout,
\[
 n=2b,\quad b\ge3\text{ odd},\quad
 E=\{0,2,\ldots,2b-2\},\quad O=\{1,3,\ldots,2b-1\},
\]
\[
 h={b-1\over2},\qquad q=b(b-1),\qquad
 N=\binom{2b}{b-1},\qquad W=\binom{2b}{b}={b+1\over b}N.       \tag{0.1}
\]

## 1. The coefficient-one scale ledger

For a middle target `C`, put
\[
 A(C)=|C\cap E|,\qquad D(C)=2A(C)-b.                          \tag{1.1}
\]

### Lemma 1.1 (hypergeometric parity tail)

For a uniformly random `b`-subset `C` of `[2b]` and every `K>=0`,
\[
 \Pr\{|D(C)|>K\}\le 2\exp\{-K^2/(8b)\}.                    \tag{1.2}
\]

#### Proof

Expose a sample without replacement of `b` objects from a population of
`b` even and `b` odd objects.  If `X=A(C)` and `F_i` is the information
after `i` draws, let `M_i=E[X|F_i]`.  Conditional on `F_i`, the two possible
values of `M_{i+1}` differ by
\[
 1-{b-i-1\over2b-i-1}={b\over2b-i-1}\le1.                 \tag{1.3}
\]
Since `M_i` is between those two values, `|M_{i+1}-M_i|<=1`.
Azuma's exponential-moment proof therefore gives
\[
 \Pr\{|X-b/2|>t\}\le2e^{-t^2/(2b)}.
\]
Taking `t=K/2` proves (1.2).  \(\square\)

Let
\[
 \mathcal B_K=\{C\in\tbinom{[2b]}b:|D(C)|\le K\}.          \tag{1.4}
\]
If `K=a_b sqrt(b)` with `a_b -> infinity`, (1.2) gives
\[
 |\mathcal B_K|=(1-o(1))W.                                 \tag{1.5}
\]
Every central flag factor uses at most one flag over each middle target.
Consequently any factor of size `N` has only `o(N)` flags outside
`B_K`, because `W/N=1+1/b`.

### Proposition 1.2 (conditional sufficiency ledger)

Assume `K->infinity`, `K=o(b)`, and suppose all but `o(N)` flags of a
central factor can be partitioned among
\[
 T=(1+o(1)){N\over q}                                      \tag{1.6}
\]
coherent partial phase supports, each obtained from a full support by
deleting `O(b(K+1))` flags.  Then the total deletion cost is `o(N)`.
An additional `O(b)` seam or connector cost per support is also `o(N)`.

#### Proof

The two totals are respectively
\[
 O\left({N\over b^2}\,b(K+1)\right)
   =O\left(N{K+1\over b}\right)=o(N),
 \qquad
 O\left({N\over b^2}b\right)=O(N/b)=o(N).                \tag{1.7}
\]
Together with the `o(N)` band complement from (1.5), these are exactly
coefficient-one-sized errors.  \(\square\)

Thus `K=a_b sqrt(b)`, with `a_b->infinity` arbitrarily slowly and
`a_b=o(sqrt(b))`, simultaneously makes the band exhaustive and makes
`O(bK)=o(q)` per-tour loss affordable.

## 2. Endpoint--deletion normal form

Let `H=(h_0,...,h_{2b-1})` be a directed Hamilton listing and encode its
coordinate parities by
\[
 \sigma_i=+1\quad(h_i\in E),\qquad
 \sigma_i=-1\quad(h_i\in O).                              \tag{2.1}
\]
The word `sigma` is balanced.

Across the two coherent phases, the internal template offsets are
\[
 z=\delta+s(b+1)\pmod {2b},\qquad
 \delta\in\{0,1\},\quad0\le s<b.                         \tag{2.2}
\]
Because `gcd(b+1,2b)=2`, these offsets run through every residue exactly
once.  For offset `z` and `1<=t<b`, the template has index set and arc
\[
 J=z+([t,b+t]\setminus\{b\}),qquad
 p=z+b+t\longrightarrow p+1.                             \tag{2.3}
\]

Put
\[
 I_p=[p-b,p]\pmod {2b},\qquad S_p=\sum_{i\in I_p}\sigma_i. \tag{2.4}
\]

### Lemma 2.1 (endpoint--deletion bijection)

The templates in the two phases are in bijection with pairs `(p,c)`,
where `p` is the arc-start index and `c` is one of the `b-1` strict
interior points of `I_p`.  The middle index set is `I_p\{c}`.  If
`sigma_p != sigma_{p+1}`, its split discrepancy is
\[
                         D=S_p-\sigma_c.                  \tag{2.5}
\]

#### Proof

In (2.3), the interval starts at `z+t=p-b`, ends at `p`, and deletes
`c=z+b=p-t`.  As `t` runs from `1` to `b-1`, `c` runs bijectively over
the strict interior of `I_p`.  Equation (2.5) is immediate. \(\square\)

This form is useful because every flag of the Catalan-switched factor has
a cross-parity coordinate arc.  Same-parity endpoints are compulsory
deletions; cross endpoints are classified only by `S_p` and the parity of
the deleted interior point.

## 3. An exact antipodal staircase

Fix `j>=1` with `4j<=b-1`.  Start with the alternating word
`sigma_i^0=(-1)^i`.  For
\[
 A_j=\{1,5,9,\ldots,4j-3\},                               \tag{3.1}
\]
flip the signs at every position in `A_j` and at every antipodal position
in `A_j+b`.  Call the resulting word `sigma^(j)`.

### Theorem 3.1 (staircase census)

The word `sigma^(j)` has the following properties.

1. It is balanced and antipodal:
   \[
   \sigma_{i+b}^{(j)}=-\sigma_i^{(j)}.                    \tag{3.2}
   \]
2. It has exactly `4j` same-parity cyclic edges.
3. At a cross edge `p->p+1`, the only possible values of `S_p` are
   \[
   -2j,-2j+4,\ldots,2j-4,2j.                             \tag{3.3}
   \]
   Write `N_{S,+}` and `N_{S,-}` for the numbers of such endpoints with
   `sigma_p=+1` and `sigma_p=-1`.  At the extremes,
   \[
   \begin{array}{c|cc}
       &N_{S,+}&N_{S,-}\\ \hline
   S= 2j&(b-4j+3)/2&(b-4j+1)/2\\
   S=-2j&(b-4j+1)/2&(b-4j+3)/2,
   \end{array}                                           \tag{3.4}
   \]
   while every interior value in (3.3) has
   \[
                         N_{S,+}=N_{S,-}=2.               \tag{3.5}
   \]

#### Proof

The base word is antipodal because `b` is odd, and paired antipodal flips
preserve (3.2).  Every antipodal pair contains one plus and one minus, so
the word is balanced.  Each flipped position is isolated from the other
flips in its own semicircle.  A flipped odd position in `A_j` creates two
`++` edges; its antipode creates two `--` edges.  These `4j` edges are
distinct, proving item 2.

Antipodality makes the two endpoints of `I_p` cancel.  Moreover
\[
 S_{p+1}-S_p=\sigma_{p+1}-\sigma_{p-b}
             =\sigma_{p+1}+\sigma_p.                    \tag{3.6}
\]
Thus `S` is constant on cross edges, rises by two across each `++` edge,
and falls by two across each `--` edge.  Scanning the isolated pairs in
(3.1), the accessible levels rise in steps of four from `-2j` to `2j`,
then fall antipodally.  Every nonextreme level is met on two cross edges
in each semicircle, once with each endpoint sign.  The two extreme cross
runs have length `b-4j+2`; their alternating endpoint signs differ by one
in the directions displayed in (3.4).  This proves (3.3)--(3.5).
\(\square\)

For a level `S`, the strict interior of `I_p` contains exactly
\[
 u_S={b-1+S\over2}\quad\hbox{plus positions},\qquad
 v_S={b-1-S\over2}\quad\hbox{minus positions},           \tag{3.7}
\]
because its antipodal endpoints cancel.

### Corollary 3.2 (exact template histogram)

Let `mu_{d,epsilon}^{(j)}` count, across both phases, the templates with
cross-parity arc, split discrepancy `d`, and arc-start sign `epsilon`.
Then
\[
 \boxed{
 \mu_{d,\epsilon}^{(j)}=
 \sum_{S\in\{-2j,-2j+4,\ldots,2j\}}N_{S,\epsilon}
 \left(u_S\mathbf1_{d=S-1}+v_S\mathbf1_{d=S+1}\right).} \tag{3.8}
\]
In particular, every odd `d` with `|d|<=2j+1` occurs with both endpoint
signs.  The number of cross-arc templates is exactly
\[
 \sum_{d,\epsilon}\mu_{d,\epsilon}^{(j)}
 =(2b-4j)(b-1).                                          \tag{3.9}
\]

#### Proof

Deleting a plus interior point gives `d=S-1` in `u_S` ways; deleting a
minus point gives `d=S+1` in `v_S` ways.  Formula (3.8) follows from
Lemma 2.1.  The pairs `S-1,S+1` for the arithmetic progression (3.3)
partition all odd integers in the stated interval.  All factors in
(3.4), (3.5), and (3.7) are positive.  Finally there are `2b-4j` cross
edges and `b-1` deletion choices over the two phases, proving (3.9).
\(\square\)

## 4. Exact labelled-orbit flag degrees

Fix any balanced parity word `sigma`.  Label its plus positions
bijectively by `E` and its minus positions bijectively by `O`; there are
`(b!)^2` such labellings.  Retain both coherent phases.  This is a labelled
multiorbit, so no unsupported simplicity or stabilizer assertion is
needed.

Let `F_{a,+}` be the complete flags whose middle contains `a` even
coordinates and whose `p=C\L` coordinate is even.  Define `F_{a,-}`
analogously.  Their sizes are
\[
 |\mathfrak F_{a,+}|=\binom ba^2a^2,
 \qquad
 |\mathfrak F_{a,-}|=\binom ba^2(b-a)^2.                 \tag{4.1}
\]

### Theorem 4.1 (orbit degree formula)

If `d=2a-b`, the labelled two-phase orbit of `sigma^(j)` has constant
degree on each complete flag type, namely
\[
 \boxed{
 \Delta_{a,+}^{(j)}=mu_{d,+}^{(j)}((a-1)!(b-a)!)^2,
 \qquad
 \Delta_{a,-}^{(j)}=mu_{d,-}^{(j)}(a!(b-a-1)!)^2.}      \tag{4.2}
\]
Equivalently,
\[
 \Delta_{a,\epsilon}^{(j)}
 ={(b!)^2\mu_{d,\epsilon}^{(j)}\over
   |\mathfrak F_{a,\epsilon}|}.                          \tag{4.3}
\]

#### Proof

Fix a template occurrence of type `(a,+)` and a particular flag of that
type.  The fixed even arc-start and odd arc-end labels leave `a-1` and
`b-a` even labels to permute inside and outside, and respectively `b-a`
and `a-1` odd labels.  Hence exactly
`((a-1)!(b-a)!)^2` labellings realize the flag.  For type `(a,-)` the
same count is `(a!(b-a-1)!)^2`.  Multiply by the exact number of template
occurrences in (3.8).  Formula (4.3) is the same identity using (4.1).
\(\square\)

## 5. What the staircase orbit covers fractionally

If only the extreme levels `S=+-2j` are retained, then the surviving
split layers are exactly
\[
 d\in\{-(2j+1),-(2j-1),2j-1,2j+1\}.                     \tag{5.1}
\]
Across both phases, deleting all other templates costs exactly
\[
 (8j-4)(b-1)=O(bj)                                      \tag{5.2}
\]
out of `2q` templates.  Therefore each individual phase loses at most
`O(bj)` templates.

For `j=o(b)`, the eight degrees (4.2) belonging to (5.1) differ from one
another by a factor `1+O(j/b)`.  Indeed every factor in (3.4) and (3.7)
is `b/2+O(j)`, the two adjacent binomial coefficients have ratio
`1+O(j/b)`, and the coordinate-choice squares in (4.1) have the same
property.

Choose the smallest of these eight degrees and independently retain an
occurrence of each type with the ratio of this minimum to its degree.
This is a nonnegative fractional mixture of coherent partial supports,
is exactly regular on all eight complete flag types, and incurs only an
additional `O(j/b)` relative loss.

Now take `j=1,3,5,...,J`, where `J` is odd.  Their type blocks (5.1) are
disjoint and partition every odd split layer
\[
                         |d|\le2J+1.                     \tag{5.3}
\]
Scaling each regularized orbit separately therefore gives an exact
nonnegative marginal fractional cover of every complete flag in (5.3).
The mean retained size of a phase support from the `j`-th orbit is
\[
                         q-O(bj).                        \tag{5.4}
\]
Taking `J=Theta(K)` realizes the affordable `O(bK)` loss scale from
Proposition 1.2 and reaches every parity layer in the exhaustive band.

The word *marginal* is essential: this cover is regular on the entire
complete flag type, not concentrated on the one flag selected by a fixed
central factor over each middle.

## 6. Uniform coordinate labelling has the wrong normalization

Let `A` be any central flag factor, so it uses at most one flag over each
middle.  Restrict attention to a band `|d|<=D<b`.  Fix a middle containing
`a` even coordinates and fix the parities of the ordered arc endpoints
`p,q`.
The four complete flag-type sizes are
\[
 \binom ba^2a^2,\quad
 \binom ba^2(b-a)^2,\quad
 \binom ba^2a(b-a),\quad
 \binom ba^2a(b-a),                                      \tag{6.1}
\]
for `(p,q)` of parity `(E,O),(O,E),(E,E),(O,O)`, respectively.
The factor contains at most `binom(b,a)^2` flags of any one type, one per
middle.  A uniformly labelled fixed parity template is uniform on its
complete type.  Its probability of hitting `A` is consequently at most
\[
 {1\over\min\{a,b-a\}^2}\le {4\over(b-D)^2}.             \tag{6.2}
\]

### Theorem 6.1 (uniform-orbit efficiency obstruction)

For every balanced parity word and either coherent phase, uniform
coordinate labelling gives
\[
 \mathbb E\,|\mathcal T\cap\mathfrak A\cap\{|d|\le D\}|
 \le {4q\over(b-D)^2}.                                   \tag{6.3}
\]
Consequently, if `D=o(b)`, every nonnegative mixture of complete
coordinate-labelled parity orbits needs support mass `Omega(R)` to give
unit load to `R` fixed-factor flags.  For `R=(1-o(1))N`, this is
`Omega(N)`, a factor `Omega(q)` above the desired `Theta(N/q)` mass.

#### Proof

Sum (6.2) over the `q` templates in one phase.  Inequality (6.3) follows.
Integrating it
over any nonnegative mixture gives total fixed-factor incidence at most
`(4+o(1))` times its support mass when `D=o(b)`.  Unit load on `R` flags
requires incidence at least `R`. \(\square\)

Thus the staircase orbit settles two questions cleanly.  There is no
parity-layer or nonnegative marginal obstruction at the mesoscopic scale,
and all degree formulas are explicit.  But uniform orbit averaging wastes
almost every flag on the complete flag universe.  The surviving Gate-C
problem is to find sufficiently many **factor-adapted**, high-overlap
labellings of these or related parity words, then round them into a
rankwise-disjoint collection and extend the retained assignments through
the full symmetric chains.

## 7. Finite audit

The companion checker
`scratch/verify_gate_c_mesoscopic_parity_staircase_20260822.py` verifies
the endpoint--deletion bijection, the staircase defect and level census,
the exact histogram (3.8), layer reach, and the labelled degree formula.
It is confirmatory; the proofs above are independent of it.
