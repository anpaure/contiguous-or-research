# Three private rails close the ungraded singleton-`T2` residual

**Date:** 2026-08-13  
**Status:** unconditional local all-height owner/lower path theorem.  The
literal Catalan tensor into the original `T0V` family is **not** proved:
there is a fixed-rank obstruction to simply adjoining the old suffix.  The
three paths would have to be installed in a new factor or by a conformal
trade; neither global step is asserted here.

## 1. Fixed prefix data

Write a 13-bit word with coordinate zero at the left, as in the frozen
`ML(13)` verifier.  Put

```text
B = 1011110011010,  x_B = 1011110011000,  y_B = 1011110010010,
C = 1010111011010,  x_C = 1010111011000,  y_C = 1010111010010,
H = 1000111011111,  x_H = 1000111010110,
                       y_H = 1000111001110,
                       z_H = 0000111001111.
```

All displayed lower-case words have rank seven.  Consecutive pairs differ
by one Johnson exchange and

\[
 x_B\cup y_B=B,\qquad x_C\cup y_C=C,
 \qquad x_H\cup y_H\cup z_H=H.                 \tag{1.1}
\]

The exact prefix lower facets are

```text
x_B cap y_B = 1011110010000,
x_C cap y_C = 1010111010000,
x_H cap y_H = 1000111000110,
y_H cap z_H = 0000111001110.
```

## 2. Auxiliary clock staircases

Let the clock ground be `Z_(2h)`, `h>=2`, and set

\[
 D_j=\{j,j+1,\ldots,j+h-1\}\pmod {2h},\qquad
 P_k=\bigcup_{j=0}^kD_j.                            \tag{2.1}
\]

Thus `P_k={0,...,h+k-1}` for `0<=k<=h`.  Define rank-`h`
sets

\[
 K_0=P_1\setminus\{0\}=D_1,qquad
 K_1=P_1\setminus\{1\},                            \tag{2.2}
\]

and, for `2<=j<=h-1`,

\[
 K_j=K_{j-1}\setminus\{j\}\cup\{h+j-1\}.          \tag{2.3}
\]

One has, for `1<=j<=h-1`,

\[
 |K_j|=h,\quad |K_{j-1}\triangle K_j|=2,\quad
 \bigcup_{i=0}^jK_i=P_j,                            \tag{2.4}
\]

while the exceptional initial union is simply `K_0=D_1`.

For the reflected rail use the involution

\[
 \rho(t)=h-1-t\pmod {2h},                           \tag{2.5}
\]

so `rho(D_j)=D_(-j)` and

\[
 \bigcup_{i=0}^j\rho(K_i)
 =D_0\cup D_{-1}\cup\cdots\cup D_{-j}
 \qquad(1\le j\le h-1),                            \tag{2.6}
\]

and `rho(K_0)=D_{-1}`.

Let `p_0,p_1` be two tag coordinates, disjoint from the clock and prefix.
The notation `(v,p,K)` means the rank-`h+8` owner
`v union {p} union K`, before adjoining any common core.

## 3. The three rails

Define the following owner paths:

\[
\begin{aligned}
 R_B={}&(x_B,p_0,K_0),(x_B,p_0,K_1),
        (y_B,p_0,K_1),(y_B,p_0,K_2),\ldots,
        (y_B,p_0,K_{h-1}),                           \tag{3.1}\\
 R_C={}&(x_C,p_0,\rho K_0),(x_C,p_0,\rho K_1),
        (y_C,p_0,\rho K_1),(y_C,p_0,\rho K_2),\ldots,
        (y_C,p_0,\rho K_{h-1}).                     \tag{3.2}
\end{aligned}
\]

Both have exactly `h+1` owners.  For the saturated rail, put

\[
\begin{aligned}
R_H={}&(x_H,p_0,D_0),(x_H,p_0,D_1),
 (y_H,p_0,D_1),(z_H,p_0,D_1),(z_H,p_1,D_1),\\
& (z_H,p_1,D_2),(z_H,p_1,D_3),\ldots,
   (z_H,p_1,D_{h+1}).                                \tag{3.3}
\end{aligned}
\]

It has `h+5` owners.  Every adjacent pair in `(3.1)--(3.3)` changes exactly
one coordinate out and one coordinate in.  Hence these are literal Johnson
owner paths, with respectively `h,h, h+4` distinct immediate-lower facets.

### Theorem 3.1 (exact literal support)

For every `h>=2`, consecutive prefixes of `R_B` after its base exchange
have values

\[
 B\cup\{p_0\}\cup P_k,qquad 1\le k\le h-1.         \tag{3.4}
\]

Consecutive prefixes of `R_C` give

\[
 C\cup\{p_0\}\cup
 (D_0\cup D_{-1}\cup\cdots\cup D_{-k}),
 \qquad1\le k\le h-1.                               \tag{3.5}
\]

The whole path `R_H` has value

\[
 H\cup\{p_0,p_1\}\cup\mathbb Z_{2h}.              \tag{3.6}
\]

These are exactly the `2h-1` ungraded residual values in Theorem 4.1 of
`MATH_THEOREM_T2_SINGLETON_CLOCK_EXACT_HIGHER_RESIDUAL_AND_REFLECTION_BARRIER_20260813.md`.

#### Proof

The base unions are `(1.1)`.  Equations `(2.4)` and `(2.6)` give
`(3.4)--(3.5)`.  The first and last clock sets on `(3.3)` are `D_0` and
`D_(h+1)` and its list contains `D_0,...,D_(h+1)`; already
`D_0 union D_h` is the full clock ground.  Its prefix owners span `H` and
the displayed tag exchange spans both tags.  This gives `(3.6)`.  The
residual classification identifies this list with the complete ungraded
current. \(\square\)

## 4. Simplicity, exposure, and residence scope

The three rails are pairwise owner- and lower-resource disjoint.  In the
concrete three-colour singleton construction they are also owner/lower
disjoint from the entire protected new `T2` factor.  This is literal, not
an orbit heuristic: the verifier checks the triples

\[
     (\text{base owner},\text{tag mask},\text{clock mask})
\quad\text{and}\quad
     (\text{base facet},\text{tag intersection},
                         \text{clock intersection}).          \tag{4.1}
\]

There are exactly

\[
 3h+7\ \text{owners},\qquad 3h+4\ \text{protected lower facets}. \tag{4.2}
\]

Within the three-rail bank, every unselected lower facet is contained in
at most two rail owners and every owner contains at most two selected rail
facets.  Thus its two literal protected-factor exposures are at most

\[
                         \alpha,\beta\le2.            \tag{4.3}
\]

The paths by themselves are clipped: their endpoint coordinate runs are
exported to a later completion.  The `B,C` internal coordinate words are
monotone or constant.  The only nonmonotone clock pattern needed in `R_H`
is, up to translation/complementation, the word of clock coordinate zero
on

```text
D0,D1,D1,D1,D1,D2,...,D_(h+1),
```

namely `1,0,...,0,1`; its unique bounded zero gap has length `h+3`.
Direct inspection of the other `R_H` coordinates gives no shorter bounded
positive run or zero gap.  Thus every internally bounded nonconstant run
or gap in the three bare rails has length at least `h`.

To obtain a globally `h`-biresident closure, each rail must be supplied
with **endpoint-compatible** collars which extend every clipped endpoint
positive run and zero gap to length at least `h`.  Mere monotonicity or
collar length `h` without this endpoint compatibility is insufficient.
The bare paths do not assert residence of an arbitrary completion.

## 5. The literal suffix tensor fails the fixed-rank check

Every local owner in `(3.1)--(3.3)` has rank `h+8`.  The old Dyck suffix
`V` in the `T0V` theorem has

\[
                         |U(V)|=r-6.                \tag{5.1}
\]

Consequently adjoining a disjoint constant suffix would produce rank

\[
                         h+8+r-6=r+h+2,             \tag{5.2}
\]

not the required upper-owner rank `r+1`.  The overshoot is `h+1`.  Thus
the tempting constant-suffix projection
argument is invalid for the literal target family.

A fixed-rank disjoint-ground tensor is possible only after shortening the
suffix to size `r-h-7`; it repairs a different decorated family.  For the
literal `T0V` family, the tag-plus-clock payload must instead be embedded
inside `U(V)`, leaving a varying core schematically of the form

\[
 C_V=U(V)\setminus(\{p\}\cup K).                   \tag{5.3}
\]

But `K` changes along a rail, so `(5.3)` is not a constant suffix
projection.  Pairwise owner/lower disjointness across different `V` and
simultaneous availability of the labelled payloads are new embedding
problems.  No Catalan tensor count or density claim is made here.

## 6. Exact factor/trade gate

The current paths use rank-`R` vertices which, in any spanning owner
factor, already have degree two somewhere.  They cannot be appended to the
incumbent MSW factor.  They must be planted prospectively in a new factor,
or arise as a balanced alternating modification which deletes the existing
two incidences at each used owner.

At the base `ML(13)` level, the selected rails are not canonical untouched
path segments.  For example their base lower exchanges are

```text
1011110010000, 1010111010000,
1000111000110, 0000111001110,
```

whereas only the last occurs between the chosen consecutive owners in the
frozen new chronology.  Direct comparison therefore gives no conformal
alternating circuit using exactly the rail owner bank.  The H100 verifier
establishes collision freedom but not factor balance.

Hence the sharp remaining global statement is:

> Find, uniformly over `V`, an alternating incidence circuit/forest whose
> positive side contains `(3.1)--(3.3)` and whose negative side removes the
> incumbent incidences at exactly the same owner and lower resources; or
> prove a fixed-rank varying-core embedding and factor extension theorem
> for the literal suffix family.

No claim of a whole MSW packet/trade is made before that balance row is
closed.

## 7. H100 certificate

Verifier:

```text
scratch/search_msw_t2_singleton_backup_rails.py
```

SHA-256:

```text
0d55d97c87322f5bd37442781b35db926856c53c90dc6e1843438d82406a3621
```

Artifact (`h=2,...,8`):

```text
scratch/search_msw_t2_singleton_backup_rails_20260813.h100.out
```

SHA-256:

```text
a1b28c84ca645e7c803e7a22b50238c9e718898f702822bcd158de1bda0422a4
```

For every tested height, the candidate counts are `42,49,14` for
`B,C,H`; a pairwise and main-factor-disjoint triple exists; the counts are
`3h+7,3h+4`; and the within-bank incidence multiplicities are `(2,2)`.
The protected-factor exposure bound `(4.3)` is the symbolic path argument,
not that narrower measured statistic.  The computation was
run on `h100`; local work was limited to patching and proof inspection.
