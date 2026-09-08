# The compatible \(r-1,r,r+1\) rectangle cube: exact conflict paths and cut capacity

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The persistent-suffix dual closes the full two-scale cube only in the
upper Catalan-overshoot sector.  Adding the immediately lower rectangle
scale changes the conclusion completely.

The adjacent-scale conflict graphs

\[
 \mathcal E_{r-1}\leftrightarrow\mathcal E_r,
 \qquad
 \mathcal E_r\leftrightarrow\mathcal E_{r+1}
\]

are matchings.  Their union consists exactly of isolated vertices,
isolated edges, and length-two paths.  The nonadjacent scales
\(r-1,r+1\) commute even when their recursion nodes are nested: their
changed phases are separated by one unchanged phase, so their affected
edge slabs are disjoint.

Taking both endpoints of every length-two path and one endpoint of every
isolated edge yields a literal exact Boolean cube.  A particularly useful
maximum family is

\[
 \boxed{
 \mathcal E_{r-1}\ \dot\cup\ \mathcal E_{r+1}
 \ \dot\cup\ \mathcal E_r^{\rm iso},}
\tag{0.1}
\]

where \(\mathcal E_r^{\rm iso}\) consists of middle-scale switches with
neither adjacent-scale conflict.  Its exact dimension is

\[
\boxed{
 B_3=M_{r-1}+M_r+M_{r+1}-L_r-U_r+I_r,}
\tag{0.2}
\]

with

\[
\begin{aligned}
 L_r&=H_{m,r+1}\Cat_{r-2},\\
 U_r&=H_{m,r+2}\Cat_{r-1},\\
 I_r&=H_{m,r+2}\Cat_{r-2}.
\end{aligned}
\tag{0.3}
\]

At every depth \(q\ge r+2\), scales \(r,r+1\) have at most three units
of canonical-cut drain per switch.  Scale \(r-1\) has at most

\[
 w_-(t)=4-\mathbf1_{\{t>R_rR_{r-1}\}},
 \qquad
 R_j={\Cat_j\over\Cat_{j-1}},
 \qquad t={\Cat_r\over p}.
\tag{0.4}
\]

Thus the maximum fixed-cut drain of (0.1) is

\[
\boxed{
 \mathscr C_3(t)
 =w_-(t)M_{r-1}
   +3\bigl(M_{r+1}+M_r-L_r-U_r+I_r\bigr).}
\tag{0.5}
\]

Writing \(M_r=\rho_{m,r}H_{m,r}\Cat_r\), one has

\[
 {\mathscr C_3(t)\over H_{m,r}\Cat_r}
 =\begin{cases}
 139/256+O(r^{-1}+r/m),&t\le R_rR_{r-1},\\
 123/256+O(r^{-1}+r/m),&t>R_rR_{r-1}.
 \end{cases}
\tag{0.6}
\]

The certified canonical demand is at most

\[
 {1\over2}-{1\over t}
 <{7\over16}={112\over256}.
\tag{0.7}
\]

Consequently the three-scale cube has more than enough *possible
canonical-cut drain* throughout the entire overshoot interval
\(4\le t<4R_r<16\).  The persistent-suffix dual therefore gives no
multidepth three-scale no-go on (q\ge r+2).

There is one self-depth exception at (q=r+1): scale (r+1) has only
two potentially useful arms.  The exact maximum envelope there is

\[
 \boxed{
 \mathscr C_3^{\rm self}(t)
 =3M_{r-1}+3M_r+2M_{r+1}
  -3L_r-2U_r+2I_r+B_{r+1},}
\tag{0.8}
\]

where (B_{r+1}\in[0,M_{r-1}]) is the number of retained lower-scale
hereditary arms which actually cross the canonical cut.  Without this
bonus the normalized envelope is

\[
 {55\over128}+o(1),
\]

and the exact necessary bonus fraction above (t=128/9+o(1)) is

\[
 \boxed{
 {B_{r+1}\over M_{r-1}}
 \ge {9\over8}-{16\over t}+o(1).}
\tag{0.9}
\]

This possible one-depth residual is (O(W/r^{3/2})=o(W)), so it does not
restore an aggregate PCap no-go.  The result remains a capacity statement,
not a positive orientation theorem: the remaining gate is common-state
selection of the arms, not physical compatibility or aggregate scalar
supply.

## 1. The two adjacent conflict matchings

Recall

\[
 M_s=H_{m,s+1}\Cat_{s-1}.
\]

A scale-\(s\) switch has local rows

\[
 A_R=1100R,
 \qquad B_R=1010R,
 \qquad R\in\mathcal D_{s-1}.
\]

The adjacent-scale classification says that a scale-\(s\) switch and a
scale-\(s+1\) switch conflict exactly in the unique direct-child pattern

\[
                         S=10R,
 \qquad B'_{10R}=10B_R.
\tag{1.1}
\]

Every vertex is in at most one such pair for a fixed adjacent pair of
scales.  Therefore the lower and upper conflict-edge counts are

\[
\begin{aligned}
 L_r
 &=H_{m,r+1}\Cat_{r-2},\\
 U_r
 &=H_{m,r+2}\Cat_{r-1}.
\end{aligned}
\tag{1.2}
\]

Here \(L_r\) counts middle parameters \(R=10P\), while \(U_r\) counts
middle contexts which are the empty-left right child of a scale-\(r+1\)
parent.

### Lemma 1.1 (the overlap of the two matchings)

The number of middle-scale switches incident with both a lower and an
upper conflict is

\[
                         \boxed{I_r=H_{m,r+2}\Cat_{r-2}.}
\tag{1.3}
\]

#### Proof

Both incidences occur precisely when the middle parameter has the form
\(R=10P\), \(P\in\mathcal D_{r-2}\), and the middle parent context is the
empty-left right child of an aligned scale-\(r+1\) context.  Choose the
outer context in \(H_{m,r+2}\) ways and \(P\) in \(\Cat_{r-2}\) ways.
Both choices are recovered from the middle switch, so the count is exact.
\(\square\)

Since each adjacent graph is a matching, their union has maximum degree
two.  It is tripartite with only the three consecutive levels, so its
components are exactly isolated vertices, isolated edges, and length-two
paths.  The numbers of the two nontrivial types are

\[
\begin{array}{c|c}
\text{component type}&\text{number}\\ \hline
(r-1)-r-(r+1)&I_r\\
(r-1)-r&L_r-I_r\\
r-(r+1)&U_r-I_r.
\end{array}
\tag{1.4}
\]

The number of isolated middle vertices is

\[
                         M_r-L_r-U_r+I_r.
\tag{1.5}
\]

## 2. The nonadjacent scales commute

### Lemma 2.1

A scale-\(r-1\) switch and a scale-\(r+1\) switch commute, including when
their recursion nodes are nested.

#### Proof

Disjoint nodes have disjoint phase slabs, as in the fixed-scale and
adjacent-scale cube theorems.  Suppose the nodes are nested.  The larger
local rows are

\[
                         1100S,
 \qquad                  1010S,
 \qquad                  |S|_s=r.
\]

A nested node of semilength \(r\) must be the displayed subtree \(S\);
the other local pieces have total semilength two.  In both larger rows,
the \(S\)-block begins two MSW phases after the larger block begins.  The
larger switch changes phase one, while the smaller switch changes phase
three.  Their affected edge slabs are

\[
                         \{0\!-!1,1\!-!2\},
 \qquad                  \{2\!-!3,3\!-!4\}.
\]

They share only the unchanged state at phase two and no edge.  Therefore
the two state substitutions and their complete local ownership-ledger
permutations commute.  The same argument applies after adjoining an
arbitrary ambient context. \(\square\)

Consequently an independent set in the adjacent-conflict graph is a
literal exact-factor Boolean cube; there is no additional
\((r-1,r+1)\) conflict.

## 3. The maximum compatible family

On a length-two conflict path, the two endpoints are compatible and give
two variables, while the middle gives only one.  On an isolated edge one
may take either endpoint.  It follows componentwise that (0.1) is a
maximum-cardinality compatible family.  Formula (1.5) gives

\[
\begin{aligned}
 B_3
 &=M_{r-1}+M_{r+1}+M_r-L_r-U_r+I_r\\
 &=H_{m,r}\Cat_{r-2}
   +H_{m,r+1}(\Cat_{r-1}-\Cat_{r-2})\\
 &\qquad
   +H_{m,r+2}(\Cat_r-\Cat_{r-1}+\Cat_{r-2}),
\end{aligned}
\tag{3.1}
\]

which proves (0.2).

This family is also maximum for the cut-drain weights below.  On a lower
edge the scale-\(r-1\) endpoint has weight three or four, versus weight
three in the middle; on an upper edge both weights are three; and on a
length-two path the two endpoint weights have sum at least six, versus
three at the middle.  Thus the componentwise choice used in (0.1) is
weight-maximizing.

## 4. Exact cut-drain coefficients

Let \(r\) be minimal with \(\Cat_r\ge4p\), and put

\[
                         t={\Cat_r\over p}.
\]

For scales \(r,r+1\), the persistent suffix endpoint loads are at least
\(\Cat_{s-1}>p\), so one of four arms is neutral on the canonical
overloaded-set cut.  Their drain coefficient is at most three.

At scale \(r-1\), the corresponding endpoint loads are

\[
                         \Cat_{r-1},
 \qquad                  \Cat_{r-2}.
\]

The first always exceeds \(p\), because

\[
 {\Cat_{r-1}\over p}={t\over R_r}>{4\over R_r}>1.
\]

The second exceeds \(p\) exactly when

\[
                         t>R_rR_{r-1}.
\tag{4.1}
\]

This proves the piecewise coefficient (0.4).  Granting four units when
the second endpoint is not protected is deliberately optimistic; it is
the correct coefficient for a no-go audit.

The componentwise maximum-weight calculation then gives (0.5).

### 4.1 The top self-depth (q=r+1)

At (q=r+1), the scale-(r+1) switches are at their own matched depth.
Their two marked occurrence arms are cap-neutral, so their optimistic
drain weight is two, not three.  The lower and middle weights are
respectively (3+b_e) and (3), where (b_e\in\{0,1\}) records whether
the lower hereditary arm actually crosses the cut.

Optimize componentwise in (1.4).  On a lower isolated edge choose the
lower endpoint; on an upper isolated edge choose the middle endpoint; on
a length-two path choose the lower and upper endpoints.  Thus all lower
vertices are retained, the retained middle vertices are exactly those
with no lower conflict, and the retained upper vertices are the isolated
ones together with the upper endpoints of the length-two paths.  The
resulting drain envelope is

\[
\begin{aligned}
 \mathscr C_3^{\rm self}
 &=3M_{r-1}+3(M_r-L_r)+2(M_{r+1}-U_r+I_r)+B_{r+1}\\
 &=3M_{r-1}+3M_r+2M_{r+1}
       -3L_r-2U_r+2I_r+B_{r+1},
\end{aligned}
\tag{4.2}
\]

where (0\le B_{r+1}\le M_{r-1}).  Using the ratios in Section 5 gives

\[
 {\mathscr C_3^{\rm self}-B_{r+1}
       \over H_{m,r}\Cat_r}
 ={55\over128}+O(r^{-1}+r/m).
\tag{4.3}
\]

Comparison with the demand (1/2-1/t) yields

\[
 {B_{r+1}\over M_{r-1}}
 \ge16\left({1\over2}-{1\over t}-{55\over128}\right)+o(1)
 ={9\over8}-{16\over t}+o(1),
\tag{4.4}
\]

whenever the right side is positive, i.e. (t>128/9+o(1)).

If (t>R_rR_{r-1}), the scale-(r-1) destination certificate is itself
above cap, so (B_{r+1}=0).  This happens only in the thin upper strip

\[
 R_rR_{r-1}=16-{48\over r}+O(r^{-2})<t<4R_r.
\]

In that strip the fixed cut leaves a positive self-depth residual, but it
is only (\Theta(H_{m,r}\Cat_r)=\Theta(W/r^{3/2})=o(W)).

## 5. Normalized exact formula and asymptotics

Put \(k=m-r-1\), and define

\[
\begin{aligned}
 \rho&={M_r\over H_{m,r}\Cat_r}
 ={(k+1)(r+1)\over4(2k+1)(2r-1)},\\
 a_-&={M_{r-1}\over M_r}={1\over\sigma_{m,r-1}},\\
 a_+&={M_{r+1}\over M_r}=\sigma_{m,r},\\
 \ell&={L_r\over M_r}={\Cat_{r-2}\over\Cat_{r-1}},\\
 h&={U_r\over M_r}={H_{m,r+2}\over H_{m,r+1}}
 ={k\over2(2k-1)}.
\end{aligned}
\tag{5.1}
\]

Then

\[
 {I_r\over M_r}=h\ell,
 \qquad
 {M_r-L_r-U_r+I_r\over M_r}=(1-\ell)(1-h).
\tag{5.2}
\]

Therefore the exact normalized cut capacity is

\[
\boxed{
 \Gamma_{m,r}(t)
 :={\mathscr C_3(t)\over H_{m,r}\Cat_r}
 =\rho\left[
    w_-(t)a_-+3a_++3(1-\ell)(1-h)
           \right].}
\tag{5.3}
\]

Uniformly for \(r=o(m)\),

\[
 \rho={1\over16}+O(r^{-1}+m^{-1}),
 \quad a_\pm=1+O(r^{-1}+r/m),
 \quad \ell={1\over4}+O(r^{-1}),
 \quad h={1\over4}+O(m^{-1}).
\]

Substitution gives (0.6).

Minimality of \(r\) gives \(t<4R_r<16\), hence

\[
 {1\over2}-{1\over t}
 <{1\over2}-{1\over16}={7\over16}.
\]

Even the smaller value in (0.6) exceeds this by

\[
                         {123-112\over256}={11\over256}.
\]

Thus for all sufficiently large \(r\) and every (q\ge r+2), the
canonical fixed-cut dual is strictly below the compatible three-scale
supply for every admissible \(t\).  Nonlinear double-boundary interactions are only
\(O(W/r^3)\) per depth by the bivariate two-hole theorem and do not alter
this constant comparison.

## 6. Scope

This theorem settles two gates:

1. the complete physical compatibility graph of the three consecutive
   rectangle scales;
2. the exact maximum canonical-cut drain ceiling of that graph, including
   the exceptional top self-depth.

It does **not** orient the retained arms to attain the ceiling.  A positive
three-scale construction must still solve the common-state, multidepth
weighted cut problem.  Conversely, any new no-go must use a stronger dual
than the persistent canonical overloaded-set indicator, because that
indicator has a constant capacity deficit against the cube (0.1).
