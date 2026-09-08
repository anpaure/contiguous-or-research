# Growing-rank wreath matchings: exact local profile and a near-full balanced residual obstruction

**Status (2026-08-21).**  Everything stated as a theorem below is proved.
The note does **not** prove or disprove the approximate Baranyai--Katona
wreath factor at a rank `r~b/2`.  It proves a sharp method boundary:
even a residual family of density `1-O(b^(-1/2))` whose point degrees differ
by only `O(b^(-3/2))` relatively can contain no wreath at all.  On the same
support there is an exactly point-regular positive weighting of mass
`(1-O(b^(-1/2))) binom(b,r)`.  Consequently an iterated nibble must preserve
genuine split-profile/global mixing, not merely residual density and
one-point regularity.

The full wreath hypergraph nevertheless has excellent local parameters away
from the exceptional complementary orbit: at `b=2r+q` with `q>=3`, its
maximum normalized pair codegree is `Theta(b^(-2))`.  Thus the obstruction is
to a proposed induction invariant, not to the desired global matching.

## 1. The one-rank wreath hypergraph

Let `1<=r<=b/2`.  An oriented cyclic order

\[
 \pi=(\pi_0,\ldots,\pi_{b-1})
\]

is read modulo rotation.  Its rank-`r` wreath deck is

\[
 \mathcal W_r(\pi)=
 \bigl\{\{\pi_i,\pi_{i+1},\ldots,\pi_{i+r-1}\}:i\in\mathbb Z_b\bigr\}.
 \tag{1.1}
\]

Let `H_(b,r)` have vertex set `binom([b],r)` and one edge
`W_r(pi)` for every oriented cyclic order.  Reversal gives a parallel copy
of the same unoriented deck; retaining or identifying those copies changes
all degrees by the same factor two and does not change matchings.

Put

\[
 M={b\choose r},\qquad D=r!(b-r)!.
\]

### Proposition 1.1 (exact degree and pair profile)

The oriented multihypergraph `H_(b,r)` is `b`-uniform and `D`-regular.
If `S,T` have Johnson distance

\[
 d=|S\setminus T|=|T\setminus S|,
\]

then for `1<=d<r`,

\[
 {\operatorname{codeg}(S,T)\over D}
 ={2\over {r\choose d}{b-r\choose d}}.                 \tag{1.2}
\]

For the disjoint orbit `d=r`, write `b=2r+q`.  Then

\[
 {\operatorname{codeg}(S,T)\over D}
 ={q+1\over {r+q\choose q}}.                          \tag{1.3}
\]

In particular, at `q=1` the disjoint orbit has normalized codegree
`2/(r+1)=Theta(1/b)`.  For every `q>=3`, the distance-one orbit is dominant
for all sufficiently large `r`, and

\[
 {\Delta_2(H_(b,r))\over D}=\Theta(b^{-2}).             \tag{1.4}
\]

#### Proof

Fix `S` and rotate an order containing it so that `S` occupies positions
`1,...,r`.  Ordering `S` and its complement gives exactly
`r!(b-r)!=D` orders.

For `d<r`, the `T`-window must start `d` places clockwise or `d` places
counterclockwise from the `S`-window.  In either direction the four blocks
`S\setminus T`, `S\cap T`, `T\setminus S`, and the outside of
`S\cup T` can be
ordered in

\[
 d!\,(r-d)!\,d!\,(b-r-d)!
\]

ways.  The two directions give (1.2).

If `S,T` are disjoint, their two length-`r` blocks leave `q` outside
symbols.  There are `q+1` possible sizes of the first intervening gap.
For each size, ordering `S`, `T`, and distributing and ordering the `q`
outside symbols gives `r!^2q!` orders.  Division by
`D=r!(r+q)!` gives (1.3).  Formula (1.4) follows from (1.2)--(1.3) and
unimodality of the binomial factors.  \(\square\)

The exact `q=1` exceptional orbit is important: the middle-rank MSW theorem
already supplies an exact factor there.  The unresolved nearby odd gaps
begin at `q=3`, where (1.4) holds and a single isolated-edge bite is locally
well calibrated because `b Delta_2/D=O(1/b)`.

## 2. A two-level transversal for every wreath

Fix a nontrivial cut `A\subset[b]`, put `a=|A|`, and define

\[
 J(S)=|S\cap A|,\qquad \mu={ar\over b}.                \tag{2.1}
\]

Let

\[
 \mathcal K_A=
 \{S\in { [b]\choose r}:J(S)\in\{\lfloor\mu\rfloor,
                                      \lceil\mu\rceil\}\},
 \qquad
 \mathcal F_A={ [b]\choose r}\setminus\mathcal K_A. \tag{2.2}
\]

If `mu` is integral, the displayed two values coincide.

### Theorem 2.1 (balanced-slice transversal)

Every wreath deck meets `K_A`.  Equivalently, the induced wreath
hypergraph on `F_A` has no edge.

#### Proof

For a cyclic order `pi`, let

\[
 x_i=|\{\pi_i,\ldots,\pi_{i+r-1}\}\cap A|.
\]

Every point of `A` belongs to exactly `r` cyclic windows, so

\[
 \sum_{i\in\mathbb Z_b}x_i=ar=b\mu.                  \tag{2.3}
\]

Moreover `|x_(i+1)-x_i|<=1`, because one point leaves and one enters.
Thus `min_i x_i<=mu<=max_i x_i`, and an integer-valued cyclic nearest-step
walk joining its minimum to its maximum assumes `floor(mu)` or `ceil(mu)`.
That window lies in `K_A`.  \(\square\)

### Corollary 2.2 (a near-full wreath-free family)

Fix `eta>0` and suppose

\[
 \eta b\le a,r,b-a,b-r\le(1-\eta)b.                  \tag{2.4}
\]

Then, with a constant depending only on `eta`,

\[
 |\mathcal K_A|=O_\eta(Mb^{-1/2}),\qquad
 |\mathcal F_A|=(1-O_\eta(b^{-1/2}))M.               \tag{2.5}
\]

#### Proof

For uniform `S in binom([b],r)`, the random variable `J(S)` is
hypergeometric and

\[
 \Pr(J=j)={{a\choose j}{b-a\choose r-j}\over {b\choose r}}. \tag{2.6}
\]

Under (2.4), uniform Stirling bounds at either integer adjacent to the mean
give `Pr(J=j)=O_eta(b^(-1/2))`.  There are at most two such integers.
This proves (2.5).  \(\square\)

## 3. The residual is almost regular, and exactly regular fractionally

The preceding obstruction is substantially stronger than a density-only
example.

### Theorem 3.1 (unweighted near-regularity)

Under (2.4), all point degrees in the induced vertex family `F_A` equal

\[
 {r|\mathcal F_A|\over b}+O_\eta(Mb^{-3/2}).          \tag{3.1}
\]

Since the main term is `Theta_eta(M)`, the relative point-degree variation
is `O_eta(b^(-3/2))`, although `F_A` contains no wreath.

#### Proof

Write `K=|K_A|` and

\[
 L_j={a\choose j}{b-a\choose r-j}.
\]

By symmetry within the two shores, the degree of a point of `A` in `K_A`
and that of a point outside `A` are respectively

\[
 k_A={1\over a}\sum_{j\in I}jL_j,
 \qquad
 k_B={1\over b-a}\sum_{j\in I}(r-j)L_j,              \tag{3.2}
\]

where `I={floor(mu),ceil(mu)}`.  Therefore

\[
 |k_A-k_B|
 ={b\over a(b-a)}\left|\sum_{j\in I}(j-\mu)L_j\right|
 \le {bK\over a(b-a)}=O_\eta(K/b).                   \tag{3.3}
\]

The full rank layer is point-regular.  Subtract (3.2), use (2.5), and note
that the average residual point degree is `r|F_A|/b`.  Equations
(3.2)--(3.3) give (3.1).  \(\square\)

There is also an exact weighted statement.  It is deliberately labelled
weighted: it is not an exact unweighted residual reachable from a wreath
matching.

### Theorem 3.2 (exact point-regular positive weighting)

For all sufficiently large `b` under (2.4), there are weights

\[
 y_S=1+O_\eta(b^{-1/2})>0\qquad(S\in\mathcal F_A)     \tag{3.4}
\]

such that every ground point has exactly the same weighted load and

\[
 \sum_{S\in\mathcal F_A}y_S
 =(1-O_\eta(b^{-1/2}))M.                              \tag{3.5}
\]

The support of this exactly point-regular measure is wreath-free.

#### Proof

Put `z_S=J(S)-mu` and

\[
 A_1=\sum_{S\in\mathcal F_A}z_S,
 \qquad
 A_2=\sum_{S\in\mathcal F_A}z_S^2,
 \qquad
 \lambda=-{A_1\over A_2},
 \qquad
 y_S=1+\lambda z_S.                                  \tag{3.6}
\]

The full-layer sum of `z_S` is zero, while `|z_S|<=1` on `K_A`; hence
`|A_1|<=K=O_eta(M/sqrt(b))`.  The exact hypergeometric variance is

\[
 \operatorname{Var}J
 =r{a\over b}\left(1-{a\over b}\right){b-r\over b-1}
 =\Theta_\eta(b).                                    \tag{3.7}
\]

Removing the two central levels changes the full sum of squares by at most
`K`, so `A_2=Theta_eta(Mb)`.  Consequently

\[
 |\lambda|=O_\eta(b^{-3/2}),\qquad
 |\lambda z_S|=O_\eta(b^{-1/2}),                     \tag{3.8}
\]

which proves positivity for large `b`.

By construction,

\[
 \sum_{S\in\mathcal F_A}y_S(J(S)-\mu)=A_1+\lambda A_2=0. \tag{3.9}
\]

Symmetry inside `A` and its complement turns (3.9) exactly into equality
of their per-point weighted loads.  Thus all `b` point loads agree.  Finally,

\[
 \sum_Sy_S=|\mathcal F_A|-{A_1^2\over A_2}
 =(1-O_\eta(b^{-1/2}))M,                              \tag{3.10}
\]

and Theorem 2.1 says that its support contains no wreath.  \(\square\)

## 4. Why the published black boxes reviewed here do not close the premise

This section records scope, not a claim that no future or unreviewed theorem
could apply.

1. **Pippenger and Alon--Kim--Spencer are fixed-uniformity statements.**
   The Alon--Kim--Spencer theorem explicitly begins “for every fixed `k`”.
   Moreover it is a simple-hypergraph theorem.  A bounded-codegree reduction
   here necessarily loses the factorial degree: if a spanning subhypergraph
   `G\subset H_(b,r)` has maximum pair codegree `C`, then for every `S`,

   \[
    2\deg_G(S)
    =\sum_{T:\,|S\setminus T|=1}\operatorname{codeg}_G(S,T)
    \le r(b-r)C.                                     \tag{4.1}
   \]

   Each retained wreath through `S` contributes exactly its two adjacent
   windows to the left side.  Thus a simple reduction has degree only
   `O(b^2)`.  Even formally inserting that degree into the fixed-`b` AKS
   leave `N D^(-1/(b-1))` gives a factor
   `(O(b^2))^(-1/(b-1))=1-o(1)`, not an `o(N)` leave.

2. **The explicit pseudorandom-matching theorem of Ehard--Glock--Joos is
   quantitatively nonuniform here.**  Its Theorem 1.2 sets
   `epsilon=delta/(50k^2)` and requires both
   `Delta_c<=Delta^(1-delta)` and
   `e(H)<=exp(Delta^(epsilon^2))`.  Since
   `Delta_c/Delta=Theta(b^(-2))`, the largest admissible `delta` is
   `Theta(1/b)`.  With `k=b`, one has `epsilon=Theta(b^(-3))` and
   `Delta^(epsilon^2)=1+o(1)`, whereas after identifying reversal copies the
   simple unoriented wreath hypergraph still has `(b-1)!/2` edges.  The
   displayed edge-count hypothesis fails by a factorial margin.

3. **The growing-codegree theorem of Gould--Kelly remains fixed-rank.**
   Its hierarchy is
   `1/D << 1/A << gamma << 1/k <=1`.  For the present `q>=3` profile its
   parameter `B` is at most
   `sqrt(D/Delta_2)=Theta(b)`, and its leave is

   \[
    N B^{-1+\gamma}\log^A D.                          \tag{4.2}
   \]

   Here `log D=Theta(b log b)`, so the displayed formal bound is already
   vacuous for the required fixed-hierarchy `A>1`; the theorem does not
   supply a diagonal growing-`b` conclusion.

Primary sources checked:

- N. Alon, J.-H. Kim, J. Spencer,
  *Nearly perfect matchings in regular simple hypergraphs*, Israel J. Math.
  100 (1997), 171--187,
  <https://web.math.princeton.edu/~nalon/PDFS/aks7.pdf>.
- S. Ehard, S. Glock, F. Joos,
  *Pseudorandom hypergraph matchings*, Combin. Probab. Comput. 29 (2020),
  868--885, <https://arxiv.org/abs/1907.09946>.
- S. Gould, T. Kelly,
  *Advancing the Rödl Nibble: New bounds on matchings and the list chromatic
  index of hypergraphs*, arXiv:2511.11375 (2025),
  <https://arxiv.org/abs/2511.11375>.

## 5. Exact conclusion for the research program

For the nearby odd gaps `q>=3`, the factorial-degree wreath hypergraph has
the right first-bite scale, and no obstruction to a global approximate
factor has been found here.  What Theorems 2.1 and 3.1--3.2 rule out is the
following induction:

> “The residual is still dense and (almost, or fractionally exactly)
> one-point regular, therefore it contains another wreath.”

That implication is false even at residual density `1-O(b^(-1/2))`.
A successful direct proof must retain at least one stronger invariant that
detects the balanced-slice transversal--for example uniform control of
split profiles `|S\cap A|` over a sufficiently rich family of cuts,
or an equivalent high-order mixing statement.  Proving such preservation
down to any residual density `o(1)` would still establish the desired
approximate one-rank factor and, by complementation, the paired endpoint
input.  That positive theorem remains open.

## 6. Reproducibility

The exhaustive checker
`scratch/audit_growing_rank_wreath_balanced_slice_obstruction_20260821.py`
verifies (1.2)--(1.3), the transversal property, and exact weighted point
balance for every tested odd `b<=9`.  It was run only on H100.  Frozen H100
hashes are recorded when this note is copied for audit.
