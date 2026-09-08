# Mersenne Kneser Hamilton angles and the all-parameter approximate depth-one factor

Date: 2026-07-26

Scope: successor to
`MATH_THEOREM_COMPLEMENT_INVARIANT_MIDDLE_LEVELS_KNESER_QUOTIENT_AND_Q1_COUNTEREXAMPLE_20260726.md`.
All arguments are purely combinatorial.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom nm,
 \qquad
 B=\frac Wn=\operatorname {Cat}_m,                           \tag{0.1}
\]

and

\[
 N=\binom n{m-1}=\frac m{m+2}W,
 \qquad
 r=W-N=\frac{2W}{m+2}.                                      \tag{0.2}
\]

For a Hamilton cycle

\[
 A_0,A_1,\ldots,A_{W-1},A_0                                 \tag{0.3}
\]

of `KG(n,m)`, its angle, or length-two overlap, at `A_j` is

\[
                              C_j=A_{j-1}\cap A_{j+1}.        \tag{0.4}
\]

The cardinality-optimal lower ledger asks that every member of
`\binom{[n]}{m-1}` occur once or twice among the `C_j`.  Exactly `r` of
them must occur twice.

The present audit gives four exact conclusions.

1. There is an exact omitted-label normal form.  If

   \[
                g_j=[n]\setminus(A_j\cup A_{j+1}),           \tag{0.5}
   \]

   then

   \[
   A_{j+2}=A_j-g_{j+1}+g_j,
   \qquad
   C_j=A_j^c\setminus\{g_{j-1},g_j\}.                       \tag{0.6}
   \]

2. An optimal ledger forces the gap word to be perfectly balanced:

   \[
                  \#\{j:g_j=x\}=B
                  \qquad(x\in[n]).                          \tag{0.7}
   \]

   It also forces the doubled lower colours to form an explicitly
   point-regular, pair-constrained design.  These conditions are derived in
   Sections 3--4.
3. For Mersenne `m=2^a-1`, all parity, divisibility, and aggregate
   point/pair counts in this normal form are compatible.  Thus there is no
   obstruction at those numerical levels.  Realizing every individual
   pair equation together with Hamiltonicity remains part of the unproved
   balanced-Hamilton construction.
4. There is, however, a genuine infinite obstruction to the most natural
   algebraic specialization.  If `a` is odd, no Hamilton cycle invariant
   under a regular cyclic permutation of the `n` coordinates can have the
   optimal ledger.  Order-three lower-set stabilizers force some angle
   loads to be divisible by three.  Any successful construction for those
   Mersenne parameters must break that coordinate-cyclic symmetry.

The non-Mersenne approximate application is unconditional and stronger
than a Hamilton-path heuristic.  For every `m>=2`, the canonical PBBS
cycle factor of `KG(n,m)` projects to a spanning Johnson `2`-factor with:

\[
\begin{array}{ll}
\text{all rank-}(m+1)\text{ union colours}&\text{exactly once},\\
\text{all rank-}(m-1)\text{ intersection colours}&\text{at least once},\\
\text{every lower load}&\text{at most three},\\
\#\{S:\mu(S)\notin\{1,2\}\}&\le W/(m+2),\\
\text{number of Johnson components}&\le 2B=2W/(2m+1).
\end{array}                                                  \tag{0.8}
\]

Thus the quotient method already gives an exact-owner, coefficient-one
depth-one pseudofactor for non-Mersenne dimensions, with only `O(W/m)`
component and load error.  What fails outside the Mersenne dimensions is
only the lift to one plain-complement-invariant Middle Levels Hamilton
cycle.  It is not a depth-one factor obstruction.

## 1. The centered projection of an arbitrary Kneser factor

The Hamilton assumption is unnecessary for the local projection.  Let
`F` be any spanning `2`-factor of `KG(n,m)`.  At each vertex `X`, denote
its two `F`-neighbours by `Y_F(X)` and `Z_F(X)`, and insert the Johnson edge

\[
                     e_X=Y_F(X)Z_F(X).                       \tag{1.1}
\]

Both endpoints are distinct `m`-subsets of the `(m+1)`-set `X^c`.
Therefore

\[
 Y_F(X)\cup Z_F(X)=X^c,
 \qquad
 \chi_F(X):=Y_F(X)\cap Z_F(X)\in\binom{[n]}{m-1}.           \tag{1.2}
\]

### Proposition 1.1 (centered-factor projection)

The graph

\[
                         P(F)=\{e_X:X\in\tbinom{[n]}m\}      \tag{1.3}
\]

is a spanning `2`-factor of `J(n,m)`.  Its union-colour map is the
bijection

\[
                              e_X\longmapsto X^c,             \tag{1.4}
\]

and its intersection-colour multiset is exactly

\[
                              \{\chi_F(X):X\in\tbinom{[n]}m\}.
                                                                    \tag{1.5}
\]

If a component of `F` has length `L`, its image under (1.3) has
`gcd(2,L)` components, each of length `L/gcd(2,L)`.

#### Proof

A vertex `Y` has two neighbours `X,Z` in `F`.  It occurs in precisely the
two centered edges `e_X` and `e_Z`, so its degree in `P(F)` is two.  The
center of a Johnson edge is unique: if `Y,Z` are adjacent in `J(n,m)`, the
only `m`-set disjoint from both is `(Y\cup Z)^c`.  Hence the edges `e_X`
are distinct and `P(F)` is a simple spanning `2`-factor.  Identities
(1.4)--(1.5) are (1.2).

On an `F`-cycle indexed by `\mathbb Z_L`, (1.3) joins `j-1` to `j+1`.
This is the step-two graph on `\mathbb Z_L`, which has `gcd(2,L)` cycles
of the stated length. `\square`

For a quotient Hamilton cycle, Proposition 1.1 gives one Johnson Hamilton
cycle when `W` is odd, and two Johnson cycles of length `W/2` when `W` is
even.  The latter is the correct non-Mersenne chronology.  The failure of
the alternating Middle Levels lift to close as one cycle does not destroy
the centered Johnson factor.

## 2. Gap-word normal form

Return to the Hamilton cycle (0.3).  Since consecutive `m`-sets are
disjoint in a ground set of size `2m+1`, (0.5) is a singleton.  We identify
it with its element.

### Lemma 2.1 (exact recurrence and angle formula)

For every cyclic index `j`,

\[
 A_{j+1}=A_j^c\setminus\{g_j\},                              \tag{2.1}
\]

\[
 A_{j+2}=A_j-\{g_{j+1}\}+\{g_j\},                           \tag{2.2}
\]

and

\[
 C_j=A_j^c\setminus\{g_{j-1},g_j\}.                         \tag{2.3}
\]

Moreover `g_{j-1}\ne g_j`; the two-step Johnson edge
`A_{j-1}A_{j+1}` swaps precisely the coordinate pair
`{g_{j-1},g_j}`.

#### Proof

Equation (2.1) is the definition of the unique coordinate outside
`A_j\cup A_{j+1}`.  Complementing (2.1) and applying it once more gives

\[
 A_{j+2}=(A_j\cup\{g_j\})\setminus\{g_{j+1}\}.              \tag{2.4}
\]

If `g_{j+1}=g_j`, then `A_{j+2}=A_j`, impossible in a Hamilton cycle.
Thus `g_{j+1}\in A_j`, and (2.2) follows.  Both `A_{j-1}` and `A_{j+1}`
are obtained from `A_j^c` by deleting, respectively, `g_{j-1}` and
`g_j`; their intersection is (2.3). `\square`

### Lemma 2.2 (gap parity)

Let

\[
                              t_x=\#\{j:g_j=x\}.              \tag{2.5}
\]

Then

\[
                              t_x\equiv W\pmod2              \tag{2.6}
\]

for every coordinate `x`.  More locally, the cyclic distance between any
two successive occurrences of `x` in the gap word is odd.

#### Proof

Across an edge whose gap is not `x`, exactly one endpoint contains `x`, so
membership of `x` toggles.  Across an edge labelled `x`, both endpoints
omit `x`, so it does not toggle.  Returning to the initial incidence bit
after `W` edges gives `W-t_x` even, proving (2.6).

Immediately after an `x`-labelled edge the incidence bit is zero.  Before
the next `x`-labelled edge it must again be zero.  The intervening
non-`x` edges therefore number evenly, so the distance between the two
label positions is odd. `\square`

For a Mersenne parameter, both `W=nB` and `B` are odd.  Thus the uniform
target `t_x=B` is exactly compatible with (2.6), rather than being
parity-obstructed.

### Lemma 2.3 (converse gap-word criterion)

Let `q_0,...,q_{L-1}` be a cyclic word in which every ground coordinate
occurs and successive occurrences of each coordinate have odd cyclic
separation.  Then there is a unique cyclic set sequence `A_0,...,A_{L-1}`
satisfying

\[
 A_{j+1}=A_j^c\setminus\{q_j\}.                              \tag{2.7}
\]

If `L` is odd, all the `A_j` have size `m`, so this is a closed walk in
`KG(2m+1,m)`.  It is a Hamilton cycle precisely when `L=W` and the `A_j`
are distinct.

#### Proof

Fix a coordinate `x`.  At every edge position labelled `x`, prescribe
that `x` is absent from both incident sets.  Between two successive
`x`-positions, toggle its incidence across every intervening edge.  The
number of intervening edges is even by the odd-separation hypothesis, so
the incidence returns to zero before the next `x`-position.  This defines
the incidence of `x` consistently and uniquely around the cycle.  Doing
this for every coordinate gives (2.7).

Let `s_j=|A_j|`.  Equation (2.7) gives

\[
                              s_{j+1}=2m-s_j.                 \tag{2.8}
\]

When `L` is odd, cyclic closure forces `s_j=m` for every `j`.  Consecutive
sets are therefore disjoint `m`-sets, with `q_j` as their unique omitted
coordinate.  The final assertion is now immediate. `\square`

## 3. Forced point design of the doubled lower colours

Suppose now that the angle loads are cardinality-optimal:

\[
                              \mu(S)\in\{1,2\}               \tag{3.1}
\]

for every `S\in\binom{[n]}{m-1}`.  Define the doubled family

\[
                              \mathcal D=\{S:\mu(S)=2\}.      \tag{3.2}
\]

Counting occurrences gives

\[
                              |\mathcal D|=r.                 \tag{3.3}
\]

### Theorem 3.1 (point regularity)

Every coordinate belongs to exactly

\[
                        d=\frac{2(m-1)B}{m+2}                \tag{3.4}
\]

members of `\mathcal D`.

#### Proof

For one Johnson edge with endpoints `P,Q`, lower colour `L=P\cap Q`, and
upper colour `U=P\cup Q`, one has pointwise

\[
 \mathbf1_{x\in P}+\mathbf1_{x\in Q}
 =\mathbf1_{x\in L}+\mathbf1_{x\in U}.                      \tag{3.5}
\]

Sum over the centered Johnson `2`-factor.  Every middle owner has degree
two and every upper colour occurs once, so the lower occurrence degree at
`x` is

\[
 2\binom{2m}{m-1}-\binom{2m}{m}
 =(m-1)B.                                                     \tag{3.6}
\]

One copy of the complete lower layer contributes

\[
 \binom{2m}{m-2}=\frac{m(m-1)}{m+2}B                         \tag{3.7}
\]

at `x`.  The difference between (3.6) and (3.7) is (3.4).
`\square`

Thus an arbitrary choice of the `r` doubled colours is impossible.  It
must be an `(m-1)`-uniform regular family.  The divisibility in (3.4) is
automatic because the right side is also the integer difference
(3.6)-(3.7).

## 4. Forced pair design and uniform gap use

For an unordered coordinate pair `T={x,y}`, let

\[
 s_T=\#\{j:\{g_{j-1},g_j\}=T\}.                              \tag{4.1}
\]

This is the multiplicity of `T` as a two-step swap pair.  Let
`d_{\mathcal D}(T)` be the number of members of `\mathcal D` containing
`T`.

### Theorem 4.1 (exact pair equation)

For every coordinate pair `T`,

\[
 \boxed{
 d_{\mathcal D}(T)=\kappa_m+s_T,
 \qquad
 \kappa_m=\frac{(m-4)B}{m+2}.
 }                                                           \tag{4.2}
\]

Consequently the transition-pair multigraph `(s_T)` is `2B`-regular and

\[
 \boxed{t_x=B\qquad(x\in[n]).}                               \tag{4.3}
\]

#### Proof

On a Johnson edge, the endpoint-containment identity for a pair `T` is

\[
 \mathbf1_{T\subseteq P}+\mathbf1_{T\subseteq Q}
 =\mathbf1_{T\subseteq L}+\mathbf1_{T\subseteq U}
  -\mathbf1_{T=U\setminus L}.                               \tag{4.4}
\]

Summing and using the complete owner and upper ledgers gives

\[
 d_L(T)
 =2\binom{2m-1}{m-2}-\binom{2m-1}{m-1}+s_T.                 \tag{4.5}
\]

Under (3.1), the left side is

\[
 d_L(T)=\binom{2m-1}{m-3}+d_{\mathcal D}(T).                 \tag{4.6}
\]

Subtracting (4.6) from (4.5) and simplifying gives

\[
 2\binom{2m-1}{m-2}
 -\binom{2m-1}{m-1}
 -\binom{2m-1}{m-3}
 =\frac{(m-4)B}{m+2},                                       \tag{4.7}
\]

which proves (4.2).

Now sum (4.2) over all pairs `T` containing a fixed `x`.  The left side is
`(m-2)d`, while the constant term contributes `2m\kappa_m`.  Hence

\[
 \sum_{y\ne x}s_{\{x,y\}}
 =(m-2)d-2m\kappa_m
 =2B.                                                        \tag{4.8}
\]

In the cyclic gap word, every occurrence of `x` is incident with the two
adjacent transition pairs.  Lemma 2.1 excludes equal adjacent labels, so
the left side of (4.8) is `2t_x`.  This proves (4.3). `\square`

For `m>=5`, (4.2) contains the nonnegative pair floor

\[
                    d_{\mathcal D}(T)\ge\kappa_m.            \tag{4.9}
\]

For `m=3`, `\kappa_3=-1`; the optimal certificate in the predecessor note
indeed has `s_T=1` or `2` and `d_{\mathcal D}(T)=s_T-1`.

The cyclic gap word is an Euler circuit of the loopless multigraph with
edge multiplicities `s_T`: its consecutive symbols are exactly the edges
counted in (4.1).  Thus an optimal construction must choose a doubled
family `\mathcal D` for which

\[
                  s_T=d_{\mathcal D}(T)-\kappa_m\ge0         \tag{4.10}
\]

is a connected `2B`-regular multigraph admitting an Euler circuit with the
odd-return property of Lemma 2.2.  This is a useful finite-dimensional
design gate.  It is still not sufficient by itself, because pair degrees
do not determine the actual sets (2.3) or prevent repetition among the
induced `A_j`.

Equations (3.3), (3.4), (4.2), the odd-return condition of Lemma 2.2, and
Hamiltonicity of the walk generated by (2.1) are the exact first design
gates.  Point regularity or uniform gap use alone is not sufficient: the
individual angle sets in (2.3) must still have loads one or two, and the
derived `A_j` must be all distinct.

## 5. Mersenne arithmetic and what remains open

Let

\[
                              m=2^a-1.                        \tag{5.1}
\]

Then `n=2^{a+1}-1`, and `B=Cat_m` is odd.  The exact target values are

\[
 |\mathcal D|=\frac{2nB}{m+2},
 \qquad
 d=\frac{2(m-1)B}{m+2},
 \qquad
 \kappa_m=\frac{(m-4)B}{m+2}.                               \tag{5.2}
\]

All are integers: `|\mathcal D|` is `W-N`, `d` is the binomial difference
(3.6)-(3.7), and `\kappa_m` is the binomial difference (4.7).  Their
incidence identities are mutually consistent:

\[
 n d=(m-1)|\mathcal D|,
 \qquad
 (m-2)d-2m\kappa_m=2B.                                      \tag{5.3}
\]

Also the forced gap count `B` is odd, exactly as Lemma 2.2 requires on the
odd cycle of length `W`.  Therefore the Mersenne family has no obstruction
at the total, point-total, aggregate pair-total, or gap-parity levels.  The
pointwise lower bounds (4.9) are genuine design constraints and are not
solved by these identities.

The remaining statement can be isolated cleanly.

### Balanced Kneser Hamilton gate

For every Mersenne `m>=3`, construct a cyclic word `g_0,...,g_{W-1}` and
the induced sets from (2.1) such that:

1. successive occurrences of each symbol have odd cyclic separation;
2. every symbol occurs exactly `B` times;
3. the induced `A_j` are all distinct; and
4. the sets `A_j^c\setminus\{g_{j-1},g_j\}` have loads in `{1,2}`.

These four conditions are necessary and sufficient for the requested
cardinality-optimal quotient Hamilton cycle.  The `m=3` certificate in the
predecessor note satisfies them.  No general construction, and no
unrestricted Mersenne-family impossibility, is proved here.

## 6. Infinite obstruction to the coordinate-cyclic algebraic route

Although the unrestricted gate remains open, a natural algebraic
specialization fails for infinitely many Mersenne parameters.

Let `\rho` be a regular `n`-cycle on the coordinates.  Call a Kneser
`2`-factor, in particular a Hamilton cycle, `\rho`-invariant when `\rho`
preserves its edge set.

### Theorem 6.1 (order-three stabilizer obstruction)

Let `m=2^a-1` with odd `a>=3`.  No `\rho`-invariant spanning Kneser
`2`-factor has all angle loads in `{1,2}`.  In particular no
`\rho`-invariant Kneser Hamilton cycle has the cardinality-optimal lower
ledger.

#### Proof

Here

\[
 n=2^{a+1}-1\equiv0\pmod3,
 \qquad
 m-1\equiv0\pmod3,
 \qquad
 m\not\equiv0\pmod3.                                       \tag{6.1}
\]

Let

\[
                              H=\langle\rho^{n/3}\rangle.    \tag{6.2}
\]

This is an order-three group whose coordinate orbits all have size three.
There are lower sets fixed by `H`: choose `(m-1)/3` of the `n/3`
coordinate triples.  In fact their number is

\[
                         \binom{n/3}{(m-1)/3}>0.              \tag{6.3}
\]

Fix one such lower set `S`.  A `\rho`-invariant factor has the equivariant
angle map

\[
                              \chi(\rho X)=\rho\chi(X),       \tag{6.4}
\]

because `\rho` carries the two factor-neighbours of `X` to the two
factor-neighbours of `\rho X`.  Hence the fibre `\chi^{-1}(S)` is
`H`-invariant.

The group `H` acts freely on the middle `m`-sets: an `H`-fixed subset is a
union of coordinate triples and therefore has cardinality divisible by
three, whereas `m` is not.  Thus every `H`-orbit in `\chi^{-1}(S)` has
size three.  It follows that

\[
                              \mu(S)=|\chi^{-1}(S)|\equiv0\pmod3. \tag{6.5}
\]

This is incompatible with `\mu(S)\in\{1,2\}`. `\square`

The obstruction applies to a regular cyclic or Singer-style coordinate
symmetry, not to arbitrary Hamilton cycles.  It explains why a single
fully equivariant algebraic ordering cannot settle all Mersenne parameters.
For even `a`, `3\nmid n`, so this particular stabilizer obstruction is
absent; reciprocity and Hamiltonicity still remain unproved.

## 7. The unconditional all-parameter approximate factor

We now use the canonical periodic box-ball `2`-factor `F_{PBBS}` of
`KG(n,m)`.  The proved PBBS first-shadow theorem states that, for every
`m>=2`,

\[
 1\le \mu_{PBBS}(S)\le3
 \qquad(S\in\tbinom{[n]}{m-1}).                              \tag{7.1}
\]

If

\[
 a_i=\#\{S:\mu_{PBBS}(S)=i\},\qquad 1\le i\le3,            \tag{7.2}
\]

then conservation gives

\[
                              a_2+2a_3=r,                    \tag{7.3}
\]

and hence

\[
                              a_3\le\frac r2=\frac W{m+2}.   \tag{7.4}
\]

This is the theorem proved from the cyclic parenthesis map in
`MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md`; only its exact conclusion
(7.1) is used here.

Every PBBS orbit length is divisible by `n`.  Therefore `F_{PBBS}` has at
most

\[
                              B=W/n                           \tag{7.5}
\]

components.  Apply the centered projection of Proposition 1.1.

### Theorem 7.1 (all-parameter coefficient-one depth-one factor)

For every `m>=2`, there is a spanning `2`-factor `J_m` of `J(2m+1,m)`
such that:

1. every rank-`(m+1)` union colour occurs exactly once;
2. every rank-`(m-1)` intersection colour occurs at least once;
3. every lower load is at most three;
4. at most `W/(m+2)` lower colours have load outside `{1,2}`; and
5. `J_m` has at most `2B=2W/(2m+1)` components.

#### Proof

Take `J_m=P(F_{PBBS})`.  Items 1--3 follow from Proposition 1.1 and
(7.1).  Since there are no holes and no loads above three, the colours
outside `{1,2}` are exactly the load-three colours; (7.4) proves item 4.
Each PBBS component produces at most two Johnson components by Proposition
1.1, and (7.5) proves item 5. `\square`

All five conclusions hold with no Mersenne hypothesis.  In particular,

\[
 \frac{W}{m+2}=o(W),
 \qquad
 \frac{2W}{2m+1}=o(W).                                      \tag{7.6}
\]

Breaking one edge in each component gives a spanning Johnson linear forest
with `W-O(W/m)` legal edges.  It misses at most `O(W/m)` formerly present
lower colours and the same number of upper colours.  Ordering its paths
creates only `O(W/m)` seams.  Thus it is a genuine non-Mersenne approximate
depth-one seed whenever the compiler accepts `o(W)` target error and
`o(W)` components.

If one insists on one Kneser Hamilton quotient rather than a factor, a
separate low-defect Hamiltonization theorem is still needed.  Ordinary
Hamiltonicity of `KG(n,m)` does not control the angle ledger, while the
PBBS proof controls the ledger but supplies a cycle factor.  Conflating
those two theorems would be the remaining hidden error.

## 8. Final distinction

There are now three different levels of conclusion.

1. **Exact Mersenne Hamilton target:** open beyond the displayed `m=3`
   certificate.  It is exactly the four-part gap-word gate in Section 5.
2. **Coordinate-cyclic exact target:** impossible for the infinite
   Mersenne subfamily with odd exponent, by Theorem 6.1.
3. **Approximate depth-one factor for all parameters:** proved by Theorem
   7.1, with complete lower coverage, exact upper coverage, `O(W/m)` bad
   loads, and `O(W/m)` components.

Accordingly the non-Mersenne parity failure should not be treated as a
depth-one no-go.  It prevents a single plain-complement-invariant Middle
Levels Hamilton lift; it does not prevent a coefficient-one Johnson factor
obtained from the same Kneser centered-edge mechanism.
