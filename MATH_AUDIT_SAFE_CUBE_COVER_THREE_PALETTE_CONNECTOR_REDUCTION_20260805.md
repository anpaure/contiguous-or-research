# Audit and reduction: combining the safe cube cover with a three-palette collar bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no finite computation, enumeration, or solver  
**Inputs:**

* `MATH_THEOREM_CATALAN_MATROID_ALIGNED_CUBE_SAFE_PATH_COVER_20260805.md`;
* `MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`,
  audited at SHA-256
  `805504df0360ce3cce7565ab41f04e2cc7d99e0ca057e20d7dea0a3cad9740e2`;
* `MATH_THEOREM_CATALAN_SCALE_PIVOT_TRACE_FACTOR_GLUING_20260805.md`;
* `MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`.

## 0. Verdict

The three-palette bank theorem is **GO in its stated prospective scope**.
Its residual-edge estimate, dense-core collar construction, palette
disjointness, exact Catalan thinning, and low-star union bound are valid.

It cannot yet be overlaid on the aligned-cube MSW path cover.  The two
theorems have opposite quantifier orders:

* the cube theorem first fixes canonical MSW paths, signs, and seam
  endpoints;
* the bank theorem first chooses arbitrary Johnson collars, with no promise
  that they are canonical MSW subpaths or expose the selected break states.

The resource arithmetic is nevertheless favourable.  If the cube cover
has `t=O((h/r)Cat_r)` paths, then the `t-1` hard cross-cover connectors use
only

\[
 O\!\left({h^2\over r}\operatorname {Cat}_r\right)
 =O(\operatorname {Cat}_r)                           \tag{0.1}
\]

owner, lower-`q1`, and upper-`q1` resources at deadline depth.  Even an
`O(h^2)` complete lower-damage ledger per connector has total scalar cost

\[
 O\!\left({h^3\over r}\operatorname {Cat}_r\right)
 =O(\sqrt r\operatorname {Cat}_r)=o(W).              \tag{0.2}
\]

Thus one extra lower row has ample **scalar** capacity.  The remaining gate
is one literal, rainbow connector selection, not a count.

## 1. Audit of the three-palette bank

Put `q=k-r in {r,r-1}` and `Delta=rq`.  One collar uses `s+2` owners,
`s+1` distinct lower colours, and `s` distinct upper colours.  After `t`
collars, deleting every used owner and every edge carrying a used lower or
upper colour loses at most

\[
 t(s+2)\Delta
 +t(s+1){q+1\choose2}
 +ts{r+1\choose2}.                                  \tag{1.1}
\]

For `t<W/(64s)`, division by `W Delta/2` gives exactly the three ratios in
the source theorem.  Their sum is below `1/2` under `r>=16s`.  Peeling
vertices below degree `Delta/4` therefore leaves a nonempty dense core.

Inside that core, each intermediate owner has degree at least `rq/4`.
At step `j`, excluding removal of an inserted rho label and insertion of a
deleted lambda label costs at most `(j-1)(r+q)` edges.  The hypothesis

\[
 {rq\over4}>h(r+q)                                   \tag{1.2}
\]

leaves an allowed exchange.  The first entering-label fibre contains at
least `r/4` possible deleted labels, so after `h` stem deletions one remains
in the core for the repeated left seam.  The identical exclusion at the
right endpoint supplies a fresh exit.  The displayed owner, lower, and
upper palettes are then pairwise disjoint with exactly the declared one
upper repetition.

Iteration gives `M=floor(W/(64s))` mutually three-palette-disjoint collars.
Uniformly selecting exactly the Catalan number `b` of blocks and applying
the weighted without-replacement Bernstein bound gives

\[
 \Pr\{|V_B\cap O(S)|>2p|O(S)|\}
 \le\exp\!\left(-{3p|O(S)|\over8(s+2)}\right).       \tag{1.3}
\]

The smallest relevant star has size

\[
 {k-r+h+1\choose h+1},                              \tag{1.4}
\]

whose logarithm is `Theta(sqrt(r) log r)`, whereas there are at most
`2^k` tests.  Since `p/(s+2)>=16/D_k`, the exponent in (1.3) dominates
`O(r)`.  The simultaneous star-spread conclusion follows.

No reversed inequality or missing palette class was found.  The theorem is
therefore proof-safe as an abstract bank theorem.

## 2. Connector resource arithmetic

Specialize to the even MSW half with

\[
 C=\operatorname {Cat}_r,
 \qquad W={2r\choose r}=(r+1)C.                     \tag{2.1}
\]

The bi-core aligned-cube theorem gives a path cover with

\[
 t\le L_r+2^{-M/16}C+{32h\over M}C,
 \qquad M=\lfloor r/2\rfloor,                       \tag{2.2}
\]

where the first two terms are `o(C)`.  In particular,

\[
 t\le(64+o(1)){h\over r}C+o(C).                    \tag{2.3}
\]

One generalized collar uses

\[
 h+3\text{ owners},\qquad
 h+2\text{ lower-}q1\text{ colours},\qquad
 h+1\text{ distinct upper-}q1\text{ colours}.       \tag{2.4}
\]

Therefore `t-1` cross-cover connectors use at most

\[
 t(h+3)
 \le(64+o(1)){h(h+3)\over r}C+o(hC)                \tag{2.5}
\]

owners, with smaller analogous bounds for both immediate palettes.

At deadline depth,

\[
 {h^2\over r}\longrightarrow {\pi\over4},           \tag{2.6}
\]

up to the harmless convention shift between `h=d+1` and `s=h+1`.
Consequently (2.5) is at most `(16\pi+o(1))C`, plus the negligible terms.
Relative to the owner layer this is `O(1/r)`:

\[
 {t(h+3)\over W}=O(1/r).                            \tag{2.7}
\]

Since `t<C` eventually, any already constructed `C-1` collar bank contains
enough mutually disjoint collars numerically.  Taking a subfamily preserves
all three disjointness properties and only improves the star-spread bound.

## 3. The `B+1` scalar lower-row ledger

At length `W+e`, the number of intervals of lengths at most `e` is

\[
 eW+{e+1\choose2}.                                  \tag{3.1}
\]

Raising the excess from the lower-bound depth `d` to `d+1` creates exactly

\[
 \left((d+1)W+{d+2\choose2}\right)
 -\left(dW+{d+1\choose2}\right)
 =W+d+1                                               \tag{3.2}
\]

new short addresses.

The two pivot rays plus singleton contribute only `2h-1` named local lower
tasks per connector.  Equations (2.3) and (2.6) give

\[
 t(2h-1)=O\!\left({h^2\over r}C\right)=O(C)=o(W).
                                                               \tag{3.3}
\]

Even if a conservative complete-damage interface costs

\[
 f(h)\le Ah^2+Bh+D                                  \tag{3.4}
\]

named tasks per connector, then

\[
 tf(h)=O\!\left({h^3\over r}C\right)
       =O(\sqrt r\,C)=o(W).                         \tag{3.5}
\]

Thus (3.2) has ample scalar room for every connector flag in either ledger.

This is **not** an incidence theorem.  The extra addresses must still be
matched to the named targets under containment, trace order, occurrence,
and common-cap restrictions.  Equations (3.3)--(3.5) rule out only an
aggregate shortage.

## 4. Zero extra length and the position caveat

The pivot bridge gluing theorem is genuinely zero-length only under its
owner-partition premise.  Bridge owners replace owners omitted from the
trace components; they are not appended on top of an already complete
owner chronology.

Accordingly, (2.5) proves that the hard connector bank is small enough to
be **reserved** inside the owner layer.  It does not authorize inserting
`t` new source positions.  If each connector required a new unbudgeted
letter, the physical overhead would be `t`, and no `B+1` conclusion would
follow.

## 5. Exact connector object

Let the safe cube cover have directed path components

\[
 \mathcal P_1,\ldots,\mathcal P_t,
\]

with signed terminal and initial states `out_i,in_i`.  Let `mathcal B` be a
three-palette-disjoint reserved collar bank.  Form the coloured connector
digraph `Gamma` on `[t]` by placing a collar-coloured arc

\[
 i\overset{B}{\longrightarrow}j                    \tag{5.1}
\]

when all of the following literal conditions hold simultaneously:

1. the initial rail of `B` equals `out_i` and its terminal rail equals
   `in_j` in ordered source letters;
2. its two endpoint owners are the required signed MSW endpoints;
3. its owner, lower-`q1`, and upper-`q1` resources are available in the
   punctured factor;
4. its boundary letter and both seam coordinates satisfy residence;
5. its named lower flags have legal literal addresses in the same
   common-cap state.

### Conditional owner/`q1` completion theorem

If `Gamma` has a directed Hamilton path whose `t-1` arcs have distinct
collar colours, and the complementary owner set has a punctured ordered
four-transversal linear forest whose edge intersections and unions
bijectively supply the remaining lower- and upper-`q1` palettes, then the
safe cube paths and those collars glue at zero extra owner length into one
owner chronology with exact immediate palettes.  The only remaining lower
cost is the literal deficiency of the deeper flag-address matching.

#### Proof

Order the cube paths along the rainbow Hamilton path in `Gamma`.  The rail
equalities permit literal concatenation.  Distinct collar colours and the
bank theorem give disjoint owner and immediate-palette resources.  The
owner partition means the bridge windows replace the punctured owners, so
the total number of owner arcs remains `W`.  The punctured ordered
four-transversal supplies both complementary immediate palettes, while
every collar has the sharp one-repeat upper ledger.  Hence the exact gluing
and upper-capacity theorems apply. `square`

The connector object is equivalently a matching in the tripartite set

\[
 \{\text{path outputs}\}\times
 \{\text{path inputs}\}\times
 \{\text{collars}\},                                \tag{5.2}
\]

together with partition constraints on inputs/outputs and a graphic
connectedness constraint on the path components.  It is not implied by
three separate Hall matchings.

## 6. The exact quantifier gap

The three-palette theorem does not establish an arc of `Gamma`.

1. Its collars are arbitrary Johnson geodesics, not initial segments of
   the canonical MSW paths selected by the cube cover.
2. Its repeated-left-upper specialization need not have a Dyck or
   anti-Dyck predecessor endpoint.  The free-repeat endpoint theorem was
   introduced precisely because this specialization has primitive
   obstructions.
3. The bank is chosen independently of the punctured ordered-four-
   transversal and the literal trace factor.
4. Low-star spread preserves many potential containment hosts, but does
   not prove ordered rail equality, endpoint compatibility, or a rainbow
   Hamilton path on the `t` cover components.

Therefore the honest combined status is

\[
 \boxed{
 \begin{gathered}
 \text{safe path cover}+\text{three-palette bank}
 \text{ is scalar-feasible at }B+1,\\
 \text{but the rainbow literal connector digraph }\Gamma
 \text{ remains unproved.}
 \end{gathered}}
\]

The next useful theorem is a **correlated connector lemma**: choose the
cube-cycle breaks and the collar bank jointly so that `Gamma` has a rainbow
Hamilton path while the punctured upper-exact forest and lower flag
matching remain feasible.
