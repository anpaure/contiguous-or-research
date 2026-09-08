# Full token-orbit links are maximally matchable; only color competition remains

**Status (2026-08-21).**  Every theorem below is proved.  In the tokenwise
orbit relaxation of the clustered product bank, each fixed
payload/phase-type link has the largest matching allowed by its three scalar
shore sizes.  The full relaxation is exactly a color-capacitated matching
problem in a Boolean containment graph.  Thus the determinant-two face of
the bare incidence matrix does not create a one-color obstruction; all
remaining difficulty comes from competition among phase types and from the
later requirement that tokenwise label choices arise from common cyclic
orders.

No theorem below says that the full color-capacitated graph has a
near-perfect matching.  Small exact optimizations reported at the end are
evidence only.

## 1. One phase type

Let `A,B` be disjoint `b`-sets.  Fix an upper offset `q`, a payload split
`r`, and a number `z` of new `A`-letters, and put

\[
 s=r+z,
 \qquad 0\le z\le q,
 \qquad q\le r,b-r.                                  \tag{1.1}
\]

The source and target shores are

\[
 \mathcal U_r=
 \{U:|U\cap A|=r, |U\cap B|=b-r\},
\]

\[
 \mathcal V_{q,s}=
 \{V:|V\cap A|=s, |V\cap B|=b+q-s\}.               \tag{1.2}
\]

Join `U` to `V` when `U subset V`.  Put

\[
 L_r=|\mathcal U_r|={b\choose r}^2,
 \qquad
 R_{q,s}=|\mathcal V_{q,s}|={b\choose s}{b\choose s-q}. \tag{1.3}
\]

The clustered phase multiplicity is

\[
 n_{r,q,z}=
 \begin{cases}
 b-r-q+1,&z=0,\\
 2,&1\le z\le q-1,\\
 r-q+1,&z=q,
 \end{cases}                                         \tag{1.4}
\]

and the number of physical occurrence tokens of this type is

\[
 Q_{r,q,z}={n_{r,q,z}\over b}{b\choose r}^2.         \tag{1.5}
\]

Under the prime-`b` product-factor hypothesis this is an integer: it is the
number of contributing phases times `b` counter points times
`(binom(b,r)/b)^2` order pairs.

### Lemma 1.1 (exact biregular link)

The containment graph between (1.2) is biregular.  Its left and right
degrees are

\[
 d_L={b-r\choose z}{r\choose q-z},
 \qquad
 d_R={s\choose r}{b+q-s\choose b-r},                 \tag{1.6}
\]

and

\[
 L_rd_L=R_{q,s}d_R.                                  \tag{1.7}
\]

#### Proof

From a source, choose the `z` added letters in `A\setminus U` and the
`q-z` added letters in `B\setminus U`.  From a target, choose its source
parts of sizes `r` and `b-r`.  This proves (1.6), and counting containment
flags from the two shores proves (1.7).  \(\square\)

### Theorem 1.2 (one-type orbit matching is optimal)

Let `\mathcal O_(r,q,z)` be a set of `Q_(r,q,z)` token vertices and form the
three-partite token-orbit hypergraph

\[
 \{(o,U,V):o\in\mathcal O_{r,q,z},\ U\in\mathcal U_r,
       \ V\in\mathcal V_{q,s},\ U\subset V\}.        \tag{1.8}
\]

Its matching number is

\[
 \boxed{\min(Q_{r,q,z},L_r,R_{q,s})
        =\min(Q_{r,q,z},R_{q,s}).}                    \tag{1.9}
\]

#### Proof

The three shore sizes give the upper bound.  A biregular bipartite graph has
a matching saturating its smaller shore: if `X` lies on the left, edge
counting gives

\[
 d_L|X|\le d_R|N(X)|,
\]

and (1.7) proves Hall on the smaller side; interchange the shores when
needed.  Take the required number of edges from such a containment matching
and assign them distinct token vertices.  Finally `Q_(r,q,z)<=L_r` because
`n_(r,q,z)<=b`.  \(\square\)

## 2. Exact reduction of the full tokenwise orbit relaxation

Fix `q`.  Let `G_q` be the bipartite containment graph whose left shore is
the disjoint union of the admissible `\mathcal U_r` and whose right shore is
the rank-`(b+q)` targets.  Color an edge `U subset V` by

\[
 \kappa(U,V)=(r,z),qquad
 r=|U\cap A|,\quad z=|V\cap A|-r.                   \tag{2.1}
\]

Give color `(r,z)` capacity `Q_(r,q,z)` from (1.5).

### Theorem 2.1 (token rows collapse exactly to color capacities)

Matchings in the full tokenwise orbit hypergraph are in size-preserving
correspondence with matchings `M` in `G_q` satisfying

\[
 |M\cap E_{r,z}|\le Q_{r,q,z}
 \quad\hbox{for every }(r,z).                         \tag{2.2}
\]

#### Proof

Project a hyperedge `(o,U,V)` to the containment edge `UV`.  Distinct middle
and upper vertices make the projected edges a graph matching, and distinct
tokens of one type give (2.2).  Conversely, for every color, inject its
selected graph edges into the `Q_(r,q,z)` available tokens.  The resulting
triples are disjoint.  \(\square\)

Thus token identities themselves create no further obstruction.  The first
unsolved relaxation is a matching in `G_q` with the cell capacities (2.2).
The determinant-two witness in
`MATH_BARRIER_CLUSTERED_TOKEN_LABEL_COINSTANTIATION_NONTU_20260821.md`
shows that its obvious three-family incidence formulation is not totally
unimodular, even though every one-color link is optimal by Theorem 1.2.

## 3. Exact local switches

Token assignments can always be permuted after a graph switch, so local
augmentation is governed by containment cycles.

For `q>=2`, whenever two targets `V_1,V_2` have an intersection containing
two distinct admissible middle sources `U_1,U_2`, the four containments form
the switch

\[
 U_1V_1, U_2V_2
 \quad\longleftrightarrow\quad
 U_1V_2, U_2V_1.                                    \tag{3.1}
\]

If the targets have the same split profile, (3.1) preserves both edge
colors and therefore every capacity in (2.2).  Central target pairs differing
by one same-side letter have intersection size `b+q-1>=b+1` and supply many
such switches.

At `q=1` the rank-`b` to rank-`(b+1)` containment graph has no four-cycle:
two distinct upper targets have at most one common rank-`b` subset.  Its
smallest switches are six-cycles.  For the next-`A` type, fix a
`(r-1)`-set `C subset A`, a `(b-r)`-set `D subset B`, and distinct
`x,y,z in A\setminus C`.  The alternating cycle is

\[
 (C+x)\cup D
 \;--\;(C+x+y)\cup D
 \;--\;(C+y)\cup D
 \;--\;(C+y+z)\cup D
 \;--\;(C+z)\cup D
 \;--\;(C+z+x)\cup D
 \;--\;(C+x)\cup D.                                  \tag{3.2}
\]

The next-`B` analogue is obtained by interchanging the sides.  These cycles
show that the full link has genuine augmentation unavailable in the
restricted determinant-two face.  They do not by themselves prove global
expansion under all color capacities.

## 4. Finite evidence and remaining gate

The focused H100 script cited below solves the complete color-capacitated
binary integer program for the following small prime cases.  In every case
the integral optimum equals the scalar bound
`sum_s min(P_(q,s),T_(q,s))`:

\[
\begin{array}{c|c|c}
(b,q)&\hbox{integral optimum}&\hbox{scalar bound}\\ \hline
(5,1)&190&190\\
(5,2)&120&120\\
(7,1)&2828&2828\\
(7,2)&2002&2002.
\end{array}                                           \tag{4.1}
\]

These computations are evidence, not an asymptotic theorem.  The exact open
question at the tokenwise-orbit level is whether the dense
color-capacitated graph (2.2) always has a matching missing only the proved
`O(W_b b^{-1/4})` scalar deficit, up to `o(W_b)` additional loss.  Even a
positive answer would still have to be lifted from independently assignable
orbit tokens to common tight-cycle orders across ranks and offsets.
