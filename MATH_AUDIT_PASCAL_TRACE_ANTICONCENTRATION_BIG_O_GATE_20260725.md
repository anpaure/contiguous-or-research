# Audit and extension of the PBBS Pascal-trace big-O gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web search is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1,
\]

where \(A>0\) is fixed.  The linear literal seam theorem makes the
following requested big-oh quotient estimate sufficient:

\[
 \boxed{\overline\nu_H=O_A(B_r/r).}                 \tag{0.1}
\]

The proposed primitive zero-winding converse is not used.  In particular,
no implication of the form
\(d(D)=1\Rightarrow g(D)=2\operatorname{ht}(D)+1\) is used below.

This note proves and audits three statements.

1. In a first peak-deletion Pascal cell, the complete mass of lifts which
   return by time \(G\) is an exact threshold in the predecessor local
   time.  In the saddle it is, up to constants, the indicator that the
   predecessor is selected twice.  The resulting factorial-moment
   majorant is an exact three-point PBBS trace.

2. The uniform-label part of that trace has precisely the desired size

   \[
    (2A^2+o_A(1))B_r/r.
   \]

   Hence the sole missing energy estimate is the peak-sensitive
   nonuniform trace excess (3.6) below.

3. The triangular zero-winding fan extends through every deletion level,
   not only through level \(h/2\): at level \(j\) it prescribes at least
   \(\min\{j,2r_j\}\) distinct common-phase Pascal coordinates.  If
   \(\ell\) is the first mountain depth, the exact curvature identity is

   \[
    \sum_{j=1}^{\ell}j
       (r_{j-1}-2r_j+r_{j+1})=r-h.                 \tag{0.2}
   \]

   This gives the unconditional profile envelope

   \[
    \boxed{Q_\ell^*\le\sqrt{h/r}.}                 \tag{0.3}
   \]

   It is a genuine all-level improvement, but it is not the required
   \(O(h/r)=O_A(1/h)\) harmonic factor.

The coefficient-one conclusion is therefore not proved here.  Moreover,
even an \(O(1/H)\) marginal fibre factor cannot simply be multiplied by
the \(1/H\) interval-length factor: an exact integral residue-class model
attains the larger \(1/H\) packing scale.  The remaining assertion must be
a PBBS-specific common-base, cross-phase anticorrelation theorem.  The
precise sufficient statement is (3.6); the precise fan version is (6.5).

Two independently audited constructions make the scale statements sharp.
First, actual overlap-one zero-winding roots have total
\(\Omega(B_r/N)\) mass in a fixed Gaussian band on infinitely many ranks.
Thus an \(o(B_r/N)\) start theorem is false, while the present
\(O(B_r/N)\) target remains possible and best-scaled.  Second, an actual
protected-sector zero-winding profile disproves every deterministic
strengthening \(Q_\ell^*=O(h/r)\).  These facts are reconciled with
(0.3) in Section 5.2.

## 1. Exact predecessor threshold, with all floors

Fix a first-pruned core \(E\in\mathcal D_d\) with

\[
 k=\operatorname{pk}(E),\qquad
 p=2d+1,\qquad
 y=r-d-k,\qquad
 M=y+2d=r+d-k.                                    \tag{1.1}
\]

The unrestricted inverse fibre has size

\[
 F_r(d,k)=\binom M{2d}.                            \tag{1.2}
\]

Let \(\kappa_t(E)\in\mathbb Z_p\) be the selected equality-particle
label, normalized by \(\kappa_0=0\), and put

\[
 V_G(E)=\#\{1\le t\le G:\kappa_t(E)=-1\}.        \tag{1.3}
\]

For terminal free-slot occupancy \(z\), the exact Pascal fibre is

\[
 K_z(d,k)=\binom{M-z-1}{2d-1},
 \qquad 0\le z\le y.                              \tag{1.4}
\]

### Theorem 1.1 (local-time threshold)

Let \(W_G(E)\) be the number of inverse roots above \(E\) whose initial
physical omitted label returns by time \(G<N\).  Set

\[
 s_E=\min\left\{y,
       \left\lfloor {V_G(E)\over2}\right\rfloor-1\right\}.
                                                               \tag{1.5}
\]

Then

\[
 \boxed{
 W_G(E)=
 \begin{cases}
 0,&V_G(E)<2,\\[2mm]
 \displaystyle \binom M{2d}-
     \binom{M-s_E-1}{2d},&V_G(E)\ge2.
 \end{cases}}                                      \tag{1.6}
\]

#### Proof

For a lift with terminal slot \(z\), the initial physical spacing from
the predecessor particle \(-1\) to the distinguished particle \(0\) is
\(2z+1\).  Immediately before the \((2z+2)\)-nd selection of particle
\(-1\), that particle has made exactly \(2z+1\) moves.  Its next move is
therefore the re-entry into the initial omitted edge.

The distinguished particle must have been reselected before this move.
This is automatic, rather than an extra counting condition: otherwise the
two equality particles would occupy or cross the same physical edge,
contrary to preservation of cyclic particle order.  Thus the exact
predecessor-passage criterion says

\[
 \text{the lift of slot }z\text{ returns by }G
 \quad\Longleftrightarrow\quad V_G(E)\ge2z+2.       \tag{1.7}
\]

Consequently

\[
 W_G(E)=\sum_{z=0}^{y}K_z(d,k)
          \mathbf1_{\{V_G(E)\ge2z+2\}}.            \tag{1.8}
\]

If \(V_G<2\), this is empty.  Otherwise its last index is (1.5), and the
hockey-stick identity gives

\[
 \sum_{z=0}^{s_E}\binom{M-z-1}{2d-1}
 =\binom M{2d}-\binom{M-s_E-1}{2d}.
\]

This proves (1.6).  \(\square\)

In the audited saddle tube

\[
 |d-r/2|+|k-r/6|\le2\sqrt{r\log r},               \tag{1.9}
\]

one has, uniformly,

\[
 {K_0(d,k)\over F_r(d,k)}={2d\over M}
 ={3\over4}+O\!\left(\sqrt{\log r\over r}\right).\tag{1.10}
\]

Therefore

\[
 \boxed{
 \left({3\over4}-o(1)\right)F_r(d,k)
       \mathbf1_{\{V_G\ge2\}}
 \le W_G(E)
 \le F_r(d,k)\binom{V_G(E)}2.}                    \tag{1.11}
\]

The first floor in (1.5) is essential: \(V_G=2\) permits exactly
\(z=0\), while \(V_G=3\) still permits only \(z=0\).

## 2. The exact three-point trace

Let

\[
 \mathsf N(d,k)={1\over d}\binom dk\binom d{k-1}\tag{2.1}
\]

be the Narayana size of the peak cell, and define

\[
 T_{u,v}(d,k)=
 \#\{E\in\mathcal D_d:\operatorname{pk}(E)=k,
             \ \kappa_u(E)=\kappa_v(E)=-1\}.      \tag{2.2}
\]

Double counting pairs of predecessor occurrences gives the integral
identity

\[
 \boxed{
 \sum_{\substack{E\in\mathcal D_d\\\operatorname{pk}(E)=k}}
       \binom{V_G(E)}2
 =\sum_{1\le u<v\le G}T_{u,v}(d,k).}              \tag{2.3}
\]

Let \(\zeta=e^{2\pi i/p}\).  Character orthogonality gives

\[
 T_{u,v}(d,k)
 ={\mathsf N(d,k)\over p^2}
 +{1\over p^2}
  \sum_{\substack{a,b\in\mathbb Z_p\\(a,b)\ne(0,0)}}
  \sum_E
  \zeta^{a(\kappa_u(E)+1)+b(\kappa_v(E)+1)}.      \tag{2.4}
\]

For a real Gram form, on the finite peak cell put

\[
 f_t(E)=\mathbf1_{\{\kappa_t(E)=-1\}},\qquad
 h_t=f_t-p^{-1}\mathbf1,
 \qquad \mu_t=\langle h_t,\mathbf1\rangle.       \tag{2.5}
\]

Then the nonuniform excess \(\mathfrak X_G(d,k)\), obtained by summing the
second term of (2.4) over \(u<v\), satisfies exactly

\[
 \boxed{
 \mathfrak X_G(d,k)
 ={G-1\over p}\sum_{t=1}^G\mu_t
 +{1\over2}\left\|\sum_{t=1}^Gh_t\right\|_2^2
 -{1\over2}\sum_{t=1}^G\|h_t\|_2^2.}            \tag{2.6}
\]

Indeed, expand
\(T_{u,v}=\mathsf N/p^2+(\mu_u+\mu_v)/p+
\langle h_u,h_v\rangle\), then use

\[
 \sum_{u<v}\langle h_u,h_v\rangle
 ={1\over2}\left\|\sum_th_t\right\|_2^2
  -{1\over2}\sum_t\|h_t\|_2^2.
\]

This audit shows why one-time homomesy is insufficient: even if every
\(\mu_t\) vanished, the coherent Gram term would remain.

## 3. Coefficient audit at the Pascal saddle

The complete outer mass of cell \((d,k)\) is

\[
 \mathsf M_r(d,k)=F_r(d,k)\mathsf N(d,k).          \tag{3.1}
\]

In (1.9),

\[
 p=r+O(\sqrt{r\log r}),\qquad
 G=2A\sqrt r+O_A(1).                              \tag{3.2}
\]

Hence

\[
 {\binom G2\over p^2}
 \le {2A^2+o_A(1)\over r}.                        \tag{3.3}
\]

Since the Pascal cells partition \(\mathcal D_r\), summing the uniform
term of (2.3) gives

\[
 \boxed{
 \sum_{(d,k)\text{ in }(1.9)}
 F_r(d,k){\binom G2\over p^2}\mathsf N(d,k)
 \le(2A^2+o_A(1)){B_r\over r}.}                  \tag{3.4}
\]

The already-audited moderate-deviation estimate says that the total outer
mass outside (1.9) is \(o(B_r/r)\).  Combining (1.11), (2.3), and (3.4)
therefore proves the following exact conditional theorem.

### Theorem 3.1 (trace-excess criterion)

If

\[
 \boxed{
 \sum_{(d,k)\text{ in }(1.9)}
 F_r(d,k)\,\mathfrak X_G(d,k)
 =O_A(B_r/r),}                                    \tag{3.5}
\]

then the total number of quotient roots which start a return by time
\(G\) is \(O_A(B_r/r)\), and consequently (0.1) holds.

This implication covers zero and positive winding simultaneously.
The local-time identity was derived from the adjacent-particle passage,
not from the zero-winding equation; the zero-winding fan is used only in
the separate profile analysis of Sections 4--6.

No absolute value is needed in (3.5): it is an upper bound on the total
real excess.  A positive-part or absolute-character estimate is a
stronger sufficient assertion.

Equivalently, the exact missing estimate is

\[
 \boxed{
 \sum_{(d,k)\text{ in }(1.9)}F_r(d,k)
 \sum_{1\le u<v\le G}
 \left(T_{u,v}(d,k)-{\mathsf N(d,k)\over(2d+1)^2}\right)
 =O_A(B_r/r).}                                    \tag{3.6}
\]

This retains the peak coordinate \(k\), the exact inverse-Pascal weight,
the predecessor label, and the full two-time reduced PBBS chronology.

## 4. All-level common-phase fan coordinates

Now suppose \(D\in\mathcal D_r\) starts a genuine zero-winding return of
gap \(2h+1\), so \(h=\operatorname{ht}(D)\).  Put

\[
 D^{(j)}=\partial^jD,\qquad
 r_j={1\over2}|D^{(j)}|,
\]

and let

\[
 \ell=\min\{j:r_j=h-j\}                           \tag{4.1}
\]

be the first mountain depth.  The audited tight-return fan gives, at
level \(j\), the \(j+1\) exact child returns with consecutive particle
labels.  We use it one inverse level earlier.

### Theorem 4.1 (wrapped fan-slot extension)

At inverse level \(j\), \(1\le j\le\ell\), put

\[
 t_j=\min\{j,2r_j\}.                               \tag{4.2}
\]

After every phase-local adjacency condition is transported to one fixed
phase of the inverse fibre, at least \(t_j\) distinct weak-composition
coordinates are fixed to prescribed nonnegative integers.  Consequently,
for every realizable rank profile and fixed level-\(\ell\) mountain core,
the compatible tower count is at most the unrestricted tower count times

\[
 \boxed{
 Q_\ell^*(\mathbf r)=
 \prod_{j=1}^{\ell}
 {\binom{r_{j-1}+r_{j+1}-t_j}{\,2r_j-t_j\,}
  \over
  \binom{r_{j-1}+r_{j+1}}{2r_j}}.}                \tag{4.3}
\]

#### Proof

At level \(j-1\), the fan intervals beginning at the first \(j\)
step-two phases force adjacency between \(j\) consecutive labelled
particle gaps at level \(j\).  There are \(p_j=2r_j+1\) cyclic particle
gaps.  Hence these conditions involve at least \(\min\{j,p_j\}\)
distinct labels.

Transport to a fixed phase preserves the label of a particle gap, but
changes its numerical spacing by a core-determined selection-count
difference.  Thus each phase-local spacing-one equation fixes the
corresponding initial free-slot coordinate to one prescribed integer.
Existence of the original fan makes every prescribed value nonnegative.

For a uniform upper bound it is enough to retain
\(t_j=\min\{j,p_j-1\}\) distinct coordinates.  If their prescribed total
is \(w\ge0\), the remaining \(y_j-w\) free leaves are distributed among
\(p_j-t_j\) boxes, where

\[
 y_j=r_{j-1}-2r_j+r_{j+1}.                        \tag{4.4}
\]

The count is largest at \(w=0\), and then equals

\[
 \binom{y_j+2r_j-t_j}{2r_j-t_j}
 =\binom{r_{j-1}+r_{j+1}-t_j}{2r_j-t_j}.
\]

The unrestricted count is
\(\binom{r_{j-1}+r_{j+1}}{2r_j}\).  Conditional fibre bounds multiply
down the tower, proving (4.3).  \(\square\)

The truncation at \(2r_j\), rather than \(2r_j+1\), is exact.  Fixing all
but one of the \(p_j\) weak-composition boxes already leaves at most one
choice after the total mass is specified.

## 5. Curvature identity and an unconditional square-root envelope

The leaf counts

\[
 L_j=r_j-r_{j+1}
\]

are nonincreasing under simultaneous leaf deletion.  Thus
\(y_j=L_{j-1}-L_j\ge0\).  At the mountain endpoint,

\[
 r_\ell=h-\ell,qquad r_{\ell+1}=h-\ell-1,
 \qquad L_\ell=1.                                 \tag{5.1}
\]

Twice summing the discrete curvature gives

\[
 r_j=h-j+
     \sum_{q=j+1}^{\ell}(q-j)y_q                 \tag{5.2}
\]

and, at \(j=0\),

\[
 \boxed{r=h+\sum_{q=1}^{\ell}q y_q.}             \tag{5.3}
\]

This proves (0.2).

### Theorem 5.1 (all-level square-root profile bound)

For every zero-winding fan profile,

\[
 \boxed{Q_\ell^*(\mathbf r)\le\sqrt{h/r}.}        \tag{5.4}
\]

#### Proof

For the level factor in (4.3), deleting successive prescribed boxes gives

\[
 {\binom{y_j+2r_j-t_j}{2r_j-t_j}
  \over\binom{y_j+2r_j}{2r_j}}
 =\prod_{i=0}^{t_j-1}
   {2r_j-i\over2r_j+y_j-i}
 \le\left(1+{y_j\over2r_j}\right)^{-t_j}.        \tag{5.5}
\]

Define the remaining weighted curvature

\[
 R_j=h+\sum_{q=j+1}^{\ell}q y_q.                  \tag{5.6}
\]

Then \(R_\ell=h\), \(R_0=r\), and

\[
 R_{j-1}=R_j+j y_j.                               \tag{5.7}
\]

Equation (5.2) gives

\[
 R_j-r_j=j\left(1+\sum_{q=j+1}^{\ell}y_q\right)
 \ge0.                                            \tag{5.8}
\]

Also \(R_j\ge h>j\).  Hence, whether
\(t_j=j\) or \(t_j=2r_j\),

\[
 {t_j\over2r_j}\ge {j\over2R_j}.                 \tag{5.9}
\]

Bernoulli's inequality and \(1+x/2\ge\sqrt{1+x}\) now give

\[
 \begin{aligned}
 \left(1+{y_j\over2r_j}\right)^{t_j}
 &\ge1+{t_jy_j\over2r_j}\\
 &\ge1+{j y_j\over2R_j}\\
 &\ge\sqrt{1+{j y_j\over R_j}}
  =\sqrt{R_{j-1}/R_j}.
 \end{aligned}                                    \tag{5.10}
\]

Multiplication over \(1\le j\le\ell\) telescopes to

\[
 (Q_\ell^*)^{-1}\ge\sqrt{R_0/R_\ell}=\sqrt{r/h},
\]

which proves (5.4).  \(\square\)

For \(h\le A\sqrt r\), (5.4) is
\(Q_\ell^*=O_A(r^{-1/4})\).  The harmonic profile has the smaller sharp
order \(\Theta(1/h)=\Theta_A(r^{-1/2})\).  Thus Theorem 5.1 is not yet
coefficient-one sufficient; it quantifies exactly how much is obtainable
from terminal curvature without a sharper extremal theorem.

If the prescribed values at level \(j\) have positive total \(w_j\), the
zero-value envelope gains the exact additional factor

\[
 \boxed{
 {\binom{y_j-w_j+2r_j-t_j}{2r_j-t_j}
  \over\binom{y_j+2r_j-t_j}{2r_j-t_j}}
 =\prod_{a=0}^{w_j-1}
   {y_j-a\over y_j+2r_j-t_j-a}.}                  \tag{5.11}
\]

On the harmonic profile, one positive unit at depth \(j\) costs
\(\Theta(j^{-2})\).  Even in the nonwrapped mesoscopic regime
\(j\le r_j\), however, the best uniform conclusion from this one level is
only \(O(1/j)\).  Indeed, with \(x=y_j/(2r_j)\), (5.5) and (5.11) are at
most

\[
 (1+x)^{-j}{2x\over1+2x},
\]

whose supremum is \(O(1/j)\): for \(x\le1/j\) use
\(2x/(1+2x)\le2/j\), and for \(x>1/j\) the derivative, or
\((1+x)^j\ge1+jx\), gives the same order.  The choice
\(x\asymp1/j\) attains order \(1/j\).  Near the wrapped terminal levels
\(j>r_j\), even this one-level statement is false and the curvature
factors from the other levels must be retained.  Therefore the harmonic
\(j^{-2}\) observation cannot be globalized without controlling the full
rank curvature or proving positive prescribed mass at more than one
independent depth.

### 5.2 Sharp reconciliation with the two actual constructions

The square-root envelope cannot be replaced by the harmonic
\(O(h/r)\) envelope uniformly over genuine return profiles.  The
independently audited protected-sector construction takes

\[
 h=10^{3K},\qquad r=h^2,\qquad \ell=10^K,
\]

and places path forests only at the sparse depths \(J_t=10^t\), with
multiplicities

\[
 Y_t={2^{K-t}h\over J_t}\quad(1\le t\le K),
\]

plus \(h^2-2^Kh\) length-one branches.  Every pre-spine forest is empty
and every post-spine forest at depth \(a\) has relative height \(a\).
The corrected no-preemption criterion therefore proves an actual
zero-winding return of duration \(h\), not merely a formal rank profile.
Its exact fan envelope \(Q\) obeys

\[
 Q\,{r\over h}=Qh>
 {9\over10}\bigl(2e^{-3/5}\bigr)^K.               \tag{5.12}
\]

Since \(2e^{-3/5}>1\), the right side diverges.  Hence no absolute
constant can make \(Q=O(h/r)\) true for all actual fans.  There is no
conflict with (5.4): here \(\sqrt{h/r}=h^{-1/2}\), while (5.12) only gives
\(Q\ge h^{-1+\varepsilon}\) for the fixed positive
\(\varepsilon=\log(2e^{-3/5})/(3\log10)<1/2\).

At the global counting level, the independently audited overlap-one
construction gives exact genuine zero-winding roots with generating
function

\[
 Z_{r,s}^{(1)}=[z^{r-s}]G_s(z)
\]

and critical Boltzmann mass

\[
 4^{-s}G_s(1/4)=
 \begin{cases}
 \displaystyle {2\over(t+1)^3(t+2)},&s=2t,\\[2mm]
 \displaystyle {2\over(t+1)(t+2)^3},&s=2t+1.
 \end{cases}                                      \tag{5.13}
\]

The cited coefficient argument proves that for fixed
\(0<a<b<\infty\), some \(c>0\), and infinitely many \(r\),

\[
 \sum_{a\sqrt r\le s\le b\sqrt r}Z_{r,s}^{(1)}
 \ge c\,{B_r\over N}.                              \tag{5.14}
\]

All but \(\exp(o(r))\) of these starts lie on long quotient cycles.
Equation (5.14) rules out an \(o(B_r/N)\) enumeration theorem, but it
does not refute the desired \(O(B_r/N)\) bound and does not itself give an
edge-disjoint packing lower bound.  Thus the coefficient in the present
big-oh gate is genuinely critical: neither a deterministic
\(Q=O(h/r)\) profile theorem nor an extra vanishing start factor is
available.  Only cross-phase trace packing remains capable of supplying
the required upper bound.

## 6. Why marginal fan capacity does not tensorize with trace length

The following integral model is the exact obstruction.

Let \(H\mid L\) and \(H\mid F\), and take the product edge set
\(\mathbb Z_L\times[F]\).  Partition the fibre labels into equal classes
\(C_0,\ldots,C_{H-1}\).  A start \((i,v)\) is eligible when

\[
 v\in C_{i\bmod H},                                \tag{6.1}
\]

and its interval is \([i,i+H)\times\{v\}\).  Every phase has exactly
\(F/H\) eligible vectors.  For fixed \(v\in C_a\), the starts are the
phases congruent to \(a\pmod H\), so their length-\(H\) intervals tile the
base cycle.  Different fibres use disjoint edges.  Therefore all eligible
intervals are pairwise edge-disjoint and their number is

\[
 \boxed{LF/H,}                                     \tag{6.2}
\]

not \(LF/H^2\).

In indicators \(x_{i,v}\), the obstruction is the exact cross-phase
identity

\[
 \sum_{i,v}x_{i,v}x_{i+H,v}=LF/H,                 \tag{6.3}
\]

where independent density \(1/H\) would give \(LF/H^2\).  Thus a
profilewise bound \(Q=O(1/H)\) and the interval edge budget combine only
by a minimum unless a common-base two-phase estimate is added.

For the actual PBBS fan, let \(\mathcal E_i\) denote the set of common-base
Pascal vectors satisfying all transported fan equations at phase \(i\).
A sufficient transported certificate, strong enough to rule out (6.1), is

\[
 \boxed{
 \sum_i\sum_v
 \mathbf1_{\{v\in\mathcal E_i\}}
 \mathbf1_{\{v\in\mathcal E_{i+H}\}}
 =O_A\!\left({1\over H^2}
              \sum_iF_i\right),}                 \tag{6.4}
\]

with the analogous inequality at every actual separation between starts
of a packed family.  A slightly more invariant sufficient statement is

\[
 \boxed{
 \sum_{I\in\mathcal P}|I|
 \le {C_A\over H}\sum_{\text{base edges }e}F(e)} \tag{6.5}
\]

for every packed family \(\mathcal P\) in a Gaussian height band, where
the left side counts transported fan-compatible clone edges and \(F(e)\)
is the full inverse-tower capacity.  Since \(|I|\asymp H\), (6.5) gives
\(|\mathcal P|=O_A(B_r/H^2)=O_A(B_r/r)\).

Neither (6.4) nor (6.5) follows from the marginal factors (4.3).  The
residue construction proves this failure with the same quantifiers.

## 7. Exact proved and conditional boundary

### Proved

1. The floor-correct local-time identity (1.6) and saddle comparison
   (1.11).
2. The exact three-point Fourier/Gram decomposition (2.3)--(2.6).
3. The uniform saddle contribution with coefficient
   \(2A^2+o_A(1)\), equation (3.4).
4. The coefficient-correct implication from the weighted trace excess
   (3.6) to the new linear-seam target.
5. The wrapped all-level fan-slot theorem, with
   \(t_j=\min\{j,2r_j\}\).
6. The exact curvature identity (5.3) and unconditional envelope
   \(Q_\ell^*\le\sqrt{h/r}\).
7. The exact positive-prescribed-mass factor (5.11).
8. The integral residue-class obstruction to multiplying marginal fan and
   interval factors.

### Not proved

1. The PBBS trace-excess estimate (3.6).
2. The common-base fan incidence estimate (6.4) or (6.5).
3. The requested bound \(\overline\nu_H=O_A(B_r/r)\).
4. Coefficient one.

The first remaining theorem can be stated without any relaxed statistic:

\[
 \boxed{
 \text{fixed-peak PBBS predecessor indicators have weighted
 three-point excess }O_A(B_r/r).}
\]

It must use the actual first-maximum/peak-deletion chronology.  Particle
homomesy, bounded terminal slot, a marginal harmonic fan factor, and the
interval edge budget do not imply it.  This is also why every consequence
of the retracted primitive-sector density claim has been removed from the
present line.
