# Fine strips: integral port sparsification and the exact annulus matching gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q},\qquad
 1\le H<h<m,
\]

and let \(\mathscr C_{m,h}\) be the complete physical cyclic
\(C_{2h}\)-strip catalogue.  A strip has \(2h\) distinct targets in every
signed rank \(m\pm q\), \(0\le q\le H\).

The raw whole-band incidence edge of one strip has

\[
                         2h(2H+1)                  \tag{0.1}
\]

vertices.  This is the wrong object for an integral matching theorem: at a
deep rank the uniform fractional solution deliberately gives load
\(N_1/N_q>1\), so most of the incidences in (0.1) are surplus cover
incidences rather than distinct resources.

This note removes that surplus **integrally**, without splitting a strip.
For every signed depth \(q\ge1\), there is a selected incidence set

\[
 \mathcal P_q^\pm
 \subseteq
 \{(C,T):T\in\mathcal T_q^\pm(C)\}                \tag{0.2}
\]

such that

1. every physical rank-\((m\pm q)\) target occurs in exactly \(D_1\)
   selected incidences;
2. every strip has either

   \[
   \left\lfloor2h{N_q\over N_1}\right\rfloor
   \quad\hbox{or}\quad
   \left\lceil2h{N_q\over N_1}\right\rceil         \tag{0.3}
   \]

   selected incidences of that sign and depth; and
3. at depth one every incidence is selected.

The proof is an exact bipartite total-unimodularity argument.  Thus (0.2)
is an integral port system, not randomized fractional thinning.

Use these ports to form a certification hypergraph \(\mathcal H^\#\): its
vertices are all middle owners and all signed nonmiddle targets through
depth \(H\); the edge \(e_C^\#\) consists of the \(2h\) middle owners of
\(C\) together with only its selected port incidences.  Then

\[
 \deg_{\mathcal H^\#}(T)=D_1
 \quad(T\text{ nonmiddle}),                       \tag{0.4}
\]

\[
 \deg_{\mathcal H^\#}(X)=D_0={N_1\over W}D_1
 \quad(X\text{ middle}),                           \tag{0.5}
\]

and, uniformly for \(H=o(m)\),

\[
 \boxed{
 |e_C^\#|
 \le2h+4h\sum_{q=1}^H{N_q\over N_1}+2H
 =O(h\sqrt m+H).}                                  \tag{0.6}
\]

In the intended range \(H<h\), this is \(O(h\sqrt m)\), rather than
\(\Theta(hH)\).

The uniform whole-cycle vector

\[
                         x_C={1\over D_1}            \tag{0.7}
\]

is now a genuine fractional **matching** of \(\mathcal H^\#\): it
saturates every nonmiddle target and gives every middle owner load
\(N_1/W<1\).

Most importantly, the final output is completely integral.

### Integral annulus matching criterion

Assume in addition that the parameter sequences satisfy

\[
                            H/h=o(1).               \tag{0.7a}
\]

If, for some integral port systems (0.2), \(\mathcal H^\#\) has an
ordinary integral matching \(\mathcal M\) which leaves only \(o(W)\)
nonmiddle target vertices unmatched, then the selected whole strips give a
literal word of length

\[
                         W+o(W)                    \tag{0.8}
\]

covering every rank in \([m-H,m+H]\).  Appending the proved product-SCD
tail at any cutoff \(H/\sqrt m\to\infty\) gives coefficient one.  No
owner recycling, fractional strip, chronology repair, or post-rounding is
left: the matching itself chooses whole physical strips, and every missing
target is appended literally.

Thus, for sequences satisfying (0.7a), the fine-strip theorem would follow
from the following precise integral annulus statement:

\[
 \boxed{
 \exists\text{ integral ports for which }\mathcal H^\#
 \text{ has a matching with nonmiddle leave }o(W).} \tag{AM}_{m,H,h}
\]

This is a more structured sufficient gate than the raw SCI set-cover LP:
it converts every deeper prescribed collision plateau into integral ports
before attempting the whole-strip rounding.  It is not claimed equivalent
to SCI; the matching additionally enforces middle-owner disjointness and
disjointness of all certified target incidences.

The theorem \((\mathrm{AM}_{m,H,h})\) is **not proved here**.  The port
reduction identifies why the currently available sparse-hypergraph
black boxes do not immediately prove it.  The critical three-layer section
has edge width \(6h\) and relative codegree \(O(1/m)\), hence the favorable
product \(h/m=o(1)\).  The full port edge has width
\(\Theta(h\sqrt m)\); multiplying this by the same worst critical
codegree gives \(h/\sqrt m\), which diverges because every admissible strip
has \(h>H\gg\sqrt m\).  That multiplication is only a method barrier—the
large codegrees are confined to nested neighboring-rank flags—but it means
that a fixed-uniformity or maximum-codegree nibble cannot be cited as the
missing proof.  What remains is a laminar/flag-aware matching theorem for
\(\mathcal H^\#\), or an absorber exploiting those nested codegrees.

Accordingly, the requested integral bridge is not closed.  What is closed
is the exact integral sparsification, the literal-word ledger, and a
single structured annulus matching gate.

## 1. Strip incidence graphs

Let

\[
                         M=|\mathscr C_{m,h}|.
\]

For each sign \(\epsilon\in\{-,+\}\) and depth \(1\le q\le H\), form the
bipartite incidence graph

\[
 G_q^\epsilon
 =\bigl(\mathscr C_{m,h},\binom{[2m]}{m+\epsilon q};E_q^\epsilon\bigr),
                                                               \tag{1.1}
\]

where \((C,T)\in E_q^\epsilon\) precisely when \(T\) is one of the
\(2h\) signed depth-\(q\) targets of \(C\).  Coordinate transitivity and
the exact within-strip distinctness give

\[
 \deg_{G_q^\epsilon}(C)=2h,                        \tag{1.2}
\]

\[
 \deg_{G_q^\epsilon}(T)=D_q
 ={(m+q)!(m-q)!\over2(m-h)!^2}.                    \tag{1.3}
\]

Double counting gives

\[
                         2hM=N_qD_q,               \tag{1.4}
\]

and therefore

\[
 {D_q\over D_1}={N_1\over N_q},
 \qquad
 \theta_q:={D_1\over D_q}={N_q\over N_1}\le1.    \tag{1.5}
\]

The equality \(\theta_1=1\) will retain every first-shadow incidence.

## 2. Exact integral port sparsification

### Theorem 2.1 (rankwise integral ports)

For every \((q,\epsilon)\), there is a spanning subgraph

\[
                         P_q^\epsilon\subseteq G_q^\epsilon             \tag{2.1}
\]

such that

\[
 \deg_{P_q^\epsilon}(T)=D_1
 \quad\text{for every target }T,                  \tag{2.2}
\]

and

\[
 \deg_{P_q^\epsilon}(C)
 \in
 \left\{
 \lfloor2h\theta_q\rfloor,
 \lceil2h\theta_q\rceil
 \right\}
 \quad\text{for every strip }C.                   \tag{2.3}
\]

For \(q=1\), one necessarily has

\[
                         P_1^\epsilon=G_1^\epsilon.              \tag{2.4}
\]

#### Proof

Give every edge of \(G_q^\epsilon\) the fractional value \(\theta_q\).
At a target vertex its incident value is

\[
                         D_q\theta_q=D_1,           \tag{2.5}
\]

while at a strip vertex it is

\[
                         2h\theta_q.                \tag{2.6}
\]

Consider the polytope of edge vectors \(z\) defined by

\[
 \sum_{C\ni T}z_{C,T}=D_1                         \tag{2.7}
\]

at every target,

\[
 \lfloor2h\theta_q\rfloor
 \le\sum_{T\in C}z_{C,T}
 \le\lceil2h\theta_q\rceil                       \tag{2.8}
\]

at every strip, and \(0\le z_{C,T}\le1\).  Equations (2.5)--(2.6) show
that the constant vector \(z=\theta_q\) is feasible.

After multiplying all rows on one shore by \(-1\), the constraint matrix
in (2.7)--(2.8) is a submatrix of the directed node--edge incidence matrix
of a bipartite graph, together with identity rows for the bounds.  It is
totally unimodular.  Every right-hand side is integral.  Hence the
nonempty polytope has an integral vertex.  Its coordinates lie in
\(\{0,1\}\) and define (2.1), proving (2.2)--(2.3).

When \(q=1\), \(\theta_1=1\), so the only feasible edge vector is the
all-one vector.  This proves (2.4). \(\square\)

The choices for different ranks and signs are made separately, but the
result is not a separate-depth final solution.  They only mark which
incidences of a whole strip will serve as certificates.  The eventual
matching still chooses one common set of whole strips simultaneously for
every rank.

## 3. The certification hypergraph

Fix one port system from Theorem 2.1 for every sign and depth.  Define
\(\mathcal H^\#\) as follows.

Its vertex set is

\[
 V(\mathcal H^\#)
 =\binom{[2m]}m
 \ \dot\bigcup\!
 \bigcup_{q=1}^H
 \left(
  \binom{[2m]}{m-q}\dot\cup\binom{[2m]}{m+q}
 \right).                                         \tag{3.1}
\]

For every physical strip \(C\), put

\[
 e_C^\#
 =\{X_t(C):t\in\mathbb Z_{2h}\}
 \ \dot\bigcup\!
 \{T:(C,T)\in P_q^\epsilon
       \text{ for some }q,\epsilon\}.             \tag{3.2}
\]

The hypergraph has one edge per whole physical strip.  No edge has been
split and no strip occurs twice.

The hypergraph is generally nonuniform: the independent integral
roundings in (2.3) can give different strips different edge sizes.  All
uses of ``width'' below mean maximum edge size.  The conditional compiler
needs no uniformity; applying a uniform-hypergraph matching theorem would
require an additional reduction or a genuinely nonuniform theorem.

### Proposition 3.1 (degrees and fractional matching)

Every nonmiddle vertex has degree exactly \(D_1\), every middle vertex has
degree

\[
                         D_0={N_1\over W}D_1,       \tag{3.3}
\]

and the vector \(x_C=1/D_1\) is a fractional matching.  It saturates every
nonmiddle vertex and has total weight

\[
 \sum_Cx_C={M\over D_1}={N_1\over2h}.              \tag{3.4}
\]

#### Proof

The nonmiddle degree assertion is (2.2).  The middle degree and the last
identity follow from the standard double counts

\[
                         2hM=WD_0=N_1D_1.          \tag{3.5}
\]

Thus a nonmiddle vertex has fractional load one and a middle vertex has
load \(D_0/D_1=N_1/W<1\).  These are exactly the fractional matching
constraints. \(\square\)

This is the promised conversion of the uniform fractional **cover** into
a fractional matching.  The conversion is exact because every surplus
deep incidence was assigned, integrally, either to a target port or to the
uncertified surplus.

## 4. Width of a port edge

By (2.3),

\[
 \begin{aligned}
 |e_C^\#|
 &\le2h+2\sum_{q=1}^H
       \left(2h{N_q\over N_1}+1\right)\\
 &=2h+4h\sum_{q=1}^H{N_q\over N_1}+2H.             \tag{4.1}
 \end{aligned}
\]

For \(q=o(m)\), the exact binomial ratio gives

\[
 {N_q\over W}
 =\prod_{j=1}^q{m-j+1\over m+j}
 \le \exp\!\left(-{q^2\over m+q}\right).          \tag{4.2}
\]

Since \(N_1/W=m/(m+1)\), (4.2) and a Gaussian sum give, uniformly for
\(H=o(m)\),

\[
 \sum_{q=1}^H{N_q\over N_1}
 \le C\sqrt m                                      \tag{4.3}
\]

for an absolute constant \(C\).  Substitution in (4.1) proves (0.6).

Notice that (4.3) sums the *physical target mass*, not the number of
protected depths.  The port width therefore remains \(O(h\sqrt m)\) even
when \(H/\sqrt m\to\infty\).

## 5. Integral matching to literal word

### Theorem 5.1 (annulus matching compiler)

Assume

\[
                         H/h=o(1),                 \tag{5.1}
\]

and let \(\mathcal M\) be an ordinary matching in \(\mathcal H^\#\).
Let \(s=|\mathcal M|\), and let \(L^\#\) be the number of unmatched
nonmiddle vertices of \(\mathcal H^\#\).  If

\[
                         L^\#=o(W),                \tag{5.2}
\]

then the physical strips indexed by \(\mathcal M\), together with literal
singleton repair, give a word of length \(W+o(W)\) covering every target
in the central band \([m-H,m+H]\).

#### Proof

Because middle vertices belong to the hyperedges, the chosen physical
strips are middle-owner-disjoint.  Hence they use exactly \(2hs\) distinct
middle owners and

\[
                         s\le {W\over2h}.           \tag{5.3}
\]

At signed depth one every strip incidence is a port incidence by (2.4).
The matching therefore covers exactly \(2hs\) distinct targets on each
depth-one side.  Consequently

\[
 2(N_1-2hs)\le L^\#=o(W).                          \tag{5.4}
\]

In particular, the middle leave is not an extra hypothesis:

\[
 W-2hs=(W-N_1)+(N_1-2hs)
 \le {W\over m+1}+{L^\#\over2}=o(W).              \tag{5.4a}
\]

If a nonmiddle vertex is met by the matching, the selected whole strip
physically contains that target.  Some unmatched port vertices may also be
covered by uncertified surplus incidences, but never the reverse.  Thus the
number of actual nonmiddle holes is at most \(L^\#\).

Only certified port incidences are forced disjoint by the matching.
Uncertified physical occurrences of two selected strips may overlap; this
can only add coverage and is not used as a resource in the length ledger.

For each chosen strip append its exact literal block of length
\(2h+2H\).  Append every uncovered middle target and every actual
nonmiddle hole as one singleton letter.  The resulting length is at most

\[
 \begin{aligned}
 &(2h+2H)s+(W-2hs)+L^\#\\
 &\hspace{2cm}=W+2Hs+L^\#\\
 &\hspace{2cm}\le W+{H\over h}W+o(W)=W+o(W),       \tag{5.5}
 \end{aligned}
\]

using (5.1), (5.2), and (5.3).  Every strip witness lies inside its own
literal block, so concatenation introduces no seam condition.  Every
singleton repair is already counted in (5.5). \(\square\)

The lower bound (5.4) also gives

\[
 s={N_1\over2h}+o(W/h)                              \tag{5.6}
\]

up to the harmless interval ending at \(W/(2h)\).  Relative to the exact
fractional strip-cover value,

\[
 \left[W+{H\over h}W\right]
 -\left[W+{H\over h}N_1\right]
 ={H\over h}{W\over m+1}=o(W).                     \tag{5.7}
\]

Thus the compiler is coefficient-sharp even if the matching uses the
largest permitted middle-owner mass.

## 6. Exterior tail and parity

Choose any sequences with

\[
 {H\over\sqrt m}\longrightarrow\infty,
 \qquad {H\over h}\longrightarrow0,
 \qquad H=o(m).                                    \tag{6.1}
\]

The product-SCD exterior word beginning beyond depth \(H\) has length

\[
                         o(W).                     \tag{6.2}
\]

It begins immediately after the band covered in Theorem 5.1, with the
usual one-rank convention.  All central witnesses lie within strip or
singleton blocks and all exterior witnesses lie within product-SCD
gadgets, so the join has zero additional cost.  Therefore
\((\mathrm{AM}_{m,H,h})\) implies

\[
                         \nu(2m)=W+o(W).            \tag{6.3}
\]

The standard two-copy one-coordinate lift gives the odd case.  Every
factor two, singleton, and collar is already present in the preceding
finite ledger.

The previously proved PBBS central word through \(o(\sqrt m)\) does not
permit the port matching word to be appended at cost \(o(W)\): the first
uncovered annulus rank itself has \((1-o(1))W\) members.  The port matching
construction is instead a replacement of the central baseline, with its
\(W\) letters paid exactly once in (5.5).  This is the precise sense in
which it performs owner/baseline recycling.

## 7. Why a generic nibble still does not finish

The certification hypergraph has an excellent degree normalization: all
nonmiddle degrees are exactly \(D_1\), middle degrees are
\((1-o(1))D_1\), and (0.7) is a fractional matching saturating every
nonmiddle vertex.

On the middle and two signed depth-one layers alone, the exact pair
codegree audit gives

\[
                         {\Delta_2\over D_1}\le{2\over m+1}.    \tag{7.1}
\]

The critical edge width is \(6h\), so

\[
                         6h{\Delta_2\over D_1}=o(1)              \tag{7.2}
\]

whenever \(h=o(m)\).  This is the favorable near-factor regime.

For the full port hypergraph, (4.1) has width \(O(h\sqrt m)\).  A theorem
whose hypothesis is only

\[
 |e_C^\#|{\Delta_2\over D_1}=o(1)                  \tag{7.3}
\]

cannot be applied, because its left side is bounded at best by the scale

\[
                         {h\over\sqrt m},           \tag{7.4}
\]

and \(h>H\gg\sqrt m\).  Choosing a larger strip makes (7.4) worse.

This failure is not an obstruction to \((\mathrm{AM}_{m,H,h})\).  The
ratio (7.1) is attained by incident middle/first-shadow pairs; only
\(O(h)\) vertices of an edge belong to those critical layers.  The other
\(O(h\sqrt m)\) port vertices lie in nested flag rows, where codegrees
depend on rank separation.  Multiplying the largest codegree by the whole
edge width discards exactly that laminar structure.

Therefore the precise remaining theorem is not an ordinary
fixed-uniformity matching result.  It must prove a matching leave
\(o(W)\) using the rank-stratified or nested-flag codegree profile, or use
an absorber which resolves the integral residual across those flags.

## 8. Exact proved and open boundary

Proved here:

1. the integral port systems (2.1)--(2.4), by total unimodularity;
2. exact degree normalization (3.3)--(3.5);
3. the fractional matching (0.7) after all deeper surplus is removed;
4. the physical-width bound \(O(h\sqrt m)\), independent of a
   super-Gaussian number of protected rows;
5. the fully integral literal compiler, Theorem 5.1; and
6. the exact product-tail and parity interface.

Not proved:

1. a matching of \(\mathcal H^\#\) with nonmiddle leave \(o(W)\);
2. a laminar/flag-aware matching theorem strong enough to imply it; or
3. the owner-recycling strip conjecture and coefficient one.

For this port-matching route, the fractional point is used only to certify that the integral port
polytope and the matching relaxation are nonempty.  Every object required
by Theorem 5.1 is integral, and every literal letter is counted.  The sole
remaining question inside this route is \((\mathrm{AM}_{m,H,h})\); the
weaker SCI set-cover gate could still be solved without such a matching.
