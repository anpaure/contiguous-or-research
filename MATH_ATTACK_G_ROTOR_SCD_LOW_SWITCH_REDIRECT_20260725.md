# Line G redirect: exact obstructions to low-switch rotor--SCD resolution

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer enumeration, or long local job is used.

## 0. Outcome

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_d=\binom{2m}{m-d},\qquad
Q_m=(2m-1)(2m)!,
\]

and let \(H=\lceil A\sqrt m\rceil\), where \(A>0\) is fixed. For a full
SCD \(\mathcal D\), clipped at radius \(H\), let
\(p_d^*(\mathcal D)\) be the minimum number of components in a spanning
directed rotor path forest on its radius-\(d\) chain states, and put

\[
\widehat\Phi_H(\mathcal D)
=\sum_{d=0}^H2d\,p_d^*(\mathcal D).
\tag{0.1}
\]

The audited chronology theorem says exactly

\[
\min\{\text{weighted run-start toll in the exact rotor master}\}
=Q_m\min_{\mathcal D\ {\rm full\ SCD}}\widehat\Phi_H(\mathcal D).
\tag{0.2}
\]

Thus the requested coloring theorem is equivalent to constructing one full
integral SCD with \(\widehat\Phi_H=o(W)\). The additional physical
initialization in the orbit construction is then \(o(Q_mW)\), including the
separate \(O(Q_mW/m)\) radius-zero term.

I do **not** prove or refute this last existence statement. Consequently this
report does not prove the constant-one contiguous-OR theorem. It does prove
three new exact obstruction theorems which close three broad proposed
shortcuts.

1. **Recursive Hall is simultaneous forced-target agreement.** At one
   layer, the minimum number of inherited rotor edges which must be deleted
   is exactly the disagreement of a pair of integral Boolean-lattice perfect
   matchings with two forced endpoint labels. It splits into a
   paired-rainbow defect and a Boolean extendability loss.
2. **Frozen palette reconciliation has a complete truncated-window
   hierarchy.** Every scale \(\ell\), not only the component count
   \(\ell=1\), gives a lower bound on palette switches. This proves exact
   \(\Theta(Q_mW\sqrt m)\) failure for a BTK target and forces every
   successful frozen-palette target to be a positive-density distance from
   every relabelled BTK SCD in each typical-radius annulus.
3. **The Johnson-label Hall certificate has a robust integral nested null
   cone.** Exact integer masses, exact one-design margins, the correct
   terminal radius counts, and common nested \(Z_1\subset\cdots\subset Z_d\)
   flags can all have zero Johnson deficiency simultaneously. Therefore no
   universal lower bound can follow from those data alone. One-color
   two-sided rank ownership or actual rotor liftability is indispensable.

There are two further exact counterexamples. A globally contiguous radius
order with one active/inactive boundary can have an isolated lower target
before rotor constraints are imposed. And an almost-complete radius-one
packing with only one missing top chain need not extend to a band SCD.

These are architecture-level no-go theorems. They do not exclude an exotic
SCD, necessarily far from BTK, whose two-sided ownership and actual rotor
paths are correlated globally.

## 1. Audited input: the exact coloring statistic

For \(d<H\), every clipped full SCD has

\[
\gamma_d=N_d-N_{d+1}
\]

radius-\(d\) states, while \(\gamma_H=N_H\). A positive-radius state is

\[
\omega=(L;z_1,\ldots,z_{2d};R),
\qquad |L|=|R|=m-d,
\]

and its rotor successors are

\[
(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
\qquad x\in L,\ y\in R.
\tag{1.1}
\]

At radius zero one uses the ordinary Johnson swap. A directed run through
\(t\) radius-\(d\) states has exact hard-reset prefix length \(t+2d\).
The complete coordinate orbit of prescribed path forests can be Eulerized
integrally while retaining every selected monochromatic path. Conversely,
the runs in each genuine SCD color are spanning rotor path forests.
These two statements give (0.2). They also show that fractional SCD
marginals, separate depthwise SCDs, or an unextendible almost-cover cannot
prove the desired coloring.

The remainder of this report attacks the three surviving integral
formulations.

## 2. Exact forced-target agreement at one recursive layer

Assume a saturated SCD has been built through radius \(h\). Let \(V_h\) be
its \(N_h\) top states, choose an active set

\[
A_h\subseteq V_h,\qquad |A_h|=N_{h+1},
\]

and let \(E_h\) be the active-induced edges of an inherited directed rotor
forest. Write an edge as

\[
e:v\longrightarrow w,
\]

where the rotor update uses \(x_e\in L_v\) and \(y_e\in R_v\). Define the
forced lower and upper-complement targets

\[
\lambda(e)=L_v-\{x_e\},\qquad
\rho(e)=R_v-\{y_e\}.
\tag{2.1}
\]

Both have rank \(m-h-1\).

Let \(\mathfrak M_-(A_h)\) be the perfect matchings

\[
P^-:A_h\longrightarrow\binom{[2m]}{m-h-1},
\qquad P^-(v)\subset L_v,
\tag{2.2}
\]

and define \(\mathfrak M_+(A_h)\) analogously, with
\(P^+(v)\subset R_v\). If either matching family is empty, this active set
cannot be extended even after every rotor edge is deleted.

### Theorem 2.1 (forced-target agreement)

Assume both matching families are nonempty. For
\(P^-\in\mathfrak M_-(A_h)\) and
\(P^+\in\mathfrak M_+(A_h)\), the edge \(e:v\to w\) lifts to radius
\(h+1\) if and only if

\[
\boxed{
P^-(v)=\lambda(e),\qquad P^+(w)=\rho(e).
}
\tag{2.3}
\]

Consequently, if

\[
M_h^\star
=\max_{P^-,P^+}
\left|\left\{
e=v\to w\in E_h:
P^-(v)=\lambda(e),\
P^+(w)=\rho(e)
\right\}\right|,
\tag{2.4}
\]

then the exact minimum number of active rotor-edge deletions at this layer
is

\[
\boxed{k_h^{\min}=|E_h|-M_h^\star.}
\tag{2.5}
\]

#### Proof

An extension of

\[
v=(L_v;z_1(v),\ldots,z_{2h}(v);R_v)
\]

chooses \(\ell_v\in L_v\), \(u_v\in R_v\), and has lower endpoint
\(L_v-\ell_v\) and upper-complement endpoint \(R_v-u_v\). The exact
one-edge lift criterion is

\[
\ell_v=x_e,\qquad
u_w=z_{2h}(v),\qquad
\ell_w\ne y_e,\qquad
u_v\ne y_e
\tag{2.6}
\]

for \(h\ge1\); at \(h=0\), \(u_w=x_e\).

The first equality in (2.6) is equivalent to
\(P^-(v)=L_v-x_e=\lambda(e)\). For \(h\ge1\),

\[
R_w=R_v-y_e+z_{2h}(v),
\]

so \(P^+(w)=R_w-z_{2h}(v)=R_v-y_e=\rho(e)\). At \(h=0\),
\(R_w=R_v-y_e+x_e\), and the same conclusion follows from \(u_w=x_e\).

The two inequalities in (2.6) are automatic from injectivity. If
\(\ell_w=y_e\), then

\[
P^-(w)=L_w-y_e=L_v-x_e=P^-(v),
\]

contrary to injectivity of \(P^-\). If \(u_v=y_e\), then

\[
P^+(v)=R_v-y_e=P^+(w),
\]

contrary to injectivity of \(P^+\). Thus (2.3) is equivalent to the full
lift criterion.

Every pair of perfect matchings therefore retains exactly its agreement set
in (2.4), and every feasible extension arises from such a pair. Maximizing
retained edges proves (2.5). \(\square\)

Form the bipartite multigraph \(\mathscr B_h\) with left and right vertex
sets consisting of rank-\((m-h-1)\) masks, and with the occurrence \(e\)
joining \(\lambda(e)\) to \(\rho(e)\). Let \(\nu_h\) be its matching
number. Any retainable edge family has distinct \(\lambda\)-targets and
distinct \(\rho\)-targets, so \(M_h^\star\le\nu_h\). Hence

\[
\boxed{
k_h^{\min}
=
\underbrace{|E_h|-\nu_h}_{\text{paired-rainbow defect}}
+
\underbrace{\nu_h-M_h^\star}_{\text{Boolean extendability loss}}.
}
\tag{2.7}
\]

There is no additional consecutive-edge obstruction hidden in (2.7). For
consecutive edges \(e:v\to w\), \(f:w\to u\),

\[
\lambda(f)=\lambda(e)\iff x_f=y_e,
\]

and, for \(h\ge1\),

\[
\rho(f)=\rho(e)\iff y_f=z_{2h}(v);
\]

at \(h=0\), the second collision is \(y_f=x_e\). Thus the local forbidden
pairs are already forced-target collisions in \(\mathscr B_h\).

The one-layer identity does not authorize independent minimization at
successive layers: a maximizing pair \((P_h^-,P_h^+)\) changes the states,
and hence the agreement instance, at layer \(h+1\). The exact surviving
*dynamic* condition for this recursive construction is the following. Find
one recursively compatible
sequence of active sets and matching pairs, satisfying the contiguous-block
and no-merger hypotheses of the recursive toll ledger, and put

\[
a_h=
\left|\left\{
e=v\to w\in E_h:
P_h^-(v)=\lambda(e),\ P_h^+(w)=\rho(e)
\right\}\right|,
\qquad
k_h=|E_h|-a_h.
\tag{2.8}
\]

The required estimate is

\[
\boxed{\sum_{h<H}k_h=o(W/H).}
\tag{2.9}
\]

For every realized layer,

\[
k_h\ge |E_h|-M_h^\star
=(|E_h|-\nu_h)+(\nu_h-M_h^\star),
\tag{2.10}
\]

with equality precisely when the chosen pair attains the one-layer optimum.
Thus the paired-rainbow and Boolean-extendability defects are exact local
obstructions, but their separately minimizing pairs need not compose.
Together with the previously proved recursive toll ledger, one compatible
sequence satisfying (2.9) would give \(\widehat\Phi_H=o(W)\) and hence the
constant-one theorem. This dynamically compatible existence statement is
**unproved**.

### Theorem 2.2 (quantitative dynamic composition)

Fix \(A>0\). If the exact odd-cut recursive construction admits a compatible
sequence satisfying (2.9), then it produces a full integral SCD
\(\mathcal D\) for which

\[
\widehat\Phi_H(\mathcal D)
\le H(H-1)+2H(B+1)+2H\sum_{h<H}k_h=o(W).
\tag{2.11}
\]

Consequently the complete coordinate-orbit coloring is integral, consists
of genuine SCD colors, and has total weighted run-start toll \(o(Q_mW)\).
The established positive-radius physical circuit-initialization charge is
at most \(2Q_m\widehat\Phi_H\), and the separate radius-zero charge is
\(O(Q_mW/m)\); hence the full literal orbit construction has \(o(Q_mW)\)
initialization overhead as well.
If the hypothesis holds for every fixed \(A\), the audited outer-tail
estimate and then \(A\to\infty\) give

\[
\nu(2m)\le(1+o(1))\binom{2m}{m}.
\tag{2.12}
\]

The audited trimmed one-bit lift then gives
\(\nu(k)\le(1+o(1))W(k)\) in all dimensions.

#### Proof

The perfect matchings at layer \(h\) extend every active chain by one lower
and one upper mask. Their bijectivity preserves exact ownership at both new
boundary ranks, while the agreement set in (2.8) preserves precisely the
undeleted inherited rotor edges. Recursive compatibility therefore gives
one saturated depth-\(H\) band SCD; the band-extension theorem completes it
to a full SCD without changing its band states.

For the globally contiguous radius blocks, the exact recursive ledger is

\[
\widehat\Phi_H
\le H(H-1)+2H(B+1)+2H K_H,
\qquad K_H=\sum_{h<H}k_h.
\]

Here \(H=O_A(\sqrt m)\), \(B=W/(m+1)\), and (2.9) says
\(HK_H=o(W)\). Thus every term on the right is \(o(W)\), proving (2.11).
Equation (0.2) gives the exact integral orbit toll. The already audited tail
bound gives, for fixed \(A\),

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{\binom{2m}{m}}
\le 1+O\bigl((1+A^2)e^{-A^2}\bigr),
\]

and sending \(A\to\infty\) proves (2.12). The audited odd-dimensional
lift supplies the final assertion. \(\square\)

### Corollary 2.3 (initial paired-shadow obstruction)

The exact odd-cut forest has \(B=\operatorname{Cat}_m=W/(m+1)\) paths,
\(W\) middle vertices, and \(N_1\) edges. Deactivating \(B\) vertices
removes at most \(2B\) path edges. If
\(\nu_0^{\rm full}\) is the matching number of the paired
\((\lambda,\rho)\)-label multigraph of all odd-cut edges, then every active
choice obeys

\[
\boxed{k_0\ge N_1-\nu_0^{\rm full}-2B.}
\tag{2.13}
\]

Indeed, the active edge count is at least \(N_1-2B\), while its paired
matching number is at most \(\nu_0^{\rm full}\). Thus a positive-density
paired-shadow defect at the first lift already forces
\(k_0=\Omega(W)\), far above the scale \(o(W/H)\).

## 3. One boundary does not imply Hall

Let the current lower endpoints have rank \(r\), and let
\(I_L\subseteq\binom{[2m]}r\) be the endpoints of the inactive states.
Assume, as in the exact recursive layer, that

\[
\left|\binom{[2m]}r\setminus I_L\right|
=\binom{2m}{r-1}.
\tag{3.1}
\]

Before any rotor constraint is imposed, the active lower extension graph
has a perfect matching onto all rank-\((r-1)\) targets if and only if

\[
\boxed{
|I_L\cap\nabla\mathcal T|
\le|\nabla\mathcal T|-|\mathcal T|
\quad
\text{for every }
\mathcal T\subseteq\binom{[2m]}{r-1},
}
\tag{3.2}
\]

where \(\nabla\mathcal T\) is the full immediate upper shadow. The upper
statement is identical after replacing upper endpoints by their complements;
throughout, \(I_R\) denotes those inactive upper-complement masks.

#### Proof

The active neighbors of \(\mathcal T\) are exactly

\[
\nabla\mathcal T\setminus I_L.
\]

Hall's inequality
\(|\nabla\mathcal T\setminus I_L|\ge|\mathcal T|\) is precisely (3.2),
and (3.1) turns the target-saturating matching into a perfect matching.
\(\square\)

This exact cut system gives a counterexample to every order-free claim that
global contiguity supplies Hall. Fix
\(T\in\binom{[2m]}{m-1}\). Its \(m+1\) middle supersets occur in at most
\(m+1\) odd-cut paths. Put all of those paths first. Each odd-cut path has
exactly \(m+1\) centers, so they occupy at most \((m+1)^2\) consecutive
centers. The elementary estimate

\[
\binom{2m}{m}\ge\frac{4^m}{2m+1}
\]

gives, for all sufficiently large \(m\),

\[
B=\operatorname{Cat}_m
\ge\frac{4^m}{(2m+1)(m+1)}>(m+1)^2.
\]

Fill the rest of the first \(B\) positions arbitrarily. If this first block
is the inactive radius-zero block, the active suffix contains no superset of
\(T\). Thus \(T\) is isolated in the unrestricted lower extension graph.
Nevertheless there is at most one active/inactive crossing along the
concatenated path forest.

No rotor-edge deletion repairs this failure, because the active vertex set
is already fixed. Therefore

\[
\boxed{
\text{one global boundary, or }s_0\le1,\text{ does not imply even
unconstrained lower Hall.}
}
\tag{3.3}
\]

This refutes order-free and boundary-count-only versions of the recursive
lift. It does not refute an existentially chosen good path order.

## 4. Defect-one failure of band absorption

Correct residual rank counts, even with leave one, do not imply completion.

### Theorem 4.1 (defect-one noncompletion)

For every \(m\ge2\), there is a mask-disjoint family of \(N_1-1\)
saturated radius-one chains in \(B_{2m}\) which cannot be completed,
while preserving those chains, to a depth-one band SCD.

#### Proof

Split the coordinates as \(X\sqcup D\), where \(|D|=4\). Choose an SCD of
\(B_X\) containing a singleton middle chain \(\{C\}\), with
\(|C|=m-2\), and take its product with an SCD of \(B_D\). Because
\(\{C\}\) is a singleton factor chain, its product fiber is an undisturbed
copy of an SCD of \(B_4\). Its clipped depth-one part contains four
radius-one triples. For example, one may use

\[
\varnothing<2<12<123<1234,\quad
1<13<134,\quad
3<23<234,\quad
4<14<124,
\]

together with the singleton chains \(24\) and \(34\).

Remove those four triples and insert

\[
C+\bigl(\{2\}<\{1,2\}<\{1,2,3\}\bigr),
\]

\[
C+\bigl(\{3\}<\{1,3\}<\{1,3,4\}\bigr),
\]

\[
C+\bigl(\{4\}<\{1,4\}<\{1,2,4\}\bigr).
\tag{4.1}
\]

Together with all nonlocal radius-one triples, these are \(N_1-1\)
pairwise mask-disjoint saturated triples. The only uncovered boundary masks
are

\[
C+\{1\},\qquad C+\{2,3,4\}.
\tag{4.2}
\]

They are incomparable. For the displayed local SCD, the unused middle mask
among the removed triples is \(C+\{2,3\}\); the middle rank is not the
obstruction. A preserving completion has only one lower and one upper mask
left, so it would have to place (4.2) in one saturated triple, which is
impossible. \(\square\)

Thus no fixed-band absorption theorem can follow merely from equal rank
counts, an \(o(W)\) leave, or even a one-chain leave. A successful rotor-atom
packing must enforce genuine completion cuts.

## 5. A multiscale obstruction to frozen palette recoloring

Fix a radius \(d\). Let \(F_d^0\) be the low-run pseudo-forest in one
pseudo-color, with \(\gamma_d\) vertices and \(p_d^0\) components. For an
integer \(\ell\ge1\), define

\[
M_{d,\ell}^0
=\sum_{R\in F_d^0}(|R|-\ell)_+,
\tag{5.1}
\]

where \(|R|\) is the number of vertices. Thus
\((|R|-\ell)_+\) counts the \(\ell\)-edge windows in \(R\).

For the radius-\(d\) class \(D_d\) of a target SCD, put

\[
M_{d,\ell}(D)
=\max_F\sum_{R\in F}(|R|-\ell)_+,
\tag{5.2}
\]

where \(F\) ranges over all spanning vertex-disjoint directed rotor path
forests in \(G_d[D_d]\).

### Theorem 5.1 (truncated-window palette obstruction)

Every integral frozen packet-palette recoloring into the complete coordinate
orbit of \(D\) satisfies

\[
\boxed{
V_d^*
\ge
\frac{Q_m}{\ell}
\bigl(M_{d,\ell}^0-M_{d,\ell}(D)\bigr)_+.
}
\tag{5.3}
\]

Equivalently, define

\[
\kappa_{d,\ell}(D)
=\min_F\sum_{R\in F}\min\{|R|,\ell\},
\qquad
\kappa_{d,\ell}^0
=\sum_{R\in F_d^0}\min\{|R|,\ell\}.
\tag{5.4}
\]

Then

\[
\boxed{
V_d^*
\ge
\frac{Q_m}{\ell}
\bigl(\kappa_{d,\ell}(D)-\kappa_{d,\ell}^0\bigr)_+.
}
\tag{5.5}
\]

#### Proof

Across the \(Q_m\) pseudo-colors there are
\(Q_mM_{d,\ell}^0\) \(\ell\)-edge windows. A color switch belongs to at
most \(\ell\) such windows. Therefore at least

\[
Q_mM_{d,\ell}^0-\ell V_d(C)
\tag{5.6}
\]

windows are monochromatic under a palette field \(C\).

For one target color, its maximal monochromatic runs are vertex-disjoint
directed rotor paths. The statewise palette partition gives that color
exactly one occurrence of every state in its radius-\(d\) class, so those
runs span the target class. Their number of monochromatic
\(\ell\)-windows is at most \(M_{d,\ell}(D)\). All \(Q_m\) target colors
are coordinate copies of \(D\). Hence

\[
Q_mM_{d,\ell}^0-\ell V_d(C)
\le Q_mM_{d,\ell}(D).
\]

Minimizing over palette fields proves (5.3). Finally,

\[
\sum_R(|R|-\ell)_+
=\gamma_d-\sum_R\min\{|R|,\ell\},
\]

which proves (5.5). \(\square\)

At \(\ell=1\), (5.5) recovers the component bound

\[
V_d^*\ge Q_m\bigl(p_d^*(D)-p_d^0\bigr)_+.
\tag{5.7}
\]

For larger \(\ell\), it says that agreement of component counts alone is
insufficient: the whole truncated run-length profile of the target must
dominate that of the low-run pseudo-resolution.

### Theorem 5.2 (exact BTK palette failure)

Let \(\mathcal B\) be the Greene--Kleitman/BTK SCD. For every native
radius \(1\le d<H\),

\[
\boxed{
V_d^*(\mathcal B)=Q_m(c_d-p_d^0),
\qquad
\text{number of radius-}d\text{ runs}=Q_mc_d,
}
\tag{5.8}
\]

where \(c_d=N_d-N_{d+1}\).

#### Proof

The induced positive-radius rotor graph on every relabelled BTK class is
empty. Hence the admissible target-color palettes of the two endpoints of
every pseudo internal edge are disjoint. Every copy of every internal
pseudo edge must switch. One pseudo-forest has \(c_d-p_d^0\) internal
edges, proving the switch identity. Adding its \(p_d^0\) hard starts per
target color gives \(Q_mc_d\) runs. \(\square\)

Fix \(0<a<b<A\) and let

\[
I_m=\{d:a\sqrt m\le d\le b\sqrt m\}.
\]

Uniformly on this annulus,

\[
\frac{N_d}{W}=e^{-d^2/m+o(1)},\qquad
c_d=N_d\frac{2d+1}{m+d+1}.
\]

Therefore

\[
\boxed{
\sum_{d\in I_m}2d\,Q_mc_d
=
\left(
4\int_a^b x^2e^{-x^2}\,dx+o(1)
\right)Q_mW\sqrt m.
}
\tag{5.9}
\]

Thus the canonical frozen target misses the desired \(o(Q_mW)\) toll by a
factor \(\Theta(\sqrt m)\).

### Theorem 5.3 (positive-density BTK-distance obstruction)

For a full SCD \(D\), define

\[
k_d(D)
=\min_{\sigma\in S_{2m}}
|D_d\setminus(\sigma\mathcal B)_d|.
\tag{5.10}
\]

Then

\[
\boxed{p_d^*(D)\ge c_d-2k_d(D).}
\tag{5.11}
\]

Consequently every frozen palette resolution has at least

\[
Q_m(c_d-2k_d(D))_+
\tag{5.12}
\]

radius-\(d\) monochromatic runs.

#### Proof

Fix a relabelling attaining \(k_d\), and take a spanning rotor path forest
on \(D_d\). No selected edge can have both endpoints in
\(D_d\cap(\sigma\mathcal B)_d\), since the relabelled BTK class is
rotor-independent. Thus every selected edge touches one of the \(k_d\)
states outside that class. A path-forest vertex has total degree at most
two, so there are at most \(2k_d\) edges. A forest on \(c_d\) vertices
therefore has at least \(c_d-2k_d\) components. Minimize over forests to
obtain (5.11). Equation (5.12) follows from (5.7), after adding the
\(Q_mp_d^0\) hard starts. \(\square\)

If the total corrected run-start toll is \(o(Q_mW)\), then (5.9)--(5.12)
give, with

\[
J_{a,b}=\int_a^b x^2e^{-x^2}\,dx,
\]

\[
\sum_{d\in I_m}2d\,k_d(D)
\ge(2J_{a,b}+o(1))W\sqrt m,
\tag{5.13}
\]

and hence

\[
\boxed{
\sum_{d\in I_m}k_d(D)
\ge\left(\frac{J_{a,b}}b+o(1)\right)W.
}
\tag{5.14}
\]

Thus a target-uniform BTK palette and every \(o(W)\)-state perturbation of
the best independently relabelled BTK classes are rigorously impossible.
The estimate does not exclude an SCD which is globally and
positive-density different from BTK.

## 6. The Johnson deficiency has an integral nested null cone

For \(1\le q\le H\), let

\[
J_q=J(2m,2q),\qquad
\Gamma_q(\mathcal S)
=\{Z':|Z\cap Z'|=2q-1\text{ for some }Z\in\mathcal S\}.
\]

For a nonnegative measure \(\mu\) on the \(2q\)-subsets, define

\[
\Delta_q(\mu)
=\max_{\mathcal S}
\bigl(\mu(\mathcal S)-\mu(\Gamma_q(\mathcal S))\bigr)_+.
\tag{6.1}
\]

The previously proved Johnson-label theorem gives
\(P_q\ge\Delta_q(\mu_q)\). The following results show that this certificate
cannot by itself prove a positive universal toll.

### Theorem 6.1 (exact transport kernel)

\(\Delta_q(\mu)=0\) if and only if there is a nonnegative transport
\(x_{ZZ'}\), supported on Johnson edges, with both marginals equal to
\(\mu\):

\[
\sum_{Z'}x_{ZZ'}=\mu(Z),\qquad
\sum_Zx_{ZZ'}=\mu(Z').
\tag{6.2}
\]

#### Proof

Use left and right copies of the label set. Give the source-to-left and
right-to-sink arcs capacities \(\mu\), and put infinite capacity on
left-to-right Johnson edges. The max-flow cut inequalities are exactly

\[
\mu(\mathcal S)\le\mu(\Gamma_q(\mathcal S)).
\]

Thus a flow of total mass \(\sum_Z\mu(Z)\) exists exactly when
\(\Delta_q(\mu)=0\). Its edge values are (6.2). \(\square\)

For \(1\le q\le m-1\), \(J_q\) is connected and nonbipartite. Hence every
proper nonempty \(\mathcal S\) satisfies

\[
|\Gamma_q(\mathcal S)|\ge|\mathcal S|+1.
\tag{6.3}
\]

Indeed, equality in the regular-graph edge count would make
\(\Gamma_q(\Gamma_q(\mathcal S))\subseteq\mathcal S\). Connectivity then
forces either the full vertex set or a bipartition, and the latter is
excluded by a Johnson triangle.

Consequently, if \(u>0\) and

\[
\|\mu-u\mathbf1\|_1\le u,
\tag{6.4}
\]

then

\[
\boxed{\Delta_q(\mu)=0.}
\tag{6.5}
\]

For if \(\delta=\mu-u\mathbf1\), then for a proper nonempty
\(\mathcal S\),

\[
\mu(\mathcal S)-\mu(\Gamma_q(\mathcal S))
\le-u+
\sum_{Z\in\mathcal S\triangle\Gamma_q(\mathcal S)}|\delta(Z)|
\le0.
\]

The empty and full cuts are immediate.

### Theorem 6.2 (integral exact-margin null measures)

For all sufficiently large \(m\), uniformly for \(q\le H\), there is an
integer measure

\[
\mu_q:\binom{[2m]}{2q}\longrightarrow\mathbb Z_{\ge0}
\]

with

\[
\sum_Z\mu_q(Z)=N_q,
\tag{6.6}
\]

\[
\sum_{Z\ni i}\mu_q(Z)
=\frac{2q}{2m}N_q
=\binom{2m-1}{m+q-1}
 -\binom{2m-1}{m-q-1}
\quad(i\in[2m]),
\tag{6.7}
\]

and

\[
\boxed{\Delta_q(\mu_q)=0.}
\tag{6.8}
\]

#### Proof

Let

\[
L_q=\binom{2m}{2q},\qquad
u_q=\frac{N_q}{L_q},
\]

and write

\[
N_q=aL_q+r,\qquad 0\le r<L_q.
\]

Put \(k=2q\). Both \(kN_q/(2m)\) and \(kL_q/(2m)\) are integers, so

\[
s=\frac{kr}{2m}
\]

is an integer. Repeat the word \(0,1,\ldots,2m-1\) exactly \(s\) times
and split its \(2ms=kr\) positions into \(r\) consecutive blocks of
length \(k\). Every block is a \(k\)-set because \(k<2m\). If \(e_Z\)
counts blocks equal to \(Z\), then

\[
\sum_Ze_Z=r,\qquad \sum_{Z\ni i}e_Z=s.
\]

Define

\[
\mu_q(Z)=a+e_Z.
\tag{6.9}
\]

This proves (6.6)--(6.7), and

\[
\|\mu_q-u_q\mathbf1\|_1<2L_q.
\tag{6.10}
\]

Uniformly for \(q\le A\sqrt m\),

\[
N_q\ge\alpha_AW
\]

for some \(\alpha_A>0\), while

\[
\log L_q
\le A\sqrt m\log m+O_A(\sqrt m).
\]

Since \(\log W=2m\log2+O(\log m)\), one has
\(N_q>2L_q^2\) for all large \(m\), uniformly in the window. Thus
\(u_q>2L_q\), and (6.4), (6.10) prove (6.8). \(\square\)

### Theorem 6.3 (common integral nesting with zero deficiency)

The measures in Theorem 6.2 can be coupled into disjoint integral flags

\[
Z_1\subset Z_2\subset\cdots\subset Z_d,\qquad |Z_q|=2q,
\tag{6.11}
\]

so that exactly \(N_d-N_{d+1}\) flags terminate at every \(d<H\), exactly
\(N_H\) terminate at \(H\), and the level-\(q\) multiplicity is
\(\mu_q\). Thus every level has \(\Delta_q=0\) simultaneously.

#### Proof

Between levels \(q+1\) and \(q\), join a \((2q+2)\)-label to every
contained \(2q\)-label. For an upper-label family \(\mathcal T\), write
\(\partial\mathcal T\) for its full lower shadow. Biregularity gives

\[
|\partial\mathcal T|
\ge\frac{L_q}{L_{q+1}}|\mathcal T|.
\tag{6.12}
\]

Hence the uniform measures have cut slack at least

\[
u_q|\partial\mathcal T|-u_{q+1}|\mathcal T|
\ge\frac{N_q-N_{q+1}}{L_{q+1}}|\mathcal T|.
\tag{6.13}
\]

For \(q\ge1\),

\[
N_q-N_{q+1}
=N_q\frac{2q+1}{m+q+1}
\ge\alpha_A'\frac Wm.
\tag{6.14}
\]

Let \(\Lambda_H=\max_{j\le H}L_j\). The preceding estimates give

\[
\frac{W}{m\Lambda_H^2}\longrightarrow\infty.
\]

Therefore, uniformly for \(q<H\),

\[
\frac{N_q-N_{q+1}}{L_{q+1}}
>
\|\mu_q-u_q\mathbf1\|_1+
\|\mu_{q+1}-u_{q+1}\mathbf1\|_1.
\tag{6.15}
\]

Equations (6.13)--(6.15) imply every multiset Hall cut

\[
\mu_{q+1}(\mathcal T)
\le\mu_q(\partial\mathcal T).
\]

Integral max flow injects every level-\((q+1)\) occurrence into a distinct
contained level-\(q\) occurrence. At level zero, inject all \(N_1\)
occurrences into \(W\) distinguishable copies of the empty label. Iterating
the injections gives disjoint nested flags. The unused level-\(q\) copies
number \(N_q-N_{q+1}\), exactly the required number of flags terminating at
that radius. \(\square\)

An abstract flag is locally compatible with a chain-state central label:
order the two new coordinates added at each step on opposite sides of the
central singleton word, and split the remaining coordinates into two equal
residual blocks. The construction does **not** provide simultaneous
bijections of the lower and upper masks at every rank, and does not lift the
Johnson transports to actual rotor arcs.

There is also a literal multicover null. For any full SCD \(\mathcal D\),
the union

\[
\bigsqcup_{\sigma\in S_{2m}}\sigma\mathcal D
\]

is an integral \((2m)!\)-fold multicover by genuine full SCDs, and its
aggregate \(\mu_q\) is uniform. Thus all aggregate Johnson deficiencies
vanish. Summing colors is not the same as extracting one good integral
color.

Theorems 6.1--6.3 prove the definitive certificate no-go

\[
\boxed{
\text{integrality, exact one-design margins, and common nested }Z_q
\text{ flags do not force positive Johnson deficiency.}
}
\tag{6.16}
\]

Any universal negative proof must use one-color two-sided rank ownership or
actual state-level rotor adjacency.

## 7. Exact status after the redirect

The following routes are now rigorously closed.

1. **Color-blind Johnson deficiency.** The full suite of integral nested
   label constraints admits a null system of the kind constructed in
   Section 6.
2. **Canonical frozen palette reconciliation.** BTK has exact
   \(\Theta(Q_mW\sqrt m)\) toll, and every successful frozen-palette target
   is a positive-density distance from all its relabellings on every
   typical annulus.
3. **Boundary-count-only recursive lifting.** Even \(s_0\le1\) can coexist
   with an isolated Hall target.
4. **Rank-count-only absorption.** Defect one already need not complete to
   a band SCD.

The exact recursive obstruction which remains is the dynamically compatible
estimate (2.9), with the local lower bound (2.10). The exact frozen-palette
obstruction is the full hierarchy (5.3), not merely its
\(\ell=1\) component count. Neither is bounded at the required scale for a
genuinely noncanonical SCD.

Thus the rotor coloring lemma and the constant-one theorem remain
**unproved**. A successful continuation must construct one full integral
SCD whose typical-radius states are globally far from BTK and whose
two-sided Boolean owners support mesoscopically long actual rotor paths.
Separate rank marginals, a common nested label flow, an abstract Johnson
self-transport, and a low-boundary chronology are all rigorously
insufficient.

## 8. Adversarial audit checklist

1. The exact run weight is \(2d\), not \(2d+1\); the latter is only the
   conservative canonical-reset ledger.
2. Theorem 2.1 assumes the unrestricted lower and upper endpoint graphs
   each possess a perfect matching. If either fails, no edge deletion can
   rescue that active set.
3. The two residual inequalities in the one-edge lift theorem are not
   dropped: injectivity of \(P^-\) and \(P^+\) proves them automatically.
4. The paired-label matching number \(\nu_h\) is only an upper bound on
   simultaneous extendable agreement. The nonnegative gap
   \(\nu_h-M_h^\star\) is retained explicitly. Moreover, independently
   optimal matching pairs at different layers are not asserted to compose;
   (2.9) quantifies over one recursively compatible sequence.
5. The bad path order disproves an order-free implication, not existential
   recursive Hall with a specially selected order.
6. The defect-one packing is not a rotor-cycle packing and does not refute
   the existential absorber. It refutes deduction of absorption from leave
   size or rank counts alone.
7. In Theorem 5.1, \(|R|\) counts vertices; an \(\ell\)-edge window uses
   \(\ell+1\) vertices and is counted by \((|R|-\ell)_+\).
8. A switch lies in at most \(\ell\) such windows; openness of the packet
   paths is used.
9. BTK is invoked only at native radii \(d<H\), and \(b<A\) keeps the
   annulus away from the clipped top class.
10. The factor two in (5.11) is necessary for this argument because one
    changed state can support one incoming and one outgoing forest edge.
11. The nested null flags lack simultaneous lower/upper rank bijections and
    actual rotor arcs. They are not promoted to an SCD.
12. No result here is asserted as a lower bound for arbitrary contiguous-OR
    words outside the rotor/SCD architecture.
