# All-fibre profile propagation by one factorial generating-function supermartingale

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. The theorem

Work in the actual vertex-induced compensated annular process. Put

\[
 r=(1+o(1))m,\qquad u_t=e^{-t/r},\qquad
 \tau={1\over u_t},\qquad
 1\le\tau\le U={1\over z},
\tag{0.1}
\]

where

\[
 z=m^{-1/2}(\log m)^{B_0}
\tag{0.2}
\]

for any fixed sufficiently large \(B_0>0\). Let

\[
 q_k(S)={d_0(S)\over D_0}
\qquad(2\le |S|=k\le r)
\tag{0.3}
\]

be the exact time-zero fibre profile.

Assume the equality-resolved conditional child profile, in the form
already required by the fibre hierarchy:

\[
 \boxed{
 \sum_{w\in V(e)\setminus S}q_{k+1}(S\cup\{w\})
 \le {C\over m}q_k(S)}
\tag{CPS}
\]

for every relevant resource orbit, every \(2\le k<r\), and every event
edge \(e\) disjoint from the protected prefix \(S\). The corresponding
compensation-resource inequality is included. Repeated children and
physical equalities are counted with their factorial multiplicities.

For \(j=k-2\), use the original uniformly scaled profile stop

\[
 \boxed{
 d_t(S)\le
 A\,u_t^{-(k-1)}q_k(S)\Delta_t,
 \qquad 2\le k<r,}
\tag{PF\(_k\)}
\]

where \(A=L^{C_A}\) may be any sufficiently large polylogarithm. At
\(k=r\), terminate the extension: a full simple edge has current degree
at most one, and no child fibre is introduced.

Then, inside the ordinary degree stop and the already closed
whole-arm/equality-resolution stop,

\[
 \boxed{
 \text{total marked incidence stopped by any }
 {\rm PF}_k,\ 2\le k<r,\text{ is }O(W/(Am))=o(W).}
\tag{0.4}
\]

The result uses one generating-function supermartingale, not a finite
PFS3--PFS4--\(\cdots\) induction.

The decisive normalization facts are:

1. after the change \(\tau=1/u\), the child coefficient \(C/(mu)\)
   becomes \(O(1)\), while the order-\(k\) negative drift becomes
   \(-(k-1)/\tau\);
2. the resulting characteristic asks for the static factorial EGF only
   at

   \[
                         \xi_0=O(\log U)=O(\log m),
   \tag{0.5}
   \]

   not at \(\xi_0=\Theta(U)\);
3. ordered-child CPS therefore gives an initial EGF of order \(1/m\);
   the \(j!\) ordered histories of one depth-\(j\) profile cancel the
   coefficient \(1/j!\), so the stop itself is not weakened by a
   factorial; and
4. the total selected owner-incidence clock is

   \[
    \int_0^T r\nu_tE_t\,dt
    =(1+o(1))W(1-z),
   \tag{0.6}
   \]

   with no extra \(\log(1/z)\) or \(z^{-1}\) factor.

If CPS is available only at time zero for resource-disjoint children,
then (0.4) remains conditional: the exact next failure is its
equality-resolved column--row/compensation extension. No divergent
all-fibre clock remains after CPS is supplied.

## 1. The complete stopped fibre tower

Fix a predictable marked owner/root cohort. Resolve every physical
resource equality before assigning fibre order. A formal depth-\(j\)
fibre flag is an ordered chain

\[
 S_0\subset S_1\subset\cdots\subset S_j,
 \qquad |S_i|=i+2,
\tag{1.1}
\]

where \(S_{i+1}\setminus S_i\) is the newly exposed physical resource.
The same terminal set is deliberately retained once for every ordering
of its \(j\) new resources. Let \(H_j(t)\) be the cohort's nonnegative
marked mass of these ordered flags at fibre order

\[
                         k=j+2,\qquad0\le j\le r-2,
\tag{1.2}
\]

normalized by its natural current base

\[
                         D_0u_t^{r-k}
\tag{1.3}
\]

and by the existing owner/root incidence reference. Every term is killed
when its marked incidence, protected prefix, or displayed row dies.
Consequently terminal deaths are favorable.

The exact pair-conditioned decay of a \(k\)-fibre has margin
\((k-1)/r\): an active full row dies at rate at least
\(1-o(1/r)\), whereas its natural base in (1.3) decays at rate
\((r-k)/r\). The profile error already absorbed by the whole-arm stop is
integrable and will be denoted \(\epsilon_t\), with

\[
                         \int_0^T|\epsilon_t|\,dt=o(1).
\tag{1.4}
\]

### Lemma 1.1 (all-order child inequality)

After multiplication by the harmless integrating factor associated with
\(\epsilon_t\), the stopped generator satisfies, simultaneously for
\(0\le j<r-2\),

\[
 \boxed{
\mathcal G_tH_j
 \le-{j+1\over r}H_j
      +{C\over m u_t}H_{j+1}.}
\tag{1.5}
\]

At the terminal level,

\[
                         \mathcal G_tH_{r-2}
 \le-{r-1\over r}H_{r-2}.
\tag{1.6}
\]

#### Proof

Write a current \(k\)-fibre as a sum of active full rows containing its
protected \(k\)-set. The physical-union hazard of each row, minus the
transport of \(u^{r-k}\), supplies the first term in (1.5). Events private
to one marginal are already differentiated by the current base.

A remaining positive common-event deficit has at least one new resource
\(w\) in the event edge. Expose its first new resource and reverse the
sum over the current \(k\)-fibres and event columns. The resulting object
is exactly one \((k+1)\)-fibre. CPS costs \(C/m\), and conditioning the
extra resource to survive rather than using the \(k\)-fibre base costs
\(u_t^{-1}\). This gives the second term in (1.5).

If one event supplies several new resources, equality resolution and
falling-factorial expansion assign it to the corresponding ordered child
flags. Thus an unordered terminal profile with \(j\) exposed resources
has exactly \(j!\) formal histories. Division by \(j!\) in the
generating function below counts that terminal profile once. This is
precisely the closed whole-arm factorial package; no
maximum-intersection estimate is substituted.

At \(k=r\), the protected set is a full simple edge. Its current
codegree is at most one and there is no \((r+1)\)-fibre. This proves
(1.6). \(\square\)

Lemma 1.1 is the only dynamic catalogue-specific input used below.

## 2. One factorial generating function

Define

\[
 \Phi(\tau,\xi)
 =\sum_{j=0}^{r-2}H_j(\tau){\xi^j\over j!}.
\tag{2.1}
\]

Since \(d\tau/dt=\tau/r\), equations (1.5)--(1.6) imply

\[
 \boxed{
 \partial_\tau\Phi
 \le-{1\over\tau}
       \bigl(\xi\partial_\xi\Phi+\Phi\bigr)
       +C_1\partial_\xi\Phi,}
\tag{2.2}
\]

where \(C_1=C(r/m)=O(1)\). There is no positive top-boundary term,
because \(H_{r-1}=0\).

Fix the terminal inverse density \(U=1/z\), and solve

\[
 {d\xi\over d\tau}={\xi\over\tau}-C_1,
 \qquad
 \xi(U)=1.
\tag{2.3}
\]

The solution is

\[
 \boxed{
 \xi(\tau)
 =\tau\left({1\over U}
       +C_1\log{U\over\tau}\right).}
\tag{2.4}
\]

It is positive on \([1,U]\). Since it is concave, its minimum occurs at
an endpoint; for large \(m\),

\[
 \min_{1\le\tau\le U}\xi(\tau)\ge1,
 \qquad
 \xi(1)={1\over U}+C_1\log U=O(\log m).
\tag{2.5}
\]

Along (2.4), equation (2.2) gives

\[
 {d\over d\tau}\bigl[\tau\Phi(\tau,\xi(\tau))\bigr]\le0
\tag{2.6}
\]

in the stopped-generator sense. Hence

\[
 \boxed{
 \mathscr M_t:=
 \tau(t)\Phi(\tau(t),\xi(\tau(t)))}
\tag{2.7}
\]

is one nonnegative stopped supermartingale controlling every fibre order.

The formerly apparent divergence

\[
 \exp[\Theta(1/z)]
\tag{2.8}
\]

comes from dropping the order-dependent negative term
\(-(\xi\partial_\xi\Phi+\Phi)/\tau\). Keeping that term changes the
characteristic input from \(1/z\) to \(\log(1/z)\).

## 3. Static initialization at logarithmic fugacity

At time zero, CPS iterated along the ordered child chain gives

\[
 H_j(1)
 \le {C_0\over m}\left({C_2\over m}\right)^j
 \mathfrak I,
\tag{3.1}
\]

where \(\mathfrak I\) is the marked owner/root incidence normalization.
The initial \(m^{-1}\) is the exact internal pair-profile mass; every
additional *ordered* child layer supplies another \(m^{-1}\). There is
no factorial on the right of (3.1): the factorial multiplicity belongs
to the number of histories represented by \(H_j\), while CPS is
iterated one history step at a time.

Using (2.5),

\[
\begin{aligned}
 \Phi(1,\xi(1))
 &\le {C_0\mathfrak I\over m}
   \sum_{j=0}^{r-2}
       {1\over j!}\left({C_2\xi(1)\over m}\right)^j\\
 &\le {C\mathfrak I\over m},
\end{aligned}
\tag{3.2}
\]

because \(\xi(1)=O(\log m)\). Full-edge termination makes the truncated
sum smaller; no unproved infinite tail is inserted.

This calculation remains valid at
\(z=m^{-1/2}(\log m)^{B_0}\), since only
\(\log(1/z)=O(\log m)\) enters.

## 4. Every unweakened profile stop is charged by the same score

Suppose PF\(_k\) first fails at the terminal profile \(S\), where
\(k=j+2\). Give this profile its static normalized incidence weight

\[
                         \omega(S)=q_k(S)=d_0(S)/D_0.
\tag{4.1}
\]

Thus \(D_0\omega(S)\) is its literal time-zero profile-star
multiplicity. After equality resolution, its \(j\) newly exposed
resources have \(j!\) ordered histories. At the violation, each cloned
history contributes at least \(A\omega(S)\) to the normalized fibre
mass (up to fixed degree-corridor constants, absorbed into \(A\)).
Therefore, since \(\xi(\tau)\ge1\), the total contribution of all
histories to \(\Phi\) is at least

\[
             j!\,A\omega(S){\xi(\tau)^j\over j!}
             \ge A\omega(S).
\tag{4.2}
\]

Stop the marked occurrence at its first profile violation. Terminal
stopping only decreases every other term. Doob's maximal inequality,
(2.7), and (3.2) therefore give

\[
 \boxed{
 \mathbb E[\text{profile-stopped marked incidence}]
 \le {C\over Am}\,\mathfrak I.}
\tag{4.3}
\]

All profile orders at the same threshold \(A\) are charged
simultaneously. There is no factor \(r\), \(2^r\), number of fibre
levels, or factorial loss. Omitting the ordered histories would indeed
make the coefficient \(1/j!\) unable to charge a high-order stop; their
inclusion is the exact reason the all-fibre EGF works.

## 5. The selected-incidence clock

It remains to convert (4.3) into the physical loss scale. Let \(N_t\)
be the active owner/root resource count and \(E_t\) the current number of
catalogue edges. Inside the degree corridor,

\[
                         rE_t=(1+o(1))N_t\Delta_t.
\tag{5.1}
\]

The edge clock rate is

\[
                         \nu_t={1\over r\Delta_t}.
\tag{5.2}
\]

Thus the rate of selected owner incidences is

\[
 r\nu_tE_t
 ={E_t\over\Delta_t}
 =(1+o(1)){N_t\over r}.
\tag{5.3}
\]

With \(N_t=(1+o(1))Wu_t\) and \(dt=-r\,du/u\),

\[
\begin{aligned}
 \int_0^T r\nu_tE_t\,dt
 &=(1+o(1)){W\over r}
       \int_0^T u_t\,dt\\
 &=(1+o(1))W\int_z^1du\\
 &=(1+o(1))W(1-z).
\end{aligned}
\tag{5.4}
\]

This proves (0.6). In particular, a uniform \(O(1/(Am))\) stopped
fraction costs

\[
                         O(W/(Am))=o(W).
\tag{5.5}
\]

The factors \(dt=-r\,du/u\) and \(N_t\asymp Wu\) cancel. Integrating a
bare stopped fraction against \(dt\) would incorrectly introduce
\(\log(1/z)\); integrating a child influence \(1/(mu)\) without the
order drift would incorrectly introduce \(z^{-1}\).

Compensation-resource stops use their actual incidence clock. Its total
mass is bounded by the same owner-deletion ledger and changes only the
constant in (5.4).

## 6. Exact boundary

Proved from Lemma 1.1 and CPS:

1. one all-order factorial EGF supermartingale;
2. logarithmic, rather than inverse-density, characteristic fugacity;
3. simultaneous control of PF\(_2\), PF\(_3\), and every higher fibre;
4. harmless termination at full simple edges; and
5. \(O(W/(Am))=o(W)\) total stopped incidence down to the square-root
   density (0.2).

The remaining audit condition is narrow:

\[
 \boxed{
 \text{verify Lemma 1.1/CPS for every equality-resolved
 column--row and compensation child orbit in the actual catalogue}.}
\tag{6.1}
\]

If that verification fails, the failure is a specific child orbit whose
conditional profile sum exceeds \(Cq_k(S)/m\). The all-order stochastic
boundary itself no longer requires a finite PFS hierarchy.

There is also an exact quantitative form of the alternative. Define
the order-
\(j\) conditional inflation

\[
 B_j=\sup_{S,e}{m\over q_{j+2}(S)}
       \sum_{w\in V(e)\setminus S}q_{j+3}(S\cup\{w\}),
 \qquad B=\max_j B_j.
\tag{6.2}
\]

If CPS with bounded \(C\) is unavailable, the same uniform-majorant
calculation uses \(C_1=(r/m)B\) and asks for the initial partition
function

\[
 \boxed{
 \mathcal Z(B)=
 {1\over\mathfrak I}
 \,\sum_{j=0}^{r-2}H_j(1)
 {\bigl((r/m)B\log U+U^{-1}\bigr)^j\over j!}.}
\tag{6.3}
\]

This uniform-majorant method closes when \(\mathcal Z(B)=o(A)\).
Failure of that inequality is the exact remaining partition-function
test; it is not by itself a trajectory counterexample, because replacing
the order-dependent \(B_j\)'s by their maximum can be lossy. In
particular, an aggregate post-\(H\) child
kernel of order one corresponds to \(B=\Theta(m)\), not \(B=O(1)\),
and must be tested at fugacity \(\Theta(m\log U)\). A single prescribed
consecutive spine does not by itself prove divergence, because the
factor \(1/j!\) remains; one needs the full ordered-profile mass in
(6.3).

This also pinpoints the omission in an order-blind scalar recurrence
which demands \(a_{j+1}\gtrsim T a_j\). Here the coefficients are

\[
 a_j(\tau)=\tau{\xi(\tau)^j\over j!},
 \qquad {a_{j+1}\over a_j}={\xi(\tau)\over j+1},
\tag{6.4}
\]

and the missing divisor \(j+1\) is supplied exactly by the fibre's
negative drift \(-(j+1)/\tau\). Dropping that drift recreates the false
\(\exp[\Theta(1/z)]\) or \(T^j\) boundary.
