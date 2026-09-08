# Quantitative two-sided rainbow forests and fresh promotion atoms

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 N_1=\binom n{m-1}=\frac m{m+2}W,
 \qquad H\asymp\sqrt{m\log m}.                    \tag{0.1}
\]

The requested quantitative bridge is not yet complete.  The following
points are proved.

1.  The existing fixed-girth conflict-matching proof gives an explicit
    component bound

    \[
      \frac{c(F)}W
      \le \frac4m+D^{-\alpha_L}+\frac1{L+1}+O(m^{-2}),
      \qquad D=2(m+3)(m+2),                       \tag{0.2}
    \]

    for every **fixed** cycle cutoff \(L\).  Its published quantifiers do
    not permit \(L=L(m)\gg H\), so it proves only \(c(F)=o(W)\), not
    \(O(W/m)\) or \(o(W/H)\).

2.  There is an exact length-\(\Theta(m)\) colored-atom formulation.  For
    even \(m\), take

    \[
       b=\frac{m+2}{2},\qquad t=\frac Wb=\frac{2W}{m+2}.          \tag{0.3}
    \]

    A perfect matching of \(t\) fresh atoms covers every middle owner and
    every lower first color exactly once, uses \(N_1\) distinct upper
    first colors, and consists of exactly \(t=O(W/m)\) literal tight
    paths.  It collars through radius \(H\) at reset cost

    \[
       2Ht=O(HW/m)=o(W).                           \tag{0.4}
    \]

    Odd \(m\) has the exact two-length analogue.

3.  The atom hypergraph has an exact fractional factor.  Its only
    \(m^{-1}\)-scale pair codegrees are the genuine two-parent inclusions

    \[
        S\subset X\subset U.                       \tag{0.5}
    \]

    Their dependency graph has maximum degree \(2m+1\).  Every other
    same- or cross-rank pair has relative codegree \(O(m^{-2})\).

4.  The vertical term cannot be removed by choosing one parent per color:
    every transition color needs both endpoint owners, so a one-parent SDR
    misses exactly half of the \(\Theta(W)\) required vertical incidences.
    What remains is a common degree-two, three-part matching whose
    components are fresh paths.  No integral rounding theorem at the
    required error is proved here.

Thus this note gives a sharp positive target and an explicit rate, but it
does not claim coefficient one.

## 1. Quantitative audit of the existing two-sided-rainbow theorem

The fixed-arity construction works in \(J(n,m-1)\).  Put

\[
 N_2=\binom n{m-2}
 =\frac{m(m-1)}{(m+2)(m+3)}W.                     \tag{1.1}
\]

The four-partite lifted transition hypergraph has asymptotic degree

\[
 D=2(m+3)(m+2),                                   \tag{1.2}
\]

and its matching scale is \(N_2\).  For every fixed integer \(L\), the
Delcourt--Postle small-codegree corollary supplies a constant
\(\alpha_L>0\) and a matching of size at least

\[
 N_2(1-D^{-\alpha_L})                              \tag{1.3}
\]

whose projected maximum-degree-two graph has no cycle of length at most
\(L\).  Delete one edge from every remaining projected cycle.  The cycles
are vertex-disjoint, so at most \(N_1/(L+1)\) edges are deleted.  The
resulting spanning linear forest therefore has

\[
\begin{aligned}
 c(F)
 &\le N_1-N_2+D^{-\alpha_L}N_2+\frac{N_1}{L+1}\\
 &=\frac{4mW}{(m+2)(m+3)}
   +D^{-\alpha_L}N_2+\frac{N_1}{L+1}.             \tag{1.4}
\end{aligned}
\]

This proves (0.2).

### Consequence 1.1 (the exact missing uniformity)

Equation (1.4) gives \(O(W/m)\) components only if

\[
 L=\Omega(m),\qquad D^{-\alpha_L}=O(1/m),          \tag{1.5}
\]

and gives \(o(W/H)\) only if

\[
 L/H\longrightarrow\infty,
 \qquad H D^{-\alpha_L}\longrightarrow0.          \tag{1.6}
\]

The cited theorem fixes its maximum conflict size before letting
\(D\to\infty\), and supplies neither a uniform lower bound for
\(\alpha_L\) nor a uniform threshold when \(L=L(m)\).  Hence the diagonal
argument \(L\to\infty\) proves no rate in (1.5) or (1.6).

This is a quantifier obstruction, not a failure of the elementary cycle
counts.  If a prescribed \(j\)-edge submatching projects to \(s\) path
components and \(t=i-j\) new edges complete an \(i\)-cycle, then direct
gap filling gives

\[
 \Delta_{i,j}^{(s)}
 \le 2^{s+1}s!\binom{t-1}{s-1}(2Q)^{t-s},
 \qquad Q=(m-1)(m+2),                             \tag{1.7}
\]

and a fixed lifted edge belongs to at most

\[
 \Delta_i\le2(2Q)^{i-2}                            \tag{1.8}
\]

projected \(i\)-cycle conflicts.  Indeed, order and orient the \(s\)
prescribed path components, compose \(t\) into \(s\) positive gap lengths,
and choose all but the forced final edge of each gap.  Clone choices give
the displayed powers of two.  Since

\[
 2Q=D\frac{m-1}{m+3}<D,                            \tag{1.9}
\]

the local numerical cycle bounds retain substantial power slack even for
\(i\le m\).  What is absent is a conflict-matching theorem uniform in that
growing conflict rank.

### Correction 1.2 (endpoint loss in the old lift)

For a rank-\((m-1)\) path \(S_0,\ldots,S_\ell\), its upper-color path has
\(\ell\) vertices.  Its adjacent intersections recover only
\(S_1,\ldots,S_{\ell-1}\), so both endpoint targets are lost.  If a
spanning forest has \(c\) components and \(e\) edges, then the lifted
rank-\((m-1)\) support misses at most \(2c\), and its rank-\((m-2)\)
triple-intersection support misses at most \(3c\).  The former printed
\(o(W)\) conclusion survives, but the quantitative constants must use
these bounds.

For comparison, applying the saturating-cycle theorem one rank lower and
breaking the cycle once gives a one-sided lower-rainbow forest with exactly

\[
 N_1-N_2+1
 =\frac{4mW}{(m+2)(m+3)}+1=O(W/m)                 \tag{1.10}
\]

components.  Thus simultaneous upper rainbowness is precisely where the
known proof loses the optimal rate.

The owner/chronology projection is also already quantitative.  Cutting an
exact odd wreath factor gives \(W/(m+1)\) complement-ended geodesics; the
audited mixed-frame chunking uses at most \(3W/(m+1)=O(W/m)\) collared
pieces and costs \(O(HW/m)=o(W)\) for every \(H=o(m)\).  Its unresolved
projection is the lower shadow support of those fixed owner paths.  The
fresh-atom system below is therefore exactly the common refinement of two
separately solved projections: optimal owner chronology and two-sided
first-color rainbowness.

## 2. Fresh tight atoms

Fix \(2\le b\le m+2\).  A labelled fresh atom is an injective word

\[
 x=(x_0,x_1,\ldots,x_{m+b-2})                     \tag{2.1}
\]

of length \(m+b-1\) in \([n]\).  Define

\[
 X_i=\{x_i,x_{i+1},\ldots,x_{i+m-1}\}
 \quad(0\le i<b),                                 \tag{2.2}
\]

and, for \(0\le i<b-1\),

\[
 S_i=X_i\cap X_{i+1}in\binom{[n]}{m-1},
 \qquad
 U_i=X_i\cup X_{i+1}\in\binom{[n]}{m+1}.         \tag{2.3}
\]

Explicitly,

\[
 S_i=\{x_{i+1},\ldots,x_{i+m-1}\},
 \qquad
 U_i=\{x_i,\ldots,x_{i+m}\}.                     \tag{2.4}
\]

All targets in any one of the three displayed ranks are distinct.  Let
\(\mathcal A_{m,b}\) be the three-partite hypergraph whose atom edge is

\[
 \{X_0,\ldots,X_{b-1}\}
 \sqcup\{S_0,\ldots,S_{b-2}\}
 \sqcup\{U_0,\ldots,U_{b-2}\}.                   \tag{2.5}
\]

Its edge size is \(3b-2\).

### Theorem 2.1 (exact fresh-atom degree ledger)

Let \((a)_k=a(a-1)\cdots(a-k+1)\).  The number of labelled atoms is

\[
 E=(2m+1)_{m+b-1}.                                \tag{2.6}
\]

The three vertex degrees are

\[
\boxed{
\begin{aligned}
 d_M&=b\,m!(m+1)_{b-1},\\
 d_L&=(b-1)(m-1)!(m+2)_b,\\
 d_U&=(b-1)(m+1)!(m)_{b-2}.
\end{aligned}}                                    \tag{2.7}
\]

#### Proof

For a fixed middle target, choose its one slot in \(b\) ways, order its
\(m\) elements, and injectively fill the remaining \(b-1\) word slots
from its \(m+1\)-element complement.  This gives \(d_M\).

For a fixed lower target, choose one of its \(b-1\) slots, order its
\(m-1\) elements, and fill the remaining \(b\) word slots from a
complement of size \(m+2\).  The upper count is identical with ranks
reversed: choose one of \(b-1\) slots, order the \(m+1\) target elements,
and fill \(b-2\) positions from its \(m\)-element complement. \(\square\)

## 3. The exactly balanced length

Assume first that \(m\) is even and put

\[
 b=\frac{m+2}{2},\qquad
 t=\frac Wb=\frac{2W}{m+2}=W-N_1.                \tag{3.1}
\]

Then

\[
 t(b-1)=N_1.                                      \tag{3.2}
\]

The degree ratios in (2.7) simplify to

\[
 \boxed{d_L=d_M=:D,\qquad d_U=\frac{b-1}{b}D.}    \tag{3.3}
\]

Indeed,

\[
 \frac{d_L}{d_M}
 =\frac{b-1}{b}\frac{m+2}{m}=1,
 \qquad
 \frac{d_U}{d_M}=\frac{b-1}{b}.                  \tag{3.4}
\]

Double counting middle incidences gives

\[
 \frac ED=\frac Wb=t.                            \tag{3.5}
\]

Consequently assigning weight \(1/D\) to every labelled atom is an exact
fractional matching of total weight \(t\): it saturates every middle and
lower resource, and gives every upper resource load
\((b-1)/b=N_1/W\).  Thus there is no marginal or divisibility obstruction.

### Theorem 3.1 (integral fresh-atom matching implies the optimal path cover)

If \(\mathcal A_{m,b}\) has a matching of size \(t\), then its projected
owner paths have all of the following properties.

1. They partition \(\binom{[n]}m\).
2. Every rank-\((m-1)\) target occurs exactly once as a transition color.
3. Their upper transition colors are distinct and miss exactly \(t\) of
   the \(W\) rank-\((m+1)\) targets.
4. They have exactly \(t=2W/(m+2)=O(W/m)\) components, each with \(b\)
   owners.

#### Proof

A matching uses distinct resources in all three parts.  Its \(t\) edges
contain \(tb=W\) middle resources and
\(t(b-1)=N_1\) lower resources.  These equal the full part sizes, proving
the first two assertions.  The same number of upper resources are distinct;
that part has size \(W\), giving the third assertion.  The fourth is the
definition of an atom path. \(\square\)

### Odd \(m\)

If \(m\) is odd, put

\[
 b_-=(m+1)/2,\qquad b_+=(m+3)/2,
 \qquad t=2W/(m+2).                               \tag{3.6}
\]

Since \(\gcd(m,m+2)=1\) and \(N_1=Wm/(m+2)\) is integral,
\(W/(m+2)\) is integral; hence \(t\) is even.  A matching containing
exactly \(t/2\) atoms of each length has

\[
 \frac t2(b_-+b_+)=W,
 \qquad
 \frac t2[(b_--1)+(b_+-1)]=N_1.                 \tag{3.7}
\]

It therefore has the same exact conclusion as Theorem 3.1.  The union of
the two atom types has an exact fractional solution: give each type total
weight \(t/2\), uniformly over all atoms of that type.  Equations (3.7)
show that middle and lower loads are one and upper load is \(N_1/W\).

## 4. Exact collar cost and the required matching accuracy

The word (2.1) leaves

\[
 n-(m+b-1)=m-b+2=\Theta(m)                        \tag{4.1}
\]

unused coordinates at the balanced length.  Since \(H=o(m)\), extend the
word forward by \(H\) unused coordinates; equivalently, the exact condition
is \(b+H\le m+2\).  Write the extended injective word as
\(y_0,\ldots,y_{m+b+H-2}\), and emit

\[
 E_j=\{y_j,\ldots,y_{j+m-H-1}\},
 \qquad 0\le j<b+2H.                              \tag{4.2}
\]

For every principal start \(0\le i<b\) and \(0\le q\le H\),

\[
 \bigcup_{j=i+q}^{i+H}E_j
 =I_y(i+q,m-q)=\bigcap_{a=0}^qX_{i+a},             \tag{4.3}
\]

and

\[
 \bigcup_{j=i}^{i+H+q}E_j
 =I_y(i,m+q)=\bigcup_{a=0}^qX_{i+a}.               \tag{4.4}
\]

The out-of-range owner windows are supplied by the forward collar.  Thus
one atom is a literal tight promotion/rotor word of exactly \(b+2H\)
nonzero entries, not merely a color transversal.

An exact atom matching has total initialization/reset cost at most

\[
 2Ht=\frac{4HW}{m+2}=o(W).                        \tag{4.5}
\]

More generally, suppose the even-\(m\) atom hypergraph has a matching of
size \(t-s\).  Its missing middle and lower resources are respectively

\[
 bs,\qquad (b-1)s,                                \tag{4.6}
\]

and its upper support misses

\[
 t+(b-1)s.                                        \tag{4.7}
\]

Therefore

\[
 \boxed{s=o(t/H)}                                 \tag{4.8}
\]

is sufficient for owner and first-color repair \(o(W/H)\), while the
number of collared paths and their reset cost remain \(O(W/m)\) and
\(o(W)\).  At depth one alone, appending every missing middle and signed
color target gives the exact upper bound

\[
 W+2H(t-s)+t+2(b-1)s.                              \tag{4.9}
\]

Thus \(s=o(t)\) already proves a \(W+o(W)\) first-band word.  The sharper
condition (4.8) is what is needed when the omitted owner/color mass itself
must be \(o(W/H)\), or is charged through all \(H\) later depths.  The
atom matching alone does not assert deeper cross-atom support.

## 5. Exact codegrees and the two-parent backbone

The large codegrees have an exact geometric description.

### Lemma 5.1 (the two vertical codegrees)

For \(S\in\binom{[n]}{m-1}\), \(X\in\binom{[n]}m\), and
\(U\in\binom{[n]}{m+1}\),

\[
 \frac{\operatorname{codeg}(S,X)}{d_L}
 =\begin{cases}
   \displaystyle\frac2{m+2},&S\subset X,\\
   0,&S\not\subset X\text{ and the pair is vertical},
  \end{cases}                                      \tag{5.1}
\]

and

\[
 \frac{\operatorname{codeg}(X,U)}{d_U}
 =\begin{cases}
   \displaystyle\frac2{m+1},&X\subset U,\\
   0,&X\not\subset U\text{ and the pair is vertical}.
  \end{cases}                                      \tag{5.2}
\]

#### Proof

Every occurrence of a lower color \(S_i\) in an atom is incident with
exactly the two owner endpoints \(X_i,X_{i+1}\).  The stabilizer of \(S\)
is transitive on its \(m+2\) middle supersets.  Double counting these two
incidences proves (5.1).  Similarly, every upper color \(U_i\) contains
exactly the two endpoints \(X_i,X_{i+1}\), and an \((m+1)\)-set has
\(m+1\) middle facets.  This proves (5.2). \(\square\)

### Lemma 5.2 (all nonvertical pairs are \(m^{-2}\)-diffuse)

Uniformly for \(b=\Theta(m)\), any same-rank pair and any cross-rank pair
other than the inclusions in Lemma 5.1 has relative codegree

\[
 O(m^{-2})                                         \tag{5.3}
\]

with respect to the degree of either endpoint, up to the harmless constant
degree ratio among the three parts.

#### Proof

Represent two labelled target slots by position intervals \(P,Q\) in the
word.  Put

\[
 a=|P\setminus Q|,qquad c=|Q\setminus P|.
\]

Conditional on a prescribed set occupying \(P\), a prescribed target can
occupy \(Q\) only with the forced intersection, and then with exact
probability

\[
 \frac1{\binom{|P|}a\binom{n-|P|}c}.              \tag{5.4}
\]

The cases \(a+c=1\) are exactly the adjacent nested slots of Lemma 5.1.
Otherwise \(a+c\ge2\).  For fixed \((a,c)\), at most \(a+c+1\) interval
slots \(Q\) have those two differences.  Since both \(|P|\) and
\(n-|P|\) are \(m+O(1)\),

\[
 \sum_{a+c\ge2}
 \frac{a+c+1}{\binom{|P|}a\binom{n-|P|}c}
 =O(m^{-2}).                                      \tag{5.5}
\]

Average over the possible first slots.  A target cannot occupy two slots
of the same rank in one fresh word, so no representation multiplicity is
lost.  This proves (5.3). \(\square\)

Let \(G_{\rm vert}\) be the graph on all three resource parts whose edges
are the inclusions \(S\subset X\subset U\).  Then

\[
 \Delta(G_{\rm vert})\le2m+1.                    \tag{5.6}
\]

Every atom contains exactly

\[
 2(b-1)+2(b-1)=4(b-1)                             \tag{5.7}
\]

vertical pairs.  At the balanced length, an interior owner of a fixed atom
has four vertical partners, and their total normalized overlap is

\[
 \frac8m+O(m^{-2}).                               \tag{5.8}
\]

Every individual nonvertical partner has normalized overlap
\(O(m^{-2})\).  More strongly, their total normalized overlap for a fixed
vertex inside a fixed test atom is \(O(m^{-2})\): one bounded factor counts
test-atom slots of a given \((a,c)\)-type and a second bounded factor counts
possible slots in a random atom, after which the reciprocal-binomial sum
in (5.5) applies.  Thus the only critical channel is the literal path
backbone; it is sparse in the resource graph but cannot be discarded.

## 6. Exact failure of one-parent absorption

A tempting two-stage argument is to use Hall separately to assign one
owner to every lower color and one owner to every upper color, and then
nibble the remaining diffuse incidences.  It loses a linear amount.

Indeed, \(t\) balanced atoms contain \(t(b-1)=N_1\) lower colors, but
their paths require

\[
 2t(b-1)=2N_1                                     \tag{6.1}
\]

lower-color--owner incidences.  A one-parent SDR accounts for only
\(N_1\) of them.  The same calculation holds for the upper colors.  The
missing \(N_1=\Theta(W)\) incidences cannot be supplied by \(o(W)\)
recourse.  The vertical backbone must therefore be rounded as one common
degree-two transition system.

There is nevertheless no marginal color obstruction.  The bipartite
inclusion graph

\[
 \binom{[n]}{m-1}\longleftrightarrow\binom{[n]}{m+1},
 \qquad S\subset U,                               \tag{6.2}
\]

is

\[
 \left(\binom{m+2}2,\binom{m+1}2\right)           \tag{6.3}
\]

biregular.  Double counting proves Hall for the smaller lower part, so
there is an injection \(S\mapsto U(S)\) with \(S\subset U(S)\).  Each
pair \((S,U)\) determines the Johnson edge joining the two middle sets in
\([S,U]\).  This solves lower/upper color pairing exactly.  It does not
control middle degrees, components, or freshness.  Conversely, owner-only
graphic Hall does not control the upper colors.  The atom theorem asks for
their common path-history intersection.

## 7. Sharpness and the deeper-rainbow warning

If a two-sided first-color-rainbow schedule has \(v\) distinct owners in
\(p\) nonempty paths, it has \(v-p\) transitions.  Lower-color injectivity
therefore gives

\[
 p\ge v-N_1.                                      \tag{7.1}
\]

For an exact owner partition \(v=W\), this is

\[
 p\ge W-N_1=\frac{2W}{m+2},                       \tag{7.2}
\]

so the balanced atom length in Section 3 is arithmetically optimal.

One must not demand strict rainbowness at every growing depth.  If all
depth-\(q\) internal flags are distinct, then at most \(N_q\) of the
\(v-qp\) internal positions can be used, whence

\[
 p\ge\frac{v-N_q}{q}.                             \tag{7.3}
\]

At \(q=H\asymp\sqrt{m\log m}\), one has \(W-N_H=(1-o(1))W\), so
\(p=\Omega(W/H)\).  Therefore the desired \(O(W/m)=o(W/H)\) fresh
first-band schedule must feed a balanced-multiplicity/promotion compiler at
deeper ranks; strict all-depth colors would contradict the component
budget.

## 8. Exact remaining lemma and audit

The positive integral gate isolated by this note is:

> **Fresh promotion-atom matching lemma (unproved).**  For even \(m\),
> \(\mathcal A_{m,(m+2)/2}\) has a matching of size
> \[
>   \frac{2W}{m+2}-o\!\left(\frac{W}{mH}\right).  \tag{8.1}
> \]
> For odd \(m\), the two-type version has the corresponding prescribed
> half-counts, with the same owner/color error.

The atom degrees, exact fractional factor, \(m^{-2}\) diffuse remainder,
and sparse vertical inclusion graph are proved above.  They do not by
themselves prove (8.1): the hypergraph rank is \(\Theta(m)\), while the
vertical relative codegree is \(\Theta(1/m)\).  Projective-plane examples
show why a theorem using only those two maximum parameters would be false.
Here the high pairs form paths rather than a dense design, but a
backbone-aware rounding theorem is still missing.

Adversarial checks:

1. The collar coordinates are not counted as new owners; they initialize
   literal flags.  There are \(\Theta(m)\) unused labels per atom, so the
   extension is valid for \(H=o(m)\).
2. A perfect atom matching controls only the first signed colors.  Deeper
   literal flags exist, but their global support is not asserted.
3. The fixed-\(L\) conflict theorem is not used with a growing \(L\).
4. The one-parent Hall injection (6.2) is not promoted to a path factor.
5. The fractional solution is not promoted to an integral matching.
6. The error scale in (8.1), rather than an unquantified \(o(W/m)\), is
   what is needed to keep growing-window repair below \(o(W)\).

Accordingly, the theorem note proves the optimal quantitative formulation
and every local estimate, but not the final fresh-atom matching.
