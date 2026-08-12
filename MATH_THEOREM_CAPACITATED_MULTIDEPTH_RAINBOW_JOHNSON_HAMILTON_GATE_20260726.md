# Capacitated multidepth-rainbow Hamilton cycles in \(J(2m,m)\)

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The unrestricted target-coverage problem has a clean formulation as a
capacitated rainbow/conflict Hamilton-cycle problem in the Johnson graph.
Its one-step conflict geometry is substantially better than a generic
colored graph:

* \(J(2m,m)\) has degree \(m^2\);
* a fixed signed depth-\(q\) color occupies one row or one column of the
  local exchange matrix, of size at most \(m\);
* all depths \(q\le H\) remain row/column constraints--there is no new
  two-dimensional local conflict; and
* a joint lower/upper depth-\(q\) flag has exactly \((2q)!\) oriented
  geodesic realizations.

Nevertheless, the numerical parameters

\[
                         D=m^2,\qquad
 \Delta_{\rm local}\le m,\qquad H=o(m)               \tag{0.1}
\]

do not imply a sequential absorption theorem.  At the level of these
numerical hypotheses, the bad rows may be distributed over the \(H\)
depths so that every individual
depth forbids only \(\lceil m/H\rceil\) rows while their union forbids all
\(m\) rows.  The same can happen to columns.  Thus a partial rainbow path
state permitted by the numerical hypotheses can have no legal
continuation even though every separate depth has \((1-o(1))m\) locally
available removals and insertions.  Proposition 5.1 below does not assert
that every such load state is canonically realizable by an earlier path.

The exact surviving condition is a *cross-depth row/column slack
invariant*.  If \(P\) is a return-free path prefix ending at \(X\), let
\(\mathcal R_q(P)\) be the removals whose new lower depth-\(q\) target has
reached capacity, and let \(\mathcal C_q(P)\) be the analogous insertion
set for upper targets.  Put

\[
 \mathcal R(P)=\bigcup_{q\le H}\mathcal R_q(P),\qquad
 \mathcal C(P)=\bigcup_{q\le H}\mathcal C_q(P).      \tag{0.2}
\]

Then the exact number of capacity-admissible return-free next exchanges,
before excluding already used vertices, is

\[
 \boxed{
 \bigl(|A(P)\setminus\mathcal R(P)|\bigr)
 \bigl(|B(P)\setminus\mathcal C(P)|\bigr),}          \tag{0.3}
\]

where \(A(P)\subseteq X\) and \(B(P)\subseteq[2m]\setminus X\) exclude
the at most \(H-1\) recent inserted and removed coordinates.  In
particular,

\[
                         |A(P)|,|B(P)|\ge m-H+1.     \tag{0.4}
\]

Thus a sequential theorem is reduced to maintaining

\[
 |\mathcal R(P)|,|\mathcal C(P)|\le(1-\varepsilon)m \tag{0.5}
\]

at every live endpoint and throughout every absorber switch.  Ordinary
global quota slack, separate-depth pseudorandomness, and the bound
\(\Delta_{\rm local}=m\) do not imply (0.5).

At depth one, the lower colors are the cliques

\[
 K_R=\{X\in\tbinom{[2m]}m:R\subset X\},
 \qquad |R|=m-1,                                    \tag{0.6}
\]

and similarly the upper colors are the \((m+1)\)-set cliques.  With the
minimum balanced cap

\[
 c_q=\left\lceil{W\over N_q}\right\rceil,\qquad
 W=\binom{2m}m,\quad N_q=\binom{2m}{m-q},            \tag{0.7}
\]

one has \(c_1=2\) and utilization

\[
 {W\over2N_1}={m+1\over2m}={1\over2}+{1\over2m}.    \tag{0.8}
\]

This is the exact quota-\(1/2\) interpretation of the depth-one clique
colors.  Exact target balance additionally requires every signed
depth-one color to occur once or twice; exactly \(W-N_1=N_1/m\) of them
occur twice.

More generally,

\[
 \rho_q:={W\over N_q}
 =\prod_{j=1}^q{m+j\over m-q+j}.                    \tag{0.9}
\]

Thus, uniformly for \(q=O(\sqrt m)\),

\[
 \log\rho_q={q^2\over m}+O\!\left({q^3\over m^2}\right).       \tag{0.10}
\]

If \(c_q=\lceil\rho_q\rceil\), then after all \(W\) windows have
been assigned, every cap-respecting assignment has at least

\[
 \bigl(\rho_q-c_q+1\bigr)N_q                       \tag{0.11}
\]

saturated depth-\(q\) colors.  For \(q=1\) this fraction is only
\(1/m\); for Gaussian depths it is the fractional residue of
\(e^{q^2/m+o(1)}\), and need not be small.  Formula (0.11) is a
marginal necessity only: it gives no license to multiply survival
fractions across depths.

The note below proves the local row/column theorem, the exact color-class
counts, and a deterministic higher-window covering obstruction.  It does
not prove the Hamilton absorption theorem.  The smallest remaining
positive statement is a robust-slack absorber theorem satisfying (0.5);
that condition is strictly stronger than the standard bounded-color-degree
hypotheses.

## 1. Window colors and the Hamilton problem

Let

\[
                         \mathcal J=J(2m,m).         \tag{1.1}
\]

An oriented Johnson edge is written

\[
 X\longrightarrow X-a+b,\qquad a\in X,\quad b\notin X.         \tag{1.2}
\]

Let

\[
                         C=(X_0,X_1,\ldots,X_{W-1}) \tag{1.3}
\]

be an oriented Hamilton cycle, with cyclic indices.  Its signed
depth-\(q\) window colors are

\[
\begin{aligned}
 L_{i,q}&=\bigcap_{j=0}^qX_{i+j},\\
 U_{i,q}&=\bigcup_{j=0}^qX_{i+j}.                  \tag{1.4}
\end{aligned}
\]

A window is **return-free** when

\[
                         |L_{i,q}|=m-q,\qquad
                         |U_{i,q}|=m+q.              \tag{1.5}
\]

Equivalently, its \(q\) removed coordinates are distinct, its \(q\)
inserted coordinates are distinct, and the removed and inserted
coordinate sets are disjoint.  In particular, neither a later removal
of an inserted coordinate nor a later reinsertion of a removed coordinate
is allowed inside the window.

For a target \(T\), define the cyclic loads

\[
\begin{aligned}
 \ell_q^-(T)&=\#\{i:L_{i,q}=T\},\\
 \ell_q^+(T)&=\#\{i:U_{i,q}=T\}.                    \tag{1.6}
\end{aligned}
\]

### Capacitated multidepth-rainbow Hamilton problem

Find a Hamilton cycle for which every \(q\le H\) window is return-free and

\[
 f_q\le\ell_q^\pm(T)\le c_q,
 \qquad
 f_q=\left\lfloor{W\over N_q}\right\rfloor,\qquad
 c_q=\left\lceil{W\over N_q}\right\rceil,           \tag{1.7}
\]

for all signed targets.  When \(f_q<c_q\), the total-load identity forces
exactly \(W-f_qN_q\) targets to have load \(c_q\) and all others to have
load \(f_q\); if \(f_q=c_q\), every load equals that common value.  Extra
radius quotas may be imposed by marking only the prescribed number of
starts at each depth; the local conflict calculation below is unchanged.

Strict rainbowness is arithmetically impossible on a cycle because
\(W>N_q\).  The caps (0.7), rather than color uniqueness, are the
canonical minimum-spread replacement.

## 2. Exact depth-one clique colors

For \(R\in\binom{[2m]}{m-1}\), the vertices containing \(R\) are

\[
                         K_R=\{R+x:x\notin R\}.      \tag{2.1}
\]

They form a clique of order \(m+1\) in \(\mathcal J\).  An edge has lower
color \(R\) exactly when it lies in this clique.  At a fixed endpoint
\(X\), fixing the lower color \(X-a\) leaves the \(m\) choices

\[
                         X-a+b,\qquad b\notin X.     \tag{2.2}
\]

Thus the exact local lower color degree is \(m\).  Dually, fixing upper
color \(X+b\) leaves the \(m\) choices of \(a\in X\).

Since

\[
 {W\over N_1}={m+1\over m}\in(1,2),                 \tag{2.3}
\]

the balanced cap is two and (0.8) follows.

For completeness, the exact ratio at every depth is

\[
 {W\over N_q}
 ={(m+q)!(m-q)!\over(m!)^2}
 =\prod_{j=1}^q{m+j\over m-q+j}.                   \tag{2.4}
\]

Taylor expansion of the logarithm gives (0.10).  Indeed, the sum of
the linear terms is

\[
 {1\over m}\sum_{j=1}^q\bigl(j+(q-j)\bigr)={q^2\over m},
\]

and the sum of the quadratic remainders is \(O(q^3/m^2)\) when
\(q=O(\sqrt m)\).

There is also an exact forced-saturation count.  If \(s_q\) colors have
load \(c_q\), while all other colors have load at most \(c_q-1\), then

\[
 W\le(c_q-1)(N_q-s_q)+c_qs_q=(c_q-1)N_q+s_q.
\]

Consequently

\[
 s_q\ge W-(c_q-1)N_q
      =(\rho_q-c_q+1)N_q,                           \tag{2.5}
\]

which proves (0.11).  Equality holds for a perfectly balanced load
vector with entries in \(\{c_q-1,c_q\}\).

## 3. Exact global color-class sizes

Fix a lower target

\[
                         L\in\binom{[2m]}{m-q}.      \tag{3.1}
\]

A return-free oriented \(q\)-window with lower color \(L\) is obtained by

1. choosing its \(q\) initially present coordinates
   \(A\subseteq[2m]\setminus L\);
2. choosing \(q\) inserted coordinates
   \(B\subseteq[2m]\setminus(L\cup A)\);
3. ordering the removals in \(q!\) ways; and
4. ordering the insertions in \(q!\) ways.

Therefore

\[
\boxed{
 |\mathcal W_q^-(L)|
 =\binom{m+q}q\binom mq(q!)^2
 =(m+q)_{\underline q}m_{\underline q}
 =(m+q)_{\underline{2q}}.}                          \tag{3.2}
\]

The upper color class has the same size by complementation.

If both the lower color \(L\) and upper color
\(U\supset L\), \(|U\setminus L|=2q\), are fixed, choose which \(q\)
members of \(U\setminus L\) are initially present and order the removals
and insertions.  Hence the exact joint-flag multiplicity is

\[
\boxed{
 |\mathcal W_q(L,U)|
 =\binom{2q}q(q!)^2=(2q)!.}                         \tag{3.3}
\]

Thus the enormous marginal color class (3.2) is a disjoint union of
\(\binom{m+q}{2q}\) joint flags of size \((2q)!\).  This decomposition is
the principal correlation available to an absorption proof.

## 4. The local exchange matrix

Let

\[
                         P=(X_{t-H+1},\ldots,X_t)    \tag{4.1}
\]

be the last \(H\) vertices of a path whose existing windows through depth
\(H\) are return-free, shortened at the beginning of the construction
when necessary, and put \(X=X_t\).

Let \(I^+\) be the set of coordinates inserted during the preceding
\(H-1\) transitions and \(I^-\) the set removed there.  Define

\[
                         A(P)=X\setminus I^+,\qquad
                         B(P)=([2m]\setminus X)\setminus I^-.   \tag{4.2}
\]

Every pair

\[
                         (a,b)\in A(P)\times B(P)    \tag{4.3}
\]

gives a neighbor \(X-a+b\) which keeps every new window of depth at most
\(H\) return-free.  Conversely, every such return-free extension belongs
to (4.3).  Indeed, return-freeness of the old suffix makes \(I^+\) and
\(I^-\) disjoint sets of the same size, with \(I^+\subseteq X\) and
\(I^-\subseteq[2m]\setminus X\).  Removing an element of \(I^+\) would
return a recently inserted coordinate, and inserting an element of
\(I^-\) would return a recently removed coordinate.  Every other
exchange introduces one new removal and one new insertion, disjoint from
all preceding ones.  For a full suffix, therefore,

\[
                         |A(P)|=|B(P)|=m-H+1,       \tag{4.3a}
\]

and the shortened case proves (0.4).

For \(1\le q\le H\), put

\[
 I_{q-1}=\bigcap_{j=0}^{q-1}X_{t-j},\qquad
 U_{q-1}=\bigcup_{j=0}^{q-1}X_{t-j}.                \tag{4.4}
\]

The new signed colors created by (4.3) are

\[
\boxed{\begin{aligned}
 L_q(a)&=I_{q-1}\setminus\{a\},\\
 U_q(b)&=U_{q-1}\cup\{b\}.
\end{aligned}}                                      \tag{4.5}
\]

The first is independent of \(b\), and the second independent of \(a\).
For each fixed \(q\), the maps

\[
                         a\mapsto L_q(a),\qquad
                         b\mapsto U_q(b)             \tag{4.6}
\]

are injective on \(A(P)\) and \(B(P)\).

### Theorem 4.1 (exact multidepth extension law)

Assume the current path prefix obeys all upper capacities.

Let

\[
\begin{aligned}
 \mathcal R_q(P)&=
 \{a\in A(P):\ell_q^-(L_q(a))=c_q\},\\
 \mathcal C_q(P)&=
 \{b\in B(P):\ell_q^+(U_q(b))=c_q\}.
                                                               \tag{4.7}
\end{aligned}
\]

An exchange \((a,b)\) is color-admissible through every depth \(q\le H\)
if and only if

\[
                         a\notin\mathcal R(P),\qquad
                         b\notin\mathcal C(P).        \tag{4.8}
\]

Consequently the number of color-admissible return-free exchanges is
exactly (0.3), before deleting exchanges whose new vertex was already
used.  Such an exchange is a valid path extension precisely when its new
vertex is also unused.

#### Proof

Equation (4.5) lists every newly created signed color.  A lower capacity
is exceeded precisely when \(a\in\mathcal R_q(P)\) for some \(q\); no
lower constraint depends on \(b\).  The upper statement is the column
analogue.  Taking the unions over \(q\) proves (4.8) and the product
count. \(\square\)

This theorem explains why the factor \(H\) does not automatically turn
the local color degree \(m\) into an \(Hm\)-vertex loss.  The forbidden
neighbors are complete rows and columns, and overlaps across depths are
the entire issue.

## 5. A deterministic higher-window covering barrier

The separate-depth data do not control the unions in (0.2).

### Proposition 5.1 (sparse layers can cover every exchange)

For every endpoint suffix \(P\) and \(1\le H\le|A(P)|\), there are sets

\[
                         R_q\subseteq A(P),\qquad1\le q\le H,   \tag{5.1}
\]

such that

\[
 |R_q|\le\left\lceil{|A(P)|\over H}\right\rceil,
 \qquad
                         \bigcup_{q=1}^HR_q=A(P).    \tag{5.2}
\]

The same holds for the insertion set \(B(P)\).

Since the maps in (4.6) are injective, the abstract local conflict system
allows one to declare the colors indexed by \(R_q\) saturated, and
similarly for the columns.  Such a saturation pattern has no legal
extension by Theorem 4.1, although each separate depth forbids only a
\((1/H+o(1))\)-fraction of the rows and columns.

#### Proof

Partition \(A(P)\) into \(H\) parts whose sizes differ by at most one and
take those parts as the \(R_q\)'s.  Injectivity in (4.6) identifies each
part with a set of distinct depth-\(q\) target colors.  Repeat for
\(B(P)\). \(\square\)

Proposition 5.1 is a conflict-system obstruction, not a claim that every
such abstract saturation vector occurs in a well-designed partial
Hamilton cycle.  It proves that no theorem based only on

* graph degree \(m^2\);
* maximum local color degree \(m\);
* separate-depth saturation densities; and
* \(H=o(m)\)

can guarantee a sequential extension.  A construction must impose
cross-depth correlation such as (0.5).

## 6. Conflict hypergraph formulation

Take the oriented Johnson edges as transitions, and seek a spanning
connected directed \(1\)-factor--equivalently, an oriented Hamilton
cycle--inside this transition graph.  For every return-free directed
\(q\)-path \(Q\), attach the two marginal colors

\[
                         \gamma_q^-(Q),\qquad
                         \gamma_q^+(Q).              \tag{6.1}
\]

For a signed color \(T\), declare every \(c_q+1\) distinct \(q\)-paths of
color \(T\) to be a capacity conflict.  On a candidate spanning cycle,
also declare:

1. every window with a coordinate return to be a geodesic conflict; and
2. every violation of a prescribed radius-start quota to be a quota
   conflict.

An upper-feasible cycle is precisely a spanning connected directed
\(1\)-factor avoiding this path-conflict hypergraph.  A balanced target
cover must in addition meet the lower bounds \(f_q\) in (1.7); these are
terminal covering requirements, not forbidden-subconfiguration
constraints.  Connectivity is also indispensable: conflict avoidance
alone may leave a disjoint cycle cover.

The marginal conflict degrees are large: a single lower color contains
\((m+q)_{\underline{2q}}\) oriented \(q\)-paths by (3.2).  A black-box
bounded-color-degree rainbow Hamilton theorem therefore sees a
high-rank, high-degree conflict system.  The useful structure discarded by
that black box is:

* the exact joint-flag decomposition (3.3); and
* the row/column extension law (4.5).

Any absorption theorem for this problem must preserve those two
structures.

## 7. Conditional sequential extension and the absorption gate

Theorem 4.1 immediately gives the following exact conditional statement.

### Theorem 7.1 (robust-slack sequential extension)

Suppose a return-free capacitated path prefix \(P\) satisfies

\[
\begin{aligned}
 |A(P)\setminus\mathcal R(P)|&\ge\sigma m,\\
 |B(P)\setminus\mathcal C(P)|&\ge\sigma m             \tag{7.1}
\end{aligned}
\]

for some \(\sigma>0\).  Then it has at least

\[
                         \sigma^2m^2                 \tag{7.2}
\]

color-admissible return-free next exchanges, before already used vertices
are removed.

If fewer than \(\sigma^2m^2\) of those exchanges lead to used vertices,
the path extends.

#### Proof

Equation (7.2) is (0.3).  Distinct exchanges \((a,b)\) give distinct
neighbors \(X-a+b\), so deleting the used ones proves the second claim.
\(\square\)

This is enough during the sparse initial stage, but not near Hamilton
completion: an arbitrary used vertex set can contain all \(m^2\)
neighbors of the endpoint.

The missing absorption theorem must therefore provide:

1. a sparse reservoir of switchable Johnson configurations;
2. the row/column slack (7.1) at every exposed endpoint of every switch;
3. a connector theorem in the unused graph respecting the same slack; and
4. closure of the final seam windows through every \(q\le H\), while
   filling every residual lower-quota deficit in (1.7).

The degree \(m^2\), local color degree \(m\), and hypothesis \(H=o(m)\)
solve none of items 2--4 by themselves.  Proposition 5.1 is the exact
higher-window reason.

## 8. Smallest viable positive theorem

A useful next theorem is now sharply stated.

> **Correlated-row absorption theorem.**  For \(H=o(m)\), construct a
> spanning absorptive path system in \(J(2m,m)\) and balanced capacities
> \(c_q\) such that every live endpoint, every connector endpoint, and
> every absorber shore satisfies
> \[
>  \left|\bigcup_{q\le H}\mathcal R_q\right|,
>  \left|\bigcup_{q\le H}\mathcal C_q\right|
>  \le(1-\varepsilon)m
> \]
> for one fixed \(\varepsilon>0\), while the final cyclic loads cover all
> signed targets up to the prescribed \(o(W)\) quota error.

Equivalently, the saturated marginal colors at different depths must be
coupled so that they repeatedly charge the same exchange coordinates.
Independent saturation would leave about
\(m\prod_q(1-\theta_q)\) good rows and is therefore the wrong model once
\(H\) grows; no independence assertion is used in the theorem above.

The unrestricted Hamilton lane is not closed, but its gate is no longer a
generic rainbow-Hamilton statement.  It is the specific cross-depth
row/column correlation invariant (0.5).
