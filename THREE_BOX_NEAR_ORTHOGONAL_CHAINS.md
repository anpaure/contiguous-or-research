# Two near-minimum orthogonal chain partitions of a cubic three-chain box

## 1. Outcome

Let

\[
                         P_m=[0,m]^3
\]

with the coordinatewise order, and let `W_m` be its width.  There are two
explicit orthogonal chain partitions of `P_m` such that

\[
                         |\mathcal L|=W_m,
                 \qquad |\mathcal R'|=W_m+m.                    \tag{1.1}

\]

Here orthogonal means that a chain from one partition and a chain from the
other share at most one point.  The additive loss is therefore only one
side length, exactly the scale permitted by the three-box constant-one
reduction.

The construction starts from the two standard hook-parenthesized SCDs
`(xy)z` and `(xz)y`.  They are already pairwise two-orthogonal: every pair
of chains meets at most twice.  Their double intersections form a triangular
family.  Cutting those chains and shifting every upper piece by one **inner
chain label** (not by one outer label) removes all doubles simultaneously,
at a total cost of exactly `m` extra chains.

This clears the strongest chain-count/orthogonality gate for cubic boxes.
It is not yet an OR word: endpoint precedence, triangular endpoint support,
and coordinatewise pinning still have to be imposed on the two partitions.

## 2. The two hook decompositions

For a point `v=(x,y,z)`, define

\[
\begin{split}
 i_L&=\min(y,m-x),&t_L&=x+y-i_L,
 &j_L&=\min(t_L,m-z),\\
 i_R&=\min(z,m-x),&t_R&=x+z-i_R,
 &j_R&=\min(t_R,m-y).                                           \tag{2.1}
\end{split}

\]

Let `L_(i,j)` be a fiber of `(i_L,j_L)` and `R_(i,j)` a fiber of
`(i_R,j_R)`.  These are precisely the standard recursive hook SCDs obtained
by first decomposing the `xy` (respectively `xz`) rectangle and then taking
the hook product with the remaining coordinate.  In particular, their
nonempty fibers are saturated symmetric chains and each family has `W_m`
members.

### Lemma 1 (all double intersections)

Every pair `L_(h,k),R_(i,j)` meets in at most two points.  A double
intersection occurs exactly when

\[
                         (h,k)=(i,j),\qquad i+j<m.               \tag{2.2}

\]

The two common points are

\[
                 u_{i,j}=(j,i,i),
       \qquad   v_{i,j}=(m-i,m-j,m-j).                          \tag{2.3}

\]

### Proof

Substitute (2.1) and separate according to which term realizes each of the
four minima.  If both labels are fixed, each regime fixes two coordinates
and leaves a monotone interval in the third.  Distinct regimes meet only at
their hook corners.  The only two compatible corners with the same pair of
labels are (2.3), and they are distinct exactly when `i+j<m`.  Conversely,
direct substitution shows that both points in (2.3) have left and right
label `(i,j)`.  \(\square\)

The elementary four-regime calculation also gives the more precise facts
used below.

## 3. Cutting the triangular family

For every label in

\[
                         \mathcal T_m={(i,j):i,j\geq0, i+j\leq m\},
                                                                    \tag{3.1}
\]

cut `R_(i,j)` at `u_(i,j)`.  Write

\[
 P_{i,j}=\{v\in R_{i,j}:v\leq u_{i,j}\},
 \qquad
 S_{i,j}=\{v\in R_{i,j}:v>u_{i,j}\}.                           \tag{3.2}
\]

The final suffix `S_(m,0)` is empty.  All other pieces needed below are
nonempty.

### Lemma 2 (left labels of the pieces)

For `i+j<=m`,

\[
              \{\lambda_L(v):v\in P_{i,j}\}
                    =\{(h,j):0\leq h\leq i\},                  \tag{3.3}
\]

whereas

\[
              \{\lambda_L(v):v\in S_{i,j}\}
                    \subseteq\{(h,k):h\geq i\}.                \tag{3.4}

\]

Within each one of `P_(i,j)` and `S_(i,j)`, no left label is repeated.

### Proof

Follow the two hook segments of `R_(i,j)` through (2.1).  Before and
including `u_(i,j)`, the first left label increases from `0` to `i` while
the second stays `j`, giving (3.3).  Strictly after the cut, the first left
label is at least `i`, giving (3.4).  Lemma 1 shows that the only possible
repetition in the full right chain is split between its prefix and suffix,
so neither piece contains a repetition internally.  \(\square\)

## 4. The inner-label shift

For

\[
             0\leq i\leq m-2,\qquad0\leq j\leq m-i-1,         \tag{4.1}

\]

form

\[
                         Q_{i,j}=P_{i,j}\cup S_{i+1,j},          \tag{4.2}

\]

with the prefix written first.  Also reunite `P_(0,m)` and `S_(0,m)` into
the original chain `R_(0,m)`.  Leave every unpaired nonempty prefix or
suffix as its own chain, and leave every original `R`-chain whose label is
outside `T_m` unchanged.  Call the resulting partition `mathcal R'`.

### Lemma 3

Every `Q_(i,j)` in (4.2) is a chain.

### Proof

Its lower piece ends at

\[
                         u_{i,j}=(j,i,i).
\]

The first point of `S_(i+1,j)` is

\[
 \begin{cases}
 (j,i+2,i+1),&j<m-i-1,\\
 (j,i+1,i+2),&j=m-i-1.
 \end{cases}                                                    \tag{4.3}

\]

Both points in (4.3) dominate `u_(i,j)`.  Thus concatenating the two chain
pieces preserves comparability.  Saturation is neither claimed nor needed.
\(\square\)

### Theorem 4

`mathcal L` and `mathcal R'` are orthogonal chain partitions, and (1.1)
holds.

### Proof

The pieces in (3.2) partition every cut right chain, and (4.2) merely pairs
some of those pieces, so `mathcal R'` is a partition.  Each unpaired piece
is individually orthogonal to `mathcal L` by Lemmas 1--2.  In (4.2), the
left labels used by the prefix have first coordinate at most `i`, by (3.3),
whereas those used by the suffix have first coordinate at least `i+1`, by
(3.4).  They are disjoint.  Hence no `Q_(i,j)` meets any left chain twice.

It remains to count.  The triangular family (3.1) has

\[
                         |\mathcal T_m|={ (m+1)(m+2)\over2}
\]

chains.  Cutting them creates `2|T_m|-1` nonempty pieces, because only
`S_(m,0)` is empty.  The number of pairings in (4.2), together with the
reunion at `(0,m)`, is

\[
 \sum_{i=0}^{m-2}(m-i)+1={m(m+1)\over2}.                        \tag{4.4}
\]

Relative to the original `|T_m|` chains, the net increase is therefore

\[
 (2|T_m|-1)-{m(m+1)\over2}-|T_m|=m.                            \tag{4.5}

\]

All chains outside `T_m` are unchanged, so
`|mathcal R'|=W_m+m`.  \(\square\)

## 5. Why shifting the outer label fails

The superficially more natural recombination

\[
                         P_{i,j}\cup S_{i,j+1}
\]

does not remove the doubles.  In fact, for fixed `i`, every nonterminal
prefix `P_(i,j)` shares a left label with every suffix `S_(i,k)`.  Thus no
permutation confined to one fixed inner-label row can make the pieces
orthogonal.  The shift `i -> i+1` in (4.2) is essential: it separates the
two left-label ranges at the strict cut `i | i+1`.

## 6. Remaining endpoint problem

The theorem supplies the correct number of chains for the two endpoint
families required by a near-width interval representation.  The next local
questions are now concrete and only polynomial-sized:

1. order the `W_m` left chains and `W_m+m` right chains so every occupied
   incidence cell lies in the physical triangle `left<=right` with only
   `O(m)` padding;
2. respect the within-chain precedence orders induced by target inclusion;
3. verify the coordinatewise interval-stabbing/pin-survival condition.

The incidence labels `(i,j)` are triangular grid coordinates and the
recombination is monotone in `i`, so an `O(m)` one-sided bandwidth ordering
is plausible.  Unlike the concentric-ring central band, this construction
is not yet subject to a cubic interval-capacity deficit.
