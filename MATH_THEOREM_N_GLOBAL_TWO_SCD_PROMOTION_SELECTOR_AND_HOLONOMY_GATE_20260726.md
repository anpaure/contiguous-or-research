# Global two-SCD promotion coupling: selector components, outer-slot spines, and the bounded-holonomy ladder

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad
 H=\lfloor\sqrt{m\log m}\rfloor,
 \qquad
 N=N_{q_0}.
\tag{0.1}
\]

This note answers the global two-SCD question at the exact statewise
level. It does not construct the required pair of SCDs, but it gives both
an exact obstruction and a quantitatively sufficient positive theorem.

1. **Two SCDs on one common owner baseline are packet switches, not an
   averaging relaxation.** There is an augmented provider/owner overlay
   graph on the rank-\((m-q_0)\) roots. Exact selectors are precisely the
   componentwise constant bits of this graph. Every component is an exact
   annular trade packet: its two colours use the same owner set, the same
   signed target set at every controlled depth, and the same clipped
   radius histogram.

2. **The common baseline is frozen.** Component switching cannot repair
   its owner point margins. Every exact path cover obeys

   \[
    p\ge\frac1{2q_0^2}
       \sum_{x=1}^{2m}|2M_x(\Omega)-N|.
   \tag{0.2}
   \]

   Thus \(p=o(W/H)\) requires

   \[
    \sum_x|2M_x(\Omega)-N|
       =o\!\left(\frac W{\sqrt{\log m}}\right).
   \tag{0.3}
   \]

   In particular, exact component switching on a second SCD with the
   canonical-BTK active owner baseline cannot repair the previously proved
   \((4/\sqrt\pi+o(1))W\) point skew. Seam deletions change the baseline
   and are a separate escape.

3. **The top-anchor Hall problem is always soluble.** For every top
   \(U\in\binom{[2m]}{m+H}\), either SCD supplies one possible middle
   owner. One can choose one of the two owners for every top with no
   repetition. The obstruction starts only when the choices must be the
   same choices at every depth and must compose chronologically.

4. **Every exact radius increase is an outer-slot event.** If a legal
   promotion joins native tags \(r\to s\), then its cache slot \(\ell\)
   satisfies

   \[
    \ell>\min\{r,s\}.
   \tag{0.4}
   \]

   Hence a nondecreasing step \(r\to s\ge r\) uses \(\ell>r\), or is a
   genuine rotor. This conclusion is colour-blind and applies to two
   unrelated SCDs.

5. **The exact radius census forces critical crossing mass.** If all
   controlled provider rows are exact and \(p=o(W/H)\), then every path
   forest has at least

   \[
    \left(\sqrt{2/e}-o(1)\right)\frac W{\sqrt m}
   \tag{0.5}
   \]

   nondecreasing, return-enabling edges. A second SCD is useful only if it
   supplies this many state-composable outer-slot spines. Aggregate
   \(o(W)\) provider error alone is too weak to retain this conclusion:
   the whole peak layer has size only \(\Theta(W/\sqrt m)=o(W)\).

6. **There is an exact fixed-schedule obstruction.** Given a formal
   promotion schedule, let \(A_T\subseteq\{0,1\}\) be the SCD colours
   whose actual chain state agrees with the prescribed owner, tag, and
   full nested flag at root \(T\). Exact coupling exists if and only if

   \[
    \bigcap_{T\in K}A_T\ne\varnothing
   \tag{0.6}
   \]

   for every overlay component \(K\). With defects allowed, the exact
   abstract obstruction is a directed \(s\)-\(t\) cut.

7. **A bounded-holonomy pair would suffice.** Suppose the common-owner
   permutation has only \(O(N_H)\) selected colour runs, every all-depth
   provider pairing is a bounded power of this one permutation, and the
   selected colour runs plus their diagonal skips lift to legal
   \(H\)-safe radius-nondecreasing promotion paths. Then

   \[
    L\le W+O(HN_H)=W+o(W),
    \qquad
    p=O(N_H)=O(W/m)=o(W/H).
   \tag{0.7}
   \]

This is the precise boundary. Two unrelated SCDs do not automatically
provide useful correlation. They work only if their relative owner and
all-depth provider maps collapse to one promotion-scale holonomy and if
that algebraic ladder has the literal queue/cache lift. Conversely, no
universal no-go for every tailored pair is possible: a pure selector
would already work if one SCD contained the desired annular promotion
factor.

## 1. Two SCDs and the common-baseline overlay

Let

\[
 \mathcal R=\binom{[2m]}{m-q_0}.
\tag{1.1}
\]

For \(c\in\{0,1\}\), let \(C_c(T)\) be the chain of the SCD
\(\mathscr D_c\) through \(T\in\mathcal R\). Write

\[
 \mu_c(T)\in\binom{[2m]}m
\]

for its middle owner and \(r_c(T)\) for its native radius. Assume the two
active owner images coincide:

\[
 \mu_0(\mathcal R)=\mu_1(\mathcal R)=:\Omega,
 \qquad |\Omega|=N.
\tag{1.2}
\]

Both maps \(\mu_c:\mathcal R\to\Omega\) are bijections. Define the owner
permutation

\[
 \rho=\mu_1^{-1}\mu_0,
 \qquad
 \mu_1(\rho T)=\mu_0(T).
\tag{1.3}
\]

For \(q_0\le q\le H\) and sign \(\sigma\in\{-,+\}\), put

\[
 \mathcal R_c(q)=\{T\in\mathcal R:r_c(T)\ge q\}.
\]

The native signed target map

\[
 F_{c,q}^{\sigma}:\mathcal R_c(q)
 \longrightarrow\binom{[2m]}{m+\sigma q}
\tag{1.4}
\]

is a bijection. Thus the roots providing the same target in the two SCDs
are paired by

\[
 \phi_{q,\sigma}
 =(F_{1,q}^{\sigma})^{-1}F_{0,q}^{\sigma}:
 \mathcal R_0(q)\longrightarrow\mathcal R_1(q).
\tag{1.5}
\]

At the lower entrance, \(\phi_{q_0,-}\) is the identity.

Define the undirected multigraph \(G_{\rm sel}\) on \(\mathcal R\) by
adding

* the owner edge \(T\sim\rho T\) for every \(T\); and
* the provider edge \(T\sim\phi_{q,\sigma}T\) for every controlled
  \((q,\sigma)\) and every \(T\in\mathcal R_0(q)\).

Loops may be suppressed. Multiplicity is retained.

## 2. Exact selectors are componentwise annular trades

A selector \(z:\mathcal R\to\{0,1\}\) chooses \(C_{z(T)}(T)\).

### Theorem 2.1 (exact component characterization)

The selector gives

1. exactly one selected occurrence of every owner in \(\Omega\); and
2. exactly one designated native provider of every signed target at every
   depth \(q_0\le q\le H\),

if and only if \(z\) is constant on every component of
\(G_{\rm sel}\).

#### Proof

Fix \(X\in\Omega\). Write

\[
 T_0=\mu_0^{-1}(X),
 \qquad
 T_1=\mu_1^{-1}(X)=\rho T_0.
\]

The selected load of \(X\) is

\[
 (1-z(T_0))+z(T_1).
\tag{2.1}
\]

It equals one exactly when \(z(T_0)=z(T_1)\), which is equality on the
owner edge.

Likewise, for
\(S=F_{0,q}^{\sigma}(T)=F_{1,q}^{\sigma}(\phi_{q,\sigma}T)\),
the selected provider load is

\[
 (1-z(T))+z(\phi_{q,\sigma}T).
\tag{2.2}
\]

It equals one exactly when the two endpoint bits agree. Thus all loads
are one exactly when \(z\) is constant on every edge, equivalently on
every component. \(\square\)

Owner simplicity alone already implies exact owner load one under (1.2):
there are \(N\) selected occurrences and only \(N\) possible baseline
owners.

### Theorem 2.2 (every component is an exact annular trade packet)

For every component \(K\) of \(G_{\rm sel}\),

\[
 \boxed{
 \{\mu_0(T):T\in K\}
 =\{\mu_1(T):T\in K\}.}
\tag{2.3}
\]

For every controlled \((q,\sigma)\),

\[
 \boxed{
 \{F_{0,q}^{\sigma}(T):T\in K\cap\mathcal R_0(q)\}
 =
 \{F_{1,q}^{\sigma}(T):T\in K\cap\mathcal R_1(q)\}.}
\tag{2.4}
\]

In particular,

\[
 |K\cap\mathcal R_0(q)|=|K\cap\mathcal R_1(q)|
 \qquad(q_0\le q\le H),
\tag{2.5}
\]

so the two colours have the same clipped exact-radius histogram on \(K\).

#### Proof

Every owner edge joins the two roots representing one common owner. Since
both endpoints lie in the same component, an owner occurs on the left of
(2.3) if and only if it occurs on the right.

The provider edges at fixed \((q,\sigma)\) are a perfect matching between
the two active root sets and pair equal target masks. Restricting a
matching to one union-component preserves both endpoints of every edge,
proving (2.4). Taking cardinalities gives (2.5). Consecutive differences
in \(q\) give equality of the exact-radius histograms. \(\square\)

Thus switching a component can re-pair histories, but it cannot change
the owner set, any signed target set, or any radius capacity. If
\(G_{\rm sel}\) is connected, the only exact selectors are the two pure
SCDs.

The number of formal provider-pair incidences, with multiplicity and with
loops retained, is

\[
 2\sum_{q=q_0}^{H}N_q
 =\left(\sqrt\pi+o(1)\right)W\sqrt m.
\tag{2.6}
\]

Indeed \(N_q/W=e^{-q^2/m+o(1)}\) in the contributing Gaussian range,
\(q_0/\sqrt m\to0\), and \(H/\sqrt m\to\infty\). This does not imply that
the same mass is nonloop: identical SCDs make every incidence a loop. If
the nonloop incidence mass is \(\Theta(W\sqrt m)\), however, independent
rootwise choices cross that order of equality edges. Useful unrelated
pairs must then be correlated on orbit scale.

## 3. The frozen point-margin obstruction

Let

\[
 M_x(\Omega)=|\{X\in\Omega:x\in X\}|.
\]

Every exact selector has the same owner support \(\Omega\), so the exact
queue point-margin theorem gives

\[
 \boxed{
 p\ge\frac1{2q_0^2}
 \sum_{x=1}^{2m}|2M_x(\Omega)-N|.}
\tag{3.1}
\]

Since

\[
 q_0^2=(1+o(1))\sqrt m,
 \qquad
 \frac WH=(1+o(1))\frac W{\sqrt{m\log m}},
\]

the condition \(p=o(W/H)\) implies (0.3).

For the canonical BTK active baseline, the midpoint-excursion calculation
gives

\[
 \sum_x|2M_x(\Omega_{\rm BTK})-N|
 \ge\left(\frac4{\sqrt\pi}+o(1)\right)W.
\tag{3.2}
\]

Thus no exact, no-deletion selector using the same active owner set can
repair canonical BTK: component colour choices do not move the left side
of (3.1). Deleting \(\Theta(W/m)\) carefully chosen seam owners can change
this point vector by \(\Theta(W)\), so the bounded-holonomy construction
of Section 8 is not ruled out by this exact-baseline statement.

There is also a conditional quantitative meaning of “unrelated.” Let
\(\iota(G_{\rm sel})\) be the edge-isoperimetric constant of the
symmetrized multigraph. If

\[
 \iota(G_{\rm sel})\ge c\sqrt m
\tag{3.3}
\]

for a fixed \(c>0\), then every selector with symmetric equality defect
\(o(W)\) has minority colour class \(o(W/\sqrt m)\). A path forest has at
most twice the minority size in cross-colour edges. Hence such a pair
cannot use cross-colour edges as the sole source of the critical mass in
Section 6. This is an exact expansion obstruction for random-like or
unrelated overlays; no bound such as (3.3) holds for arbitrary deliberately
correlated SCD pairs.

## 4. The top-anchor Hall problem always passes

For \(U\in\binom{[2m]}{m+H}\), let \(x_c(U)\) be the middle owner of the
\(\mathscr D_c\)-chain containing \(U\). Each map \(U\mapsto x_c(U)\) is
injective: one SCD chain contains only one set at rank \(m+H\).

Form a multigraph on middle owners with one edge labelled \(U\), joining
\(x_0(U)\) to \(x_1(U)\); a loop is allowed.

### Theorem 4.1 (two-SCD top-anchor SDR)

One can select, for every top \(U\), one of \(x_0(U),x_1(U)\) so that all
selected owners are distinct.

#### Proof

At a middle owner there is at most one incident edge in colour zero and
at most one in colour one. Hence the multigraph has maximum degree two;
its components are paths, cycles, and isolated loops. On a path, assign
successive edges to successive vertices. On a cycle, orient cyclically and
assign each edge to its head. Assign an isolated loop to its vertex. Every
edge receives a distinct incident vertex. \(\square\)

Thus no Hall obstruction occurs at the \(H\)-anchor row alone. The choices
become difficult only after all provider equalities and the common history
are imposed.

## 5. Exact cross-SCD promotion spine

Fix full length-\(H\) refinements of the selected chain states. For a
state \(v\), write

\[
 \boldsymbol\alpha_v=(\alpha_1(v),\ldots,\alpha_H(v)),
 \qquad
 \boldsymbol\beta_v=(\beta_1(v),\ldots,\beta_H(v)).
\]

Let \(v\to w\) be an owner-changing bridge-one promotion, with

\[
 X_w=X_v-\alpha_1(v)+b,
 \qquad
 b=\beta_\ell(v).
\tag{5.1}
\]

The queue/cache normal form is

\[
 \boldsymbol\alpha_w
 =\bigl(\alpha_2(v),\ldots,\alpha_H(v),x\bigr),
 \qquad x\in L_H(v),
\tag{5.2}
\]

and

\[
 \boldsymbol\beta_w
 =\bigl(\alpha_1(v),
   \boldsymbol\beta_v\setminus\beta_\ell(v)\bigr),
\tag{5.3}
\]

with the unaffected cache entries retaining their order.

### Theorem 5.1 (flag spine formulas)

For \(q<H\),

\[
 \boxed{L_q(w)=L_{q+1}(v)\cup\{b\}.}
\tag{5.4}
\]

Moreover,

\[
 \boxed{
 U_q(w)=
 \begin{cases}
 U_q(v),&\ell\le q,\\[1mm]
 U_q(v)-\{\beta_q(v)\}+\{b\},&\ell>q.
 \end{cases}}
\tag{5.5}
\]

A genuine rotor satisfies the second line for every \(q<H\), with \(b\)
drawn from the upper residual. At the entrance depth, every late promotion
or rotor satisfies

\[
 A_w=A_v-\{\alpha_1(v)\}+\{\alpha_{q_0+1}(v)\},
\tag{5.6}
\]

\[
 B_w=B_v-\{\beta_{q_0}(v)\}+\{\alpha_1(v)\}.
\tag{5.7}
\]

#### Proof

Equation (5.4) follows by deleting the first \(q\) entries of (5.2) from
\(X_w=X_v-\alpha_1+b\). If \(\ell\le q\), the first \(q\) target-cache
entries at \(w\), together with the arrival already in \(X_w\), recover
exactly the first \(q\) cache entries at \(v\). This gives the first line
of (5.5). If \(\ell>q\), the first \(q\) entries at \(w\) are
\(\alpha_1(v),\beta_1(v),\ldots,\beta_{q-1}(v)\); adjoining them to
\(X_w\) replaces \(\beta_q(v)\) by \(b\), proving the second line.
Equations (5.6)--(5.7) are the corresponding first-\(q_0\) set identities.
\(\square\)

### Corollary 5.2 (outer-slot necessity)

If the selected upper depth-\(q\) targets are injective and both endpoint
flags are native through depth \(q<H\), then \(\ell>q\). At \(q=H\),
every promotion preserves \(U_H\), so two distinct injective native
tag-\(H\) endpoints cannot be joined by a promotion. Consequently an
exact owner-changing edge between native tags \(r,s\) is either a genuine
rotor, or is a promotion obeying

\[
 \boxed{\ell>\min\{r,s\}.}
\tag{5.8}
\]

In particular a radius increase \(r\to s>r\) requires \(\ell>r\), or a
genuine rotor.

#### Proof

If \(\ell\le q<H\), (5.5) gives \(U_q(v)=U_q(w)\), contradicting
injectivity. If \(q=H\), the promotion case preserves the full top
\(U_H\), again contradicting injectivity. Take
\(q=\min\{r,s\}\). \(\square\)

If upper depth-\(q\) repeat excess is \(c_q^+\), at most \(c_q^+\)
selected forest arcs can violate \(\ell>q\): every such edge lies inside
one repeated upper-target fibre.

## 6. Critical radius-crossing burden

Exact designated coverage at every controlled depth gives the universal
tag census

\[
 c_d=N_d-N_{d+1}.
\tag{6.1}
\]

It is maximized at

\[
 d_*=\sqrt{m/2}+O(1),
\]

and

\[
 \boxed{
 c_{d_*}
 =\left(\sqrt{2/e}+o(1)\right)\frac W{\sqrt m}.}
\tag{6.2}
\]

Let \(b\) be the number of selected path edges which do not strictly
decrease native radius. Deleting those \(b\) edges leaves strictly
radius-decreasing paths, each containing at most one radius-\(d_*\) state.
Therefore

\[
 \boxed{p+b\ge c_{d_*}.}
\tag{6.3}
\]

For \(p=o(W/H)\), equations (6.2)--(6.3) give (0.5). By Corollary 5.2,
every nondecreasing promotion \(r\to s\) among these edges uses an outer
slot \(\ell>r\).

This does not force \(\ell=\Theta(H)\). For fixed \(c>1\), the number of
available sources with native radius between \(q_0\) and \(cq_0\) is

\[
 N_{q_0}-N_{\lfloor cq_0\rfloor+1}
 =\left(c^2-1+o(1)\right)\frac W{\sqrt m}.
\tag{6.4}
\]

Hence at least

\[
 \boxed{
 \left(\sqrt{2/e}-(c^2-1)-o(1)\right)_+
 \frac W{\sqrt m}}
\tag{6.5}
\]

of the required nondecreasing edges have source radius greater than
\(cq_0\). Every such edge is either a genuine rotor or a promotion with
slot \(\ell>r>cq_0\). This is nonzero for

\[
 1<c<\sqrt{1+\sqrt{2/e}}.
\]

The conclusion remains only an order-\(q_0\) lookahead statement.
Unrelated SCDs may make large tag jumps from shallow sources.

Finally, the exact census hypothesis matters. If the designated hole and
duplicate counts at depths \(d,d+1\) are \(h_d,c_d^{\rm dup},h_{d+1},
c_{d+1}^{\rm dup}\), then the exact-radius count changes by at most

\[
 h_d+c_d^{\rm dup}+h_{d+1}+c_{d+1}^{\rm dup}.
\tag{6.6}
\]

Since the right side needed to erase (6.2) is only
\(\Theta(W/\sqrt m)=o(W)\), aggregate \(o(W)\) error without local
control does not preserve the peak obstruction.

## 7. Exact coupling and cut obstruction for a prescribed schedule

Fix a formal entrance-exact promotion schedule \(\mathcal F\), indexed by
\(T\in\mathcal R\). Its prescription at \(T\) includes its owner, clipped
native radius, and full nested signed flags. Define

\[
 A_T=\{c\in\{0,1\}:C_c(T)
 \text{ agrees with the complete prescription }\mathcal F(T)\}.
\tag{7.1}
\]

### Theorem 7.1 (component-intersection criterion)

There is an exact two-SCD coupling of \(\mathcal F\) if and only if

\[
 \boxed{
 \bigcap_{T\in K}A_T\ne\varnothing
 \quad\text{for every component }K\text{ of }G_{\rm sel}.}
\tag{7.2}
\]

#### Proof

By Theorem 2.1, an exact selector is one bit per component. Such a bit is
compatible with every prescribed state in \(K\) exactly when it lies in
the displayed intersection. Choices on distinct components are
independent. \(\square\)

If every \(A_T\) is a singleton, the minimum number of state
prescriptions which must be abandoned or repaired under an exact
componentwise selector is

\[
 \boxed{
 \sum_K\min\{n_{K,0},n_{K,1}\}}
\tag{7.3}
\]

where \(n_{K,c}=|\{T\in K:A_T=\{c\}\}|\).

For the defect-tolerant formulation, use the directed selector multigraph
\(\Gamma\): every target arc is directed from its colour-zero provider
root to its colour-one provider root, and every owner arc is directed in
the reverse convention which charges a repeated owner. Put

\[
 Z=\{T:z(T)=1\}.
\]

Then the exact additive mismatch-plus-selector-ledger objective for the
fixed schedule is

\[
 \boxed{
 \mathfrak C(\mathcal F)
 =\min_z\left[
   \sum_T1_{\{z(T)\notin A_T\}}
   +|\delta_\Gamma^+(Z)|
 
 \right].}
\tag{7.4}

The second term is exactly the designated target-hole plus repeated-owner
ledger. Unary incompatibility costs and directed cut costs make (7.4) an
ordinary integral \(s\)-\(t\) cut. A value
\(\mathfrak C(\mathcal F)=\Omega(W)\) is an
\(\Omega(W)\)-state obstruction to retaining that prescribed schedule.
It is not by itself an \(\Omega(W)\) literal-word lower bound: abandoned
state prescriptions may sometimes be rethreaded without one new letter
each. Such a literal conclusion needs an explicit repair toll, and a
support-only conclusion also requires that arbitrary extension flags
cannot refill the designated native holes.

Likewise, a proposed family \(\mathcal M\) of cross-colour promotion
spines fixes terminal bits at its endpoints. Its unavoidable selector
cost is the minimum directed cut over selectors satisfying those terminal
conditions. If two terminals in one equality component are forced to
opposite colours, exact coupling is impossible.

## 8. A quantitatively sufficient bounded-holonomy ladder

The preceding theorems also expose a genuine positive route. Retain the
common baseline and owner permutation \(\rho\) from (1.3). Suppose that,
on every relevant \(\rho\)-orbit \(K\), every provider map is a power of
the same permutation:

\[
 \boxed{
 \phi_{q,\sigma}(T)=\rho^{e_{q,\sigma,K}}T
 \quad
 (T\in K\cap\mathcal R_0(q)).}
\tag{8.1}
\]

Here exponents are interpreted modulo \(|K|\), and
\(e_{q_0,-,K}=0\). This is the all-depth holonomy hypothesis.

Choose a cyclic binary selector on every \(\rho\)-orbit. Let \(a_K\) be
the number of \(0\to1\) runs on \(K\), and put

\[
 a=\sum_Ka_K.
\tag{8.2}
\]

Delete the selected colour-one occurrence at the head of every
\(0\to1\) seam.

### Lemma 8.1 (exact owner repair)

After the deletion, the remaining \(N-a\) occurrences have distinct
owners, and exactly one owner is omitted at every \(1\to0\) seam.

#### Proof

For \(X=\mu_0(T)=\mu_1(\rho T)\), its pre-deletion owner load is

\[
 1-z(T)+z(\rho T).
\tag{8.3}
\]

It is two at a \(0\to1\) seam, zero at a \(1\to0\) seam, and one
elsewhere. Deleting the colour-one occurrence at every \(0\to1\) head
removes exactly the duplicate occurrences. \(\square\)

For an integer shift \(e\) on a cycle \(K\), let \(B_K(e)\) be the number
of \(1\to0\) patterns between \(z(T)\) and \(z(\rho^eT)\). Then

\[
 B_K(e)\le a_K\|e\|_K,
\tag{8.4}
\]

where \(\|e\|_K\) is cyclic distance to zero. For one interval of length
\(s\) on a cycle of length \(L\), the exact value is

\[
 B_K(e)=\min\{\|e\|_K,s,L-s\}.
\tag{8.5}
\]

Before deletion, the number of holes in row \((q,\sigma)\) is at most

\[
 \sum_KB_K(e_{q,\sigma,K}).
\]

Deletion creates at most one further hole per deleted occurrence active
in that row. Therefore the total native signed hole count obeys

\[
 \boxed{
 \mathcal H
 \le
 \sum_Ka_K\sum_{q,\sigma}\|e_{q,\sigma,K}\|_K
 +2a(H-q_0+1).}
\tag{8.6}
\]

There is an equally exact threshold ledger. If \(K'_q\) is the number of
retained selected chains with native radius at least \(q\), put
\(E_q=K'_q-N_q\). Then

\[
 |E_q|
 \le
 \sum_Ka_K\min_\sigma\|e_{q,\sigma,K}\|_K+a,
\tag{8.7}
\]

and the aggregate exact-tag error satisfies

\[
 \sum_{d=q_0}^{H}|\gamma'_d-\gamma_d|
 \le2\sum_q|E_q|.
\tag{8.8}
\]

Here \(q\) ranges from \(q_0\) through \(H\),
\(\gamma_d=N_d-N_{d+1}\) for \(d<H\), the clipped terminal class is
\(\gamma_H=N_H\), and one sets \(E_{H+1}=0\) when taking consecutive
differences.

### Theorem 8.2 (conditional physical promotion ladder)

Assume, in addition to (8.1), the following literal state conditions.

1. Every selected same-colour run has full collars for which its
   consecutive root steps are legal bridge-one, two-sided \(H\)-safe
   arcs.
2. At a \(0\to1\) seam \(T\to\rho T\), delete the occurrence at
   \(\rho T\), and use the diagonal skip

   \[
   \omega_0(T)\longrightarrow\omega_1(\rho^2T),
   \tag{8.9}
   \]

   which is required to be a legal \(H\)-safe radius-nondecreasing arc.
   Every colour-one run is assumed to have length at least two.
3. Open the physical path at every \(1\to0\) seam. Constant-colour
   orbits may be cut once, provided their selected pure-colour track is
   legal.

Let \(c_0\) be the number of constant-colour orbits. Then there is a
literal partial-annulus compiler with

\[
 p\le a+c_0
\tag{8.10}
\]

and

\[
 \boxed{L\le W+2Hp+\mathcal H.}
\tag{8.11}
\]

In particular, if

\[
 a+c_0=O(N_H)
\tag{8.12}
\]

and

\[
 \sum_Ka_K\sum_{q,\sigma}\|e_{q,\sigma,K}\|_K
 =O(HN_H),
\tag{8.13}
\]

then

\[
 \boxed{
 L=W+O(HN_H)=W+o(W),
 \qquad
 p=O(W/m)=o(W/H).}
\tag{8.14}
\]

#### Proof

Lemma 8.1 leaves \(N-a\) distinct bundled owners and \(a\) owner holes.
Appending those holes together with the \(W-N\) owners outside \(\Omega\)
makes the middle-owner contribution exactly \(W\). Conditions 1--3 join
each selected colour run across every repaired \(0\to1\) seam and open at
the opposite seams, giving (8.10). Hard starts cost \(2Hp\). Append every
remaining signed native hole; (8.6) bounds their number. This proves
(8.11).

Finally,

\[
 N_H=(1+o(1))\frac Wm,
 \qquad
 HN_H=O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W),
\]

and (8.12)--(8.13) imply (8.14). \(\square\)

This theorem is a real coefficient-one sufficient statement. Its missing
hypothesis is geometric: no pair of SCDs is presently known to satisfy
the bounded holonomy and the diagonal \(H\)-safe promotion lift.

## 9. Diagnostics for natural pairs

### 9.1 Coordinate conjugates

Suppose \(\mathscr D_1=\pi\mathscr D_0\) for a coordinate permutation
\(\pi\), and \(\pi\Omega=\Omega\). Then

\[
 \rho(T)
 =\pi\mu_0^{-1}\!\left(\pi^{-1}\mu_0(T)\right).
\tag{9.1}
\]

Likewise, if \(F_{0,q}^{\sigma}\) is the original target map, the relative
provider map is

\[
 \phi_{q,\sigma}(T)
 =\pi(F_{0,q}^{\sigma})^{-1}
   \!\left(\pi^{-1}F_{0,q}^{\sigma}(T)\right).
\tag{9.2}
\]

Thus conjugacy helps precisely when all maps (9.2) are bounded powers of
the single permutation (9.1). Mere conjugacy gives no such conclusion. If
the SCD maps are \(\pi\)-equivariant, then \(\rho\) is the identity and
there are \(N\) owner orbits, which is maximally bad for the component
scale.

### 9.2 Opposite-corner paired SCDs

For two SCDs with the same paired lower/upper half-chain skeleton, which
use opposite corners of every common central diamond, suppose additionally
that the radius-at-least-\(q_0\) owner baseline is common. On a directed
factor cycle, this says that the radius-at-least-\(q_0\) flags form a
shift-invariant set, hence that the whole factor cycle is retained or the
whole cycle is omitted. Under this extra threshold hypothesis the provider
edges are loops and the retained owner-overlay components are exactly the
retained cycles of the doubly-rainbow central two-factor. Theorem 2.1
forces an exact selector to choose one SCD's tail/head assignment on the
whole component. This is not additional edgewise orientation freedom. The
second SCD therefore supplies no within-component colour seams.

Allowing interval selectors creates one owner duplicate and one owner hole
per colour run, as in Lemma 8.1, but the required diagonal skip (8.9) is
not supplied by the paired-SCD axioms. In particular, the same-root
opposite corners have the same outer native target tower and already repeat
the depth-one upper target; their direct seam is not an automatic
full-memory bridge. This observation does not rule out the different
diagonal seam \(T\to\rho^2T\).

Without the common-baseline threshold hypothesis, active runs of a factor
cycle become open owner-overlay paths, and the different-baseline analysis
of Section 9.4 applies instead.

### 9.3 Direct complementary switching

Assume direct complementary switches are the sole nondecreasing mechanism;
in particular, there are no radius-increasing arcs. Then two visits to the
same radius layer on one path must be joined by a horizontal complementary
switch in that layer. The peak-layer cut therefore requires
\(c_{s_*}-p\) direct complementary switches at the peak radius

\[
 s_*=\sqrt{m/2}+O(1),
\]

up to a lower-order term. Directly switching a chain state there to its
complementary reversed state must
reverse at least \(2(s_*-q_0)\) forced singleton blocks. The ordered-tail
bridge formula therefore costs at least

\[
 2(s_*-q_0)-1=(\sqrt2+o(1))\sqrt m
\tag{9.3}
\]

updates per direct complementary crossing. Since
\(p=o(W/H)=o(W/\sqrt m)\), their aggregate bridge cost is at
least

\[
 \boxed{
 \left(\frac2{\sqrt e}+o(1)\right)W.}
\tag{9.4}
\]

Thus the direct complement/reversal pair is coefficient-one fatal.
Noncomplementary pairs can evade (9.3) only by satisfying the one-update
promotion spine (5.2)--(5.5).

### 9.4 Different owner baselines

If \(\Omega_0\ne\Omega_1\), the union of the two root-owner matchings is
a graph of maximum degree two. Its path components have endpoints exactly
at \(\Omega_0\triangle\Omega_1\), so their number is

\[
 \frac12|\Omega_0\triangle\Omega_1|.
\tag{9.5}
\]

Any construction which follows these owner-overlay components without
additional cross-component splices therefore needs

\[
 |\Omega_0\triangle\Omega_1|=o(W/H).
\tag{9.6}
\]

A generic \(\Theta(W/\sqrt m)\) mismatch is too large by a factor
\(\Theta(\sqrt{\log m})\). Additional physical fusions may evade this
restricted orbit count, so (9.6) is not a universal no-go outside the
owner-overlay architecture.

## 10. Proved boundary

The following statements are proved exactly.

* Exact common-baseline selectors are componentwise bits.
* Every component is an owner-, target-, and radius-neutral annular trade.
* The common owner point vector is immutable.
* The top-anchor SDR always exists.
* Cross-SCD promotions obey the exact spine formulas (5.4)--(5.7).
* Exact nondecreasing promotions are outer-slot events.
* Exact radius census forces the mass (0.5), but aggregate \(o(W)\)
  provider error can erase it at the peak.
* A prescribed promotion schedule has the exact component obstruction
  (7.2) and the directed cut obstruction (7.4).
* Bounded owner/provider holonomy plus the literal diagonal lift implies
  the coefficient-one estimate (8.14).
* Exact no-deletion canonical common-owner selectors, direct complementary
  switches, and purely equivariant conjugate pairs fail for the stated
  reasons.

What remains unproved is one tailored pair of SCDs with

\[
 \boxed{
 \begin{gathered}
 \text{a point-balanced common owner baseline,}\\
 O(N_H)\text{ owner-scale colour runs,}\\
 \text{bounded all-depth provider holonomy, and}\\
 \Theta(W/\sqrt m)\text{ legal radius-nondecreasing outer-slot spines,}
 \end{gathered}}
\]

including the diagonal skips after duplicate-owner deletion.

Thus two unrelated SCDs can help only by ceasing to be unrelated: their
relative maps must organize into one common promotion-scale orbit system.
The algebraic sufficient theorem is complete; the physical promotion
ladder is the remaining construction gate.
