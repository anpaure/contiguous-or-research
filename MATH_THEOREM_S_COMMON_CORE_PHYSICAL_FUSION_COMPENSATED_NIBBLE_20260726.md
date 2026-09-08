# Common-core physical fusion: exact path degrees, a compensated bite, and a signed-trace amplification obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Result and scope

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
\]

and

\[
 M=m+H,\qquad s=m-H,\qquad n=m-2H,
 \qquad L=m-3H+1,
\tag{0.1}
\]

where

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>5H,
\tag{0.2}
\]

and, for fixed constants \(c_0,C_0>0\),

\[
 L+c_0H\le\Lambda=\frac W{N_H}\le m+C_0H.
\tag{0.2a}
\]

This report attacks the integral physical-fusion gate left by the global
common-core atlas. It proves the following.

1. The simple rooted hypergraph of **middle shadows** of physical
   common-core tight paths has
   exact root degree

   \[
   R=\frac{M!}{2(3H)!},
   \tag{0.3}
   \]

   exact middle degree

   \[
   D=\frac{L(m!)^2}{2(3H)!(m-H)!}
     =\rho R,
   \qquad \rho=\frac L\Lambda<1,
   \tag{0.4}
   \]

   and exact middle-pair sequence

   \[
   \frac{d(X,Y)}D=
   \begin{cases}
   \displaystyle\frac{2(L-d)}{L\binom md^2},&1\le d<H,\\[2mm]
   \displaystyle\frac{(L-H)(L-H+1)}{L\binom mH^2},&d=H,\\[2mm]
   0,&d>H,
   \end{cases}
   \tag{0.5}
   \]

   where \(d=d_J(X,Y)\). Thus

   \[
   \frac{\Delta_2}{D}=\frac{2(L-1)}{Lm^2}
   =\frac{2+o(1)}{m^2}.
   \tag{0.6}
   \]

2. Linear-path geometry improves the crude \(L\Delta_2\) union bound.
   If \(e\) is a path edge and \(X\notin e\), then the exact asymptotic
   maximum external middle-link influence is

   \[
   \max_{X\notin e}
   \frac{|\{f:X\in f,\ f\cap e\ne\varnothing\}|}{D}
   =\frac{6(L-1)}{Lm^2}+O(m^{-4}).
   \tag{0.7}
   \]

3. There is an exact compensated one-bite lemma. It makes every root and
   every middle owner have the same deletion marginal, while accepting a
   genuine matching. In the initial common-core catalogue, a bite with
   root activation probability \(\gamma/L\) accepts

   \[
   \left(\gamma e^{-\gamma\rho}+o(1)\right)\frac{N_H}{L}
   \tag{0.8}
   \]

   paths in expectation. This is an integral one-wave theorem, not a
   near-perfect factor theorem; hereditary regeneration remains unproved.

4. After losing only \(O(HN_H)=o(W)\) aggregate occurrences, the nested
   signed traces can be placed away from both path endpoints and become
   literal unions and intersections of consecutive middle owners. Thus
   endpoint collars are not the remaining obstruction.

5. Middle fusion does not automatically propagate to signed fusion. A
   new local-reversal gadget has **no middle collision between its two
   paths**, but has exactly \(\ell\) common traces at every deletion
   length

   \[
   1\le\ell\le\lfloor H/2\rfloor.
   \tag{0.9}
   \]

   Replacing only

   \[
   K=\left\lfloor\frac{cW}{H^2}\right\rfloor
   \tag{0.10}
   \]

   disjoint top pairs changes middle overload plus leave by only
   \(O(W/\log m)=o(W)\), but creates \(\Omega(W)\) activatable upper
   signed repeats. The required high-tag scalar capacity fits exactly;
   actual completion is conditional on a legal compensation reservoir,
   because the short-path catalogue alone has fewer than \(W\) phase
   slots.

Consequently, an RPRN theorem whose state consists only of roots, middle
owners, and middle external influence cannot prove signed inheritance.
The exact surviving positive gate is a trace-weighted regeneration theorem
controlling both the rankwise occurrence deficit and the active interval
influence defined in Section 5. No coefficient-one conclusion is claimed.

## 1. The physical middle-path hypergraph

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad
 \mathcal X=\binom{[2m]}m.
\]

A reduced decorated option consists of a top \(U\), an unordered core
\(Q\in\binom U{2H}\), and an oriented injective word

\[
 w=(w_1,\ldots,w_n)
\tag{1.1}
\]

in \(U\setminus Q\). The remaining \(H\) noncore coordinates are left
unordered. Put

\[
 B_i(w)=\{w_i,\ldots,w_{i+H-1}\},\qquad
 X_i(U,w)=U\setminus B_i(w),\qquad1\le i\le L.
\tag{1.2}
\]

The rooted hyperedge is

\[
 e(U,Q,w)=\{U\}\cup\{X_1,\ldots,X_L\}.
\tag{1.3}
\]

Ordering the unused \(H\) coordinates before the word in (1.1), and
ordering the core separately, reconstructs the literal full common-core
promotion path. The quotient in this section forgets only data invisible
to the middle owner set. That data is not invisible to lower signed
traces, so the middle quotient and the all-depth trace catalogue must be
distinguished.

### Theorem 1.1 (decorated degrees and physical multiplicity)

The reduced decorated root and middle degrees are

\[
 D_U^{\rm dec}=\frac{M!}{(2H)!H!},\qquad
 D_X^{\rm dec}=\frac{L(m!)^2}{(2H)!H!(m-H)!}.
\tag{1.4}
\]

Every unordered simple rooted path has exactly

\[
 \mu_{\rm red}=2\binom{3H}{2H}
\tag{1.5}
\]

reduced decorated representations. If all hidden orders are restored,
the full-order catalogue has \(M!\) options per root and simple-edge
multiplicity

\[
 \mu_{\rm full}=2(3H)!.
\tag{1.6}
\]

Hence the simple degrees are exactly (0.3)--(0.4).

#### Proof

For a fixed root, choose the core and inject the \(n\)-word into the
remaining \(s\) letters:

\[
 \binom M{2H}(s)_n=\frac{M!}{(2H)!H!}.
\]

For a fixed middle owner \(X\), choose a top in \(\binom mH\) ways, a
core in \(\binom m{2H}\) ways, the one of \(L\) window positions, and
then the word in \(n!\) ways. This gives the second formula in (1.4).

From an unordered physical edge, the distance-one graph of the omitted
\(H\)-windows recovers their linear order up to reversal. Their successive
differences recover all \(n\) used word coordinates. The remaining
\(3H\) coordinates may contain any \(2H\)-subset as the core, and reversal
gives the factor two in (1.5). Restoring the internal core and unused-tail
orders multiplies by \((2H)!H!\), giving (1.6). Division proves
(0.3)--(0.4). \(\square\)

### Corollary 1.1a (raw all-depth trace degrees)

Retain the unordered core \(Q\) and the entire oriented tail order rather
than quotienting the hidden prefix. Then the raw all-depth option degrees
are

\[
 R_{\rm tr}=\binom M{2H}s!=\frac{M!}{(2H)!},
\tag{1.6a}
\]

\[
 D_{\rm tr}=\binom mH\binom m{2H}LH!n!
 =\frac{L(m!)^2}{(2H)!(m-H)!}.
\tag{1.6b}
\]

Thus \(D_{\rm tr}/R_{\rm tr}=L/\Lambda\), and all normalized pair and
external-influence formulas below are unchanged. A simple unoriented
middle edge has

\[
 \frac{R_{\rm tr}}R=\frac{2(3H)!}{(2H)!}
\tag{1.6c}
\]

full-tail extensions. These extensions can have different lower traces;
they may be collapsed for the middle matching audit but not for signed
fusion.

All regular degree formulas in this report use the union over every
admissible core. If one freezes one prescribed core \(Q_U\) at each top,
the rootwise simple middle degree becomes

\[
 R_{Q_U}=\frac{(m-H)!}{2\,H!},
\tag{1.6d}
\]

and a compatible root--owner codegree is \(L(m-2H)!/2\), but global
owner degrees need not remain transitive. Consequently the compensated
regular bite in Section 3 applies verbatim to the full selectable-core
catalogue; a frozen nonuniform core assignment needs a separate degree
regularization theorem.

### Theorem 1.2 (root--owner and owner--owner codegrees)

For a top \(U\) and middle owner \(X\),

\[
 d(U,X)=
 \begin{cases}
 \displaystyle\frac{LH!m!}{2(3H)!},&X\subset U,\\[1mm]
 0,&X\not\subset U.
 \end{cases}
\tag{1.7}
\]

Thus, for an incident pair,

\[
 \frac{d(U,X)}D=\frac1{\binom mH},\qquad
 \frac{d(U,X)}R=\frac L{\binom MH}.
\tag{1.8}
\]

The complete owner-pair sequence is (0.5), and its maximum is (0.6).

#### Proof

In the reduced decorated catalogue, fixing \(U\supset X\) removes only
the choice of the top from the middle-degree count, giving
\(Lm!/(2H)!\). Divide by (1.5) to obtain (1.7), and then cancel.

Let \(d=d_J(X,Y)\). A common top exists if and only if \(d\le H\), in
\(\binom{m-d}{H-d}\) ways. For \(d<H\), two prescribed omitted windows
overlap in \(H-d\) letters. Their starts differ by \(d\), giving two
orientations and \(L-d\) placements. Exact cancellation against (1.4)
gives

\[
 \frac{d(X,Y)}D=\frac{2(L-d)}{L\binom md^2}.
\]

For \(d=H\), the top is unique and the omitted windows are disjoint. The
number of unordered start pairs is

\[
 \sum_{g=H}^{L-1}(L-g)=\frac{(L-H)(L-H+1)}2.
\]

Double counting edge--pair incidences gives the second line of (0.5).
There is no common top for \(d>H\). The values for \(1\le d<H\) decrease
strictly with \(d\), the endpoint \(d=H\) is superpolynomially smaller,
and (0.6) follows. \(\square\)

## 2. Exact pair mass and external influence

For a middle owner \(X\notin e\), define

\[
 a_X(e)=|\{f:X\in f,\ f\cap e\ne\varnothing\}|.
\tag{2.1}
\]

### Lemma 2.1 (linear-path spheres)

If \(E=\{X_1,\ldots,X_L\}\) is one physical middle path, then, for
\(1\le d<H/2\),

\[
 |\{i:d_J(X,X_i)=d\}|\le2d+1.
\tag{2.2}
\]

For \(d=1\), three is attainable with \(X\notin E\).

#### Proof

Any two qualifying path vertices have mutual Johnson distance at most
\(2d\). Along the tight path,

\[
 d_J(X_i,X_j)=\min\{|i-j|,H\}.
\]

Since \(2d<H\), their indices lie in an interval of diameter at most
\(2d\). Three consecutive windows admit an external \(H\)-set differing
from each in one letter, proving sharpness at \(d=1\). \(\square\)

### Theorem 2.2 (sharp external influence)

Uniformly over all physical path edges \(e\) and all middle owners
\(X\notin e\),

\[
 \frac{a_X(e)}D
 \le\frac{6(L-1)}{Lm^2}+O(m^{-4}).
\tag{2.3}
\]

There are \(X,e\) attaining the right side up to \(O(m^{-4})\).

For a root \(V\) external to an edge rooted at \(U\),

\[
 \frac{a_V(e)}R\le\frac{HL}{\binom MH},
\tag{2.4}
\]

which is superpolynomially smaller than \(m^{-2}\).

#### Proof

A union bound gives

\[
 a_X(e)\le {\bf1}_{X\subset U}d(U,X)
       +\sum_{Y\in e\cap\mathcal X}d(X,Y).
\tag{2.5}
\]

The root term is a fraction \(1/\binom mH\) of \(D\). Lemma 2.1 and
(0.5) give at most three distance-one terms, totaling the main term in
(2.3). All shells \(d\ge2\) contribute \(O(Dm^{-4})\).

For the sharp example, the three distance-one pair-links have no common
option in adjacent pairs, because the distance-one graph of windows is a
path. Their remaining overlap is at most the distance-two codegree,
\(O(Dm^{-4})\). Inclusion--exclusion proves the lower bound.

For (2.4), put \(A=U\setminus V\ne\varnothing\). A path owner lies below
\(V\) only if its omitted \(H\)-window contains \(A\). At most \(H\)
windows do so; use the second ratio in (1.8). \(\square\)

For later use, fix an edge \(e\) and let every other root \(V\) choose a
uniform option. If \(p_V(e)\) is its probability of meeting \(e\), then

\[
 T_e:=\sum_{V\ne U}p_V(e)
 =\frac{L^2}{\Lambda}+O(1/m)=L\rho+O(1/m).
\tag{2.6}
\]

Indeed, the first incidence mass is exactly

\[
 F=L^2\left(\frac1\Lambda-\frac1{\binom MH}\right),
\tag{2.7}
\]

and Bonferroni loses at most

\[
 \frac2\Lambda\sum_{d=1}^{H-1}
 \frac{(L-d)^2}{\binom md^2}
 +\frac{((L-H)(L-H+1))^2}
 {2\Lambda\binom mH^2}
 =\frac{2+o(1)}m.
\tag{2.8}
\]

Thus (2.6) is uniform, not merely an average over paths.

## 3. An exact compensated RPRN bite

The compensation mechanism is abstract and exact.

### Theorem 3.1 (root/owner marginal compensation)

Let a rooted hypergraph have option classes \(\mathcal E_A\), one for
each root \(A\), and let \(w_A\) be a probability distribution on
\(\mathcal E_A\). Put

\[
 \lambda_X=\sum_A\sum_{e\in\mathcal E_A:X\in e}w_A(e),
\tag{3.1}
\]

and assume \(\lambda_X\le1\) for every owner \(X\).

Activate every root independently with probability \(a\), and let each
active root propose one option according to \(w_A\). For an option \(e\),
let \(S_e\) be its conditional probability of being owner-disjoint from
all other proposals. Fix

\[
 0<s_0\le\min_e S_e.
\tag{3.2}
\]

Retain an isolated proposal \(e\) with the additional probability
\(s_0/S_e\). Put \(h=as_0\). Then

\[
 \Pr(e\text{ is accepted})=h\,w_A(e),
\tag{3.3}
\]

every root is accepted with probability \(h\), and every owner is covered
with probability \(h\lambda_X\). The accepted options form a matching.

Afterwards, conditionally delete every uncovered owner \(X\) with
probability

\[
 \frac{h(1-\lambda_X)}{1-h\lambda_X}.
\tag{3.4}
\]

Then every owner, like every root, has total deletion probability exactly
\(h\).

#### Proof

Conditional isolation and the second thinning cancel:

\[
 a\,w_A(e)S_e\frac{s_0}{S_e}=h\,w_A(e).
\]

Isolated proposals are pairwise owner-disjoint. Summing (3.3) over the
one option class of a root gives \(h\). Summing it over the pairwise
disjoint accepted events through an owner gives \(h\lambda_X\). Finally,

\[
 h\lambda_X+(1-h\lambda_X)
 \frac{h(1-\lambda_X)}{1-h\lambda_X}=h.
\]

This proves every assertion. \(\square\)

If every option has \(L\) owners, the expected number of artificial owner
deletions in this bite is exactly

\[
 h\sum_X(1-\lambda_X)=h(|\mathcal X|-L|\mathcal A|).
\tag{3.5}
\]

Thus compensation spends only the genuine owner slack.

### Corollary 3.2 (initial common-core bite)

Use the uniform distribution on the simple options of every common-core
root, and set

\[
 a=\frac\gamma L,qquad \gamma>0\text{ fixed}.
\]

Then \(\lambda_X=\rho\) for every middle owner. Moreover, uniformly in
the proposed option,

\[
 S_e=\prod_{V\ne U}(1-a p_V(e))
     =e^{-\gamma\rho+o(1)}.
\tag{3.6}
\]

Theorem 3.1 therefore accepts the number of paths in (0.8), and its
expected artificial-deletion cost is

\[
 h(W-LN_H)=o(hW).
\tag{3.7}
\]

#### Proof

Exact regularity gives \(\lambda_X=D/R=\rho\). Equations (2.4) and
(2.6) give

\[
 \log S_e=-aT_e+O\left(a^2\sum_Vp_V(e)^2\right)
          =-\gamma\rho+o(1)
\]

uniformly. Now apply Theorem 3.1 and use
\(W-LN_H=(\Lambda-L)N_H=O(HN_H)=o(W)\). \(\square\)

This compensation is exact at the one-vertex marginal level. It is not a
hereditary theorem. Covering a \(1-o(1)\) fraction of the roots requires
\(\Theta(L)\) dependent bites, and no proof is known that the residual
option menus retain (2.3). A sparse, root-covering exceptional owner
family already refutes a stronger statewise regeneration statement based
only on original containment support. That construction does not refute
a high-probability theorem for the unbiased trajectory, nor the literal
residual-pair-link version. These quantifier limits are essential.

### Proposition 3.3 (conditional dynamic ledger)

Let \(\delta=1-\rho=\Theta(H/m)\). Run the compensated bite repeatedly,
using the current root distributions, and let \(z_t\) be the common
one-vertex survival scale. Suppose the following unproved dynamic
regeneration statement holds until the first time \(z_t\le z_*\):

1. after culling \(o(N_H)\) roots and \(o(W)\) owners, every current root
   and owner degree is within a multiplicative \(e^{\pm\delta/8}\) of
   predictable scales whose ratio keeps \(\lambda_X\le1\);
2. every residual external link obeys

   \[
   \frac{a_{v,t}(e)}{d_t(v)}\le\frac{C}{m^2z_t};
   \tag{3.8}
   \]

3. in a stopped exposure of each log degree, the conditional drift,
   quadratic variation, and maximum jump contributed by bite \(t\) are
   each \(O((m^2z_t)^{-1})\).

If

\[
 z_*=o(1),\qquad z_*\log m\longrightarrow\infty,
\tag{3.9}
\]

then the process chooses an owner-disjoint physical middle path at all but
\(o(N_H)\) roots. Assigning arbitrary paths to the remaining roots creates
only \(o(W)\) middle repeat mass.

#### Proof

Use a conservative bite with constant acceptance probability
\(h=\gamma(1-\gamma)/L\). The load hypothesis lets Theorem 3.1 apply at
every good step. Since \(z_{t+1}=(1-h)z_t\), geometric summation gives

\[
 \sum_{t<T}\frac{C}{m^2z_t}
 =O\left(\frac{L}{m^2z_*}\right)
 =O\left(\frac1{mz_*}\right).
\tag{3.10}
\]

On the other hand,

\[
 \delta^2=\Theta(\log m/m).
\]

Freedman's inequality at threshold \(\delta/8\) therefore has exponent
\(\Omega(z_*\log m)\). Under (3.9), the expected exceptional fraction in
each vertex shore is \(o(1)\), so some outcome has the stated cull sizes.
The uncaptured root fraction is at most \(z_*+o(1)=o(1)\). If \(s=o(N_H)\)
roots remain, arbitrary completion adds at most \(Ls=o(LN_H)=o(W)\)
middle repeats. \(\square\)

The ideal independent product residual has precisely the scale in (3.8):
conditioning on a vertex removes one survival factor and amplifies the
initial \(6/m^2\) influence by \(z^{-1}\). This validates the numerical
ledger, not the regeneration hypothesis. The latter is the exact middle
RPRN gate.

## 4. Interiorization of the nested signed traces

Return to a literal full tail

\[
 t_1,\ldots,t_s
\]

after the \(2H\)-core. The retained middle owners are

\[
 X_j=U\setminus\{t_{j+H},\ldots,t_{j+2H-1}\},
 \qquad1\le j\le L.
\tag{4.1}
\]

Whenever the displayed indices stay in \([1,L]\), the signed traces obey
the exact identities

\[
 T^+_{j,q}=X_j\cup X_{j+1}\cup\cdots\cup X_{j+q},
\tag{4.2}
\]

\[
 T^-_{j,q}=X_{j-q}\cap X_{j-q+1}\cap\cdots\cap X_j.
\tag{4.3}
\]

They follow by intersecting, respectively unioning, the consecutive
omitted \(H\)-windows.

For the separately feasible common-core threshold profile, put

\[
 b_0=L,
\]

and, for \(1\le q<H\),

\[
 b_q=\min\left\{L-1,
 \max\left\{0,\left\lfloor\frac{N_q}{N_H}\right\rfloor-1\right\}
 \right\}.
\tag{4.4}
\]

### Theorem 4.1 (floor-correct interior nested profile)

Define

\[
 \widetilde b_q=\min\{b_q,(L-2q)_+\}.
\tag{4.5}
\]

For every top there are nested active phase sets \(A_q\) such that

\[
 |A_q|=\widetilde b_q,qquad
 A_q\subseteq\{q+1,\ldots,L-q\},qquad
 A_{q+1}\subseteq A_q.
\tag{4.6}
\]

Moreover,

\[
 \sum_{q=1}^{H-1}(b_q-\widetilde b_q)=O(H).
\tag{4.7}
\]

Thus using (4.2)--(4.3) on both signs loses only

\[
 O(HN_H)=o(W)
\tag{4.8}
\]

aggregate signed occurrences.

#### Proof

Both sequences \(b_q\) and \((L-2q)_+\) are nonincreasing, hence so is
\(\widetilde b_q\). The domains in (4.6) are nested and have sizes
\(L-2q\). Starting at the largest nonempty depth and extending backwards
constructs the required nested subsets. They define legal phase tags by
\(\tau(j)=\max\{q:j\in A_q\}\).

If \(b_q>\widetilde b_q\), then \(b_q>L-2q\). Since
\(\Lambda=m+O(H)\), \(L=m-3H+1\), and

\[
 \frac{N_q}{N_H}
 =\Lambda\exp\left(-\frac{q^2}{m}
 +O\left(\frac q m+\frac{q^4}{m^3}\right)\right),
\tag{4.9}
\]

this inequality forces \(q^2=O(H+q)\), hence \(q=O(\sqrt H)\).
For such a depth the loss is at most \(2q\). Summing over
\(q=O(\sqrt H)\) gives (4.7). Doubling for the two signs proves (4.8),
because \(HN_H/W=O(H/m)=o(1)\). \(\square\)

Therefore the endpoint collars can be removed within the allowed
\(o(W)\) ledger. The remaining signed problem is the global coincidence
pattern of the unions and intersections in (4.2)--(4.3).

## 5. The exact active trace-influence gate

For a tagged path \(P_U\), let \(\tau_U(j)\) be the radius tag of phase
\(j\). At deletion length \(\ell\), put

\[
 q=|H-\ell|.
\]

For two paths, let \(c_{UV}^{\tau}(\ell)\) count equal length-\(\ell\)
targets whose two phases both have tag at least \(q\). Define

\[
 \Xi_\tau=\sum_{\{U,V\}}\sum_{\ell=1}^{2H}
 c_{UV}^{\tau}(\ell).
\tag{5.1}
\]

If \(A_r\) is the number of active occurrences at rank \(m+r\), put

\[
 B_r=\binom{2m}{m+r}=N_{|r|},\qquad
 \Delta=\sum_{r=-H}^H(B_r-A_r)_+.
\tag{5.2}
\]

### Theorem 5.1 (floor-correct trace defect bound)

Let \(e_r\) and \(h_r\) be, respectively, repeat excess and leave at
rank \(m+r\). Then

\[
 \boxed{
 \sum_{r=-H}^H(e_r+h_r)\le2\Xi_\tau+\Delta.}
\tag{5.3}
\]

Consequently

\[
 \Xi_\tau=o(W),\qquad\Delta=o(W)
\tag{5.4}
\]

is a complete deterministic sufficient condition for aggregate signed
overload plus leave \(o(W)\).

#### Proof

At a fixed rank, if \(\mu(T)\) is target load, then

\[
 e_r=\sum_T(\mu(T)-1)_+,qquad
 A_r-B_r=e_r-h_r.
\]

Hence

\[
 e_r+h_r=2e_r+B_r-A_r
 \le2e_r+(B_r-A_r)_+.
\]

Every equal pair of active occurrences belongs to two distinct top paths;
within one path all positive-deletion traces are distinct, while the
zero-deletion top rank has at most one active phase. Therefore
\(\sum_re_r\le\Xi_\tau\). Sum the last inequality over ranks. \(\square\)

For untagged paths, two tops \(U,V\), and their exclusive sets
\(A=U\setminus V,B=V\setminus U\), the exact collision normal form is

\[
 U\setminus I=V\setminus J
 \Longleftrightarrow
 I=A\mathbin{\dot\cup}K,quad J=B\mathbin{\dot\cup}K
\tag{5.5}
\]

for one common \(K\subseteq U\cap V\). Consequently, if
\(\operatorname{span}_U(A)\) is the shortest tail interval containing
\(A\),

\[
 c_{UV}(\ell)\le
 \min\{(\ell-\operatorname{span}_U(A)+1)_+,
       (\ell-\operatorname{span}_V(B)+1)_+\}\le\ell.
\tag{5.6}
\]

This is the exact two-path influence to be charged by a trace-aware
nibble. Middle owner incidence does not determine it.

## 6. A middle-disjoint local-reversal gadget

The following strengthens the full reversed-tail gadget: its two paths
have no common middle owner.

Fix coordinates \(a,b\), a set

\[
 C\in\binom{[2m]\setminus\{a,b\}}{M-1},
\]

and tops

\[
 U=C+\{a\},\qquad V=C+\{b\}.
\tag{6.1}
\]

Choose a common core \(Q\subset C\), \(|Q|=2H\), and let
\(\varphi:U\to V\) fix \(C\) and send \(a\) to \(b\). Put

\[
 p=2H,qquad h=\lfloor H/2\rfloor.
\tag{6.2}
\]

Choose a full \(U\)-tail \(w_1,\ldots,w_s\) with \(w_p=a\). On the
local block

\[
 \mathcal L=[p-h+1,p+h-1],
\tag{6.3}
\]

define the \(V\)-tail by reflection:

\[
 v_{p+t}=\varphi(w_{p-t}),\qquad |t|\le h-1.
\tag{6.4}
\]

### Theorem 6.1 (short collision saturation with zero middle collision)

The tail outside \(\mathcal L\) can be completed so that:

1. for every \(1\le\ell\le h\), the two paths have exactly \(\ell\)
   equal length-\(\ell\) targets; and
2. at deletion length \(H\), they have no equal target.

In particular, the two physical middle hyperedges are owner-disjoint.

#### Proof

For \(\ell\le h\), every length-\(\ell\) interval containing
\(a=w_p\) lies wholly in \(\mathcal L\). There are exactly \(\ell\) such
allowed intervals, with starts

\[
 p-\ell+1,\ldots,p.
\]

Reflection (6.4) sends each to the unique \(V\)-interval with set
\(\varphi(I)\). Equation (5.5) proves equality of the two targets and
also proves that no interval avoiding \(a\) can collide. Hence the count
is exactly \(\ell\), independently of the exterior completion.

It remains to choose that completion. Let

\[
 R_0=s-(2h-1)
\]

be the number of exterior tail positions and labels. Fill them by a
uniform random bijection. Fix an allowed \(V\)-side \(H\)-window \(J\)
containing \(p\), and let

\[
 t_J=|J\setminus\mathcal L|\ge1.
\]

For any fixed \(U\)-side \(H\)-window \(I\) containing \(p\), the event
that the two targets coincide either is impossible from the already fixed
local labels, or requires the labels in the \(t_J\) exterior positions of
\(J\) to equal one prescribed \(t_J\)-set. Its probability is
\(1/\binom{R_0}{t_J}\).

There are at most two windows \(J\) with \(t_J=1\); all others have
\(t_J\ge2\). There are \(H\) choices of \(I\) and \(H\) choices of
\(J\). Therefore the union of all bad middle-collision events has
probability at most

\[
 \frac{2H}{R_0}+\frac{H^2}{\binom{R_0}{2}}=o(1).
\tag{6.5}
\]

For all sufficiently large \(m\), some exterior completion avoids every
bad event. Equation (5.5) then proves that there is no middle collision.
\(\square\)

## 7. Linear signed amplification from an \(o(W)\) middle perturbation

The coordinate swap \(a\leftrightarrow b\) partitions all tops containing
exactly one of \(a,b\) into

\[
 P_m=\binom{2m-2}{M-1}
\tag{7.1}
\]

disjoint pairs, where

\[
 \frac{P_m}{N_H}
 =\frac{(m+H)(m-H)}{2m(2m-1)}=\frac14+o(1).
\tag{7.2}
\]

Fix a small constant \(c>0\) and use \(K\) from (0.10). Since
\(H^2=(1+o(1))m\log m\), one has \(K=o(N_H)\), so the required disjoint
top pairs exist.

### Theorem 7.1 (middle-safe-mass, signed-linear perturbation)

Assume a one-path-per-top family has middle overload plus leave
\(D_m=o(W)\). Replace its paths on \(K\) paired tops by the paths in
Theorem 6.1. Then the new middle overload plus leave is at most

\[
 D_m+4KL=D_m+O(W/\log m)=o(W).
\tag{7.3}
\]

Internally, each replacement pair has zero middle collision.

Put

\[
 q_0=H-h=\lceil H/2\rceil,
 \qquad q_1=\lfloor2H/3\rfloor.
\tag{7.4}
\]

Prescribe the following minimum tags on the first \(h\) phases of every
gadget path:

\[
 r_j=
 \begin{cases}
 q_1,&1\le j\le H-q_1,\\
 H-j,&H-q_1<j\le h.
 \end{cases}
\tag{7.4a}
\]

If every such phase receives a tag at least \(r_j\), then the aggregate
upper repeat excess satisfies

\[
 \sum_{q=q_0}^{q_1}e_q^+
 \ge K\sum_{q=q_0}^{q_1}(H-q)
 \ge\left(\frac c{42}+o(1)\right)W.
\tag{7.5}
\]

There are only

\[
 2Kh=O(W/H).
\tag{7.6}
\]

prescribed phase jobs. They fit the exact scalar SCD tag capacities below
\(H\). Indeed, with

\[
 \gamma_d=N_d-N_{d+1}
 =\frac{2d+1}{m+d+1}N_d,
\tag{7.7}
\]

one has, for every \(q_0\le q\le q_1\),

\[
 2K(H-q)
 \le \sum_{d=q}^{H-1}\gamma_d=N_q-N_H,
\tag{7.8}
\]

with polynomial slack. These nested inequalities are Hall's complete set
of cuts for assigning a job of minimum tag \(r_j\) to an exact tag class
\(d\ge r_j\).

#### Proof

Removing and inserting the \(2K\) old and new paths changes at most
\(4KL\) middle occurrences. Each single occurrence deletion or insertion
changes overload plus leave by at most one, proving (7.3).

At upper depth \(q\in[q_0,q_1]\), the deletion length is
\(\ell=H-q\le h\). Theorem 6.1 supplies exactly \(\ell\) collision pairs,
on the first \(\ell\) phases of each path. For \(j\le\ell=H-q\),
(7.4a) gives \(r_j\ge q\), so all are active. Distinct gadgets use
disjoint occurrences. If several duplicate
pairs land on one target, repeat excess can only increase relative to the
number of pairs. For all sufficiently large \(H\), there are at least
\(H/7\) depths in (7.4), and \(H-q\ge H/3\), so the sum in (7.5) is at
least \(KH^2/21\). Floors in (0.10) give the displayed constant.

Finally,

\[
 \frac{N_{q_1}}W
 =\exp\left(-\frac{q_1^2}{m}+o(\log m)\right)
 =m^{-4/9+o(1)}.
\]

Hence, uniformly for \(q_0\le q\le q_1\),

\[
 \frac{N_q-N_H}{W/H}
 \ge
 \frac{N_{q_1}-N_H}{W/H}
 =m^{1/18+o(1)}\sqrt{\log m}\longrightarrow\infty,
\]

whereas \(2K(H-q)=O(W/H)\). This proves every cut in (7.8), and
integral Hall gives the scalar tag assignment. \(\square\)

The scalar capacity in (7.8) lets one distribute the gadget phases among
exact tag classes below \(H\), so the one-tag-\(H\)-per-top restriction is
irrelevant. It does **not** by itself construct the remaining physical tag
assignment inside a fixed full SCD. Thus the untagged collision potential,
the zero internal middle collision, and the perturbation bound (7.3) are
unconditional given the base selection; the actual tagged lower bound
(7.5) is conditional on a legal compensation reservoir. This is the same
integrality distinction imposed by the frozen logic.

## 8. Consequence for the fusion programme

The physical common-core hypergraph has every favorable static middle
statistic currently requested:

* exact near-regular root and owner degrees;
* an exact symmetric fractional root factor;
* maximum relative pair codegree \((2+o(1))/m^2\);
* sharp external middle-link influence \((6+o(1))/m^2\); and
* an exact root/owner compensated first bite.

These facts do not yet produce a near-perfect middle path factor. The
missing middle theorem is hereditary regeneration, or an absorber, through
\(\Theta(L)\) dependent restrictions.

More decisively for the requested physical fusion, even a hypothetical
\(o(W)\)-defect middle theorem would not make the signed conclusion
formal. Theorem 7.1 concentrates only \(O(W/\log m)\) middle perturbation
mass on path pairs whose nested upper traces carry \(\Omega(W)\) repeat
mass. The two paths in each bad pair are themselves middle-disjoint. Thus
neither middle load, middle pair codegree, nor the compensated marginal
law controls the amplification.

For a partial selected family \(\mathcal P\), the exact incremental trace
charge of a new tagged path \(e\) is

\[
 \psi_\tau(e\mid\mathcal P)
 =\sum_{f\in\mathcal P}\sum_{\ell=1}^{2H}
 c_{ef}^{\tau}(\ell).
\tag{8.1}
\]

The cumulative sum of these charges is \(\Xi_\tau\). Therefore the exact
positive successor to middle RPRN is:

1. regenerate the compensated root/owner option distributions;
2. keep total cumulative charge \(\sum\psi_\tau=o(W)\);
3. keep the rankwise occurrence deficit \(\Delta=o(W)\); and
4. complete the unused masks and tags inside one integral SCD.

Theorem 5.1 would then give aggregate signed defect \(o(W)\). None of
items 1--4 is inferred from the separate-rank Hall or fractional cuts.

## 9. Proved and conditional boundary

Proved unconditionally:

1. all raw and normalized middle path degrees and pair codegrees;
2. the sharp \(6/m^2\) external middle-link influence;
3. the exact compensated one-bite lemma and its initial common-core
   asymptotics;
4. the floor-correct interior nested trace profile with \(o(W)\) loss;
5. the active trace-defect inequality (5.3);
6. the local-reversal gadget, including zero internal middle collision;
7. its \(O(W/\log m)\) middle perturbation and \(\Omega(W)\) untagged
   signed collision potential; and
8. the exact scalar high-tag capacity (7.8).

Conditional:

1. the actual tagged \(\Omega(W)\) repeat conclusion assumes a legal
   compensation reservoir for the remaining exact tag census.

Not proved:

1. hereditary middle-path regeneration or a matching missing
   \(o(N_H)\) roots;
2. a selected family with \(\Xi_\tau=o(W)\);
3. completion to one full SCD; or
4. the coefficient-one theorem.

The rigorous endpoint of this lane is therefore a separation theorem:
the common-core middle hypergraph admits a strong compensated first bite,
but middle \(o(W)\)-defect is not a sufficient invariant for nested
signed-trace fusion. A trace-weighted compensated nibble is genuinely
additional mathematics.
