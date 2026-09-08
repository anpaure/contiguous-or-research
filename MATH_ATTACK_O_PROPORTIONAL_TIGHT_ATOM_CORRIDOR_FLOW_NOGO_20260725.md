# Lane O: proportional tight atoms — exact corridor-flow obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Retain the notation of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`:

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 p=\left\lfloor\frac Wb\right\rfloor,
\]

\[
 N_{-d}=\binom{2m+1}{m-d},\qquad
 \beta_d=b_{-d}=\left\lfloor\frac{N_{-d}}p\right\rfloor.
\]

For the displayed Gaussian reduction,

\[
 b=\lfloor m^{3/4}\rfloor,
 \qquad
 H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,
 \qquad \alpha>1/\sqrt2.
\]

The requested proportional tight-atom matching lemma is **not proved** in
this report. The report instead gives a definitive obstruction to the
natural sequential corridor/min-cost-flow implementation.

The main theorem is stronger than a constant-factor failure. Start with an
arbitrary SCD of \(B_{2m}\), lift it to \(B_{2m+1}\) by either standard
one-coordinate product phase independently in every parent chain, select
the proportional complete symmetric columns, and try to route them through
one contiguous active interval at every radius. If the resulting number of
physical rows is \(p-t\), then

\[
 \boxed{
 \frac{t}{p/\sqrt m}\longrightarrow\infty.}
 \tag{0.1}
\]

Thus this entire product-SCD/BTK corridor class cannot attain the required
leave \(o(p/\sqrt m)\). The theorem permits:

1. an arbitrary parent SCD of \(B_{2m}\);
2. an independent choice of either product phase in every parent chain;
3. arbitrary central depth truncation of longer product chains to the
   required radius;
4. arbitrary selection of the proportional number of eligible chains; and
5. the full allowed atom leave \(t\).

The obstruction is a literal rotor signature. At every useful radius the
new product coordinate creates many chains which are forced sources or
forced sinks even against all clipped higher-radius chains. A physical row
with one active interval has only two boundary locations at that radius.

Two companion results isolate the scope.

* A fixed coordinate orientation, or even a menu of
  \(\exp(o(b^2/m))\) fixed orientations, covers only \(o(W)\) middle
  owners by vertex-disjoint length-\(b\) monotone geodesics.
* Raw first leave/add label capacity is not the obstruction: any surjective
  first deletion map uses one coordinate at most
  \((3/2+o(1))W/m=o(p)\) times, and the leave/add pairs admit an equitable
  proper \(p\)-edge-colouring.

Consequently a surviving corridor proof must evade each applicable
obstruction. It may retain enough two-parent consistency rather than merge
states as in Section 1; it may abandon one-interval product ownership by
using nonproduct states or the high fragmentation quantified in Corollary
3.4; and, if it models rows as monotone geodesics for fixed coordinate
bipartitions, it needs \(\exp(\Omega(b^2/m))\) orientation types. This is a
rigorous no-go for the stated corridor subclasses, not a counterexample to
the atom hypergraph itself.

## 1. Exact Pascal-strip state and the failure of marginal flow

### 1.1 Complete symmetric flag states

A complete symmetric radius-\(d\) column in \(B_{2m+1}\) is written

\[
 \gamma=(L;w_1,\ldots,w_{2d+1};R),
 \qquad |L|=|R|=m-d,
 \tag{1.1}
\]

and denotes the saturated flag

\[
 L\subset L+w_1\subset\cdots\subset
 L+w_1+\cdots+w_{2d+1}.
\]

Two consecutive columns of one literal injective interval word are related,
in one of the two orientations, by the exact rotor move

\[
 \boxed{
 (L;w_1,\ldots,w_{2d+1};R)
 \longmapsto
 (L-x+y;x,w_1,\ldots,w_{2d};R-y+w_{2d+1}),}
 \tag{1.2}
\]

where \(x\in L\) and \(y\in R\). Reversing the row reverses (1.2).
In particular, one common leave label and one common enter label control
all ranks of the column simultaneously.

This is the exact memory which an ordinary rankwise flow loses. If flow is
merged at a shared target set and then leaves in a state belonging to a
different incoming flag, the outgoing lower and upper parents need not use
the same \(x,y\), and the projected walk need not lift to an injective
interval word.

### 1.2 A literal Boolean holonomy witness

The failure already occurs in one four-set Boolean diamond. Consider the
four two-element pools

\[
\begin{array}{c|cc}
\text{pool}&1&2\\ \hline
B&\{1\}&\{2\}\\
X&\{1,3\}&\{2,4\}\\
Y&\{1,4\}&\{2,3\}\\
T&\{1,2,3\}&\{1,2,4\}.
\end{array}
\tag{1.3}
\]

Use ordinary inclusion on \(B-X,B-Y,X-T,Y-T\). The first three side
graphs have the identity as their unique perfect matching, while \(Y-T\)
has the transposition as its unique perfect matching. Hence every marginal
cover transport is integral and perfectly Hall-feasible, but there is no
coherent diamond. Starting from \(\{1\}\) forces \(\{1,3\}\) and
\(\{1,4\}\); these force different top sets. The same happens from
\(\{2\}\).

Therefore a network obtained by putting a capacity node at each Boolean
target and independently routing the two cover directions is not an exact
extended formulation of literal Pascal strips. Keeping the whole state
(1.1) prevents the illegal switch, but then the common target capacity is
a coupling between many state copies rather than a one-commodity network.

## 2. Fixed-orientation geodesics cover only \(o(W)\)

The next theorem rules out a different natural simplification: use one
coordinate bipartition and route every row monotonically across it.

### Theorem 2.1 (fixed-orientation Gaussian escape)

Let \(P\sqcup Q=[2m+1]\) be fixed. A \(P\)-to-\(Q\) monotone Johnson
geodesic is a path

\[
 X_0,X_1,\ldots,X_{b-1}\in\binom{[2m+1]}m
\]

such that

\[
 X_{j+1}=X_j-\{a_j\}+\{c_j\},
 \qquad a_j\in P,\quad c_j\in Q.
 \tag{2.1}
\]

If \(b/\sqrt m\to\infty\), every vertex-disjoint family of such
length-\(b\) paths covers

\[
 \boxed{
 O\!\left(W\exp\left[-c\frac{b^2}{m}\right]\right)=o(W)}
 \tag{2.2}
\]

middle sets, for an absolute constant \(c>0\).

More generally, if every selected path is monotone for one member of a
menu of \(K_m\) fixed coordinate bipartitions and

\[
 \log K_m=o(b^2/m),
 \tag{2.3}
\]

then their total covered middle mass is still \(o(W)\).

#### Proof

Put

\[
 h(X)=|X\cap Q|,
 \qquad
 \mu=\frac{m|Q|}{2m+1}.
\]

Along (2.1), \(h\) increases by one at every step. A path meeting the
central slab

\[
 |h-\mu|\le b/8
\]

has one endpoint satisfying

\[
 |h-\mu|\ge 3b/8-1.
 \tag{2.4}
\]

Distinct vertex-disjoint paths have distinct chosen endpoints. The paths
which miss the central slab use only vertices satisfying
\(|h-\mu|>b/8\).

For a uniformly random middle set, \(h\) is hypergeometric. The standard
sampling-without-replacement exponential-moment argument gives

\[
 \Pr(|h-\mu|\ge u)
 \le 2\exp(-2u^2/m).
 \tag{2.5}
\]

Thus the paths missing the slab cover at most
\(2W\exp[-b^2/(32m)]\) vertices.

There is no extra factor \(b\) for the paths meeting the slab. Starting
at a slab vertex, choose the longer of the two directions along the path;
it contains at least \((b-1)/2\) steps. Since \(h\) changes by one at
every step, at least \(b/8-O(1)\) vertices at the far end of this
subpath satisfy

\[
 |h-\mu|\ge b/4.
\]

The paths are vertex-disjoint. Hence their number is at most

\[
 \frac{|\{X:|h(X)-\mu|\ge b/4\}|}{b/8-O(1)},
\]

and all of those paths together cover at most

\[
 (8+o(1))|\{X:|h(X)-\mu|\ge b/4\}|
 \le(16+o(1))W\exp[-b^2/(8m)]
\]

vertices. Combining the two classes proves (2.2), for example with any
fixed \(c<1/32\). Grouping the paths by their menu orientation and summing
this bound gives

\[
 O\!\left(K_mW\exp[-c b^2/m]\right)=o(W)
\]

under (2.3). \(\square\)

For \(b=m^{3/4}+O(1)\), the forbidden menu size is
\(\exp(o(\sqrt m))\). Thus any construction in this
fixed-bipartition-monotone model which covers \((1-o(1))W\) owners needs
\(\exp(\Omega(\sqrt m))\) orientation types.

## 3. Standard product SCDs force too many rotor endpoints

This section contains the decisive theorem.

### 3.1 The full product class

Let \(\mathscr D\) be an arbitrary SCD of \(B_{2m}\). Write a parent
chain of radius \(r\) as

\[
 C_0\subset C_1\subset\cdots\subset C_{2r},
 \qquad
 C_j=L+z_1+\cdots+z_j,
 \tag{3.1}
\]

where \(|L|=m-r\). Introduce a new coordinate \(a\). Independently for
every parent chain, choose either of the two standard decompositions of
\(C\times B_{\{a\}}\).

The last-coordinate phase is

\[
\begin{aligned}
 &C_0<C_1<\cdots<C_{2r}<C_{2r}+a,\\
 &C_0+a<C_1+a<\cdots<C_{2r-1}+a,
\end{aligned}
\tag{3.2}
\]

and the first-coordinate phase is

\[
\begin{aligned}
 &C_0<C_0+a<C_1+a<\cdots<C_{2r}+a,\\
 &C_1<C_2<\cdots<C_{2r}.
\end{aligned}
\tag{3.3}
\]

The second chain is empty when \(r=0\). The union over parent chains is an
SCD \(\mathscr E\) of \(B_{2m+1}\). This class includes the standard
one-coordinate BTK recursion, but permits an arbitrary parent SCD and
arbitrary boxwise phases.

An \(\mathscr E\)-owned physical row means that every complete symmetric
column used by the row is the central truncation of a distinct chain of
\(\mathscr E\), and that consecutive active owned columns follow the rotor
move (1.2), or all follow its global reversal. At depth \(d\), the row is
**active** at a start only when it owns the full symmetric column from rank
\(m-d\) through rank \(m+d+1\), not merely its lower endpoint.

### Lemma 3.1 (product-coordinate signatures)

At native radius \(d\ge1\), every central depth-\(d\) truncation of an
\(\mathscr E\)-chain has the product coordinate \(a\) in one of four
locations:

\[
 a\in L,qquad a\in R,qquad a=w_1,qquad a=w_{2d+1}.
 \tag{3.4}
\]

The last two cases occur exactly once for every native-radius-\(d\)
parent chain of \(\mathscr D\): they are the long native-radius-\(d\)
child, with \(a\) first or last according to the chosen phase. Truncating
any child of native radius greater than \(d\) puts \(a\) in \(L\) or in
\(R\). A native-radius-\(d\) short child also puts \(a\) in \(L\) or
\(R\).

#### Proof

The long children in (3.2)--(3.3) have signatures

\[
 (L;z_1,\ldots,z_{2r},a;R),
 \quad (L;a,z_1,\ldots,z_{2r};R).
 \tag{3.5}
\]

A native-radius-\(d\) short child comes from a parent of radius \(d+1\).
In (3.2) it contains \(a\) in its bottom set; in (3.3) it avoids \(a\)
at its top and hence contains \(a\) in its exterior set.

For a native-radius-\(e\) state

\[
 (L;w_1,\ldots,w_{2e+1};R),\qquad e\ge d,
\]

its central depth-\(d\) truncation is exactly

\[
\begin{aligned}
 (&L+w_1+\cdots+w_{e-d};\\
 &w_{e-d+1},\ldots,w_{e+d+1};\\
 &R+w_{e+d+2}+\cdots+w_{2e+1}).
\end{aligned}
\tag{3.6}
\]

If \(e>d\), a first singleton moves into the new bottom and a last
singleton moves into the new exterior. Equations (3.5)--(3.6) prove the
claim. \(\square\)

### Lemma 3.2 (forced source/sink law)

In the compatibility digraph induced by **all** central depth-\(d\)
truncations of \(\mathscr E\)-chains:

* a native-radius-\(d\) long child with \(a=w_{2d+1}\) has indegree zero;
* a native-radius-\(d\) long child with \(a=w_1\) has outdegree zero.

This remains true after every higher-native-radius chain is admitted as a
possible clipped predecessor or successor.

#### Proof

Use the rotor orientation (1.2). If a state with \(a=w_{2d+1}\) had a
predecessor, that predecessor would have \(a\) in its penultimate
singleton position. If a state with \(a=w_1\) had a successor, the
successor would have \(a\) in its second singleton position. Lemma 3.1
shows that neither signature occurs anywhere in the clipped product
dictionary. \(\square\)

### Theorem 3.3 (supercritical product-SCD deficit)

Let the integers \(b=b(m)\) and \(H=H(m)\) satisfy

\[
 \frac b{\sqrt m}\longrightarrow\infty,
 \qquad
 \frac H{\sqrt m}\longrightarrow\infty,
 \qquad
 H=o(b),
 \qquad
 b=o(m).
 \tag{3.7}
\]

For \(0\le d\le H\), put

\[
 N_d=N_{-d}=\binom{2m+1}{m-d},
 \qquad
 \beta_d=\left\lfloor\frac{N_d}{p}\right\rfloor,
 \qquad
 R_d=N_d-p\beta_d,\qquad 0\le R_d<p.
 \tag{3.8}
\]

Fix one product SCD \(\mathscr E\) constructed in Section 3.1, and let
\(0\le t\le p\). Suppose \(s=p-t\) pairwise target-disjoint, fully
\(\mathscr E\)-owned
physical rows of \(b\) central starts are selected. Suppose also that,
for every depth \(d\), the starts owning a complete symmetric
depth-\(d\) column form one interval of cardinality \(\beta_d\) in each
row. Then

\[
 \boxed{
 \frac{t}{p/\sqrt m}\longrightarrow\infty.}
 \tag{3.9}
\]

In particular, no construction in this class proves the proportional
tight-atom matching lemma.

#### Proof

Fix \(1\le r\le H\). The number of native-radius-\(r\) parent chains in
an arbitrary SCD of \(B_{2m}\) is

\[
 E_r=\binom{2m}{m-r}-\binom{2m}{m-r-1}.
 \tag{3.10}
\]

There is exactly one long native-radius-\(r\) child per such parent, so
Lemma 3.2 gives exactly \(E_r\) forced sources or sinks at depth \(r\).
There are \(N_r\) eligible odd chains of native radius at least \(r\).
The selected rows use exactly \(s\beta_r\) eligible chains. Hence the
number of eligible chains left inactive is

\[
 N_r-s\beta_r
 =R_r+t\beta_r.
 \tag{3.11}
\]

Even if every inactive chain is chosen from the forced family, the number
of active forced states is at least

\[
 E_r-R_r-t\beta_r.
 \tag{3.12}
\]

By hypothesis the active depth-\(r\) starts form one interval in each
physical row. A forced source can occur only at the first start of that
interval and a forced sink only at its last start. Thus at most two forced
states occur per row, and

\[
 E_r-R_r-t\beta_r\le2(p-t).
 \tag{3.13}
\]

There is an exact identity

\[
 \boxed{
 E_r=\frac{2r+1}{2m+1}N_r.}
 \tag{3.14}
\]

Indeed,

\[
 \binom{2m}{m-r}
 =\frac{m+r+1}{2m+1}N_r
\]

and the difference ratio in (3.10) is
\((2r+1)/(m+r+1)\). Put

\[
 \theta_r=\frac{2r+1}{2m+1}.
\]

Using \(N_r=p\beta_r+R_r\) in (3.13) gives, whenever
\(\beta_r>2\),

\[
\begin{aligned}
 t(\beta_r-2)
 &\ge E_r-R_r-2p\\
 &=p(\theta_r\beta_r-2)-(1-\theta_r)R_r\\
 &\ge p(\theta_r\beta_r-3).
\end{aligned}
\tag{3.15}
\]

Now set

\[
 g_m=\frac b{\sqrt m},
 \qquad h_m=\frac H{\sqrt m},
 \qquad
 x_m=\min\left\{h_m-1,
       \sqrt{\log g_m-2\log\log g_m}\right\},
 \qquad
 r_m=\lfloor x_m\sqrt m\rfloor.
 \tag{3.16}
\]

By (3.7), \(x_m\to\infty\) and \(r_m\le H\) for all large \(m\).
The elementary binomial product gives, uniformly for this choice,

\[
 \frac{N_{r_m}}W
 =\prod_{j=0}^{r_m-1}\frac{m-j}{m+2+j}
 =\exp(-x_m^2+o(1)).
 \tag{3.17}
\]

Here \(x_m=O(\sqrt{\log m})\), so expansion of the logarithm has total
error \(O(x_m/\sqrt m+x_m^3/\sqrt m)=o(1)\).
Since

\[
 e^{-x_m^2}\ge\frac{(\log g_m)^2}{g_m},
\]

equations (3.8) and \(W/p=b+o(1)\) imply

\[
 \beta_{r_m}
 \ge(1-o(1))\sqrt m\,(\log g_m)^2.
 \tag{3.18}
\]

In particular \(\beta_{r_m}>2\),

\[
 \frac{\sqrt m}{\beta_{r_m}-2}=o(1),
 \qquad
 \sqrt m\,\theta_{r_m}=x_m+o(1).
 \tag{3.19}
\]

Multiply (3.15) by \(\sqrt m\) and use (3.19):

\[
 \frac{t}{p/\sqrt m}
 \ge
 \sqrt m\left(
 \theta_{r_m}-\frac{3-2\theta_{r_m}}{\beta_{r_m}-2}
 \right)
 =x_m-o(1)\longrightarrow\infty.
\]

This proves (3.9). \(\square\)

### 3.2 Specialization to the Gaussian atom parameters

For \(b=\lfloor m^{3/4}\rfloor\) and
\(H=\lceil\alpha\sqrt{m\log m}\rceil\), all hypotheses (3.7) hold.
Moreover

\[
 g_m=m^{1/4+o(1)},qquad
 h_m=\alpha\sqrt{\log m}+o(1),
\]

so (3.16) may be taken with

\[
 x_m=\left(\frac12-o(1)\right)\sqrt{\log m}.
\]

The concrete conclusion is therefore

\[
 \boxed{
 t\ge\left(\frac12-o(1)\right)
          \sqrt{\log m}\,\frac p{\sqrt m}.}
 \tag{3.20}
\]

The obstruction is already larger than the permitted leave by a diverging
factor.

### Corollary 3.4 (exact fragmentation price)

Retain the product-SCD hypotheses, but allow the common active depth-
\(r\) start set to have \(\gamma_r\) interval components rather than one.
Then the exact endpoint count becomes

\[
 \boxed{
 E_r-R_r-t\beta_r\le2(p-t)\gamma_r.}
 \tag{3.21}
\]

Consequently, if \(t=o(p/\sqrt m)\), then at

\[
 \widehat r_m=\lfloor\sqrt m\rfloor,
\]

\[
 \boxed{
 \gamma_{\widehat r_m}
 \ge(1-o(1))
       \frac{\theta_{\widehat r_m}\beta_{\widehat r_m}}2.}
 \tag{3.22}
\]

For the Gaussian parameters this forces

\[
 \boxed{
 \gamma_{\widehat r_m}
 \ge\left(\frac1{2e}-o(1)\right)m^{1/4}.}
 \tag{3.23}
\]

Thus fragmentation is a genuine possible escape from Theorem 3.3 only at
the price of a polynomial number of depth components in every row.

#### Proof

Every active interval has only one first position and one last position,
so Lemma 3.2 permits at most \(2\gamma_r\) forced states in one row. This
replaces (3.13) by (3.21).

At \(r=\widehat r_m\), the same elementary product expansion gives

\[
 E_r=\theta_r(p\beta_r+R_r),
 \qquad
 \theta_r=\frac{1+o(1)}{\sqrt m},
 \qquad
 \beta_r=(e^{-1}+o(1))b.
\]

In particular \(\theta_r\beta_r=(e^{-1}+o(1))g_m\to\infty\).

Moreover

\[
 \frac{R_r+t\beta_r}{E_r}
 \le
 \frac{p}{\theta_rp\beta_r}
 +\frac{t/p}{\theta_r}
 =o(1),
\]

because \(\theta_r\beta_r\to\infty\),
\(t/p=o(1/\sqrt m)\), and
\(\sqrt m\,\theta_r=1+o(1)\).
Hence (3.21) yields (3.22).

For \(g_m=m^{1/4+o(1)}\), half their product gives (3.23).
\(\square\)

## 4. First leave/add label capacity is not the obstruction

The previous theorem is a continuity obstruction. The raw first leave/add
label counts themselves have ample capacity. This section makes no claim
about all-depth label continuity.

### Proposition 4.1 (first-deletion coordinate cap)

Let

\[
 f:\binom{[2m+1]}m\longrightarrow\binom{[2m+1]}{m-1}
\]

be a surjective deletion map with \(f(X)\subset X\). For a coordinate
\(a\), put

\[
 D_a=\{X:f(X)=X-\{a\}\}.
\]

Then

\[
\boxed{
 |D_a|
 \le\binom{2m}{m-1}-\binom{2m}{m-2}
 =\frac{3mW}{(m+2)(2m+1)}
 =\left(\frac32+o(1)\right)\frac Wm.}
\tag{4.1}
\]

For \(b=m^{3/4}+O(1)\), this is \(o(p)\).

#### Proof

There are \(\binom{2m}{m-1}\) middle owners containing \(a\). Every
lower set containing \(a\) needs a distinct preimage because \(f\) is a
function and is surjective. There are \(\binom{2m}{m-2}\) such lower
sets, and none can be the image of a deletion of \(a\). Therefore at most
the difference in (4.1) of the \(a\)-containing owners can delete \(a\).
The displayed identity follows by elementary binomial ratios. \(\square\)

The complementary statement holds for a surjective first-addition map.

### Proposition 4.2 (equitable label binning)

Suppose every middle owner is assigned an ordered leave/add pair
\((a(X),c(X))\), and every coordinate occurs at most \(p\) times on each
side. Then these pairs can be partitioned into \(p\) classes whose sizes
differ by at most one and in which no leave label and no add label repeats.

#### Proof

Make a bipartite multigraph on two copies of \([2m+1]\), with one edge
\(a(X)c(X)\) for every owner. Its maximum degree is at most \(p\).
Kőnig's line-colouring theorem gives a proper edge-colouring with
\(p\) colours. If two colour classes differ in size by at least two, their
two-colour subgraph is a union of alternating paths and even cycles. An
alternating path with one more edge of the larger colour can be swapped,
decreasing the size difference by two without destroying properness.
Iteration makes all class sizes differ by at most one. \(\square\)

Thus one can bin the coordinate pairs into approximately \(b\)-edge
rainbow packets. What is missing is exactly endpoint continuity: a proper
colour class need not be a directed path under (1.2).

## 5. Independent audit and exact implication scope

The decisive product-SCD argument was audited independently.

1. The product signatures (3.5), the short-child locations of \(a\), and
   the clipping formula (3.6) were checked against both product phases.
   There is exactly one long native-radius-\(d\) child per native-radius-
   \(d\) parent, not two.
2. The rotor predecessor/successor test was checked against all clipped
   chains, not only against native-radius-\(d\) chains. The forbidden
   second and penultimate singleton signatures never occur.
3. The count of active forced states is exactly (3.12); the floor remainder
   is \(R_d\), and the atom leave contributes exactly \(t\beta_d\).
4. The two-endpoint capacity is per radius and per row. It uses the stated
   one-interval hypothesis; it does not silently count endpoint incidences
   as distinct rows.
5. The exact identity (3.14) independently confirms all factors of two.

The theorem proves the following no-go:

> No fixed standard one-coordinate product/BTK SCD dictionary, with
> complete symmetric columns and one-interval proportional cutoffs, can be
> routed into \(p-o(p/\sqrt m)\) literal tight atoms.

It does **not** prove any of the following stronger assertions.

* It does not disprove the unrestricted matching lemma for
  \(\mathcal P_{m;b,H}\).
* It does not exclude a densely nonproduct SCD or a column dictionary which
  changes on a positive density of states.
* It does not exclude highly fragmented choices of the active start sets
  \(I_q\). Corollary 3.4 quantifies the required fragmentation but does not
  rule it out.
* It does not exclude a full state-retaining colored path-factor or an
  integral trade construction using exponentially many row-specific
  orientations.

Therefore the precise proved/conditional boundary is this:

> The already-audited rank-proportional Boolean capacities are feasible,
> and raw first leave/add label capacity does not obstruct rainbow binning. The
> state-merging marginal resource-node flow described in Section 1, every
> fixed or subexponential fixed-bipartition-monotone orientation menu, and the standard
> product-SCD/BTK common-row implementation with complete symmetric columns
> and one-interval cutoffs are rigorously closed. The unrestricted
> proportional tight-atom matching lemma remains open. A surviving proof
> must evade whichever of these restricted architectural hypotheses it
> uses; the present theorems do not force one unique replacement
> architecture.

No conditional exact-factor selector is asserted in this report.
