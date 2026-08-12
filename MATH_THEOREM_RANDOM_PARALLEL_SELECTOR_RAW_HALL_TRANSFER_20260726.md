# Random parallel selectors transfer the maximal harmonic Hall gate to physical packets

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let the rank-twisted product cells retained in the middle layer be

\[
                         C\cong Q_{S_C},\qquad S_C\ge r,
\]

with total owner mass \(G\).  Assume

\[
                         H=o(r).
\tag{0.1}
\]

In every cell choose one \(r\)-subset of its intrinsic split axes and
partition the cell into the parallel physical \(Q_r\)-fibres obtained by
freezing the other axes.  This is the owner-packet interface used by the
diverse-order compiler.

This note proves that the retained-axis step itself need not create a new
raw Hall loss.  Define the maximal source-normalized loads

\[
 \Lambda_q^\epsilon(T)
   =\sum_{\substack{X\sim_{\rm max}^\epsilon T\\
                     X\text{ in a retained cell}}}
             {1\over\binom{S(X)}q},
 \qquad
 \rho_q={N_q\over W}.
\tag{0.2}
\]

There is one deterministic choice of the active \(r\)-set in every cell,
common to all depths and both signs, for which

\[
 \boxed{
 \sum_{q\le H,\epsilon}
       \operatorname{def}G_{q,{\rm sel}}^\epsilon
 \le
 \sum_{q\le H,\epsilon}\sum_T
       (1-\rho_q\Lambda_q^\epsilon(T))_+
       +O\!\left({W\over\sqrt r}\right).}
\tag{0.3}
\]

Here \(G_{q,{\rm sel}}^\epsilon\) is the exact raw graph obtained after
the parallel packet split but before imposing a compiler chronology.
Consequently the single harmonic lower-tail condition

\[
 \sum_{q\le H,\epsilon}\sum_T
       (1-\rho_q\Lambda_q^\epsilon(T))_+=o(W)
\tag{0.4}
\]

implies simultaneous selected-axis raw Hall with aggregate deficiency
\(o(W)\).  No cut-norm estimate or union bound over target families is
needed.

The proof is exact and preserves coordinate cylinders: it bounds every
literal Hall cut through one source-normalized load certificate.  It also
shows that the nonparallel transversal selector is not necessary at the
raw Hall stage; independent uniform *cellwise* parallel directions already
give a deterministic good choice by averaging.

Condition (0.4) is a genuine remaining hypothesis, not an automatic
consequence of total mass or profile Hall.  A second theorem below gives
a sharp obstruction.  For the legal constant-in-rank matching array, a
positive Gaussian fraction of owners overloads the natural two-step
Sinkhorn scaling, and (0.4) has linear defect.  Thus any proof of (0.4)
must use rank diversity essentially.

No chronological or compiler-conjugate assertion is made here.  The
diverse-order theorem may be installed after the packet split, but its
cross-packet choice is a later grouped problem.

## 1. The exact selected-axis load

Fix one sign and depth \(q\le H\).  In each retained cell \(C\cong Q_{S_C}\),
choose

\[
                         A_C\in\binom{[S_C]}r
\tag{1.1}
\]

independently and uniformly.  The complement axes are frozen in every
orientation, producing a parallel partition into physical \(Q_r\)'s.

A literal signed target \(T\) can be a physical \(q\)-face of a fixed
cell in at most one way.  Its varying direction set is then a uniquely
determined \(D_C(T)\in\binom{[S_C]}q\).  The face survives the packet split
exactly when

\[
                         D_C(T)\subseteq A_C.
\tag{1.2}
\]

If it survives, the face contains exactly \(2^q\) compatible middle
owners.  Every retained owner has exactly \(\binom rq\) selected-axis
targets.  Therefore the selected source-normalized load at \(T\) is

\[
 Z_q^\epsilon(T)
 ={\rho_q\over\binom rq}
       \#\{X:X\sim_{\rm sel}^\epsilon T\}
 ={\rho_q2^q\over\binom rq}
       \sum_{C:T\text{ is a }q\text{-face of }C}
          \mathbf1_{\{D_C(T)\subseteq A_C\}}.
\tag{1.3}
\]

The same formula holds on the lower and upper shores.  The fixed exterior,
zero, full, and spectator decorations ensure uniqueness of the cell face;
no physical target is counted twice inside one cell.

## 2. Exact mean and variance

For a fixed \(q\)-set \(D\subseteq[S_C]\),

\[
 \Pr(D\subseteq A_C)
 ={\binom{S_C-q}{r-q}\over\binom{S_C}r}
 ={\binom rq\over\binom{S_C}q}.
\tag{2.1}
\]

Substitution in (1.3) gives

\[
 \begin{aligned}
 \mathbb EZ_q^\epsilon(T)
 &=\rho_q\sum_{C:T\text{ a }q\text{-face of }C}
                         {2^q\over\binom{S_C}q}\\
 &=\rho_q\Lambda_q^\epsilon(T)=:\mu_q^\epsilon(T).
 \end{aligned}
\tag{2.2}
\]

The last equality is the exact whole-cell twirl identity: each physical
face has \(2^q\) source vertices, all in a cell of dimension \(S_C\).

Put

\[
                         a_q={\rho_q2^q\over\binom rq}.
\tag{2.3}
\]

The summands indexed by different cells in (1.3) are independent and
each is either zero or \(a_q\).  Hence

\[
 \boxed{
 \operatorname{Var}Z_q^\epsilon(T)
       \le a_q\mu_q^\epsilon(T).}
\tag{2.4}
\]

No independence among targets, signs, or depths is used.

Conservation of maximal twirled mass gives

\[
 \sum_T\Lambda_q^\epsilon(T)=G,
 \qquad
 \sum_T\mu_q^\epsilon(T)=\rho_qG\le N_q.
\tag{2.5}
\]

## 3. Every Hall cut is dominated by the load deficit

Let \(\mathcal Z\) be an arbitrary literal target family.  From (1.3),

\[
 \begin{aligned}
 \sum_{T\in\mathcal Z}Z_q^\epsilon(T)
 &= {\rho_q\over\binom rq}
       \sum_{X\in N(\mathcal Z)}
         |\{T\in\mathcal Z:T\sim_{\rm sel}^\epsilon X\}|\\
 &\le \rho_q|N(\mathcal Z)|
 \le |N(\mathcal Z)|.
 \end{aligned}
\tag{3.1}
\]

Therefore

\[
 |\mathcal Z|-|N(\mathcal Z)|
 \le\sum_{T\in\mathcal Z}(1-Z_q^\epsilon(T))
 \le\sum_T(1-Z_q^\epsilon(T))_+.
\tag{3.2}
\]

The deficiency form of Hall's theorem gives the exact certificate

\[
 \operatorname{def}G_{q,{\rm sel}}^\epsilon
 \le D_q^\epsilon:=\sum_T(1-Z_q^\epsilon(T))_+.
\tag{3.3}
\]

This is why coordinate cylinders and all other literal target families
are retained automatically.

## 4. Expected deficiency and simultaneous selection

For every target, (2.4) and Cauchy--Schwarz give

\[
 \begin{aligned}
 \mathbb E(1-Z_q^\epsilon(T))_+
 &\le(1-\mu_q^\epsilon(T))_+
       +\mathbb E|Z_q^\epsilon(T)-\mu_q^\epsilon(T)|\\
 &\le(1-\mu_q^\epsilon(T))_+
       +\sqrt{a_q\mu_q^\epsilon(T)}.
 \end{aligned}
\tag{4.1}
\]

Summing and using (2.5),

\[
 \begin{aligned}
 \mathbb ED_q^\epsilon
 &\le \sum_T(1-\rho_q\Lambda_q^\epsilon(T))_+
       +\sqrt{a_qN_q\sum_T\mu_q^\epsilon(T)}\\
 &\le \sum_T(1-\rho_q\Lambda_q^\epsilon(T))_+
       +N_q\sqrt{a_q}\\
 &\le \sum_T(1-\rho_q\Lambda_q^\epsilon(T))_+
       +W\sqrt{a_q}.
 \end{aligned}
\tag{4.2}
\]

Since \(\rho_q\le1\),

\[
                         a_q\le{2^q\over\binom rq}.
\tag{4.3}
\]

For \(q<H\),

\[
 {2^{q+1}/\binom r{q+1}\over2^q/\binom rq}
 ={2(q+1)\over r-q}
 \le\eta_m:={2(H+1)\over r-H}=o(1).
\tag{4.4}
\]

Thus

\[
 \sum_{q=1}^H\sqrt{a_q}
 \le {\sqrt{2/r}\over1-\sqrt{\eta_m}}
 =O(r^{-1/2}).
\tag{4.5}
\]

Sum (4.2) over all protected depths and both signs.  Linearity of
expectation is sufficient although the same \(A_C\)'s occur in every
summand.  Some deterministic common choice therefore attains at most the
expected total.  Equations (3.3) and (4.5) prove (0.3).

This proof also applies after omitting cells of total owner mass \(L\):
their entire effect is already present in \(G=W-L\) and in the maximal
loads (0.2).  More precisely, the harmonic term already contains at least
the depthwise mass deficit \(\rho_qL\), and hence its all-depth sum contains
the corresponding \(O(HL)\) baseline.  There is no *additional* omitted-cell
term outside the right side of (0.3); for the exponential leave used here
that included baseline is negligible.

## 5. A two-step fractional criterion

For completeness, let

\[
 B_{TX}={\mathbf1_{\{T\sim_{\rm max}X\}}
                    \over\binom{S(X)}q},
 \qquad
 \Lambda(T)=\sum_XB_{TX}.
\tag{5.1}
\]

Every source column of \(B\) sums to one.  If \(\Lambda(T)>0\), row
normalization gives

\[
                         K_{TX}={B_{TX}\over\Lambda(T)}.
\tag{5.2}
\]

Every target row of \(K\) sums to one, while the load at source \(X\) is

\[
 C(X)={1\over\binom{S(X)}q}
       \sum_{T\sim X}{1\over\Lambda(T)}.
\tag{5.3}
\]

Thus

\[
                         C(X)\le1\quad\hbox{for every }X
\tag{5.4}
\]

is a sufficient raw fractional Hall theorem.  Also

\[
                         \sum_XC(X)=N_q
\tag{5.5}
\]

exactly, so the average source load is \(\rho_q\).  This is the natural
one-sided Sinkhorn/LYM candidate.

There is a quantitative excess version.  Put

\[
                         E_q=\sum_X(C(X)-1)_+.
\tag{5.6}
\]

For every overloaded source column, multiply that column of \(K\) by
\(1/C(X)\), leaving the other columns unchanged.  The resulting fractional
matching uses source capacity at most one and removes total target mass
exactly \(E_q\).  Hence its total value is at least \(N_q-E_q\).
Bipartite matching-polytope integrality gives

\[
 \boxed{\operatorname{def}G_{q,{\rm max}}^\epsilon\le E_q.}
\tag{5.7}
\]

Thus \(E_q=o(W)\) is enough; pointwise (5.4) is not required.  The next
section proves that even this aggregate excess is linear for one legal
rank array.

## 6. Exact fixed-frame obstruction

Take one perfect matching of the \(2m\) ground coordinates and use it at
every local rank.  Equivalently, in the macroblock construction take
\(\pi_{j,k}=\pi_j\) for all \(k\).  This is a legal deterministic
rank-matching array.

For a middle owner \(X\), let \(f\) be its number of full matching pairs.
It also has \(f\) empty pairs and

\[
                         s=m-2f
\tag{6.1}
\]

split pairs.  Every lower depth-\(q\) neighbor of \(X\) has \(f\) full,
\(f+q\) empty, and \(s-q\) split pairs.  Such a target has exactly

\[
                         2^q\binom{f+q}q
\]

compatible middle sources, and every one of those sources has \(s\) split
pairs.  Hence its exact source-normalized load is

\[
 \boxed{
 \Lambda_f={2^q\binom{f+q}q\over\binom sq}.}
\tag{6.2}
\]

The upper shore has the same formula by complementation.  All neighbors
of one source have the same \(f\), so (5.3) becomes

\[
 \boxed{C(X)={1\over\Lambda_f}.}
\tag{6.3}
\]

Let

\[
 q=A\sqrt m+O(1),\qquad
 f={m\over4}+x\sqrt m+O(1),qquad
 s={m\over2}-2x\sqrt m+O(1),
\tag{6.4}
\]

with bounded \(x\).  Uniformly in such \(x\), the falling-factorial
expansion gives

\[
 \begin{aligned}
 \log\Lambda_f
 &=q\log{2(f+q)\over s}
   -{q(q-1)\over2}
      \left({1\over f+q}-{1\over s}\right)+o(1)\\
 &=3A^2+8Ax+o(1).
 \end{aligned}
\tag{6.5}
\]

For a uniform middle owner,

\[
 {f-m/4\over\sqrt m}\Longrightarrow N(0,1/16).
\tag{6.6}
\]

One way to see the variance is to start with independent density-one-half
coordinates.  For one matching pair, the full-pair indicator has variance
\(3/16\), its covariance with the pair occupancy is \(1/4\), and the
occupancy variance is \(1/2\).  Conditioning the total occupancy to equal
its mean leaves variance

\[
                         {3\over16}-{(1/4)^2\over1/2}
                         ={1\over16}
\]

per pair; the conditional central limit theorem gives (6.6).

Equations (6.3)--(6.6) imply

\[
 \Pr\{C(X)>1\}\longrightarrow
                         \Phi(-3A/2)>0.
\tag{6.7}
\]

Indeed \(C(X)>1\) is \(\Lambda_f<1\), whose limiting threshold is
\(x<-3A/8\).  Thus the one-step row normalization overloads a positive
fraction of sources.  Restricting to any bounded interval strictly below
that threshold makes \(C(X)-1\) uniformly positive, so

\[
                         E_q=\Omega_A(W).
\tag{6.7a}
\]

The stronger harmonic deficit in (0.4) is also linear for this array.
Since

\[
                         \rho_q=e^{-A^2+o(1)},
\]

(6.5) gives

\[
 \log(\rho_q\Lambda_f)=2A^2+8Ax+o(1).
\tag{6.8}
\]

Choose any fixed \(\delta>0\) and the bounded source band

\[
              -{A\over4}-2\delta\le x
                    \le-{A\over4}-\delta.
\]

It has positive limiting middle-owner mass, while throughout the band
\(\rho_q\Lambda_f\le e^{-8A\delta+o(1)}<1\).  The exact profile identity

\[
                         V_f=\Lambda_f T_{f,q}
\tag{6.9}
\]

between the number \(V_f\) of middle sources and the number \(T_{f,q}\)
of lower targets with full-pair count \(f\) shows that these target strata
have \(\Omega_A(W)\) total mass.  Consequently

\[
                         \sum_T(1-\rho_q\Lambda_q(T))_+
                              =\Omega_A(W).
\tag{6.10}
\]

The same holds above the middle.  Therefore (0.4), and not merely its
proof, fails for the constant-in-rank fixed matching.

This does not obstruct independent rank matchings.  It proves that a
deterministic one-sided LYM theorem valid for every rank array is false;
the look-ahead rank diversity must enter any positive proof.

## 7. Independent audit

The two key normalizations were checked in both directions.

1. A surviving physical \(q\)-face contributes \(2^q\) source incidences,
   and a selected owner has degree \(\binom rq\).  This gives exactly the
   coefficient \(\rho_q2^q/\binom rq\) in (1.3).
2. Multiplying that coefficient by the face-retention probability
   \(\binom rq/\binom{S_C}q\) gives
   \(\rho_q2^q/\binom{S_C}q\), exactly the contribution of the \(2^q\)
   source vertices to \(\rho_q\Lambda_q(T)\).

The variance estimate is cellwise, so the common active set across all
sibling fibres creates no omitted covariance.  Different cells are the
only independent variables used.  The geometric-series estimate is
dominated by \(q=1\), giving \(O(W/\sqrt r)\), not \(O(HW/\sqrt r)\).

For the obstruction, the \(+q\) inside \(\binom{f+q}q\) contributes
\(4A^2\) in the first term of (6.5), while the reciprocal
falling-factorial correction contributes \(-A^2\); this verifies the
coefficient \(3A^2\).  The normalization by \(\rho_q\) shifts it to
\(2A^2\) in (6.8).  The row-overload threshold \(-3A/8\) and harmonic
deficit threshold \(-A/4\) are therefore distinct and both are correct.

## 8. Exact boundary

Proved:

1. a common deterministic parallel-axis selection with the raw Hall
   transfer bound (0.3);
2. an \(O(W/\sqrt r)=o(W)\) total selector fluctuation through all
   \(q\le H\) and both signs;
3. preservation of every literal target cut, including coordinate
   cylinders; and
4. a linear fixed-frame obstruction to both the harmonic condition (0.4)
   and the universal two-step inequality (5.4).

Not proved:

1. the harmonic lower-tail estimate (0.4) for an independent or specially
   designed rank-diverse matching array;
2. a different raw fractional flow when (0.4) fails;
3. compiler-conjugate covariance or integral floor balancing; or
4. coefficient one.

Thus the retained-axis Hall gate is reduced sharply to the maximal
rank-diverse harmonic lower tail.  The next positive theorem must prove
that lower tail, or replace the source-normalized kernel by a genuinely
different cross-profile fractional flow.
