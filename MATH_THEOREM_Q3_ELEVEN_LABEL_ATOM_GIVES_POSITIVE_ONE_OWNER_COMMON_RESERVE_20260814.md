# The eleven-label q3 atom gives a genuine positive one-owner common reserve

**Date:** 2026-08-14
**Status:** exact positive owner theorem for `q=3`, conditional only on the
explicit ambient-size/packing inequalities below.  All components are legal
closed rails and both final states are owner matchings.  Typed q1/q2 banks,
residence and global topology remain separate.

## 0. Setup

Put

\[
 q=3,\qquad R=c+3,\qquad M=k-c,\qquad N=M-2,             \tag{0.1}
\]

and assume

\[
 c\ge4,\qquad M\ge\max\{13,c+2\},\qquad
 {N\choose3}>6(N+1)^2.                                \tag{0.2}
\]

Choose a `(c-1)`-set `C_0`, disjoint reduced labels
`V={0,1,...,10}`, and put

\[
 C=C_0\cup\{0\},\qquad P=\{1,2,3\},\qquad
 H=C_0\cup\{0,1,2,3\}=C\cup P.                       \tag{0.3}
\]

Let `A^+,A^-` be the four-by-four atom from
`MATH_THEOREM_Q3_FOUR_BY_FOUR_NEAR_C_ATOM_ON_ELEVEN_LABELS_20260814.md`,
lifted by `C_0`.  Its exact named-owner identity is

\[
 \sum_{Q\in\mathcal A^+}f(Q)
 =\sum_{Q\in\mathcal A^-}f(Q)+e_H,                    \tag{0.4}
\]

with 34 simple positive owners and 33 simple negative owners.

## 1. An insertion pair meeting the atom only at H

There are at least three labels outside `C_0 union V` by `(0.2)`; choose
distinct fresh labels `alpha,beta,gamma`.  With core `C`, take the old and
new toggle words

```text
sigma^- = 2 3 alpha 4 5 beta 6 gamma                 (period 8)
sigma^+ = 1 2 3 alpha 4 5 beta 6 gamma               (period 9).
```

Thus `1` is inserted in the cut immediately before `2`.  Write the two
rails as `Q_Delta^-`, `Q_Delta^+` and put

\[
                 \Delta=f(Q_\Delta^+)-f(Q_\Delta^-). \tag{1.1}
\]

The insertion identity gives

\[
                       P_R\Delta={\bf1}_C+3e_1.      \tag{1.2}
\]

The cyclic three-windows are worth recording.  In the old word they are

```text
23alpha, 3alpha4, alpha45, 45beta,
5beta6, beta6gamma, 6gamma2, gamma23;
```

in the new word they are

```text
123, 23alpha, 3alpha4, alpha45, 45beta,
5beta6, beta6gamma, 6gamma1, gamma12.
```

Hence `H` is the sole insertion owner containing no fresh label.  Every
other owner in either insertion deck contains one of
`alpha,beta,gamma` and therefore cannot collide with either atom shore.
In particular,

\[
 \mathcal D(\mathcal A^+)\cap\mathcal D(Q_\Delta^-)=\varnothing,
 \qquad
 \mathcal D(\mathcal A^-)\cap\mathcal D(Q_\Delta^+)=\varnothing. \tag{1.3}
\]

## 2. The q3 point-correction star

Choose a `(c+1)`-set `S` disjoint from `C` and containing `P`, choose
`z` outside `C union S`, and put

\[
                     E=[k]\setminus(S\cup\{z\}),qquad |E|=N. \tag{2.1}
\]

For `u in {1,2,3}`, a star insertion potential has the form

\[
 \Phi_u=f(S-u,E+z,\tau_u^+)-f(S-u,E,\tau_u),         \tag{2.2}
\]

where `tau_u^+` inserts `z` into the cyclic order `tau_u`.  Its periods
are `N+1` and `N`, and

\[
                      P_R\Phi_u={\bf1}_S-e_u+3e_z.  \tag{2.3}
\]

Choose two copies `Phi_1^(2),Phi_1^(3)` with their period-`N` decks
disjoint and their period-`N+1` decks disjoint.  The standard random-order
greedy bound for the second copy is

\[
 {N^2\over{N\choose3}}+{(N+1)^2\over{N+1\choose3}}<1             \tag{2.4}
\]

under `(0.2)`.  Choose arbitrary leaf potentials `Phi_2,Phi_3`; different
star cores are signature-disjoint.  Put

\[
 K=(\Phi_1^{(2)}-\Phi_2)+(\Phi_1^{(3)}-\Phi_3),
 \qquad Y_H=\Delta+K.                               \tag{2.5}
\]

Equations `(1.2)` and `(2.3)` give

\[
                         P_RY_H={\bf1}_H.           \tag{2.6}
\]

The two raw component shores are

\[
\begin{aligned}
 \mathcal Y^+=\{&Q_\Delta^+,
   (\Phi_1^{(2)})^+,(\Phi_1^{(3)})^+,
   (\Phi_2)^-,(\Phi_3)^-\},\\
 \mathcal Y^-=\{&Q_\Delta^-,
   (\Phi_1^{(2)})^-,(\Phi_1^{(3)})^-,
   (\Phi_2)^+,(\Phi_3)^+\}.
                                                               \tag{2.7}
\end{aligned}
\]

They are owner matchings.  The repeated centre decks were packed in
`(2.4)`; different star cores are disjoint; and an insertion owner contains
the `c`-core `C`, whereas a star owner contains the disjoint `c`-core
`S-u`.  Since `2c>c+3`, the insertion and star decks cannot meet.  The
owner `H` occurs once in `Y^+`, in `Q_Delta^+`, and nowhere else.

For the boundary `c=4`, choose every small star order so the three labels
of `C_0` are not a cyclic consecutive triple.  Inserting `z` cannot create
a new consecutive triple of old labels.  The two repeated-centre orders
can still be packed: for a random second order, add

\[
 {N\over{N\choose3}}
\]

to the failure probability in `(2.4)`; `(0.2)` makes the resulting sum
less than one.  Thus the order restriction is compatible with the packing.

## 3. Complete atom/macro collision audit

Every atom owner contains `C_0`.  Every star owner contains a core `S-u`
of size `c`, disjoint from `C_0`.  If `c>=5`, equality of an atom owner and
a star owner would force a rank-`(c+3)` set to contain a union of size

\[
                  |C_0|+|S-u|=2c-1>c+3,             \tag{3.1}
\]

which is impossible.

At `c=4`, equality in `(3.1)` is possible numerically.  It would force the
star core `S-u` to be the four reduced labels of the atom owner and the
star toggle three-window to be exactly `C_0`.  The nonconsecutive-order
condition in Section 2 excludes precisely this event in both the small and
enlarged star cycles.

Together with `(1.3)`, this proves that the matching shore `A^+` is
disjoint from `Y^-`, and `A^-` is disjoint from `Y^+`.

## 4. Genuine positive common reserve

Remove the unique compulsory owner from the positive macro shore and put

\[
 \mathcal B^+=\sum_{Q\in\mathcal Y^-}f(Q),\qquad
 \mathcal B^-=\sum_{Q\in\mathcal Y^+}f(Q)-e_H.       \tag{4.1}
\]

These are simple, equal-size owner matchings with equal point degrees.
Define

\[
             \boxed{R_H=\sum_{Q\in\mathcal A^+}f(Q)}.          \tag{4.2}
\]

Then `R_H` is a nonnegative simple 34-owner vector, itself the union of
four legal closed rails, and

\[
\begin{aligned}
 \mathcal B^++R_H
   &=\sum_{Q\in\mathcal Y^-}f(Q)
     +\sum_{Q\in\mathcal A^+}f(Q),\\
 \mathcal B^-+R_H
   &=\sum_{Q\in\mathcal Y^+}f(Q)
     +\sum_{Q\in\mathcal A^-}f(Q).                 \tag{4.3}
\end{aligned}
\]

Both right sides are sums of nine pairwise owner-disjoint legal closed
rails.  The first state's periods are

```text
macro:   8,N,N,N+1,N+1       atom: 8,8,9,9;
```

the second state's periods are

```text
macro:   9,N+1,N+1,N,N       atom: 9,8,8,8.
```

Each state has exactly `4N+44` owners.  Thus `(4.2)` is a genuine positive
common reserve for the q3 insertion/star one-owner macro, not a signed
lattice identity.

## 5. Protected atom placement

The literal auxiliary labels `4,...,10` may be relabelled.  Fix `C_0` and
the target labels `0,1,2,3`, let `X` be an available pool of `L>=7`
auxiliary labels, and let `F` be a forbidden owner bank not containing `H`.  Only
members of `F` containing `C_0` can meet the lifted atom; let their number
be `F_0`.

In the 34-owner atom deck, the number of owners using respectively
`0,1,2,3` auxiliary labels is

```text
1, 7, 16, 10.
```

The zero-auxiliary owner is exactly `H`.  A uniformly random injection of
the seven abstract auxiliary labels into `X` therefore has expected
forbidden collisions at most

\[
 {7F_0\over L}+{16F_0\over{L\choose2}}
              +{10F_0\over{L\choose3}}.             \tag{5.1}
\]

If `(5.1)<1`, some injection avoids `F` completely.  This is an external
owner-bank placement criterion for both shores, because the negative atom
deck is a subset of the positive deck.  It does not claim simultaneous
avoidance of typed q1/q2 resources.

## 6. What does not inflate automatically

Adding a fixed label to the core of every displayed rail lifts ambient rank
but leaves the toggle width equal to three.  It is not a `q -> q+1`
recurrence.  Nor can one suspend the atom by demanding one new toggle label
in every window: in a legal period-`T` rail a toggle occurs in exactly `q`
of the `T>=2(q+1)` windows, never all of them.  A block concatenation also
creates new seam-crossing windows not present in the old owner identity.

Thus the V11 atom gives a complete positive q3 common reserve and a base
case for any future inflation, but no direct one-label or naive three-block
tensor currently promotes it to all `q`.
