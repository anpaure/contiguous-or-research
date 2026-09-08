# The cyclic-unmatched triangle normal form for Catalan pathization

**Date:** 2026-08-13  
**Status:** unconditional all-parameter structural reduction and exact
capacity obstruction.  The restricted three-choice family is impossible
for every `r>=14`, even before acyclicity.

## 0. Outcome

Fix \(r\ge2\), put \(n=2r-1\), and write

\[
 \mathcal L={ [n]\choose r-1},\qquad
 \mathcal M={ [n]\choose r},\qquad
 \mathcal U={ [n]\choose r+1}.
\tag{0.1}
\]

Cyclic parenthesis matching of every \(U\in\mathcal U\) leaves exactly three
unmatched one-positions.  Deleting two cyclically consecutive unmatched
ones gives three distinguished diamonds below `U`.

This restricted family has a much stronger structure than the full
diamond graph.

1. It is canonically a family of directed triangles on \(\mathcal L\).
2. The canonical map from lower colours to middle owners is a bijection.
3. Choosing one side of every triangle with distinct tails and heads
   already gives the physical degree-two condition.
4. In Dyck language, each side is an explicit root-child rotation.
5. More decisively, the restricted family cannot have physical maximum
   degree two for any \(r\ge14\), by an exact omission-capacity count.
6. Acyclicity is also not automatic: for every \(r\ge3\) the restricted family
   contains a rainbow directed `C_5` whose upper, lower, tail, and head
   labels are all distinct.

Thus the cyclic triangles give a very sparse Catalan normal form and a
successful small-parameter laboratory, but **not** an all-parameter
pathization route.  Any surviving construction must enlarge the three-side
menu so that high-degree lower vertices can be bypassed often enough.

## 1. Cyclic parenthesis matching

Interpret `0` as an opening parenthesis and `1` as a closing parenthesis,
and cancel cyclic noncrossing `01` pairs.  A word of length `n` and weight
`r+1` has three excess closings, so exactly three ones survive.  List them in cyclic
order as

\[
                     f_0,f_1,f_2.                  \tag{1.1}
\]

Equivalently there are unique Dyck words `P_0,P_1,P_2`, up to simultaneous
cyclic shift of the subscripts, such that the cyclic word is

\[
                     1P_0\,1P_1\,1P_2.             \tag{1.2}
\]

For indices modulo three define

\[
 L_i(U)=U\setminus\{f_i,f_{i+1}\},                 \tag{1.3}
\]

and let `e_i(U)` be the Johnson edge between

\[
 A_i(U)=L_i(U)+f_i,\qquad
 B_i(U)=L_i(U)+f_{i+1}.                             \tag{1.4}
\]

Then

\[
 \ell(e_i(U))=L_i(U),\qquad u(e_i(U))=U.           \tag{1.5}
\]

So every `e_i(U)` is a legal diamond having the required upper colour.

## 2. The canonical lower-to-middle bijection

A word \(L\in\mathcal L\) has one excess opening zero.  Cyclic parenthesis matching
therefore leaves a unique unmatched zero, denoted `z(L)`.  Define

\[
                    \tau(L)=L+z(L)\in\mathcal M.   \tag{2.1}
\]

### Lemma 2.1

The map

\[
                         \tau:\mathcal L\to\mathcal M
\tag{2.2}
\]

is a bijection.

#### Proof

A middle word has excess one `1`, so cyclic matching leaves a unique
unmatched one.  Deleting it is inverse to `(2.1)`: adding the unmatched
zero creates the unique unmatched one at the same position, while every
old noncrossing pair remains paired. \(\square\)

### Lemma 2.2 (directed-triangle identity)

Orient `e_i(U)` from `A_i(U)` to `B_i(U)`.  Then

\[
 \boxed{
 A_i(U)=\tau(L_i(U)),\qquad
 B_i(U)=\tau(L_{i+2}(U)).}
\tag{2.3}
\]

Consequently the three choices below one upper colour form the directed
triangle

\[
 L_0\longrightarrow L_2\longrightarrow L_1\longrightarrow L_0
\tag{2.4}
\]

after transporting middle owners back through `tau`.

#### Proof

In `L_i`, changing `f_i` from `1` to `0` leaves that position as the
unique cyclic unmatched zero; the interval between consecutive survivors
in `(1.2)` is Dyck and all its positions remain internally paired.  Hence
`tau(L_i)=L_i+f_i=A_i`.

The other endpoint is `B_i=U-f_i`.  But

\[
 L_{i+2}=U-\{f_{i+2},f_i\},
\]

and its unique unmatched zero is `f_{i+2}`.  Therefore

\[
 \tau(L_{i+2})=L_{i+2}+f_{i+2}=U-f_i=B_i.
\]

This gives the cyclic order `(2.4)`. \(\square\)

### Corollary 2.3 (no repeated sides)

No directed side occurs in two different upper triangles.

#### Proof

The physical endpoints of a side recover their union `U`, and within that
triangle `(2.3)` recovers its orientation and lower label. \(\square\)

## 3. Exact plane-tree/root-child normal form

Cut the cyclic word at `f_i`.  Formula `(1.2)` gives

\[
 U=1P_i\,1P_{i+1}\,1P_{i+2}.                       \tag{3.1}
\]

After deleting `f_i,f_{i+1}`, the unique unmatched zero of `L_i` is the
former position `f_i`.  Delete this zero and append a final closing step.
The resulting ordinary Dyck word is

\[
                  D_i=P_i\,0P_{i+1}1\,P_{i+2}.     \tag{3.2}
\]

Thus the triangle vertex `L_i` is a rooted plane tree in which the middle
Dyck block \(P_{i+1}\) is a distinguished root child.  Advancing around
`(2.4)` cyclically moves this root-child pointing through the three-block
decomposition.  The restricted pathization gate is therefore intrinsic to
rooted plane trees; it is not an arbitrary three-choice CSP.

The degree of a lower vertex in the undirected triangle complex is its
number of admissible root-child pointings.  Direct Catalan enumeration
gives, for \(1\le d\le r-1\),

\[
 \#\{L:\deg(L)=d\}
 =(2r-1)\frac{d}{2r-2-d}{2r-2-d\choose r-1-d}.     \tag{3.3}
\]

For example, at `r=7` the degree histogram is

\[
 1:546,\quad2:546,\quad3:364,\quad4:182,\quad5:65,\quad6:13.
\tag{3.4}
\]

Formula `(3.3)` follows by cutting the lower word at its unmatched zero,
writing the remaining length-`2r-2` Dyck word as a root with `d` children,
and applying the ballot coefficient formula (equivalently, Lagrange
inversion).  The factor \(2r-1\) restores the marked cyclic cut.  It also
explains why a raw local
greedy argument is delicate: the maximum triangle-complex degree grows
linearly with `r`.

## 4. Exact capacity no-go from `r=14`

Put

\[
 V=|\mathcal L|=|\mathcal M|,\qquad
 F=|\mathcal U|,\qquad
 N_d=|\{L\in\mathcal L:\deg(L)=d\}|.               \tag{4.1}
\]

Every upper triangle has three vertices, so

\[
 \sum_{d\ge1}dN_d=3F,\qquad \sum_{d\ge1}N_d=V.    \tag{4.2}
\]

Choosing one side of a triangle omits exactly one of its three lower
vertices.  Let `o_L` be the number of incident triangles whose selected
side omits `L`.  The selected physical degree at `tau(L)` is

\[
                         d(L)-o_L.                  \tag{4.3}
\]

Thus maximum degree two forces

\[
                         o_L\ge(d(L)-2)_+.          \tag{4.4}
\]

But there is only one omission per triangle, hence

\[
                         \sum_L o_L=F.              \tag{4.5}
\]

### Theorem 4.1 (sharp aggregate capacity obstruction)

The restricted cyclic-unmatched three-choice family has no one-side-per-
upper selection of physical maximum degree at most two for any \(r\ge14\).
This remains true if lower-colour injectivity and acyclicity are discarded.

#### Proof

The demand in `(4.4)` is

\[
\begin{aligned}
 R&:=\sum_{d\ge3}(d-2)N_d\\
  &=\sum_d dN_d-2\sum_dN_d+N_1\\
  &=3F-2V+N_1.                                     \tag{4.6}
\end{aligned}
\]

Since `V-F=Cat_r`, the available omission margin is

\[
 F-R=2\operatorname{Cat}_r-N_1.                   \tag{4.7}
\]

Formula `(3.3)` at `d=1` gives

\[
 N_1=\frac{2r-1}{2r-3}{2r-3\choose r-2},\qquad
 \frac{N_1}{\operatorname{Cat}_r}
 =\frac{r(r+1)}{4(2r-3)}.                          \tag{4.8}
\]

Therefore

\[
 \boxed{
 F-R=\operatorname{Cat}_r
       \frac{-r^2+15r-24}{4(2r-3)}.}               \tag{4.9}
\]

The quadratic numerator is negative exactly for integral \(r\ge14\) in the
range \(r\ge2\).  Hence `R>F`, contradicting `(4.4)--(4.5)`. \(\square\)

At the threshold,

\[
 \operatorname{Cat}_{14}=2,674,440,\qquad
 F-R=-267,444.                                      \tag{4.10}
\]

So the first failure is not a delicate parity issue: the menu is short by
more than a quarter million mandatory local omissions.  At `r=13` the
margin is still positive but only `16,150`.

## 5. Exact restricted selector theorem

Let \(\mathscr T_r\) be the directed triangle family `(2.4)`, one triangle
for every \(U\in\mathcal U\).

### Theorem 5.1 (two-SDR pathization reduction)

Suppose one can choose one directed side

\[
                         x_U\longrightarrow y_U
\tag{5.1}
\]

from every triangle of \(\mathscr T_r\) so that

\[
 U\mapsto x_U\quad\hbox{and}\quad U\mapsto y_U
\tag{5.2}
\]

are both injective.  Then the corresponding Johnson graph has maximum
degree at most two and its lower colours are pairwise distinct.  If the
selected directed graph is acyclic, it is a Catalan linear forest with
exactly \(\operatorname{Cat}_r\) components.

#### Proof

By `(2.3)`, the physical edge is

\[
                         \tau(x_U)\tau(y_U).
\]

Tail and head injectivity give outdegree and indegree at most one at every
physical owner because `tau` is bijective.  Hence the undirected degree is
at most two.

Each selected lower colour is exactly its tail `x_U`, so tail injectivity
also gives distinct lower colours.  The upper colours are exact because
one side was selected from every `U`-triangle.  If there is no directed
cycle, a digraph with indegree and outdegree at most one is a disjoint
union of directed paths and isolated vertices.  Finally

\[
 |\mathcal M|-|\mathcal U|
 ={2r-1\choose r}-{2r-1\choose r+1}
 =\operatorname {Cat}_r,
\]

so Euler's identity gives the component count. \(\square\)

The two-SDR condition is slightly stronger than necessary.  The literal
degree-two condition allows two selected heads at a vertex provided that
the same vertex is not a selected tail.  The stronger form is preferable
because it isolates acyclicity as the only nonmatching condition.

### Corollary 5.2 (finite exact witnesses)

The restricted two-SDR pathization problem is feasible for every

\[
                         2\le r\le7.                \tag{5.3}
\]

In each case an acyclic first SAT model exists.  The census is

\[
\begin{array}{c|r|r|r|r}
r&|\mathcal U|&\text{distinct lower}&\text{distinct tail}&
\text{distinct head}\\ \hline
2&1&1&1&1\\
3&5&5&5&5\\
4&21&21&21&21\\
5&84&84&84&84\\
6&330&330&330&330\\
7&1287&1287&1287&1287
\end{array}                                                   \tag{5.4}
\]

These are finite certificates, not an all-parameter proof.  The replay is
implemented in
`scratch/audit_cyclic_unmatched_triangle_selector_20260813.py`.

## 6. Acyclicity is an independent gate

It is tempting to hope that a tail/head-injective side transversal of the
triangles is automatically acyclic.  This is false in every nontrivial
dimension.

### Theorem 6.1 (rainbow directed pentagon)

For every \(r\ge3\), \(\mathscr T_r\) contains a directed `5`-cycle whose five
upper labels, five lower labels, five tails, and five heads are all
pairwise distinct.

#### Proof for \(r\ge4\)

Let

\[
 Q=\{0,\ldots,r-4\},\qquad
 a=r-3,\quad b=r-2,\quad c=r-1,\quad d=r,\quad e=r+1. \tag{6.1}
\]

Choose the following five upper words and rules:

\[
\begin{array}{c|c|c|c}
U& (f_0,f_1,f_2)&i&L_i\\ \hline
Qabcd&(b,c,d)&0&Qad\\
Qacde&(a,d,e)&1&Qac\\
Qabce&(a,b,c)&0&Qce\\
Qbcde&(c,d,e)&0&Qbe\\
Qabde&(a,b,e)&2&Qbd.
\end{array}                                                   \tag{6.2}
\]

Here juxtaposition means union.  The prefix `Q` consists of consecutive
ones, and direct cyclic cancellation gives the displayed free triples.
Using `(1.4)`, the five directed physical edges are

\[
 Qabd\longrightarrow Qacd\longrightarrow Qace
 \longrightarrow Qbce\longrightarrow Qbde
 \longrightarrow Qabd.                              \tag{6.3}
\]

The labels in each of the four columns of `(5.2)--(5.3)` are distinct.
This is the required rainbow directed pentagon.

#### The case \(r=3\)

On ground set `{0,1,2,3,4}`, take upper/rule pairs

\[
 0123/0,\quad0234/2,\quad0124/0,\quad1234/1,\quad0134/0.
\tag{6.4}
\]

Their lower labels are respectively

\[
                         03,\quad02,\quad24,\quad14,\quad13, \tag{6.5}
\]

and their oriented physical edges are

\[
 013\to023\to024\to124\to134\to013.               \tag{6.6}
\]

Again all four label shores are injective. \(\square\)

### Consequence 6.2

Neither of the following is valid:

* “two SDRs imply a forest”; or
* “a flow/TU proof of the two marginal matchings automatically solves
  pathization.”

A proof must either include the directed-forest inequalities, construct a
strict potential compatible with its chosen sides, or give explicit
cycle-opening exchanges that preserve both SDRs.

## 7. The corrected target: enlarge the local menu

Theorem 4.1 disproves the cyclic-triangle forest-selector conjecture for
all `r>=14`.  The finite witnesses through `r=7` therefore support only a
small-parameter phenomenon; they cannot be extrapolated to all `r`.

The useful surviving output is a design constraint for the next family.
If a menu gives each upper colour several candidate edges, define, for a
middle owner `X`, the number `a_X` of upper menus all of whose candidate
edges meet `X`.  Every selection must use `X` at least `a_X` times.
Therefore the immediate local capacity test is

\[
                            a_X\le2                 \tag{7.1}
\]

for every owner, together with its subset/Hall strengthening.  In the
three-choice family, the equivalent aggregate overload is exactly `(4.6)`.

The smallest plausible enlargement is to add a second cyclic chart (for
example the reverse-parenthesis triangle) and deduplicate the resulting
at-most-six diamonds below each upper colour.  Such an enlargement must be
audited in this order:

1. recompute mandatory owner incidences and prove that every capacity cut
   has nonnegative slack uniformly in `r`;
2. choose one diamond per upper with distinct lower colours and owner
   degree at most two; and only then
3. impose acyclicity or prove a colour-preserving cycle-opening exchange.

The normal form in Sections 1--3 and the pentagon in Section 6 remain
useful for this enlarged search, but the literal three-choice catalogue is
closed negatively.
