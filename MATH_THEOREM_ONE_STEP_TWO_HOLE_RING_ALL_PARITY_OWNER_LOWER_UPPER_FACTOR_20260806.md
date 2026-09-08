# One-step two-hole rings give an all-parity owner/lower/upper fractional factor

## Status

Natural one-step de Bruijn balance removes the old parity restriction on
source-ring periods.  The shortest period with a noncollapsed immediate-
upper palette is therefore

\[
                            L=D+2=d+3
\]

for both parities of `d`.  This note gives the literal packet and its exact
owner, immediate-lower, and immediate-upper degrees.  Uniform packet weight
is an exact owner/lower fractional factor and has only the sharp factor
`(r+1)/(r-1)` of upper oversupply; uniform upper thinning closes that row.

This is a fractional packet theorem.  It does not select an integral packet
matching or cover the deeper named targets.

## 1. The packet

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+2,\qquad c=r-D,           \tag{1.1}
\]

and assume `d>=1` and `L<=r+D-1`, so the labels below fit on `[n]`.
Choose

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+2,        \tag{1.2}
\]

put `F=H-K`, and cyclically order the `L` elements of `F` as
`f_0,...,f_(L-1)`.  Use the source ring

\[
                         A_t=K\cup\{f_t\}.                 \tag{1.3}
\]

### Theorem 1.1 (all-parity two-hole ring)

The successive length-`D` source windows of (1.3) form one balanced
order-`d` de Bruijn component for every parity of `L`.  Its owner,
immediate-lower, and immediate-upper resources are

\[
 \begin{aligned}
 O_t&=K\cup\{f_t,\ldots,f_{t+D-1}\},\\
 Q_t&=O_t\cap O_{t+1}
     =K\cup\{f_{t+1},\ldots,f_{t+D-1}\},\\
 U_t&=O_t\cup O_{t+1}
     =K\cup\{f_t,\ldots,f_{t+D}\}.
 \end{aligned}                                             \tag{1.4}
\]

The `L` values in each of the three rows are pairwise distinct, of ranks
`r`, `r-1`, and `r+1`, respectively.  The owners form a simple Johnson
cycle.  At every proper source width, the `L` interval unions are likewise
pairwise distinct.

#### Proof

Every cyclic source word is a circulation under the one-letter de Bruijn
shift.  Since `D<L`, a length-`D` window in (1.3) has the first form in
(1.4), and shifting it deletes one private label and inserts one.  The
intersection and union formulas follow.  Their private parts are cyclic
intervals of lengths `D`, `D-1`, and `D+1`, all strictly between zero and
`L=D+2`; hence each interval recovers its start phase.  The same argument
works at every source width below `D`.  \(\square\)

The period `D+2` is sharp for upper simplicity in this common-core class.
At period `D+1`, every consecutive owner union is the whole packet top
`H`; at period `D+2`, the `D+1`-intervals in (1.4) are distinct.

## 2. Exact packet degrees

Treat reversal-equivalent cyclic orders as one packet.  Let

\[
 \mathcal O={ [n]\choose r},\qquad
 \mathcal Q={ [n]\choose r-1},\qquad
 \mathcal U={ [n]\choose r+1},\qquad
 W=|\mathcal O|=|\mathcal Q|.                              \tag{2.1}
\]

### Theorem 2.1 (owner and lower-root degree)

Every owner and every immediate-lower root occurs in exactly

\[
 \boxed{
 D_0=\binom{r-1}{2}\binom rD D!
    =3\binom r3\binom{r-1}{D-1}(D-1)! .}                   \tag{2.2}
\]

The total packet count is

\[
                         |\mathcal P|={W D_0\over L}.       \tag{2.3}
\]

For every incident pair `Q subset O`,

\[
                         {d(O,Q)\over D_0}={2\over r}.      \tag{2.4}
\]

#### Proof

Fix an owner `O`.  Choose the two labels of `H-O` in `binom(r-1,2)`
ways, choose `K subset O` in `binom(r,D)` ways, and cyclically order the
private set so that the two missing labels form a cyclic interval.  Treat
that ordered two-set as one block: there are `2! D!/2=D!` unoriented
orders.  This gives the first expression in (2.2).

Fix a root `Q`.  Choose the three labels of `H-Q` in `binom(r,3)` ways,
choose `K subset Q` in `binom(r-1,D-1)` ways, and force the three missing
labels to form a cyclic interval.  There are

\[
                         {3!(D-1)!\over2}=3(D-1)!
\]

unoriented orders, giving the second expression.  The two expressions
agree by cancellation.  Equation (2.3) follows by owner--packet incidence
counting.

For fixed `Q subset O`, choose the two labels of `H-O`, choose
`K subset Q`, and place the two missing labels as an ordered adjacent block
beside the unique label of `O-Q`.  The count is

\[
 \binom{r-1}{2}\binom{r-1}{D-1}2!(D-1)!,
\]

whose ratio to (2.2) is `2/r`.  \(\square\)

### Theorem 2.2 (upper degree and sharp oversupply)

Every rank-`r+1` upper target occurs in exactly

\[
 \boxed{
 D_U=(r-2)\binom{r+1}{D+1}{(D+1)!\over2}
     ={r+1\over r-1}D_0.}                                 \tag{2.5}
\]

For every incident pair `O subset U`,

\[
                         {d(O,U)\over D_0}={2\over r-1}.    \tag{2.6}
\]

#### Proof

Fix `U`.  Choose the extra label of `H-U` in `r-2` ways, choose
`K subset U` in `binom(r+1,D+1)` ways, and cyclically order the `L`
private labels.  The target `U` is obtained by omitting its unique extra
label, so every unoriented cyclic order contributes once.  This gives the
first expression in (2.5); direct cancellation gives the second.

For fixed `O subset U`, choose `H-U`, choose `K subset O`, and require the
two labels of `H-O` to be adjacent.  The count is

\[
                         (r-2)\binom rD D!,
\]

which is `2D_0/(r-1)`.  \(\square\)

## 3. Fractional three-shore factor

### Corollary 3.1

Give every packet weight `1/D_0`.  Then every owner and every immediate-
lower root has load exactly one, while every immediate-upper target has
load

\[
                            {D_U\over D_0}={r+1\over r-1}.  \tag{3.1}
\]

Mark every upper occurrence with the common fraction

\[
                            {r-1\over r+1}.                 \tag{3.2}
\]

The marked packet family is an exact fractional factor on all three
shores.

The excess before marking is only

\[
                            {2\over r-1}=O(r^{-1}).         \tag{3.3}
\]

per upper target.  It is the unavoidable shore-size ratio: every packet
has `L` owners and `L` uppers, while

\[
                         |\mathcal U|={r-1\over r+1}W.      \tag{3.4}

\]

Thus the all-parity two-hole family has no fractional owner, lower-q1, or
upper-q1 separator.  Its remaining difficulty is integral correlation:
select owner-disjoint packets, choose their cyclic orders and upper marks
without collisions, decorate their deeper pull profiles, and fuse the
resulting state components.
