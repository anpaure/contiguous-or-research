# Gate B: a stable `j=2` near--far determinant and Venn-gap localization

**Date:** 2026-08-22

**Status.**  This note replaces the symmetric puncture-side pair, whose
leading determinant can be cancelled by rootless decorations, with a near--
far pair.  For the complete local blocker bank on at most six incident cuts,
its normalized determinant has an exact positive rational formula for every
`r>=23`:

\[
 \boxed{\det N_r={P(r)\over12Q(r)^2}>0,qquad
        \det N_r={2\over3}r^{-6}+{23\over6}r^{-7}
                    +O(r^{-8}).}                            \tag{0.1}
\]

In particular,

\[
                         \boxed{\det N_r\ge2^{-272}r^{-6}.} \tag{0.2}
\]

The same `2/3` leading coefficient survives the complete one-rootless-edge
dressing of the rooted-core truncation specified in Section 5.  The proof
uses a new refinement of the boundary-codegree theorem:
if `delta` is the total length outside the two largest elementary Venn gaps,
then, for `0<=delta<=r-2`,

\[
 \boxed{{\deg(J)\over D_M}
 \le32^{|J|-1}{r+2\over
  (\delta+1){r\choose\delta+1}}.}                           \tag{0.3}
\]

Thus every fixed polynomial order is controlled by finitely many local
offset types.  This does **not** yet sum rooted cores with more than six
incident cuts, arbitrary collections of rootless components, or the
all-depth zero-avoidance determinant.

## 1. The near--far finite bank

Put

\[
 b=2r+1,
 \qquad B_r=\operatorname {Cay}(\mathbb Z_b,
             \{\mathord\pm1,\mathord\pm3\}),
 \qquad p=0,\ q=5,
 \qquad D_M=2r\,r!(r+1)!.                                  \tag{1.1}
\]

Let `W_5` be the union of the graph balls of radius five about `p,q`.
In the full unpunctured graph, form the signed inclusion--exclusion bank
over every blocker set `J` satisfying

\[
 \{p,q\}\subseteq V(J),\qquad4\le|V(J)|\le6,
 \qquad V(J)\subseteq W_5,                                 \tag{1.2}
\]

with no connected-component restriction.  Let `L^(6)_(s,2)(t)` be its
profile after deleting the two start-zero edges at event shift `t`, and
let `C^(6)_(s,2)(t)` be the sum of the full-bank terms which use at least
one of those two deleted edges.  The full bank is translation invariant,
so

\[
 L^{(6)}_{s,2}(u)-L^{(6)}_{s,2}(t)
 =C^{(6)}_{s,2}(t)-C^{(6)}_{s,2}(u).                         \tag{1.3}
\]

Use the adjacent near defect and the far puncture defect

\[
 U_s={C^{(6)}_{s,2}(0)-C^{(6)}_{s,2}(1)\over D_M},
 \qquad
 V_s={C^{(6)}_{s,2}(r+2)-C^{(6)}_{s,2}(r+3)\over D_M},      \tag{1.4}
\]

and put

\[
                         N_r=\begin{pmatrix}
                         U_r&U_{r-1}\\V_r&V_{r-1}
                         \end{pmatrix}.                     \tag{1.5}
\]

This differs from the symmetric pair of the six-vertex rooted-core note:
the first row now has scale `r^-3`, while the second has scale `r^-2`.

## 2. Exact finite-cell calculation

For an ordered blocker tuple, let `c_eta` be its Boolean label-cell sizes,
`m_eta` the numbers of the four event labels in those cells, and `u_eta`
the positional-root counts.  Choosing one label from each event pair gives
the exact `j=2` weight

\[
 \prod_\eta(c_\eta-m_\eta)!
 \sum_\sigma\operatorname {sgn}(\sigma)
 \prod_\eta (u_\eta)_{h_\eta(\sigma)}
 (c_\eta-u_\eta)_{m_\eta-h_\eta(\sigma)}.                 \tag{2.1}
\]

This follows by replacing
`binom(c_eta-m_eta,u_eta-h_eta)u_eta!(c_eta-u_eta)!` with the
corresponding two falling factorials.  Fixing the first positional blocker
at relative start zero, the exact number of allowed cyclic translates is

\[
 b-\left|\{0,-d_1,\ldots,-d_m,-u\}\right|,                 \tag{2.2}
\]

where the `d_i` and `u` are the other relative blocker starts and the root
start.  Equations (2.1)--(2.2) therefore enumerate every retained
positional tuple without approximation.

For `r>=23`, five boundary-graph steps from `{0,5}` lift to `[-15,20]`
without collision.  Under the inverse cut map,

\[
 \phi_r(2h)=-h\pmod b,
 \qquad\phi_r(2h+1)=r-h\pmod b.                             \tag{2.3}
\]

Every blocker edge joins opposite parities.  Hence its two cuts lie in the
two bounded clusters in (2.3), and the Boolean cells have exactly two
macroscopic sizes `r+a,r+b`; the other cell sizes are bounded.  After their
factorials are removed, (2.1), (2.2), and the root-start sum give a
polynomial in `r` of degree at most six.  There are thirty-three
macroscopic-factor types.  Seven exact radii determine each degree-six
polynomial, and six unused radii, including `r=23`, replay the identities.

## 3. Exact sign certificate

The common denominator is

\[
 Q(r)=(r-10)(r-9)\prod_{h=1}^{8}(r-h)^2\,r^3(r+1).          \tag{3.1}
\]

Equation (0.1) holds with `x=r-23` and

\[
                         P(r)=\sum_{i=0}^{38}a_ix^i,        \tag{3.2}
\]

where the coefficients, in increasing order, are

\[
\begin{array}{r|r}
i&a_i\\ \hline
0&4879302165098587130178407895697767116328271872000\\
1&10418836712359730502268108374962675806477143244800\\
2&10821723411603219756330719548450827588423936245760\\
3&7284671057128420424450002380296060215147487035392\\
4&3572533175454373094057917812636180502733835629568\\
5&1360406211079774857416293749990375318508400891904\\
6&418638307308295855469400195468462471592018927872\\
7&106984746515332412820012510670520362656122966016\\
8&23155107302993587077489946141411571589906898944\\
9&4307248884501709536205867059318761818833509536\\
10&696454015218466098581245760020452234677292880\\
11&98757737134945312538646761464789878634110896\\
12&12367575620817162417747564889237481548731364\\
13&1375503654956603018031275156691076131786850\\
14&136469545458289462205785902317205620834716\\
15&12120795218380225270348028548451500649040\\
16&966331545077770682754310262301522609550\\
17&69294261365458380903851565739483250437\\
18&4475585443413186427689350381472343950\\
19&260578553411308374844647229702017735\\
20&13679789684461779556100247435748920\\
21&647369901151670196992941959915478\\
22&27593020498217064073661625953124\\
23&1057816441529317991807422874828\\
24&36400333471714234440156816760\\
25&1121249085255499694925044238\\
26&30808598953171545690748928\\
27&751757426126284259092386\\
28&16198929662894343538736\\
29&306087047607228353730\\
30&5026925281795765752\\
31&70948510689294668\\
32&847962843502330\\
33&8415287035765\\
34&67480822562\\
35&420101503\\
36&1905076\\
37&5598\\
38&8
\end{array}                                                  \tag{3.3}
\]

Every coefficient is positive, so (3.1)--(3.3) prove the sign for every
`r>=23`.  The four entries expand as

\[
\begin{aligned}
 U_r&=-{2\over3}r^{-3}-{7\over3}r^{-4}
                         +{7\over3}r^{-5}+O(r^{-6}),\\
 U_{r-1}&=-{2\over3}r^{-3}-{4\over3}r^{-4}
                         +{7\over3}r^{-5}+O(r^{-6}),\\
 V_r&={2\over3}r^{-2}-{5\over6}r^{-3}
                         +{29\over3}r^{-4}+O(r^{-5}),\\
 V_{r-1}&={2\over3}r^{-2}-{17\over6}r^{-3}
                         +{73\over6}r^{-4}+O(r^{-5}).       \tag{3.4}
\end{aligned}
\]

Their determinant is

\[
 \det N_r={2\over3}r^{-6}+{23\over6}r^{-7}
           -{163\over6}r^{-8}+O(r^{-9}).                   \tag{3.5}
\]

For (0.2), positivity gives
`P(r)>=8(x^38+1)>=2^-34(x+1)^38`.  Also
`x+1=r-22>=r/23`, and all twenty-two linear factors of `Q` are at most
`2r`.  Using `23^38<2^190` and `12<2^4` in (0.1) proves (0.2).

## 4. Venn-gap localization

Let `J` contain `t>=1` prescribed tagged central targets.  Write

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
\]

where `E(w)` is the directed punctured configuration of the cyclic word
`w`; thus each of its middle and lower targets has nonzero start.  List the
`q>=2` distinct original cut positions of `J` in cyclic order, and let
their positive elementary gaps be

\[
                         g_1\ge g_2\ge\cdots\ge g_q,
 \qquad\sum_i g_i=b,                                       \tag{4.1}
\]

and define

\[
                         \delta=\sum_{i=3}^qg_i.             \tag{4.2}
\]

### Theorem 4.1

If `0<=delta<=r-2`, then (0.3) holds.

#### Proof

Fix an anchor target.  A second central interval with prescribed length and
intersection has at most four possible relative starts.  Hence the number
of retained positional target tuples with the labelled Venn signature of
`J` is at most

\[
                         (b-1)4^{t-1}.                       \tag{4.3}
\]

If the labelled Venn-cell sizes are `n_tau`, compatible labels contribute
`V(J)=prod_tau n_tau!`.  Put `G(J)=prod_i g_i!`.  Refining the cells one
interval at a time gives

\[
                         V(J)\le8^{t-1}\prod_{i=1}^qg_i!.    \tag{4.4}
\]

Here is the full refinement argument.  Expose the targets one at a time and
write `R=V/G`.  If an old Venn cell of size `n` receives `a` labels of the
new target, its factorial contribution is multiplied by
`a!(n-a)!/n!=1/binom(n,a)`.  If a new cut splits an old elementary gap of
size `g` into `u,g-u`, the gap-factorial contribution is multiplied by
`1/binom(g,u)`.  When the two new cuts lie in different old gaps, choosing
the required labels independently in the split gaps injects into the
choice of the required labels in their containing Venn cells.  Hence the
product of the gap binomials is at most the product of the Venn-cell
binomials, and `R` cannot increase.  The same argument covers one new cut;
two old cuts can only decrease `V`.

If both new cuts lie in one old gap of size `g`, write the three pieces as
`x,y,z`, with `y` between the new cuts.  The gap-refinement factor is

\[
 {g!\over x!y!z!}={g\choose y}{g-y\choose x}.              \tag{4.4a}
\]

The middle piece has length `r` or `r-1`, or the complementary length.
The containing Venn-cell binomial cancels `binom(g,y)`.  Every old gap lies
inside one of the two arcs of the first exposed central target, so
`g<=r+2`.  Therefore `g-y<=3` in the first case and `g-y<=1` in the
complementary case.  The uncancelled factor in (4.4a) is at most
`2^(g-y)<=8`.  Thus each added target multiplies `R` by at most eight,
which proves (4.4).

Write `G=prod_i g_i!`.  Merging the gaps after the two largest gives
`prod_(i>=3)g_i!<=delta!`.  Every elementary gap is at most `r+2`.
Since `g_1+g_2=2r+1-delta` and `delta<=r-2`, factorial log-convexity moves
mass toward the larger gap and yields

\[
 G\le(r+2)!(r-1-\delta)!\,\delta!.                          \tag{4.5}
\]

The exact Venn count is the positional count times `V(J)`.  Divide
(4.3)--(4.5) by `D_M=(b-1)r!(r+1)!` and use

\[
 { (r+2)!(r-1-\delta)!\delta!\over r!(r+1)!}
 ={r+2\over(\delta+1){r\choose\delta+1}}.                  \tag{4.6}
\]

This proves (0.3). \(\square\)

For fixed `delta`, (0.3) is `O_t(delta! r^-delta)`.  A consequence needed
below avoids any assertion about the number of positions at fixed
`delta`.  Fix `t_0` and a family of `O_(t_0)(1)` rooted boundary-graph
shapes, each rooted at `{p,q}` and having at most `t_0-1` blocker edges;
to each realization adjoin one central blocker edge.  There are at most
`2b=O(r)` choices for that edge.  For
`7<=delta<=r/2`, the right side of (0.3) is largest at `delta=7`; hence the
sum over *all* edge positions is at most

\[
 O_{t_0}\left({r(r+2)\over8{r\choose8}}\right)
 =O_{t_0}(r^{-6}).                                         \tag{4.7}
\]

For `delta>r/2`, use the unsimplified bound (4.3)--(4.4).  Since
`q<=2t_0`, one has

\[
 g_3\ge {\delta\over q-2}\ge {r\over2(2t_0-2)},
 \qquad g_1,g_2\ge g_3.                                   \tag{4.8}
\]

Also every `g_i<=r+2`.  With `p_i=g_i/b`, the vectors `(p_i)` therefore
belong, up to `O(1/r)`, to the compact set

\[
 \sum p_i=1,qquad \max p_i\le {1\over2},qquad
 p_3\ge {1\over6(2t_0-2)}.
\]

On this set Shannon entropy is at least `log 2+c_(t_0)` for some
`c_(t_0)>0`: under `max p_i<=1/2`, equality at `log 2` is possible only
for `(1/2,1/2,0,...)`, which the lower bound on `p_3` excludes.  Stirling's
bounds now give, uniformly in this range,

\[
 {\prod_i g_i!\over r!(r+1)!}
 \le \exp(-c'_{t_0}r).                                    \tag{4.9}
\]

The positional factor (4.3), the at most `2b` edge choices, and the
bounded number of rooted core types are polynomial and are absorbed by
the exponential.  Combining (4.7)--(4.9) proves

\[
 \sum_{\substack{J:\text{from the fixed core family}\
                         \text{plus one edge},\ \delta(J)\ge7}}
 \deg(J)=O_{t_0}(D_Mr^{-6}).                               \tag{4.10}
\]

Multiplying by the rooted-current bound `2r` makes their normalized profile
contribution `O(r^-5)`.

## 5. The first rootless-edge sector

A blocker set is **rooted** when every one of its connected components
meets `{p,q}`.  Define the disjoint local bank
`F_(6,loc)^(1)` to consist of

1. every rooted blocker set with at most six incident cuts; and
2. every `J=J_0 dotcup {e}` in which `J_0` is rooted with at most five
   incident cuts, `e` is one boundary-vertex-disjoint rootless edge, and
   `delta(J)<=6`.

The two clauses are disjoint: the first has no rootless component and the
second has exactly one.  Let `N_(r,loc)^(1)` denote the near--far correction
matrix (1.4)--(1.5) formed from this bank.  This definition does not add
any blocker set twice.

For the full bank `F_(6,loc)^(1)`, the exact calculation (2.1)--(2.3) gives

\[
\begin{aligned}
 U_{r,\mathrm{loc}}^{(1)}&=-{2\over3}r^{-3}-{7\over3}r^{-4}
                         -{17\over6}r^{-5}+O(r^{-6}),\\
 U_{r-1,\mathrm{loc}}^{(1)}&=-{2\over3}r^{-3}-{4\over3}r^{-4}
                         -{17\over6}r^{-5}+O(r^{-6}),\\
 V_{r,\mathrm{loc}}^{(1)}&={2\over3}r^{-2}-{5\over6}r^{-3}
                         +{37\over3}r^{-4}+O(r^{-5}),\\
 V_{r-1,\mathrm{loc}}^{(1)}&={2\over3}r^{-2}-{17\over6}r^{-3}
                         +{89\over6}r^{-4}+O(r^{-5}).       \tag{5.1}
\end{aligned}
\]

Consequently

\[
 \det N_{r,\mathrm{loc}}^{(1)}={2\over3}r^{-6}+{23\over6}r^{-7}
                         -{181\over6}r^{-8}+O(r^{-9}).      \tag{5.2}
\]

Equation (4.10) shows that adjoining the omitted clause-2 edges with
`delta>=7` changes
each normalized row entry by `O(r^-5)`, hence changes (5.2) only by
`O(r^-7)` at determinant scale.  The same conclusion holds if clause 2 is
extended to rooted cores with six or more incident cuts.  Indeed, when
the core has six cuts, `delta<=6` leaves only `O(1)` local positions:
removing the two largest gaps leaves two cut clusters of total internal
length at most six, and the two event roots anchor those clusters.  The
two endpoints of the added edge therefore each have only `O(1)` choices.
The augmented set has at least eight cuts, so boundary codegree followed
by the `2r` current bound is `O(r^-5)`; `delta>=7` follows from (4.10).
For cores with at least seven cuts, the ordinary boundary-codegree sum is
already `O(r^-5)` after the free edge position and current factor are
included.  The bounded-degree shape series is geometric for large `r`.

Let `widehat N_r^(1)` instead use every set in clause 1 and every set
obtained by adjoining exactly one isolated rootless edge to an arbitrary
rooted core.  The preceding estimates prove that completing the edge
sector does not change the leading wedge of the six-cut rooted truncation:

\[
                         \boxed{\det\widehat N_r^{(1)}
                         ={2\over3}r^{-6}+O(r^{-7})>0}       \tag{5.3}
\]

for all sufficiently large `r`.  Equations (5.1)--(5.2) are the exact
local reconstruction used to obtain its leading coefficient.

## 6. Exact remaining gate

The isolated rootless-edge sector no longer threatens the determinant of
the six-cut rooted truncation.  Two classes are still unsummed:

1. pure rooted cores with at least seven incident cuts; their first
   unsigned near-row bound is `O(r^-4)`, so their wedge with the `r^-2`
   far row can occur at the leading `r^-6` scale;
2. a nontrivial rootless component, or two or more rootless components.

Their unsigned polymer activity is small, but converting that mass into
the required signed near-row and transverse-shore bounds still needs a
grouped cumulant theorem.  The exact residual is:

\[
 \boxed{\text{prove that the pure rooted }|V|\ge7\text{ tail and all
 higher rootless families perturb }\widehat N_r^{(1)}
 \text{ by }o(r^{-6})\text{ in wedge scale}.}              \tag{6.1}
\]

Uniform depth, multidepth coinstantiation, and stopped-process stability
remain separate downstream requirements.
