# Persistent pentagon companion edges are not pairwise all-width current-isomorphic

## Status

The suffix-suspended anchored `D_3` pentagon exposes the phase matchings

\[
                  M^- =\{12,54\},\qquad M^+=\{14,32\},
\]

whose union is connected.  This note tests the shortest possible guarded
reuse mechanism: cancel one native move in one phase against one native move
in the other phase.

No cross-phase edge pair has the same complete all-width current once the
tail is nonempty.  Edges `54` and `32` have opposite immediate-upper current,
but leave one explicit nested square at every intermediate width.  Edges
`12` and `14`, despite having identical ordered banks, use different active
endpoint pairs and already fail at q1.

Thus the pentagon closes companion-edge creation and connectedness, but not
reusable zero-current loops.  A longer multi-edge cocycle or a separate halo
router is still required.

No computation or search is used.

## 1. Current notation

Put `m=s+3`, and let

\[
             U=(u_1,\ldots,u_s),\qquad
             V=(v_1,\ldots,v_s)
\tag{1.1}
\]

be the common deletion and insertion tail banks.  For a word `Z`, write
`Z_j^-` and `Z_j^+` for its prefix and suffix of length `j`.

For ordered banks `|X|=m-2`, `|Y|=m-1`, define the proper
length-`j+1` current

\[
\begin{aligned}
 \mathcal D_j(X,Y;a,d)={}&
 [Y_j^++d]+[Y_j^-+a]-[Y_j^++a]-[Y_j^-+d]\\
 &+[X_j^-+a]+[X_j^++d]-[X_j^-+d]-[X_j^++a].
\end{aligned}                                           \tag{1.2}
\]

The all-width inverse-pair theorem proves that (1.2) is the complete signed
current for `0<=j<=m-2`.  It is antisymmetric in the active endpoints:

\[
                 \mathcal D_j(X,Y;d,a)
                    =-\mathcal D_j(X,Y;a,d).           \tag{1.3}
\]

## 2. The four persistent edge currents

Reading the exact normal forms in the companion theorem gives

\[
\begin{array}{c|c}
12&\mathcal D_j(V\infty,1U6;4,3)\\
54&\mathcal D_j(U2,V\infty1;4,5)\\
14&\mathcal D_j(V\infty,1U6;5,2)\\
32&\mathcal D_j(U3,V\infty1;5,4).
\end{array}                                             \tag{2.1}
\]

In particular, `12` and `14` have the same two ordered banks, but their
active endpoint pairs are `(4,3)` and `(5,2)`.  Equality of banks does not
make their currents equal.

## 3. The q1 filter

At q1, `j=m-2=s+1`, the `X` rectangle vanishes.  For the common bank

\[
                         Y_A=(1,U,6),
\]

the two currents are

\[
\begin{aligned}
 C_{12}^{q1}={}&[U63]+[U14]-[U64]-[U13],\\
 C_{14}^{q1}={}&[U62]+[U15]-[U65]-[U12].              \tag{3.1}
\end{aligned}
\]

Their supports are disjoint, so they are neither equal nor opposite.

For

\[
 W=(v_2,\ldots,v_s,\infty),
\]

with the evident interpretation `W=(infinity)` when `s=1`, the other two
q1 currents are

\[
\begin{aligned}
 C_{54}^{q1}={}&[W15]+[v_1W4]-[W14]-[v_1W5],\\
 C_{32}^{q1}={}&[W14]+[v_1W5]-[W15]-[v_1W4]
                =-C_{54}^{q1}.                       \tag{3.2}
\end{aligned}
\]

The q1 cores in (3.1) and (3.2) use disjoint tail banks.  Hence no crossed
pair among `12,54` and `14,32` has equal or opposite q1 current, except for
the anti-pair `54,32` in (3.2).

## 4. Exact deeper residual of the q1 anti-pair

Use the same orientation on edges `54` and `32`.  Their `Y` rectangles
cancel at every width by (1.3), because they have the same `Y` bank and
reversed active endpoints.  The `X` banks differ only in their terminal
labels `2,3`.

For `1<=j<=s`, let

\[
                       T_j=(u_{s-j+2},\ldots,u_s)
\tag{4.1}
\]

be the suffix of `U` of length `j-1`, empty at `j=1`.  Direct cancellation
in (1.2) gives

\[
\boxed{
 C_{54,j}+C_{32,j}
   =[T_j25]+[T_j34]-[T_j24]-[T_j35].}                 \tag{4.2}
\]

At `j=0` and `j=s+1` the sum is zero.  For every `1<=j<=s`, the four sets
in (4.2) are distinct, so the residual is nonzero.

### Theorem 4.1 (no two-edge all-width cancellation)

For every nonempty common tail, no edge of `M^-` is literal-current
isomorphic to an edge of `M^+`, with either sign, at all widths
simultaneously.

#### Proof

Equation (3.1) rules out `12` paired with `14`.  The distinct q1 tail cores
rule out the two crossed pairings.  Equation (3.2) leaves only `54` paired
with `32`; (4.2) rules it out at every intermediate width. \(\square\)

In particular, the proposed excursion consisting of a negative `12` loop
and the transported inverse positive `14` loop does **not** have zero
current.  The formal row action `(g_2,g_4^{-1})` is therefore not yet a
guard-safe physical generator.

### Corollary 4.2 (the four fixed unit currents are independent)

Over both `Z` and `Q`, the complete all-width current vectors of

\[
                         12,54,14,32
\]

are linearly independent.

#### Proof

At q1, the supports of `C_12` and `C_14` are disjoint from one another and
from the `V`-core support of `C_54,C_32`.  Hence a zero relation forces the
coefficients of `12,14` to vanish.  Equation (3.2) then forces the
coefficients of `54,32` to be equal.  At any intermediate width,
equation (4.2) forces that common coefficient to vanish. \(\square\)

Thus even a signed multiset using all four **fixed time-zero unit slots**
cannot close the all-width current.  A successful longer word must first
change a slot/current, or must use an exterior absorber.

## 5. Group-theoretic scope

At the level of one native move per phase, Theorem 4.1 leaves no nontrivial
zero-current edge-difference generator.  Consequently the perfect-group
commutator argument cannot yet be invoked without additional current
absorption.

This is not a no-go against longer dynamic words, because later moves may
occur at newly exposed slots with different currents.  The residuals (4.2)
are nested elementary squares, exactly the kind of cocycles that may cancel
after such slot transport.  The next sharp statement is:

> **Pentagon dynamic current-circuit lemma.**  Starting from the four
> persistent edges, expose additional slots during the word so that the
> total nested-rail current is zero, the phase transports close, and the net
> row action is nontrivial.

A positive lemma would turn the already-connected phase union into reusable
guarded control.  Absent it, a bounded external halo router must absorb the
explicit squares (3.1) and (4.2).
