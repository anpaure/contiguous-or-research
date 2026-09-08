# AD7: cross-component deep support, threading, and trace condensation

Date: 2026-07-25

## 0. Exact outcome

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil ,
\]

where \(A>0\) is fixed and \(2\le H\le m-1\).  All asymptotic
statements take \(m\to\infty\) with \(A\) fixed.

The missing cross-component theorem is **not proved** here.  Instead, this
report proves four exact advances which locate its remaining content more
sharply.

1. **Owner-marginal deep support is always feasible.**  Any oriented
   spanning linear forest whose lower and upper first-band colours each
   exhaust their complete rank admits an integral nested radius-\(H\) flag
   assignment which covers every target in every band rank.  The prescribed
   first-band colours stay at the same owners.  Thus, after forgetting
   chronology, the hole family can be made empty.
2. **Physical threading imposes an exact curvature law.**  If those lower
   chains are realized by one canonical MTF path forest with \(p\)
   components, their deletion-slot histograms \(D_1,\ldots,D_H\) obey
   \[
   \sum_{j=1}^{H-1}\|D_{j+1}-D_j\|_1\le2p(H-1).
   \]
   Equivalently, the point-incidence profiles of successive supported ranks
   have total discrete second variation at most \(2p(H-1)\).  For the exact
   odd factor \(p=W/(m+1)\), this is \(o_A(W)\).
3. **Trace compression requires superdense cross-depth alignment.**  For
   every marked set \(Z\), if \(M\) is the aggregate number of holes and
   \(E_Z^\times\) counts pairs of holes in different signed ranks with the
   same \(Z\)-trace, then
   \[
   \boxed{
   M-\Phi_Z
   \le\frac{E_Z^\times}{\nu(n-|Z|)}.}
   \tag{0.1}
   \]
   Hence \(M\ge cW\) and \(\Phi_Z=o(W)\) force
   \[
   E_Z^\times\ge(c-o(1))W\,\nu(n-|Z|).
   \tag{0.2}
   \]
   Almost all holes must in fact lie in trace cells populated at an
   unbounded number of signed depths.
4. **Global relabelling supplies none of this condensation.**  If
   \(W_n=\binom n{\lfloor n/2\rfloor}\), \(|\mathcal H|=M\le W_n\),
   \(|Z|=t\), and \(\sigma\) is uniform in \(S_n\), then
   \[
   \boxed{
   \mathbb E_\sigma\Phi_Z(\sigma\mathcal H)
   \ge
   M\left(
   1-\sqrt{\frac{t}{2n}\log\frac{2^n}{M}}
   \right).}
   \tag{0.3}
   \]
   Moreover,
   \[
   \min_{|Z|=t}\Phi_Z(\sigma\mathcal H)
   =
   \min_{|Z|=t}\Phi_Z(\mathcal H)
   \tag{0.4}
   \]
   for every fixed permutation \(\sigma\).  Thus an optimized marked set is
   exactly relabelling-invariant.  For \(cW\le M\le W\), a random
   relabelling with \(t=o(m/\log m)\) preserves essentially the entire raw
   cost; for \(M>W\), the proved conclusion is only
   \(\Phi_Z=\Omega(W)\).

A separate four-symbol construction gives three or four fully legal,
long-geodesic-embeddable endpoint flags whose ranks \(-1,0,+1\) are all
separately injective but whose every deeper signed flag coincides.  It gives
the sharp local signed \(H\)-fold Hall gaps \(H-7\) and \(2H-10\).
Therefore canonical legality, long components, componentwise injectivity,
and the three anchor injections supplied by the perfect first-band
partitions cannot by themselves prove the selected-support theorem.

The surviving theorem has two honest alternatives.  It may thread a
full-support owner-level flag flow through the shift/curvature law, in which
case there are no holes.  Or it may retain holes in a tail-assisted
chronology, in which case a deliberately correlated marked set must carry
the unbounded cross-depth trace multiplicity proved below.

No literal interval is altered in deriving these necessities.  No web
search, finite search, computation, fractional owner, or cross-factor
operation is used.

---

## 1. Static owner-level completion has zero holes

Let \(\mathcal F\) be an oriented spanning linear forest on
\(\binom{[2m]}m\).  Suppose it has

\[
e=N_1=\binom{2m}{m-1}
\tag{1.1}
\]

edges and satisfies:

* the masks \(X\cap Y\), over directed edges \(X\to Y\), are pairwise
  distinct;
* the masks \(X\cup Y\), over directed edges \(X\to Y\), are pairwise
  distinct.

Because both colour ranks have size \(N_1\), each displayed colour family
is its whole rank.  The number of path components is exactly

\[
p=W-e=W-N_1=\frac{W}{m+1}.
\tag{1.2}
\]

### Lemma 1.1 — small central families have an SDR of facets

If

\[
\mathcal A\subseteq\binom{[2m]}m,
\qquad |\mathcal A|\le\frac W2,
\]

then its lower shadow satisfies

\[
|\partial\mathcal A|\ge|\mathcal A|.
\tag{1.3}
\]

Consequently the incidence graph between the members of \(\mathcal A\) and
their rank-\((m-1)\) facets has a matching saturating \(\mathcal A\).

#### Proof

Write \(|\mathcal A|=\binom xm\) in the generalized-binomial
parametrization.  Since

\[
|\mathcal A|
\le\frac12\binom{2m}{m}
=\binom{2m-1}{m},
\]

one has \(x\le2m-1\).  The Lovász form of the
Kruskal--Katona theorem gives

\[
|\partial\mathcal A|
\ge\binom{x}{m-1}.
\]

Moreover,

\[
\frac{\binom{x}{m-1}}{\binom xm}
=\frac{m}{x-m+1}\ge1.
\]

This proves (1.3).  Every subfamily of \(\mathcal A\) also has size at most
\(W/2\), so (1.3) is precisely Hall's condition.  \(\square\)

### Lemma 1.2 — one-step complete-layer routing

For \(1\le r\le m\), there is an injection

\[
\iota_r:
\binom{[2m]}{r-1}\longrightarrow\binom{[2m]}r
\]

such that \(S\subset\iota_r(S)\) for every \(S\).  Dually, for
\(m\le r<2m\), there is an injection from rank \(r+1\) into rank \(r\)
along reverse containments.

#### Proof

Any symmetric-chain decomposition of the Boolean lattice matches each set
below the middle to its successor on its chain.  Complementation gives the
dual assertion.  \(\square\)

### Theorem 1.3 — exact owner-marginal saturated completion

For every \(1\le H\le m-1\), one can assign to every middle owner \(T\) an
integral saturated pair of chains

\[
F^-_{T,H}\subset\cdots\subset F^-_{T,1}\subset T
\subset F^+_{T,1}\subset\cdots\subset F^+_{T,H},
\tag{1.4}
\]

where

\[
|F^-_{T,q}|=m-q,\qquad |F^+_{T,q}|=m+q,
\tag{1.5}
\]

such that:

1. for every directed edge \(X\to Y\),
   \[
   F^-_{X,1}=X\cap Y,\qquad
   F^+_{Y,1}=X\cup Y;
   \tag{1.6}
   \]
2. for every \(1\le q\le H\),
   \[
   \{F^-_{T,q}:T\in\binom{[2m]}m\}
   =\binom{[2m]}{m-q},
   \tag{1.7}
   \]
   and
   \[
   \{F^+_{T,q}:T\in\binom{[2m]}m\}
   =\binom{[2m]}{m+q},
   \tag{1.8}
   \]
   where equality denotes support equality and repetitions are allowed.
3. Every individual flag (1.4) is literal at one shared right endpoint in a
   \(2H+1\)-letter word.

At depth one, on each sign, the exact floor is

\[
c_1=\left\lfloor\frac{W}{N_1}\right\rfloor=1,
\qquad
r_1=W-c_1N_1=\frac{W}{m+1};
\tag{1.8a}
\]

exactly \(r_1\) targets have load \(2\), and all others have load \(1\).
No floor/ceiling assertion is made here for \(q\ge2\).

In particular the static hole family is empty at every signed depth.

#### Proof

Every nonterminal owner already has its prescribed lower rank-\((m-1)\)
flag, and those \(e=N_1\) flags exhaust rank \(m-1\) exactly once.  There
are \(p=W/(m+1)\le W/2\) terminal owners.  Apply Lemma 1.1 to this terminal
family and choose pairwise distinct facets for them.  These extra facets
may duplicate prescribed edge colours, but only once each.  Thus every
rank-\((m-1)\) target has positive load.

Complement the \(p\) initial owners and apply the same lemma.  This chooses
pairwise distinct rank-\((m+1)\) supersets at the initial owners.  Together
with the prescribed incoming upper edge colours, every rank-\((m+1)\)
target has positive load.

Now suppose the lower flags at rank \(r\le m-1\) have been chosen, are
nested at their owners, and cover every \(r\)-set.  Regard the \(W\)
owners as labelled tokens located at their current \(r\)-sets.  Use
Lemma 1.2 to inject every \((r-1)\)-set \(S\) into a distinct containing
\(r\)-set \(\iota_r(S)\).  Each image contains at least one token.  Send one
such token down to \(S\).  Send every remaining token to an arbitrary
facet of its current set.  All moves are integral cover relations, and
every \((r-1)\)-set receives a token.  Iterating reaches rank \(m-H\).

The complementary upward procedure, beginning with the already fixed
rank-\((m+1)\) flags, reaches rank \(m+H\).  The two constructions alter
neither the middle owners nor the prescribed first-band flags.  This proves
(1.4)--(1.8).

For local literalization, write

\[
d_q(T)=F^-_{T,q-1}\setminus F^-_{T,q},
\qquad
a_q(T)=F^+_{T,q}\setminus F^+_{T,q-1},
\]

with \(F^-_{T,0}=F^+_{T,0}=T\).  These are singletons.  Reverse-write the
useful blocks as

\[
a_H,\ldots,a_1,d_1,\ldots,d_H,F^-_{T,H}.
\tag{1.9}
\]

Its augmented last-occurrence prefix is

\[
\bigl(
F^-_{T,H},d_H,\ldots,d_1,a_1,\ldots,a_H
\bigr).
\]

Every flag in (1.4) is therefore a literal suffix OR with the same right
endpoint.  \(\square\)

### Exact scope

Theorem 1.3 is deliberately an owner-marginal theorem.  It proves that
integrality, nestedness, the two perfect first-band colour ledgers, and
rankwise support admit a simultaneous solution.  It does **not** order the
owners into MTF-compatible paths.  The missing condition is the threading
law proved next.

There is nevertheless an exact cross-depth Hall condition on every proposed
owner assignment.

For a lower flag system, define the deepest load

\[
\mu_H^-(L)=|\{T:F^-_{T,H}=L\}|,
\qquad L\in\binom{[2m]}{m-H}.
\tag{1.10}
\]

For
\(\mathcal A\subseteq\binom{[2m]}{m-H}\), put

\[
\mu_H^-(\mathcal A)=\sum_{L\in\mathcal A}\mu_H^-(L)
\tag{1.11}
\]

and let

\[
\nabla^{H-q}\mathcal A
=
\left\{
S\in\binom{[2m]}{m-q}:
L\subseteq S\text{ for some }L\in\mathcal A
\right\}.
\tag{1.12}
\]

### Theorem 1.4 — exact deepest-load shadow deficiency

Let \(M_q^-\) be the number of unsupported rank-\((m-q)\) lower targets.
Then, for every \(0\le q\le H\),

\[
\boxed{
M_q^-
\ge
\Delta_q^-(\mu_H^-),}
\tag{1.13}
\]

where

\[
\boxed{
\Delta_q^-(\mu)
:=
\max_{\mathcal A\subseteq\binom{[2m]}{m-H}}
\left[
\mu(\mathcal A)
-|\nabla^{H-q}\mathcal A|
-(W-N_q)
\right]_+.}
\tag{1.14}
\]

At the deepest rank,

\[
\boxed{
\Delta_H^-(\mu_H^-)=M_H^-.}
\tag{1.15}
\]

At the middle rank, distinct middle ownership gives

\[
\boxed{\Delta_0^-(\mu_H^-)=0.}
\tag{1.16}
\]

Dually, if \(\mu_H^+\) is the load on rank-\((m+H)\) upper flags and
\(\partial^{H-q}\mathcal B\) is the rank-\((m+q)\) lower shadow of
\(\mathcal B\subseteq\binom{[2m]}{m+H}\), then

\[
\boxed{
\Delta_q^+(\mu)
:=
\max_{\mathcal B\subseteq\binom{[2m]}{m+H}}
\left[
\mu(\mathcal B)
-|\partial^{H-q}\mathcal B|
-(W-N_q)
\right]_+.}
\tag{1.17}
\]

It satisfies

\[
\boxed{
M_q^+
\ge\Delta_q^+(\mu_H^+).}
\tag{1.18}
\]

Moreover,

\[
\boxed{
\Delta_H^+(\mu_H^+)=M_H^+,
\qquad
\Delta_0^+(\mu_H^+)=0.}
\tag{1.19}
\]

#### Proof

Fix \(\mathcal A\).  The \(\mu_H^-(\mathcal A)\) endpoints whose deepest
cores lie in \(\mathcal A\) have rank-\((m-q)\) flags in
\(\nabla^{H-q}\mathcal A\).  The other \(W-\mu_H^-(\mathcal A)\)
endpoints contribute at most that many further distinct targets.  Hence

\[
|\mathcal S_q^-|
\le
|\nabla^{H-q}\mathcal A|
+W-\mu_H^-(\mathcal A).
\]

Subtract from \(N_q\), take the positive part, and maximize over
\(\mathcal A\).  This proves (1.13)--(1.14).

For \(q=H\), let \(\mu=\mu_H^-\) and let

\[
E=\sum_L(\mu(L)-1)_+.
\]

Since \(\sum_L\mu(L)=W\), while exactly \(M_H^-\) targets have load zero,

\[
E-M_H^-=W-N_H.
\tag{1.20}
\]

Also

\[
\max_{\mathcal A}\bigl(\mu(\mathcal A)-|\mathcal A|\bigr)=E,
\]

by taking precisely the targets of load at least \(2\).  Equations
(1.14) and (1.20) give (1.15).

For \(q=0\), map every endpoint to its distinct middle owner containing
its deepest core.  This is a matching from the cloned deepest cores into
their rank-\(m\) upper shadow, so
\(\mu(\mathcal A)\le|\nabla^H\mathcal A|\) for every \(\mathcal A\).
Since \(N_0=W\), (1.16) follows.  Complementation proves
(1.18)--(1.19).
\(\square\)

For the useful-prefix trace functional on depths \(2,\ldots,H\), the
rankwise trace sandwich gives the immediate necessary condition

\[
\boxed{
\Phi_Z(\mathcal H_{\ge2})
\ge
\max_{\substack{2\le q\le H\\\epsilon\in\{-,+\}}}
\Delta_q^\epsilon.}
\tag{1.21}
\]

Thus near-surjective deepest support alone is insufficient: the complete
deepest load, including its duplicate mass above the exact baseline
\(W-N_H\), must pass every intermediate Boolean-shadow cut.

---

## 2. Exact MTF threading and point-profile curvature

Let the \(W\) middle owners be partitioned into \(p\) directed paths.  At
each owner \(v\), write its canonical lower chain as

\[
F^-_{v,q}
=T_v\setminus\{d_1(v),\ldots,d_q(v)\},
\qquad 1\le q\le H,
\tag{2.1}
\]

where terminal future slots are supplied by one fixed legal dummy
continuation.  For a coordinate \(x\), define

\[
D_j(x)=|\{v:d_j(v)=x\}|,
\tag{2.2}
\]

and define the point-incidence profile

\[
I_q(x)=|\{v:x\in F^-_{v,q}\}|,
\qquad I_0(x)=|\{T:x\in T\}|=\frac W2.
\tag{2.3}
\]

### Theorem 2.1 — exact shift and boundary restitution

If \(v\to w\) is an actual canonical MTF path edge, then

\[
d_j(w)=d_{j+1}(v),
\qquad 1\le j<H.
\tag{2.4}
\]

Let \(\sigma_j(x)\) count source vertices \(w\) with \(d_j(w)=x\), and let
\(\tau_j(x)\) count terminal vertices \(v\) with \(d_j(v)=x\).  Then

\[
\boxed{
D_{j+1}-D_j=\tau_{j+1}-\sigma_j}
\qquad(1\le j<H).
\tag{2.5}
\]

Consequently,

\[
\boxed{
\|D_{j+1}-D_j\|_1\le2p,}
\tag{2.6}
\]

and

\[
\boxed{
\sum_{j=1}^{H-1}\|D_{j+1}-D_j\|_1
\le2p(H-1).}
\tag{2.7}
\]

#### Proof

Along a canonical path with departure sequence \(p_i\),

\[
d_j(T_i)=p_{i+j-1}.
\]

Therefore

\[
d_j(T_{i+1})=p_{i+j}=d_{j+1}(T_i),
\]

which proves (2.4), including transitions whose later slot uses the fixed
dummy continuation.

The path edges biject nonterminal vertices with nonsource vertices.
Under this bijection, (2.4) identifies the \(D_{j+1}\)-contribution of
every nonterminal vertex with the \(D_j\)-contribution of its successor.
Only terminal contributions to \(D_{j+1}\) and source contributions to
\(D_j\) remain, giving (2.5).  Both boundary histograms have total mass
\(p\), so the triangle inequality gives (2.6).  Summing gives (2.7).
\(\square\)

### Corollary 2.2 — exact point-incidence curvature

For every \(1\le j\le H\),

\[
D_j=I_{j-1}-I_j
\tag{2.8}
\]

coordinatewise.  Hence

\[
\boxed{
\sum_{j=1}^{H-1}
\|I_{j-1}-2I_j+I_{j+1}\|_1
\le2p(H-1).}
\tag{2.9}
\]

For the exact odd factor,

\[
p=\frac{W}{m+1},
\]

and therefore, at \(H=\lceil A\sqrt m\rceil\),

\[
2p(H-1)
=\frac{2(H-1)W}{m+1}
=o_A(W).
\tag{2.10}
\]

#### Proof

At an owner, the coordinate removed between depths \(j-1\) and \(j\) is
exactly \(d_j(v)\), proving (2.8).  Substitute (2.8) into (2.7).
\(\square\)

Thus any zero-hole owner-level completion cleanly threaded on this
\(p\)-component canonical forest must be selected from the much smaller
class whose point-incidence profiles have \(o(W)\) total curvature.  The
recursive Hall routing in Theorem 1.3 does not enforce this constraint.

The lower shift is forced on every directly threaded canonical path.  A
clean two-sided threading has a stronger exact invariant.  Write

\[
a_j(v)=F^+_{v,j}\setminus F^+_{v,j-1},
\qquad
A_j(x)=|\{v:a_j(v)=x\}|.
\tag{2.11}
\]

### Theorem 2.3 — exact two-sided boundary curvature

Assume that every path edge \(v\to w\) obeys the clean direct-compatibility
laws

\[
d_j(w)=d_{j+1}(v)\quad(1\le j<H),
\tag{2.12}
\]

\[
a_1(w)=d_1(v),
\tag{2.13}
\]

and

\[
a_{j+1}(w)=a_j(v)\quad(1\le j<H).
\tag{2.14}
\]

For each path with source \(f\) and terminal vertex \(\ell\), one has the
exact signed identities

\[
\boxed{
D_{j+1}-D_j
=
\sum_{\rm paths}
\bigl(e_{d_{j+1}(\ell)}-e_{d_j(f)}\bigr),}
\tag{2.15}
\]

\[
\boxed{
A_1-D_1
=
\sum_{\rm paths}
\bigl(e_{a_1(f)}-e_{d_1(\ell)}\bigr),}
\tag{2.16}
\]

and

\[
\boxed{
A_{j+1}-A_j
=
\sum_{\rm paths}
\bigl(e_{a_{j+1}(f)}-e_{a_j(\ell)}\bigr).}
\tag{2.17}
\]

Thus

\[
\boxed{
\mathfrak V_H
:=
\sum_{j=1}^{H-1}\|D_{j+1}-D_j\|_1
+\|A_1-D_1\|_1
+\sum_{j=1}^{H-1}\|A_{j+1}-A_j\|_1
\le2(2H-1)p.}
\tag{2.18}
\]

In particular,

\[
\boxed{
p\ge
\left\lceil
\frac{\mathfrak V_H}{2(2H-1)}
\right\rceil.}
\tag{2.19}
\]

#### Proof

Sum (2.12) along every path.  Every internal contribution cancels, leaving
the terminal \(d_{j+1}\) symbol and the negative source \(d_j\) symbol.
This proves (2.15).  The same telescoping with (2.13) and (2.14) proves
(2.16)--(2.17), including one-vertex paths.  Every right side is the
difference of two histograms of mass \(p\), so each of the \(2H-1\)
displayed norms is at most \(2p\).  This gives (2.18)--(2.19).
\(\square\)

If these \(p\) clean runs are independently useful-prefix initialized,
their exact length is \(W+2Hp\).  Therefore

\[
\boxed{
L_{\rm ind}
\ge
W+2H
\left\lceil
\frac{\mathfrak V_H}{2(2H-1)}
\right\rceil.}
\tag{2.20}
\]

Here \(L_{\rm ind}=W+2Hp\) denotes the independently initialized clean-run
word.  Thus (2.20) is an exact obstruction to clean canonical threading,
not to arbitrary useful-prefix portals.  A refined inherited tail can
recruit a singleton after deletion and thereby start a new useful prefix
without satisfying (2.13)--(2.14).  No lower bound for that broader
mechanism is claimed.

---

## 3. Exact trace-condensation energy

This section is finite and does not assume an exact factor.  Let
\(\mathcal H\) be a family of distinct holes, partitioned by their distinct
signed-rank layers:

\[
\mathcal H=\bigsqcup_{\alpha\in\mathcal A}\mathcal H_\alpha.
\tag{3.1}
\]

Let \(Z\subsetneq[n]\), put

\[
t=|Z|,\qquad d=n-t\ge1,
\]

and, for \(R\subseteq Z\), define

\[
h_{\alpha,R}
=|\{S\in\mathcal H_\alpha:S\cap Z=R\}|,
\qquad
h_R=\sum_\alpha h_{\alpha,R}.
\tag{3.2}
\]

Put

\[
\ell_R=\nu(d)+\mathbf1_{R\ne\varnothing},
\qquad
M=|\mathcal H|=\sum_Rh_R,
\tag{3.3}
\]

so the fixed-trace repair functional is

\[
\Phi_Z(\mathcal H)=\sum_{R\subseteq Z}\min\{h_R,\ell_R\}.
\tag{3.4}
\]

### Proposition 3.1 — exact saturated-trace decomposition

Let

\[
\mathcal A_Z=\{R\subseteq Z:h_R>\ell_R\}.
\tag{3.5}
\]

Then

\[
\boxed{
\Phi_Z
=\sum_{R\in\mathcal A_Z}\ell_R
+\sum_{R\notin\mathcal A_Z}h_R,}
\tag{3.6}
\]

and

\[
\boxed{
M-\Phi_Z
=\sum_R(h_R-\ell_R)_+.}
\tag{3.7}
\]

In particular, \(\Phi_Z=o(W)\) holds exactly when both the cap mass on
saturated traces and the raw mass on unsaturated traces are \(o(W)\).

#### Proof

Split the minimum in (3.4) according to (3.5).  \(\square\)

Define the cross-rank same-trace energy

\[
E_Z^\times
=\sum_{R\subseteq Z}E_R^\times,
\qquad
E_R^\times
=\sum_{\alpha<\beta}h_{\alpha,R}h_{\beta,R}.
\tag{3.8}
\]

### Lemma 3.2 — sharp capped cross-product inequality

If \(L>0\) and \(0\le x_i\le L\), then

\[
\boxed{
\sum_{i<j}x_ix_j
\ge L\left(\sum_i x_i-L\right)_+.}
\tag{3.9}
\]

#### Proof

Scale to \(L=1\) and put \(x=\sum_i x_i\).  The assertion is trivial for
\(x\le1\).  If \(x=k+r\), where \(k=\lfloor x\rfloor\ge1\) and
\(0\le r<1\), convexity shows that \(\sum_i x_i^2\) is maximized by
\(k\) entries equal to \(1\), one entry equal to \(r\), and all others
zero.  Therefore

\[
\sum_{i<j}x_ix_j
=\frac{x^2-\sum_i x_i^2}{2}
\ge\frac{(k+r)^2-k-r^2}{2}
=\frac{k(k-1)}2+kr.
\]

The last expression minus \(x-1\) is

\[
\frac{(k-1)(k-2)}2+r(k-1)\ge0.
\]

Rescaling proves (3.9).  \(\square\)

### Theorem 3.3 — trace envelope and cross-rank energy obstruction

For every hole family and every proper marked set \(Z\),

\[
\boxed{
\Phi_Z(\mathcal H)
\ge\sum_R\max_\alpha h_{\alpha,R},}
\tag{3.10}
\]

and

\[
\boxed{
M-\Phi_Z(\mathcal H)
\le
\sum_R\frac{E_R^\times}{\ell_R}
\le
\frac{E_Z^\times}{\nu(d)}.}
\tag{3.11}
\]

Equivalently,

\[
\boxed{
\Phi_Z(\mathcal H)
\ge M-\frac{E_Z^\times}{\nu(d)}.}
\tag{3.12}
\]

#### Proof

If the layer \(\mathcal H_\alpha\) has rank \(r_\alpha\), then

\[
h_{\alpha,R}
\le
\binom d{r_\alpha-|R|}
\le
\binom d{\lfloor d/2\rfloor}
\le\nu(d)
\le\ell_R.
\tag{3.13}
\]

We use the convention \(\binom ds=0\) for
\(s\notin\{0,\ldots,d\}\), and set
\(\max_\alpha h_{\alpha,R}=0\) when the layer family is empty.

Also \(h_{\alpha,R}\le h_R\).  Hence

\[
\max_\alpha h_{\alpha,R}
\le\min\{h_R,\ell_R\},
\]

and summing proves (3.10).

Apply Lemma 3.2 with \(x_i=h_{\alpha,R}\) and \(L=\ell_R\).  It gives

\[
(h_R-\ell_R)_+
\le\frac{E_R^\times}{\ell_R}.
\]

Sum this inequality and use (3.7).  Finally
\(\ell_R\ge\nu(d)\), proving (3.11)--(3.12).  \(\square\)

### Corollary 3.4 — necessary superdense collision resource

If, along a sequence of instances,

\[
M\ge cW
\tag{3.14}
\]

for a fixed \(c>0\), while

\[
\Phi_Z(\mathcal H)=o(W),
\tag{3.15}
\]

then

\[
\boxed{
E_Z^\times
\ge(c-o(1))W\,\nu(d).}
\tag{3.16}
\]

Thus a linear aggregate hole family can be compressed only if it has a
superdense family of cross-depth pairs with identical \(Z\)-trace.

#### Proof

Rearrange (3.11):

\[
E_Z^\times\ge\nu(d)(M-\Phi_Z).
\]

Use (3.14)--(3.15).  \(\square\)

### Corollary 3.5 — unbounded-depth alignment is necessary

For a real \(B\ge1\), put

\[
\mathcal G_B(Z)=\{R:h_R>B\ell_R\}.
\tag{3.17}
\]

Then

\[
\boxed{
\sum_{R\notin\mathcal G_B(Z)}h_R
\le B\Phi_Z.}
\tag{3.18}
\]

Every trace in \(\mathcal G_B(Z)\) contains holes from at least

\[
\boxed{\lfloor B\rfloor+1}
\tag{3.19}
\]

distinct signed-rank layers.

Consequently, if \(M=\Omega(W)\), \(\Phi_Z=o(W)\), and the number of band
layers tends to infinity, there is a choice \(B_m\to\infty\) for which all
but \(o(W)\) holes lie in trace cells meeting at least
\(\lfloor B_m\rfloor+1\) distinct signed depths.

#### Proof

If \(R\notin\mathcal G_B(Z)\), then

\[
h_R\le B\min\{h_R,\ell_R\}.
\]

Summing proves (3.18).  By (3.13), a single layer contributes at most
\(\ell_R\) holes to trace \(R\).  Thus \(h_R>B\ell_R\) requires more than
\(B\) nonempty layers, proving (3.19).

If \(a_m=\Phi_Z/W\to0\), choose, for example,
\(B_m=a_m^{-1/2}\) whenever \(a_m>0\).  Under \(M=\Omega(W)\), eventually
\(a_m>0\).  Then \(B_m\to\infty\) and \(B_m\Phi_Z=o(W)\).  Apply (3.18).
\(\square\)

This rules out bounded-depth trace packets as an explanation of
\(\Phi_Z=o(W)\) when the raw aggregate hole mass is linear.

### Proposition 3.6 — exact permutation kernel for trace collisions

Fix a \(t\)-set \(Z\), and let \(\sigma\) be uniform in \(S_n\).  Then

\[
\boxed{
\mathbb E_\sigma E_Z^\times(\sigma\mathcal H)
=
\sum_{\alpha<\beta}
\sum_{\substack{S\in\mathcal H_\alpha\\T\in\mathcal H_\beta}}
\frac{\binom{n-|S\triangle T|}{t}}{\binom nt}.}
\tag{3.20}
\]

The numerator is interpreted as zero when \(t>n-|S\triangle T|\).

Consequently, suppose \(M\ge cW\), and put

\[
\varepsilon_m
=
\frac{\mathbb E_\sigma E_Z^\times(\sigma\mathcal H)}
{W\nu(n-t)}
\longrightarrow0,
\qquad
\rho_m=\sqrt{\varepsilon_m}.
\]

Then

\[
\boxed{
\mathbb P_\sigma\!\left\{
\Phi_Z(\sigma\mathcal H)<(c-\rho_m)W
\right\}
\le\rho_m.}
\tag{3.21}
\]

with probability \(1-o(1)\).

#### Proof

The traces of \(\sigma S\) and \(\sigma T\) on \(Z\) are equal exactly
when

\[
\sigma^{-1}Z\cap(S\triangle T)=\varnothing.
\]

The preimage \(\sigma^{-1}Z\) is a uniform \(t\)-set, so the probability
of equality is the displayed binomial ratio.  Sum the corresponding pair
indicators to prove (3.20).

Markov's inequality gives

\[
\mathbb P_\sigma\!\left\{
E_Z^\times>\rho_mW\nu(n-t)
\right\}
\le\rho_m.
\]

Outside this event, (3.12) and \(M\ge cW\) give
\(\Phi_Z\ge(c-\rho_m)W\), proving (3.21).  \(\square\)

### Corollary 3.7 — deterministic cylinder-concentration gate

For \(0\le t<n\) and \(M>0\), define

\[
\kappa_t(\mathcal H)
=
\max_{\substack{|Z|=t\\R\subseteq Z}}
|\{S\in\mathcal H:S\cap Z=R\}|.
\tag{3.22}
\]

Then every \(t\)-set \(Z\) satisfies

\[
\boxed{
\Phi_Z(\mathcal H)
\ge
M\min\left\{
1,\frac{\nu(n-t)}{\kappa_t(\mathcal H)}
\right\}.}
\tag{3.23}
\]

Hence \(M=\Omega(W)\) and \(\Phi_Z=o(W)\) force

\[
\frac{\kappa_t(\mathcal H)}{\nu(n-t)}\longrightarrow\infty
\tag{3.24}
\]

for some specially correlated trace cylinder.

#### Proof

For every trace, \(h_R\le\kappa_t(\mathcal H)\) and
\(\ell_R\ge\nu(n-t)\).  Therefore

\[
\min\{h_R,\ell_R\}
\ge
h_R\min\left\{
1,\frac{\nu(n-t)}{\kappa_t(\mathcal H)}
\right\}.
\]

Sum over \(R\).  \(\square\)

---

## 4. Coordinate averaging cannot create trace condensation

Continue to use natural logarithms.  Put

\[
W_j=\binom j{\lfloor j/2\rfloor}.
\tag{4.1}
\]

### Lemma 4.1 — exact central-mass monotonicity

The sequence \(2^{-j}W_j\) is nonincreasing.  Consequently, for
\(d=n-t\),

\[
W_d\ge2^{-t}W_n.
\tag{4.2}
\]

#### Proof

For \(s\ge1\),

\[
\frac{W_{2s-1}}{2^{2s-1}}
=\frac{W_{2s}}{2^{2s}},
\]

whereas

\[
\frac{W_{2s+1}}{2^{2s+1}}
=\frac{2s+1}{2s+2}\,
\frac{W_{2s}}{2^{2s}}.
\]

The multiplier \((2s+1)/(2s+2)\) is less than one.  Iterate.
\(\square\)

### Theorem 4.2 — universal entropy lower bound

Let \(\mathcal H\subseteq2^{[n]}\) be a family of \(M\) distinct sets with

\[
1\le M\le W_n.
\tag{4.3}
\]

Fix a deterministically chosen \(Z\subset[n]\) with \(|Z|=t<n\), and let
\(\sigma\) be uniformly random in \(S_n\).  Then

\[
\boxed{
\mathbb E_\sigma\Phi_Z(\sigma\mathcal H)
\ge
M\left(
1-\delta_{n,t,M}
\right),}
\tag{4.4}
\]

where

\[
\boxed{
\delta_{n,t,M}
=
\sqrt{\frac{t}{2n}\log\frac{2^n}{M}}.}
\tag{4.5}
\]

More precisely, for every \(\eta>0\),

\[
\boxed{
\mathbb P_\sigma\!\left(
\Phi_Z(\sigma\mathcal H)<(1-\eta)M
\right)
\le\frac{\delta_{n,t,M}}{\eta}.}
\tag{4.6}
\]

#### Proof

Let \(X\) be uniform on \(\mathcal H\).  For a uniformly random
\(t\)-set \(Y\subset[n]\), Shearer's projection inequality gives

\[
\mathbb E_Y H(X\cap Y)
\ge\frac tn H(X)
=\frac tn\log M.
\tag{4.7}
\]

Let \(p_Y\) be the law of \(X\cap Y\) on \(2^Y\), and let \(u_Y\) be
uniform on \(2^Y\).  Then

\[
D(p_Y\|u_Y)=t\log2-H(X\cap Y).
\]

Therefore

\[
\mathbb E_YD(p_Y\|u_Y)
\le\frac tn\log\frac{2^n}{M}.
\tag{4.8}
\]

Pinsker's inequality and Jensen's inequality yield

\[
\mathbb E_Y\|p_Y-u_Y\|_{\rm TV}
\le\delta_{n,t,M}.
\tag{4.9}
\]

For a fixed \(Y\), write \(h_R=M p_Y(R)\).  By (4.2), (4.3), and
Sperner's lower bound,

\[
\ell_R\ge\nu(d)\ge W_d\ge\frac{M}{2^t}.
\tag{4.10}
\]

Hence

\[
\begin{aligned}
M-\Phi_Y(\mathcal H)
&=\sum_R(h_R-\ell_R)_+\\
&\le\sum_R(h_R-W_d)_+\\
&\le M\sum_R(p_Y(R)-2^{-t})_+\\
&=M\|p_Y-u_Y\|_{\rm TV}.
\end{aligned}
\tag{4.11}
\]

A uniform \(\sigma\) makes \(Y=\sigma^{-1}Z\) a uniform \(t\)-set, with
only an irrelevant relabelling of trace coordinates.  Taking expectations
in (4.11) and using (4.9) proves (4.4).  Equation (4.6) follows from
Markov's inequality applied to \(M-\Phi_Z\).  \(\square\)

If \(M>W_n\), apply Theorem 4.2 to any \(W_n\)-element subfamily and use
monotonicity of \(\Phi_Z\) under enlargement of the hole family.

### Corollary 4.3 — slowly growing marked sets are generically useless

Let \(n=2m\), so \(W_n=W\), and suppose

\[
cW\le M\le W
\tag{4.12}
\]

for a fixed \(c>0\).  If

\[
t=o\left(\frac{m}{\log m}\right),
\tag{4.13}
\]

then

\[
\Phi_Z(\sigma\mathcal H)=(1-o_{\mathbb P}(1))M
\tag{4.14}
\]

for a uniformly random global relabelling \(\sigma\).  In particular,
\(\Phi_Z=\Omega(W)\) with probability \(1-o(1)\).

#### Proof

Under (4.12),

\[
\log\frac{2^{2m}}M=\frac12\log m+O_c(1).
\]

Thus (4.13) makes \(\delta_{2m,t,M}=o(1)\).  Use (4.6) with any
\(\eta=\eta_m\to0\) satisfying \(\delta/\eta\to0\).  \(\square\)

### Proposition 4.4 — exact relabelling invariance after optimizing \(Z\)

For every permutation \(\sigma\), every \(Z\subsetneq[n]\), and every hole
family \(\mathcal H\),

\[
\boxed{
\Phi_Z(\sigma\mathcal H)
=\Phi_{\sigma^{-1}Z}(\mathcal H).}
\tag{4.15}
\]

Consequently,

\[
\boxed{
\min_{|Z|=t}\Phi_Z(\sigma\mathcal H)
=
\min_{|Z|=t}\Phi_Z(\mathcal H).}
\tag{4.16}
\]

#### Proof

The map

\[
R\subseteq Z\longmapsto\sigma^{-1}R\subseteq\sigma^{-1}Z
\]

bijections trace classes and preserves their counts.  The complement
dimension \(n-t\), and therefore every cap \(\ell_R\), is unchanged.
This proves (4.15).  The permutation \(Z\mapsto\sigma^{-1}Z\) bijects all
\(t\)-sets, proving (4.16).  \(\square\)

Thus the product-box relabelling used to create high endpoint degree cannot
simultaneously improve the optimized trace functional.  It can only move a
previously existing exceptional marked set.

### Proposition 4.5 — exact entropy profile of every successful marked set

Assume

\[
cW_n\le M\le W_n,\qquad
0<\varepsilon\le c/2,
\tag{4.17}
\]

and suppose a \(t\)-set \(Z\) satisfies

\[
\Phi_Z(\mathcal H)\le\varepsilon W_n.
\tag{4.18}
\]

Let \(p_R=h_R/M\), let \(u\) be uniform on \(2^Z\), and let
\(\mathcal A_Z\) be the saturated trace set in (3.5).  Then

\[
\boxed{
|\mathcal A_Z|\le\varepsilon2^t,}
\tag{4.19}
\]

\[
\boxed{
p(\mathcal A_Z^c)\le\frac{\varepsilon}{c},}
\tag{4.20}
\]

and

\[
\boxed{
D(p\|u)
\ge
\left(1-\frac{\varepsilon}{c}\right)
\log\frac1\varepsilon
-h_2\!\left(\frac{\varepsilon}{c}\right),}
\tag{4.21}
\]

where

\[
h_2(x)=-x\log x-(1-x)\log(1-x).
\]

If the right side of (4.21) is positive, the fraction of \(t\)-sets
\(Z\) satisfying (4.18) is at most

\[
\boxed{
\frac{\frac tn\log(2^n/M)}
{\left(1-\frac{\varepsilon}{c}\right)\log(1/\varepsilon)
-h_2(\varepsilon/c)}.}
\tag{4.22}
\]

#### Proof

Every saturated trace contributes at least
\(\nu(n-t)\ge W_{n-t}\) to \(\Phi_Z\).  By Lemma 4.1,

\[
|\mathcal A_Z|
\le\frac{\varepsilon W_n}{W_{n-t}}
\le\varepsilon2^t,
\]

proving (4.19).  Proposition 3.1 gives

\[
\sum_{R\notin\mathcal A_Z}h_R
\le\Phi_Z\le\varepsilon W_n,
\]

and division by \(M\ge cW_n\) proves (4.20).

Put \(\beta=p(\mathcal A_Z^c)\le\varepsilon/c\).  A distribution with mass
\(1-\beta\) on at most \(\varepsilon2^t\) atoms has entropy at most

\[
t\log2+(1-\beta)\log\varepsilon+h_2(\beta).
\]

Thus

\[
D(p\|u)
\ge(1-\beta)\log(1/\varepsilon)-h_2(\beta).
\]

For \(0\le\beta\le\varepsilon/c\le1/2\), the right side is minimized at
\(\beta=\varepsilon/c\), proving (4.21).

Finally, (4.8) bounds the average of \(D(p_Z\|u_Z)\) over all \(t\)-sets.
Every set satisfying (4.18) has divergence at least (4.21).  Markov's
inequality proves (4.22).  \(\square\)

Equations (4.19)--(4.21) are the exact structural boundary: successful
trace compression of a linear hole family is necessarily a low-entropy,
coordinate-exceptional phenomenon.

---

## 5. A sharp local selected-support obstruction with all three anchors

This section returns to the productive interior of the exact odd-factor
useful-prefix word.  For an endpoint \(v\), write its saturated flag as

\[
\mathcal F(v)=
\{F_{v,a}:-H\le a\le H\},
\qquad |F_{v,a}|=m+a.
\tag{5.1}
\]

At a fully internal endpoint, the three maps

\[
v\longmapsto F_{v,-1},\qquad
v\longmapsto F_{v,0},\qquad
v\longmapsto F_{v,+1}
\tag{5.2}
\]

are globally injective.  They are, respectively, the outgoing lower edge
colour, the middle owner, and the incoming upper edge colour of the exact
two-sided-rainbow factor.

For a set \(X\) of endpoints, let

\[
\mathcal N_a(X)=\{F_{v,a}:v\in X\},
\qquad
\mathcal N(X)=\bigcup_{a=-H}^H\mathcal N_a(X).
\tag{5.3}
\]

Since different signed ranks are disjoint,

\[
\boxed{
|\mathcal N(X)|
=3|X|
+\sum_{a\notin\{-1,0,+1\}}|\mathcal N_a(X)|.}
\tag{5.4}
\]

An \(H\)-fold selected-target assignment asks for \(H\) distinct targets
at every endpoint, with no target reused.  Cloning each endpoint \(H\)
times shows that its exact Hall condition is

\[
\boxed{
|\mathcal N(X)|\ge H|X|
\quad\text{for every endpoint set }X.}
\tag{5.5}
\]

Thus all three anchor injections, not merely ranks \(0,+1\), must be
included in any local Hall calculation.

### Proposition 5.1 — exact portal-fibre degree

Suppose fully internal endpoints share one lower flag \(S\) at depth
\(q\ge2\) and one upper flag \(U\) at depth \(r\ge2\).  Then their number
is at most

\[
\boxed{
\min\left\{
\binom{q+r}{q-1},
\binom{q+r}{q},
\binom{q+r}{q+1}
\right\}.}
\tag{5.6}
\]

For \(q=r=2\), the bound is \(4\).

#### Proof

Every such endpoint has

\[
S\subset F_{v,-1}\subset F_{v,0}\subset F_{v,+1}\subset U.
\]

The interval \(U\setminus S\) has size \(q+r\).  Relative to \(S\), the
three anchor ranks have sizes \(q-1,q,q+1\).  By (5.2), the endpoints give
distinct choices at each anchor rank.  Their number is therefore bounded
by each of the three binomial coefficients.  \(\square\)

### Theorem 5.2 — sharp four-symbol branch/merge obstruction

Let \(K\) have size \(m-H\).  Choose pairwise distinct coordinates

\[
d_3,\ldots,d_H,\quad
z_0,z_1,z_2,z_3,\quad
y_3,\ldots,y_H
\tag{5.7}
\]

outside \(K\), and define

\[
L_q=K\cup\{d_{q+1},\ldots,d_H\}
\qquad(2\le q\le H),
\tag{5.8}
\]

\[
U_2=L_2\cup\{z_0,z_1,z_2,z_3\},
\tag{5.9}
\]

\[
U_q=U_2\cup\{y_3,\ldots,y_q\}
\qquad(3\le q\le H).
\tag{5.10}
\]

For \(i\in\mathbb Z/4\mathbb Z\), put

\[
F^{(i)}_{-q}=L_q\quad(2\le q\le H),
\tag{5.11}
\]

\[
F^{(i)}_{-1}=L_2\cup\{z_i\},
\tag{5.12}
\]

\[
F^{(i)}_0=L_2\cup\{z_i,z_{i+1}\},
\tag{5.13}
\]

\[
F^{(i)}_{+1}
=L_2\cup\{z_i,z_{i+1},z_{i+2}\},
\tag{5.14}
\]

and

\[
F^{(i)}_{+q}=U_q\quad(2\le q\le H).
\tag{5.15}
\]

Then:

1. each \(\mathcal F^{(i)}\) is an integral saturated radius-\(H\) flag;
2. the four maps at each of ranks \(-1,0,+1\) are injective;
3. every signed depth of magnitude at least \(2\) is common to all four
   flags;
4. any three flags have
   \[
   |\mathcal N(X)|=2H+7,
   \tag{5.16}
   \]
   and signed \(H\)-fold Hall gap
   \[
   3H-|\mathcal N(X)|=H-7;
   \tag{5.17}
   \]
5. all four flags have
   \[
   |\mathcal N(X)|=2H+10,
   \tag{5.18}
   \]
   and signed \(H\)-fold Hall gap
   \[
   4H-|\mathcal N(X)|=2H-10.
   \tag{5.19}
   \]

Thus a positive-deficit triple first occurs at \(H=8\), while for
\(H=6,7\) the four-endpoint obstruction already applies.  In the local
canonical-state category with the three anchor injections, the four
endpoints attain the degree \(4\) bound in Proposition 5.1 at \(q=r=2\).

#### Proof

The ranks in (5.8)--(5.15) increase by exactly one at every step and the
displayed sets are nested.  The rank-\(-1\) anchors use the four distinct
singletons \(z_i\); the middle anchors use the four distinct cyclic pairs;
and the rank-\(+1\) anchors use the four distinct cyclic triples.  Every
other signed rank is independent of \(i\).

There are \(2H-2\) nonanchor signed ranks.  Three endpoints contribute
nine distinct anchor targets, giving \(2H-2+9=2H+7\).  Four endpoints
contribute twelve, giving \(2H-2+12=2H+10\).  Subtract these numbers from
the \(H|X|\) demands.  \(\square\)

### Lemma 5.3 — every displayed flag is a legal long-geodesic state

Let

\[
F_{-H}\subset\cdots\subset F_0=T
\subset\cdots\subset F_H
\tag{5.20}
\]

be any saturated radius-\(H\) flag.  For every integer

\[
H\le t_0\le m-H,
\tag{5.21}
\]

it occurs at time \(t_0\) on a length-\(m\) no-return complementary
Johnson geodesic.  Reverse useful-prefix initialization makes all its flags
literal suffix intervals.

#### Proof

Let

\[
D=T\setminus F_{-H},\qquad P=F_H\setminus T,
\]

so \(|D|=|P|=H\), with their orders prescribed by the two arms of
(5.20).  Choose

\[
O\subseteq T,\qquad D\subseteq O,\qquad |O|=m-t_0,
\]

which is possible by \(t_0\le m-H\), and put \(Q=T\setminus O\).
Choose

\[
E\subseteq([2m]\setminus T)\setminus P,
\qquad |E|=t_0-H.
\]

Start from

\[
A=O\cup P\cup E.
\]

First remove the elements of \(E\), then remove the elements of \(P\) in
the reverse of the prescribed upper-arm order, while inserting all elements
of \(Q\).  After \(t_0\) transitions the current middle set is \(T\), and
the last \(H\) departures give exactly the upper arm.

Next remove \(D\) in the prescribed lower-arm order, then remove
\(O\setminus D\), while inserting the remaining complement of \(A\).
All initial elements depart exactly once, all complementary elements arrive
exactly once, and no arrival later departs.  The terminal middle set is
\([2m]\setminus A\).  Hence this is a no-return complementary geodesic and
its state at time \(t_0\) has exactly the flag (5.20).

Reverse-writing the \(2H+1\) useful blocks gives literal suffix witnesses,
as in (1.9).  \(\square\)

For \(m\ge3H\), one may take \(t_0=2H\), inside the productive guard
\(2H\le t\le m-H\).  In the exact odd factor the number of endpoints in
this guard is

\[
(m-3H+1)\frac{W}{m+1}
=W-\frac{3HW}{m+1}
=W-o_A(W).
\tag{5.22}
\]

Thus Theorem 5.2 is compatible with long components, delayed legality, and
literal shared endpoints.  It is constructed on separate components and is
**not** asserted to occur inside one exact owner-disjoint factor.  Its exact
conclusion is that no proof based only on
local canonical legality, componentwise fixed-rank injectivity, and the
three anchor injections implied by the two perfect first-band colour
partitions can establish the global selected-support theorem.  A nonlocal
argument using global colour exhaustivity or edge pairing is not ruled out.

---

## 6. Precise proved and conditional boundary

Theorem 1.3 proves more than near-support at the owner level: it gives zero
holes, integral nesting, the same first-band owners, and a literal
single-endpoint realization for every owner separately.

If one can choose those flags so that every edge of the
\(p=W/(m+1)\)-component first-band forest obeys the direct shift laws
(2.12)--(2.14), and also obeys the deepest-core legality condition

\[
d_H(w)\in F^-_{v,H}
\quad\text{for every edge }v\to w,
\tag{6.0}
\]

then

\[
F^-_{w,H}
=F^-_{v,H}-\{d_H(w)\}+\{T_w\setminus T_v\}.
\]

Useful-prefix initialize each component and perform these core updates.
This gives one literal word of exact length

\[
\boxed{
W+2Hp
=W+\frac{2HW}{m+1}}
\tag{6.1}
\]

with no band holes, and therefore \(\Phi_Z=0\) for every proper \(Z\).
This is a conditional proof of the requested missing gate, not an
unconditional construction.

What remains unproved is exactly one of the following two alternatives.

1. **Clean threading:** choose the owner-level full-support extension so
   that the three shift identities and (6.0) hold on every first-band edge.
   The exact necessary marginal condition is
   \(\mathfrak V_H\le2(2H-1)p\), together with the point-profile curvature
   bound (2.9).
2. **Tail-assisted threading:** use inherited useful-prefix tails to break
   one or more clean shift/core-transport laws while retaining total portal
   defect \(o(W)\).  Such a construction must still satisfy the trace necessities
   (3.11), (3.18), and (4.19)--(4.21).

The entropy theorem closes global coordinate averaging and generic
relabelling as ways to create the required trace geometry.  The
four-symbol theorem closes purely local legality and first-band
rainbowness as ways to force selected support.  Neither theorem rules out
a deliberately correlated exact factor, a specially chosen large marked
set, or a tail-assisted common chronology.  Accordingly:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
The cross-component selected deep-support / trace-compression theorem
remains open.  A clean zero-hole solution must realize a nearly
curvature-free integral threading of the full-support owner chains.  A
tail-assisted solution which retains linear aggregate hole mass must instead
produce an exceptional low-entropy marked trace geometry with unbounded
cross-depth multiplicity.  Static Hall completion, long no-return legality,
the local consequences of perfect first-band colours, and global
relabelling do not supply either alternative.
\end{minipage}}
\tag{6.2}
\]

No coefficient-one theorem, MWB, or labelled common-owner synchronization
is claimed.

---

## 7. Independent audit record

Three independent proof reconstructions were applied to the final
statements.

1. The owner-flow audit rederived the exact
   \(W/2=\binom{2m-1}{m}\) Kruskal--Katona threshold, both terminal SDRs,
   the rank-by-rank token routing, the \(2H+1\)-letter local literal order,
   all boundary signs in (2.15)--(2.17), and the factor
   \(2(2H-1)p\).  It found and corrected the necessary deepest-core
   condition (6.0); the three shift identities alone are not sufficient.
2. The shadow audit independently checked the baseline \(W-N_q\), the
   equality \(\Delta_H^\pm=M_H^\pm\), the middle-owner identities
   \(\Delta_0^\pm=0\), and the trace implication (1.21).
3. The trace audit rederived the scalar constant \(1\) in (3.9), both
   denominator directions in (3.11), the exact permutation kernel with no
   factor two, central-binomial monotonicity, Shearer's direction,
   Pinsker's \(1/2\), every high-probability quantifier, and the entropy
   bound (4.21).  The additive identity (3.6), the \(M=0\) convention, and
   all finite binomial conventions were checked explicitly.
4. The local-obstruction audit verified all ranks in
   (5.8)--(5.15), the signed Hall gaps, the degree-four fibre bound, and
   the long-geodesic embedding.  Its scope was narrowed to local
   consequences of the first-band partitions because simultaneous
   realization inside one exact factor is not proved.

After these corrections, no asserted theorem retains an unaudited
factor-of-two, endpoint, floor, integrality, or literal-interval step.  The
two alternatives in Section 6 remain genuinely open.
