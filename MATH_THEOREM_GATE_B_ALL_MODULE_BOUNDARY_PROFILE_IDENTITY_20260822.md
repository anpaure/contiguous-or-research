# The all-module boundary-profile identity closes the complete `W_2` Hilbert scalar

**Date:** 2026-08-22

**Status.**  This note proves, for every `r>=5` and every depth-two module
`2<=j<=r-2`,

\[
 \boxed{\alpha^{(2)}_{r,j}\ge {1\over108r^6}},\qquad
 \boxed{\alpha^{(2)}_{r,j}\Theta_{r,j}\ge {1\over3888r^{12}}}. \tag{0.1}
\]

Thus (H.47), including every dependent `W_2` module, is closed.  The proof
does not estimate `xi` or invert a conditioned two-column Gram matrix.  It
uses a signed average over unique-shallow-window boundary events and one
exact three-profile identity.  Transfer from `W_2` to full exposure and the
downstream inverse/stopping/gain requirements remain separate.

## 1. Complete-state objects

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=b-k=r+3,
 \qquad N={b\choose k}.                              \tag{1.1}
\]

On the position cycle `Z_b`, write `I_s(t)` for the cyclic interval of
length `s` starting at `t`, and set

\[
 X=\{I_r(t),I_{r-1}(t):t\in\mathbb Z_b\},
 \quad A=I_r(0),\quad B=I_{r-1}(0),\quad
 E_0=X-\{A,B\}.                                    \tag{1.2}
\]

The orbit of `E_0` under all coordinate permutations is the complete
punctured configuration catalogue.  For central targets `S,T,U`, let
`deg(S,T,U)` be the number of configurations containing all distinct
displayed conditions.  Simultaneous coordinate relabelling preserves this
degree.

Throughout, (L^2(S_b)) means the probability-normalized space for the
uniform measure on (S_b):

\[
 \langle f,h\rangle={1\over b!}\sum_{g\in S_b}f(g)h(g),
 \qquad \|f\|_2^2={1\over b!}\sum_{g\in S_b}|f(g)|^2.          \tag{1.3}
\]

Fix `j` ordered distinguished coordinate pairs
`(a_i,b_i)`, `1<=i<=j`.  For an `s`-set `S`, put

\[
 H_{s,j}(S)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in S\}}-\mathbf1_{\{b_i\in S\}}).          \tag{1.4}
\]

For a coefficient vector `x` on the `s`-sets, its harmonic lift is

\[
                         R_x(g)=\sum_Sx(S)H_{s,j}(gS).        \tag{1.5}
\]

The four constraint columns and the shallow target are

\[
 c_s=R_{\mathbf1_{\{I_s(t):1\le t\le b-1\}}},
 \qquad s\in\{r,r-1\},                                \tag{1.6}
\]

\[
 W_{2,s}(S)=\sum_{\{T,U\}\in{E_0\choose2}}\deg(S,T,U),
 \qquad w_s=R_{W_{2,s}},                             \tag{1.7}
\]

\[
 q=R_{\mathbf1_{\{I_k(t):t\in\mathbb Z_b\}}}.       \tag{1.8}
\]

Accordingly,

\[
 \alpha^{(2)}_{r,j}=
 {\operatorname {dist}(q,
   \operatorname {span}\{c_r,c_{r-1},w_r,w_{r-1}\})^2
  \over\|q\|_2^2}.                                  \tag{1.9}
\]

No independence of these four columns is assumed.

## 2. Signed boundary averages at every harmonic level

For \(t\in\mathbb Z_b\), put \(K_t=I_k(t)\).  Let \(\mathcal B_t\) denote the following set
of ordered injective placements of the `2j` distinguished labels:

1. pair one occupies the boundary edge `(t-1,t)`;
2. pair two occupies the boundary edge `(t+k-1,t+k)`;
3. each remaining pair has one endpoint in
   `K_t-{t,t+k-1}` and one endpoint in
   `K_t^c-{t-1,t+k}`;
4. every pair may use either orientation.

The choices are labelled and injective, so

\[
 |\mathcal B_t|
 =2^j(k-2)_{j-2}(\ell-2)_{j-2}.                    \tag{2.1}
\]

For \(z\in\mathcal B_t\), let

\[
 \varepsilon(z)=H_{k,j}(K_t)\in\{-1,1\}.           \tag{2.2}
\]

The two boundary pairs force any `k`-interval splitting all distinguished
pairs to have exactly the two displayed boundary edges.  The other arc has
length `ell!=k`; hence `K_t` is the unique such `k`-interval and

\[
                         q(z)=\varepsilon(z).       \tag{2.3}
\]

The same argument shows that no interval of length `r` or `r-1` splits the
first two pairs, so

\[
                         c_r(z)=c_{r-1}(z)=0.        \tag{2.4}
\]

Define the two signed profiles

\[
 \omega_{s,j}(t)={1\over|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)w_s(z),
 \qquad s\in\{r,r-1\},                             \tag{2.5}
\]

and their best constant-approximation error

\[
 \rho_{r,j}={1\over b}\min_{x,y\in\mathbb R}
 \sum_{t\in\mathbb Z_b}
 (1-x\omega_{r,j}(t)-y\omega_{r-1,j}(t))^2.        \tag{2.6}
\]

### Lemma 2.1 (boundary quotient)

For every `2<=j<=k`,

\[
 \boxed{
 \alpha^{(2)}_{r,j}\ge
 {\rho_{r,j}\over b\,k(k-1)\ell(\ell-1)}.}         \tag{2.7}
\]

#### Proof

The sets \(\mathcal B_t\) are disjoint, and a uniform permutation gives a
uniform ordered injective `2j`-tuple.  Indeed, the unordered position edge
occupied by pair one is exactly `\{t-1,t\}`, so it determines `t`; hence
no placement lies in two distinct boundary events.  On \(\mathcal B_t\), multiply the
residual by `epsilon(z)` and use (2.3)--(2.4).  Jensen's inequality gives,
for every four coefficients `a_M,a_L,x,y`,

\[
\begin{split}
 \|q-a_Mc_r-a_Lc_{r-1}-xw_r-yw_{r-1}\|_2^2
 \ge{}&{|\mathcal B_t|\over(b)_{2j}}
 \sum_t(1-x\omega_{r,j}(t)-y\omega_{r-1,j}(t))^2\\
 \ge{}&{b|\mathcal B_t|\over(b)_{2j}}\rho_{r,j}.
                                                               \tag{2.8}
\end{split}
\]

For one fixed `k`-set,

\[
 \kappa_{k,j}=\|H_{k,j}(gK_t)\|_2^2
 ={2^j(k)_j(\ell)_j\over(b)_{2j}}.                 \tag{2.9}
\]

Since `q` is a sum of `b` single-interval lifts, the triangle inequality
gives \(\|q\|_2\le b\sqrt{\kappa_{k,j}}\).  Divide (2.8) by this upper bound
squared and use (2.1), (2.9): all factors involving `j-2` cancel, leaving
(2.7). `square`

For auditability, the signed average over the last `m=j-2` pairs is an
explicit Hahn polynomial.  After the four boundary positions are removed,
let the inside and outside pool sizes be `K=k-2`, `L=ell-2`, and suppose a
root set meets them in `a,c` points.  The unnormalised signed injection sum
is

\[
 \sum_{h=0}^m(-1)^{m-h}{m\choose h}
 (a)_h(K-h)_{m-h}(c)_{m-h}(L-m+h)_h.               \tag{2.10}
\]

Indeed, expand the `m` factors according to whether their inside or outside
endpoint supplies the membership indicator, then place the constrained
endpoints first and all unconstrained endpoints afterward.  This gives an
exact finite evaluator for (2.5): divide (2.10) by
`(K)_m(L)_m` to obtain the signed average over the remaining endpoint
placements.  To see why orientations introduce no further factor, write
`u_i` for the endpoint of pair `i` inside `K_t`, `v_i` for its endpoint
outside, and `sigma_i=+1` or `-1` according as `a_i` or `b_i` is at
`u_i`.  For every root set `S`, write `S'=gS` for its positional image in
this placement.  Then

\[
 \varepsilon(z)H_{s,j}(gS)
 =\prod_i\sigma_i\prod_i
   \sigma_i(\mathbf1_{\{u_i\in S'\}}-\mathbf1_{\{v_i\in S'\}})
 =\prod_i(\mathbf1_{\{u_i\in S'\}}-\mathbf1_{\{v_i\in S'\}}). \tag{2.11}
\]

Thus the signed summand is orientation-independent.  The `2^j`
orientations cancel between the event sum and its cardinality; the same
`2^j` cancels between (2.1) and `kappa_(k,j)` in the quotient (2.7).

## 3. Six-state localization

It is useful to extend only the **blocker-pair sum** in (1.7) from `E_0`
to the full cyclic target set `X`, while retaining the same equivariant
degree kernel.  Let `Omega_s(t)` be the resulting signed profile.  Since
`X` is cyclically invariant and the degree kernel is equivariant,
`Omega_s(t)` is independent of `t`; write its value as `Omega_s`.

Let `C_s(t)=Omega_s-omega_(s,j)(t)` be the contribution from pairs in
`{X choose 2}` which meet the omitted set `{A,B}`.

### Lemma 3.1 (puncture localization)

For both root shores and every harmonic level,

\[
 C_s(t)=0\quad\text{unless}\quad
 t\in\{0,1,2,r-1,r,r+3\}.                         \tag{3.1}
\]

#### Proof

Fix a pair of blockers `T,U` meeting `{A,B}`.  If the two endpoints at one
of the displayed boundary edges lie in the same cell of the partition
generated by `T,U`, let `pi` transpose those two **positions**.  In the
positional root-set sum, pair `S'` with `pi S'`.  The transposition fixes `T,U`; hence
equivariance gives
`deg(S',T,U)=deg(pi S',T,U)`.  It also fixes all other distinguished
positions and swaps membership at this pair, so the orientation-free
product in (2.11) changes sign.  (This is a transposition of positions in
the root set, not a reversal of placement orientation.)  The paired signed
contribution is zero.  Thus both event edges must be boundaries of `T` or
`U`.

If neither event edge were a boundary of the omitted blocker, the other
blocker would have both event edges as its boundaries.  That is impossible:
the two intervening arc lengths are `k=r-2` and `ell=r+3`, not `r` or
`r-1`.  Hence one event edge is a boundary of an omitted target.  The
boundaries of `A` give `t in {0,2,r,r+3}`, while those of `B` give
`t in {0,1,r-1,r+3}`.  Their union is (3.1). `square`

For `r>=5`, neither event edge at `t=3` is an omitted boundary, so

\[
                         \omega_{s,j}(3)=\Omega_s.             \tag{3.2}
\]

## 4. The exact three-profile identity

At a boundary event, a nonzero complete blocker pair has one target
supplying each displayed event edge; no one central target can supply both.
Classify the supplier at each edge as `S` if that edge is its cyclic start
boundary and `E` if it is its cyclic end boundary.  Let

\[
                         F_{SS},F_{SE},F_{ES},F_{EE}           \tag{4.1}
\]

be the four total signed contributions to the complete profile, on either
fixed root shore and harmonic level.  Cyclically rotate the two events
used below so that their displayed boundary edges are aligned before using
this common notation; complete-profile invariance makes the value unchanged.
Their sum is `Omega_s`.

Reflection of the position cycle through the two event edges preserves the
complete target set and the equivariant degree kernel, interchanges start
and end at both edges, and merely swaps the first two distinguished pairs.
The signed boundary average is unchanged: after reflection and the pair
swap, formula (2.11) is the same product, merely with its commuting factors
reordered.  Therefore

\[
                         \boxed{F_{SS}=F_{EE}.}                \tag{4.2}
\]

At `t=0`, the common omitted boundary `(-1,0)` is the left event edge.
The omitted targets are exactly the two central targets which **start** at
that edge.  Consequently

\[
                         C_s(0)=F_{SS}+F_{SE}.                 \tag{4.3}
\]

At `t=ell`, the same omitted boundary is the right event edge, so

\[
                         C_s(\ell)=F_{SS}+F_{ES}.              \tag{4.4}
\]

The pair `{A,B}` itself contributes zero at these events because it cannot
supply the other event edge, so there is no double-counting exception in
(4.3)--(4.4).  Equations (4.1)--(4.2) now give

\[
 C_s(0)+C_s(\ell)
 =2F_{SS}+F_{SE}+F_{ES}
 =F_{SS}+F_{SE}+F_{ES}+F_{EE}
 =\Omega_s.                                       \tag{4.5}
\]

Using `omega=Omega-C` and (3.2) proves the key identity

\[
 \boxed{
 \omega_{s,j}(0)+\omega_{s,j}(\ell)=\omega_{s,j}(3),
 \qquad s\in\{r,r-1\}.}                           \tag{4.6}
\]

This is an exact vector identity, uniform in `j`.

### Theorem 4.1 (uniform boundary error)

For every `r>=5` and `2<=j<=r-2`,

\[
                         \boxed{\rho_{r,j}\ge {1\over3b}.}   \tag{4.7}
\]

#### Proof

Every constraint prediction
`p_t=x omega_(r,j)(t)+y omega_(r-1,j)(t)` obeys
`p_0+p_ell-p_3=0` by (4.6).  For errors `e_t=1-p_t`,

\[
                         e_0+e_\ell-e_3=1.                    \tag{4.8}
\]

Cauchy--Schwarz gives
`e_0^2+e_ell^2+e_3^2>=1/3`.  The full residual sum is no smaller; divide by
`b` and take the infimum. `square`

## 5. Uniform complete-state scalar

Combining (2.7) and (4.7), and using
`b<=3r`, `k(k-1)<=r^2`, and `ell(ell-1)<=4r^2`, gives

\[
 \boxed{
 \alpha^{(2)}_{r,j}\ge
 {1\over3b^2k(k-1)\ell(\ell-1)}
 \ge {1\over108r^6}.}                              \tag{5.1}
\]

For completeness, the same boundary event gives the orbit lower bound.
Let

\[
 F_{r,j}={\|q\|_2^2\over\kappa_{k,j}},\qquad
 \Theta_{r,j}={N\over b^2}F_{r,j}.                 \tag{5.2}
\]

Indeed, the cyclic-window incidence Gram acts by the unconstrained
eigenvalue `theta_(r,j)` on this harmonic module, while the squared
counting norm of `H_(k,j)` is `N kappa_(k,j)`.  Hence
`||q||^2=N theta kappa`, so `F=N theta` and the displayed `Theta` is the
relative-density orbit factor.

On one fixed \(\mathcal B_t\), `|q|=1`, so (2.1), (2.9) imply

\[
 F_{r,j}\ge {1\over k(k-1)\ell(\ell-1)},
 \qquad
 \Theta_{r,j}\ge
 {N\over b^2k(k-1)\ell(\ell-1)}.                  \tag{5.3}
\]

Since `N>=1`, multiplication with (5.1) yields

\[
 \boxed{
 \alpha^{(2)}_{r,j}\Theta_{r,j}
 \ge {N\over3b^4[k(k-1)\ell(\ell-1)]^2}
 \ge {1\over3888r^{12}}.}                         \tag{5.4}
\]

This proves (0.1) and closes (H.47) without separating rank-two and
dependent modules.

## 6. Exact checks and remaining scope

The checker independently:

1. verifies the extra-pair injection polynomial (2.10) against brute-force
   signed placements on small pools;
2. constructs the exact Hahn--Venn `W_2` coefficient vectors for
   `5<=r<=8` and every `2<=j<=r-2`;
3. verifies the six-state localization, (4.6), and (4.7) exactly;
4. verifies rank two of the two restricted profiles and rank three after
   adjoining the constant in every tested module.

The checker authenticates both local helper sources before importing them.
Their frozen SHA-256 hashes are

* `research_gate_b_allj_boundary_averages_20260822.py`:
  `f3a1e3e1cff2d585e20448e077adcc71d8b63918441b5936c7bff2430d31c2df`;
* `research_w2_hahn_venn_exact_20260822.py`:
  `8b7916edd570e7705b9154f88e66b0922d9d0f3ac05e1c8ed874eaac695c04d4`.

The observed `rho_(r,j)` values in those exact tests lie between `.0498`
and `.0779`, far above the deliberately crude `1/(3b)` theorem.

What remains open is not (H.47).  One must still transfer from `W_2` to the
full exposure columns with a perturbation estimate relative to the proved
angular margin, then obtain a delocalized simultaneous inverse, stopped
stability, and logarithmic hole-aligned gain.
