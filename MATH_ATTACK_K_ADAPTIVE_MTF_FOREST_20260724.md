# Line K: adaptive-MTF Johnson forests

## Outcome

Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

The Gaussian statement \(\mathrm{AD}_A\), with
\(H=\lceil A\sqrt m\rceil\), is still open.  The attack nevertheless gives
four theorem-level advances.

1.  A cyclic Johnson strip can be cut and fused by the canonical adaptive
    MTF construction with **no cut-induced deep-support loss**.  The terminal
    dummies and the initial residual queue recover all cyclic lower and upper
    flags, including those crossing the cut.

2.  Combining this closure with the audited quantitative strip matching
    proves the adaptive-MTF forest statement for every

    \[
    H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
    \]

    An explicit version is

    \[
    H=\left\lfloor
       \sqrt{\frac{\log m}{64\omega(m)\log\log m}}
       \right\rfloor,
    \qquad
    \omega(m)\longrightarrow\infty,
    \quad
    \omega(m)=o\!\left(\frac{\log m}{\log\log m}\right).
    \]

    This improves the independently-cut strip scale from a cube root to a
    square root of the logarithmic window.

3.  At Gaussian depth, cutting an exact odd wreath factor already solves the
    component count, all short-run constraints, all MTF boundary choices, and
    one of the two first-shadow partitions.  Within this odd-cut architecture,
    the entire remaining problem is a joint support condition for explicit
    cyclic interval maps.

4.  There is a stronger, very compact sufficient lemma.  A symmetric
    hypergraph of decorated complementary geodesics has an exact fractional
    matching which saturates the middle layer and has aggregate deterministic
    floor loss only \(O_A(W/\sqrt m)\).  It is enough to round it to an
    integral matching leaving

    \[
    L=o(W/H)
    \]

    middle vertices.  This is the sharpened Gaussian missing theorem.  A
    generic \((1-o(1))\)-near-perfect matching is not strong enough.

There are also exact deterministic improvements to the run-reset ledger.  If
\(\tau_H\) is the interval-transversal number of the short positive runs,
then the explicit reset/component term involving \(\rho_H\) can be replaced
by one involving \(\tau_H\), with the deep supports recomputed for the same
new cut set; one always has

\[
\frac{\rho_H}{H+1}\le \tau_H\le\rho_H,
\]

and both the factor \(H+1\) and the factor two needed to preserve every cut
edge colour are sharp.

The independent proof audits found no defect in the cyclic-boundary theorem,
the strip degree/codegree calculation, the matching parameters, the
\(U\)-ledger, the interval-transversal theorem, or the certified-slot
normalization.  Exact implication scopes and the remaining gaps are recorded
below.

---

## 1. Canonical MTF notation

Let an oriented Johnson path be

\[
T_0,T_1,\ldots,T_r,
\qquad
T_{i+1}=T_i-\{p_i\}+\{q_i\}.
\tag{1.1}
\]

After choosing \(H\) terminal dummy departures, define

\[
P^-_{i,q}
=T_i\setminus\{p_i,p_{i+1},\ldots,p_{i+q-1}\}.
\tag{1.2}
\]

Let \(\Theta_i\) be the ordered complement queue in the canonical MTF
state.  It starts with exactly \(H\) singleton blocks and one nonempty
residual block, and evolves by

\[
\Theta_{i+1}=(\{p_i\},\Theta_i\setminus\{q_i\}).
\tag{1.3}
\]

The upper flag is

\[
P^+_{i,q}
=T_i\cup\{\hbox{the first \(q\) singleton markers of \(\Theta_i\)}\}.
\tag{1.4}
\]

At depth one, the actual edge colours are

\[
P^-_{i,1}=T_i\cap T_{i+1},
\qquad
P^+_{i+1,1}=T_i\cup T_{i+1}.
\tag{1.5}
\]

An internal positive run is short if a coordinate enters and then exits at
most \(H\) transitions later.  Once all such runs have been cut, the audited
adaptive-MTF theorem gives a literal component word of length

\[
\#\{\hbox{middle vertices}\}+2H+1
\tag{1.6}
\]

per component, and the forest-level upper bound is

\[
W+(2H+1)C+2(N_1-e)
+\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+),
\tag{1.7}
\]

where \(C\) is the post-cut component count.  All support counts below refer
to these common canonical flags, not to independently optimized depthwise
choices.

---

## 2. Exact virtual cyclic closure

The ordinary erosion analysis loses \(q\) lower and \(q\) upper windows when
a cyclic strip is cut.  The adaptive MTF state does not have to lose them.

### Theorem 2.1 (cyclic-boundary MTF closure)

Let

\[
T_i=C\cup I_\gamma(i,\ell),
\qquad i\in\mathbb Z_{2\ell},
\tag{2.1}
\]

where \(\gamma=(z_0,z_1,\ldots,z_{2\ell-1})\) is a cyclic order,
\(I_\gamma(i,a)\) is its cyclic interval of length \(a\), and
\(|C|=m-\ell\).  Assume

\[
H<\ell<m.
\tag{2.2}
\]

Cut the cycle edge \(T_{2\ell-1}T_0\).  There are compatible terminal
dummies and an initial residual order for which, for every
\(0\le i<2\ell\) and \(1\le q\le H\),

\[
\boxed{
P^-_{i,q}=C\cup I_\gamma(i+q,\ell-q)
}
\tag{2.3}
\]

and

\[
\boxed{
P^+_{i,q}=C\cup I_\gamma(i-q,\ell+q).
}
\tag{2.4}
\]

Thus the cut path exposes all \(2\ell\) cyclic labels in every signed depth
\(q\le H\).  There is no boundary support loss.

### Proof

The cyclic transition is

\[
p_i=z_i,\qquad q_i=z_{i+\ell},
\tag{2.5}
\]

with indices modulo \(2\ell\).  Extend the departure sequence at the right
boundary by

\[
p_{2\ell-1+r}=z_{2\ell-1+r\pmod {2\ell}},
\qquad 0\le r<H.
\tag{2.6}
\]

Thus the dummy list is

\[
z_{2\ell-1},z_0,z_1,\ldots,z_{H-2}.
\]

All these coordinates are distinct and present whenever they are needed,
because a coordinate remains present for exactly \(\ell\) cyclic steps and
\(H<\ell\).

Initialize

\[
\Theta_0=
(\{z_{2\ell-1}\},\{z_{2\ell-2}\},\ldots,
  \{z_{2\ell-H}\},R_0),
\tag{2.7}
\]

where

\[
R_0=([2m]\setminus T_0)
\setminus\{z_{2\ell-1},\ldots,z_{2\ell-H}\}.
\]

The residual is nonempty because it has size \(m-H\).  The arrival
\(q_i=z_{i+\ell}\) is never one of the last \(H\) departures, again because
\(H<\ell\).  Induction in the update (1.3) therefore shows that the first
\(q\) markers of \(\Theta_i\) are

\[
z_{i-1},z_{i-2},\ldots,z_{i-q}.
\tag{2.8}
\]

Consequently

\[
\begin{aligned}
P^-_{i,q}
&=T_i\setminus\{z_i,\ldots,z_{i+q-1}\}\\
&=C\cup I_\gamma(i+q,\ell-q),
\end{aligned}
\]

and

\[
\begin{aligned}
P^+_{i,q}
&=T_i\cup\{z_{i-1},\ldots,z_{i-q}\}\\
&=C\cup I_\gamma(i-q,\ell+q).
\end{aligned}
\]

These are precisely all cyclic lower and upper strip rows.  Notice that the
upper window is backward-indexed: it ends at \(T_i\).  This is only an index
shift and does not change the row as \(i\) ranges cyclically.  Finally, every
cyclic positive run has length \(\ell>H\); after one cut it is either still a
long internal run or is split into two boundary runs.  Hence the canonical
MTF recurrence is legal.  \(\square\)

### General form

The same proof applies to a cyclic Johnson walk whenever transition supports
\(\{p_i,q_i\}\) at nonzero cyclic distance at most \(H\) are disjoint.  That
hypothesis enforces both long positive runs and long zero-runs.  The latter is
stronger than MTF legality alone, but it is exactly what identifies the
adaptive upper flags with ordinary cyclic unions.  The strip satisfies it
because two transition supports meet only at cyclic distance \(\ell\).

---

## 3. A deterministic growing-depth theorem

### 3.1 The full strip hypergraph

Choose disjoint cores \(C,D\subset[2m]\), each of size \(m-\ell\), and an
undirected cyclic order \(\gamma\) on the remaining \(2\ell\) coordinates.
Assume here that \(\ell-H\ge2\), as is automatic for the parameters below.
The full strip is

\[
\mathcal E(C,D,\gamma)=
\{C\cup I_\gamma(t,\ell+d):
  -H\le d\le H,\ t\in\mathbb Z_{2\ell}\}.
\tag{3.1}
\]

Let \(\mathcal G(m,H,\ell)\) be the hypergraph whose vertex set is the
disjoint union of ranks \(m-H,\ldots,m+H\), and whose hyperedges are these
full strips.  Its uniformity is

\[
R=2\ell(2H+1).
\tag{3.2}
\]

The lowest row recovers both cores and the undirected cycle, so the
hypergraph is simple.  Direct counting gives

\[
|E(\mathcal G)|=
\frac{(2m)!}{4\ell(m-\ell)!^2},
\tag{3.3}
\]

and the degree of a vertex in rank \(m+d\) is

\[
D_d=
\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.
\tag{3.4}
\]

Writing \(D=D_H=D_{-H}\),

\[
\frac D{D_0}
=\frac{(m+H)!(m-H)!}{m!^2}
=\exp(O(H^2/m)),
\tag{3.5}
\]

and

\[
\log D=(2+o(1))\ell\log m.
\tag{3.6}
\]

The stabilizer-orbit codegree argument gives

\[
\frac{\Gamma}{D}\le\frac{2\ell}{m-H}.
\tag{3.7}
\]

Indeed, after fixing one band mask, every nontrivial orbit of a second mask
under its stabilizer has size at least \(m-H\), while a strip through the
first mask has only \(2\ell\) members in the second mask's rank.  The only
relevant trivial-orbit candidate is the complement of the first mask; it has
codegree zero because every strip member contains the same nonempty core
\(C\).

### 3.2 Parameters and matching residual

Put

\[
L=\log m,\qquad \lambda=\log L,
\tag{3.8}
\]

and choose

\[
\omega\longrightarrow\infty,
\qquad
\omega=o(L/\lambda),
\tag{3.9}
\]

with

\[
H=\left\lfloor
\sqrt{\frac{L}{64\omega\lambda}}
\right\rfloor,
\qquad
\ell=\lceil\omega H\rceil.
\tag{3.10}
\]

Then

\[
R=(1+o(1))\frac{L}{16\lambda},
\qquad
\log D=(2+o(1))\ell L.
\tag{3.11}
\]

Set

\[
C_*=\left\lceil\frac{2\ell D}{m-H}\right\rceil,
\qquad
\eta=\frac{C_*\log(1+C_*)}{D}.
\tag{3.12}
\]

Equations (3.6)--(3.7) imply

\[
\eta=O\!\left(\frac{\ell^2L}{m}\right),
\qquad
\log\eta=-L+O(\lambda),
\tag{3.13}
\]

and hence

\[
\eta^{1/(R-1)}\le L^{-16+o(1)}.
\tag{3.14}
\]

The quantitative near-regular hypergraph matching theorem applies.  For
completeness, its relevant hypotheses reduce here to

\[
R\le\tfrac12\log D,
\tag{3.15}
\]

\[
e^{2R}\frac{C_*\log D}{D}=o(1),
\tag{3.16}
\]

and admissibility of the relative degree defect.  They follow from

\[
\frac R{\log D}=O(H/L)=o(1),
\tag{3.17}
\]

\[
\log\!\left(
 e^{2R}\frac{C_*\log D}{D}
\right)
=-L+2R+O(\lambda)=-L+o(L),
\tag{3.18}
\]

and

\[
\frac{H^2}{m}
=o\!\left[
 \left(\frac{\ell^2L}{m}\right)^{1/3}
\right].
\tag{3.19}
\]

The theorem therefore gives, deterministically, a strip matching whose total
number \(U\) of uncovered band vertices satisfies

\[
U=O\!\left(R\eta^{1/(R-1)}|V(\mathcal G)|\right)
\le W L^{-10}.
\tag{3.20}
\]

No random forest is being asserted here: the matching theorem supplies an
existence conclusion for a definite finite hypergraph.

### 3.3 Exact forest ledger

Suppose the matching selects \(p\) strips, and put \(s=2\ell\).  In the
middle and signed depth-\(q\) classes the uncovered counts are

\[
u_0=W-sp,
\qquad
u_q^-=u_q^+=N_q-sp.
\tag{3.21}
\]

Thus

\[
U=u_0+\sum_{q=1}^H(u_q^-+u_q^+).
\tag{3.22}
\]

Cut each selected middle cycle once, use Theorem 2.1 at the boundary, and add
the \(u_0\) uncovered middle masks as isolated vertices.  The resulting
spanning linear forest has

\[
c=p+u_0,
\qquad
\rho_H=0.
\tag{3.23}
\]

Every actual edge of a selected path can be certified.  Separate lower and
upper rainbowness follows from strip-matching disjointness.  Hence

\[
e=p(s-1),
\tag{3.24}
\]

and

\[
N_1-e=(N_1-sp)+p=u_1^-+p
\le U+\frac Ws=o(W).
\tag{3.25}
\]

By virtual cyclic closure, every selected path exposes all \(s\) matched
labels at every signed depth.  Isolated components and incidental witnesses
can only add supports, so

\[
\widetilde M_q^\pm\le u_q^\pm.
\tag{3.26}
\]

It follows that

\[
\begin{aligned}
H(c+\rho_H)
&+\sum_{q=2}^H
 (\widetilde M_q^-+\widetilde M_q^+)\\
&\le \frac{HW}{2\ell}+(H+1)U\\
&=\left(\frac1{2\omega}+o(1)\right)W+o(W)
=o(W).
\end{aligned}
\tag{3.27}
\]

We have proved the following.

### Theorem 3.1 (unconditional adaptive-MTF special case)

For the parameters (3.9)--(3.10), there is an oriented spanning Johnson
linear forest with compatible canonical MTF data satisfying

\[
N_1-e=o(W)
\tag{3.28}
\]

and

\[
H(c+\rho_H)+
\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)=o(W).
\tag{3.29}
\]

More generally this holds for every prescribed

\[
H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
\tag{3.30}
\]

Indeed, because \(H^2=o(L/\lambda)\), one can choose a slowly divergent
\(\ell/H\) while retaining the quantitative bound

\[
\ell H\le\frac{L}{64\lambda}.
\tag{3.31}
\]

The same matching estimates then have at least the residual margin used
above.

This is a genuine adaptive-MTF theorem, but it is far below
\(H=A\sqrt m\).  It therefore does not imply coefficient one.

---

## 4. Why the full-rainbow strip architecture stops

For

\[
q=t\sqrt m+o(\sqrt m),
\]

the exact product formula gives

\[
\frac{N_q}{W}\longrightarrow e^{-t^2}.
\tag{4.1}
\]

If full strip rows were required to be disjoint at every depth and the
middle row covered \((1-o(1))W\) masks, then the same number of distinct
rank-\((m-q)\) labels would be required.  At any fixed \(t>0\), this exceeds
the available \(N_q=(e^{-t^2}+o(1))W\).  Thus equal-slot full-rainbow strips
are capacity-impossible at Gaussian depth.  A successful Gaussian theorem
must either

- certify fewer, rank-dependent slots per component, or
- permit controlled overlap while covering almost every deep target.

The two exact formulations in Sections 6 and 7 implement these alternatives.

### 4.1 Independent occupancy is also at the wrong scale

If \(M=(1+o(1))W\) flags are sampled independently and uniformly from a
rank of size \(N_q\), the expected missing count is

\[
N_q\left(1-\frac1{N_q}\right)^M.
\tag{4.2}
\]

For \(q=t\sqrt m+o(\sqrt m)\),

\[
\frac1W\mathbb E M_q
\longrightarrow
e^{-t^2-e^{t^2}}>0.
\tag{4.3}
\]

The missing-label statistic is one-Lipschitz in each sample, so bounded
differences concentrates it on an \(o(W)\) scale.  Independent-looking
permutation or random-walk flags therefore leave a positive-density coupon
defect.  Any probabilistic construction must build strong negative
dependence and then be converted to a deterministic packing/covering object;
plain conditional expectation around the independent model cannot repair
this baseline.

For a locally stationary random Johnson walk, a newly inserted coordinate is
removed within the next \(H\) transitions with probability

\[
1-\left(1-\frac1m\right)^H.
\tag{4.4}
\]

At \(H=A\sqrt m\), this is

\[
\frac A{\sqrt m}+O_A(m^{-1}).
\tag{4.5}
\]

Thus a walk with \(M\) transitions has expected
\(\Theta_A(M/\sqrt m)\) short runs, and the reset charge
\(H\mathbb E\rho_H\) is \(\Theta_A(M)\), not \(o(M)\).

Projected high girth alone does not cure either defect.  A selected graph can
be a path while a coordinate is inserted and removed after any prescribed
\(r\le H\) steps.  Likewise the depth-one-rainbow path

\[
Rab,\quad Rbc,\quad Rcd,\quad Rda
\tag{4.6}
\]

has two identical depth-two intersections \(R\) and two identical
depth-two unions \(Rabcd\).  Girth and first-shadow rainbowness do not control
deep support.

---

## 5. Exact Gaussian reduction from an odd factor

The known exact odd wreath factor theorem may be cut at a distinguished
coordinate \(\infty\).  It produces

\[
B=\operatorname{Cat}_m=\frac{W}{m+1}
\tag{5.1}
\]

vertex-disjoint complementary geodesics

\[
T_0,T_1,\ldots,T_m
\tag{5.2}
\]

which partition \(\binom{[2m]}m\).  On each path there is a cyclic order

\[
w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1})
\tag{5.3}
\]

such that

\[
T_t=I_w(t,m),
\qquad 0\le t\le m.
\tag{5.4}
\]

The transition removes \(a_t=w_t\) and inserts
\(b_t=w_{t+m}\).  Inserted coordinates are never removed and removed
coordinates never return.  Hence

\[
\rho_H=0,
\qquad
c=B.
\tag{5.5}
\]

At Gaussian depth,

\[
Hc=\frac{HW}{m+1}=O_A(W/\sqrt m)=o(W).
\tag{5.6}
\]

Choose the initial singleton queue

\[
(\{w_{2m-1}\},\ldots,\{w_{2m-H}\},R_0)
\tag{5.7}
\]

and terminal dummies

\[
w_m,w_{m+1},\ldots,w_{m+H-1}.
\tag{5.8}
\]

Then for every \(0\le t\le m\) and \(q\le H\),

\[
\boxed{
P^-_{t,q}=I_w(t+q,m-q),
\qquad
P^+_{t,q}=I_w(t-q,m+q).
}
\tag{5.9}
\]

This includes the boundary flags.  The \(mB=N_1\) actual upper edge colours
partition rank \(m+1\): they are complements of the odd factor's
length-\(m\) cyclic intervals containing \(\infty\).  Thus all actual upper
colours are automatically distinct.

Let \(\mathcal L_1(F)\) be the support of the actual lower edge colours in
the cut factor.  Since the actual upper colours are unique, choosing one edge
for every label in \(\mathcal L_1(F)\) gives a certified set of size

\[
e=|\mathcal L_1(F)|.
\tag{5.10}
\]

Consequently, the following is a sharp sufficient theorem inside the odd-cut
architecture.

### Missing theorem 5.1 (odd-cut support theorem)

For every fixed \(A>0\), some exact odd wreath factor and one common cut
coordinate satisfy

\[
N_1-|\mathcal L_1(F)|=o(W)
\tag{5.11}
\]

and

\[
\sum_{q=2}^H
\left(
N_q-\left|\{I_w(t+q,m-q)\}_{P,t}\right|
+N_q-\left|\{I_w(t-q,m+q)\}_{P,t}\right|
\right)
=o(W),
\tag{5.12}
\]

where \(P\) ranges over all cut paths and \(0\le t\le m\).

If (5.11)--(5.12) hold, then (5.5)--(5.10) prove \(\mathrm{AD}_A\)
literally.  No component, run, dummy, residual-order, or upper first-shadow
lemma remains.  This is still unproved, but it is strictly sharper than the
original formulation because every MTF compatibility choice has disappeared
from the quantifier.

---

## 6. Certified-slot complementary-geodesic matching

The odd-cut support theorem permits repeats.  A stronger standard packing
statement is obtained by certifying only the number of flags that each rank
can support.

### 6.1 Atoms and quotas

Put

\[
K=m+1.
\tag{6.1}
\]

A complementary geodesic atom is determined by an initial set \(A_0\), an
ordering \(a_0,\ldots,a_{m-1}\) of \(A_0\), and an ordering
\(b_0,\ldots,b_{m-1}\) of its complement:

\[
T_i=
\left(A_0\setminus\{a_0,\ldots,a_{i-1}\}\right)
\cup\{b_0,\ldots,b_{i-1}\},
\qquad 0\le i\le m.
\tag{6.2}
\]

For \(1\le q\le H\) and \(0\le i\le m-q\), define genuine internal
fragment colours

\[
D^-_{i,q}=\bigcap_{j=0}^qT_{i+j},
\qquad
D^+_{i,q}=\bigcup_{j=0}^qT_{i+j}.
\tag{6.3}
\]

Explicitly,

\[
D^-_{i,q}=
\left(A_0\setminus\{a_0,\ldots,a_{i+q-1}\}\right)
\cup\{b_0,\ldots,b_{i-1}\},
\tag{6.4}
\]

and

\[
D^+_{i,q}=
\left(A_0\setminus\{a_0,\ldots,a_{i-1}\}\right)
\cup\{b_0,\ldots,b_{i+q-1}\}.
\tag{6.5}
\]

There are exactly \(K-q\) distinct colours of each sign.

Set

\[
r_q=\frac{N_q}{W},
\qquad
s_q=\lfloor Kr_q\rfloor.
\tag{6.6}
\]

Then

\[
s_q\le K-q.
\tag{6.7}
\]

To prove this, note that

\[
r_1=\frac m{m+1}=\frac{K-1}{K}
\tag{6.8}
\]

and

\[
r_{q+1}=r_q\frac{m-q}{m+q+1}.
\tag{6.9}
\]

If \(r_q\le(K-q)/K\), then

\[
r_{q+1}
\le\frac{m+1-q}{m+1}\frac{m-q}{m+q+1}
\le\frac{m-q}{m+1}
=\frac{K-q-1}{K}.
\]

At depth one,

\[
s_1=m=K-1,
\tag{6.10}
\]

so every actual edge is certified on both signs.  Uniformly for
\(q\le A\sqrt m\),

\[
r_q=\exp(-q^2/m+O_A(m^{-1/2})),
\qquad
s_q=\Theta_A(K).
\tag{6.11}
\]

### 6.2 The decorated atom hypergraph

Let \(\mathcal Q_{m,H}\) have parts

\[
V_0=\binom{[2m]}m,
\qquad
V_q^-=\binom{[2m]}{m-q},
\qquad
V_q^+=\binom{[2m]}{m+q}.
\tag{6.12}
\]

A decorated atom edge contains

- all \(K\) middle vertices of a complementary geodesic;
- \(s_q\) chosen internal lower colours and \(s_q\) chosen internal upper
  colours at every depth \(q\);
- all \(K-1\) actual colours at \(q=1\).

Include the full \(S_{2m}\)-invariant family of atoms and all allowed slot
choices.  The full-family quantifier is essential: restricting to a frozen
factor destroys the degree calculation.  Parallel decorated descriptions may
be retained as atom multiplicity or aggregated; the matching condition is
simply disjointness of all displayed set labels.

The rank is

\[
R_{\rm atom}=K+2\sum_{q=1}^Hs_q
=\Theta_A(m^{3/2}).
\tag{6.13}
\]

Let \(E\) be the decorated atom set and let \(D_0,D_q^\pm\) be the part
degrees.  Coordinate transitivity and incidence double counting give

\[
D_0W=|E|K,
\qquad
D_q^\pm N_q=|E|s_q.
\tag{6.14}
\]

Therefore

\[
\frac{D_q^\pm}{D_0}
=\frac{s_qW}{KN_q}
\le1,
\tag{6.15}
\]

and, uniformly for \(q\le H\),

\[
\frac{D_q^\pm}{D_0}=1+O_A(1/m).
\tag{6.16}
\]

At \(q=1\) the ratio is exactly one.

Assigning weight \(1/D_0\) to every atom is consequently an exact
fractional matching: it saturates every middle vertex and gives load at most
one to every certified-colour vertex.  Its total mass is

\[
\frac WK=\operatorname{Cat}_m.
\tag{6.17}
\]

The unused fractional capacity in either signed \(q\)-part is

\[
N_q-\frac WK s_q<\frac WK.
\tag{6.18}
\]

Thus the aggregate deterministic floor over all signed depths is

\[
2\sum_{q=1}^H
\left(N_q-\frac WK s_q\right)
<\frac{2HW}{K}
=O_A(W/\sqrt m)=o(W).
\tag{6.19}
\]

There is no marginal, divisibility, or fractional-capacity obstruction.

### Missing theorem 6.1 (high-precision atom rounding)

For every fixed \(A>0\), the hypergraph \(\mathcal Q_{m,H}\) has an
integral matching \(\mathcal M\) such that

\[
\boxed{
L:=W-K|\mathcal M|=o(W/H).
}
\tag{6.20}
\]

This statement implies \(\mathrm{AD}_A\).

### Proof of the implication

Use the matched atoms as oriented path components and add the \(L\)
uncovered middle vertices as singleton components.  Complementary geodesics
have no internal positive re-exit, so

\[
c=|\mathcal M|+L\le\frac WK+L,
\qquad
\rho_H=0.
\tag{6.21}
\]

All actual first colours are separately rainbow, and

\[
e=m|\mathcal M|.
\tag{6.22}
\]

Since \(N_1=mW/K\),

\[
N_1-e=\frac{mL}{K}<L=o(W).
\tag{6.23}
\]

For every \(q\ge2\), the canonical support contains the certified colours,
so

\[
\begin{aligned}
\widetilde M_q^\pm
&\le N_q-|\mathcal M|s_q\\
&=\left(N_q-\frac WK s_q\right)
  +\frac LK s_q\\
&<\frac WK+L.
\end{aligned}
\tag{6.24}
\]

Consequently

\[
\begin{aligned}
H(c+\rho_H)
&+\sum_{q=2}^H
 (\widetilde M_q^-+\widetilde M_q^+)\\
&\le H\left(\frac WK+L\right)
 +2(H-1)\left(\frac WK+L\right)\\
&=o(W),
\end{aligned}
\tag{6.25}
\]

because \(K=m+1\), \(H=O_A(\sqrt m)\), and (6.20) holds.

Literal MTF compatibility is automatic.  Internal lower fragments use only
actual future departures.  An internal upper fragment ending at state \(i\)
uses the previous departed coordinates
\(a_{i-1},\ldots,a_{i-q}\), none of which re-enter.  Legal boundary dummies
and an initial queue exist because \(m\ge2H\) eventually, and they affect only
uncertified boundary slots.  Singleton components also admit legal boundary
data.

### Exact scope of the remaining matching problem

The rank (6.13) grows like \(m^{3/2}\).  Nested flag pairs can have normalized
codegree of order \(1/m\), and the required relative atom leave is
\(o(1/H)\), not merely \(o(1)\).  Fixed-uniformity nibble theorems therefore
do not establish (6.20).  This observation is not an impossibility theorem;
it identifies the missing specialized rounding/absorption input.

The known odd-wreath normal form proves that the middle-only atom system has
perfect matchings.  At \(q=1\), the upper part enforces exactly the edge-union
partition needed to reconstruct an odd factor, while the separate lower part
adds the desired first-shadow rainbow.  Thus no hidden wreath-validity
condition is omitted from the atom definition.

---

## 7. Alternative Gaussian strip packing/covering lemma

The same obstruction can be stated without discarding deep strip slots.
Choose

\[
H\ll\ell=o(m).
\tag{7.1}
\]

It is enough to select \(p\) full strips such that

1. their middle rows and their two signed depth-one rows are disjoint;
2. with
   \[
   \delta=N_1-2\ell p,
   \tag{7.2}
   \]
   one has \(\delta=o(W/H)\);
3. the aggregate missing support of the selected full rows at signed depths
   \(2,\ldots,H\) is \(o(W)\).

Indeed, after cyclic closure and adding uncovered middles,

\[
u_0=W-2\ell p=(W-N_1)+\delta,
\tag{7.3}
\]

\[
c=p+u_0,
\qquad
\rho_H=0,
\tag{7.4}
\]

and

\[
e=p(2\ell-1),
\qquad
N_1-e=\delta+p=o(W).
\tag{7.5}
\]

Moreover

\[
Hc
\le\frac{HW}{2\ell}
 +\frac{HW}{m+1}+H\delta
=o(W).
\tag{7.6}
\]

This packing/covering problem has an exact symmetric fractional solution.
The strip degrees obey

\[
\frac{D_q}{D_0}
=\frac{(m+q)!(m-q)!}{m!^2}
=\frac W{N_q}.
\tag{7.7}
\]

Put

\[
\alpha=\frac{N_1}{W}=\frac m{m+1}
\tag{7.8}
\]

and weight every strip by \(\alpha/D_0\).  Every middle label receives load
\(\alpha\), every signed first-shadow label load one, and every signed
depth-\(q\) label load

\[
\alpha\frac{D_q}{D_0}=\frac{N_1}{N_q}\ge1.
\tag{7.9}
\]

The total strip weight is \(N_1/(2\ell)\), exactly the desired value of
\(p\).  Hence the Gaussian difficulty is integral correlated rounding of a
hybrid packing/covering system, not its fractional margins.

The certified-slot theorem in Section 6 converts the same rank imbalance to
an ordinary packing problem by retaining only \(s_q\) flags per atom.

---

## 8. Exact projected-walk defect identity

The canonical support defects admit a useful topological decomposition.

Let a post-cut MTF forest have \(C\) path components and \(W\) middle-state
occurrences.  Refine each residual partition to a full order without changing
its first \(H\) singleton blocks.  For a fixed sign and depth \(q\), form a
multigraph \(\Gamma_q\) as follows.

- Its vertices are the distinct canonical \(q\)-mask labels.
- Every adjacency of consecutive middle states inside a source path produces
  one edge between their two \(q\)-labels.
- Multiplicity and loops are retained.

There are \(W-C\) edge occurrences.  Let

- \(\ell_q\) be the loop count;
- \(d_q\) be the number of connected components after loops are deleted,
  retaining isolated vertices;
- \(\beta_q\) be the cyclomatic number
  \[
  \beta_q=(W-C-\ell_q)-|V(\Gamma_q)|+d_q;
  \tag{8.1}
  \]
- \(\mu_q=C-d_q\), the number of source-component mergers under the
  projection.

Every source path has connected image, so \(d_q\le C\) and \(\mu_q\ge0\).

### Theorem 8.1 (exact defect decomposition)

For either sign,

\[
\boxed{
\widetilde M_q
=\ell_q+\beta_q+\mu_q-(W-N_q).
}
\tag{8.2}
\]

### Proof

Deleting loops leaves \(W-C-\ell_q\) edges.  By the definition of cycle
rank,

\[
|V(\Gamma_q)|
=(W-C-\ell_q)-\beta_q+d_q.
\tag{8.3}
\]

Substitute this into
\(\widetilde M_q=N_q-|V(\Gamma_q)|\), and use
\(\mu_q=C-d_q\).  \(\square\)

Equivalently,

\[
W-|V(\Gamma_q)|=\ell_q+\beta_q+\mu_q.
\tag{8.4}
\]

Thus loops, projected cycles/parallel returns, and mergers account for every
repeated occurrence; \(W-N_q\) is the unavoidable pigeonhole floor.

For the lower tower, all projected transitions are nonloops through depth
\(H\).  Indeed,

\[
P^-_{i+1,q}
=P^-_{i,q}-\{p_{i+q}\}+\{q_i\},
\tag{8.5}
\]

and equality would mean that the coordinate entering at transition \(i\)
exits within \(q\le H\) steps.  Such a transition was cut when
\(p_{i+q}\) is actual, and equality is forbidden by compatible dummy
legality when \(p_{i+q}\) is virtual near the right boundary.  For \(q<H\),
the lower flags also satisfy the exact rhombus identities

\[
P^-_{i,q}\cap P^-_{i+1,q}=P^-_{i,q+1},
\tag{8.6}
\]

\[
P^-_{i,q}\cup P^-_{i+1,q}=P^-_{i+1,q-1}.
\tag{8.7}
\]

On the upper side, let \(s_i\) be the position of the arrival \(q_i\) in
the pre-update complement order.  Then the projected step is a loop exactly
when \(s_i\le q\).  If \(s_i>q\), it is a Johnson edge and obeys the analogous
rhombus relations.  In particular,

\[
\ell_q^+=|\{i:s_i\le q\}|,
\tag{8.8}
\]

and

\[
\sum_{q=2}^H\ell_q^+
=\sum_i(H-\max\{2,s_i\}+1)_+.
\tag{8.9}
\]

This identifies the deep AD term exactly as projected self-intersection
energy above the unavoidable floors.  First-shadow rainbowness controls only
the \(q=1\) projection; it does not bound the higher \(\beta_q\) or
\(\mu_q\).  Formula (8.2) is an identity, not a dispersion theorem.

---

## 9. Optimal deterministic cutting of short runs

The original AD ledger cuts every short positive run at its entry edge.  A
smaller exact cut set is available.

Consider one path

\[
T_0,T_1,\ldots,T_s,
\qquad
e_i:T_{i-1}\to T_i
\quad(1\le i\le s).
\tag{9.1}
\]

Within this section, write the removed and inserted coordinates on \(e_i\)
as \(p_i\) and \(q_i\).  This is the local one-based reindexing of (1.1).

If a coordinate enters at \(e_a\) and exits at \(e_b\), its positive run is
\(T_a,\ldots,T_{b-1}\), of length \(b-a\).  Associate a short run with the
closed transition interval

\[
I_x=[a,b]\subseteq\{1,\ldots,s\}.
\tag{9.2}
\]

### Theorem 9.1 (interval-transversal theorem)

Let \(\tau_H\) be the minimum number of path edges meeting every short-run
interval.  Then

\[
\tau_H
=\max\{\hbox{number of pairwise edge-disjoint short-run intervals}\}.
\tag{9.3}
\]

A cut set \(C\) makes every fragment free of internal short positive runs if
and only if it meets every interval \(I_x\).

Moreover, if \(\rho_H\) is the number of short runs, then

\[
\boxed{
\frac{\rho_H}{H+1}\le\tau_H\le\rho_H.
}
\tag{9.4}
\]

### Proof

If \(C\cap[a,b]=\varnothing\), the entry, positive vertices, and exit remain
in one fragment, so the run stays internal.  A cut at \(a\) or \(b\) moves
one end to a boundary, while a cut strictly between them splits the run into
a terminal and an initial boundary run.  Cutting creates no new positive
run.  This proves the first equivalence.

For interval duality, repeatedly choose a remaining interval with least right
endpoint, put that endpoint into \(C\), and discard every interval it hits.
The chosen witness intervals are pairwise disjoint, and every transversal
needs one point for each witness.  The chosen endpoints form a transversal,
proving (9.3).

A transition \(j\) lies in at most \(H+1\) short-run intervals: their entry
indices are distinct and lie in \([j-H,j]\).  Thus any transversal of size
\(\tau_H\) can hit at most \((H+1)\tau_H\) runs, which proves the lower bound
in (9.4); the upper bound follows by selecting one point from every interval.
\(\square\)

For a forest, \(\tau_H\) means the minimum transversal size over the disjoint
union of all component edge sets.  Equivalently it is the sum of the
componentwise values, since no cut edge can hit intervals from two different
components.

### Sharpness

For \(H\le m-2\), there is a simple Johnson path with exactly \(H+1\) short
runs whose intervals are

\[
[1+t,H+1+t],
\qquad 0\le t\le H.
\tag{9.5}
\]

They all meet only at transition \(H+1\).  One construction starts with
\(R\cup\{y_0,\ldots,y_{H-1}\}\), where \(|R|=m-H\), replaces
\(y_t\) by \(x_t\) for \(0\le t<H\), replaces \(x_0\) by \(x_H\), then
replaces \(x_t\) by \(y_t\) for \(1\le t<H\), and finally replaces
\(x_H\) by a new coordinate \(z\).  The only internal short runs are the
\(x_t\).  Hence

\[
\rho_H=H+1,
\qquad
\tau_H=1.
\tag{9.6}
\]

### 9.1 Exact colour-aware cut ledger

Let \(F\) be an oriented spanning forest with \(c\) components and \(e\)
certified edges.  Let \(C\) hit every short-run interval.  The post-cut
forest has \(c+|C|\) components.

At a cut edge \(e_i:T_{i-1}\to T_i\), the removed coordinate \(p_i\) is
always legal as the first initial upper singleton on the right, recovering
the upper colour \(T_i\cup\{p_i\}\).  It is legal as the first terminal
dummy on the left unless it entered within the preceding \(H\) steps and no
earlier cut separated that entry from \(e_i\).

Define

\[
b_H(C)=
\#\left\{
\begin{array}{l}
i\in C\cap E_{\rm cert}:\ 
\text{there is a short interval }[a,i],\\
\hfill C\cap[a,i]=\{i\}
\end{array}
\right\}.
\tag{9.7}
\]

Exactly \(b_H(C)\) certified lower cut-edge occurrences fail their prescribed
canonical terminal recovery.  An incidental occurrence elsewhere may still
represent the same mask, so the global lower support loses at most
\(b_H(C)\) labels.  Therefore

\[
\boxed{
\begin{aligned}
L_{\rm band}\le {}&
W+(2H+1)(c+|C|)+2(N_1-e)+b_H(C)\\
&+\sum_{q=2}^H
(\widetilde M_{q,C}^-+\widetilde M_{q,C}^+).
\end{aligned}
}
\tag{9.8}
\]

The proof is exactly the first-band ledger: every certified upper colour
survives, while the lower support loses at most \(b_H(C)\) additional
labels.  When \(m\ge2H\), every legal prescribed first dummy can be extended
to \(H\) distinct dummies, and every prescribed initial singleton can be
extended to \(H\) complement singletons plus a nonempty residual.

Since \(b_H(C)\le|C|\), taking a minimum transversal replaces the sufficient
reset condition

\[
H(c+\rho_H)
\tag{9.9}
\]

by

\[
\boxed{H(c+\tau_H).}
\tag{9.10}
\]

Constants are absorbed because the additional \(b_H(C)\) is at most
\(\tau_H\).  The canonical deep defects in this improved criterion are those
produced by the same minimum-transversal cut and its compatible boundary
data; they cannot be retained from a different cut scheme.

If one insists that every certified cut-edge lower colour survive, there is
always a transversal \(C\) with

\[
|C|\le2\tau_H,
\qquad
b_H(C)=0.
\tag{9.11}
\]

Take the earliest-right-endpoint greedy witnesses \([a_k,b_k]\), cut at all
\(b_k\), and add every \(a_k\).  The cut at \(b_k\) is protected by \(a_k\).
If a newly added \(a_k\) were the bad exit of an earlier short run, that
earlier interval had smaller right endpoint and must already have been hit by
an earlier greedy point.  Thus every added cut is good.  The family (9.5)
shows that the factor two is sharp: its unique one-point transversal is a bad
exit when that common exit edge is declared certified, whereas two cuts
suffice.

The original entry-edge rule corresponds to \(|C|=\rho_H\) and
\(b_H(C)=0\).  The interval theorem is a strict deterministic improvement,
not a change in the meaning of the original theorem.

---

## 10. Exact safe-splice identities and conflict-free augmentation

Endpoint splicing can reduce the component count, but safety must be checked
against run ages.

Let an oriented path \(P\) end at \(A\), an oriented path \(Q\) start at
\(B\), and suppose the seam

\[
A\longrightarrow B=A-\{x\}+\{y\}
\tag{10.1}
\]

is a Johnson edge.  For \(z\in A\), let \(\alpha_P(z)\) be the length of
its terminal positive suffix if that suffix began internally; otherwise use
a boundary symbol \(\partial\).  For \(z\in B\), let \(\beta_Q(z)\) be the
length of its initial positive prefix if it exits internally; otherwise use
\(\partial\).

### Theorem 10.1 (exact seam penalty)

The number of new short positive runs created by the seam is

\[
\boxed{
\begin{aligned}
\eta_H(P,Q)={}&
\mathbf1_{\{\alpha_P(x)\in[H]\}}
+\mathbf1_{\{\beta_Q(y)\in[H]\}}\\
&+\left|
\left\{
z\in A\cap B:
\begin{array}{l}
\alpha_P(z),\beta_Q(z)\text{ are numeric},\\
\alpha_P(z)+\beta_Q(z)\le H
\end{array}
\right\}
\right|.
\end{aligned}
}
\tag{10.2}
\]

Consequently

\[
\rho_H(P\oplus Q)
=\rho_H(P)+\rho_H(Q)+\eta_H(P,Q).
\tag{10.3}
\]

The three terms are disjoint and exhaustive: the seam closes the terminal
run of \(x\), opens the initial run of \(y\), and fuses terminal and initial
runs of common coordinates.  Boundary runs are excluded exactly by the
symbol \(\partial\).  There is at most one coordinate of each exact terminal
age, so

\[
\eta_H(P,Q)\le H+1.
\tag{10.4}
\]

A seam is locally \(H\)-safe precisely when \(\eta_H(P,Q)=0\).

### Theorem 10.2 (static long-block composition)

Suppose selected endpoint seams form a directed linear forest after the base
components are contracted.  Assume every base component receiving both an
incoming and an outgoing seam has more than \(H\) middle vertices, and every
selected seam is locally safe in its induced orientation.  Then their
simultaneous concatenation creates no new short positive run.

Indeed, a new run crossing two or more seams contains every middle vertex of
an intervening degree-two base block and is therefore longer than \(H\).  A
short new run can cross only one seam and would be counted by (10.2).

This removes the usual noncomposition flaw for safe-splice graphs with long
internal blocks.

### A component-count special case

Assume an \(H\)-safe forest has all components longer than \(H\), and every
undirected Johnson adjacency between endpoints of distinct components admits
a locally safe directed seam after orienting or reversing the two components
so that the chosen endpoints are terminal and initial.
Greedily splice distinct components until no such adjacency remains.  The
outer profiles can change a boundary symbol into a numeric age larger than
\(H\), but their truncated \(H\)-relevant safety data do not change.  Thus
Theorem 10.2 keeps the forest safe.

If \(c\) components remain, their \(2c\) endpoints induce at most \(c\)
Johnson edges, since every edge between different components would be an
available splice.  The Johnson graph \(J(2m,m)\) is \(m^2\)-regular and has
least eigenvalue \(-m\).  For any endpoint set \(S\),

\[
2e(S)\ge
\frac{(m^2+m)|S|^2}{W}-m|S|.
\tag{10.5}
\]

Putting \(|S|=2c\) and \(e(S)\le c\) gives

\[
c\le\frac{W}{2m}.
\tag{10.6}
\]

Hence \(Hc=o(W)\) whenever \(H=o(m)\).  Old certified colours survive
because the new splices may be left uncertified.  This theorem solves only
the component/run part; it does not control deep projected support.

### Conflict formulation for certified augmentations

If new splices must also be certified, encode each candidate by the resources

\[
\{\hbox{left endpoint slot},\hbox{right endpoint slot},
  \hbox{lower colour},\hbox{upper colour}\}.
\tag{10.7}
\]

First discard every candidate whose lower or upper colour is already used by
the certified base forest.  A matching on the remaining candidates enforces
endpoint capacity and separate lower/upper rainbowness.
One must additionally forbid

- every cycle in the contracted component multigraph, including a two-cycle
  formed by two endpoint-disjoint seams between the same two base paths;
- every minimal selected-seam set producing a short positive run.

The latter conflict has size at most \(H+1\).  Under the long-degree-two
hypothesis it reduces to a forbidden singleton, namely a locally unsafe seam.
This is the correct conflict-free augmentation object.  A matching on
endpoint and colour resources alone is insufficient.

---

## 11. What has and has not been proved

### Proved here

1. Exact virtual cyclic-boundary MTF closure, with the correct upper-window
   indexing and zero deep-support loss.
2. A deterministic adaptive-MTF forest theorem through
   \[
   H=o\!\left(\sqrt{\log m/\log\log m}\right).
   \]
3. The exact Gaussian odd-cut reduction in which components, runs, dummies,
   residual queues, and upper first-shadow rainbowness are automatic.
4. An exactly degree-balanced certified-slot fractional matching and the
   rigorous implication
   \[
   L=o(W/H)\Longrightarrow\mathrm{AD}_A.
   \]
5. The projected-walk identity (8.2), isolating deep defects as loops, cycle
   rank, and component mergers above the pigeonhole floor.
6. The sharp interval-transversal theorem, the colour-aware ledger (9.8),
   and the replacement of the explicit reset/component charge based on
   \(\rho_H\) by one based on \(\tau_H\), with supports recomputed jointly.
7. Exact seam additivity, a valid static composition criterion, and a
   spectral component-count special case.

### Still missing

Any one of the following would finish the direct Gaussian lane:

- the odd-cut support theorem (5.11)--(5.12);
- the high-precision certified-slot matching theorem (6.20);
- the hybrid strip packing/covering lemma of Section 7;
- a different deterministic augmentation theorem simultaneously controlling
  the upper loop terms and driving the projected cycle/merger excess in
  (8.2) to its floor, while retaining the first-shadow and reset estimates.

The cleanest compact target is (6.20): round one explicit symmetric
fractional matching of rank \(\Theta_A(m^{3/2})\) to relative atom leave
\(o(1/H)\).  The cleanest structurally minimal target is (5.11)--(5.12):
choose one exact odd factor whose explicit interval maps have aggregate
support defect \(o(W)\).

### Caveats

- The near-square-root-log theorem is not a slow-diagonal claim; its
  parameters are quantitative.  It still gives no information at
  \(H=A\sqrt m\).
- Full all-depth rainbowness is impossible at Gaussian depth.  The certified
  quotas or controlled multiplicities are essential.
- Rank balance and small pair codegrees do not by themselves yield the
  \(o(W/H)\) integral leave required in (6.20).
- The projected defect identity is descriptive.  It does not prove a bound
  on cycle rank or component merger.
- Safe splicing controls runs and components but not automatically the deep
  MTF supports.
- All upper and lower supports in the implications come from one common
  oriented forest and one common compatible boundary/residual assignment.
  Independently optimized ranks would not prove \(\mathrm{AD}_A\).
- This lane constructs a literal adaptive-MTF word if its missing theorem is
  proved.  It does not prove MWB or labelled wreath synchronization.

---

## 12. Independent audit record

Three independent audits were used.

1. The cyclic-strip audit rederived the terminal dummy order, the initial
   queue order, the backward indexing of upper flags, all degree and
   codegree constants, every quantitative matching hypothesis, and the
   exact \(U\)-ledger.  Verdict: valid.
2. The run/augmentation audit independently proved interval duality, the
   sharp \(H+1\) example, the bad-cut term \(b_H(C)\), the sharp
   colour-preserving \(2\tau_H\) construction, the seam formula, and the
   long-block composition theorem.  Verdict: valid with the stated scopes.
3. The MTF/hypergraph audit checked \(s_q\le K-q\), the first-depth equality
   \(s_1=K-1\), the part-degree normalization, the fractional floor, the
   exact leave requirement \(L=o(W/H)\), literal boundary compatibility, and
   the projected-walk identity.  Verdict: valid; the integral rounding
   theorem remains genuinely unproved.

No web search, finite search, or computational experiment is used in any of
the arguments above.
