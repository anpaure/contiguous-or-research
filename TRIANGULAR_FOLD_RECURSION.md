# The exact fold recursion for triangular bounding-box words

## 1. Outcome

Let

\[
 \mathcal T_R=\{(0,0)\}\cup
 \{(s,y):1\le s\le R,\ 0\le y<s\}.
\]

The target indexed by \(0\le u<r\le R\), \(0\le x<r\), is the
bounding rectangle

\[
                         [u,r]\times[0,x].
\]

There is an exact self-similarity behind every target with both
\(u\ge1\) and \(x\ge1\).  The coordinate fold

\[
       \phi_R(s,y)=(s-1,\max\{y-1,0\})               \tag{1.1}
\]

maps \(\mathcal T_R\setminus\{(0,0)\}\) onto
\(\mathcal T_{R-1}\).  Its fibres have size two precisely over the nonzero
peaks.  Expanding those peaks into their two preimages lifts every universal
word for \(R-1\) to a word covering all strict positive-interior targets for
\(R\).

The complementary boundary targets \(u=0\) or \(x=0\) have one common
linear scaffold of length \(2R\).  Thus one sharp sufficient architecture
for the full triangular problem is a superposition between:

1. a recursively lifted interior word; and
2. one descending-peak/increasing-diagonal boundary scaffold.

Literal concatenation is rigorous but duplicates \(2R-1\) compulsory cells
at each level.  Superposing the scaffold with a sparsified or rearranged
lift is therefore a natural sufficient route to a near-once construction.
It is not proved to be a necessary normal form.  The fold nevertheless
isolates one recursive obstruction more sharply than a generic portal
formulation.

## 2. The fold map

Write \(P_s=(s,0)\).  For \(s\ge1\), define \(\phi_R\) by (1.1).
The fibres are

\[
\begin{aligned}
 \phi_R^{-1}(P_0)&=\{P_1\},\\
 \phi_R^{-1}(P_a)&=\{P_{a+1},(a+1,1)\}
                                      &&(1\le a\le R-1),\\
 \phi_R^{-1}(a,b)&=\{(a+1,b+1)\}
                                      &&(b\ge1).
\end{aligned}                                         \tag{2.1}
\]

These fibres partition \(\mathcal T_R\setminus\{P_0\}\).

### Lemma 1 (folding a positive-interior witness)

Suppose an interval of cells in \(\mathcal T_R\) has bounding box

\[
                         [u,r]\times[0,x]
\]

with \(u\ge1\) and \(x\ge1\).  Applying \(\phi_R\) entrywise gives an
interval with bounding box

\[
                         [u-1,r-1]\times[0,x-1].       \tag{2.2}
\]

#### Proof

The first coordinate is translated by \(-1\), so its minimum and maximum
become \(u-1,r-1\).  The interval contains a height-zero cell, and all
heights are transformed by \(y\mapsto\max(y-1,0)\).  Hence the transformed
minimum height is zero and the transformed maximum is \(x-1\).  QED.

The converse needs a controlled choice of preimages, because a lower peak
has both a height-zero and a height-one preimage.

### Proposition 1a (exact quotient)

The parameter map

\[
                 (u,r,x)\longmapsto(u-1,r-1,x-1)      \tag{2.3}
\]

is a bijection from the targets with \(u,x\ge1\) in \(\mathcal T_R\) to
all targets in \(\mathcal T_{R-1}\).

Moreover, if an upper word is universal, delete every occurrence of \(P_0\)
and apply \(\phi_R\) to the remaining entries.  The resulting word is
universal for \(\mathcal T_{R-1}\).  If the upper word spans
\(\mathcal T_R\), the folded word spans \(\mathcal T_{R-1}\).

#### Proof

The parameter inequalities translate exactly under subtraction by one.
For a lower target, take its corresponding strict upper target.  Any upper
witness for that target has first-coordinate minimum at least one, so it
contains no \(P_0\).  It remains contiguous after all \(P_0\) occurrences
are deleted, and Lemma 1 folds it to the requested lower target.  Spanning
follows because every lower cell has a preimage in (2.1).  QED.

## 3. Exact block lift

For a word \(W\) over \(\mathcal T_{R-1}\), define its full block lift
\(\mathcal L_R(W)\) by replacing entries as follows:

\[
\begin{aligned}
 P_0&\longmapsto [P_1],\\
 P_a&\longmapsto [P_{a+1},(a+1,1)]
                                      &&(a\ge1),\\
 (a,b)&\longmapsto[(a+1,b+1)]
                                      &&(b\ge1).
\end{aligned}                                         \tag{3.1}
\]

The order inside the two-letter peak block may be reversed; fix the
displayed orientation for definiteness.

### Theorem 2 (interior lifting theorem)

If \(W\) covers every target of \(\mathcal T_{R-1}\), then
\(\mathcal L_R(W)\) covers every target

\[
       [u,r]\times[0,x],
       \qquad 1\le u<r\le R,\quad1\le x<r.             \tag{3.2}
\]

If \(W\) contains every cell of \(\mathcal T_{R-1}\), then
\(\mathcal L_R(W)\) contains every cell of
\(\mathcal T_R\setminus\{P_0\}\).

#### Proof

Given (3.2), fold its parameters to

\[
       [u-1,r-1]\times[0,x-1].
\]

Choose a witnessing interval in \(W\), and in the lifted word take the
interval spanning the complete replacement block of every entry of that
witness.

The first-coordinate extrema increase by one.  Every lower witness contains
a peak, and its complete lifted block contains a height-zero preimage.  If
the lower maximum height is positive, a cell of that height lifts to height
\(x\).  If the lower maximum height is zero, its maximum first coordinate is
at least one, so the witness contains a nonzero peak; the corresponding
two-letter block contains a height-one preimage.  Thus the lifted height
extrema are exactly \(0,x\).

The spanning assertion follows directly from the fibre list (2.1): one
base occurrence of every lower cell supplies every cell in its fibre.  QED.

If \(n=|W|\) and \(p_+(W)\) is the total number of occurrences of
nonzero peaks in \(W\), then

\[
                      |\mathcal L_R(W)|=n+p_+(W).      \tag{3.3}
\]

## 4. A single boundary scaffold

Put

\[
\begin{split}
 \mathcal B_R={}&
 P_R,P_{R-1},\ldots,P_1,P_0,\\
 & (2,1),(3,2),\ldots,(R,R-1).
\end{split}                                           \tag{4.1}
\]

Its length is \(2R\).

### Theorem 3 (boundary scaffold)

Every target with \(x=0\) or \(u=0\) is represented inside
\(\mathcal B_R\).

#### Proof

For \(x=0\), the peak interval

\[
                         P_r,P_{r-1},\ldots,P_u
\]

has first-coordinate range \([u,r]\) and height zero.

For \(u=0\) and \(x\ge1\), use

\[
 P_r,P_{r-1},\ldots,P_0,
 (2,1),(3,2),\ldots,(x+1,x).                          \tag{4.2}
\]

Because \(x<r\), every diagonal cell in (4.2) has first coordinate at most
\(x+1\le r\).  The four extrema are therefore \(0,r,0,x\).  QED.

### Corollary 4 (literal recursive construction)

For every universal spanning word \(W\) on \(\mathcal T_{R-1}\),

\[
                    \mathcal B_R\Vert\mathcal L_R(W)  \tag{4.3}
\]

is a universal spanning word on \(\mathcal T_R\).

The two parts cover disjoint target regimes:

\[
 \{u=0\text{ or }x=0\}
 \quad\text{and}\quad
 \{u\ge1\text{ and }x\ge1\}.                         \tag{4.4}
\]

If \(W\) has excess \(q\) over \(|\mathcal T_{R-1}|\), the excess of
(4.3) over \(|\mathcal T_R|\) is exactly

\[
                         q+R+p_+(W).                  \tag{4.5}
\]

Indeed, \(|\mathcal T_R|-|\mathcal T_{R-1}|=R\), while (3.3) and the
\(2R\)-term in (4.3) give (4.5).

Formula (4.5) is not competitive with the existing fan word when iterated
literally.  Its value is structural, not numerical.

## 5. A sufficient superposition target

The lift already contains every scaffold cell except \(P_0\):

\[
 \{P_1,\ldots,P_R,(2,1),(3,2),\ldots,(R,R-1)\}
 \subseteq \mathcal L_R(W).                           \tag{5.1}
\]

Literal concatenation recopies all \(2R-1\) of these cells.  Consequently,
realizing the boundary family with occurrences already used by a valid
interior lift, with only subquadratic total repair over all levels, would
be sufficient for this recursive route to reach near-once length.  Other
boundary orders and non-fold constructions are not excluded.

The complete peak-block lift (3.1) is deliberately too rigid: it interleaves
\(P_{a+1}\) with \((a+1,1)\), whereas the scaffold wants all peaks together
and the top diagonal together.  Therefore the next lemma should not try to
preserve every lower witness by literal block substitution.  It should
prove a global pinning statement:

> Choose one or both preimages of each lower peak occurrence, and place the
> unused fibre elements into the same word, so that all lifted
> positive-interior targets survive and the existing occurrences contain
> the boundary scaffold.

This is a coupled interval-pinning problem on the peak fibres, not merely
independent binary choices: different witnesses may use different fibres,
and moving one preimage can contaminate several intervals.  A theorem with
\(o(R)\) repair per level would give \(o(R^2)\) repetitions in the
fixed-\(c\) triangular problem and would reopen the width-plus-surface
four-box construction.  A proof that every such superposition costs
\(\Omega(R)\) per level would obstruct this architecture only; a separate
normal-form theorem would be needed to infer an unrestricted quadratic
lower bound.

The fold theorem therefore gives an exact quotient and a sharp sufficient
construction target; no asymptotic conclusion is claimed here.
