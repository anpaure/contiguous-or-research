# Six-slot endpoint-efficient Bellman clocks: subcomplementary-pair closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It closes the genuine
size-six-efficient branch after first-crossing deletion, endpoint saturation,
and least-maximizer assignment.  It does not close the other six-slot
efficiency branches, the all-grid Bellman inequality, or an OR-word upper
bound.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F(w)=F_A(w)=\sum_{q\ge0}K(qA+w),
 \qquad
 C=F(0).
\tag{0.1}
\]

We use the following previously proved train bounds:

\[
 C>{43\over1000},
 \qquad
 F(w)>{57\over1400}\quad(0\le w\le A/4),
\tag{0.2}
\]

\[
 F(w)<{61\over1000}\quad(0\le w\le2A/5),
 \qquad
 F(w)>0\quad(0\le w\le A/2),
\tag{0.3}
\]

and

\[
 F(w)+F(A-w)>-\varepsilon,
 \qquad
 \varepsilon={1\over20000}.
\tag{0.4}
\]

The train is decreasing on `[A/4,A/2]`.  Combining this with the upper
bound in (0.3) gives

\[
 F(w)<{61\over1000}\qquad(0\le w\le A/2).
\tag{0.5}
\]

Indeed, (0.3) covers `w<=2A/5`, while for `2A/5<=w<=A/2` monotonicity gives
`F(w)<=F(2A/5)<61/1000`.

## 1. A train pair requiring no ceiling allocation

### Lemma 1.1 (subcomplementary pair)

If

\[
 0\le y\le z,
 \qquad
 y+z\le A,
\tag{1.1}
\]

then

\[
 \boxed{
 F(y)+F(z)>-{8541\over420000}.}
\tag{1.2}
\]

#### Proof

If `z<=A/2`, both terms are positive by (0.3).  Hence suppose `z>A/2`
and put

\[
                         v=A-z.
\tag{1.3}
\]

Then `0<=y<=v<A/2`.  Reflection gives

\[
 F(y)+F(z)>F(y)-F(v)-\varepsilon.
\tag{1.4}
\]

If `y>=A/4`, then `A/4<=y<=v<A/2`; monotone decrease on this interval
gives `F(y)>=F(v)`, and (1.4) is greater than `-epsilon`.

If `y<A/4`, equations (0.2), (0.4), and (0.5) give

\[
\begin{aligned}
 F(y)+F(z)
 &>{57\over1400}-{61\over1000}-{1\over20000}\\
 &=-{8541\over420000}.
\end{aligned}
\tag{1.5}
\]

Since `1/20000<8541/420000`, both cases imply (1.2). \(\square\)

## 2. Complete six-efficient branch

### Theorem 2.1

Let

\[
 (c_0,c_1,c_2,c_3,c_4,c_5,c_6)
\]

be an internally superadditive first-crossing table after endpoint
saturation and least-maximizer assignment, and suppose size six is the
least maximum-density denomination.  Then its Bellman functional is
strictly positive.

#### Proof

Least-critical endpoint normalization gives

\[
                         c_6=A.
\tag{2.1}
\]

The literal endpoint-period comparison gives

\[
 \Phi(c)\ge C+\sum_{i=1}^{5}F(c_i).
\tag{2.2}
\]

This is a comparison with the actual Bellman clock: at capacity `6q+i`,
the configuration consisting of `q` endpoint generators and the size-`i`
generator has value `qA+c_i`.  At `q=0`, internal superadditivity gives
equality; for `q>=1`, both sides lie in the increasing Gaussian tail of
`K`.

Internal superadditivity at the endpoint yields

\[
 c_1+c_5\le A,
 \qquad
 c_2+c_4\le A,
 \qquad
 2c_3\le A.
\tag{2.3}
\]

The table is nondecreasing, so Lemma 1.1 applies to the pairs `(c_1,c_5)`
and `(c_2,c_4)`.  Also `F(c_3)>0` by (0.3).  Therefore

\[
\begin{aligned}
 \Phi(c)
 &>{43\over1000}-2{8541\over420000}\\
 &= {163\over70000}>0.
\end{aligned}
\tag{2.4}
\]

This proves the complete genuine size-six-efficient branch. \(\square\)

## 3. Consequence and scope

After the proof-safe normalization order

\[
 \text{first crossing}\longrightarrow
 \text{endpoint saturation}\longrightarrow
 \text{least maximum-density size},
\]

a nonpositive six-slot table cannot be assigned to efficiency size six.
The remaining possible least-maximizer sizes are `2,3,4,5`.  No assertion
about those branches is made here.

The new point is structural: one ceiling train pays simultaneously for the
two endpoint-complementary residue pairs.  It is unnecessary to bound the
five nonzero residue trains independently.

## 4. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| least-critical endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complementary reflection, small-shift lower bound, positivity, monotonicity | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| sharp ceiling and half-band upper bounds | `MATH_THEOREM_FIVE_SLOT_SHORT_SINGLETON_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md` | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |

The current short-singleton dependency is independently bound by audit SHA
`c0427eb680265563ffb85448a0a538d89a63c6421d668a847d9d09f05e6e3760`.
