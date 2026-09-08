# Anti-dihedral sliding rigidity and the Gaussian signed-coboundary obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom n m,
 \qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.

The exact anti-dihedral nested-Ucycle architecture is statewise impossible.
More precisely, suppose a cyclic singleton sliding component has distinct
rank-\(m\) windows and a rank-reversing coordinate anti-automorphism sends
those windows, in either cyclic orientation, to the adjacent rank-\(m+1\)
windows of the same or another component. Then the singleton word has period
\(n\), its component length is exactly \(n\), and it is an ordinary wreath.

Consequently every exact anti-dihedral sliding factor has exactly

\[
 \boxed{W/n=\operatorname {Cat}_m}
\]

wreath components. In particular:

1. the proposed one-component or sub-Catalan-component anti-dihedral nested
   Ucycle does not exist;
2. the singleton-padding ledger \(W+C(m+H)\) is
   \((3/2+o(1))W\), not \(W+o(W)\);
3. the typed erosion ledger \(W+2HC\) is still \(W+o(W)\) at Gaussian
   \(H\), but anti-dihedral symmetry then gives no new lower-profile
   freedom: it reduces exactly to low-collision rounding of an ordinary
   exact wreath factor;
4. reflection symmetry carries the lower signed-coboundary graph to a
   switching-isomorphic upper graph. It duplicates lower frustration rather
   than cancelling it; and
5. in the natural fixed-pair reflected fine-strip subclass, the signed graph
   can be a perfect coboundary while the one-sided Gaussian type-capacity
   deficit is still \(\Omega_A(W)\). Thus coboundary is necessary for
   integral synchronization but does not supply the missing marginal
   transport. More quantitatively, relative to any one fixed pair frame, a
   low-excess chronology must contain \(\Omega_A(W/\sqrt m)\) transitions
   which leave that frame.

If long approximate anti-dihedral components carry \(W-o(W)\) owners, they
must have \(\Omega(W/m)\) defective phases. Their naive Gaussian all-depth
exposure is \(\Omega_A(W)\), so the only surviving variant is a genuinely
mixed-frame approximate symmetry whose defect profiles form an
all-but-\(o(W)\) signed coboundary and which simultaneously escapes the
fixed-pair Gaussian cut.

No such construction is proved here.  Nor is an exact anti-invariant wreath
factor with low factorial excess excluded: that branch is simply the
original exact-wreath balancing problem with an additional symmetry
restriction.

## 1. Sliding components and anti-dihedral pairing

Let

\[
 s=(s_i)_{i\in\mathbb Z_\ell},
 \qquad
 t=(t_j)_{j\in\mathbb Z_\ell}
\]

be cyclic singleton words. Define

\[
 X_i^s=\{s_i,s_{i+1},\ldots,s_{i+m-1}\},
 \qquad
 Y_j^t=\{t_j,t_{j+1},\ldots,t_{j+m}\}.
\]

Assume that the \(X_i^s\) are distinct rank-\(m\) sets and that the
\(Y_j^t\) are distinct rank-\(m+1\) sets. The two words may describe the
same component or two different components of one factor.

Let \(R\) be a coordinate permutation and put

\[
 \theta(A)=[n]\setminus R(A).
\]

Assume that for some \(c\in\mathbb Z_\ell\) and
\(\epsilon\in\{+1,-1\}\),

\[
 \boxed{\theta(X_i^s)=Y_{\epsilon i+c}^t
        \quad(i\in\mathbb Z_\ell).}
 \tag{1.1}
\]

This is exactly the componentwise anti-dihedral relation used in the
nested-Ucycle proposal. Allowing \(s\ne t\) includes components paired by
\(\theta\).

The sliding transition is

\[
 X_{i+1}^s=X_i^s-\{s_i\}+\{s_{i+m}\}.
 \tag{1.2}
\]

Applying \(\theta\) reverses membership changes, so

\[
 \theta(X_{i+1}^s)
 =\theta(X_i^s)-\{R(s_{i+m})\}+\{R(s_i)\}.
 \tag{1.3}
\]

Because consecutive \(Y\)-windows are distinct and differ by one exchange,
the removed and inserted coordinates in their transition are unique.

## 2. Exact anti-dihedral sliding rigidity

### Theorem 2.1 (period-\(n\) rigidity)

Under the hypotheses of Section 1,

\[
 \boxed{s_{i+n}=s_i\quad\text{and}\quad t_{j+n}=t_j}
 \tag{2.1}
\]

for all cyclic indices, for both \(\epsilon=+1\) and
\(\epsilon=-1\).

#### Proof: rotational orientation

Let \(\epsilon=+1\). Comparing (1.3) with

\[
 Y_{i+c+1}^t
 =Y_{i+c}^t-\{t_{i+c}\}+\{t_{i+c+m+1}\}
\]

gives the exact coordinate identities

\[
 t_{i+c}=R(s_{i+m}),
 \qquad
 t_{i+c+m+1}=R(s_i).
 \tag{2.2}
\]

Use the first identity with index \(i+m+1\) and compare it with the
second identity at index \(i\). Their left sides are the same, so

\[
 R(s_{i+2m+1})=R(s_i).
\]

Since \(R\) is injective and \(n=2m+1\), this proves
\(s_{i+n}=s_i\). Equivalently, using the first identity at \(i-m\)
and the second at \(i\) proves \(t_{j+n}=t_j\).

#### Proof: reflected orientation

Let \(\epsilon=-1\) and put \(j=-i+c\). Comparing (1.3) with

\[
 Y_{j-1}^t
 =Y_j^t-\{t_{j+m}\}+\{t_{j-1}\}
\]

gives

\[
 t_{c-i+m}=R(s_{i+m}),
 \qquad
 t_{c-i-1}=R(s_i).
 \tag{2.3}
\]

Apply the second identity with index \(i-m-1\). Its left side is
\(t_{c-i+m}\), the left side of the first identity. Hence

\[
 R(s_{i+m})=R(s_{i-m-1}),
\]

and injectivity of \(R\) gives

\[
 s_{i+m}=s_{i-m-1}.
\]

The two indices differ by \(2m+1=n\), proving the first identity in
(2.1). The symmetric comparison proves it for \(t\). \(\square\)

### Corollary 2.2 (every component is one wreath)

Every component satisfying (1.1) has

\[
 \boxed{\ell=n,}
 \tag{2.4}
\]

and one period of each singleton word is a permutation of \([n]\).

#### Proof

Equation (2.1) gives \(X_{i+n}^s=X_i^s\). Since all \(\ell\) middle
windows on the component are distinct, the shift by \(n\) is zero modulo
\(\ell\), so \(\ell\mid n\).

A cyclic singleton component with injective rank-\(m\) windows and distinct
adjacent owners must have \(\ell>m\). Every proper divisor of the odd
integer \(n=2m+1\) is at most \(n/3<m+1\). Thus \(\ell=n\).

If one period contained a repeated coordinate, either two copies would lie
in one length-\(m\) window, or their cyclic separation would be \(m\) or
\(m+1\), in which case two adjacent length-\(m\) window sets would be
equal. Both contradict the hypotheses. Thus the period contains every
coordinate exactly once. \(\square\)

### Corollary 2.3 (factor component count)

If the components partition all \(W\) middle owners, then

\[
 \boxed{C=W/n=\operatorname {Cat}_m.}
 \tag{2.5}
\]

This remains true when \(\theta\) pairs two different components. The
proof of Theorem 2.1 was explicitly written with two words \(s,t\), so no
fixed-component hypothesis was used.

## 3. Consequences for the two literal ledgers and the factorial criterion

The singleton nested-Ucycle literalization opens every cyclic singleton
component by repeating its first \(m+H\) symbols. By (2.5), its length is

\[
 W+C(m+H)
 =W+\frac{m+H}{2m+1}W
 =\left(\frac32+o_A(1)\right)W.
 \tag{3.1}
\]

Therefore the claimed one-component and sub-Catalan-component singleton
endgames are impossible.

There is an important scope distinction. The typed erosion compiler for an
\(H\)-safe owner cycle costs only \(2H\) letters per component. Every
wreath is globally strongly \(H\)-safe when \(H+1<m\): transition supports
at cyclic edge distance below \(m\) are disjoint. Hence the same factor has
typed length

\[
 W+2HC
 =W+\frac{2H}{2m+1}W
 =W+O_A(W/\sqrt m)
 =W+o(W).
 \tag{3.2}
\]

Thus sliding rigidity does not rule out the wholesale typed-block route.
It proves instead that exact anti-dihedral symmetry contributes no fusion:
the surviving object is precisely an ordinary exact wreath factor.

Here is the exact sufficient criterion which remains after this collapse.
Let an owner-valid strongly \(H\)-safe middle-owner chronology have \(C\)
cyclic components.  At lower or upper depth \(q\), write \(z_q(T)\) for
the target loads, put

\[
 N_q=\binom{2m+1}{m-q},\qquad
 c_q=\left\lfloor{W\over N_q}\right\rfloor,
 \qquad W=c_qN_q+\rho_q,
\]

and define its balanced factorial excess by

\[
 \Delta_q
 :=\sum_T\binom{z_q(T)}2
   -\left(N_q\binom{c_q}2+c_q\rho_q\right).
 \tag{3.3}
\]

Since \(\sum_Tz_q(T)=W\), expansion gives the exact integral identity

\[
 \boxed{
 \Delta_q=\sum_T
 {\bigl(z_q(T)-c_q\bigr)
  \bigl(z_q(T)-c_q-1\bigr)\over2}.}
 \tag{3.4}
\]

Every summand is nonnegative.  A hole contributes
\(c_q(c_q+1)/2\), and therefore

\[
 h_q\le {2\Delta_q\over c_q(c_q+1)}.
 \tag{3.5}
\]

The cyclic erosion compiler has length \(W+2HC\).  Appending one literal
target block for every remaining hole gives the following fully integral
implication:

\[
 \boxed{
 C=o(W/H),\quad
 \sum_{q\le H}{\Delta_q^-+\Delta_q^+\over c_q}=o(W)
 \quad\Longrightarrow\quad
 L=W+o(W).}
 \tag{3.6}
\]

Indeed, \(c_q\ge1\), so (3.5) and the hypothesis make the aggregate hole
count \(o(W)\); all compiler blocks and appended hole blocks are literal
nonempty OR letters.  No fractional factor or cross-factor averaging is
used.

For such a factor let \(z_q^-(T)\) be its lower target histogram. Exact
trace duality gives only

\[
 z_q^+(\theta T)=z_q^-(T).
 \tag{3.7}
\]

Consequently the balanced factorial excesses satisfy

\[
 \boxed{\Delta_q^+=\Delta_q^-.}
 \tag{3.8}
\]

The symmetry orbit also cannot improve energy probabilistically.  If
\(g\) is a coordinate relabelling, cyclic phase shift, or reversal, then
the target histogram of \(gF\) is obtained from that of \(F\) by a target
permutation.  Therefore every \(\Delta_q^\pm\) is constant on the entire
dihedral-coordinate orbit of \(F\).  A law supported only on this orbit has
exactly the same statewise factorial excess as \(F\).

No upper bound on either side follows. Proving

\[
 \sum_{q\le A\sqrt m}
 \frac{\Delta_q^-+\Delta_q^+}{c_q}=o(W),
 \qquad
 c_q=\left\lfloor
 {W\over\binom{2m+1}{m-q}}
 \right\rfloor,
 \tag{3.9}
\]

contains no new balancing mechanism.  After the now-useless exact
anti-dihedral closure is dropped, it is exactly the original low-collision
exact-wreath/MWB gate; retaining the closure merely restricts the feasible
factor class.

## 4. Fine-strip signed coboundaries do not follow from reflection

Consider two support-matched owner factors, with packet variables
\(x_P\in\mathbb F_2\). Suppose a target \(T\) has exactly two selected
catalogue occurrences

\[
 (P,a),\qquad(Q,b),
\]

where occurrence \((P,a)\) is selected when \(x_P=a\). Its exact-one
constraint is

\[
 x_P\oplus x_Q=s_T,
 \qquad
 s_T=1\oplus a\oplus b.
 \tag{4.1}
\]

Let \(G^-\) be the signed graph of lower targets. Suppose the
anti-automorphism sends packets by \(P\mapsto\sigma P\) and occurrence
literals by

\[
 (P,a)\longmapsto(\sigma P,a\oplus\eta_P).
 \tag{4.2}
\]

Then the upper edge corresponding to \(T\) has sign

\[
 s_{\theta T}
 =s_T\oplus\eta_P\oplus\eta_Q.
 \tag{4.3}
\]

Thus the upper graph is switching-isomorphic to the lower graph. In
particular,

\[
 \boxed{\tau(G^+)=\tau(G^-),}
 \tag{4.4}
\]

where \(\tau\) is the signed frustration index.

Indeed, if

\[
 (Jx)_P=x_{\sigma P}\oplus\eta_P,
\]

then the number of upper violations under \(x\) is the number of lower
violations under \(Jx\). Therefore

\[
 F_-(x)+F_+(x)
 =F_-(x)+F_-(Jx)
 \ge2\tau(G^-).
 \tag{4.5}
\]

If the selected state is itself \(\theta\)-equivariant, so \(Jx=x\),
the lower and upper violated edges occur in exact pairs.

Reflection therefore never cancels lower frustration. At best it proves
one common coboundary and copies it to the other sign.

There is also a packet-orbit integrality obstruction which is independent
of signed-cycle frustration.  A \(\theta\)-equivariant choice must obey

\[
 x_{\sigma P}=x_P\oplus\eta_P.                    \tag{4.6}
\]

On every orbit of \(\sigma\), the xor of the \(\eta_P\)'s must therefore
vanish.  In particular, if \(\sigma P=P\) and \(\eta_P=1\), reflection
fixes the owner packet but swaps its two shores, and no equivariant
integral choice exists.  For an involution, a two-cycle \(\{P,\sigma P\}\)
requires \(\eta_P=\eta_{\sigma P}\).  This condition is necessary only
when the output itself is required to be reflection-equivariant; a common
non-equivariant choice is still governed by (4.5).

## 5. Factorial excess and signed frustration

Consider one mean-one residual port layer, after any deterministic quota
baseline has been removed.  On its regular two-occurrence target set, a
violated signed equation has residual selected load zero or two, while a
satisfied equation has load one. Write

\[
 V=\#\{\text{violated regular edges}\},
 \quad
 M=\#\{T:L(T)=0\},
 \quad
 D=\#\{T:L(T)=2\}.
\]

Then

\[
 V=M+D,
 \qquad
 \sum_T(L(T)-1)=D-M.
 \tag{5.1}
\]

At the mean-one port normalization, the factorial collision energy is
exactly

\[
 \sum_T\binom{L(T)}2=D.
 \tag{5.2}
\]

For a fixed assignment, let \(F(x)=V\) be its number of signed violations.
If the residual port-mass error \(|D-M|\) and the exceptional
non-two-occurrence target mass are \(o(W)\), equations (5.1)--(5.2) give

\[
 D={F(x)\over2}+o(W).                              \tag{5.3}
\]

Consequently, if those two error bounds hold uniformly for the admissible
packet choices, existence of a choice with residual factorial excess
\(o(W)\) is equivalent to

\[
 \boxed{
 \text{residual factorial excess }o(W)
 \quad\Longleftrightarrow\quad
 \tau(G)=o(W).}
 \tag{5.4}
\]

This is the exact interface between the wholesale low-collision criterion
and the fine-strip signed-coboundary gate.  It is a residual-layer theorem,
not an assertion that arbitrary floor baselines automatically decompose
into two-occurrence graphs.  It is conditional on the audited pair-balance,
exceptional-mass, and port-mass hypotheses; anti-dihedral symmetry supplies
none of them.

For fixed Gaussian \(H=A\sqrt m\), the fine-strip mass calculation remains
valid with any \(h\) satisfying

\[
 H\ll h=o(m).
\]

Indeed

\[
 2\sum_{q=1}^{H}N_q
 =\left(2\int_0^A e^{-x^2}\,dx+o(1)\right)W\sqrt m,
 \tag{5.5}
\]

and the selected port-mass error is at most

\[
 O_A(W/\sqrt m)+O_A(HW/h)=o(W).
 \tag{5.6}
\]

Thus at fixed Gaussian width the required coboundary accuracy is still
absolute \(o(W)\), not merely a vanishing fraction of the
\(\Theta_A(W\sqrt m)\) port universe.

## 6. A statewise odd-dimensional same-frame obstruction

Coboundary controls the integral choice between two shores. It does not
correct a one-sided source/target capacity deficit.

Pair the first \(2m\) coordinates and distinguish the coordinate
\(\infty\).  For a lower rank-\((m-q)\) target let \(\varepsilon\in\{0,1\}\)
record whether it contains \(\infty\), and let \(f\) be its number of full
pairs.  The exact target and compatible middle-source capacities are

\[
 T_{f,q}^{\varepsilon}
 ={m!\,2^{m-2f-q-\varepsilon}\over
 f!(f+q+\varepsilon)!(m-2f-q-\varepsilon)!},
 \tag{6.1}
\]

\[
 V_f^{\varepsilon}
 ={m!\,2^{m-2f-\varepsilon}\over
 f!(f+\varepsilon)!(m-2f-\varepsilon)!}.
 \tag{6.2}
\]

Here (6.1) is used for
\(0\le f\le\lfloor(m-q-\varepsilon)/2\rfloor\) and is zero outside that
range; (6.2) is used for
\(0\le f\le\lfloor(m-\varepsilon)/2\rfloor\) and is zero outside that
range.  All sums below are over \(f\ge0\) with this zero-extension.

They satisfy

\[
 \sum_{\varepsilon,f}T_{f,q}^{\varepsilon}=N_q,
 \qquad
 \sum_{\varepsilon,f}V_f^{\varepsilon}=W.          \tag{6.3}
\]

Every depth-\(q\) window confined to this pairing preserves
\((\varepsilon,f)\).  Since each middle owner starts one lower window, any
same-frame chronology obeys the exact statewise Hall cut

\[
 h_q^-\ge D_{m,q}^{\rm odd}
 :=\sum_{\varepsilon,f}
   (T_{f,q}^{\varepsilon}-V_f^{\varepsilon})_+.
 \tag{6.4}
\]

Let \(q/\sqrt m\to a>0\).  If a target is sampled with weight
\(T_{f,q}^{\varepsilon}/N_q\), then the exact ratio

\[
 R_{f,q}^{\varepsilon}
 ={V_f^{\varepsilon}\over T_{f,q}^{\varepsilon}}
 ={2^q(f+\varepsilon+1)^{\overline q}\over
   (m-2f-\varepsilon)_{\underline q}}
 \tag{6.5}
\]

converges in distribution to

\[
 R_a=e^{-a^2+2aZ},\qquad Z\sim N(0,1).              \tag{6.6}
\]

The function \(x\mapsto(1-x)_+\) is bounded and continuous, so weak
convergence suffices (equivalently one may use the exact local
central-limit expansion). As \(N_q/W\to e^{-a^2}\), (6.4) has the audited
limit

\[
 \boxed{
 {D_{m,q}^{\rm odd}\over W}\longrightarrow
 \delta(a)
 :=e^{-a^2}\Phi(a/2)-\Phi(-3a/2)>0.}               \tag{6.7}
\]

For completeness, positivity follows from

\[
 \delta(a)=e^{-a^2}\,
 \mathbb E(1-R_a)_+>0.                              \tag{6.8}
\]

Fix the requested outer constant \(A>0\), and choose

\[
 a_A={1\over2}\min\{A,\sqrt{\log2}\},
 \qquad q=\lfloor a_A\sqrt m\rfloor.               \tag{6.9}
\]

Then \(q\le H\) and \(c_q=1\) for all sufficiently large \(m\).  The
natural reflected pair may have \(\tau(G)=0\), but (3.4), (6.4), and
(6.7) give

\[
 \boxed{
 {\Delta_q^-\over c_q}\ge h_q^-
 \ge(\delta(a_A)+o(1))W.}                           \tag{6.10}
\]

If exact anti-dihedral trace duality is imposed, \(\Delta_q^+=\Delta_q^-\),
so the two-sided weighted sum is at least

\[
 \boxed{
 \sum_{r\le H}{\Delta_r^-+\Delta_r^+\over c_r}
 \ge(2\delta(a_A)+o(1))W.}                         \tag{6.11}
\]

This remains true under arbitrary dependence among shore choices, phases,
and direction orders as long as every selected transition stays in the
same unordered pairing frame.

There is a useful stability form.  Call a transition in-frame precisely
when it exchanges the two endpoints of one pair in the fixed matching; such
a transition preserves the full state \((\varepsilon,f)\).  Suppose exactly
\(s\) transition occurrences of an owner-exact strongly \(H\)-safe
chronology are not in-frame.  At most \(qs\) cyclic depth-\(q\) windows
contain one of those transitions.
Removing those exceptional windows leaves the type-capacity proof of (6.4)
unchanged; each exceptional window can repair at most one missing target.
Hence

\[
 \boxed{h_q^-\ge D_{m,q}^{\rm odd}-qs.}             \tag{6.12}
\]

Consequently \(\Delta_q^-=o(W)\) at (6.9) forces

\[
 \boxed{
 s\ge(\delta(a_A)+o(1)){W\over q}
   =\Omega_A(W/\sqrt m).}                           \tag{6.13}
\]

Thus exact signed coboundary plus reflection is not sufficient for the
Gaussian factorial-excess criterion.  The construction must transport
positive mass between fixed-pair types on the full soft-switch scale, by
genuinely mixed frames or cross-type seams.  The scope is exact: this is
not a no-go for an arbitrary mixed-frame approximate anti-dihedral routing.

## 7. Approximate anti-dihedral rigidity

Let a sliding component have length \(\ell>n\), and let

\[
 \mathcal B
 =\{i:\theta(X_i^s)\ne Y_{\epsilon i+c}^t\}
\]

be its defective phase set. Define

\[
 E=\{j:s_{j+n}\ne s_j\}.
\]

The comparisons in Theorem 2.1 use two adjacent anti-dihedral identities
at each of two phase locations.  More explicitly, for either orientation,
if the four phases

\[
 i,\quad i+1,\quad i+m+1,\quad i+m+2
\]

are outside \(\mathcal B\), the two exact transition comparisons give
\(s_{i+n}=s_i\).  Hence

\[
 |E|\le4|\mathcal B|.
 \tag{7.1}
\]

If some cyclic interval of \(m\) consecutive positions avoided \(E\),
then every symbol in that interval would agree with its shift by \(n\),
and consequently

\[
 X_{i+n}^s=X_i^s,
\]

contrary to distinct middle ownership. Therefore every cyclic
length-\(m\) interval meets \(E\). Double counting interval--point
incidences gives

\[
 m|E|\ge\ell.
\]

Together with (7.1),

\[
 \boxed{|\mathcal B|\ge{\ell\over4m}.}
 \tag{7.2}
\]

If the long components contain total owner mass \(W_{\rm long}\), summing
over precisely those components forces

\[
 |\mathcal B|\ge {W_{\rm long}\over4m}.
 \tag{7.3}
\]

A depth-\(q\) trace is declared naively exceptional when its phase interval
meets \(\mathcal B\).  The support-blind union bound through \(H\) is

\[
 O\left(|\mathcal B|\sum_{q=1}^{H}q\right)
 =O(|\mathcal B|H^2).
 \tag{7.4}
\]

There is also a matching lower bound at the level of phase--depth
incidences, not merely an inconclusive upper estimate.  In the proof of
(7.1), every \(i\in E\) forces a bad phase among four positions contained
in an interval of length at most \(m+3\).  Since every length-\(m\) interval
meets \(E\), every cyclic interval of length \(2m+3\) meets
\(\mathcal B\).  Thus the gaps \(g_j\) between consecutive bad phases are
at most \(2m+3\).  If \(N_q(\mathcal B)\) denotes the starts of length-\(q\)
phase intervals meeting \(\mathcal B\), then

\[
 |N_q(\mathcal B)|
 =\sum_j\min\{q,g_j\}
 \ge {q\over2m+3}\sum_jg_j
 ={q\ell\over2m+3}                                  \tag{7.5}
\]

for \(q\le H=o(m)\).  Consequently each long component has

\[
 \sum_{q=1}^{H}|N_q(\mathcal B)|
 \ge {\ell H(H+1)\over2(2m+3)}.                     \tag{7.6}
\]

At \(H=A\sqrt m\), this is
\((A^2/4+o_A(1))\ell\).  Hence if
\(W_{\rm long}=W-o(W)\), a repair which pays separately for every
defect-meeting phase--depth trace has \(\Omega_A(W)\) cost.  This does not
exclude vertical sharing of many depths at one literal endpoint.  It does
prove that support-blind trace quarantine is insufficient: the defect
profiles must themselves be bundled or satisfy an all-but-\(o(W)\)
signed-coboundary/collision cancellation.

## 8. Precise proved boundary

Proved:

1. exact anti-dihedral sliding components, in both orientations and even
   when paired, have length exactly \(n\);
2. the long anti-dihedral nested Ucycle and sub-Catalan-component factor
   do not exist;
3. exact anti-dihedral typed factors collapse to ordinary wreath factors,
   with identical lower and upper factorial profiles;
4. reflection sends the lower signed graph to a switching-isomorphic upper
   graph and cannot cancel frustration;
5. on a mean-one residual two-occurrence layer, under pair balance and
   \(o(W)\) exceptional mass, factorial excess and signed frustration are
   the same \(o(W)\) gate;
6. a natural fixed-pair reflected coboundary still has an
   \(\Omega_A(W)\) Gaussian type-capacity/factorial defect; and
7. every long approximate anti-dihedral fusion has \(\Omega(W/m)\)
   defective phases and \(\Omega_A(W)\) defect-meeting phase--depth
   incidences through the Gaussian window.

Not proved:

1. a mixed-frame approximate anti-dihedral rethreading;
2. an \(o(W)\)-frustration signed labelling for its defect packets;
3. the weighted factorial-excess bound (3.9); or
4. coefficient one.

The genuinely new surviving theorem is now strictly narrower than either
input alone: construct a mixed-frame owner-exact \(H\)-safe long
rethreading with \(o(W/H)\) hard components, whose unavoidable
\(\Omega(W/m)\) anti-dihedral defects are bundled at sublinear literal cost,
which separately has at least \(\Omega_A(W/\sqrt m)\) frame-changing soft
transitions transporting the fixed-pair Gaussian type mass, and whose
two-shore target labels form a signed coboundary off \(o(W)\) targets.
Exact anti-dihedral sliding symmetry cannot realize the long-component
part of this theorem.  The alternative surviving branch is to remain with
the \(W/n\) exact wreaths and solve (3.9) directly; this note neither proves
nor obstructs that branch outside the fixed-frame subclass.

## 9. Dependency and implication audit

The note uses, and has restated in the required odd-dimensional
normalization, exactly four inputs:

1. the owner-valid strongly \(H\)-safe erosion compiler from
   `MATH_ATTACK_PBBS_GAUSSIAN_ANNULUS_NONLINEAR_LOW_SWITCH_20260726.md`;
2. the exact trace duality and singleton period rigidity from
   `MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`;
3. the two-occurrence reflection/coboundary interface from
   `MATH_THEOREM_FINE_STRIP_REFLECTION_COBBOUNDARY_AND_PAIR_ORBIT_NO_GO_20260726.md`;
   and
4. the odd fixed-pair type census and lognormal Gaussian limit from
   `MATH_THEOREM_FIXED_PAIR_CUBE_MWB_QUOTA_ENERGY_20260726.md`.

The decisive period comparison was independently checked in both cyclic
orientations and with two distinct paired components.  The fixed-pair cut
was independently checked after replacing the even-strip shorthand by the
exact \((\varepsilon,f)\) odd census.  No implication in this note crosses
from a fractional mixture to an integral factor: (3.6), (6.10), (6.12),
and the rigidity theorem are all statewise.
