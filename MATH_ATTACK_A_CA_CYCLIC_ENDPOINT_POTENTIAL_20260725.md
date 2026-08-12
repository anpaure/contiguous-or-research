# Cyclic endpoint potentials and the obstruction to extraction-based CA completion

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation was used.

## 0. Verdict

The audited pointed cyclic-flag extraction theorem does not prove the
common-cover theorem.  This note isolates the exact missing compatibility
at one rank.

For every owner and depth, grant not only its canonical cyclic child but
also the other cyclic child of the same canonical parent.  These pairs form
a multigraph which is a union of literal wreath cycles.  There is an exact
integral potential formula for the minimum number of owners which must use a
target outside their two cyclic children in order to realize prescribed
balanced loads.  Every actual common nested resolution pays at least this
rankwise cost.

The height-one part is the exact cut quantity

\[
\max_{\mathcal U}
\left{
e_q(\mathcal U)-b_q(\mathcal U),
\ b_q(\mathcal U)-e_q(\mathcal U)-|\delta_q(\mathcal U)|,
\ 0
\right}.
\tag{0.1}
\]

Higher integral potential levels record the legal Boolean-root correction
which a one-cut argument misses.  This is the cyclic analogue of the
depth-one root potential in the directed crossing-packet report.

Pointed extraction supplies many globally distinct **cyclic** flag targets,
but it neither bounds (0.1), controls the higher potential, nor ensures that
the selected starts hit the internal/external owner packets exposed below.
Thus the direct combination is closed.  A new crossing-compatible colored
extraction theorem would be needed.  No exact factor with asymptotically
large potential is constructed, so \((\mathrm{CA}_A)\) remains open.

## 1. The literal cyclic sibling multigraph

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
H=\lceil A\sqrt m\rceil,
\]

and fix one oriented exact wreath factor \(F\).  If the pointed occurrence
of its middle owner \(X\) is \((\pi,j)\), write

\[
\Gamma_q(X)=I_\pi(j,m-q)
\]

for the canonical same-start child.  For \(1\le q\le H\), put

\[
\Lambda_q(X)=I_\pi(j+1,m-q).
\tag{1.1}
\]

Both sets in

\[
K_q(X):=\{\Gamma_q(X),\Lambda_q(X)\}
\tag{1.2}
\]

are facets of the canonical parent
\(\Gamma_{q-1}(X)=I_\pi(j,m-q+1)\).

Let \(G_q(F)\) be the multigraph on

\[
V_q=\binom{[n]}{m-q}
\]

with one edge \(K_q(X)\) for every middle owner \(X\).  Parallel edges from
different wreaths are retained.  There are no loops.

### Lemma 1.1 — exact cycle and degree laws

Every wreath row contributes one \(n\)-cycle to \(G_q(F)\), and

\[
\boxed{\deg_{G_q}(S)=2\mu_q^F(S)}
\tag{1.3}
\]

for every \(S\in V_q\).

#### Proof

On one row put \(S_j=I_\pi(j,m-q)\).  The owner beginning at \(j\)
contributes the edge \(S_jS_{j+1}\).  The \(n\) proper cyclic intervals
\(S_j\) are distinct, so these edges form an \(n\)-cycle.  A target \(S\)
which occurs in this row is incident with the two adjacent row edges.  It
occurs at most once per row.  Summing over its \(\mu_q^F(S)\) row
occurrences proves (1.3). \(\square\)

Orienting every edge toward \(\Gamma_q(X)\) gives indegree vector
\(\mu_q^F\).  Thus the construction retains the actual canonical owner
labels, not merely the degree sequence.

## 2. Exact complete-off cut theorem

Fix an integral target load vector \(b:V_q\to\mathbb Z_{\ge0}\) with

\[
\sum_{S\in V_q}b(S)=W.
\tag{2.1}
\]

For \(\mathcal U\subseteq V_q\), let \(e_q(\mathcal U)\) be the number of
edges of \(G_q\) internal to \(\mathcal U\), and let
\(|\delta_q(\mathcal U)|\) be its edge-boundary size.  Define

\[
\chi_q(F,b)
=\max_{\mathcal U\subseteq V_q}
\bigl(b(\mathcal U)-e_q(\mathcal U)
                 -|\delta_q(\mathcal U)|\bigr)_+.
\tag{2.2}
\]

Taking complements and using

\[
W=e_q(\mathcal U)+e_q(V_q\setminus\mathcal U)
  +|\delta_q(\mathcal U)|
\]

gives the equivalent exact forms

\[
\boxed{
\chi_q(F,b)
=\max_{\mathcal U}(e_q(\mathcal U)-b(\mathcal U))_+
=\max_{\mathcal U}
\left\{
e_q(\mathcal U)-b(\mathcal U),
b(\mathcal U)-e_q(\mathcal U)-|\delta_q(\mathcal U)|,
0
\right\}.}
\tag{2.3}
\]

### Theorem 2.1 — exact two-endpoint relaxation

Among all maps \(\psi:V_0\to V_q\) with fibre vector \(b\), if a target
outside \(K_q(X)\) is allowed without any containment restriction, the
minimum number of off-endpoint assignments is exactly

\[
\boxed{\chi_q(F,b).}
\tag{2.4}
\]

#### Proof

Make \(b(S)\) labelled clones of every target \(S\).  Join owner \(X\) to
the clones of the two vertices in \(K_q(X)\).  Let \(M\) be a maximum
matching in this zero-cost bipartite graph.

For a set of target clones with support \(\mathcal U\), its neighbour set
is the set of graph edges incident with \(\mathcal U\), of size

\[
e_q(\mathcal U)+|\delta_q(\mathcal U)|.
\]

For fixed support the worst clone set contains all \(b(\mathcal U)\)
clones.  The deficiency form of Hall's theorem therefore gives

\[
W-|M|
=\max_{\mathcal U}
\bigl(b(\mathcal U)-e_q(\mathcal U)
                   -|\delta_q(\mathcal U)|\bigr)_+
=\chi_q(F,b).
\tag{2.5}
\]

Match the remaining \(W-|M|\) owners bijectively to the remaining target
clones using the permitted complete off-endpoint relation.  This constructs
a map of cost at most \(W-|M|\).  Conversely, the zero-cost assignments in
any map form a matching, so every map has cost at least \(W-|M|\).
Equations (2.4)--(2.5) follow. \(\square\)

For a balanced quota vector

\[
b(S)=c_q+\mathbf1_{H_q}(S),
\]

the cut baseline remains exactly

\[
b(\mathcal U)=c_q|\mathcal U|+|H_q\cap\mathcal U|.
\tag{2.6}
\]

No proportional replacement or independent optimization is hidden in
(2.2).

## 3. Exact legal-root potential

The complete-off relaxation ignores the Boolean root of an owner.  Restore
literal rankwise legality by permitting owner \(X\) to choose only

\[
\mathcal L_q(X)=\{S\in V_q:S\subseteq X\}.
\tag{3.1}
\]

Assume \(b\) is rankwise feasible for these roots; this holds in particular
when \(b\) is the depth-\(q\) load vector of a common balanced nested
resolution.  Define

\[
R_q^{\rm cyc}(F,b)
=\min_{\substack{\psi(X)\in\mathcal L_q(X)\\|\psi^{-1}(S)|=b(S)}}
\#\{X:\psi(X)\notin K_q(X)\}.
\tag{3.2}
\]

For an integral potential \(z:V_q\to\mathbb Z_{\ge0}\), put

\[
M_X^0(z)=\max_{S\in K_q(X)}z(S),
\]

\[
M_X^1(z)=
\max_{S\in\mathcal L_q(X)\setminus K_q(X)}z(S),
\]

and

\[
P_X(z)=\bigl(M_X^1(z)-M_X^0(z)-1\bigr)_+.
\tag{3.3}
\]

The irrelevant empty maximum may be omitted in the asymptotic range; if it
occurs, set \(P_X=0\).

### Theorem 3.1 — exact integral cyclic potential

\[
\boxed{
R_q^{\rm cyc}(F,b)
=\max_{\substack{z:V_q\to\mathbb Z_{\ge0}\\\min z=0}}
\left{
\sum_{S\in V_q}b(S)z(S)
-\sum_{X\in V_0}M_X^0(z)
-\sum_{X\in V_0}P_X(z)
\right}.}
\tag{3.4}
\]

In particular,

\[
\boxed{R_q^{\rm cyc}(F,b)\ge\chi_q(F,b).}
\tag{3.5}
\]

#### Proof

Use the transportation problem with variables \(x_{X,S}\) on
\(S\in\mathcal L_q(X)\), owner supply one, target demand \(b(S)\), and
cost zero on \(K_q(X)\), one otherwise.  After changing the signs of one
class of equality constraints, its matrix is a bipartite incidence matrix;
it is totally unimodular and the integral optimum equals the linear optimum.
The integral dual is

\[
\max\left{
\sum_X\alpha_X+\sum_Sb(S)z(S):
\alpha_X+z(S)\le
\mathbf1_{\{S\notin K_q(X)\}}
\right}.
\tag{3.6}
\]

Adding a constant to every \(z(S)\) and subtracting it from every
\(\alpha_X\) preserves the objective because both sides have total mass
\(W\).  Normalize \(\min z=0\).  For fixed \(z\), the largest permitted
owner potential is

\[
\alpha_X
=\min\{-M_X^0(z),1-M_X^1(z)\}
=-M_X^0(z)-P_X(z).
\]

Substitution proves (3.4).

If \(z=\mathbf1_{\mathcal U}\), then \(P_X(z)=0\), while
\(M_X^0(z)=1\) exactly for graph edges incident with \(\mathcal U\).
The dual value is

\[
b(\mathcal U)-e_q(\mathcal U)-|\delta_q(\mathcal U)|.
\]

Maximizing over \(\mathcal U\) and using (2.3) proves (3.5). \(\square\)

### Nested-level form

Let

\[
V_q=\mathcal U_0\supseteq\mathcal U_1\supseteq\cdots
\supseteq\mathcal U_h\ne\varnothing
\tag{3.7}
\]

be a finite nested sequence, with repetitions allowed.  Define

\[
h_q(\mathcal U_t,\mathcal U_{t-1})
=\#\left\{X:
K_q(X)\cap\mathcal U_{t-1}=\varnothing,
\ (\mathcal L_q(X)\setminus K_q(X))
       \cap\mathcal U_t\ne\varnothing
\right\}.
\tag{3.8}
\]

Layer-cake summation in (3.4) gives the equivalent formula

\[
\boxed{
R_q^{\rm cyc}(F,b)
=\max_{(3.7)}
\sum_{t=1}^h
\left[
b(\mathcal U_t)
-e_q(\mathcal U_t)-|\delta_q(\mathcal U_t)|
-h_q(\mathcal U_t,\mathcal U_{t-1})
\right].}
\tag{3.9}
\]

The empty nested sequence is allowed and contributes zero; it represents
the zero potential.

Indeed, \(M_X^0(z)\) counts the levels met by a cyclic endpoint, and
\(P_X(z)\) counts exactly the levels at which an off-cyclic legal target is
present in \(\mathcal U_t\) while both cyclic endpoints lie outside
\(\mathcal U_{t-1}\).  Leading repetitions of \(V_q\) contribute zero and
may be removed, exactly as in the depth-one potential formula.

## 4. Literal internal and external repair packets

For \(\mathcal U\subseteq V_q\), let

\[
\mathcal I_q(\mathcal U)
=\{X:K_q(X)\subseteq\mathcal U\},
\qquad
\mathcal J_q(\mathcal U)
=\{X:K_q(X)\cap\mathcal U=\varnothing\}.
\tag{4.1}
\]

Thus \(|\mathcal I_q(\mathcal U)|=e_q(\mathcal U)\), while the remaining
owners are boundary or external edges.

### Proposition 4.1 — exact directional demands

For every map \(\psi\) with load vector \(b\),

\[
\boxed{
\#\{X\in\mathcal I_q(\mathcal U):\psi(X)\notin\mathcal U\}
\ge(e_q(\mathcal U)-b(\mathcal U))_+,}
\tag{4.2}
\]

\[
\boxed{
\#\{X\in\mathcal J_q(\mathcal U):\psi(X)\in\mathcal U\}
\ge(b(\mathcal U)-e_q(\mathcal U)
                   -|\delta_q(\mathcal U)|)_+.}
\tag{4.3}
\]

Every owner counted on the left of (4.2) or (4.3) uses a target outside its
two cyclic endpoints.

#### Proof

All but the owners counted in (4.2) among the \(e_q(\mathcal U)\) internal
edges contribute inside \(\mathcal U\).  Other owners contribute
nonnegatively, which proves (4.2).  Internal and boundary edges can
contribute at most \(e_q(\mathcal U)+|\delta_q(\mathcal U)|\) assignments
inside \(\mathcal U\).  Every further contribution comes from an external
edge, proving (4.3). \(\square\)

If \(P\) is an actual balanced nested resolution, put

\[
R_q(P)=\#\{X:P_q(X)\notin K_q(X)\}.
\tag{4.4}
\]

Then

\[
\boxed{
e_q(F,P)\ge R_q(P)
\ge R_q^{\rm cyc}(F,b_q)
\ge\chi_q(F,b_q).}
\tag{4.5}
\]

The first inequality holds because every off-cyclic target differs from
the canonical endpoint \(\Gamma_q(X)\).  The second holds because
\(P_q(X)\subseteq X\) is a feasible rankwise assignment in (3.2).

Owners in (4.2)--(4.3) are literal directed repair packets.  The full
directed crossing theorem further requires their choices to be nested with
the preceding rank; (3.2) deliberately forgets that coupling and is only a
lower bound.

## 5. Necessary condition for \((\mathrm{CA}_A)\)

Let \(b_q\) be the actual load vectors of a common balanced nested
resolution.  Summing (4.5) gives

\[
\boxed{
\sum_{q=1}^H\frac{e_q(F,P)}{c_q}
\ge
\sum_{q=1}^H\frac{R_q^{\rm cyc}(F,b_q)}{c_q}
\ge
\sum_{q=1}^H\frac{\chi_q(F,b_q)}{c_q}.}
\tag{5.1}
\]

Hence \((\mathrm{CA}_A)\) requires one exact factor and one **common**
balanced quota flow for which both lower sums in (5.1) are \(o(W)\).  The
prime-equivariant flag flow supplies a common feasible \(b\) on prime
dimensions, but supplies no estimate for either cyclic potential.

The fixed-order star collar is also insufficient: (2.2) and (3.9) range
over arbitrary target families \(\mathcal U\), including orders tending to
infinity and multilevel nested potentials.

## 6. What audited pointed extraction does and does not supply

The final audit of `MATH_ATTACK_H_POINTED_CYCLIC_FLAG_EXTRACTION_20260725.md`
proves the following useful variable-demand statement.  Under its audited
product-parent hypotheses, if the retained cap mass is at least
\(\varepsilon HW\), then every demand \(D_m=o(W)\) can be packed onto

\[
O_{A,\varepsilon}(D_m/H+1)=o(W/H)
\]

literal pointed starts, provided one may select **any** \(D_m\) distinct
targets from its large prescribed target reservoir.

This does not cover the packets in Section 4:

1. the extraction quotas \(\beta_q\) minimize spill independently at each
   depth and need not be the common vectors \(b_q\) in (5.1);
2. capping alone only designates occurrences; the subsequent extraction
   matching does select pointed roots, but does not force those roots into
   the prescribed internal/external packet directions or embed them in one
   common residual flow;
3. globally distinct signed targets need not correspond to owners in
   \(\mathcal I_q(\mathcal U)\) or \(\mathcal J_q(\mathcal U)\) with the
   required direction;
4. the product-box parent pruned in the extraction theorem is not the
   Boolean owner root in (3.1);
5. even granting both cyclic endpoints to every owner leaves the exact
   potential (3.4).  A selected pointed incidence exposes one oriented
   same-start endpoint; a neighboring start can expose the other endpoint,
   but the extraction matching does not enforce the owner or cut direction
   required in (4.2)--(4.3).

There is also a sharp direct-composition no-go.  If one identifies a sparse
list of \(D_m=o(W)\) required repair units one-for-one with signed prescribed
targets, then, because every signed fibre is capped by
\(\Delta_A=O_A(1)\), its entire capped incidence graph has at most

\[
\Delta_AD_m=o(W)
\]

edges.  It cannot satisfy the positive retained-mass premise
\(L=\Omega(HW)\).  Thus a valid combination needs a large redundant target
reservoir together with a **colored** or packet-aware matching theorem which
forces the extracted starts to represent every required repair class.  The
uncolored Hall matching in pointed extraction does not do this.

## 7. Precise boundary

The following are proved:

1. \(G_q(F)\) is an exact union of literal wreath cycles with degree vector
   \(2\mu_q^F\).
2. The complete-off cyclic endpoint cost equals the exact cut quantity
   \(\chi_q(F,b)\).
3. With the actual Boolean root restriction, the exact integral cost is the
   multilevel potential (3.4), whose height-one part is \(\chi_q\).
4. Every common nested resolution pays these costs rankwise, with every
   floor and high-quota term retained in \(b_q\).
5. Pointed extraction alone supplies no bound on these costs and cannot be
   applied directly to a sparse repair-token list.

What remains unproved is the original genuinely joint theorem:

> Choose one exact factor, one common balanced quota flow, and
> \(o(W/H)\) owners which simultaneously cover the survival packets and the
> directed crossing packets.  Any such completion necessarily realizes the
> cyclic internal/external demands (4.2)--(4.3).

A sufficient extraction-based route would be a crossing-compatible colored
extraction theorem whose selected starts are forced to realize all those
packet directions.  No such colored theorem is proved here.

No lower bound showing that the potential is large for every exact factor
is proved here.  Therefore this is a sharper obstruction to the proposed
combination, not a counterexample to \((\mathrm{CA}_A)\), MWB, or the
contiguous-OR conjecture.
