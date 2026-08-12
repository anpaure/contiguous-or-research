# Five-layer conflict lifting and an explicit growing-depth central-band theorem

Date: 2026-07-26

Method: pure hand mathematics only. No finite search, computation, solver,
or web input is used.

Audit: three independent adversarial derivations checked the direct
five-layer conflict codegree and strip ledgers; the growing-(J) ABKV
hypotheses and residual exponent; and the repeated-prefix, repair,
finite-erosion, and rank-imbalance arguments. All corrections from those
audits are incorporated below.

## 0. Outcome and exact scope

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

The adjacent three-layer construction in ASYMPTOTIC_MATCHING.md selects
directed Johnson edges while making their rank-\((m-1)\) intersections and
rank-\((m+1)\) unions globally distinct. This note first extends its
conflict formulation to the five ranks

\[
                    m-2,m-1,m,m+1,m+2.
\]

The direct extension is mathematically well defined but cannot be certified
by the same Delcourt--Postle theorem: after fixing one two-edge geodesic
window, there are \(\Theta(m^4)=\Theta(D^2)\) disjoint windows with the same
rank-\((m-2)\) intersection. Thus its size-four collision family has

\[
                         \Delta_{4,2}=\Theta(D^2),
\]

with no required power saving.

The correct reformulation packages a complete cyclic interval strip as one
matching edge. At depth two this is a simple \(10\ell\)-uniform hypergraph
with one class in each of the five ranks. At general depth \(J\) its
uniformity is

\[
                         K=2\ell(2J+1).
\]

Every deep collision is then a literal shared vertex, not a high-codegree
forbidden configuration. The structural recursion is

\[
\boxed{
 L_t^{q+1}=L_t^q\cap L_{t+1}^q,\qquad
 U_t^{q+1}=U_t^q\cup U_{t+1}^q.}
\]

Uniformly for growing \(J<\ell<m\), the strip hypergraph has

\[
 \frac{D_J}{D_0}
 =\prod_{i=1}^J\frac{m+i}{m-i+1}
 =\exp\!\left(\frac{J^2}{m}
              +O\!\left(\frac{J^3}{m^2}\right)\right)
\]

and maximum pair codegree

\[
\boxed{\frac{\Gamma}{D_J}\le\frac{2\ell}{m-J}.}
\]

These estimates permit an explicit growing-\(J\) application of the
near-regular Alon--Bollobás--Kim--Vu matching theorem.

### Main theorem (explicit growing depth)

Let \(L=\log m\), \(\lambda=\log\log m\), and let
\(\omega=\omega(m)\) satisfy

\[
 \omega\longrightarrow\infty,\qquad
 \omega=o(L/\lambda).
\]

Set

\[
 J=\left\lfloor
       \sqrt{\frac{L}{64\omega\lambda}}
    \right\rfloor,
 \qquad
 \ell=\lceil\omega J\rceil.                                      \tag{0.1}
\]

Then there is a sequence \(T=(T_1,\ldots,T_n)\) of middle \(m\)-sets such
that

\[
 n=W+O(W/\omega)+o(W)=W+o(W),                                    \tag{0.2}
\]

every middle set occurs, every positive coordinate run has length at least
\(J+1\), and for every \(1\le q\le J\),

\[
 \left\{\bigcap_{s=0}^qT_{i+s}\right\}_i
       \supseteq\binom{[2m]}{m-q},\qquad
 \left\{\bigcup_{s=0}^qT_{i+s}\right\}_i
       \supseteq\binom{[2m]}{m+q}.                                \tag{0.3}
\]

Consequently the maximal delay-\(J\) factor of \(T\), after deleting zero
entries, is a literal contiguous-OR sequence of length \(W+o(W)\) covering
every mask in the growing central band

\[
                         m-J,\ldots,m+J.                           \tag{0.4}
\]

This is a quantitative improvement over the existing fixed-\(J\) theorem:
it gives

\[
 J=\Theta\!\left(
 \sqrt{\frac{\log m}{\omega(m)\log\log m}}
 \right)\longrightarrow\infty
\]

with an explicit rate. It does not prove coefficient one for all ranks:
this \(J\) is still far below the Gaussian tail-discarding scale.

## 1. The direct five-layer conflict formulation

Let

\[
 \mathcal M^{\rm out},\mathcal M^{\rm in}
\]

be two role clones of \(\binom{[2m]}m\), and let

\[
 \mathcal L_1=\binom{[2m]}{m-1},\qquad
 \mathcal U_1=\binom{[2m]}{m+1}.
\]

For every directed Johnson edge \(X\to Y\), put

\[
 e(X,Y)=
 \{X^{\rm out},Y^{\rm in},X\cap Y,X\cup Y\}.          \tag{1.1}
\]

The resulting directed cloned hypergraph is \(4\)-uniform. Its exact
degrees are

\[
 d(S)=d(U)=m(m+1),\qquad
 d(X^{\rm out})=d(X^{\rm in})=m^2,                   \tag{1.2}
\]

and, for \(m\ge2\), its maximum pair codegree is \(m\). Hence, with

\[
                         D=m(m+1),
\]

it is asymptotically regular and has \(\Delta_2=o(D)\).

A matching projects to a directed graph with indegree and outdegree at most
one, with globally distinct rank-\((m-1)\) edge intersections and
rank-\((m+1)\) edge unions.

### Lemma 1.1 (two selected steps are automatically geodesic)

If

\[
                  X_0\longrightarrow X_1\longrightarrow X_2
\]

comes from two edges of a matching in (1.1), then

\[
 \left|X_0\cap X_1\cap X_2\right|=m-2,\qquad
 \left|X_0\cup X_1\cup X_2\right|=m+2.              \tag{1.3}
\]

#### Proof

Write the first transition as removal of \(a_1\) and insertion of \(b_1\),
and the second as removal of \(a_2\) and insertion of \(b_2\). The two lower
edge colours are

\[
 X_1\setminus\{b_1\},\qquad X_1\setminus\{a_2\}.
\]

Their distinctness gives \(b_1\ne a_2\). The two upper colours are

\[
 X_1\cup\{a_1\},\qquad X_1\cup\{b_2\},
\]

so their distinctness gives \(a_1\ne b_2\). Thus neither transition reverses
the other, all two removals and two insertions are effective, and (1.3)
follows. \(\square\)

To enforce the five-layer target directly, define a configuration system
whose conflicts are:

1. unions of two distinct geodesic two-edge windows with the same
   rank-\((m-2)\) intersection;
2. the analogous equal rank-\((m+2)\) unions; and
3. projected short directed cycles, if a long linear forest is also wanted.

Only unions which are submatchings of (1.1) are declared conflicts. Two
overlapping two-windows give size-three conflicts; two disjoint windows give
size-four conflicts.

### Proposition 1.2 (fatal five-layer collision codegree)

For the size-four equal-lower-shadow conflicts,

\[
                         \Delta_{4,2}=\Theta(m^4)
                                      =\Theta(D^2).    \tag{1.4}
\]

The same statement holds for equal upper shadows. In particular the
Delcourt--Postle condition

\[
                         \Delta_{4,2}\le D^{2-\beta}
\]

fails for every fixed \(\beta>0\).

#### Proof

Fix a geodesic two-edge window \(P\), and let

\[
                         S=\bigcap_{X\in P}X
\]

have size \(m-2\). For any ordered four-tuple of distinct coordinates
\(a,b,c,d\notin S\), define

\[
 S\cup\{a,b\}\longrightarrow
 S\cup\{b,c\}\longrightarrow
 S\cup\{c,d\}.                                      \tag{1.5}
\]

Its lower depth-two shadow is \(S\). There are
\((m+2)_4=\Theta(m^4)\) such ordered four-tuples. If \(Q\) is the
four-coordinate support of \(P\), then every ordered quadruple from
\(([2m]\setminus S)\setminus Q\) gives a path whose middle-role clones
and rank-\((m\pm1)\) colours are disjoint from those of \(P\). Thus, for
\(m\ge6\), at least \((m-2)_4\) choices give a four-edge submatching.

Fixing the two lifted edges of \(P\) therefore leaves
\(\Omega(m^4)\) size-four conflicts containing them. Conversely, allocate
two fixed arcs among the four ordered path slots in at most twelve ways. If
they occupy one path, the other has at most \((m+2)_4\) choices. If they
are split between the two paths, each fixed arc has at most \((m-1)^2\)
geodesic one-arc extensions. Hence \(\Delta_{4,2}=O(m^4)\). Since
\(D=\Theta(m^2)\), this proves (1.4). Complementation gives the
upper-shadow case. \(\square\)

Thus the direct conflict formulation has been extended exactly to five
layers, but its natural black-box proof fails at a precise codegree. The
next construction removes that codegree by lifting every depth-two colour
into the base matching hypergraph.

## 2. Five-layer cyclic strips

Fix

\[
                         4\le\ell<m.
\]

Choose disjoint sets \(C,D\subset[2m]\) of size \(m-\ell\), and put

\[
                         R=[2m]\setminus(C\cup D),
                         \qquad |R|=2\ell.
\]

Give \(R\) an undirected cyclic order
\(\gamma=(z_t)_{t\in\mathbb Z_{2\ell}}\), and write

\[
 I_\gamma(t,r)=\{z_t,z_{t+1},\ldots,z_{t+r-1}\}.
\]

For \(-2\le d\le2\), take all \(2\ell\) masks

\[
                         C\cup I_\gamma(t,\ell+d),
                         \qquad t\in\mathbb Z_{2\ell}. \tag{2.1}
\]

Their union is one edge of the five-layer strip hypergraph
\(\mathcal S_{m,\ell,2}\). It has exactly

\[
                         5(2\ell)=10\ell             \tag{2.2}
\]

vertices.

Its middle row is the cyclic Johnson sequence

\[
                         T_t=C\cup I_\gamma(t,\ell).  \tag{2.3}
\]

Direct cyclic interval geometry gives

\[
\begin{aligned}
 T_t\cap T_{t+1}
   &=C\cup I_\gamma(t+1,\ell-1),\\
 T_t\cup T_{t+1}
   &=C\cup I_\gamma(t,\ell+1),\\
 T_t\cap T_{t+1}\cap T_{t+2}
   &=C\cup I_\gamma(t+2,\ell-2),\\
 T_t\cup T_{t+1}\cup T_{t+2}
   &=C\cup I_\gamma(t,\ell+2).                       \tag{2.4}
\end{aligned}
\]

Thus a matching in \(\mathcal S_{m,\ell,2}\) gives vertex-disjoint middle
cycles whose rank-\((m\pm1)\) and rank-\((m\pm2)\) shadow colours are all
globally distinct. The five-layer collision constraints have become
ordinary matching constraints.

### Proposition 2.1 (exact five-layer ledger)

The strip hypergraph is simple, has

\[
 |E(\mathcal S_{m,\ell,2})|
   =\frac{(2m)!}{4\ell(m-\ell)!^2},                  \tag{2.5}
\]

and every rank-\((m+d)\) vertex, \(-2\le d\le2\), has degree

\[
 D_d=\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.              \tag{2.6}
\]

In particular

\[
 \frac{D_2}{D_0}
  =\frac{(m+1)(m+2)}{m(m-1)}
  =1+\frac4m+O(m^{-2}).                              \tag{2.7}
\]

If \(\Gamma\) is the maximum pair codegree and \(D=D_2\), then

\[
                         \frac{\Gamma}{D}
                         \le\frac{2\ell}{m-2}.         \tag{2.8}
\]

#### Proof

The lowest row in (2.1) consists of all cyclic
\((\ell-2)\)-intervals with the same core \(C\). Its total intersection
recovers \(C\), and its total union recovers \(C\cup R\), hence also \(D\).
Since \(\ell-2\ge2\), two coordinates of \(R\) are adjacent in \(\gamma\)
exactly when they occur together in \(\ell-3\) members of this row; a
nonadjacent pair occurs together in at most \(\ell-4\). Thus the row
recovers the undirected cycle and the hypergraph is simple.

There are

\[
 \binom{2m}{m-\ell}
 \binom{m+\ell}{m-\ell}
 \frac{(2\ell-1)!}{2}
 =\frac{(2m)!}{4\ell(m-\ell)!^2}
\]

choices, proving (2.5). Every edge has \(2\ell\) vertices in each rank.
Double-counting incidences with
\(\binom{2m}{m+d}\) rank-\((m+d)\) vertices proves (2.6), and (2.7)
is immediate.

For (2.8), fix distinct band vertices \(X,Y\). The stabilizer of \(X\)
has orbit on \(Y\) of size

\[
 \binom{|X|}{|X\cap Y|}
 \binom{2m-|X|}{|Y\setminus X|}.                    \tag{2.9}
\]

If this product is not one, it is at least \(m-2\). Product one would force
\(Y\in\{\varnothing,X,X^c,[2m]\}\). The first and last are outside the
five layers, \(X\ne Y\), and \(X^c\) cannot co-occur with \(X\) because
every strip member contains the nonempty core \(C\).

All members of the orbit have the same codegree with \(X\), while each
strip through \(X\) has only \(2\ell\) vertices in the rank of \(Y\).
Therefore

\[
 \operatorname{codeg}(X,Y)(m-2)
 \le2\ell\,d(X)\le2\ell D,
\]

which proves (2.8). \(\square\)

For fixed \(\ell\), the usual almost-perfect matching theorem now gives a
five-layer strip matching leaving \(o(W)\) vertices in all five classes.
The quantitative growing-depth theorem below uses the same ledger uniformly.

## 3. The fixed-\(J\) strip hypergraph and its recursion

Let

\[
                         1\le J<\ell-1,\qquad \ell<m.
\]

For the same \(C,D,R,\gamma\), put into one edge every mask

\[
 C\cup I_\gamma(t,\ell+d),
 \qquad -J\le d\le J,\quad t\in\mathbb Z_{2\ell}.     \tag{3.1}
\]

Call the resulting hypergraph \(\mathcal S_{m,\ell,J}\). Its uniformity is

\[
                         K=2\ell(2J+1).               \tag{3.2}
\]

For the middle cyclic row \(T_t=C\cup I_\gamma(t,\ell)\), define

\[
 L_t^q=\bigcap_{s=0}^qT_{t+s},\qquad
 U_t^q=\bigcup_{s=0}^qT_{t+s}.                       \tag{3.3}
\]

### Lemma 3.1 (exact shadow tower)

For every \(0\le q\le J\),

\[
\boxed{
 L_t^q=C\cup I_\gamma(t+q,\ell-q),\qquad
 U_t^q=C\cup I_\gamma(t,\ell+q).}                    \tag{3.4}
\]

In particular,

\[
\boxed{
 L_t^{q+1}=L_t^q\cap L_{t+1}^q,\qquad
 U_t^{q+1}=U_t^q\cup U_{t+1}^q.}                    \tag{3.5}
\]

For fixed \(q\), all \(2\ell\) lower shadows and all \(2\ell\) upper
shadows are distinct.

#### Proof

The intersection of \(q+1\) consecutive cyclic \(\ell\)-intervals deletes
the first \(q\) residual coordinates and has length \(\ell-q\). Their union
starts at the first coordinate and has length \(\ell+q\). This is (3.4).
Applying the same interval identities to two adjacent \(q\)-shadows gives
(3.5). Since every displayed interval has length strictly between zero and
\(2\ell\), its cyclic start is determined, proving distinctness.
\(\square\)

This recursion is the structural reason the formulation scales from five
layers to fixed \(J\): the whole nested tower is encoded by one cyclic
interval system. A matching in \(\mathcal S_{m,\ell,J}\) is simultaneously
rainbow at every signed depth \(q\le J\).

### Theorem 3.2 (uniform degree and codegree ledger)

The hypergraph \(\mathcal S_{m,\ell,J}\) is simple. It has the same edge
count (2.5), and every rank-\((m+d)\) vertex, \(|d|\le J\), has degree

\[
 D_d=\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.              \tag{3.6}
\]

The minimum is \(D_0\), the maximum is \(D=D_J=D_{-J}\), and

\[
 \frac{D}{D_0}
 =\frac{(m+J)!(m-J)!}{(m!)^2}
 =\prod_{i=1}^J\frac{m+i}{m-i+1}.                   \tag{3.7}
\]

For \(J\le m/2\),

\[
 \log\frac{D}{D_0}
 =\frac{J^2}{m}
   +O\!\left(\frac{J^3}{m^2}\right),                 \tag{3.8}
\]

and the maximum pair codegree satisfies

\[
\boxed{
                         \frac{\Gamma}{D}
                         \le\frac{2\ell}{m-J}.}        \tag{3.9}
\]

Moreover, if \(\ell+J=o(m)\), then

\[
 \log D
 =2\ell\log m
  +O\!\left(\frac{\ell^2+J^2}{m}+1\right)
 =(2+o(1))\ell\log m.                                \tag{3.10}
\]

#### Proof

The lowest row in (3.1) consists of the cyclic
\((\ell-J)\)-intervals. Since \(\ell-J\ge2\), its intersection, union, and
pair co-occurrence counts recover \(C,R,D,\gamma\) exactly as in
Proposition 2.1. This proves simplicity.

Every edge has \(2\ell\) vertices in each rank. Double counting gives
(3.6). Also

\[
 \frac{D_{d+1}}{D_d}=\frac{m+d+1}{m-d}>1
 \qquad(d\ge0),
\]

which proves the extrema and (3.7). Expanding

\[
 \log\frac{D}{D_0}
 =\sum_{i=1}^J
   \left[
     \log\left(1+\frac{i}{m}\right)
    -\log\left(1-\frac{i-1}{m}\right)
   \right]
\]

gives (3.8), because the linear terms sum to \(J^2/m\) and the quadratic
error is \(O(J^3/m^2)\).

For distinct band vertices \(X,Y\), their stabilizer orbit has size

\[
 M(X,Y)=
 \binom{|X|}{|X\cap Y|}
 \binom{2m-|X|}{|Y\setminus X|}.                    \tag{3.11}
\]

If \(M(X,Y)>1\), then \(M(X,Y)\ge m-J\). If it equals one, the only
distinct in-band possibility is \(Y=X^c\), whose codegree with \(X\) is
zero because two disjoint masks cannot both contain the nonempty core
\(C\). Every strip through \(X\) contains at most \(2\ell\) members in
the rank of \(Y\). Orbit double counting gives

\[
 \operatorname{codeg}(X,Y)M(X,Y)
 \le2\ell\,d(X)\le2\ell D,
\]

which proves (3.9).

Finally

\[
 D_0=\frac{(m)_\ell^2}{2},
\]

so

\[
 \log D_0
 =2\sum_{i=0}^{\ell-1}\log(m-i)-\log2
 =2\ell\log m+O(\ell^2/m+1).
\]

Combine this with (3.8) to obtain (3.10). \(\square\)

For fixed \(J,\ell\), (3.8)--(3.9) recover the earlier fixed-depth
almost-perfect matching argument. Their value here is that every dependence
on \(J,\ell\) is explicit.

## 4. An explicit growing-\(J\) matching

We use the following previously audited near-regular
Alon--Bollobás--Kim--Vu theorem. Let a simple \(K\)-uniform hypergraph have
maximum degree \(D\), maximum pair codegree at most \(C_*\), and minimum
degree at least

\[
 D-f(D),\qquad
 f(D)=20(D^2C_*\log D)^{1/3}.                       \tag{4.1}
\]

If

\[
\begin{gathered}
 K>4,\qquad K\le\tfrac12\log D,\qquad f(D)\le D/10,\\
                         e^{2K}C_*\log D=o(D),
\end{gathered}                                        \tag{4.2}
\]

then there is a matching leaving at most

\[
 O\!\left[
 K\left(\frac{C_*\log(1+C_*)}{D}\right)^{1/(K-1)}
 |V|
 \right]                                             \tag{4.3}
\]

vertices uncovered.

Take \(L,\lambda,\omega,J,\ell\) as in (0.1), and put

\[
                         C_*=
 \left\lceil\frac{2\ell D}{m-J}\right\rceil.          \tag{4.4}
\]

The hypotheses on \(\omega\) imply

\[
\begin{aligned}
 J&=(1+o(1))
       \sqrt{\frac{L}{64\omega\lambda}},\\
 \ell&=(1+o(1))\omega J,\\
 K&=2\ell(2J+1)
    =(1+o(1))\frac{L}{16\lambda}.                    \tag{4.5}
\end{aligned}
\]

In particular \(J\to\infty\), \(J<\ell<m\), and
\(\ell+J=o(m)\).

### Theorem 4.1 (quantitative band matching)

For all sufficiently large \(m\), the hypergraph
\(\mathcal S_{m,\ell,J}\) has a matching whose total number \(U\) of
uncovered vertices over all \(2J+1\) rank classes satisfies

\[
\boxed{
                         U\le W(\log m)^{-12}.}        \tag{4.6}
\]

#### Proof

By (3.8), the relative degree defect is

\[
 1-\frac{D_0}{D}=O(J^2/m).                           \tag{4.7}
\]

Equations (3.9)--(3.10) and (4.4) give

\[
 \frac{C_*\log D}{D}
 =\Theta\!\left(\frac{\ell^2L}{m}\right),            \tag{4.8}
\]

and the right side tends to zero. Moreover,

\[
 \frac{J^2}{m}
 =o\!\left[
 \left(\frac{C_*\log D}{D}\right)^{1/3}
 \right].                                            \tag{4.9}
\]

Thus the minimum degree is at least \(D-f(D)\), and

\[
 \frac{f(D)}D
 =O\!\left[
 \left(\frac{\ell^2L}{m}\right)^{1/3}
 \right]=o(1).                                       \tag{4.10}
\]

Also \(K=o(\log D)\), so \(K\le\frac12\log D\). Finally,

\[
\begin{aligned}
 \log\left(
 e^{2K}\frac{C_*\log D}{D}
 \right)
 &\le -L+2K+O(\log(\ell^2L))\\
 &=-L+o(L),                                          \tag{4.11}
\end{aligned}
\]

which verifies the growing-uniformity condition.

Put

\[
                         \eta=
 \frac{C_*\log(1+C_*)}{D}.
\]

Here \(C_*/D=(2+o(1))\ell/m\), while
\(\log D=(2+o(1))\ell L\); hence
\(\log(1+C_*)=(1+o(1))\log D\). Therefore

\[
 \eta=\Theta(\ell^2L/m),\qquad
 \log\eta=-L+O(\lambda).                              \tag{4.12}
\]

Together with (4.5), this yields

\[
                         \eta^{1/(K-1)}
                         \le L^{-16+o(1)}.             \tag{4.13}
\]

The band has

\[
 |V|=W+2\sum_{q=1}^JN_q\le(2J+1)W.                  \tag{4.14}
\]

Substitution into (4.3) gives

\[
 \frac UW
 \le O\!\left(K(2J+1)L^{-16+o(1)}\right)
 \le L^{-29/2+o(1)}
 \le L^{-12},                                        \tag{4.15}
\]

for large \(m\). \(\square\)

If the matching has \(p\) strips, then its exact uncovered ledger is

\[
 U=(W-2\ell p)+
   2\sum_{q=1}^J(N_q-2\ell p).                       \tag{4.16}
\]

There is no separate collision error: all selected depth-\(q\) shadows are
globally distinct by matching disjointness.

## 5. Repeated-prefix linearization and exact repair

Fix an orientation and a starting point on every selected middle cycle

\[
                         X_0,X_1,\ldots,X_{2\ell-1}.
\]

Output the block word

\[
 \underbrace{X_0,\ldots,X_0}_{J\ {\rm extra\ copies}},
 X_0,X_1,\ldots,X_{2\ell-1},
 X_0,X_1,\ldots,X_{J-1},
 \underbrace{X_{J-1},\ldots,X_{J-1}}_{J\ {\rm extra\ copies}}.
                                                               \tag{5.1}
\]

Its length is exactly \(2\ell+3J\).

### Lemma 5.1 (all cyclic shadows survive)

For every \(0\le q\le J\), all \(2\ell\) cyclic \(q\)-windows of the
middle cycle occur contiguously inside (5.1).

#### Proof

A window starting at \(a\) already lies in
\(X_0,\ldots,X_{2\ell-1}\) if \(a+q<2\ell\). Otherwise its wrapped part
ends at \(X_{a+q-2\ell}\), whose index is at most \(J-1\). The repeated
prefix therefore contains it. Endpoint padding only adds entries.
\(\square\)

Let \(U_0=W-2\ell p\) be the missed middle count, and let
\(U_q^-,U_q^+\) be the missed rank-\((m-q)\) and rank-\((m+q)\) counts.
Thus

\[
                         U=U_0+\sum_{q=1}^J(U_q^-+U_q^+).          \tag{5.2}
\]

For a missing lower target \(S\) of rank \(m-q\), choose disjoint ordered
\(q\)-tuples outside \(S\) and append the geodesic path

\[
 Y_t=S\cup\{a_{t+1},\ldots,a_q\}\cup\{b_1,\ldots,b_t\},
 \qquad0\le t\le q.                                  \tag{5.3}
\]

Its intersection is \(S\). For a missing upper target \(Z\) of rank
\(m+q\), choose an \((m-q)\)-subset \(S\subset Z\), partition \(Z\setminus
S\) into two ordered \(q\)-tuples, and use (5.3); its union is \(Z\).

Pad every repair path by \(J\) extra copies of each endpoint. Treat every
missing middle set as a one-state gadget with \(J\) extra copies on each
side. Concatenate all selected block words and all repair gadgets.

### Proposition 5.2 (length and run ledger)

The resulting middle row \(T\) satisfies all shadow conditions (0.3),
contains every middle set, and every positive coordinate run has length at
least \(J+1\). Its exact length is at most

\[
\boxed{
 |T|
 \le W+\frac{3J}{2\ell}W+(3J+1)U.}                  \tag{5.4}
\]

#### Proof

Matching disjointness and Lemma 5.1 retain every selected shadow. Formula
(5.3) repairs every missed lower or upper target, and the singleton gadgets
insert every missed middle target.

An active residual coordinate has one cyclic positive run of length exactly
\(\ell\). In the repeated-prefix word it can be truncated only at an
endpoint. If an endpoint fragment does not already have length at least
\(\ell>J\), the \(J\) identical endpoint copies extend it to length at least
\(J+1\). Coordinates in \(C\) are constant one and coordinates in \(D\)
are constant zero. At a seam, endpoint runs either merge or retain the
\(J+1\) occurrences supplied on their own side.

Along a repair path every coordinate is constant, prefix-present, or
suffix-present. Its endpoint padding gives the same lower bound. Thus the
run assertion is exact.

The selected strips contribute \(p(2\ell+3J)\) entries. A missed middle
gadget has length \(2J+1\), and a signed depth-\(q\) repair has length
\(2J+q+1\le3J+1\). Since

\[
                         2\ell p+U_0=W,
\]

we obtain

\[
\begin{aligned}
 |T|
 &=p(2\ell+3J)+(2J+1)U_0\\
 &\quad+\sum_{q=1}^J(2J+q+1)(U_q^-+U_q^+)\\
 &\le W+3Jp+(3J+1)U\\
 &\le W+\frac{3J}{2\ell}W+(3J+1)U,
\end{aligned}
\]

which is (5.4). \(\square\)

By (0.1), \(J/\ell=(1+o(1))/\omega\), while Theorem 4.1 gives
\(JU=o(W)\). Therefore (5.4) proves (0.2).

## 6. Literal contiguous-OR realization

There are two integral realizations. The first factors the middle row; the
second reads the same strip matching directly as an OR word.

### 6.1 Maximal delay factor

Let \(T=(T_1,\ldots,T_n)\) be the padded row from Proposition 5.2 and define

\[
 A_j=
 \bigcap_{i=\max(1,j-J)}^{\min(n,j)}T_i,
 \qquad1\le j\le n+J.                                \tag{6.1}
\]

### Lemma 6.1 (finite erosion identities)

If every positive coordinate run of \(T\) has length at least \(J+1\),
then

\[
                         T_i=\bigcup_{j=i}^{i+J}A_j.  \tag{6.2}
\]

Moreover, for every valid \(q\)-window with \(0\le q\le J\),

\[
\begin{aligned}
 \bigcap_{t=i-q}^iT_t
   &=\bigcup_{j=i}^{i+J-q}A_j,\\
 \bigcup_{t=i}^{i+q}T_t
   &=\bigcup_{j=i}^{i+J+q}A_j.                       \tag{6.3}
\end{aligned}
\]

#### Proof

Work coordinatewise. Every length-\((J+1)\) erosion window contributing
to an \(A_j\) in the first line of (6.3) contains the target interval
\([i-q,i]\), proving one inclusion. Conversely, a positive run containing
\([i-q,i]\) has length at least \(J+1\), so that interval extends inside the
run to a length-\((J+1)\) interval \([j-J,j]\), with
\(i\le j\le i+J-q\). This proves the reverse inclusion. The case \(q=0\)
is (6.2). The second line follows by substituting (6.2) and associating the
unions. Clipped boundary windows only weaken the erosion requirement and
give the same conclusion. \(\square\)

Every target in the central band is therefore the OR of one literal
contiguous interval of \(A\). Since

\[
 |A|=|T|+J=W+o(W),
\]

this proves (0.4). If some \(A_j\) is empty, delete it after fixing all
witness intervals. Removing zero entries preserves the OR and contiguity of
the remaining entries in every witness.

### 6.2 Direct shortest-row OR word

There is also a shorter proof which does not pass through the middle row.
For one selected strip put

\[
                         B_t=C\cup I_\gamma(t,\ell-J).             \tag{6.4}
\]

Then for every \(0\le r\le2J\),

\[
\boxed{
 \bigcup_{s=0}^rB_{t+s}
 =C\cup I_\gamma(t,\ell-J+r).}                    \tag{6.5}
\]

Thus the \(2J+1\) strip rows are exactly the ORs of the cyclic windows of
the shortest row. Output

\[
 B_0,B_1,\ldots,B_{2\ell-1},B_0,\ldots,B_{2J-1}       \tag{6.6}
\]

for every selected strip, and then append every one of the \(U\) uncovered
band masks as a one-letter word. Every selected band mask is witnessed by
(6.5), including the wrapping windows, and every missed mask witnesses
itself. The resulting literal nonzero OR word has length

\[
\begin{aligned}
 p(2\ell+2J)+U
 &\le W+\frac{J}{\ell}W+U\\
 &=W+O(W/\omega)+o(W).                               \tag{6.7}
\end{aligned}
\]

This direct realization is the cleanest coefficient-one consequence of the
strip matching. It does not produce a permutation of the middle layer; it
uses \(o(W)\) repetitions and arbitrary-rank singleton repairs, all of which
are permitted in a literal OR word.

## 7. A sharp limitation of equal rank occupancy

The growing theorem above is polylogarithmic, so rank imbalance is
negligible. At larger \(J\), equal use of \(2\ell\) slots in every rank has
an exact cost.

Because the smallest class is the outer rank \(m-J\), every matching has

\[
                         2\ell p\le N_J.
\]

Even an ideal matching saturating this class leaves at least

\[
 U_{\min}
 =(W-N_J)+2\sum_{q=1}^J(N_q-N_J)
 =W+2\sum_{q=1}^JN_q-(2J+1)N_J                    \tag{7.1}
\]

band vertices uncovered.

### Proposition 7.1 (rank-imbalance asymptotic)

If \(J\to\infty\) and \(J=o(\sqrt m)\), then

\[
\boxed{
                         \frac{U_{\min}}W
                         =\left(\frac43+o(1)\right)
                           \frac{J^3}{m}.}             \tag{7.2}
\]

Consequently the separate padded-repair construction of Section 5 incurs

\[
 \frac{|T|-W}{W}
 \ge\left(\frac83+o(1)\right)\frac{J^4}{m}.           \tag{7.3}
\]

Thus, within the displayed regime \(J=o(\sqrt m)\), that particular
equal-occupancy middle-row scheme can have \(|T|=W+o(W)\) only if
\(J=o(m^{1/4})\). This is not a lower bound on
arbitrary OR words: direct singleton insertion, rank-dependent strip
occupancies, or shared repair gadgets can evade the padded-repair toll.

#### Proof

Uniformly for \(q\le J=o(\sqrt m)\),

\[
\begin{aligned}
 \frac{N_q}{W}
 &=\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}\\
 &=1-\frac{q^2}{m}+o(J^2/m).                         \tag{7.4}
\end{aligned}
\]

Substitute (7.4) into (7.1). The constant terms cancel, and

\[
\begin{aligned}
 \frac{U_{\min}}W
 &=\frac{(2J+1)J^2-2\sum_{q=1}^Jq^2}{m}
    +o(J^3/m)\\
 &=\left(\frac43+o(1)\right)\frac{J^3}{m},
\end{aligned}
\]

proving (7.2). In the Section 5 scheme every omitted outer target receives
two endpoint pads of length \(J\), so its repair costs at least \(2J\).
Equations (7.2)--(7.3) follow. \(\square\)

## 8. Proved boundary

The following statements are unconditional.

1. The direct five-layer configuration system exists, but its
   equal-depth-two-shadow conflicts have
   \(\Delta_{4,2}=\Theta(D^2)\), closing the direct Delcourt--Postle route.
2. The simple \(10\ell\)-uniform five-layer strip hypergraph has the exact
   degrees (2.6) and pair-codegree bound (2.8).
3. The recursion (3.5) packages all fixed depths into one matching edge.
4. The degree spread and pair-codegree estimates (3.8)--(3.10) are uniform
   for growing \(J,\ell\).
5. The quantitative growing-uniformity matching theorem applies at

   \[
   J=\Theta\!\left(
      \sqrt{\frac{\log m}{\omega\log\log m}}
   \right),
   \]

   and misses at most \(W(\log m)^{-12}\) targets over the whole band.
6. Repeated-prefix linearization plus exact repair gives the growing-depth
   middle-row theorem (0.2)--(0.3), while the shortest-row interpretation
   gives a literal OR word directly.
7. The construction remains far below the
   \(\Theta(\sqrt{m\log m})\) tail-removal scale. No full coefficient-one
   theorem is claimed.

The nontrivial advance beyond fixed \(J\) is therefore quantitative and
integral: an explicit square-root-polylogarithmic central band is covered by
one literal \(W+o(W)\) contiguous-OR word. The remaining coefficient-one
gate is a rank-balanced multiscale construction at Gaussian depth, not
five-layer compatibility.
