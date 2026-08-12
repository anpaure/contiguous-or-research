# Primal-dual audit of the fine strip-cover LP

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The claimed fractional value is correct:

\[
 \boxed{\tau^*_{m,H,h}
 =W_m+\frac Hh\binom{2m}{m-1}.}
\tag{0.1}
\]

It has a particularly short certificate.  The primal is the uniform
whole-strip vector at scale \(D_1^{-1}\), with singleton repair only on
the middle layer.  The dual puts weight one on every middle target,
weight \(H/(2h)\) on each of the two depth-one layers, and zero elsewhere.
Every strip column is dual-tight.

For an integral strip family there is also an exact nonnegative
integrality-gap ledger.  It shows that an \(o(W_m)\) gap is equivalent to
simultaneously:

1. choosing nearly the breakpoint number of strips;
2. having only \(o(W_m)\) excess collisions on the middle and first
   shadows; and
3. leaving only \(o(W_m)\) total holes over every deeper layer.

Thus the fractional calculation is not hiding an elementary rounding
argument.  It transfers the entire difficulty into the simultaneous
labelled collision ledger.

The critical three-layer strip hypergraph has excellent pairwise
geometry:

\[
 \frac{\Delta_2}{\Delta_1}\le\frac{2}{m+1}.
\tag{0.2}
\]

This rules out a pair-concentration obstruction and makes an
almost-matching theorem on the three critical layers plausible.  It does
not round the full band: a whole band column has
\(2h(2H+1)\) vertices, the deeper layers are deliberately overcovered,
and the remaining condition is a cover/discrepancy problem rather than a
matching problem.  No \(o(W_m)\) integral rounding or statewise
\(\Omega(W_m)\) obstruction is proved here.

## 1. The primal and its orbit solution

Write

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 c=2h+2H.
\tag{1.1}
\]

The fractional primal is

\[
 \begin{aligned}
 \min\quad&
 c\sum_{C\in\mathscr C_{m,h}}x_C+
 \sum_{S\in\mathcal B_{m,H}}z_S,\\
 \text{subject to}\quad&
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1,\\
 &x_C,z_S\ge0.
 \end{aligned}
\tag{1.2}
\]

Every strip contains \(2h\) distinct targets in each signed layer
\(q<h\).  Let \(D_q\) be the number of catalogue strips through a fixed
signed depth-\(q\) target.  Double counting gives

\[
 D_q=
 \frac{(m+q)!(m-q)!}{2(m-h)!^2},
 \qquad 0\le q<h.
\tag{1.3}
\]

In particular,

\[
 \frac{D_q}{D_1}=\frac{N_1}{N_q}\ge1\quad(q\ge1),
 \qquad
 \frac{D_0}{D_1}=\frac{N_1}{W}=\frac{m}{m+1}.
\tag{1.4}
\]

Set

\[
 x_C=\frac1{D_1}\quad\text{for every }C,
\qquad
 z_S=
 \begin{cases}
 1-\dfrac{N_1}{W},&|S|=m,\\
 0,&|S|\ne m.
 \end{cases}
\tag{1.5}
\]

Equation (1.4) proves feasibility.  Since

\[
 \frac{|\mathscr C_{m,h}|}{D_1}=\frac{N_1}{2h},
\tag{1.6}
\]

the value of (1.5) is

\[
 c\frac{N_1}{2h}+W-N_1
 =W+\frac HhN_1.
\tag{1.7}
\]

## 2. A matching dual certificate

The dual of (1.2) is

\[
 \begin{aligned}
 \max\quad&\sum_{S\in\mathcal B_{m,H}}y_S,\\
 \text{subject to}\quad&
 \sum_{S\in\mathcal T_H(C)}y_S\le c
       \quad(C\in\mathscr C_{m,h}),\\
 &0\le y_S\le1.
 \end{aligned}
\tag{2.1}
\]

Define

\[
 y_S=
 \begin{cases}
 1,&|S|=m,\\[1mm]
 \dfrac{H}{2h},&|S|=m-1\text{ or }m+1,\\[1mm]
 0,&\text{otherwise}.
 \end{cases}
\tag{2.2}
\]

The bound \(H<h\) makes (2.2) dual-feasible with respect to the singleton
columns.  Every strip contains \(2h\) middle targets and \(2h\) targets
on each depth-one side, so its dual column sum is

\[
 2h+2(2h)\frac{H}{2h}=2h+2H=c.
\tag{2.3}
\]

Thus every strip constraint is tight.  The dual objective is

\[
                         W+\frac HhN_1.
\tag{2.4}
\]

Equations (1.7) and (2.4) prove (0.1) by weak duality, with no appeal to
piecewise minimization.

The certificates also satisfy complementary slackness:

* every positive strip variable meets the tight equation (2.3);
* positive middle singleton repair meets \(y_S=1\);
* both depth-one primal layers are exactly saturated; and
* deeper layers may have slack because their dual weights vanish.

## 3. Exact integral gap decomposition

For an integral family \(\mathcal F\subseteq\mathscr C_{m,h}\), put

\[
                         s=|\mathcal F|.
\tag{3.1}
\]

Let \(U_0\) be the number of uncovered middle targets and let
\(U_q^\pm\) be the numbers of uncovered targets in the signed depth-\(q\)
layers.  Once \(\mathcal F\) is fixed, the optimal integral singleton
choice repairs exactly these targets, so its objective is

\[
 J(\mathcal F)
 =cs+U_0+\sum_{q=1}^H(U_q^-+U_q^+).
\tag{3.2}
\]

Define the unavoidable occurrence deficits

\[
 a_0(s)=(W-2hs)_+,\qquad
 a_1(s)=(N_1-2hs)_+
\tag{3.3}
\]

and

\[
 f(s)=cs+a_0(s)+2a_1(s).
\tag{3.4}
\]

Since one strip has only \(2h\) targets in any fixed layer,

\[
 U_0\ge a_0(s),\qquad
 U_1^\pm\ge a_1(s).
\tag{3.5}
\]

Subtracting the fractional optimum gives the exact identity

\[
\boxed{
\begin{aligned}
J(\mathcal F)-\tau^*
={}&[f(s)-\tau^*]
 +[U_0-a_0(s)]\\
&+[U_1^--a_1(s)]+[U_1^+-a_1(s)]\\
&+\sum_{q=2}^H(U_q^-+U_q^+).
\end{aligned}}
\tag{3.6}
\]

Every term on the right is nonnegative.

Let

\[
                         s_*=\frac{N_1}{2h}.
\tag{3.7}
\]

The breakpoint term is explicit:

\[
 f(s)-f(s_*)=
 \begin{cases}
 (4h-2H)(s_*-s),&s\le s_*,\\
 2H(s-s_*),&s_*\le s\le W/(2h),\\
 2H\!\left(W/(2h)-s_*\right)
 +(2h+2H)\!\left(s-W/(2h)\right),
 &s\ge W/(2h).
 \end{cases}
\tag{3.8}
\]

Consequently \(J(\mathcal F)=\tau^*+o(W)\) forces

\[
 s\ge s_*-o(W/h),
\qquad
 s\le s_*+o(W/H),
\tag{3.9}
\]

and every collision/hole term in (3.6) has total \(o(W)\).

There is no arithmetic obstruction from the nonintegrality of \(s_*\).
Taking \(s=\lceil s_*\rceil\) in the scalar ledger gives

\[
                         0\le f(s)-f(s_*)<2H,
\tag{3.9a}
\]

which is \(o(W)\).  Any macroscopic integral gap must therefore come from
the labelled collision/hole terms, not from rounding the number of
cycles.

When \(2hs=N_1\), equation (3.6) is especially transparent.  The middle
term

\[
                         U_0-(W-N_1)
\tag{3.10}
\]

is exactly the number of middle occurrences lost to collisions beyond
the unavoidable middle deficit.  At depth one, \(U_1^\pm\) is exactly
the collision count.  For \(q\ge2\), the selected strips supply \(N_1\)
occurrences, of which \(N_1-N_q\) collisions are arithmetically
unavoidable; \(U_q^\pm\) is precisely the excess collision count beyond
that baseline.

Thus at the fractional breakpoint the additive integrality gap is
literally the total excess-collision ledger over all signed layers.

## 3A. The exact depth-one combinatorial object

There is a useful phase-free reformulation of the zero-gap critical
ledger.  Form the bipartite containment graph

\[
 \mathcal G_1:
 \binom{\Omega}{m-1}\longleftrightarrow
 \binom{\Omega}{m+1},
 \qquad
 R\sim U\iff R\subset U.
\tag{3.11}
\]

An edge \(R\subset U\) has \(|U\setminus R|=2\).  Its two intermediate
middle sets are adjacent in the Johnson graph, with intersection \(R\)
and union \(U\).  Thus edges of \(\mathcal G_1\) are in bijection with
Johnson edges on \(\binom{\Omega}{m}\).

Each side of \(\mathcal G_1\) has \(N_1\) vertices, and every vertex has
degree

\[
                         \binom{m+1}{2}.
\tag{3.12}
\]

Hence \(\mathcal G_1\) has a perfect matching unconditionally.

### Proposition 3A.1 (critical zero-gap normal form)

Assume \(2hs=N_1\).  A strip family has

\[
                         U_1^-=U_1^+=0
\tag{3.13}
\]

if and only if its \(N_1\) Johnson transition edges correspond to a
perfect matching of \(\mathcal G_1\).  If in addition

\[
                         U_0=W-N_1,
\tag{3.14}
\]

then its strip cycles are vertex-disjoint on the middle layer.

#### Proof

Every strip transition supplies one pair
\((R,U)=(X_t\cap X_{t+1},X_t\cup X_{t+1})\), hence one edge of
\(\mathcal G_1\).  There are \(2hs=N_1\) transitions.  Having no lower
or upper hole means every vertex on both sides occurs at least once;
equality of occurrence and vertex counts makes every occurrence unique,
which is exactly a perfect matching.

The strips contain \(2hs=N_1\) middle occurrences.  Equation (3.14) says
that they cover \(N_1\) distinct middle vertices, so no two cycles share a
middle vertex. \(\square\)

Thus ordinary depth-one matching is not the obstruction: the regular
bipartite graph (3.11) already has a perfect matching.  The additional
requirements are that its corresponding Johnson edges form
vertex-disjoint physical \(C_{2h}\)'s and that the same cycles satisfy all
deeper cover constraints.

## 4. Pair codegrees on the critical three layers

Let \(\mathcal H_{\mathrm{crit}}\) be the hypergraph whose vertices are

\[
 \binom{\Omega}{m-1}\ \dot\cup\
 \binom{\Omega}{m}\ \dot\cup\
 \binom{\Omega}{m+1}
\tag{4.1}
\]

and whose edge corresponding to \(C\) is its \(6h\) targets on these
three layers.  Side vertices have degree \(D_1\), while middle vertices
have degree

\[
                         D_0=\frac{m}{m+1}D_1.
\tag{4.2}
\]

### Proposition 4.1 (exact worst pair scale)

For distinct critical vertices \(S,T\),

\[
 \deg(S,T)\le\frac{2D_1}{m+1}.
\tag{4.3}
\]

Equality occurs when one vertex is a middle set \(X\), the other is an
incident \((m-1)\)-subset \(R\subset X\), or dually an incident
\((m+1)\)-superset.

#### Proof

Fix a middle set \(X\).  Every strip through \(X\) supplies exactly two
incident lower depth-one targets.  The stabilizer of \(X\) is transitive
on its \(m\) subsets of size \(m-1\), so for fixed \(R\subset X\),

\[
 \deg(X,R)=\frac{2D_0}{m}=\frac{2D_1}{m+1}.
\tag{4.4}
\]

The upper formula follows by complementation.

For two middle sets at Johnson distance \(d<h\), every strip through the
first has exactly two middle states at distance \(d\); for \(d=h\) it
has one.  Hence their codegree is at most

\[
 \frac{2D_0}{\binom md^2}\le\frac{2D_0}{m^2}.
\tag{4.5}
\]

For two lower targets at Johnson distance one and \(h>2\), double
counting their cyclic positions gives

\[
 \frac{2D_1}{(m-1)(m+1)};
\tag{4.6}
\]

all other distance classes have larger orbit size.  When \(h=2\), distance
one is itself the maximal-distance class and occurs three times, giving
\(3D_1/(m^2-1)\), which is still bounded by (4.4) for \(m\ge3\).
The maximal-distance class for general \(h\) may likewise occur three
times but has a much larger denominator.  The same holds for two upper
targets.

For a lower \(R\) and upper \(U\) with \(R\subset U\), a strip through
\(R\) has exactly three upper depth-one intervals containing it.  Thus

\[
 \deg(R,U)
 =\frac{3D_1}{\binom{m+1}{2}}
 =\frac{6D_1}{m(m+1)}.
\tag{4.7}
\]

The remaining cross-distance orbits have larger denominators and no
larger cyclic multiplicity.  For \(m\ge3\), (4.5)--(4.7) are bounded by
(4.4). \(\square\)

Therefore the critical hypergraph is \(6h\)-uniform, almost regular, and
has relative maximum codegree \(O(1/m)\).  In the chosen regime
\(h=m^{3/4+o(1)}\),

\[
                         6h\,\frac{\Delta_2}{D_1}=o(1).
\tag{4.8}
\]

This is strong evidence for an almost-matching theorem on the three
critical layers.  It is not itself such a theorem, and even a critical
almost matching would not control the deeper targets in (3.6).

## 5. Why the full-band rounding is different

A whole strip column contains

\[
                         2h(2H+1)
\tag{5.1}
\]

band targets.  Its fractional load at depth \(q\) is \(N_1/N_q\), which
is one at \(q=1\) and larger than one for \(q>1\).  Thus deeper layers
must use their surplus occurrences with almost minimal excess collision;
they are not matching layers.

Although the worst pair-codegree ratio remains governed by the shallow
incidence scale \(O(1/m)\), the naive product

\[
 2h(2H+1)\,\frac{\Delta_2}{D_1}
 =\Theta\!\left(\frac{hH}{m}\right)
\tag{5.2}
\]

does not tend to zero for
\(h=m^{3/4+o(1)}\) and
\(H=\Theta(\sqrt{m\log m})\).  Consequently a direct invocation of a
sparse almost-matching theorem on the entire band is not justified.
Moreover, matching would wrongly forbid the unavoidable deeper-layer
collisions \(N_1-N_q\).

The exact rounding target furnished by (3.6) is a plateau-aware
multicover/discrepancy theorem:

\[
 \sum_{q=0}^H
 \bigl(\text{actual collisions at }q
       -\text{unavoidable collisions at }q\bigr)
 =o(W).
\tag{5.3}
\]

No theorem proving (5.3), and no statewise inequality forcing it to be
\(\Omega(W)\), is established here.

## 6. Rigorous frontier

The following points are now certified.

1. The value (0.1) has matching explicit primal and dual certificates.
2. Every integral gap decomposes exactly into the nonnegative terms
   (3.6); no hidden rounding loss remains outside that ledger.
3. At the optimal cycle mass, the gap is exactly aggregate excess
   collision across the band.
4. The critical three-layer incidence system has relative codegree at
   most \(2/(m+1)\), so there is no pairwise concentration obstruction.
5. The all-band problem is not a standard matching problem because its
   deeper layers have prescribed collision plateaux.

The unresolved assertion is a whole-strip integral selection whose
aggregate excess collision is \(o(W)\).  Pairwise sparsity is compatible
with such a selection but does not prove it.
