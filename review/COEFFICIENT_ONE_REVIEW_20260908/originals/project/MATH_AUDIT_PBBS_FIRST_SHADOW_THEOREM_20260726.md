# Independent audit of the PBBS first-shadow theorem

Date: 2026-07-26

Audited file:
`MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md`, especially Sections
2--3 and the imported orbit-length assertion.

Finite diagnostic:
`scratch/audit_pbbs_first_shadow.py`.

## 0. Verdict

The theorem passes.

For the canonical cyclic-parenthesis/PBBS permutation `f` on
`\binom{[2m+1]}m`, and every
`S\in\binom{[2m+1]}{m-1}`, the angle load satisfies

\[
                              1\le\mu_P(S)\le3.               \tag{0.1}
\]

The lower-bound witness and the multiplicity-three upper bound in the
attacked note are correct.  Their prose suppresses two elementary matching
lemmas, but no false implication is hidden.  Those lemmas are supplied in
Sections 2--4 below.

The PBBS orbit assertion also passes, with an important dependency label:

\[
                 \text{every PBBS orbit length is divisible by }2m+1.
                                                                    \tag{0.2}
\]

This does **not** follow merely from `f` being a cyclic-equivariant
permutation.  It uses the componentwise coordinate-homomesy theorem for the
periodic box-ball map.  The proof chain in
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md` is valid: parenthesis flip is
the infinite-capacity periodic BBS evolution, the theta-function period is
genuine even with repeated soliton amplitudes, and telescoping gives exact
site homomesy.  Section 6 records the short implication from homomesy to
(0.2).  Thus (0.2) is rigorous but imported, not proved internally in the
attacked note.

Finally, centering the two PBBS neighbours at every Kneser vertex gives a
simple spanning `2`-factor of `J(2m+1,m)` with:

* every rank-`(m+1)` union colour exactly once;
* lower intersection histogram exactly `\mu_P`; and
* at most

  \[
                              2\operatorname {Cat}_m
                              =\frac{2W}{2m+1}=O(W/m)        \tag{0.3}
  \]

  components.

No counterexample occurs in exhaustive exact checks through `m=8` for all
local matching assertions and through `m=10` for the load, orbit, and
projection assertions.  The finite checks are diagnostic only; the proof
of (0.1)--(0.3) is symbolic.

Accordingly the PBBS first-shadow theorem and its centered Johnson-factor
corollary are safe to use, provided the orbit-divisibility statement remains
explicitly attributed to PBBS homomesy.

## 1. Exact matching conventions

Put

\[
                              n=2m+1.                         \tag{1.1}
\]

Write a subset as a cyclic binary word, with `1` an opening step and `0` a
closing step.

The **forward matching** repeatedly removes cyclic adjacent `10` pairs.
The **reverse matching** repeatedly removes cyclic adjacent `01` pairs.
When a word has more zeros than ones, the survivors are zeros.  The result
is independent of the deletion order: cut immediately after one surviving
zero and use the ordinary stack matching on the resulting linear word.
Equivalently, these are the two orientations of the unique cyclic
noncrossing matching.

For `A\in\binom{[n]}m`, each matching leaves one zero.  Denote the forward
and reverse survivors by

\[
                              r_+(A),\qquad r_-(A).            \tag{1.2}
\]

The PBBS map is

\[
                              f(A)=A^c\setminus\{r_+(A)\}.    \tag{1.3}
\]

### Lemma 1.1 (inverse formula)

The map `f` is a permutation and

\[
                              f^{-1}(A)=A^c\setminus\{r_-(A)\}. \tag{1.4}
\]

#### Proof

Forward matching pairs every `1` of `A` with a matched `0`.  Formula (1.3)
flips both bits in every pair and leaves the unique unmatched zero fixed.
The same pairs in the new word are noncrossing `01` pairs, and reverse
matching leaves the same zero unmatched.  Flipping those reverse pairs
recovers `A`.  This proves both invertibility and (1.4). `\square`

Adjacent PBBS states are disjoint because every old `1` is changed to zero.
Thus the permutation orbits are closed walks in `KG(n,m)`.  Once (0.2) is
known, their lengths are at least `n>=5` for `m>=2`, so they are simple
cycle components and `f(A)\ne f^{-1}(A)`.

## 2. The clean-label lemma used by the upper bound

Fix

\[
                              S\in\binom{[n]}{m-1},
 \qquad                       T=[n]\setminus S.              \tag{2.1}
\]

Both cyclic matchings of the deficit-three word `S` leave three zeros.
Let their survivor sets be

\[
                              U_+(S),\qquad U_-(S),
 \qquad |U_+(S)|=|U_-(S)|=3.                                \tag{2.2}
\]

For `u\in T`, define

\[
 \alpha_S(u)=r_+(S\cup\{u\}),
 \qquad
 \beta_S(u)=r_-(S\cup\{u\}).                               \tag{2.3}
\]

### Lemma 2.1 (clean-label images)

One has

\[
 \boxed{alpha_S(T)\subseteq U_+(S)},
 \qquad
 \boxed{eta_S(T)\subseteq U_-(S)}.                        \tag{2.4}
\]

#### Proof

Contract every old forward-matched pair of `S`.

If `u` is one of the three unmatched zeros, flipping it leaves, after the
old contractions, one `1` and two old unmatched zeros.  Forward reduction
therefore leaves one of those old zeros.

If `u` was matched, omit its old pair from the contraction.  Its old
partner is a `1`, and the flipped `u` is now another `1`.  The reduced
cyclic word has two `1`s and the same three old unmatched zeros.  Reducing
it leaves one of those three zeros.  In either case
`\alpha_S(u)\in U_+(S)`.

The identical argument with `01` pairs proves the reverse inclusion for
`\beta_S`. `\square`

This contraction proof is the precise justification for the
“deficit-three clean-label argument” in line (3.9) of the attacked note.
It does not assume that `u` is an unmatched zero or that the Dyck blocks
have distinct heights.

## 3. Exact occurrence/fixed-point bijection

For `u\in T`, formulas (1.3)--(1.4) give

\[
 f(S\cup\{u\})
 =T\setminus\{u,\alpha_S(u)\},                              \tag{3.1}
\]

and

\[
 f^{-1}(S\cup\{v\})
 =T\setminus\{v,\beta_S(v)\}.                              \tag{3.2}
\]

The unmatched coordinate cannot be the newly flipped coordinate, so

\[
                              \alpha_S(u)\ne u,
 \qquad                       \beta_S(v)\ne v.               \tag{3.3}
\]

### Lemma 3.1 (angle occurrences are fixed points)

Directed PBBS two-paths

\[
 S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{v\}  \tag{3.4}
\]

whose endpoint intersection is `S` are in bijection with the fixed points
of `\beta_S\circ\alpha_S` on `T`.

#### Proof

Equations (3.1)--(3.2) give the same middle state `X` exactly when

\[
                 \{u,\alpha_S(u)\}=\{v,\beta_S(v)\}.        \tag{3.5}
\]

The two endpoints in (3.4) are distinct, and (3.3) holds, so (3.5) is
equivalent to

\[
                              v=\alpha_S(u),
 \qquad                       u=\beta_S(v).                  \tag{3.6}
\]

This is precisely `\beta_S(\alpha_S(u))=u`.  Conversely a fixed point
gives (3.4) with

\[
                              X=T\setminus\{u,\alpha_S(u)\}. \tag{3.7}
\]

The predecessor label `u` determines `X`, so distinct fixed points are not
double-counted. `\square`

By Lemma 2.1, every fixed point belongs to

\[
                       \beta_S(T)\subseteq U_-(S),           \tag{3.8}
\]

a set of size three.  Therefore

\[
                              \mu_P(S)\le3.                  \tag{3.9}
\]

The upper-bound argument in the attacked note is consequently correct.

## 4. The constructive fixed point used by the lower bound

List the forward-unmatched zeros of `S` in cyclic order.  Cutting at them
gives the unique decomposition

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,                       \tag{4.1}
\]

where every `D_i` is a possibly empty Dyck word.  Since `m>=2`, the word
contains `m-1>0` ones, so at least one block is nonempty.

Choose `D_i` of maximum height.  Let `u` be the down-step immediately after
the rightmost occurrence of its maximum.  Such a step exists because
`D_i` returns to height zero.

### Lemma 4.1 (forward label)

\[
                              r_+(S\cup\{u\})=z_i.           \tag{4.2}
\]

#### Proof

In the old matching, `u` is paired with an earlier opening step in `D_i`.
Contract all other old matched pairs.  After flipping `u`, the reduced
cyclic word, starting at `z_i`, has the form

\[
                       0_{z_i}\,1\,1\,0_{z_{i+1}}\,0_{z_{i+2}}. \tag{4.3}
\]

Forward reduction matches the two `1`s to `z_{i+1}` and `z_{i+2}` and
leaves `z_i`. `\square`

We also need the standard reverse cycle lemma.

### Lemma 4.2 (reverse survivor from height)

In a cyclic `0/1` word with one more zero than one, the reverse-unmatched
zero is the down-step following the rightmost global maximum of the prefix
height (`1=+1`, `0=-1`).

#### Proof

Let `M` be the global maximum and rotate the word to begin with the zero
step which leaves the rightmost occurrence of `M`.  Treat `0` as an opening
step and `1` as a closing step.  Before the rotation wraps, the original
height never returns to `M`, so every reverse-height prefix is positive.
After the wrap, the original total is `-1` and every original prefix has
height at most `M`; the reverse-height prefix is again positive.  Its total
is one.  Ordinary linear `01` stack matching therefore pairs every symbol
except the initial zero.  Rotating back preserves the cyclic noncrossing
matching.  This is the reverse form of the usual cycle lemma. `\square`

Now flip `z_i` instead of `u` and rotate the resulting middle word as

\[
                         1D_i\,0D_{i+1}\,0D_{i+2}.           \tag{4.4}
\]

If `H(D)` denotes maximum Dyck height, the maximum prefix heights in its
three regions are at most

\[
 1+H(D_i),\qquad H(D_{i+1}),\qquad H(D_{i+2})-1.             \tag{4.5}
\]

The first is strictly largest because `D_i` was chosen with maximum height.
Its rightmost occurrence is the rightmost maximum of `D_i`, followed by
`u`.  Lemma 4.2 gives

\[
                              r_-(S\cup\{z_i\})=u.           \tag{4.6}
\]

Equations (4.2) and (4.6) say

\[
 \alpha_S(u)=z_i,
 \qquad
 \beta_S(z_i)=u.                                            \tag{4.7}
\]

Thus `u` is a fixed point of `\beta_S\circ\alpha_S`, and Lemma 3.1 gives

\[
                              \mu_P(S)\ge1.                  \tag{4.8}
\]

For `m=2`, the three blocks contain in total one opening and one closing;
exactly one is `10`, so the same construction applies.  This verifies every
step of the lower-bound proof.

Combining (3.9) and (4.8) proves (0.1).

## 5. Load identities and the claimed `O(W/m)` exception set

Let

\[
 a_j=\#\{S:\mu_P(S)=j\},\qquad 1\le j\le3.                 \tag{5.1}
\]

There are

\[
 N=\binom n{m-1}
\]

lower targets and `W=\binom nm` angle occurrences.  Since there are no
holes and no loads above three,

\[
 a_1+a_2+a_3=N,
 \qquad
 a_1+2a_2+3a_3=W.                                          \tag{5.2}
\]

Subtracting gives

\[
 a_2+2a_3=W-N=\frac{2W}{m+2}.                              \tag{5.3}
\]

Consequently

\[
 \boxed{a_3\le\frac{W}{m+2}=O(W/m).}                       \tag{5.4}
\]

The only loads outside `{1,2}` are the load-three targets, so the attacked
note's defect conclusion is exact.

## 6. Orbit lengths: valid imported theorem and exact implication

The attacked note invokes the following external PBBS homomesy theorem.

### PBBS site-homomesy theorem

For a periodic BBS orbit of fundamental period `P` on words of length `L`
and weight `K<L/2`, every coordinate is occupied exactly

\[
                              \frac{PK}{L}                   \tag{6.1}
\]

times during the orbit.

The dedicated audit
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md` checks the complete proof
chain:

1. cutting after an unmatched zero identifies the cyclic parenthesis flip
   with the infinite-capacity periodic carrier evolution;
2. the Kuniba--Sakamoto formula used there allows repeated soliton
   amplitudes;
3. translating by `D=det F` is a genuine theta period; and
4. the time telescope is independent of the spatial coordinate and equals
   `DK/L`, hence `PK/L` on the fundamental orbit.

No generic-amplitude assumption or unproved orbit transitivity is used.
Accepting that named periodic-BBS theorem, the orbit-length conclusion here
is immediate and exact.

### Proposition 6.1 (PBBS orbit divisibility)

Every orbit of `f` on `\binom{[2m+1]}m` has length divisible by `2m+1`.

#### Proof

Apply (6.1) with `L=2m+1` and `K=m`.  The occupation count `Pm/L` is an
integer.  Since

\[
                              \gcd(2m+1,m)=1,                \tag{6.2}
\]

one has `2m+1\mid P`. `\square`

This is the only place where the first-shadow package needs the external
homomesy theorem.  Cyclic equivariance of `f` by itself would not prove
Proposition 6.1.

Since the orbit lengths sum to `W`, their number is at most

\[
                              \frac W{2m+1}=B=\operatorname {Cat}_m. \tag{6.3}
\]

## 7. Centered projection audit

Let `F_P` be the PBBS Kneser cycle factor.  For each center `X`, define

\[
                    e_X=\{f^{-1}(X),f(X)\}.                  \tag{7.1}
\]

### Theorem 7.1 (exact centered Johnson factor)

The family `\{e_X\}` is a simple spanning `2`-factor of `J(2m+1,m)`.
Its union colours are all members of `\binom{[n]}{m+1}`, exactly once, its
intersection histogram is `\mu_P`, and it has at most `2B` components.

#### Proof

Both members of `e_X` are PBBS neighbours of `X`, hence are disjoint from
`X`.  They are distinct by Proposition 6.1.  They are distinct `m`-subsets
of the `(m+1)`-set `X^c`, so

\[
 f^{-1}(X)\cup f(X)=X^c,
 \qquad
 f^{-1}(X)\cap f(X)=\chi_P(X).                              \tag{7.2}
\]

Thus `e_X` is a Johnson edge with the stated colours.  The center is
recoverable from the edge as

\[
                              X=(\bigcup e_X)^c,              \tag{7.3}
\]

so distinct centers give distinct edges.  As `X` ranges over all middle
sets, `X^c` ranges bijectively over every upper colour.

A Johnson vertex `Y` lies in the two centered edges belonging to its two
Kneser-factor neighbours.  Hence every Johnson vertex has degree two and
the centered graph is a simple spanning `2`-factor.

On a PBBS component of length `P`, centering joins cyclic positions `j-1`
and `j+1`.  The step-two graph on `\mathbb Z_P` has `\gcd(2,P)\le2`
components.  Proposition 6.1 and (6.3) therefore give at most `2B`
Johnson components. `\square`

Combining Theorem 7.1 with (0.1) and (5.4) proves every PBBS assertion used
in the Mersenne/non-Mersenne successor note.

## 8. Exact small-case counterexample search

The independent checker

[`scratch/audit_pbbs_first_shadow.py`](scratch/audit_pbbs_first_shadow.py)

constructs the cyclic `10` matching directly.  It does not import an orbit
table or angle histogram.  For every tested lower target it also checks:

\[
 \alpha_S(T)\subseteq U_+(S),
 \qquad
 \beta_S(T)\subseteq U_-(S),
 \qquad
 \mu_P(S)=|\operatorname {Fix}(\beta_S\circ\alpha_S)|.       \tag{8.1}
\]

It then checks permutation/inverse consistency, Kneser adjacency, orbit
divisibility, centered-edge uniqueness, Johnson degree two, exact union
coverage, equality of the centered and PBBS angle histograms, and the
component bound.

The complete structural check through `m=8` gives:

\[
\begin{array}{c|r|rrrr|rr|r}
m&W&\mu=0&\mu=1&\mu=2&\mu=3&c(P)&c(J)&\max(P)/(2m+1)\\ \hline
1&3&0&0&0&1&1&1&1\\
2&10&0&0&5&0&2&2&1\\
3&35&0&7&14&0&3&3&3\\
4&126&0&45&36&3&6&6&5\\
5&462&0&209&110&11&12&12&7\\
6&1716&0&884&377&26&26&26&21\\
7&6435&0&3630&1320&55&73&73&11\\
8&24310&0&14722&4590&136&146&146&77
\end{array}                                                  \tag{8.2}
\]

A lighter full histogram/orbit/projection scan at `m=9,10` likewise found
no hole, no load above three, no nondivisible orbit, and no projection
failure.  At those parameters the load triples were respectively

\[
\begin{array}{c|rrr}
m&\#(\mu=1)&\#(\mu=2)&\#(\mu=3)\\ \hline
9&59223&15922&437\\
10&236733&55608&1589.
\end{array}                                                  \tag{8.3}
\]

These computations found no counterexample, including the boundary case
`m=2`.  They are not used to infer the general theorem.

## 9. Corrections and dependency discipline

No mathematical retraction is needed.  Two expository corrections should
be observed when reusing the result.

1. The sentence “Since `gcd(n,m)=1`, every orbit length is divisible by
   `n`” is not a consequence of coprimality alone.  Its missing premise is
   PBBS site homomesy.  Proposition 6.1 supplies the exact implication.
2. The image inclusions in the multiplicity-three proof use confluence of
   cyclic matching after contraction.  Lemma 2.1 supplies that argument;
   the informal phrase “the third old unmatched zero remains” is correct
   but too compressed to serve as the proof by itself.

With those dependencies exposed, the chain

\[
 \text{PBBS permutation}
 \Longrightarrow 1\le\mu_P\le3
 \Longrightarrow \text{complete lower shadow and }O(W/m)\text{ bad loads}
\]

and

\[
 \text{PBBS homomesy}
 \Longrightarrow (2m+1)\mid P
 \Longrightarrow O(W/m)\text{ centered Johnson components}
\]

is fully rigorous.
