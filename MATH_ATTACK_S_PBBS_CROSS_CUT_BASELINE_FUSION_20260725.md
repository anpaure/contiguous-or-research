# PBBS cross-cut sharing after the corrected linear-cost ledger

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Exact outcome

Write

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\operatorname{Cat}_m=\frac{W}{2m+1}.
\]

The corrected residence ledger allows

\[
 J=\Omega(B\sqrt m)=\Omega(W/H)
\]

forced cuts in a Gaussian window. Therefore a repair costing \(cH\) new
letters independently at each cut can cost \(\Theta(W)\). The previously
proved \(4H-1\) one-cut dominance seam is valid, but it cannot by itself
give coefficient one.

This report proves four exact statements.

1. **Dense cuts really can share.** A rank-\(k\) Johnson block with \(M\)
   transitions has one word of exactly \(2M+1\) nonzero letters which
   represents every consecutive upper union and every floor-correct
   consecutive lower intersection in that block. Consequently all cuts
   contained in a diameter-\(\Delta\) cluster have one repair packet of
   length

   \[
   2\Delta+4H-1
   \]

   and exact overhead \(\Delta+2H-1\) over the retained owner segment,
   provided \(\Delta+2H-1\le m\). Thus \(\Theta(H)\) cuts of diameter
   \(O(H)\) have total overhead \(O(H)\) for all sufficiently large
   \(m\) in the Gaussian regime.

2. **There is no cluster-free standalone theorem.** A word of length
   \(L\) represents at most \(L\) distinct targets of one fixed rank.
   There is an explicit cyclic Johnson walk with \(r=\Theta(H)\) genuinely
   forced, \(H\)-separated cuts for which one rank alone has

   \[
   r(H-1)=\Theta(H^2)
   \]

   distinct floor-correct crossing targets. Every self-contained
   occurrence-preserving repair atlas therefore has quadratic length,
   even with arbitrary helper letters and arbitrary cross-cut sharing.

3. **The quadratic lower bound is not an excess lower bound.** The same
   forced example has an explicit no-cut word of length

   \[
   M+2H
   \]

   representing all upper and lower windows through depth \(H\). Its
   existing \(M\) baseline positions carry the necessary fixed-rank
   endpoints. Thus the viable escape is precisely an in-place,
   rank-monotone factorization, not an appended seam chart.

4. **Local ambient-wreath completions do not glue through overlapping
   genuine PBBS returns.** Two properly crossing or endpoint-touching
   zero-winding return arcs cannot both remain intact in one exact wreath
   factor, regardless of the \((m-s)!^2\) free core orders. Their forced
   owner arcs overlap, so owner uniqueness would put them in the same
   wreath; that wreath would then have two edges omitting the same
   coordinate. In a block of \(O(H)\) edges containing \(\Theta(H)\)
   overlapping return arcs of gap \(\Omega(H)\), all but \(O(1)\) returns
   per phase must therefore be rethreaded rather than merely assigned
   compatible local completions.

The resulting boundary is exact. A coefficient-one PBBS proof now needs a
global, baseline-relative deck braid in which, at every demanded rank, all
but the small overhead number of target witnesses reuse existing owner
starts, with compatible nesting wherever starts are shared across depths.
Neither a separate \(O(H)\) chart nor a choice of independent ambient
wreath completions can do this. Such a global braid is not proved here, so
coefficient one is not claimed.

## 1. A global staircase for an entire Johnson block

Let

\[
 X_0,X_1,\ldots,X_M\in\binom{\Omega}{k},
\qquad
 X_{i+1}=X_i-\{r_i\}+\{a_i\},
\]

and assume

\[
 0\le M\le k-1.
\tag{1.1}
\]

For \(0\le a\le b\le M\), put

\[
 L_{a,b}=\bigcap_{i=a}^{b}X_i,
\qquad
 U_{a,b}=\bigcup_{i=a}^{b}X_i.
\tag{1.2}
\]

Call the lower query floor-correct when

\[
 |L_{a,b}|=k-(b-a).
\tag{1.3}
\]

### Theorem 1.1 (global Johnson-block staircase)

Under (1.1), one nonzero literal word of exactly

\[
 \boxed{2M+1}
\tag{1.4}
\]

letters represents simultaneously

* every \(U_{a,b}\), with no rank hypothesis;
* every floor-correct \(L_{a,b}\); and
* every owner \(X_i\).

Thus the word replaces the \(M+1\) owner occurrences at exact overhead

\[
 \boxed{M}.
\tag{1.5}
\]

#### Proof

For each coordinate \(x\), decompose its zero-one indicator along
\(X_0,\ldots,X_M\) into maximal positive runs

\[
 [\alpha,\beta]\subseteq[0,M].
\]

Associate to a run the point

\[
 p=(-\alpha,\beta)\in[-M,0]\times[0,M].
\tag{1.6}
\]

A query interval \([a,b]\) is represented by

\[
 q=(-a,b).
\tag{1.7}
\]

The run contains the query if and only if \(p\ge q\) coordinatewise.

We first record the exact rank test.

### Lemma 1.2 (internal-run criterion)

The query \(L_{a,b}\) is floor-correct if and only if there is no maximal
positive run satisfying

\[
 a<\alpha\le\beta<b.
\tag{1.8}
\]

Equivalently, no run point lies strictly southwest of \(q=(-a,b)\).

#### Proof

Map every coordinate of \(X_a\) which is absent from \(L_{a,b}\) to its
first departure among the \(b-a\) internal transitions. This map is
injective.

If (1.8) holds, the departure at the end of that internal run is not the
first departure of an initial coordinate. The coordinate was either
absent initially, or had already departed before its displayed re-entry.
Hence at most \(b-a-1\) initial coordinates disappear and

\[
 |L_{a,b}|\ge k-(b-a)+1,
\]

so the query is not floor-correct.

Conversely, suppose equality in (1.3) fails. Then some internal departure
is not the first departure of a distinct coordinate of \(X_a\). Its
coordinate is either noninitial or has departed and re-entered. Its current
positive run therefore starts strictly after \(a\) and ends strictly before
\(b\), giving (1.8). \(\square\)

The exact Pascal break is now explicit. For \(1\le a\le b\le M-1\), put

\[
 R_{a,b}
 =
 L_{a,b}\setminus
 \bigl(L_{a-1,b}\cup L_{a,b+1}\bigr).
\tag{1.9}
\]

Then \(R_{a,b}\) consists exactly of coordinates whose maximal positive
run is \([a,b]\), and

\[
 \boxed{
 L_{a,b}
 =
 L_{a-1,b}\cup R_{a,b}\cup L_{a,b+1}.}
\tag{1.10}
\]

Thus the two extension children union to their parent exactly when
\(R_{a,b}=\varnothing\). Each child either equals the parent or deletes
exactly one coordinate. If \(R_{a,b}=\varnothing\) and both children are
proper, they delete different coordinates and are distinct facets.
Without the empty-pin hypothesis the two proper children can coincide;
without properness one child can equal its parent. A short coordinate run
breaks Pascal cancellation by contributing its literal pin to
\(R_{a,b}\).

Let \(\mathcal D\) be the set of distinct run points. Take its Pareto-minimal
points, ordered with first coordinate increasing; their second coordinates
strictly decrease. Augment this ordered list by

\[
 (-M,M)\quad\hbox{and}\quad(0,0),
\]

deleting repetitions. Between successive augmented points, move first east
and then south by unit lattice steps. Call the resulting southeast path
\(\Gamma\).

The path has \(M\) east and \(M\) south steps, and hence exactly \(2M+1\)
vertices. Every vertex \(z=(u,v)\) lies in the valid-interval region
\(-u\le v\): eastward motion decreases the left endpoint \(-u\), and a
subsequent southward segment stops at a valid endpoint. Define

\[
 I_z=[-u,v],
\qquad
 W_z=\bigcap_{i=-u}^{v}X_i.
\tag{1.11}
\]

Emit the \(W_z\)'s in their order along \(\Gamma\). Since \(I_z\) has at
most \(M\) transitions,

\[
 |W_z|\ge k-M\ge1,
\tag{1.12}
\]

so every letter is nonzero.

We use the standard rectangle-interception fact. If a query point \(q\)
has no run point strictly southwest of it and \(p\in\mathcal D\) satisfies
\(p\ge q\), then

\[
 \Gamma\cap[q,p]\ne\varnothing.
\tag{1.13}
\]

Indeed, choose a Pareto-minimal \(d\le p\). If \(d\ge q\), use \(d\).
Otherwise \(d\) is west and north of \(q\), or east and south of \(q\).
In the first case follow the path forward until its first coordinate
reaches \(q_1\); the east-before-south convention and the absence of a
strict southwest minimum keep the second coordinate at least \(q_2\).
The resulting point is still at most \(p\). The second case is the
backward vertical analogue.

Now let \(q=(-a,b)\) be floor-correct. If \(z\ge q\), then \(I_z\)
contains \([a,b]\), so \(W_z\subseteq L_{a,b}\). Conversely, if
\(x\in L_{a,b}\), choose the positive run \(p\) of \(x\) which contains
\([a,b]\). Then \(p\ge q\), and Lemma 1.2 plus (1.13) gives
\(z\in\Gamma\cap[q,p]\). The interval \(I_z\) lies inside that run, so
\(x\in W_z\). Therefore

\[
 \boxed{
 L_{a,b}
 =
 \bigcup_{\substack{z\in\Gamma\\z\ge(-a,b)}}W_z.}
\tag{1.14}
\]

Along \(\Gamma\), the first coordinate is nondecreasing and the second is
nonincreasing. Thus the first inequality in \(z\ge(-a,b)\) is a suffix
condition and the second is a prefix condition; the selected vertices form
one contiguous subword.

It remains to prove every upper union. Put

\[
 q^+=(-b,a).
\]

No run point is strictly southwest of \(q^+\): such a run would have
\(\alpha>b\) and \(\beta<a\), impossible because
\(\alpha\le\beta\) and \(a\le b\). A run \([\alpha,\beta]\) meets
\([a,b]\) exactly when its point \(p=(-\alpha,\beta)\) satisfies
\(p\ge q^+\). Thus the same rectangle-interception argument applies.

For a vertex \(z=(u,v)\), its interval \(I_z\) meets \([a,b]\) exactly
when

\[
 u\ge-b,\qquad v\ge a.
\tag{1.15}
\]

These again define one contiguous subpath. If \(W_z\) belongs to this
subpath, \(I_z\) contains an index of \([a,b]\), so
\(W_z\subseteq U_{a,b}\). Conversely, if \(x\in U_{a,b}\), choose a
positive run of \(x\) meeting \([a,b]\). Its point \(p\ge q^+\), and
rectangle interception supplies \(z\in\Gamma\cap[q^+,p]\). Then \(I_z\)
lies inside the chosen run and meets \([a,b]\), so \(x\in W_z\). Hence

\[
 \boxed{
 U_{a,b}
 =
 \bigcup_{\substack{z\in\Gamma\\I_z\cap[a,b]\ne\varnothing}}W_z.}
\tag{1.16}
\]

The indexing set is the contiguous subpath in (1.15). Singleton upper
queries in (1.16) also represent every owner \(X_i\). This proves all
claims. \(\square\)

## 2. Exact clustered-cut consequence

Index a cut by the edge between \(X_{c-1}\) and \(X_c\). Suppose the
selected cuts have extreme indices \(c_{\min}\) and \(c_{\max}\), and put

\[
 \Delta=c_{\max}-c_{\min}.
\tag{2.1}
\]

Every crossing window of at most \(H+1\) owners lies in the single block

\[
 X_{c_{\min}-H},\ldots,X_{c_{\max}+H-1}.
\tag{2.2}
\]

Its edge span is

\[
 M=\Delta+2H-1.
\tag{2.3}
\]

If \(M\le m\), Theorem 1.1 gives one packet of length

\[
 \boxed{2M+1=2\Delta+4H-1}
\tag{2.4}
\]

which represents every upper crossing union and every floor-correct lower
crossing intersection at every selected cut, while also representing all
owners in (2.2). Since (2.2) has \(M+1\) owners, the exact extra cost is

\[
 \boxed{M=\Delta+2H-1.}
\tag{2.5}
\]

In particular, any \(\Theta(H)\) cuts with \(\Delta=O(H)\) fuse at total
overhead \(O(H)\). For a partition into clusters of diameters
\(\Delta_\alpha\), the exact extra ledger supplied by this construction is

\[
\sum_\alpha(\Delta_\alpha+2H-1).
\tag{2.6}
\]

This is a self-contained block statement. If the owner block is physically
replaced inside a larger chronology, windows crossing its two outer
boundaries require intact witnesses elsewhere or an additional fusion
argument. The theorem exactly preserves every target wholly inside (2.2),
including all windows crossing the selected interior cuts; it does not by
itself prove a global packet-concatenation theorem.

The diameter term is real. The next sections show that it cannot be
removed by a universal standalone repair theorem.

## 3. Fixed-rank endpoint throughput

### Lemma 3.1 (one fixed rank per word position)

Let a literal word have length \(L\). It represents at most \(L\) distinct
sets of any one fixed cardinality.

#### Proof

Choose one witness interval for every represented target. Two witness
intervals with the same left endpoint are nested. Their unions are
therefore comparable by inclusion. Distinct sets of the same cardinality
are incomparable, so their chosen left endpoints are distinct. There are
only \(L\) possible left endpoints. \(\square\)

The same proof works with right endpoints.

Let \(D\) be a cut set on a cyclic Johnson walk, now indexing
\(e_c=X_cX_{c+1}\) by \(c\). At depth \(q\ge1\), a window of \(q+1\)
owners crosses the cut edge \(e_c\) exactly for starts

\[
 c-q+1,\ldots,c.
\]

Put

\[
 F_q(D)=
 \bigcup_{c\in D}\{c-q+1,\ldots,c\},
\qquad
 I_{i,q}=\bigcap_{h=0}^{q}X_{i+h}.
\tag{3.1}
\]

If all these intersections are floor-correct and no target value occurs
more than \(\mu_q\) times, every self-contained chart preserving all the
crossing occurrences obeys

\[
 \boxed{
 L\ge
 \left|\{I_{i,q}:i\in F_q(D)\}\right|
 \ge
 \left\lceil\frac{|F_q(D)|}{\mu_q}\right\rceil.}
\tag{3.2}
\]

If the cyclic gaps between successive cuts are \(g_1,\ldots,g_{|D|}\),
then exactly

\[
 \boxed{|F_q(D)|=\sum_j\min(q,g_j).}
\tag{3.3}
\]

Equations (3.2)--(3.3) allow arbitrary helper letters and arbitrary
sharing among cuts.

There is an essential scope qualification. For support-only PBBS repair,
one must replace the crossing occurrence family by the distinct target
sets whose other selected witnesses have all been destroyed. Equation
(3.2) applies without this qualification to a universal
occurrence-preserving seam, and it applies to support repair after that
essential-target statement is proved. Crossing occurrence count alone is
not support loss.

## 4. A sharp forced-run obstruction in the Johnson class

Fix \(H\ge2\), an integer \(r\ge1\), and put

\[
 M=2rH\le m+H.
\tag{4.1}
\]

Choose a core

\[
 |G|=m+1-H
\]

and distinct active coordinates \(a_0,\ldots,a_{M-1}\), with all indices
modulo \(M\). Define

\[
 \boxed{
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\}.}
\tag{4.2}
\]

The ground set can be enlarged by unused coordinates to size \(2m+1\);
(4.1) is exactly the required capacity inequality. It also implies
\(H\le m\), so \(G\ne\varnothing\). The \(X_i\)'s form a cyclic
rank-\((m+1)\) Johnson walk, since the transition from \(i\) to \(i+1\)
removes \(a_i\) and inserts \(a_{i+H}\).

For \(0\le t<r\), the coordinate

\[
 a_{(2t+1)H-1}
\]

has the positive owner run

\[
 [2tH,(2t+1)H-1].
\tag{4.3}
\]

Its insertion-to-departure edge collar is

\[
 \{e_{2tH-1},e_{2tH},\ldots,e_{(2t+1)H-1}\}.
\tag{4.4}
\]

Any path decomposition with no internally bounded positive run of at most
\(H\) owners must cut at least one edge of every collar (4.4). These
collars are disjoint, with \(H-1\) intervening edges between successive
collars. Hence any choice of one cut \(c_0,\ldots,c_{r-1}\), one from
each collar, has cyclic index separation at least \(H\).

Take depth

\[
 q=H-1.
\]

The \(H-1\) crossing-start sets associated with the selected cuts are
pairwise disjoint. Directly from (4.2),

\[
 \boxed{
 I_{i,H-1}
 =
 \bigcap_{j=0}^{H-1}X_{i+j}
 =
 G\cup\{a_{i+H-1}\}.}
\tag{4.5}
\]

These sets are all distinct and have cardinality

\[
 |G|+1=m+2-H=(m+1)-(H-1),
\]

so every one is floor-correct. Lemma 3.1 gives

\[
 \boxed{L\ge r(H-1)}
\tag{4.6}
\]

for every standalone occurrence-preserving repair atlas.

For fixed \(A>0\), take \(H=\lceil A\sqrt m\rceil\) and

\[
 r=\left\lfloor\frac{m+H}{2H}\right\rfloor.
\]

Then

\[
 r=\left(\frac{1}{2A^2}+o(1)\right)H
\]

and

\[
 \boxed{
 L\ge
 \left(\frac{1}{2A^2}+o(1)\right)H^2.}
\tag{4.7}
\]

The Pascal failure is completely visible. Put

\[
 P_i=I_{i,H-1}=G\cup\{a_{i+H-1}\}.
\]

Its two one-owner extensions satisfy

\[
 I_{i-1,H}=I_{i,H}=G.
\tag{4.8}
\]

Thus the two children collapse to the same set and their union misses the
unique short-run pin \(a_{i+H-1}\). The \(r(H-1)\) demanded parents in
(4.6) have distinct pins at one common rank.

This example also lifts integrally to the odd graph. Put

\[
 A_i=[2m+1]\setminus X_i,
\qquad
 B_i=X_i\cap X_{i+1}.
\]

Then \(A_i,B_i,A_{i+1}\) are consecutive rank-\(m\) vertices joined by
Kneser edges. The resulting alternating cycle is literal. It is not proved
to be a component of the canonical PBBS factor; (4.6) is a sharp
general-Johnson obstruction, not by itself a PBBS no-go.

## 5. The same obstruction has a no-cut factorization

The preceding example deliberately demonstrates why (4.6) cannot be read
as an excess lower bound. Define

\[
 E_j=G\cup\{a_j\},
\qquad j\in\mathbb Z/M\mathbb Z.
\tag{5.1}
\]

For \(0\le q\le H-1\),

\[
 \bigcap_{h=0}^{q}X_{i+h}
 =
 G\cup\{a_{i+q},\ldots,a_{i+H-1}\}
 =
 \bigcup_{j=i+q}^{i+H-1}E_j,
\tag{5.2}
\]

while for \(0\le q\le H\),

\[
 \bigcup_{h=0}^{q}X_{i+h}
 =
 G\cup\{a_i,\ldots,a_{i+H+q-1}\}
 =
 \bigcup_{j=i}^{i+H+q-1}E_j.
\tag{5.3}
\]

The depth-\(H\) lower intersection is the common set

\[
 \bigcap_{h=0}^{H}X_{i+h}=G.
\tag{5.4}
\]

Emit one cyclic period \(E_0,\ldots,E_{M-1}\), repeat its first
\(2H-1\) letters to linearize every interval in (5.2)--(5.3), and append
the one letter \(G\). This is a nonzero literal word of length

\[
 \boxed{M+2H}
\tag{5.5}
\]

covering every upper and lower window through depth \(H\), including every
owner. It has only \(2H\) overhead over the \(M\) baseline owners,
independently of the \(r(H-1)\) crossing demands.

This is the model rank-monotone sliding template which any successful
phase-sharing theorem must generalize.

## 6. Baseline threading is mathematically necessary

### Theorem 6.1 (common-start nested-flag necessity)

Suppose a literal word of length

\[
 L=M+e
\]

represents \(M\) distinct middle-rank owners and, at lower depth \(q\), a
family \(\mathcal T_q\) of \(D_q\) distinct equal-rank targets. Choose one
witness interval for every set.

Then at least

\[
 \boxed{D_q-e}
\tag{6.1}
\]

targets in \(\mathcal T_q\) share their left endpoint with a distinct
middle owner, and each such target is contained in that owner.

For a set \(Q\) of depths, at least

\[
 \boxed{
 \left[
 L-\left(e+\sum_{q\in Q}(L-D_q)\right)
 \right]_+}
\tag{6.2}
\]

left endpoints simultaneously carry a middle owner and one target at
every depth in \(Q\). At each such endpoint the represented sets form a
nested rank-monotone flag.

#### Proof

By Lemma 3.1, the chosen starts for the \(M\) owners are distinct, as are
the \(D_q\) starts at each lower rank. Their two start sets, both subsets
of the \(L\) word positions, intersect in at least

\[
 M+D_q-L=D_q-e
\]

positions. Intervals with one common start are nested, and the lower-rank
union must be the smaller set. This proves (6.1). Applying the union bound
to the complements of all the start sets gives (6.2). At a common start,
all interval unions are comparable; their distinct cardinalities put them
in rank order. \(\square\)

Thus an \(O(H)\)-overhead packet containing \(\Theta(H^2)\) or
\(\Theta(NH)\) baseline owners cannot be a small chart attached to those
owners. At each rank, all but at most \(e\) distinct lower targets must
reuse owner starts. This is not the assertion that almost every owner
carries every Gaussian-depth rank: \(D_q/M\) can be bounded away from one,
and the multi-depth bound (6.2) can be zero. Histogram cancellation or
target support alone does not supply the literal nesting at the starts
which are shared.

## 7. Overlapping genuine PBBS returns defeat local wreath completion

Let \(A_t\) be the canonical rank-\(m\) PBBS states and let

\[
 e_t=A_tA_{t+1}
\]

have omitted label \(\lambda_t\). A genuine zero-winding short return is
an interval

\[
 R=[i,j],
\qquad
 \lambda_i=\lambda_j,
\qquad
 0<j-i<2m+1.
\tag{7.1}
\]

The simple-return label theorem says that

\[
 \lambda_i,\lambda_{i+1},\ldots,\lambda_{j-1}
\]

are pairwise distinct. The owner-wreath theorem says that the forced owner
path

\[
 P_R=(A_i,A_{i+1},\ldots,A_j)
\tag{7.2}
\]

has \((m-s)!^2\) ambient exact wreath completions when \(j-i=2s+1\).

### Theorem 7.1 (crossing-return completion obstruction)

Let

\[
 R=[i,j],\qquad S=[p,q]
\]

be genuine zero-winding short returns with

\[
 i<p\le j<q.
\tag{7.3}
\]

No exact wreath factor can retain both forced paths \(P_R\) and \(P_S\)
intact inside its wreath rows.

#### Proof

The two paths share at least the owner \(A_p\), and in the endpoint-touching
case \(p=j\) they share \(A_j\). Since an exact wreath factor uses every
middle owner in exactly one row, intact embeddings of both paths would
have to lie in the same wreath row.

That row contains the edge \(e_i\), because \(i<j\), and it contains
\(e_j\), because \(p\le j<q\). Both edges omit the same coordinate:

\[
 \lambda_i=\lambda_j.
\]

But an exact \((2m+1,m)\)-wreath omits each ground coordinate on exactly
one edge. This is impossible. \(\square\)

A distinct return cannot be properly nested inside \(R\), because that
would repeat one of the internal labels in the simple list above.
Therefore every family of returns retained intact by ambient completion
has pairwise vertex-disjoint closed arcs.

Let \(\mathcal G\) be the conflict graph on demanded returns, joining two
arcs when they properly cross or touch. If \(\alpha(\mathcal G)\) is its
independence number, then at least

\[
 \tau(\mathcal G)
 =
 |\mathcal R|-\alpha(\mathcal G)
\tag{7.4}
\]

returns in each physical phase must be broken or rerouted before ambient
completion. More precisely, fix one nonwrapping quotient block and take
all \(2m+1\) literal coordinate translates of that same block. The cyclic
action on rank-\(m\) owners is free because
\(\gcd(2m+1,m)=1\), so the translated packet demands are distinct.
Applying the phasewise bound to this deck-equivariant family gives at
least

\[
 (2m+1)\tau(\mathcal G)
\tag{7.5}
\]

lifted return paths.

For a circular family with nonzero phase holonomy, the safe object is the
full phase-lifted conflict graph; its vertex-cover number is the exact
necessary rerouting count. The product bound (7.5) requires the translated
nonwrapping-block hypothesis just stated (or an equivalent zero-holonomy
identification).

More concretely, in a quotient block of \(L\le CH\) edges, return arcs of
gap at least \(\eta H\) have an intact packing of size at most

\[
 \left\lfloor\frac{L+1}{\eta H+1}\right\rfloor
 =
 O_{C,\eta}(1).
\tag{7.6}
\]

Thus a packet containing \(\Theta(H)\) such overlapping demands must
rethread \(\Theta(H)\) of them per phase. The factorial number of unused
core orders does not change this conclusion.

This is an architecture obstruction, not a word-length lower bound. One
nonlocal rethreading may break several return arcs, and a target may have
another witness. The theorem closes only the strategy of preserving every
local return segment and selecting compatible ambient completions.

There is also a global form which does not prespecify local completions.

### Theorem 7.2 (return-transversal edge-edit invariant)

Let \(P\) be the physical PBBS owner \(2\)-factor and let \(F\) be any
exact wreath factor on the same middle-owner vertex set. For every short
omitted-label return interval

\[
 R=[i,j],
\qquad
 \lambda_i=\lambda_j,
\qquad
 0<j-i<2m+1,
\]

the removed-edge set

\[
 S=E(P)\setminus E(F)
\]

meets the closed PBBS edge interval

\[
 \{e_i,e_{i+1},\ldots,e_j\}.
\tag{7.7}
\]

Consequently, for any family \(\mathcal I\) of short return intervals,

\[
 \boxed{
 |E(P)\setminus E(F)|
 \ge \tau(\mathcal I),}
\tag{7.8}
\]

where \(\tau(\mathcal I)\) is its minimum edge-transversal number.

#### Proof

Suppose all of \(e_i,\ldots,e_j\) remain in \(F\). Consecutive edges share
owners, so they all lie in one component row of \(F\). That row contains
the two distinct edges \(e_i,e_j\), both omitting the coordinate
\(\lambda_i=\lambda_j\). An exact wreath omits each coordinate on exactly
one edge, a contradiction. Thus \(S\) hits every return interval, proving
(7.7)--(7.8). \(\square\)

Under a residence lower bound of order \(W/H\), every exact wreath
rethreading therefore changes \(\Omega(W/H)\) PBBS edges. This does not
imply \(\Omega(W)\) literal overhead: an alternating trade can remove and
add edges entry-neutrally, and one changed edge can participate in a
larger baseline-threaded packet. It does prove that “no cut” cannot mean
retaining PBBS adjacency. Any successful no-cut word must reincarnate the
residence transversal as a global in-place rethreading.

## 8. Exact proved and unproved boundary

The corrected ledger is now reconciled as follows.

* The \(4H-1\) one-cut seam is valid but globally insufficient when
  \(J=\Omega(W/H)\).
* Theorem 1.1 gives genuine cross-cut sharing: \(\Theta(H)\) cuts in one
  \(O(H)\)-diameter block cost \(O(H)\) total overhead.
* Section 4 shows that no universal standalone \(O(H)\) packet can serve
  \(\Theta(H)\) separated forced cuts, even in a literal odd-graph cycle.
* Section 5 shows why this does not kill coefficient one: the required
  \(\Theta(H^2)\) endpoints can be recycled from the baseline in a
  sliding-core no-cut factorization.
* Theorem 6.1 proves that any \(W+o(W)\) solution must recycle baseline
  starts for all but \(o(W)\) target witnesses at each fixed demanded
  rank; it does not assert a full-depth flag at almost every owner.
* Theorem 7.1 shows that the audited local ambient-wreath completion of a
  genuine PBBS return is not composable across overlapping returns.
* Theorem 7.2 shows that every exact wreath factor on the same owners must
  edit an entire return transversal; local PBBS adjacency cannot simply be
  retained.

What remains unproved is one concrete statement:

> Partition the PBBS deck into blocks, each containing its existing
> baseline owner occurrences. Reorder or reletter those same positions,
> with only \(O(H)\) additional positions per block of \(\Theta(H)\)
> return demands, so that at every demanded rank all but \(O(H)\) target
> witnesses reuse distinct baseline starts, those sharing starts across
> depths are nested, all required upper flags remain literal, overlapping
> returns are serviced after nonlocal rethreading, and every middle owner
> is used exactly once globally.

This is stronger than histogram balance, support completeness, a list of
local seam charts, or independent wreath completion. It is exactly the
baseline-relative dynamic deck braid. No proof or counterexample to that
final PBBS-specific factorization is obtained here.

## 9. Independent audit

The decisive steps were audited independently.

* The \(2M+1\) theorem passed with the exact hypotheses
  \(M\le k-1\), inclusion of every maximal positive run, deletion of
  repeated Pareto/end points, and east-before-south connector order.
  The audit separately verified the upper identity, including the
  equivalence
  \[
  I_z\cap[a,b]\ne\varnothing
  \iff z\ge(-b,a).
  \]
* The forced sliding example passed with \(H+1\)-edge collars,
  \(H-1\) crossing starts per selected cut at depth \(H-1\), exact lower
  bound \(r(H-1)\), and no-cut length \(M+2H\).
* The overlap-rigidity theorem passed including the endpoint-touching
  case. The deck multiplier in (7.5) was restricted, as required, to a
  translated nonwrapping block (or an equivalent zero-holonomy setting);
  arbitrary circular phase holonomy must instead be handled in the full
  lifted conflict graph.

No audit promoted the remaining dynamic deck braid from an open condition
to a theorem.
