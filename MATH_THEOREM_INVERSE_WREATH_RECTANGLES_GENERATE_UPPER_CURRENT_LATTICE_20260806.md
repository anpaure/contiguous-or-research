# Inverse-wreath rectangles generate the abstract upper-current lattice

## Status

The native inverse-pair wreath substitution has signed immediate-upper
current equal to one distance-two `2 x 2` rectangle.  This note proves the
converse: **every** distance-two upper rectangle is the current of an
explicit inverse-pair wreath substitution.  Consequently, after allowing
the catalytic reserve rows from the distance-two factorization theorem,
inverse-pair wreath currents generate the complete integer fixed-coordinate
current lattice.

This is a palette-level and prospective-row theorem.  It does not assert
that all required row pairs coexist in one wreath factor, that the canonical
MSW inverse-pair subcatalogue has full span, or that widths at least two are
preserved.

No computation or search is used.

## 1. Every distance-two rectangle is one inverse-wreath current

Put

\[
                         N=2m+1,
 \qquad                 k=m+2,
 \qquad                 m\ge3.                       \tag{1.1}
\]

Let `K` be an `m`-set, and choose four distinct labels

\[
                         a,d,u,v\notin K.              \tag{1.2}
\]

The associated distance-two rectangle on rank-`k` sets is

\[
 \begin{aligned}
 \partial(K;a,d;u,v)
   ={}&[K+d+u]+[K+a+v]\\
      &-[K+a+u]-[K+d+v].                              \tag{1.3}
 \end{aligned}
\]

Choose distinct `b,c in K`, order

\[
                         X=K-\{b,c\},                  \tag{1.4}
\]

and order the remaining `m-1` ground labels as

\[
                         Y=(v,y_2,\ldots,y_{m-2},u).   \tag{1.5}
\]

Define the two old and two new cyclic coordinate orders

\[
 \begin{aligned}
 r_0&=(a,b,X,c,d,Y),&
 r_1&=(b,d,X,a,c,Y),\\
 r'_0&=(b,a,X,d,c,Y),&
 r'_1&=(d,b,X,c,a,Y).                                \tag{1.6}
 \end{aligned}
\]

### Theorem 1.1 (surjectivity onto physical rectangles)

The substitution `(r_0,r_1) -> (r'_0,r'_1)` preserves the complete
length-`m` and length-`(m+1)` interval palettes.  Its complete signed
length-`(m+2)` palette current is exactly

\[
                         \partial(K;a,d;u,v).          \tag{1.7}
\]

Hence every palette-nontrivial physical Boolean `C6` rectangle has an
explicit two-wreath inverse-pair realization which preserves both central
shores and is biresident at every deadline at most `m-1`.

#### Proof

The central-palette equality and residence are Theorem 1.1 and Proposition
4.1 of
`MATH_THEOREM_MSW_INVERSE_PAIR_Q1_BIRAIL_CURRENT_20260806.md`.
It remains only to identify its current.

Write

\[
 Y^- =Y-\{u\},\qquad Y^+=Y-\{v\}.                    \tag{1.8}
\]

The inverse-pair current is

\[
 [\overline{Y^-+a}]+[\overline{Y^++d}]
 -[\overline{Y^-+d}]-[\overline{Y^++a}].             \tag{1.9}
\]

By construction, the complement of `Y^-` is `K+a+d+u`, and the
complement of `Y^+` is `K+a+d+v`.  Therefore the four terms in (1.9) are,
in order,

\[
 K+d+u,\qquad K+a+v,\qquad K+a+u,\qquad K+d+v.
\]

This is (1.3).  The last assertion follows from the exact comparison
between distance-two palette rectangles and Boolean incidence `C6`s.
\(\square\)

The choices of `b,c`, the orders of `X`, and the internal order of `Y`
show that one abstract rectangle has many prospective wreath realizations.
This multiplicity is not a neighbourhood count inside a fixed factor.

## 2. One fixed core has no further lattice invariant

Fix `K` and let

\[
                         V=[N]-K,
 \qquad                 |V|=m+1.                    \tag{2.1}
\]

Identify the rank-`(m+2)` targets containing `K` with the edges of the
complete graph on `V`:

\[
                         K+x+y\longleftrightarrow xy. \tag{2.2}
\]

Let `z` be an integer vector on these targets.  Its coordinate current on
`V` is the ordinary unsigned edge-degree vector

\[
                         d_z(x)=\sum_{y\ne x}z_{xy}.   \tag{2.3}
\]

### Theorem 2.1 (fixed-core birail lattice)

For `m>=3`, every integer vector `z` satisfying

\[
                         d_z(x)=0\qquad(x\in V)        \tag{2.4}
\]

is an integer combination of currents (1.3) with the same fixed core
`K`.

#### Proof

We give an integer elimination proof, which also covers alternating closed
walks whose support is a pair of odd cycles and therefore avoids an
unjustified simple-cycle decomposition.

Induct on `|V|`.  The assertion is trivial for `|V|<=3`, because the
unsigned vertex-edge incidence matrix of `K_3` has zero kernel.  Fix a
vertex `v`.  If some incident coefficient `z_(vx)` is positive, (2.4)
provides an incident edge `vy` with negative coefficient.  Choose
`w` distinct from `v,x,y`; this is possible for `|V|>=4`.  One signed
four-cycle on

\[
                         v,x,w,y,v                   \tag{2.5}
\]

has coefficient `+1` on `vx`, coefficient `-1` on `vy`, and coefficients
of opposite signs on `xw,wy`.  Subtract the appropriate positive multiple
of this four-cycle to reduce

\[
                         |z_{vx}|+|z_{vy}|            \tag{2.6}
\]

without changing any other edge incident with `v`.  Repeating eliminates
all edges at `v`.  (If the first nonzero incident coefficient is negative,
reverse the square.)

The remaining vector is supported on `K_(V-v)` and still has zero degree
at every remaining vertex.  The induction hypothesis decomposes it into
four-cycles.  Every four-cycle is exactly (1.3), and Theorem 1.1 realizes
it by an inverse-pair wreath substitution. \(\square\)

Thus the inverse-pair move is not merely one useful current: on every
fixed common-core fibre it is the complete integer Markov move.

## 3. Global current generation with catalytic rows

Let `P,Q` be two rank-`k` targets and consider an abstract Ryser switch

\[
                         (P,Q)\mapsto(P-x+y,Q-y+x).    \tag{3.1}
\]

The catalytic factorization theorem in
`MATH_THEOREM_CATALAN_DUPLICATE_CURRENT_RYSER_AND_PREPARED_C6_RADO_20260803.md`
proves that if

\[
                         t=|P-Q|\ge2,                 \tag{3.2}
\]

then (3.1) is a composition of `t-1` distance-two rectangles after adding
`t-2` labelled reserve rows, all of which return to their initial values.
Theorem 1.1 realizes every one of those rectangles as an inverse-wreath
pair.

### Corollary 3.1 (complete abstract upper-current generation)

Let `A,B` be two labelled multisets of rank-`(m+2)` targets with the same
number of rows and the same coordinate degrees.  After adjoining finitely
many catalytic rows which are restored at the end, there is a finite
sequence of inverse-pair wreath substitutions whose signed palette current
is `B-A`.

#### Proof

Ryser switching connects `A` to `B` by fixed-margin `2 x 2` switches.
Factor every palette-nontrivial switch into distance-two rectangles by the
catalytic theorem, and apply Theorem 1.1 to each rectangle.  Palette-trivial
row exchanges contribute zero current. \(\square\)

In particular, the cyclic Catalan duplicate multidesign from the cited note
is reachable from the upper palette of any two-perfect-matching central
factor at the level of signed palette algebra.  There is no remaining
scalar, coordinate-current, or distance obstruction.

## 4. The exact remaining physical theorem

The result deliberately changes the quantifier.  It proves

\[
 \text{desired balanced upper current}
 \quad\Longrightarrow\quad
 \text{a finite prospective list of inverse-wreath row pairs}. \tag{4.1}
\]

It does **not** prove that those pairs are simultaneously rows of one
owner/root-exact wreath factor.  Nor does it prove that their catalytic
rows have private occurrences.  The sharp next statement is therefore:

> **Inverse-pair factor-lifting theorem.**  Given a balanced upper-current
> decomposition into inverse-pair rectangles, choose a shortest-wreath
> factor containing occurrence-disjoint realizations of all noncancelling
> pairs and private occurrences of the catalytic rows, with only bounded
> terminal deficiency.

A positive theorem of that form closes the immediate-upper algebraic gate.
One must still protect widths at least two, join the resulting components,
and solve the terminal lower/common-cap assignment.  Those requirements
are not consequences of the present lattice theorem.
