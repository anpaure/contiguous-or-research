# O/N cross-audit and a positive distant-factor corridor-flow theorem

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Exact outcome

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

The numerical core of
MATH_ATTACK_N_AO_LINEAR_HOLE_OBSTRUCTION_20260725.md passes audit:

\[
\frac{(2m-3)\operatorname{Cat}_{m-2}}W
=\frac{m(m+1)}{4(2m-1)(2m+1)}
\longrightarrow\frac1{16},
\]

and a factor at row distance \(b\) from canonical MSW satisfies

\[
T_1\ge
\left[
(2m-3)\operatorname{Cat}_{m-2}
-(m-1)b-\frac{2W}{m+2}
\right]_+.
\]

Thus \(T_1=o(W)\) forces

\[
b\ge(1/8-o(1))B.
\]

The only correction to the depth-one bounded-star theorem is scope:
each displayed star has a nonempty admissible high-count interval when the
high family may depend on that star. It does not construct one simultaneous
high family and is false for an arbitrary prescribed high family.

The new result is positive. At one stage, clip the canonical histogram at
the floor and ceiling. There is an explicit set of exactly

\[
\mathfrak O=\max\left\{
\sum_v(c-\mu(v))_+,\ 
\sum_v(\mu(v)-c-1)_+
\right\}
\]

owners whose release would make the retained canonical assignments
extend to a balanced histogram. If the released owners satisfy one direct
owner-to-deficit Hall corridor, they can be matched integrally and exactly
\(\mathfrak O\) owners change. This attains the information-theoretic
histogram lower bound with no transport amplification.

For the actual cyclic sibling relation, this coefficient-one conclusion
has four explicit necessary-and-sufficient submodular entrance-cut
families, (5.3)--(5.6). They eliminate the existential choice of which
excess copies to release and which low cells to declare high.

More generally, for the actual anchor-to-alternate owner digraph, all
nonstar Hall inequalities are precisely the cut conditions of a
unit-capacity transshipment. Fractional high variables and fractional
owner flow of cost \(C\) round jointly to an integral high family and an
integral supported orientation of cost at most \(C\). The exact minimum
cost is also the minimum mass of an annular relay measure satisfying
(6.19+)--(6.19-); ordinary Hoffman cuts are precisely its zero-width
instances. In particular, feasible defect-bearing components of directed
height \(\ell_C\) have total cost at most
\(\sum_C\ell_C(p_C+h_C)\). Consequently, a
fixed-cost-amplification fractional corridor with constant \(L_A\), together
with

\[
\sum_{q\le\lceil A\sqrt m\rceil}
\frac{\mathfrak O_q(F_m)}{c_q}=o(W),
\]

constructs an integral adaptive history of weighted cost \(o(W)\).
Here the corridor is required after every balanced legal prefix, or along
one explicitly specified future-compatible integral strategy.
Because the depth-one audit forces every such \(F_m\) outside the
\((1/8-o(1))B\) row-distance basin of every coordinate relabelling of
MSW, this is a positive theorem specifically on the necessary
distant-factor branch.

No existence theorem for factors satisfying these entrance or annular
corridors is proved here. What is proved is that each of the displayed
cut, relay, and defect-basin conditions is sufficient, remains integral
inside the chosen exact factor, and requires no robust interior slack.

## 1. Cross-audit of the linear hole theorem

Assume \(m\ge3\). At depth one,

\[
N_1=\binom{2m+1}{m-1}=\frac m{m+2}W,\qquad
c_1=1,\qquad
\rho_1=\frac{2W}{m+2}.
\tag{1.1}
\]

Let

\[
\Gamma_m=(2m-3)\operatorname{Cat}_{m-2}.
\]

The audited marked-gap insertion theorem gives \(\Gamma_m\) collision
pairs with pairwise-disjoint pointed slots. Hence

\[
\Gamma_m
\le\sum_S\left\lfloor\frac{\mu_1(S)}2\right\rfloor
\le\sum_S(\mu_1(S)-1)_+.
\tag{1.2}
\]

If \(M_1\) is the number of holes, then

\[
\sum_S(\mu_1(S)-1)_+
=W-(N_1-M_1)=\rho_1+M_1.
\tag{1.3}
\]

Equations (1.2)--(1.3) prove

\[
M_1(F_m^{\rm MSW})
\ge[\Gamma_m-\rho_1]_+.
\tag{1.4}
\]

The factorial cancellation is exact:

\[
\frac{\Gamma_m}{W}
=\frac{m(m+1)}{4(2m-1)(2m+1)}.
\tag{1.5}
\]

A canonical row starts at most \(m-1\) marked patterns: two starts of
\(1100\) or \(1010\) cannot be consecutive among the \(2m-3\) possible
linear starts. Removing \(b\) canonical rows therefore leaves at least
\([\Gamma_m-(m-1)b]_+\) certificates. Since every hole costs one
stage-one toggle,

\[
\boxed{
T_1(F')
\ge[\Gamma_m-(m-1)b-\rho_1]_+.}
\tag{1.6}
\]

The exact finite rearrangement is

\[
\boxed{
b\ge
\left\lceil
\frac{\Gamma_m-\rho_1-T_1}{m-1}
\right\rceil}
\tag{1.7}
\]

whenever the numerator is positive. Dividing by
\(W=(2m+1)B\) gives the \(1/8\) radius and, for fixed
\(0<\varepsilon<1/8\),

\[
b\le(1/8-\varepsilon)B
\quad\Longrightarrow\quad
T_1\ge(\varepsilon/2-o(1))W.
\tag{1.8}
\]

All fixed-\(A\) window statements require \(m\) sufficiently large that
\(\lceil A\sqrt m\rceil\le m-1\).

## 2. Exact correction to depth-one star safety

For a \(t\)-set \(T\), put

\[
U_T=\left\{S\in\binom{[n]}{m-1}:T\subseteq S\right\},
\qquad u_t=|U_T|.
\]

At depth one a free balanced high family can put between

\[
0
\quad\text{and}\quad
\min\{u_t,\rho_1\}
\]

high cells in \(U_T\), because \(u_t\le N_1-\rho_1\) in the audited
ranges. If \(\iota(U_T)\) and \(\eta(U_T)\) are the internal and incident
owner-edge counts, the two extreme inequalities

\[
\iota(U_T)\le u_t+\min\{u_t,\rho_1\},
\qquad
\eta(U_T)\ge u_t
\tag{2.1}
\]

and \(\iota\le\eta\) imply that some integer high count makes this one
star safe. The calculations in the source report prove (2.1) for
\(t=1,2\), \(m\ge3\), and for \(t=3\), \(m\ge21\).

This is a per-star feasibility envelope. It does not say that an arbitrary
high family is safe or that the per-star choices are simultaneous. For
example, when \(m\ge6\), a high family of size \(\rho_1\) contained in one
point star \(U_x\) gives quota mass \((m+1)B\), while

\[
\eta(U_x)=mB,
\]

so its incident Hall row fails by \(B\).

For a literal exact endpoint, however, point regularity fixes

\[
\deg_H(x)=d_1=\frac{2(m-1)}{m+2}B.
\]

The exact point-star quantities are

\[
\iota(U_x)=(m-2)B,\qquad
u_1+d_1=(m-1)B,\qquad
\eta(U_x)=mB.
\tag{2.2}
\]

Thus every literal point star has exactly \(B\) raw slack on both Hall
sides. Literal singular cuts begin at pair order or at genuinely nonstar
families, not at point stars.

## 3. The complete arbitrary-cut corridor

Fix one stage and one actual earlier history. Let \(\mathcal V\) be the
set of \(N\) rank cells and let \(G\) be the resulting loopless labelled
owner multigraph with \(W=cN+\rho\) edges. Every owner edge has a
distinguished immutable canonical anchor, whose histogram is \(\mu\).

For \(U\subseteq\mathcal V\), write

\[
u=|U|,\qquad
\iota(U)=\#\{\text{edges internal to }U\},\qquad
\eta(U)=\#\{\text{edges incident with }U\}.
\]

Every internal edge has its anchor in \(U\), and every anchor in \(U\)
belongs to an incident edge. Therefore

\[
\boxed{\iota(U)\le\mu(U)\le\eta(U).}
\tag{3.1}
\]

A balanced orientation has load

\[
b(v)=c+\mathbf1_H(v),\qquad |H|=\rho.
\]

The complete free-high interval at \(U\) is

\[
\boxed{
L(U)=\max\{0,\rho-(N-u),\iota(U)-cu\},}
\tag{3.2}
\]

\[
\boxed{
R(U)=\min\{u,\rho,\eta(U)-cu\}.}
\tag{3.3}
\]

Every supported balanced orientation necessarily satisfies

\[
L(U)\le |H\cap U|\le R(U).
\tag{3.4}
\]

For a containment star, (3.2)--(3.3) specialize exactly to the corridor
in the audited N report:

\[
\iota(U_T)=M_{q+1}^F(T),
\]

\[
\eta(U_T)
=c_{q-1}M'+h_{q-1}(T)-\Sigma_q(T).
\]

Now decompose the immutable histogram as

\[
\mu=c\mathbf1+\mathbf1_{\mathcal A}+P-N^-,
\tag{3.5}
\]

where

\[
\mathcal A=\{v:\mu(v)\ge c+1\},\qquad
P(v)=(\mu(v)-c-1)_+,
\]

\[
N^-(v)=(c-\mu(v))_+,\qquad
p=\sum_vP(v),\qquad h=\sum_vN^-(v).
\tag{3.6}
\]

Summing (3.5) gives

\[
|\mathcal A|+p-h=\rho.
\tag{3.7}
\]

### Theorem 3.1 (arbitrary-cut defect domination)

For every \(U\subseteq\mathcal V\),

\[
\boxed{
(L(U)-|\mathcal A\cap U|)_+\le p,\qquad
(|\mathcal A\cap U|-R(U))_+\le h.}
\tag{3.8}
\]

More precisely, the internal term is bounded by \(P(U)\), the incident
term by \(N^-(U)\), and the two cardinality terms by
\((p-h)_+\) and \((h-p)_+\), respectively.

#### Proof

Put \(a=|\mathcal A\cap U|\). By (3.1) and (3.5),

\[
\iota(U)-cu-a
\le\mu(U)-cu-a
=P(U)-N^-(U)\le P(U).
\]

Also

\[
\rho-(N-u)-a
=|\mathcal A\setminus U|+p-h-(N-u)
\le p-h.
\]

These are every term in \(L(U)-a\). The upper side follows from

\[
a-(\eta(U)-cu)
\le a-(\mu(U)-cu)
=N^-(U)-P(U)\le N^-(U)
\]

and

\[
a-\rho\le|\mathcal A|-\rho=h-p.
\]

The remaining cardinality term \(a-u\) is nonpositive. \(\square\)

There is an exact four-regime version. The largest individually optimized
internal Hall deficit obeys

\[
\left[
\iota(U)-cu-\min\{u,\rho\}
\right]_+
\le
\begin{cases}
P(U),&u\le\rho,\\
N^-(\mathcal V\setminus U),&u\ge\rho,
\end{cases}
\tag{3.9}
\]

and the incident deficit obeys

\[
\left[
cu+\max\{0,\rho-(N-u)\}-\eta(U)
\right]_+
\le
\begin{cases}
N^-(U),&u\le N-\rho,\\
P(\mathcal V\setminus U),&u\ge N-\rho.
\end{cases}
\tag{3.10}
\]

For example, when \(u\ge\rho\),

\[
\mu(U)-cu-\rho
=c(N-u)-\mu(\mathcal V\setminus U)
\le N^-(\mathcal V\setminus U);
\]

the other three cases follow directly from (3.5). Hence the maximum
scalar nonstar Hall defect is no larger than

\[
\boxed{\mathfrak O=\max\{p,h\}.}
\tag{3.11}
\]

This domination is used positively below: the corridor needs only
transport or release of the already existing violation mass; it has no
additional macroscopic scalar demand.

## 4. All nonstar cuts form one integral orientation matroid

Make \(c\) mandatory clones and one optional clone of every
\(v\in\mathcal V\). Join a clone of \(v\) to the labelled owner edges
incident with \(v\). Let \(\mathsf T_G\) be the resulting transversal
matroid on the clones, let \(\mathcal C\) be the mandatory clones, and let
\(\mathcal O\) be the optional clones.

### Theorem 4.1 (orientation-high matroid)

Assume that the fixed stage graph \(G\) admits at least one balanced
supported orientation. Then \(\mathcal C\) is independent,

\[
\mathsf M_G=(\mathsf T_G/\mathcal C)|_{\mathcal O}
\]

has rank \(\rho\), and its bases are exactly the feasible high families
\(H\).

#### Proof

An orientation of \(G\) with indegrees \(c+\mathbf1_H\) matches each owner
edge to one clone of its head. Since the numbers of selected clones and
owner edges are both \(W\), this is a matching of
\(\mathcal C\cup H\) onto all owner edges.

Conversely, such a matching orients every owner edge toward the vertex of
its matched clone and gives the required indegrees. Thus feasible high
families are exactly the \(\rho\)-element sets whose optional clones,
together with \(\mathcal C\), are independent. Existence of one
orientation makes \(\mathcal C\) independent and gives contracted rank

\[
W-cN=\rho.
\]

This proves the theorem. \(\square\)

For fixed \(H\), clone Hall is

\[
c|U|+|H\cap U|\le\eta(U)\qquad(U\subseteq\mathcal V).
\]

Applying the same inequality to \(\mathcal V\setminus U\), and using

\[
\eta(\mathcal V\setminus U)=W-\iota(U),
\]

gives the internal inequality. Hence Theorem 4.1 incorporates every
crossing star and nonstar Hall row simultaneously, not merely the scalar
interval for one \(U\).

### Corollary 4.2 (a feasible high family close to the raw support)

Under the hypothesis of Theorem 4.1, there is a feasible high family
\(H\) such that

\[
\boxed{
\frac12\|\mu-(c\mathbf1+\mathbf1_H)\|_1
\le p+h\le2\mathfrak O.}
\tag{4.1}
\]

#### Proof

For each cell \(v\), choose \(\min\{c,\mu(v)\}\) mandatory clones and, if
\(v\in\mathcal A\), its optional clone. Match these clones to distinct
owner edges at their canonical anchors. This canonically matches

\[
(cN-h)+|\mathcal A|=W-p
\]

clones. Therefore

\[
\operatorname{rk}_{\mathsf M_G}(\mathcal A)\ge\rho-p.
\]

Choose an independent \(I\subseteq\mathcal A\) of size at least
\(\max\{0,\rho-p\}\), and extend \(I\) to a base \(H\). Equation (3.7)
then gives

\[
|\mathcal A\setminus H|\le h.
\]

The positive-support identity is

\[
\frac12\|\mu-(c\mathbf1+\mathbf1_H)\|_1
=p+|\mathcal A\setminus H|,
\]

which proves (4.1). \(\square\)

Without assuming feasibility, the same canonical partial matching proves
the exact rank-deficiency bounds

\[
\boxed{
cN-\operatorname{rk}_{\mathsf T_G}(\mathcal C)\le h,\qquad
W-\operatorname{rk}_{\mathsf T_G}(\mathcal C\cup\mathcal O)\le p.}
\tag{4.2}
\]

These are positive near-completion bounds, not a short-toggle theorem:
an augmenting path realizing the nearby base can still be long.

If every owner edge is labelled by its middle root \(X\) and each endpoint
is contained in \(X\), then every base of \(\mathsf M_G\) is also a base
of the shadow-quota matroid from the singular-boundary report. The
orientation matching itself is the required containment matching. Thus
the nonstar orientation matroid refines ordinary containment Hall
integrality. Literal point regularity and cyclic-row packaging remain
additional requirements.

## 5. Exact clipping and direct release

Let \(\Omega\) be the \(W\) labelled owners and let
\(a:\Omega\to\mathcal V\) be their canonical-anchor map. Fix an allowed
release relation

\[
\mathscr R\subseteq\Omega\times\mathcal V.
\]

For the adjacent-deletion model, \((X,v)\in\mathscr R\) means that \(v\)
is the actual alternate endpoint of the current owner edge. For a
rank-local common-owner release, it may instead mean \(v\subseteq X\).

### Theorem 5.1 (optimal direct-release theorem)

There is an explicit choice of

\[
R=\mathfrak O=\max\{p,h\}
\tag{5.1}
\]

owners and an \(R\)-element multiset \(\mathcal D\) of deficit slots such
that:

1. retaining every owner outside the released set at its canonical anchor
   leaves exactly the slots in \(\mathcal D\) unfilled in a balanced
   floor/ceiling histogram;
2. if the bipartite graph between the released owners and the slots
   \(\mathcal D\), using \(\mathscr R\), satisfies Hall, then an integral
   assignment changes exactly \(R\) owners and produces a balanced
   histogram;
3. no assignment can change fewer than \(R\) owners.

#### Construction and proof

First suppose \(p\ge h\). At every cell \(v\), release exactly

\[
P(v)=(\mu(v)-c-1)_+
\]

owners anchored there. This gives \(p\) released owners. Since

\[
|\mathcal A|=\rho-p+h,
\]

choose an arbitrary

\[
J\subseteq\mathcal V\setminus\mathcal A,
\qquad |J|=p-h,
\]

and put \(H=\mathcal A\cup J\). Let \(\mathcal D\) contain
\(N^-(v)\) copies of every \(v\), together with one additional copy of
each \(v\in J\). Its size is

\[
h+(p-h)=p.
\]

After the releases, every cell of \(\mathcal A\) has retained load
\(c+1\), while a cell below the floor has retained load
\(c-N^-(v)\). Filling \(\mathcal D\) therefore produces
\(c+\mathbf1_H\).

Now suppose \(h>p\). Release the \(P(v)\) upper-excess occurrences and
choose

\[
Q\subseteq\mathcal A,\qquad |Q|=h-p.
\]

At every \(v\in Q\), release one further owner after the \(P(v)\)
upper-excess owners have been selected. Put \(H=\mathcal A\setminus Q\).
There are \(h\) released owners, and let \(\mathcal D\) contain exactly
\(N^-(v)\) copies of every below-floor cell \(v\). Removing the extra
owner at a member of \(Q\) changes its retained load from \(c+1\) to
\(c\); filling the \(h\) mandatory deficit slots again gives
\(c+\mathbf1_H\).

In either case, Hall gives a matching of released owners to all deficit
slots. This is an integral common-owner reassignment with exactly
\(\mathfrak O\) changes. The balanced-histogram distance theorem gives
the matching lower bound \(\mathfrak O\), proving optimality. \(\square\)

The direct release Hall condition has the explicit form

\[
\boxed{
|\mathcal D(U)|
\le
\#\{X\text{ released}:\exists v\in U
\text{ with }(X,v)\in\mathscr R\}
\quad(U\subseteq\operatorname{supp}\mathcal D).}
\tag{5.2}
\]

Thus (5.2) is a positive, integral, no-amplification corridor. It is
stronger than the free-high scalar corridor: it controls the actual
released owners and actual deficit slots, rather than optimizing their
cardinalities separately.

For rank-local common-owner release, every edge of the matching in
Theorem 5.1 assigns an owner only to a cell contained in its same middle
root. Thus the theorem preserves exact middle ownership at that rank.
It does not by itself make the choices at different ranks nested or package
them into literal cyclic rows.

### Theorem 5.2 (exact coefficient-one cyclic-entrance cuts)

Now take \(\mathscr R\) to be the actual alternate-endpoint relation, and
let

\[
g(v,w)=\#\{e\in E(D):e=v\to w\}
\]

be its labelled arc multiplicity. Use the abbreviations

\[
g(I,w)=\sum_{v\in I}g(v,w),
\qquad
g(v,J)=\sum_{w\in J}g(v,w).
\]

There is a balanced supported orientation with exactly
\(\mathfrak O=\max(p,h)\) toggles if and only if the appropriate one of
the following two systems holds.

If \(p\ge h\), put

\[
E^+=\{v:P(v)>0\},
\qquad
T=\mathcal V\setminus\mathcal A.
\]

Then, for every \(I\subseteq E^+\) and \(J\subseteq T\), respectively,

\[
\boxed{
P(I)\le
\sum_{w\in T}\min\{N^-(w)+1,g(I,w)\},}
\tag{5.3}
\]

\[
\boxed{
N^-(J)\le
\sum_{v\in E^+}\min\{P(v),g(v,J)\}.}
\tag{5.4}
\]

If \(h>p\), put

\[
D^-=\{w:N^-(w)>0\}.
\]

Then, for every \(I\subseteq D^-\) and \(J\subseteq\mathcal A\),
respectively,

\[
\boxed{
N^-(I)\le
\sum_{v\in\mathcal A}\min\{P(v)+1,g(v,I)\},}
\tag{5.5}
\]

\[
\boxed{
P(J)\le
\sum_{w\in D^-}\min\{N^-(w),g(J,w)\}.}
\tag{5.6}
\]

Whenever these inequalities hold, all chosen arcs are literal current
owner sibling edges. Thus the optimum histogram cost \(\mathfrak O\) is
attained integrally inside the same exact middle factor.

#### Proof

For an arbitrary toggle set \(x\), write

\[
\operatorname{div}_x(v)
=\sum_{e\in\delta^+(v)}x_e-
  \sum_{e\in\delta^-(v)}x_e.
\]

If its terminal histogram is balanced, the exact histogram-distance
theorem gives

\[
|x|\ge
\sum_v(\operatorname{div}_x(v))_+
\ge\mathfrak O.
\tag{5.7}
\]

At equality, the first inequality is rigid: every selected arc has its
tail at a positive-divergence cell and its head at a negative-divergence
cell. Indeed, the sum of all selected outdegrees is \(|x|\), whereas the
sum of the positive divergences is obtained from it by subtracting every
selected arc leaving a nonpositive cell and every selected arc entering a
positive cell. Equality makes both subtracted quantities zero.

For any high family \(H\) of size \(\rho\), equal total mass gives the
exact identity

\[
\frac12\|\mu-(c\mathbf1+\mathbf1_H)\|_1
=p+|\mathcal A\setminus H|.
\tag{5.7a}
\]

Thus the descriptions of all closest high families in the two cases below
are forced, not merely sufficient choices.

Suppose first that \(p\ge h\). Every closest balanced histogram has high
family

\[
H=\mathcal A\cup J_0,
\qquad
J_0\subseteq T,\qquad |J_0|=p-h.
\]

Its positive divergences are exactly \(P(v)\) on \(E^+\). A cell
\(w\in T\) has negative divergence \(N^-(w)\), or
\(N^-(w)+1\) when \(w\in J_0\). Hence equality in (5.7) is equivalent to
selecting arcs from \(E^+\) to \(T\) with exact left degrees \(P(v)\)
and right degrees in the intervals

\[
N^-(w)\le d(w)\le N^-(w)+1.
\tag{5.8}
\]

The total degree is \(p\), so exactly \(p-h\) right vertices receive the
extra unit; these vertices are \(J_0\).

We use the following capacitated bipartite lemma. Let left vertex \(i\)
have exact degree \(r_i\), let right vertex \(j\) have degree in
\([\ell_j,u_j]\), and let edge \(ij\) have integral capacity \(g_{ij}\).
An integral \(b\)-matching exists if and only if, for all
\(I\subseteq L\), \(J\subseteq R\),

\[
r(I)\le u(J)+g(I,R\setminus J),
\tag{5.9}
\]

\[
\ell(J)\le r(I)+g(L\setminus I,J).
\tag{5.10}
\]

This is Hoffman's theorem applied to the circulation

\[
s\longrightarrow L\longrightarrow R\longrightarrow t
\longrightarrow s,
\]

with fixed capacities \(r_i\) on \(s\to i\), capacities \(g_{ij}\) on
\(i\to j\), intervals \([\ell_j,u_j]\) on \(j\to t\), and total return
flow \(\sum_ir_i\). The network matrix is totally unimodular, so
feasibility is integral.

For fixed \(I\), minimizing the right side of (5.9) over \(J\) gives

\[
\sum_{w\in R}\min\{u_w,g(I,w)\}.
\]

For fixed \(J\), minimizing the right side of (5.10) over \(I\) gives

\[
\sum_{v\in L}\min\{r_v,g(v,J)\}.
\]

With \(r=P\), \(\ell=N^-\), and \(u=N^-+1\), these are exactly
(5.3)--(5.4).

If \(h>p\), every closest balanced histogram instead has

\[
H=\mathcal A\setminus Q,
\qquad |Q|=h-p.
\]

Every target in \(D^-\) has exact demand \(N^-(w)\), while a source
\(v\in\mathcal A\) sends \(P(v)\), or \(P(v)+1\) when \(v\in Q\).
Apply the same lemma to the transposed bipartite graph, with exact left
degrees \(N^-\) and right intervals \([P,P+1]\). Its two minimized cut
families are (5.5)--(5.6). This proves necessity, sufficiency, and
integrality in both regimes. \(\square\)

For completeness, these cuts are literal cyclic-entrance counts. At stage
\(1\le q\le m-1\), the exact entry is

\[
g_q(I,J)=
\sum_{X\in\Omega}
\mathbf1\{L_q(X)\in I,\ 
L_{q+1}(X)\cup\{\kappa_q(X)\}\in J\},
\tag{5.11}
\]

where \(\kappa_q(X)\) is the carried deletion letter before the stage-
\(q\) decision. If a row is written cyclically as \(\rho\), put
\(I_\rho(j,s)=\{\rho_j,\ldots,\rho_{j+s-1}\}\). Under the phase convention
which renumbers that row's owners at the fixed stage \(q\) so that

\[
L_q(X_{\rho,j})=I_\rho(j,m-q),
\qquad
L_{q+1}(X_{\rho,j})=I_\rho(j,m-q-1),
\]

(5.11) becomes the explicit half-open interval count

\[
g_q(I,J)=
\sum_{\rho}\sum_{j\in\mathbb Z_n}
\mathbf1\{I_\rho(j,m-q)\in I,\ 
I_\rho(j,m-q-1)\cup\{\kappa_q(X_{\rho,j})\}\in J\}.
\tag{5.12}
\]

For \(q=1\), and ownerwise whenever the stage-\((q-1)\) decision was
no-toggle, \(\kappa_q(X)=a_q(X)\). In all cases (5.11) uses the actual
carried letter. Every unit selected by the cut theorem is therefore one
distinct, physically available sibling toggle, not a histogram-only
reassignment.

Each right side in (5.3)--(5.6) is a transversal-polymatroid rank
function: it is a sum of truncations of nonnegative modular incidence
counts, hence is monotone and submodular. Thus Theorem 5.2 is an explicit
submodular Hall test for coefficient-one repair, not an existential choice
of a released set or a high family.

## 6. Integral anchor-to-alternate flow

Orient every current owner edge from its canonical anchor to its alternate
endpoint. Denote this directed multigraph by \(D\). A toggle set has
indicator \(x_e\in\{0,1\}\), and its final load is

\[
b(v)=\mu(v)-\sum_{e\in\delta^+(v)}x_e
                 +\sum_{e\in\delta^-(v)}x_e.
\tag{6.1}
\]

Fix a high family \(H\) and put

\[
z_H(v)=\mu(v)-c-\mathbf1_H(v).
\tag{6.2}
\]

Then balancing is exactly the unit-capacity transshipment equation

\[
\sum_{e\in\delta^+(v)}x_e
-\sum_{e\in\delta^-(v)}x_e
=z_H(v).
\tag{6.3}
\]

### Theorem 6.1 (exact corridor-flow theorem)

For a fixed \(H\), the following are equivalent.

1. There is a supported balanced orientation with high family \(H\).
2. For every \(U\subseteq\mathcal V\),
   \[
   -\operatorname{out}_D(U)
   \le c|U|+|H\cap U|-\mu(U)
   \le\operatorname{in}_D(U).
   \tag{6.4}
   \]
3. The linear system (6.3), \(0\le x_e\le1\), has a fractional solution.
4. The same system has an integral solution.

Moreover, if a fractional solution has cost

\[
\sum_e x_e\le C,
\tag{6.5}
\]

then there is an integral solution of cost at most \(C\).

#### Proof

Summing (6.3) over \(U\) gives the two cut inequalities (6.4).
Conversely, (6.4) is exactly Hoffman's cut condition for the
unit-capacity transshipment (6.3), so it gives a fractional flow.
The node--arc incidence matrix is totally unimodular and all supplies and
capacities are integral. A minimum-cost feasible flow therefore has an
integral optimum. Taking the fractional solution as a cost upper bound
proves the final assertion. \(\square\)

The identities

\[
\operatorname{out}_D(U)=\mu(U)-\iota(U),
\qquad
\operatorname{in}_D(U)=\eta(U)-\mu(U)
\tag{6.6}
\]

show that (6.4) is exactly the internal/incident Hall corridor. Hence
Theorem 6.1 converts the necessary distant-factor corridor into a positive
integral flow theorem without any interior-slack assumption.

If \(\operatorname{in}_D(U)=0\), only the upper sign in (6.4) becomes
singular; if \(\operatorname{out}_D(U)=0\), only the lower sign does. The
exact equation

\[
|H\cap U|
=|\mathcal A\cap U|+P(U)-N^-(U)
\tag{6.7}
\]

is forced only when both directed boundaries vanish, equivalently when
\(U\) is a union of weak components. This is automatically handled by
the flow criterion; it need not be given artificial robust slack.

### Theorem 6.2 (joint fractional-high rounding)

Let \(y_v\in[0,1]\) be fractional high variables. Suppose

\[
\sum_{e\in\delta^+(v)}x_e
-\sum_{e\in\delta^-(v)}x_e+y_v
=\mu(v)-c,
\qquad 0\le x_e\le1,
\tag{6.8}
\]

has a fractional solution of cost

\[
\sum_e x_e\le C.
\tag{6.9}
\]

Then it has a solution with

\[
x_e\in\{0,1\},\qquad y_v\in\{0,1\},
\]

and cost at most \(C\). The set

\[
H=\{v:y_v=1\}
\]

has size \(\rho\), and the integral \(x\) is a supported balanced
orientation with high family \(H\).

#### Proof

Adjoin a sink \(t\) and, for every cell \(v\), a zero-cost arc
\(v\to t\) of capacity interval \([0,1]\). Give \(v\) supply
\(\mu(v)-c\), and give \(t\) demand

\[
\sum_v(\mu(v)-c)=W-cN=\rho.
\]

The owner arcs have capacity \([0,1]\) and cost one. Equation (6.8) is
exactly this min-cost flow. The network matrix is totally unimodular, so
an optimal flow for the integral supplies and capacities is integral and
has cost no larger than the stipulated fractional flow. The sink balance
gives \(\sum_vy_v=\rho\), and the cell balances give final load
\(c+y_v\). \(\square\)

Thus the high family itself does not have to be rounded separately. In
particular, the flexible-high corridor

\[
\boxed{
\iota(U)\le(c+1)|U|,
\qquad
\eta(U)\ge c|U|
\quad(U\subseteq\mathcal V)}
\tag{6.10}
\]

is sufficient as well as necessary for some integral balanced supported
orientation. The global edge count forces exactly \(\rho\) high cells.

Indeed, the incident inequalities are precisely Hall for the \(c\)
mandatory clones. The internal inequalities are Hall for matching all
\(W\) owner edges into the \(c+1\) clones per cell: an arbitrary owner
subfamily whose endpoint set is \(U\) has size at most \(\iota(U)\).
Thus the mandatory clones are independent and the full clone transversal
matroid has rank \(W\). Extend the mandatory set to a \(W\)-element base;
the \(\rho=W-cN\) optional clones in that base give the orientation.

The global high-cardinality terms are already encoded by complementary
instances of (6.10). Namely,

\[
\eta(\mathcal V\setminus U)\ge c(N-|U|)
\quad\Longrightarrow\quad
\iota(U)\le c|U|+\rho,
\]

while the internal inequality on \(\mathcal V\setminus U\) gives the
complementary strengthened incident lower bound. Combining these with the
two raw inequalities yields exactly the minimum and maximum cardinality
terms in (3.2)--(3.3).

At depth one, the incident half of (6.10) is equivalent to every
connected component of the owner graph containing a cycle. Indeed, a
whole component gives necessity. Conversely, every proper connected
component of an induced \(U\) has at least \(|C|-1\) internal edges and
at least one boundary edge. The internal half of (6.10) is the remaining
nonstar density condition.

### Definition 6.3 (fractional bounded-flow corridor)

For \(L\ge1\), say that a stage graph has the
\(L\)-bounded-flow corridor relative to \(\mu\) if there is a fractional
pair \((x,y)\) satisfying (6.8) with

\[
\sum_e x_e
\le L(p+h).
\tag{6.11}
\]

By Theorem 6.2, this condition jointly constructs an integral high family
and an integral supported orientation with

\[
\boxed{T\le L(p+h)\le2L\mathfrak O.}
\tag{6.12}
\]

The direct-release corridor of Theorem 5.1 is the no-amplification
special case: its matched moves have no neutral intermediate vertices and
give \(T=\mathfrak O\).

### Theorem 6.4 (exact potential dual for bounded transport)

Put

\[
r(v)=\mu(v)-c
\]

and, for a real potential \(\varphi:\mathcal V\to\mathbb R\), define

\[
\mathcal J_D(\varphi)
=
\sum_v r(v)\varphi(v)
-\sum_v(\varphi(v))_+
-\sum_{e=u\to v}
  (\varphi(u)-\varphi(v)-1)_+.
\tag{6.13}
\]

If the flexible corridor (6.10) is feasible, then its minimum fractional
toggle cost, and hence its minimum integral toggle cost, is exactly

\[
\boxed{
\mathcal T(D,\mu,c)
=\sup_{\varphi\in\mathbb R^{\mathcal V}}
  \mathcal J_D(\varphi).}
\tag{6.14}
\]

Consequently the \(L\)-bounded-flow corridor of Definition 6.3 is
equivalent to the explicit family of potential inequalities

\[
\boxed{
\mathcal J_D(\varphi)\le L(p+h)
\qquad(\varphi:\mathcal V\to\mathbb R).}
\tag{6.15}
\]

More sharply, if the right side of (6.15) is replaced by
\(L\mathfrak O\), then the integral orientation produced by Theorem 6.2
has at most \(L\mathfrak O\) toggles.

#### Proof

Minimize \(\sum_ex_e\) over (6.8). Attach the unrestricted multiplier
\(\varphi(v)\) to the equality at \(v\), in the sign
\(r-Bx-y=0\), where \(Bx\) is outflow minus inflow. The Lagrangian is

\[
\sum_vr(v)\varphi(v)
+\sum_{e=u\to v}
 x_e\bigl(1-\varphi(u)+\varphi(v)\bigr)
-\sum_vy_v\varphi(v).
\]

Minimizing separately over \(0\le x_e\le1\) and
\(0\le y_v\le1\) gives respectively

\[
-(\varphi(u)-\varphi(v)-1)_+,
\qquad
-(\varphi(v))_+.
\]

Thus the LP dual is exactly (6.14). Feasibility and boundedness give
strong duality. Theorem 6.2 identifies the common fractional optimum with
an integral optimum, proving all assertions. \(\square\)

This dual separates feasibility from transport length. For example,
\(\varphi=\mathbf1_U\) and \(\varphi=-\mathbf1_U\) recover the two raw
floor/ceiling displacement tests. For \(M\ge1\), the two choices
\(M\mathbf1_U\) and \(-M\mathbf1_U\) give

\[
M\bigl(\mu(U)-(c+1)|U|\bigr)
-(M-1)\operatorname{out}_D(U),
\tag{6.16}
\]

and

\[
M\bigl(c|U|-\mu(U)\bigr)
-(M-1)\operatorname{in}_D(U).
\tag{6.17}
\]

If either flexible cut in (6.10) fails, the corresponding expression is
unbounded as \(M\to\infty\). Once all cuts are feasible, multilevel
potentials measure the additional cost of moving violation mass through
neutral cells. Therefore (6.15), rather than independent scalar slack in
each cut, is the exact robust-transport condition needed in Theorem 7.1.

### Theorem 6.5 (exact annular relay-cut theorem)

For \(U\subseteq U'\subseteq\mathcal V\), put

\[
S(U,U')=U'\setminus U
\]

and let

\[
q_D(U,U')
=\#\{e=u\to v:u\in U,\ v\notin U'\},
\tag{6.18}
\]

counting labelled arc multiplicity. Consider nonnegative relay measures
\(\sigma:\mathcal V\to\mathbb R_{\ge0}\) satisfying, for every
\(U\subseteq U'\),

\[
\boxed{
r(U)-|U|-q_D(U,U')
\le\sigma(U'\setminus U),}
\tag{6.19+}
\]

\[
\boxed{
r(U)-\rho-q_D(U,U')
\le\sigma(U'\setminus U).}
\tag{6.19-}
\]

Then the minimum joint toggle cost in (6.8) is exactly

\[
\boxed{
\mathcal T(D,\mu,c)
=\min_\sigma\sigma(\mathcal V),}
\tag{6.20}
\]

where the minimum on the right is over (6.19+)--(6.19-). If one side is
infeasible, both sides are \(+\infty\). When finite, an integral optimal
relay measure exists.

#### Proof: a flow produces every annular inequality

Let \((x,y)\) satisfy (6.8), and set

\[
\sigma(v)=\sum_{e\in\delta^-(v)}x_e.
\tag{6.21}
\]

Then \(\sigma(\mathcal V)=\sum_ex_e\). Summing (6.8) over \(U\), and
using \(y(U)\le|U|\), gives

\[
r(U)-|U|\le x(U,\mathcal V\setminus U).
\]

Summing instead over \(\mathcal V\setminus U\), and using
\(r(\mathcal V)=\rho\) and \(y\ge0\), gives

\[
r(U)-\rho\le x(U,\mathcal V\setminus U).
\]

For either inequality split

\[
x(U,\mathcal V\setminus U)
=x(U,U'\setminus U)+x(U,\mathcal V\setminus U').
\]

The first term is at most \(\sigma(U'\setminus U)\), and unit capacities
bound the second by \(q_D(U,U')\). This proves (6.19+)--(6.19-) and hence

\[
\min_\sigma\sigma(\mathcal V)\le\mathcal T(D,\mu,c).
\tag{6.22}
\]

#### Proof: annular inequalities dominate every dual potential

The diagonal instances \(U'=U\), together with their complements, imply
the flexible cuts (6.10). Hence any feasible relay measure puts us in the
feasible case of Theorem 6.4.

Fix a real potential \(\varphi\), and for \(t\in\mathbb R\) put

\[
U_t=\{v:\varphi(v)\ge t\}.
\]

The elementary layer-cake identities

\[
\varphi(v)=
\int_{\mathbb R}
\left(\mathbf1_{\{\varphi(v)\ge t\}}
-\mathbf1_{\{0\ge t\}}\right)dt
\]

and

\[
(\varphi(u)-\varphi(v)-1)_+
=\int_{\mathbb R}
\mathbf1_{\{u\in U_t,\ v\notin U_{t-1}\}}dt
\]

turn (6.13) into the exact identity

\[
\mathcal J_D(\varphi)
=\int_{\mathbb R}
\left[
r(U_t)-\rho\mathbf1_{\{t\le0\}}
-|U_t|\mathbf1_{\{t>0\}}
-q_D(U_t,U_{t-1})
\right]dt.
\tag{6.23}
\]

Apply (6.19+) to \(U_t\subseteq U_{t-1}\) when \(t>0\), and apply
(6.19-) when \(t\le0\). This gives

\[
\mathcal J_D(\varphi)
\le
\int_{\mathbb R}
\sigma(U_{t-1}\setminus U_t)dt
=\sigma(\mathcal V),
\]

because each vertex \(v\) belongs to
\(U_{t-1}\setminus U_t\) for a set of \(t\)-values of measure exactly
one. Take the supremum over \(\varphi\) and use Theorem 6.4. Together with
(6.22), this proves (6.20). An integral minimum-cost flow exists by
Theorem 6.2; its incoming-load measure (6.21) is integral and attains the
same value, proving the final assertion. \(\square\)

The diagonal case \(U'=U\) has no relay shell. Equation (6.19+) becomes

\[
\iota(U)\le(c+1)|U|,
\]

and (6.19-), applied also to complements, becomes

\[
\eta(U)\ge c|U|.
\]

Thus the ordinary necessary distant-factor corridor is exactly the
zero-width part of the annular system. Positive-width shells quantify,
without approximation, the cost of neutral cascades between those cuts.

### Corollary 6.6 (overload-charged annular corridor)

Let

\[
\omega(v)=P(v)+N^-(v).
\]

If, for some \(L<\infty\), every \(U\subseteq U'\) satisfies both

\[
r(U)-|U|-q_D(U,U')
\le L\omega(U'\setminus U)
\tag{6.24+}
\]

and

\[
r(U)-\rho-q_D(U,U')
\le L\omega(U'\setminus U),
\tag{6.24-}
\]

then there is an integral balanced supported orientation with

\[
\boxed{
T\le L(p+h)\le2L\mathfrak O.}
\tag{6.25}
\]

Indeed, take \(\sigma=L\omega\) in Theorem 6.5. This is a genuine cut
criterion: its diagonal instances impose feasibility, and its proper
annuli pay explicitly for relay depth.

### Theorem 6.7 (defect-component-height corridor)

Assume the flexible cuts (6.10). For a weak component \(C\) of \(D\),
put

\[
p_C=P(C),\qquad h_C=N^-(C),
\]

and let \(\ell_C\) be the maximum number of arcs in a simple directed path
of \(D[C]\). Then

\[
\boxed{
\mathcal T(D,\mu,c)
\le
\sum_C\ell_C(p_C+h_C).}
\tag{6.26}
\]

There is also the independent basin-volume bound

\[
\boxed{
\mathcal T(D,\mu,c)
\le
\sum_{C:p_C+h_C>0}|E(C)|.}
\tag{6.27}
\]

Both estimates are componentwise, so they combine to the sharper bound

\[
\mathcal T(D,\mu,c)
\le
\sum_C
\min\left\{
\ell_C(p_C+h_C),
\mathbf1_{\{p_C+h_C>0\}}|E(C)|
\right\}.
\tag{6.27a}
\]

Consequently, the \(L\)-bounded-flow corridor follows automatically if

\[
\sum_C\ell_C(p_C+h_C)\le L(p+h).
\tag{6.28}
\]

In particular, one may take \(L=s-1\) when every defect-bearing weak
component has at most \(s\) vertices. Components of arbitrary size with
\(p_C=h_C=0\) cost nothing.

#### Proof

The flexible cuts restricted to \(C\) give a balanced supported
orientation on that component, with forced local high count

\[
\rho_C=|E(C)|-c|C|\in[0,|C|].
\]

This includes the boundary cases \(\rho_C=0\) and \(\rho_C=|C|\), where
all local cells are respectively low or high. In the first case
\(H_C=\varnothing\) is forced and the half-\(\ell^1\) distance is \(h_C\);
in the second case \(H_C=C\) is forced and that distance is \(p_C\).
For \(0<\rho_C<|C|\), apply Corollary 4.2 componentwise. Thus in every
case there is a feasible high family \(H_C\) with

\[
\frac12
\|\mu_C-(c\mathbf1+\mathbf1_{H_C})\|_1
\le p_C+h_C.
\]

Take a corresponding integral toggle flow and delete directed cycles from
its selected support. This preserves every divergence and can only lower
the cost. The remaining acyclic integral flow decomposes into exactly its
total positive divergence many edge-disjoint directed source--sink paths.
Their number is the displayed half-\(\ell^1\) distance, and every path in
\(C\) has at most \(\ell_C\) arcs. This proves the component contribution
in (6.26), and components sum independently.

If \(p_C=h_C=0\), the anchor orientation itself already has loads in
\(\{c,c+1\}\), so it costs zero. On every other feasible component, any
supported orientation toggles at most all \(|E(C)|\) owner arcs. This gives
(6.27). Choosing the better construction independently in each component
gives (6.27a). \(\square\)

## 7. Positive fixed-window theorem on the distant branch

For an exact factor \(F_m\), let

\[
K_A=\lceil A\sqrt m\rceil
\]

and, from its immutable depth-\(q\) anchor histogram, define

\[
p_q=\sum_S(\mu_q(S)-c_q-1)_+,\qquad
h_q=\sum_S(c_q-\mu_q(S))_+,
\]

\[
\mathfrak O_q=\max\{p_q,h_q\}.
\tag{7.1}
\]

### Theorem 7.1 (bounded-corridor adaptive flow)

Fix \(A>0\) and a constant \(L_A<\infty\), independent of \(m\).
Suppose a sequence of exact factors \(F_m\) has:

1. mobile two-sided overload
   \[
   \Phi_A(F_m)
   :=\sum_{q=1}^{K_A}\frac{\mathfrak O_q}{c_q}
   =o(W);
   \tag{7.2}
   \]
2. the following robust corridor property: after every balanced legal
   prefix history through stage \(q-1\), the
   resulting stage-\(q\) owner digraph has the
   \(L_A\)-bounded-flow corridor of Definition 6.3.

Then there is an integral one-pass adjacent-deletion history through
\(K_A\) with

\[
\boxed{
\sum_{q=1}^{K_A}\frac{T_q}{c_q}
\le
2L_A\Phi_A(F_m)
=o(W).}
\tag{7.3}
\]

Every owner remains inside the same chosen exact middle factor throughout.

#### Proof

Proceed inductively. The history before stage one is empty. At stage
\(q\), apply the robust corridor hypothesis to the actual graph produced
by the earlier integral choices. Theorem 6.2 jointly replaces the
stipulated fractional high variables and fractional flow by an integral
high family and an integral toggle set of size

\[
T_q\le L_A(p_q+h_q)\le2L_A\mathfrak O_q.
\]

Orient those owner edges accordingly. This gives the next balanced state
and hence a legal prefix for the next induction step. Sum the displayed
bound with weights \(1/c_q\) to obtain (7.3). \(\square\)

The robust hypothesis can be weakened to one recursively future-compatible
strategy: at each reached graph the strategy specifies an integral
orientation with the stated cost bound, and the successor graph is again
certified. The stronger version is convenient because it is
history-independent.

### Corollary 7.2 (direct-release, coefficient one at the repair scale)

Under (7.2), suppose that at every reached stage the actual cyclic-entrance
multiplicities satisfy (5.3)--(5.4) when \(p_q\ge h_q\), and satisfy
(5.5)--(5.6) when \(h_q>p_q\). Then an integral adaptive history exists
with the sharper bound

\[
\boxed{
\sum_{q=1}^{K_A}\frac{T_q}{c_q}
=
\sum_{q=1}^{K_A}\frac{\mathfrak O_q}{c_q}
=o(W).}
\tag{7.4}
\]

Here “every reached stage” means either every balanced legal prefix
(the robust form), or the prefixes of one explicitly future-compatible
policy which selects one of the coefficient-one solutions supplied by
Theorem 5.2.

#### Proof

Theorem 5.2 toggles exactly the \(\mathfrak O_q\) selected owner edges and
reaches a clipped balanced histogram, without requiring a prior choice of
the released copies or of \(J\) or \(Q\). Iterate as in Theorem 7.1.
The histogram lower bound gives equality in (7.4). \(\square\)

Corollary 7.2 is an integral common-owner statement for the
adjacent-deletion
architecture: a matched owner uses its actual alternate child, and every
unmatched owner retains its canonical child. Thus the construction, not
merely the histogram, is integral inside one exact middle factor. It does
not assert that the resulting lower flags form a second cyclic wreath
factor.

Within the established AO/SDH implication used by the constant-one
program, Theorem 7.1 for every fixed \(A\), followed by the standard
diagonalization, supplies the required \(o(W)\) fixed-window loss. No
labelled-to-unlabelled reversal is used.

### Corollary 7.3 (the constructed factors are distant from the MSW orbit)

Every sequence satisfying (7.2) obeys

\[
\min_{\sigma\in S_n}
\operatorname{dist}_{\rm row}(F_m,\sigma F_m^{\rm MSW})
\ge(1/8-o(1))B.
\tag{7.5}
\]

#### Proof

At depth one, \(c_1=1\), so

\[
\mathfrak O_1\ge h_1=M_1(F_m).
\]

Equation (7.2) gives \(M_1(F_m)=o(W)\). The underlying audited stability
inequality

\[
M_1(F_m)\ge
[\Gamma_m-(m-1)b-\rho_1]_+
\]

applies after every coordinate relabelling, with the same constants. Apply
it to \(\sigma^{-1}F_m\) for each \(\sigma\in S_n\). The error term is
uniform in \(\sigma\), because the bound depends only on \(m\) and the row
distance. This gives (7.5). \(\square\)

Thus the positive theorem does not compete with the MSW obstruction; it
lies on the branch necessary for this exact-factor AO route.

### Theorem 7.4 (adaptive annular-relay theorem)

Fix \(A>0\), put \(K_A=\lceil A\sqrt m\rceil\), and let
\(S_{m,q}\ge0\) be deterministic budgets. Suppose that after every
balanced legal prefix through stage \(q-1\), the actual stage-
\(q\) owner digraph has a relay measure satisfying
(6.19+)--(6.19-) with total mass at most \(S_{m,q}\). Then there is an
integral one-pass history with

\[
\boxed{
\sum_{q=1}^{K_A}\frac{T_q}{c_q}
\le
\sum_{q=1}^{K_A}\frac{S_{m,q}}{c_q}.}
\tag{7.6}
\]

In particular, the exact positive fixed-window recourse conclusion follows
whenever the right side is \(o(W)\). The robust all-prefix hypothesis may
again be replaced by one explicitly future-compatible policy which, at
each reached graph, chooses an integral orientation of cost at most its
relay mass and recursively reaches the next certified graph. The total
weighted relay mass along that policy must be \(o(W)\).

#### Proof

At the reached stage \(q\), Theorem 6.5 converts the relay measure into an
integral high family and an integral set of at most \(S_{m,q}\) actual
owner toggles. This creates the next balanced legal prefix. Induction gives
the whole history, and summation gives (7.6). \(\square\)

### Corollary 7.5 (defect-local basins suffice)

For every stage graph \(G\), let

\[
S_q^{\rm basin}
=
\sum_C
\min\left\{
\ell_{q,C}(p_{q,C}+h_{q,C}),
\mathbf1_{\{p_{q,C}+h_{q,C}>0\}}|E(C)|
\right\}.
\tag{7.7}
\]

Either of the following hypotheses suffices.

1. There are deterministic bounds \(\overline S_{m,q}\) such that every
   graph after a balanced legal prefix satisfies the flexible cuts and
   \(S_q^{\rm basin}(G)\le\overline S_{m,q}\), with
   \[
   \sum_{q=1}^{K_A}\frac{\overline S_{m,q}}{c_q}=o(W).
   \tag{7.8}
   \]
2. There is a recursively future-compatible policy which chooses in each
   component one of the two orientations used in (6.27a), reaches another
   certified graph, and whose actual reached graphs satisfy
   \[
   \sum_{q=1}^{K_A}
   \frac{S_q^{\rm basin}(G_q)}{c_q}=o(W).
   \tag{7.9}
   \]

Then an integral one-pass history of weighted cost \(o(W)\) exists inside
the same exact factor.

Indeed, Theorem 6.7 supplies the stage budget in (7.7), and the induction
is the same as in Theorem 7.4. The component choices unite without a quota
error because every component has its forced local high count \(\rho_C\),
and \(\sum_C\rho_C=\rho\). This is a positive regime not requiring a
uniform bound on the sizes of defect-free components.

## 8. Scalar bounded-star margins available to the corridor

The bounded-order star calculation can be strengthened from mere safety
to an exact margin census. At depth one, fix a \(t\)-set \(T\), and for a
factor row \(\pi\) let

\[
a_\pi(T)=\#\{\text{middle windows of }\pi\text{ containing }T\},
\]

\[
z_T=\#\{\pi:a_\pi(T)\ge1\},\qquad
k_T=\#\{\pi:a_\pi(T)\ge2\}.
\]

Put

\[
L=m-t+1,\qquad
A_t=\binom{n-t}{m-t},\qquad
\sigma_T=\Sigma_1(T).
\]

Exact row-span truncation gives

\[
\sum_\pi a_\pi(T)=A_t,
\]

\[
M_1^F(T)=A_t-z_T,\qquad
M_2^F(T)=A_t-z_T-k_T.
\tag{8.1}
\]

Therefore the anchor-matching high count

\[
h_T^*=M_1^F(T)-|U_T|
\]

has exact lower and upper Hall margins

\[
\boxed{k_T,\qquad z_T-\sigma_T.}
\tag{8.2}
\]

Every row contributes at most one to \(\sigma_T\), so the margins in
(8.2) are nonnegative whenever \(h_T^*\) is cardinal-admissible.
Furthermore, for \(1\le t\le m-1\),

\[
\boxed{
k_T\ge
\left\lceil\frac{(A_t-B)_+}{L-1}\right\rceil.}
\tag{8.3}
\]

For \(2\le t\le m-1\),

\[
\sum_{|T|=t}\sigma_T
=W\binom{m-2}{t-2}.
\tag{8.4}
\]

If \(s_t\) is the number of upper-singular stars
\(z_T=\sigma_T\), then \(z_T\ge A_t/L\) and (8.4) imply

\[
\boxed{
s_t\le
(m-t+1)\binom{m-2}{t-2}\frac{(n)_t}{(m)_t},}
\tag{8.5}
\]

or equivalently

\[
\boxed{
\frac{s_t}{\binom nt}
\le
\frac{t(t-1)(m-t+1)}{m(m-1)}
=O_t(1/m).}
\tag{8.6}
\]

For pairs, at most \(2n\) stars are singular, and at most \(4n\) have
upper margin at most \(B/4\). Every other pair star has a positive-density
upper corridor, while (8.3) gives

\[
k_T\ge
\left\lceil\frac{(m-3)B}{2(m-2)}\right\rceil.
\tag{8.7}
\]

Indeed, for pairs \(A_2/L=B/2\), so
\(z_T-\sigma_T\le B/4\) implies \(\sigma_T\ge B/4\). Since

\[
\sum_{|T|=2}\sigma_T=W=nB,
\]

there are at most \(4n\) such pairs.

Thus point stars have robust literal slack, and among
cardinal-admissible anchor-matching scalar pair quotas the low upper-margin
exceptions are sparse, uniformly even for factors arbitrarily far from
MSW. This does not construct one high family realizing all the scalar
moments. For \(t\ge4\), \(h_T^*\) need not be cardinal-admissible.
The fractional high family in Theorem 6.2 is not point-regular, so even
point-star safety remains part of the joint AO flow certificate.
Verification of Theorem 7.1 requires simultaneous crossing-cut control,
including point stars, the exceptional pair stars, growing-order
families, and genuinely nonstar directed cuts.

## 9. Compatibility with singular-boundary caps

Let \(M(U)\) be an occurrence cap valid for a class of exact endpoint
factors which contains the old factor \(F\), and write

\[
M(U)=c|U|+\kappa(U).
\]

Since \(F\) itself obeys the cap,

\[
\mu_F(U)\le M(U).
\]

Using (3.5), with \(a=|\mathcal A\cap U|\), gives

\[
a+P(U)-N^-(U)\le\kappa(U).
\]

Therefore the excess-plus-high-slot demand from the singular-boundary
report satisfies

\[
\boxed{
\delta(U)
=P(U)+(a-\kappa(U))_+
\le\max\{P(U),N^-(U)\}.}
\tag{9.1}
\]

This applies in particular to owner-containment caps and to the exact
cyclic row-span caps, because the old exact factor belongs to both cap
classes. Thus those cuts localize which owners must be released, but their
amount is already normalized by the same two-sided violation mass used in
Theorems 5.1 and 7.1.

For nonnegative tests \((U_i,\lambda_i)\), if

\[
\Lambda=\max_v\sum_{i:v\in U_i}\lambda_i,
\]

then

\[
\boxed{
\sum_i\lambda_i\delta(U_i)
\le\Lambda(p+h)
\le2\Lambda\mathfrak O.}
\tag{9.2}
\]

For the four-regime complement form of Section 3, congestion must be
measured on the actual witness \(U_i\) or \(\mathcal V\setminus U_i\)
selected by that regime. Equations (9.1)--(9.2) are positive
compatibility estimates: bounded-congestion cyclic and nonstar cuts do not
inflate the release budget beyond a fixed multiple.

The cap class must contain the old factor. A release-dependent endpoint
cap which deliberately excludes \(F\) is not covered by (9.1).

## 10. Proved and conditional boundary

### Proved

1. The \(1/16\) marked-gap constant, the \(1/8\) row-distance radius, and
   the \(\varepsilon/2\) interior-basin cost are exact.
2. The bounded-order depth-one star theorem is valid per star with a free
   high count; literal point stars have exact \(B\)-scale Hall slack.
3. Every arbitrary star/nonstar scalar corridor defect is bounded by the
   old two-sided violation mass.
4. For one fixed stage graph, all nonstar Hall cuts form one contracted
   transversal matroid. Feasible high families are its bases.
5. The clipping construction releases exactly
   \(\mathfrak O=\max(p,h)\) owners. Direct owner-to-deficit Hall produces
   an integral balanced reassignment with the optimal number of changes.
   The four cyclic-entrance cut families (5.3)--(5.6) are necessary and
   sufficient for attaining that optimum on actual sibling edges.
6. The complete directed corridor is necessary and sufficient for an
   integral anchor-to-alternate transshipment. Fractional high variables
   and fractional owner flow round jointly with no cost loss. Equation
   (6.15) is an exact potential-dual characterization of constant-cost
   amplification.
7. The annular inequalities (6.19+)--(6.19-) exactly characterize minimum
   toggle cost by relay mass. The defect-component-height and basin-volume
   estimates (6.26)--(6.27) are concrete positive sufficient regimes.
8. A fixed \(L_A\)-bounded-flow corridor plus \(\Phi_A=o(W)\) constructs
   an integral adaptive history of cost \(o(W)\) inside the labelled owner
   system of one exact factor. More generally, weighted annular relay mass
   \(o(W)\) suffices directly. The direct-release version attains stage
   cost exactly \(\mathfrak O_q\).
9. Every factor sequence entering this positive theorem is automatically
   at row distance at least \((1/8-o(1))B\) from the entire coordinate-
   relabelling orbit of MSW.

### Still conditional

The report does not construct a sequence of exact factors satisfying both
\(\Phi_A=o(W)\) and any one of the coefficient-one entrance, bounded
annular-relay, or defect-basin hypotheses at every reached graph. That is
now a positive factor-selection target, not an unresolved rounding step:
once an annular relay certificate is supplied, Theorems 6.5 and 7.4 make
the history integral with no extra cost.

The adaptive adjacent-deletion theorems already produce nested
cross-depth owner paths. To obtain a second literal exact endpoint wreath
factor, one must additionally impose point-regular high families and cyclic
row packaging. If one invokes only the rank-local containment version of
Theorem 5.1, then cross-depth nesting is also absent.

The precise constant-one construction target left by this report is:

> for every fixed \(A\), choose exact-factor sequences on the necessary
> distant branch, allowed to depend on \(A\), with mobile two-sided
> overload \(o(W)\), and prove either the coefficient-one cyclic-entrance
> cuts, annular relay mass \(o(W)\) after weighting, or the defect-basin
> estimate along every reached sibling graph; an explicit future-compatible
> strategy suffices in place of the robust all-prefix form.

That statement is sufficient, quantitatively constant-preserving, and
gives an integral labelled AO history after Theorems 6.2 and 6.5. It does not
construct a second exact endpoint wreath factor; the constant-one
conclusion still uses the separately audited AO/SDH implication.

## 11. Independent audit of the decisive positive step

The new flow package was audited independently in three pieces after all
corrections above were incorporated.

1. The coefficient-one audit verified equality rigidity, both closest-high
   classifications, the capacitated interval \(b\)-matching lemma, all four
   minimized cut families (5.3)--(5.6), the ownerwise carry indexing in
   (5.11)--(5.12), and the robust/future-compatible quantifier in
   Corollary 7.2.
2. The min-cost audit verified the signs in (6.13), strong duality, the
   two indicator-potential formulas (6.16)--(6.17), both annular signs,
   the real-threshold layer-cake identity (6.23), equality of flow and relay
   minima, and existence of an integral optimal relay measure.
3. The component/adaptive audit verified the local boundary cases
   \(\rho_C=0,|C|\), directed-cycle deletion, edge-disjoint path
   decomposition, the componentwise minimum (6.27a), the noncircular
   quantifiers in Theorem 7.4 and Corollary 7.5, and the uniform
   relabelled-MSW deduction in Corollary 7.3.

No mathematical correction remains in those steps. The exact positive
composition proved here is therefore:

\[
\boxed{
\begin{array}{c}
\text{coefficient-one entrance cuts plus }\Phi_A=o(W),\quad\text{or}\\
\text{weighted annular relay mass }o(W),\quad\text{or}\\
\text{flexible cuts plus weighted defect-basin mass }o(W)
\end{array}
\Longrightarrow
\text{integral common-owner AO cost }o(W).}
\]

This holds for every fixed \(A\), with the exact factor and constants
allowed to depend on \(A\). Every such factor sequence is necessarily on
the branch at row distance at least \((1/8-o(1))B\) from the entire MSW
orbit. The remaining antecedent is positive exact-factor selection together
with one of the displayed robust or recursively future-compatible corridor
certificates; conditional on that certificate, the release/flow and
integral-rounding gates are closed by the theorems above.
