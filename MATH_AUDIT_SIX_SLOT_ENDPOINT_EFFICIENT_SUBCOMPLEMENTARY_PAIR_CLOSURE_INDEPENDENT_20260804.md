# Independent audit: six-slot endpoint-efficient subcomplementary-pair closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The theorem closes exactly the genuine
size-six-efficient branch after the stated proof-safe normalizations.  The
train inequalities, reflection direction, pair split, endpoint-period
comparison, least-maximizer use, and final strict margin all check.

No theorem byte was edited during this audit.

## 1. Exact binding and dependencies

Audited theorem:

`MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md`

SHA-256:

`4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0`

Every frozen dependency hash matches the current workspace:

| role | SHA-256 |
|---|---|
| least-critical endpoint normalization | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complementary-pair train estimates | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| short-train ceiling/upper estimates | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| independent current-byte short-train audit | `c0427eb680265563ffb85448a0a538d89a63c6421d668a847d9d09f05e6e3760` |

Their scopes supply exactly the ingredients used here:

\[
 C>{43\over1000},
 \qquad F(w)>{57\over1400}\quad(0\le w\le A/4),
\]

\[
 F(w)<{61\over1000}\quad(0\le w\le2A/5),
 \qquad F(w)>0\quad(0\le w\le A/2),
\]

\[
 F(w)+F(A-w)>-{1\over20000},
\]

and nonincreasing behaviour of `F` on `[A/4,A/2]`.  The endpoint
normalization theorem applies after saturation when size six is the least
maximum-density denomination.

## 2. Extension of the upper train bound

The theorem extends the strict estimate

\[
 F(w)<{61\over1000}\qquad(0\le w\le2A/5)
\]

to the full half band.  For `2A/5<=w<=A/2`, nonincreasing behaviour gives

\[
 F(w)\le F(2A/5)<{61\over1000}.
\]

Thus the extended bound remains strict even though the monotonic comparison
itself is weak.  The direction is correct: moving right cannot increase
`F` on this interval.

## 3. Subcomplementary-pair lemma

Assume

\[
 0\le y\le z,
 \qquad y+z\le A.
\]

If `z<=A/2`, both terms are strictly positive, which is stronger than the
claimed negative lower bound.

If `z>A/2`, put `v=A-z`.  Then

\[
 0\le y\le v<A/2.
\]

Reflection is used in the proof-safe direction:

\[
 F(v)+F(z)>-\varepsilon
 \quad\Longrightarrow\quad
 F(y)+F(z)>F(y)-F(v)-\varepsilon.
\]

There are two exhaustive cases.

1. If `y>=A/4`, then `A/4<=y<=v<A/2`.  Since `F` is nonincreasing,
   `F(y)>=F(v)`, so the pair is greater than `-epsilon`.
2. If `y<A/4`, the small-shift lower bound and the extended half-band upper
   bound give

   \[
   \begin{aligned}
   F(y)+F(z)
   &>{57\over1400}-{61\over1000}-{1\over20000}\\
   &=-{8541\over420000}.
   \end{aligned}
   \]

Finally,

\[
 {1\over20000}={21\over420000}
 <{8541\over420000},
\]

so the first case also satisfies the displayed uniform bound.  Boundary
values `y=0`, `y=A/4`, `z=A/2`, and `y+z=A` are all covered with the stated
strictness.

## 4. Normalization and endpoint-period comparison

The normalizations occur in the required order: first crossing, endpoint
saturation, then least-maximizer assignment.  If size six is the least
maximum-density size, no lower denomination ties its density, so the
least-critical endpoint theorem gives

\[
 c_6=A.
\]

The endpoint-period lower bound is literal.  For every `q>=0` and
`0<=i<=5`, the configuration consisting of `q` endpoint generators and
one size-`i` generator gives

\[
 V_{6q+i}\ge qA+c_i.
\]

At `q=0`, internal superadditivity makes the single size-`i` generator
optimal, so `V_i=c_i`.  For `q>=1`, both sides lie in `[A,infinity)`,
where `K` is increasing.  Hence summing over all six residue classes gives

\[
 \Phi(c)\ge C+\sum_{i=1}^5F(c_i).
\]

No eventual-period equality is assumed.

The standard Bellman-table hypotheses include nonnegativity.  Moreover,
internal superadditivity itself gives

\[
 c_{i+1}\ge c_i+c_1\ge c_i,
\]

so the needed ordering

\[
 c_1\le c_5,
 \qquad c_2\le c_4
\]

is available.  Endpoint superadditivity gives

\[
 c_1+c_5\le A,
 \qquad c_2+c_4\le A,
 \qquad 2c_3\le A.
\]

Thus the pair lemma applies to both `(c_1,c_5)` and `(c_2,c_4)`, while
`0<=c_3<=A/2` gives `F(c_3)>0`.

## 5. Exact strict margin and scope

Combining the literal endpoint lower bound, the two strict pair bounds,
the strict ceiling bound, and `F(c_3)>0` gives

\[
\begin{aligned}
 \Phi(c)
 &>{43\over1000}-2{8541\over420000}\\
 &= {9030-8541\over210000}\\
 &= {489\over210000}
  ={163\over70000}>0.
\end{aligned}
\]

The arithmetic and inequality strictness are correct.

The theorem concludes only that a normalized nonpositive six-slot table
cannot belong to the genuine size-six-efficient branch.  Least-maximizer
sizes `2,3,4,5`, the complete six-slot theorem, the all-grid Bellman
inequality, and every OR-word upper bound remain outside its scope.

Markdown display delimiters, equation tags, lists, and inequality symbols
are balanced and well formed.
