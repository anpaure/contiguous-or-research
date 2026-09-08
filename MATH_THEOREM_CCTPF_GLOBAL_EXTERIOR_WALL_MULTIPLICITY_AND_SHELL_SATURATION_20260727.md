# CCTPF global exterior-wall multiplicity: diagonal shells, exact moments, and the saturation obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Decision

Work in the fixed-good-core CCTPF catalogue with one fixed admissible
nested phase profile in every root. Put

\[
 M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
 \qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

\[
 c_0=L,\qquad c_r=b_{|r|}\quad(0<|r|<H),
 \qquad \ell_r=H-r,
\tag{0.2}
\]

and retain only the signed ranks for which \(c_r>0\). Write

\[
 d_r=\binom{s}{\ell_r},\qquad
 p_r=\frac{c_r}{d_r},\qquad
 p_*=\max_r p_r,
\tag{0.3}
\]

\[
 k=\sum_r c_r
   =L+2\sum_{q=1}^{H-1}b_q
   =(\sqrt\pi+o(1))m^{3/2},
\tag{0.4}
\]

and

\[
 h_*:=\sum_{\ell=1}^{2H-1}\ell=H(2H-1)<2H^2.
\tag{0.5}
\]

For a literal selected history \(f\) over root \(V\), define its
exposure to the complete fibre over \(U\) by

\[
 w_U(f)=\sum_{T\in P(f)}p_U(T),
\tag{0.6}
\]

where \(p_U(T)=p_r\) when \(T\) has signed rank \(r\) and is compatible
with \(U\), and \(p_U(T)=0\) otherwise.

This note resolves the purely geometric wall-multiplicity question as
follows.

1. For every literal history, all roots with \(w_U(f)>0\) lie in one
   reciprocal-core diagonal shell. If \(g\) is the shortest active
   deletion length, then

   \[
    \boxed{
    |\{U\ne V:w_U(f)>0\}|
    \le \Sigma_H:=2H\binom{s}{2H-g}.}
   \tag{0.7}
   \]

   At the calibrated height,

   \[
    \log\Sigma_H=O\!\left(H\log\frac mH\right)=o(m),
    \qquad \Sigma_H=o(N/\sqrt m).
   \tag{0.8}
   \]

2. The complete first- and second-moment bounds are

   \[
    \boxed{
    \sum_Uw_U(f)\le k,\qquad
    \sum_Uw_U(f)^2\le h_*k p_*.}
   \tag{0.9}
   \]

   More precisely, for every \(\tau>0\),

   \[
    \boxed{
    |\{U\ne V:w_U(f)\ge\tau\}|
    \le\min\left\{\Sigma_H,\frac{k}{\tau},
                          \frac{h_*kp_*}{\tau^2}\right\}.}
   \tag{0.10}
   \]

   These statements apply in particular when the displayed roots are
   unmatched roots of a maximum target-simple CCTPF matching.

3. The diagonal geometry improves the block-augmentation increment from
   \(kp_*\) to \(h_*p_*\). Hence every failed block of size
   at most \((2h_*p_*)^{-1}\) contains a root with an exterior wall of
   exposure at least \(1/2\), supplied by at least
   \((2h_*p_*)^{-1}\) distinct exterior histories.

4. Nevertheless (0.7)--(0.10) do not imply the required leave
   \(o(N/\sqrt m)\). There is a fixed core atlas satisfying all audited
   degree caps and, in fact, the stronger two-sided balance

   \[
    \deg_r(T)=(1+O(1/m))\frac{d_r}{\Lambda_{|r|}},
    \qquad \Lambda_q=\frac{\binom{2m}{m-q}}N,
   \tag{0.11}
   \]

   such that **every** literal history satisfies

   \[
    \boxed{
    \sum_{U\ne V}w_U(f)=(1-o(1))k.}
   \tag{0.12}
   \]

   Since its whole support has size \(o(N/\sqrt m)\), that support can be
   embedded in a root set \(R_f\) of size \(\lfloor N/\sqrt m\rfloor\),
   and then

   \[
    \boxed{
    \sum_{U\in R_f}w_U(f)=(1-o(1))k.}
   \tag{0.13}
   \]

   A hoped-for geometry-only estimate of order \(o(1/\sqrt m)\) is
   therefore false by the exact factor

   \[
    (1-o(1))k\sqrt m=(\sqrt\pi+o(1))m^2.
   \tag{0.14}
   \]

5. The obstruction is literal, not only fractional. On the balanced
   atlas there is a one-literal-history-per-root selection for which the
   **union** of the other selected target sets has exposure \(\Omega(k)\)
   to every complete root fibre. Duplicate exterior targets are counted
   only once.
   One prescribed selected history may simultaneously be required to be
   target-disjoint from every other selected history. Deleting
   \(\Theta(k/(h_*p_*))\) owner histories leaves that many unowned roots,
   all with exposure walls much larger than \(1/2\), and the prescribed
   history has positive exposure into each chosen wall. These walls
   survive a further \(\Theta(k/(h_*p_*))\) history deletions.

The last construction is an owner-exact literal selection, but the
histories other than the prescribed one are not asserted to be mutually
target-disjoint. Consequently it is not a counterexample to coefficient
one. It proves the sharp obstruction requested here: exact core/path
geometry, diagonal-shell support, all column moments, and failure of all
small additive wall tests still do not beat the \(k\sqrt m\) factor. A
positive theorem must use the target-simplicity and alternating
optimality of the actual matching, not another single-column incidence
bound.

## 1. Exact reciprocal-core shell

Fix a literal history \(f\) over root \(V\), with core \(Q_V\), and
write its tail order as

\[
                         w=(w_1,\ldots,w_s).
\tag{1.1}
\]

Every protected target has the form

\[
 T_{j,\ell}=V\setminus I_{j,\ell},
 \qquad
 I_{j,\ell}
 =\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\}.
\tag{1.2}
\]

For another root \(U\), put

\[
 A=U\setminus V,\qquad B=V\setminus U,
 \qquad |A|=|B|=\delta.
\tag{1.3}
\]

### Lemma 1.1 (exact diagonal criterion)

The target \(T_{j,\ell}\) is compatible with root \(U\) if and only if

\[
 Q_V\subseteq U,\qquad Q_U\subseteq V,
\tag{1.4}
\]

\[
 B\subseteq I_{j,\ell},\qquad
 Q_U\cap I_{j,\ell}=\varnothing.
\tag{1.5}
\]

#### Proof

Compatibility is the pair of inclusions

\[
                         Q_U\subseteq T_{j,\ell}\subseteq U.
\tag{1.6}
\]

The second inclusion holds exactly when every point of \(V\setminus U=B\)
is deleted, namely \(B\subseteq I_{j,\ell}\). Since the deletion interval
lies in \(V\setminus Q_V\), this also says \(Q_V\subseteq U\). The first
inclusion in (1.6) says exactly that \(Q_U\subseteq V\) and that the
deletion interval avoids \(Q_U\). This proves (1.4)--(1.5). \(\square\)

If \(B\subseteq V\setminus Q_V\), let \(a_w(B)\) be its linear span in
the word \(w\). A length-\(\ell\) interval contains \(B\) in at most

\[
                         (\ell-a_w(B)+1)_+
\tag{1.7}
\]

positions. Hence, if \(n_\ell(U,V;f)\) counts the compatible protected
cells at deletion length \(\ell\), then

\[
 \boxed{
 w_U(f)=\sum_\ell n_\ell(U,V;f)p_\ell,
 \qquad
 n_\ell(U,V;f)\le(\ell-a_w(B)+1)_+.}
\tag{1.8}
\]

In particular,

\[
 \boxed{w_U(f)\le h_*p_*.}
\tag{1.9}
\]

This bound uses all vertical depths as one diagonal context. Replacing it
by the target count \(k\) loses a factor of order \(k/H^2\).

## 2. Exact support cardinality

Let

\[
 g=\min\{\ell_r:c_r>0\}.
\tag{2.1}
\]

Because the same quota \(b_q\) is used at the two signs, the largest
active deletion length is

\[
                         \ell_{\max}=2H-g.
\tag{2.2}
\]

At the calibrated height,

\[
 g=\left(\frac{\log2}{2}+o(1)\right)\frac mH
   =\left(\frac{\log2}{2}+o(1)\right)
      \sqrt{\frac m{\log m}}.
\tag{2.3}
\]

Indeed, \(b_q>0\) is equivalent, up to the endpoint integer convention,
to \(\Lambda_q\ge2\), while

\[
 \log\Lambda_q
 =\sum_{i=q+1}^{H}\log\frac{m+i}{m-i+1}
 =\left(2+o(1)\right)\frac{H(H-q)}m
\tag{2.4}
\]

uniformly when \(H-q=O(m/H)\).

### Theorem 2.1 (two exact shell bounds)

For every literal history \(f\) over \(V\),

\[
 \boxed{
 |\operatorname{supp}(f)|
 :=|\{U\ne V:w_U(f)>0\}|
 \le
 \min\left\{
  \sum_{r:c_r>0}d_r,
  \ s\binom{s+\ell_{\max}}{\ell_{\max}}
 \right\}.}
\tag{2.5}
\]

Consequently,

\[
 \boxed{
 |\operatorname{supp}(f)|
 \le\Sigma_H:=2H\binom{s}{2H-g}.}
\tag{2.6}
\]

#### Proof

At signed rank \(r\), the history contains exactly \(c_r\) targets. The
fixed-core degree cap says that each such target is compatible with at
most

\[
                         \frac{d_r}{c_r}=\frac1{p_r}
\tag{2.7}
\]

roots. The union of their root stars therefore has size at most \(d_r\).
Summing over signed ranks gives the first term of (2.5).

For the geometric term, Lemma 1.1 says that \(B=V\setminus U\) is a
\(\delta\)-set contained in some tail interval of length at most
\(\ell_{\max}\). There are at most

\[
                         s\binom{\ell_{\max}}\delta
\tag{2.8}
\]

choices for such a \(B\), with overcounting allowed. Having fixed \(B\),
the entering set \(A=U\setminus V\) is a \(\delta\)-subset of the
\(s\)-set outside \(V\). Thus the number of possible roots is at most

\[
 s\sum_{\delta=1}^{\ell_{\max}}
       \binom{\ell_{\max}}\delta\binom{s}\delta
 <s\binom{s+\ell_{\max}}{\ell_{\max}},
\tag{2.9}
\]

where the last identity is Vandermonde's identity. The additional
condition on \(Q_U\) only removes roots.

Finally all active deletion lengths are at most \(2H-g<s/2\), so
\(d_r\le\binom{s}{2H-g}\). There are fewer than \(2H\) active signed
ranks. This proves (2.6). \(\square\)

Since

\[
 \log\binom{s}{2H-g}
 \le(2H-g)\log\frac{es}{2H-g}
 =O\!\left(H\log\frac mH\right)=o(m),
\tag{2.10}
\]

while \(\log N=(2\log2+o(1))m\), equation (0.8) follows.

## 3. First, second, and level-set moments

For a protected target \(T\), put

\[
                         \rho(T)=\sum_Up_U(T).
\tag{3.1}
\]

The fixed-core degree caps give \(\rho(T)\le1\).

### Theorem 3.1 (complete single-history moment bounds)

For every literal history \(f\),

\[
 \sum_Uw_U(f)\le k,
 \qquad
 \sum_Uw_U(f)^2\le h_*kp_*.
\tag{3.2}
\]

For every root family \(\mathcal R\) and every \(\tau>0\),

\[
 |\{U\in\mathcal R\setminus\{V\}:w_U(f)\ge\tau\}|
 \le\min\left\{
  \Sigma_H,\frac{k}{\tau},\frac{h_*kp_*}{\tau^2}
 \right\}.
\tag{3.3}
\]

#### Proof

Exchange the two sums:

\[
 \sum_Uw_U(f)
 =\sum_{T\in P(f)}\sum_Up_U(T)
 =\sum_{T\in P(f)}\rho(T)\le k.
\tag{3.4}
\]

By (1.9), \(w_U(f)^2\le h_*p_*w_U(f)\). Sum and use (3.4), proving the
second assertion of (3.2). The support, first-moment Markov, and
second-moment Markov bounds give the three terms in (3.3). \(\square\)

No independence, randomness, or matching assumption is present in this
theorem.

## 4. The improved block wall and what double counting gives

Let \(\mathcal M\) be a target-simple rooted matching, let
\(S\subseteq\mathcal M\), and let \(R\) be a nonempty family of roots
unmatched by \(\mathcal M\). Put

\[
 \mathcal A=R\mathbin{\dot\cup}\operatorname{root}(S),
 \qquad a=|\mathcal A|,
\tag{4.1}
\]

and let \(\mathcal B_{\rm ext}\) be the target set used by
\(\mathcal M\setminus S\).

### Theorem 4.1 (diagonal-shell block augmentation)

If the roots of \(\mathcal A\) can be ordered
\(U_1,\ldots,U_a\) so that

\[
 \omega_{U_i}(\mathcal B_{\rm ext})+(i-1)h_*p_*<1
 \qquad(1\le i\le a),
\tag{4.2}
\]

then \(\mathcal M\setminus S\) can be extended by one new literal
history in every root of \(\mathcal A\). The matching size increases by
\(|R|\).

#### Proof

Choose the new histories in the displayed order. One previously chosen
history contributes at most \(h_*p_*\) exposure to the next root by
(1.9). Hence the complete forbidden target family has exposure less
than one at every step. The exact forbidden-port lemma supplies a
literal avoiding history. \(\square\)

### Corollary 4.2 (wall forced by a maximum matching)

If \(\mathcal M\) is maximum, then for every \(R,S\) as above,

\[
 \boxed{
 \max_{U\in\mathcal A}
 \omega_U(\mathcal B_{\rm ext})
 \ge1-(a-1)h_*p_*.}
\tag{4.3}
\]

If \(a\le(2h_*p_*)^{-1}\), some root in \(\mathcal A\) has exterior
exposure at least \(1/2\), supplied by at least
\((2h_*p_*)^{-1}\) distinct exterior histories.

The last assertion follows because each exterior history contributes at
most \(h_*p_*\) to one root.

Now let \(\mathcal R\) be any family of roots carrying exposure walls at
least \(1/2\), and suppose all blockers belong to a target-simple family
of at most \(N\) literal histories. Let

\[
 E=\{(U,f):U\in\mathcal R,\ w_U(f)>0\}.
\tag{4.4}
\]

The wall lower bound and Theorem 2.1 give

\[
 \frac{|\mathcal R|}{2h_*p_*}
 \le |E|\le N\Sigma_H,
\tag{4.5}
\]

and hence

\[
                         |\mathcal R|
 \le2Nh_*p_*\Sigma_H.
\tag{4.6}
\]

This is the strongest direct unweighted shell count. It is not a useful
leave bound. Indeed \(p_*\ge1/\binom{s}{g}\), while
\(\Sigma_H=2H\binom{s}{2H-g}\), and (2.3) gives

\[
 \log\left(
 h_*\frac{\binom{s}{2H-g}}{\binom{s}{g}}
 \right)
 =\Theta\!\left(H\log\frac mH\right).
\tag{4.7}
\]

Thus the explicit coefficient on the right side of (4.6) is much larger
than one.

The square bound also stops short. From Theorem 3.1,

\[
 \sum_f\sum_{U\in\mathcal R}w_U(f)^2
 \le Nh_*kp_*.
\tag{4.8}
\]

For a wall row, Cauchy--Schwarz over at most \(N\) exterior histories
gives only

\[
 \sum_fw_U(f)^2\ge\frac1{4N}.
\tag{4.9}
\]

Combining (4.8)--(4.9) yields

\[
                         |\mathcal R|\le4N^2h_*kp_*,
\tag{4.10}
\]

again vacuous because \(Np_*\) is exponentially large. Higher
nonnegative column moments have the same defect: an exposure wall may
be assembled from exponentially many individually tiny blockers.

## 5. A two-sided balanced good-core atlas

The preceding failure is not an artefact of one badly concentrated core
assignment.

### Lemma 5.1 (uniform two-sided core balance)

For all sufficiently large \(m\), the cores can be fixed so that every
active signed target \(T\) of rank \(m+r\) satisfies

\[
 \boxed{
 \deg_r(T)=\left(1+O\!\left(\frac1m\right)\right)
                  \frac{d_r}{\Lambda_{|r|}},}
\tag{5.1}
\]

and simultaneously

\[
                         \deg_r(T)\le\frac{d_r}{c_r}.
\tag{5.2}
\]

#### Proof

Choose each \(Q_U\) independently and uniformly from
\(\binom U{2H}\). For a fixed signed target, its compatible-root degree
is binomial with mean

\[
                         \mu_r=\frac{d_r}{\Lambda_{|r|}}.
\tag{5.3}
\]

Uniformly in the active band, \(\Lambda_{|r|}\le\Lambda_0=O(m)\).
The minimum active deletion length is \(g=\Omega(m/H)\), so

\[
 \min_r\mu_r
 \ge\frac1{O(m)}\binom{s}{g}.
\tag{5.4}
\]

This grows so rapidly that

\[
                         \frac{\min_r\mu_r}{m^2}\gg m.
\tag{5.5}
\]

Choose a fixed sufficiently large constant \(C\) and apply the two-sided
Chernoff bound at relative error \(1/(Cm)\). The failure probability for
one target is at most

\[
                         2\exp\{-c\mu_r/m^2\}.
\tag{5.6}
\]

There are fewer than \(2H4^m\) protected signed targets, so (5.5) and a
union bound prove simultaneous two-sided balance.

It remains to retain the audited upper caps. The quota definition gives

\[
                         c_r\le\Lambda_{|r|}-1
\tag{5.7}
\]

at every active signed rank, including the capped ranks; at the middle,
\(\Lambda_0-L=\Theta(H)\). Since \(c_r,\Lambda_{|r|}=O(m)\), the relative
gap between \(d_r/c_r\) and the mean \(d_r/\Lambda_{|r|}\) is at least
\(1/(C_0m)\) for an absolute \(C_0\). Taking \(C>2C_0\) makes the
upper side of (5.1) lie below (5.2). \(\square\)

For this atlas every active target has load

\[
 \rho(T)=p_r\deg_r(T)
 =\left(1+O\!\left(\frac1m\right)\right)
          \frac{c_r}{\Lambda_{|r|}}.
\tag{5.8}
\]

Define

\[
 \kappa
 =\frac{L^2}{\Lambda_0}
   +2\sum_{q=1}^{H-1}\frac{b_q^2}{\Lambda_q}.
\tag{5.9}
\]

The quota ledger gives

\[
                         \kappa=(1-o(1))k.
\tag{5.10}
\]

For completeness, at an uncapped depth
\(b_q=\lfloor\Lambda_q\rfloor-1\), so
\(b_q-b_q^2/\Lambda_q=O(1)\). There are \(O(H)\) such depths. Only
\(O(\sqrt H)\) depths are capped, and each contributes \(O(H)\) to the
difference. The middle contributes \(O(H)\). Hence

\[
                         k-\kappa=O(H^{3/2})=o(k).
\tag{5.11}
\]

### Theorem 5.2 (every literal column saturates its first moment)

On the balanced atlas, every literal history \(f\) over every root \(V\)
satisfies

\[
 \boxed{
 \sum_{U\ne V}w_U(f)=(1-o(1))k.}
\tag{5.12}
\]

It also satisfies

\[
 \boxed{
 c p_*\le\sum_{U\ne V}w_U(f)^2\le h_*kp_*}
\tag{5.13}
\]

for an absolute \(c>0\), and

\[
 \boxed{
 \frac{(1-o(1))k}{h_*p_*}
 \le|\operatorname{supp}(f)|\le\Sigma_H.}
\tag{5.14}
\]

#### Proof

Every history contains \(c_r\) targets at signed rank \(r\). Equations
(5.8)--(5.10) give

\[
 \sum_Uw_U(f)
 =\sum_{T\in P(f)}\rho(T)
 =\left(1+O\!\left(\frac1m\right)\right)\kappa
 =(1-o(1))k.
\tag{5.15}
\]

The same-root contribution is at most \(kp_*=o(1)\), proving (5.12).

Choose an active rank \(r_*\) attaining \(p_*\), and choose one of the
\(c_{r_*}\) targets of \(f\) at that rank. Uniformly over active ranks,

\[
                         \frac{c_r}{\Lambda_{|r|}}\ge\frac13-o(1).
\tag{5.16}
\]

Indeed this is immediate in the capped and middle cases; in the
uncapped case it follows from
\(c_r=\lfloor\Lambda_{|r|}\rfloor-1\) and
\(\Lambda_{|r|}\ge2\). Thus the chosen target is compatible with at
least \((1/4)/p_*\) roots for large \(m\). Each of those roots has
\(w_U(f)\ge p_*\). Deleting the possible root \(V\) changes the following
bound by only \(p_*^2\), so for large \(m\),

\[
                         \sum_{U\ne V}w_U(f)^2\ge p_*/5.
\tag{5.17}
\]

The upper side is Theorem 3.1. Finally (1.9) and (5.12) give the lower
support bound, while Theorem 2.1 gives the upper bound. \(\square\)

Because \(\Sigma_H=o(N/\sqrt m)\), enlarge
\(\operatorname{supp}(f)\) to any root family \(R_f\) of size
\(\lfloor N/\sqrt m\rfloor\). Equation (5.12) becomes

\[
                         \sum_{U\in R_f}w_U(f)=(1-o(1))k.
\tag{5.18}
\]

This proves (0.13)--(0.14). Notice that even the complete square moment
in (5.13) is entirely contained in the same critical-size family. A
column-moment argument cannot force any of its mass outside \(R_f\).

To see the calibration directly, a family of \(N/\sqrt m\) half-walls
has total demand \(\Theta(N/\sqrt m)\). With at most \(N\) blocker
histories, a columnwise proof would have to force exposure
\(o(1/\sqrt m)\) from each history into that root family. Equation
(5.18) instead permits \((1-o(1))k\), larger by
\((1-o(1))k\sqrt m\). This is exactly the \(\Theta(m^2)\) discrepancy
left by the scalar wall budget.

## 6. Literal simultaneous saturation of all union walls

The concentration in Theorem 5.2 can coexist with literal walls at every
root. It is important here to use the union of selected target sets, not
the sum with collision multiplicity.

For distinct roots put

\[
 q_{U,V}=\frac1D\sum_{e\in\Omega_V}w_U(e)
         =\sum_Tp_U(T)p_V(T),
 \qquad D=s!.
\tag{6.1}
\]

### Lemma 6.1 (uniform mean summed exposure)

On the balanced atlas, uniformly in \(U\),

\[
 \boxed{
 a_U:=\sum_{V\ne U}q_{U,V}=(1-o(1))k.}
\tag{6.2}
\]

#### Proof

Using \(\rho(T)=\sum_Vp_V(T)\),

\[
 a_U
 =\sum_Tp_U(T)(\rho(T)-p_U(T)).
\tag{6.3}
\]

At signed rank \(r\), root \(U\) has exactly \(d_r\) compatible targets,
each with \(p_U(T)=c_r/d_r\). Equations (5.8)--(5.10) therefore give

\[
                         \sum_Tp_U(T)\rho(T)=(1-o(1))k.
\tag{6.4}
\]

Moreover,

\[
 \sum_Tp_U(T)^2
 =\sum_r\frac{c_r^2}{d_r}
 \le p_*\sum_rc_r=kp_*=o(1).
\tag{6.5}
\]

Substitute into (6.3). \(\square\)

We use the following weighted coverage inequality.

### Lemma 6.2 (weighted self-bounding coverage)

Let \(E_1,\ldots,E_n\) be independent random subsets of a finite set
\(\mathcal X\), let \(a_x\ge0\), and put

\[
 Z=\sum_{x\in\cup_iE_i}a_x.
\tag{6.6}
\]

Suppose every possible value of every \(E_i\) has total weight at most
\(b\). Then, for \(0<t<\mathbb EZ\),

\[
 \boxed{
 \Pr(Z\le\mathbb EZ-t)
 \le\exp\left\{-\frac{t^2}{2b\mathbb EZ}\right\}.}
\tag{6.7}
\]

#### Proof

Let \(Z_i\) be the coverage weight after deleting coordinate \(i\). Then

\[
 0\le Z-Z_i\le b,
 \qquad
 \sum_i(Z-Z_i)\le Z.
\tag{6.8}
\]

The second inequality holds because a target contributes to the sum only
when it is covered uniquely, in which case it contributes once. Thus
\(Z/b\) is a nonnegative self-bounding function of independent
coordinates. The lower-tail self-bounding inequality, obtained by
tensorizing entropy for \(\exp(-\lambda Z/b)\) and applying exponential
Markov, is exactly (6.7). Conditions (6.8) verify all its hypotheses.
\(\square\)

### Theorem 6.3 (literal robust union-wall selection)

There is a one-literal-history-per-root selection \((e_U)_U\) such that

\[
 \boxed{
 Z_U:=
 \omega_U\left(\bigcup_{V\ne U}P(e_V)\right)
 \ge\frac{\gamma k}{4}
 \qquad\text{for every root }U,}
 \qquad \gamma:=1-e^{-1/5}>0.
\tag{6.9}
\]

The union in (6.9) deduplicates every repeated exterior target. Moreover,
one literal history \(f\in\Omega_{V_0}\) may be prescribed in advance,
and all other selected histories may simultaneously be required to avoid
every target of \(f\).

#### Proof

First ignore the final avoidance condition and choose one uniform literal
history independently in every root. Fix \(U\). For every target \(T\)
compatible with \(U\), its total selection probability in the other root
fibres satisfies

\[
 \sum_{V\ne U}p_V(T)=\rho(T)-p_U(T)\ge\frac15
\tag{6.10}
\]

for all sufficiently large \(m\), by (5.8), (5.16), and \(p_*=o(1)\).
Independence over root fibres gives

\[
 \Pr\left(T\in\bigcup_{V\ne U}P(e_V)\right)
 =1-\prod_{V\ne U}(1-p_V(T))
 \ge1-e^{-1/5}=\gamma.
\tag{6.11}
\]

There are \(d_r\) targets compatible with \(U\) at signed rank \(r\),
each having weight \(p_U(T)=c_r/d_r\). Therefore

\[
                         \mathbb EZ_U\ge\gamma\sum_rc_r=\gamma k.
\tag{6.12}
\]

Deleting one exterior history decreases \(Z_U\) by at most \(h_*p_*\),
by (1.9). Apply Lemma 6.2 with \(b=h_*p_*\) and
\(t=\mathbb EZ_U/2\). It gives

\[
 \Pr(Z_U<\gamma k/2)
 \le\exp\left\{-c\frac{k}{h_*p_*}\right\}.
\tag{6.13}
\]

The exponent in (6.13) is much larger than \(m\), whereas
\(\log N=O(m)\). A union bound proves a stronger form of (6.9) without
the prescribed-history condition.

Now prescribe \(f\) at \(V_0\). At every other root \(V\), choose a
uniform history conditioned to avoid \(P(f)\). Such a history exists
because the probability of meeting \(P(f)\) is at most
\(w_V(f)\le h_*p_*=o(1)\). These conditional choices remain independent.

Changing the distribution of one selected history changes the expected
union exposure by at most \(2h_*p_*\) times the total-variation distance.
Conditioning away an event of probability \(\theta<1/2\) has
total-variation distance at most \(2\theta\). Here
\(\theta\le w_V(f)\). Hence, for every fixed root \(U\), the total change
in \(\mathbb EZ_U\) is at most

\[
 4h_*p_*\sum_Vw_V(f)+2h_*p_*
 \le4h_*kp_*+2h_*p_*=o(1),
\tag{6.14}
\]

where the last term accounts for fixing the \(V_0\)-history. The same
self-bounding bound and union bound show that (6.9) holds with room to
spare. Every chosen history outside \(V_0\) avoids \(f\), as required.
\(\square\)

Theorem 5.2 and (1.9) show that the prescribed history has positive
exposure to at least

\[
                         \frac{(1-o(1))k}{h_*p_*}
\tag{6.15}
\]

distinct roots. Choose

\[
 t=\left\lfloor\frac{\gamma k}{32h_*p_*}\right\rfloor
\tag{6.16}
\]

of these roots, none equal to \(V_0\), and call the resulting family
\(R_0\). Delete their selected histories, leaving these roots unowned.
Removing one selected history can reduce a root's union exposure by at
most \(h_*p_*\). Therefore, for every root \(U\), and in particular every
\(U\in R_0\), the remaining selected target union has exposure at least

\[
                         \frac{\gamma k}{4}-t h_*p_*
                         \ge\frac{7\gamma k}{32}.
\tag{6.17}
\]

Also \(w_U(f)>0\) for every \(U\in R_0\). If an additional block of at
most \(t\) selected histories is deleted, every one of these walls still
has exposure at least

\[
                         \frac{3\gamma k}{16}>\frac12
\tag{6.18}
\]

for large \(m\).

Thus one prescribed literal history contributes physically to
\(\Theta(k/(h_*p_*))\) simultaneous robust union walls after all
additive block tests of that order have failed. The construction uses
complete literal histories, exact cores, exact phase contexts, and
deduplicated exterior target families.

The limitation is equally exact: the retained histories other than
\(f\) may collide with one another. The prescribed \(f\) is disjoint
from all of them, but the retained family is not claimed to be a
target-simple matching. Turning this owner-exact wall system into a
target-simple exterior is precisely the global common-history rounding
problem; assuming it here would be circular.

## 7. Final theorem and exact remaining gate

### Theorem 7.1 (global wall-multiplicity dichotomy)

For fixed-good-core CCTPF at calibrated height:

1. a matched literal history can contribute to walls only inside its
   reciprocal-core diagonal shell, whose size is at most \(\Sigma_H\)
   and is \(o(N/\sqrt m)\);
2. its complete contribution level sets obey (3.3), including the exact
   squared bound \(h_*kp_*\);
3. the correct per-pair block increment is \(h_*p_*\), not \(kp_*\);
4. a failed block below \((2h_*p_*)^{-1}\) forces at least
   \((2h_*p_*)^{-1}\) exterior blocker histories;
5. neither the support double count nor the square double count yields a
   nontrivial root-leave estimate;
6. there is a good balanced atlas on which every literal history places
   \((1-o(1))k\) exposure inside a root set of size \(o(N/\sqrt m)\),
   saturating the missing factor \(k\sqrt m=(\sqrt\pi+o(1))m^2\);
7. there is an owner-exact literal selection with simultaneous robust
   union walls at every root and with one prescribed history feeding
   \(\Theta(k/(h_*p_*))\) of those walls; but
8. that saturation selection is not target-simple away from the
   prescribed history.

Therefore no averaged, squared, or finite-moment wall-support estimate
derived only from fixed-core/path geometry can prove coefficient one.
The exact surviving statement would have to say:

> In a maximum **target-simple** matching, the unmatched-root set cannot
> correlate with the diagonal shells of the matched histories as in the
> balanced literal saturation construction.

This is an alternating-integrality theorem, not another incidence
moment. Proving it would close the exterior-wall lane; constructing a
target-simple version of Theorem 6.3 would give the corresponding sharp
obstruction.

## 8. Dependency ledger

This note uses only the following already audited local inputs:

- the exact fixed-core port count and forbidden-port lemma;
- the reciprocal-core diagonal-shell criterion and span bound;
- the simultaneous common-core degree caps;
- the calibrated quota estimate \(k=(\sqrt\pi+o(1))m^{3/2}\); and
- the fact that active upper deletion lengths begin at
  \((\log2/2+o(1))m/H\).

All global balance, moment, concentration, and obstruction statements
are proved above. No target-simple near-factor, coefficient-one theorem,
or computational experiment is assumed.
